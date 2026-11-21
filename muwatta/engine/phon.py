# -*- coding: utf-8 -*-
"""Fully vowelled Arabic  ->  phoneme stream, independent of any target script.

Every target language reuses this one analysis; only the renderer (engine/scripts/*.py) differs.
Generalised from books/ar/_wip/*/translit.py (the ভাষার দরজা Arabic book), with the same reading rules:

  * the article: sun letters assimilate (aš-šams), moon letters keep l (al-qamar); hyphen after it
  * hamzat al-waṣl: dropped after a vowel (fi l-bayti), helping vowel i after a consonant/tanwin,
    pronounced ʔa/ʔi/ʔu after a pause
  * pause (waqf) before . ، ؛ : ؟ ! » and at the end: no final short vowel, -an -> ā, ة -> h, -iyy -> ī
  * long vowels from ا ى و ي, diphthongs ay aw, shadda = gemination, tanwin = n
  * known spellings with an unwritten long ā (هذا، ذلك، لكن، الله، الرحمن، إله، أولئك…) and the
    unvowelled ﷺ formula (صلى الله عليه وسلم) are normalised first.

Token types in a word:  ("C", code, geminate)  ("V", v)  ("-",)   v in a i u A I U (capital = long)
Consonant codes (ASCII, one per Arabic phoneme):
  ' b t T(th) j H(ḥ) x(kh) d D(dh) r z s S(sh) c(ṣ) Q(ḍ) X(ṭ) Z(ẓ) E(ʿ) g(gh) f q k l m n h w y
"""
import re
import unicodedata

FATHA, DAMMA, KASRA, SUKUN, SHADDA = "َ", "ُ", "ِ", "ْ", "ّ"
TAN_F, TAN_D, TAN_K, DAGGER = "ً", "ٌ", "ٍ", "ٰ"
MARKS = {FATHA, DAMMA, KASRA, SUKUN, SHADDA, TAN_F, TAN_D, TAN_K, DAGGER}
TANWIN = {TAN_F, TAN_D, TAN_K}

CONS = {
    "ء": "'", "أ": "'", "إ": "'", "ؤ": "'", "ئ": "'",
    "ب": "b", "ت": "t", "ث": "T", "ج": "j", "ح": "H", "خ": "x", "د": "d", "ذ": "D", "ر": "r", "ز": "z",
    "س": "s", "ش": "S", "ص": "c", "ض": "Q", "ط": "X", "ظ": "Z", "ع": "E", "غ": "g", "ف": "f", "ق": "q",
    "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w", "ي": "y", "ة": "t",
}
SUN = set("تثدذرزسشصضطظلن")
PAUSE_PUNCT = set(".،؛:؟!»…")
PUNCT = set(".،؛:؟!«»…{}()[]-\"*/0123456789")

# ------------------------------------------------------------------ normalisation
_SPECIAL = [
    # unvowelled eulogies in the sunnah.com text
    ("صلى الله عليه وسلم", "صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ"),
    ("رضى الله عنه", "رَضِيَ اللَّهُ عَنْهُ"),
    ("رضي الله عنه", "رَضِيَ اللَّهُ عَنْهُ"),
    ("ـ", ""),                       # tatweel
    ("ٱ", "ا"),                       # alif wasla -> bare alif (handled as waṣl)
]

def _skel(w):
    return "".join(c for c in w if c not in MARKS)

# words whose long ā is not written (no dagger alif in this text): insert a dagger after the letter
_IMPLICIT_A = {   # skeleton -> index (0-based) of the letter that carries the unwritten ā
    "هذا": 0, "هذه": 0, "هذان": 0, "هذين": 0, "ذلك": 0, "ذلكم": 0, "ذلكما": 0, "كذلك": 1, "فذلك": 1,
    "وذلك": 1, "لذلك": 1, "بذلك": 1, "لكن": 0, "ولكن": 1, "فلكن": 1, "هؤلاء": 0, "وهؤلاء": 1,
    "الرحمن": 4, "إله": 1, "الإله": 3,
}

def _insert_dagger(word, letter_index):
    """Put a dagger alif after the letter number `letter_index` (0-based, letters only) and its marks."""
    out, k, i = [], -1, 0
    chars = list(word)
    while i < len(chars):
        out.append(chars[i])
        if chars[i] not in MARKS:
            k += 1
            if k == letter_index:
                i += 1
                while i < len(chars) and chars[i] in MARKS:
                    out.append(chars[i]); i += 1
                out.append(DAGGER)
                continue
        i += 1
    return "".join(out)

def normalise_word(w):
    sk = _skel(w)
    if sk in _IMPLICIT_A and DAGGER not in w:
        w = _insert_dagger(w, _IMPLICIT_A[sk])
    # Allah / Allahumma: the ā after the doubled lam is not written in this text
    if DAGGER not in w and re.fullmatch("[وفبتك]?(ا|ل)?للهم?", sk):
        w = re.sub("(ل(?:\u0651\u064E|\u064E\u0651))(ه)", lambda mm: mm.group(1) + DAGGER + mm.group(2), w, count=1)
    # ى with its own vowel/shadda is the consonant y (sunnah.com writes الْمَذْىُ , السَّعْىُ)
    w = re.sub("ى(?=[\u064B-\u0651])", "ي", w)
    # alif carrying the vowel of the previous letter (lam-alif mark order: لاَ, also any "Cاَ"): move it
    w = re.sub("([^ً-ْٰا])ا([ًَ])", lambda mm: mm.group(1) + mm.group(2) + "ا", w)
    return w

def normalise(text):
    t = unicodedata.normalize("NFC", text).replace("‏", "")
    for a, b in _SPECIAL:
        t = t.replace(a, b)
    return t

# ------------------------------------------------------------------ word parsing
class Warn(Exception):
    pass

def _units(word):
    out = []
    for ch in word:
        if ch in MARKS:
            if not out:
                raise Warn("mark without letter in %r" % word)
            out[-1][1].add(ch)
        else:
            out.append([ch, set()])
    return out

def _vowel(m):
    if FATHA in m or TAN_F in m: return "a"
    if KASRA in m or TAN_K in m: return "i"
    if DAMMA in m or TAN_D in m: return "u"
    return None

_EXCEPT = {   # skeleton -> phoneme spelling (rare irregular orthography)
    "أولئك": "'ulA'ika", "أولي": "'ulI", "أولو": "'ulU", "أولات": "'ulAt",
    "عمرو": None,   # handled by the generic silent-waw rule
}

def parse_word(word):
    """-> (tokens, info).  info: waṣl (None | 'article' | 'a'/'i'/'u'), article ('sun'/'moon'), allah flag."""
    word = normalise_word(word)
    u = _units(word)
    n = len(u)
    toks, info = [], {"wasl": None, "article": None}
    i = 0

    def article_at(k):
        """u[k] is a bare alif followed by lam: return 'sun'/'moon'/None."""
        if k + 1 >= n or u[k + 1][0] != "ل":
            return None
        lm = u[k + 1][1]
        if SUKUN in lm:
            return "moon"
        if not lm and k + 2 < n:
            if SHADDA in u[k + 2][1]:
                return "sun"
            return "moon"        # e.g. الأَنْصَارِيُّ (lam unmarked before hamza)
        return None

    # word-initial bare alif = hamzat al-waṣl (article or verb/noun)
    if n and u[0][0] == "ا" and not (u[0][1] - {SUKUN}):
        art = article_at(0)
        if art:
            info["wasl"], info["article"] = "article", art
            toks.append(("ART", art))
            i = 2
        else:
            v = _vowel(u[0][1])
            if not v:
                # third letter's damma -> u (اُدْخُلْ), otherwise i
                v = "u" if n > 2 and DAMMA in u[2][1] else "i"
            info["wasl"] = v
            toks.append(("WASL", v))
            i = 1
    # li-l / wa-l / fa-l / bi-l + article written without alif:  لِلصَّلاَةِ , لِلَّهِ
    while i < n:
        ch, m = u[i]
        nxt = u[i + 1] if i + 1 < n else None
        prev_v = toks[-1][1] if toks and toks[-1][0] == "V" else None

        if ch == "ا":
            # article after a one-letter prefix: وَالْ فَالْ بِالْ كَالْ
            if i > 0 and prev_v in ("a", "i", "u") and not (m - {SUKUN}):
                art = article_at(i)
                if art:
                    toks.append(("ART", art)); i += 2; continue
                if nxt and SUKUN in nxt[1]:          # waṣl inside: وَاسْتَيْقَظَ
                    i += 1; continue
            if prev_v == "a":
                toks[-1] = ("V", "A"); i += 1; continue
            if toks and toks[-1][0] == "N":          # alif after tanwin fatḥa
                i += 1; continue
            if prev_v in ("U", "i", "u", "I", "A"):  # قَالُوا ، مِائَة ، silent
                i += 1; continue
            if m & {FATHA, TAN_F, KASRA, DAMMA}:     # الاِسْتِطَابَة: al-istiṭābah
                toks.append(("V", _vowel(m))); i += 1; continue
            if i == n - 1 and i > 0 and u[i - 1][0] == "و":   # فَاسْعَوْا: silent alif after wāw
                i += 1; continue
            raise Warn("unexpected alif in %r" % word)
        if ch == "آ":
            toks.append(("C", "'", False)); toks.append(("V", "A")); i += 1; continue
        if ch == "ى":
            if prev_v in ("a", "A") or (toks and toks[-1][0] == "N"):
                if prev_v == "a": toks[-1] = ("V", "A")
                i += 1; continue
            if prev_v == "i":                        # عَلَىَّ-type spellings, rare
                toks[-1] = ("V", "I"); i += 1; continue
            if DAGGER in m:
                toks.append(("V", "A")); i += 1; continue
            raise Warn("bad alif maqsura in %r" % word)
        if ch == "ل" and i == 0 and KASRA in m and nxt and nxt[0] == "ل":
            # لِلْ / لِلـّ : li + article
            toks += [("C", "l", False), ("V", "i")]
            if SUKUN in nxt[1]:
                toks.append(("ART", "moon")); i += 2; continue
            if SHADDA in nxt[1] or (not nxt[1] and i + 2 < n and SHADDA in u[i + 2][1]):
                toks.append(("ART", "sun"))
                i += 1 if SHADDA in nxt[1] else 2
                if SHADDA in nxt[1]:
                    # the lam itself is the sun letter (لِلَّهِ): keep it as the assimilated consonant
                    u[i] = ["ل", u[i][1]]
                continue
        if ch in ("و", "ي") and not (m - {SUKUN}):
            # long vowel or diphthong
            if ch == "ي" and prev_v == "i": toks[-1] = ("V", "I"); i += 1; continue
            if ch == "و" and prev_v == "u": toks[-1] = ("V", "U"); i += 1; continue
            if ch == "ي" and prev_v == "a": toks[-1] = ("V", "a"); toks.append(("C", "y", False)); i += 1; continue
            if ch == "و" and prev_v == "a": toks[-1] = ("V", "a"); toks.append(("C", "w", False)); i += 1; continue
            if ch == "و" and i == n - 1 and prev_v in ("i", "u", None) and not m:
                i += 1; continue                      # silent final waw: عَمْرٌو
            if ch == "و" and i == n - 1 and toks and toks[-1][0] == "N":
                i += 1; continue
        if ch not in CONS:
            raise Warn("unknown char %r in %r" % (ch, word))
        gem = SHADDA in m
        toks.append(("C", CONS[ch], gem))
        if ch == "ة":
            toks[-1] = ("C", "TM", False)            # tāʾ marbūṭa: t, or h at a pause
        v = _vowel(m)
        if DAGGER in m:
            toks.append(("V", "A"))
        elif v:
            toks.append(("V", v))
        if m & TANWIN:
            toks.append(("N",))
        i += 1
    return toks, info


def apply_pause(toks):
    t = list(toks)
    if t and t[-1] == ("N",):
        t.pop()
        if t and t[-1] == ("V", "a"):
            if len(t) >= 2 and t[-2][0] == "C" and t[-2][1] == "TM":
                t.pop(); t[-1] = ("C", "TMh", False); return t
            t[-1] = ("V", "A"); return t
        if t and t[-1][0] == "V":
            t.pop()
    elif t and t[-1][0] == "V" and t[-1][1] in "aiu":
        t.pop()
    if t and t[-1][0] == "C" and t[-1][1] == "TM":
        t[-1] = ("C", "TMh", False)
    if len(t) >= 2 and t[-1] == ("C", "y", True) and t[-2] == ("V", "i"):
        t.pop(); t[-1] = ("V", "I")
    if len(t) >= 2 and t[-1] == ("C", "w", True) and t[-2] == ("V", "u"):
        t.pop(); t[-1] = ("V", "U")
    return t


# ------------------------------------------------------------------ sentence level
TOKEN_RE = re.compile(r"(\s+|[.،؛:؟!«»…{}()\[\]\-\"*/0-9])")

def _finish(toks):
    """Resolve ART / WASL / N / TM into plain C and V tokens (+ '-' after the article)."""
    out = []
    i = 0
    while i < len(toks):
        tk = toks[i]
        if tk[0] == "ART":
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if (tk[1] == "sun" and nxt and nxt[0] == "C" and nxt[1] == "l" and i + 3 < len(toks)
                    and toks[i + 2] == ("V", "A") and toks[i + 3][0] == "C" and toks[i + 3][1] == "h"):
                out.append(("C", "l", True))       # Allah: allāh, rasūlu llāh (no hyphen)
                i += 2; continue
            if tk[1] == "sun" and nxt and nxt[0] == "C":
                out.append(("C", nxt[1], False))
                out.append(("-",))
                out.append(("C", nxt[1], False))
                i += 2; continue
            out.append(("C", "l", False)); out.append(("-",))
        elif tk[0] == "N":
            out.append(("C", "n", False))
        elif tk[0] == "C" and tk[1] == "TM":
            out.append(("C", "t", False))
        elif tk[0] == "C" and tk[1] == "TMh":
            out.append(("C", "h", False))
        else:
            out.append(tk)
        i += 1
    return out


def analyse(text, pause_at_commas=True):
    """Arabic text -> list of items: ("W", tokens) words, ("S",) space, ("P", ch) punctuation.

    Words are already joined across waṣl (the joined word carries the previous word's tokens), so a
    renderer can render each ("W", tokens) on its own.
    """
    text = normalise(text)
    raw = [p for p in TOKEN_RE.split(text) if p]
    items = []
    for p in raw:
        if p.isspace():
            items.append(["S"])
        elif p in PUNCT:
            items.append(["P", p])
        else:
            items.append(["W", p])
    pause_set = set(PAUSE_PUNCT) | {"}"}
    if not pause_at_commas:
        pause_set.discard("،")
    # decide pause per word
    for k, it in enumerate(items):
        if it[0] != "W":
            continue
        j = k + 1
        while j < len(items) and items[j][0] == "S":
            j += 1
        nxt = items[j] if j < len(items) else None
        it.append(nxt is None or (nxt[0] == "P" and nxt[1] in pause_set))
    out = []
    warnings = []
    prev_word = None          # index in `out` of the previous word if directly connected (no punctuation)
    for it in items:
        if it[0] == "S":
            out.append(("S",)); continue
        if it[0] == "P":
            out.append(("P", it[1])); prev_word = None; continue
        try:
            toks, info = parse_word(it[1])
        except Warn as e:
            warnings.append(str(e))
            out.append(("RAW", it[1])); prev_word = None; continue
        if it[2]:
            toks = apply_pause(toks)
        w = info["wasl"]
        if w:
            body = toks[1:]
            if prev_word is not None:
                ptoks = out[prev_word][1]
                last = ptoks[-1] if ptoks else None
                if last and last[0] == "V":
                    # shorten a final long vowel before the cluster: fī l-bayti -> fi l-bayti
                    if last[1] in "AIU":
                        ptoks[-1] = ("V", last[1].lower())
                else:
                    # consonant (tanwin or sukun) before waṣl: helping vowel i
                    ptoks.append(("V", "i"))
                if info["article"]:
                    body = [("ART", info["article"])] + body
                toks = body
                joined = True
            else:
                v = "a" if info["article"] else w
                toks = [("C", "'", False), ("V", v)] + ([("ART", info["article"])] if info["article"] else []) + body
                joined = False
        else:
            joined = False
            # word starting with a vowelless consonant (بْنُ after a vowel): fine if connected, else prothetic i
            if toks and toks[0][0] == "C" and (len(toks) < 2 or toks[1][0] != "V") and prev_word is None:
                toks = [("C", "'", False), ("V", "i")] + toks
        fin = _finish(toks)
        if w and prev_word is not None:
            # glue to the previous word, as the phrase is pronounced as one unit
            out.append(("W", fin, "joined"))
        else:
            out.append(("W", fin))
        prev_word = len(out) - 1
        if it[2]:
            prev_word = None
    # finish the tokens of words that were mutated (helping vowels) — they are plain already
    return out, warnings
