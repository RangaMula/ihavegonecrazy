# -*- coding: utf-8 -*-
"""Fully vowelled Arabic -> (Bangla pronunciation, simplified ALA-LC) following books/ar/STYLE.md §3-§4."""
import re, sys

FATHA, DAMMA, KASRA, SUKUN, SHADDA = "َ", "ُ", "ِ", "ْ", "ّ"
TAN_F, TAN_D, TAN_K, DAGGER = "ً", "ٌ", "ٍ", "ٰ"
MARKS = {FATHA, DAMMA, KASRA, SUKUN, SHADDA, TAN_F, TAN_D, TAN_K, DAGGER}
NUK = "়"
YA_BN = "য়"  # য়

# letter -> (en, bn)
CONS = {
    "ب": ("b", "ব"), "ت": ("t", "ত"), "ث": ("th", "থ" + NUK), "ج": ("j", "জ"), "ح": ("ḥ", "হ" + NUK),
    "خ": ("kh", "খ" + NUK), "د": ("d", "দ"), "ذ": ("dh", "দ" + NUK), "ر": ("r", "র"), "ز": ("z", "জ" + NUK),
    "س": ("s", "স"), "ش": ("sh", "শ"), "ص": ("ṣ", "স" + NUK), "ض": ("ḍ", "ড"), "ط": ("ṭ", "ট"),
    "ظ": ("ẓ", "য"), "ع": ("ʿ", "ʿ"), "غ": ("gh", "গ" + NUK), "ف": ("f", "ফ" + NUK), "ق": ("q", "ক" + NUK),
    "ك": ("k", "ক"), "ل": ("l", "ল"), "م": ("m", "ম"), "ن": ("n", "ন"), "ه": ("h", "হ"),
    "و": ("w", "W"), "ي": ("y", "Y"), "ء": ("ʾ", "ʾ"), "أ": ("ʾ", "ʾ"), "إ": ("ʾ", "ʾ"), "ؤ": ("ʾ", "ʾ"),
    "ئ": ("ʾ", "ʾ"), "ة": ("t", "ত"),
}
SUN = set("تثدذرزسشصضطظلن")
VSIGN = {"a": "া", "i": "ি", "u": "ু", "A": "াː", "I": "ীː", "U": "ূː", "ay": "াই", "aw": "াও"}
VIND = {"a": "আ", "i": "ই", "u": "উ", "A": "আː", "I": "ঈː", "U": "ঊː", "ay": "আই", "aw": "আও"}
VEN = {"a": "a", "i": "i", "u": "u", "A": "ā", "I": "ī", "U": "ū", "ay": "ay", "aw": "aw"}
SHORT = {"A": "a", "I": "i", "U": "u"}
PLAIN_DOUBLE = {"র", "ʿ", "ʾ"}  # doubled without a conjunct (also any nukta letter)
PUNCT_BN = {"/": "/", "؟": "?", "،": ",", "؛": ";", ".": "।", "!": "!", ":": ":", "…": "…", "«": "«", "»": "»", "—": "—", "-": "-", "(": "(", ")": ")"}
PUNCT_EN = {"/": "/", "؟": "?", "،": ",", "؛": ";", ".": ".", "!": "!", ":": ":", "…": "…", "«": "«", "»": "»", "—": "—", "-": "-", "(": "(", ")": ")"}
PAUSE_PUNCT = set(".؟!:…؛/")

class Warn(Exception):
    pass

def units(word):
    """Split into [letter, set(marks)]"""
    out = []
    for ch in word:
        if ch in MARKS:
            if not out:
                raise Warn("mark without letter in %r" % word)
            out[-1][1].add(ch)
        elif ch == "ـ":
            continue
        else:
            out.append([ch, set()])
    return out

def vowel_of(m):
    if FATHA in m or TAN_F in m: return "a"
    if KASRA in m or TAN_K in m: return "i"
    if DAMMA in m or TAN_D in m: return "u"
    return None

def parse(word):
    """-> dict(tokens, wasla, article) ; tokens: ('C', key, doubled) ('V', v) ('N',) [tanwin n] ('H',) [ta marbuta at pause marker]"""
    u = units(word)
    toks = []
    info = {"wasla": None, "article": None, "allah": False}
    i = 0
    n = len(u)
    # word-initial bare alif = hamzat al-wasl
    def is_article_at(k):
        # u[k] is bare alif, u[k+1] is lam
        if k + 1 >= n or u[k + 1][0] != "ل": return None
        lm = u[k + 1][1]
        if SUKUN in lm: return "moon"
        if not lm and k + 2 < n and SHADDA in u[k + 2][1]: return "sun"
        return None
    if n > 2 and u[0][0] == "ل" and KASRA in u[0][1] and u[1][0] == "ل" and not (n > 2 and DAGGER in u[1][1]) and (SUKUN in u[1][1] or (not u[1][1] and SHADDA in u[2][1] and DAGGER not in u[2][1])):
        toks.append(("C", "ل", False)); toks.append(("V", "i"))
        toks.append(("ART", "moon" if SUKUN in u[1][1] else "sun"))
        i = 2
    elif n > 2 and u[0][0] == "ل" and KASRA in u[0][1] and u[1][0] == "ل" and SHADDA in u[1][1] and DAGGER not in u[1][1]:
        toks.append(("C", "ل", False)); toks.append(("V", "i"))
        toks.append(("ART", "sun"))
        i = 1
    elif n > 3 and u[0][0] == "ا" and u[1][0] == "ل" and KASRA in u[1][1] and u[2][0] == "ا":
        info["wasla"] = "article"; info["article"] = "moon"
        toks.append(("ART", "moon")); toks.append(("V", "i"))
        i = 3
    elif n and u[0][0] == "ا":
        art = is_article_at(0)
        if art:
            info["wasla"] = "article"
            info["article"] = art
            if art == "sun" and u[2][0] == "ل" and DAGGER in u[2][1] and n > 3 and u[3][0] == "ه":
                info["allah"] = True
            info["art_index"] = len(toks)
            i = 2 if art == "moon" else 2  # skip alif + lam; for sun the lam is absorbed
            toks.append(("ART", art))
        else:
            info["wasla"] = vowel_of(u[0][1]) or ("a" if n > 1 and u[1][0] == "ل" and SHADDA in u[1][1] else "i")
            toks.append(("WASLA",))
            i = 1
    while i < n:
        ch, m = u[i]
        nxt = u[i + 1] if i + 1 < n else None
        if (i == 1 and u[0][0] in "وف" and ch == "ل" and KASRA in m and nxt and nxt[0] == "ل" and DAGGER not in nxt[1]
                and not (i + 2 < n and DAGGER in u[i + 2][1])):
            if SUKUN in nxt[1]:
                toks += [("C", "ل", False), ("V", "i"), ("ART", "moon")]; i += 2; continue
            if not nxt[1] and i + 2 < n and SHADDA in u[i + 2][1]:
                toks += [("C", "ل", False), ("V", "i"), ("ART", "sun")]; i += 2; continue
            if SHADDA in nxt[1]:
                toks += [("C", "ل", False), ("V", "i"), ("ART", "sun")]; i += 1; continue
        if ch == "ا":
            # article after a one-letter prefix (wa-, fa-, bi-, ka-)
            art = is_article_at(i) if i > 0 else None
            if art and toks and toks[-1][0] == "V":
                toks.append(("ART", art))
                if art == "sun" and u[i + 2][0] == "ل" and DAGGER in u[i + 2][1] and i + 3 < n and u[i + 3][0] == "ه":
                    info["allah"] = True
                i += 2
                continue
            # wasla after prefix: next letter has sukun
            if i > 0 and nxt and SUKUN in nxt[1] and toks and toks[-1][0] == "V" and toks[-1][1] in "aiu":
                i += 1
                continue
            # long a
            if toks and toks[-1][0] == "V" and toks[-1][1] == "a":
                toks[-1] = ("V", "A"); i += 1; continue
            # silent alif after tanwin fatha or after -uu
            if toks and toks[-1][0] == "N":
                i += 1; continue
            if toks and toks[-1] == ("V", "U") and i == n - 1:
                i += 1; continue
            raise Warn("unexpected alif in %r" % word)
        if ch == "آ":
            if toks: toks.append(("C", "ء", False))
            toks.append(("V", "A")); i += 1; continue
        if ch == "ى":
            if toks and toks[-1][0] == "V" and toks[-1][1] == "a":
                toks[-1] = ("V", "A")
            elif toks and toks[-1][0] == "N":
                pass
            elif toks and toks[-1] == ("V", "A"):
                pass
            else:
                raise Warn("bad alif maqsura in %r" % word)
            i += 1; continue
        if ch in ("و", "ي") and not (m - {SHADDA}) and SHADDA not in m:
            # bare w/y: long vowel or diphthong
            if toks and toks[-1][0] == "V":
                pv = toks[-1][1]
                if ch == "ي" and pv == "i": toks[-1] = ("V", "I"); i += 1; continue
                if ch == "و" and pv == "u": toks[-1] = ("V", "U"); i += 1; continue
        if ch in ("و", "ي") and m == {SUKUN} and toks and toks[-1][0] == "V":
            pv = toks[-1][1]
            if ch == "ي" and pv == "i": toks[-1] = ("V", "I"); i += 1; continue
            if ch == "و" and pv == "u": toks[-1] = ("V", "U"); i += 1; continue
            if ch == "ي" and pv == "a": toks[-1] = ("V", "ay"); i += 1; continue
            if ch == "و" and pv == "a": toks[-1] = ("V", "aw"); i += 1; continue
        if ch not in CONS:
            raise Warn("unknown char %r in %r" % (ch, word))
        doubled = SHADDA in m
        if ch == "ة":
            toks.append(("C", "ة", False))
        elif ch in ("ي",) and doubled and toks and toks[-1] == ("V", "a"):
            toks[-1] = ("V", "ay"); toks.append(("C", "ي", False))
        elif ch == "و" and doubled and toks and toks[-1] == ("V", "a"):
            toks[-1] = ("V", "aw"); toks.append(("C", "و", False))
        else:
            toks.append(("C", ch, doubled))
        if DAGGER in m:
            v = vowel_of(m)
            toks.append(("V", "A"))
        else:
            v = vowel_of(m)
            if v: toks.append(("V", v))
        if m & {TAN_F, TAN_D, TAN_K}:
            toks.append(("N",))
        if ch not in ("ة",) and not v and DAGGER not in m and SUKUN not in m :
            # no vowel and no sukun: allowed only at very end (pause) -- warn otherwise
            if i != n - 1:
                raise Warn("letter without haraka: %r in %r" % (ch, word))
        i += 1
    return toks, info

def apply_pause(toks):
    t = list(toks)
    if not t: return t
    # tanwin
    if t[-1] == ("N",):
        t.pop()
        v = t[-1]
        if v == ("V", "a"):
            # -an: after ة -> ah ; else ā
            if len(t) >= 2 and t[-2][0] == "C" and t[-2][1] == "ة":
                t.pop(); t[-1] = ("C", "ة_h", False); return t
            t[-1] = ("V", "A"); return t
        t.pop()
    elif t[-1][0] == "V" and t[-1][1] in "aiu":
        t.pop()
    # ta marbuta
    if t and t[-1][0] == "C" and t[-1][1] == "ة":
        t[-1] = ("C", "ة_h", False)
    # -iyy -> ī
    if len(t) >= 2 and t[-1] == ("C", "ي", True) and t[-2] == ("V", "i"):
        t.pop(); t[-1] = ("V", "I")
    return t

def render(toks, word_initial=True):
    """-> (en, bn)"""
    en, bn = [], []
    prev = None  # previous token
    k = 0
    for idx, tk in enumerate(toks):
        typ = tk[0]
        nxt = toks[idx + 1] if idx + 1 < len(toks) else None
        if typ == "C":
            key, dbl = tk[1], tk[2]
            if key == "ة_h":
                en.append("h"); bn.append("হ"); prev = tk; continue
            e, b = CONS[key]
            # word-initial hamza: silent
            if key in ("أ", "إ", "ء") and idx == 0 and word_initial:
                prev = ("HZ0",); continue
            has_v = nxt is not None and nxt[0] == "V"
            en.append(e * 2 if dbl else e)
            if b == "W":
                pv = prev[1] if prev and prev[0] == "V" else None
                if dbl:
                    bn.append("ওয়" if has_v else "ও")
                elif has_v:
                    bn.append(YA_BN if pv == "aw" else "ওয়")
                else:
                    bn.append("ও")
            elif b == "Y":
                pv = prev[1] if prev and prev[0] == "V" else None
                if dbl and pv == "i":
                    bn.append(YA_BN + "্য" if has_v else "ই")
                elif has_v:
                    bn.append("ইয়" if prev is None or prev[0] == "HZ0" else YA_BN)
                elif pv == "ay":
                    bn.append("")
                else:
                    bn.append("ই")
            else:
                if dbl:
                    if NUK in b or b in PLAIN_DOUBLE or has_v is False and False:
                        bn.append(b + b)
                    else:
                        bn.append(b + "্" + b)
                else:
                    bn.append(b)
            prev = tk
        elif typ == "V":
            v = tk[1]
            en.append(VEN[v])
            after_cons = prev is not None and prev[0] == "C" and CONS.get(prev[1], ("", ""))[1] not in ("ʿ", "ʾ")
            if prev is not None and prev[0] == "C" and prev[1] in ("و", "ي"):
                after_cons = True
            if after_cons:
                bn.append(VSIGN[v])
            else:
                bn.append(VIND[v])
            prev = tk
        elif typ == "N":
            en.append("n"); bn.append("ন"); prev = ("C", "ن", False)
    return "".join(en), "".join(bn)

TOKEN_RE = re.compile(r"(\s+|[؟،؛.!:…«»—()/]|___)")

WARNINGS = []

def transliterate(text, nopause=False):
    parts = [p for p in TOKEN_RE.split(text) if p != ""]
    # identify words
    items = []
    for p in parts:
        if p.isspace(): items.append(("SP", p))
        elif p == "___": items.append(("BL", p))
        elif p in PUNCT_EN: items.append(("P", p))
        else: items.append(("W", p))
    # pause flags
    widx = [i for i, it in enumerate(items) if it[0] == "W"]
    pause = set()
    for i in widx:
        j = i + 1
        while j < len(items) and (items[j][0] == "SP" or (items[j][0] == "P" and items[j][1] in "»)")):
            j += 1
        if j >= len(items) or (items[j][0] == "P" and items[j][1] in PAUSE_PUNCT):
            pause.add(i)
    out_en, out_bn = [], []
    last_kind = None  # 'V' if previous word output ended in a vowel (and no punctuation between)
    for i, it in enumerate(items):
        kind, s = it
        if kind == "SP":
            out_en.append(" "); out_bn.append(" "); continue
        if kind == "BL":
            out_en.append("___"); out_bn.append("___"); last_kind = None; continue
        if kind == "P":
            out_en.append(PUNCT_EN[s]); out_bn.append(PUNCT_BN[s]); last_kind = None; continue
        toks, info = parse(s)
        if i in pause and not nopause:
            toks = apply_pause(toks)
        w = info["wasla"]
        connected = last_kind == "V"
        if w and last_kind == "N":
            # tanwin before hamzat al-wasl takes a helping kasra: -un/-in/-an + i
            j = len(out_en) - 1
            while j >= 0 and out_en[j] == " ": j -= 1
            out_en[j] += "i"; out_bn[j] += "ি"
            connected = True
        elif w and last_kind == "C":
            WARNINGS.append("wasla after consonant-final word: %r in %r" % (s, text))
        body = toks
        pre_en = pre_bn = ""
        join = False
        if w:
            body = toks[1:]
            if w == "article":
                art = info["article"]
                first = body[0]
                letter = first[1]
                e_l, b_l = ("l", "ল") if art == "moon" else CONS[letter]
                if info["allah"]:
                    # allāh: no hyphen
                    if connected:
                        join = True; pre_en, pre_bn = "", ""
                        # body: l(doubled)+ā+h... render whole, it starts with doubled l
                    else:
                        pre_en, pre_bn = "a", "আ"
                else:
                    if connected:
                        join = True
                        pre_en, pre_bn = e_l + "-", b_l + "-"
                    else:
                        pre_en, pre_bn = "a" + e_l + "-", "আ" + b_l + "-"
                    if art == "sun":
                        body = [("C", letter, False)] + body[1:]
            else:
                if connected:
                    join = True
                else:
                    body = [("V", w)] + body
        else:
            if toks and toks[0][0] == "ART":
                pass
        # handle article after prefix inside the word
        if any(t[0] == "ART" for t in body):
            k = [t[0] for t in body].index("ART")
            art = body[k][1]
            head, tail = body[:k], body[k + 1:]
            letter = tail[0][1]
            if info["allah"]:
                e1, b1 = render(head, word_initial=not join)
                e2, b2 = render(tail, word_initial=False)
                e, b = e1 + e2, b1 + b2
            else:
                e_l, b_l = ("l", "ল") if art == "moon" else CONS[letter]
                if art == "sun":
                    tail = [("C", letter, False)] + tail[1:]
                e1, b1 = render(head, word_initial=not join)
                e2, b2 = render(tail, word_initial=True)
                e, b = e1 + e_l + "-" + e2, b1 + b_l + "-" + b2
        else:
            if info.get("allah"):
                e, b = render(body, word_initial=False)
            elif w == "article":
                e, b = render(body, word_initial=True)
            else:
                e, b = render(body, word_initial=not join)
        e, b = pre_en + e, pre_bn + b
        if join:
            # shorten previous final long vowel, drop the space before
            while out_en and out_en[-1] == " ": out_en.pop(); out_bn.pop()
            pe, pb = out_en[-1], out_bn[-1]
            for L, S in (("ā", "a"), ("ī", "i"), ("ū", "u")):
                if pe.endswith(L): pe = pe[:-1] + S
            for L, S in (("াː", "া"), ("ীː", "ি"), ("ূː", "ু"), ("আː", "আ"), ("ঈː", "ই"), ("ঊː", "উ")):
                if pb.endswith(L): pb = pb[:-len(L)] + S
            out_en[-1], out_bn[-1] = pe + e, pb + b
        else:
            out_en.append(e); out_bn.append(b)
        last = toks[-1] if toks else None
        last_kind = "V" if (last and last[0] == "V") else ("N" if last == ("N",) else "C")
        if i + 1 < len(items) and False:
            pass
    en = "".join(out_en)
    bn = "".join(out_bn)
    bn = bn.replace("য়", YA_BN)
    return bn, en

def check_wasla_after_consonant(text):
    """Return list of problems: a wasla word following a consonant-final word."""
    probs = []
    words = [w for w in re.split(r"[\s]+", text) if w]
    for a, b in zip(words, words[1:]):
        if re.search(r"[؟،؛.!:…«»]$", a): continue
        if b.startswith("ا") and not b.startswith("ا" + "َ") :
            if a.endswith(SUKUN) or re.search("[ًٌٍ]ا?$", a):
                probs.append((a, b))
    return probs

if __name__ == "__main__":
    tests = ["كِتَاب", "ثَلَاثَة", "حَلِيب", "خُبْز", "ذَهَب", "صَبَاح", "ضَيْف", "طَالِب", "ظُهْر", "عَيْن", "غَزَال", "قَلْب",
             "مَاء", "سَأَلَ", "وَلَد", "يَد", "مُدَرِّس", "أُمّ", "الشَّمْس", "النُّور", "فِي الْبَيْتِ", "مَدْرَسَة",
             "مَدْرَسَةُ الْبَنَاتِ", "كَتَبْتُ", "يَوْم", "بَيْت", "شُكْرًا", "كَيْفَ حَالُكَ؟", "بِسْمِ اللّٰهِ", "إِنْ شَاءَ اللّٰهُ.",
             "الْحَمْدُ لِلّٰهِ.", "وَالْبَيْتُ كَبِيرٌ.", "السَّلَامُ عَلَيْكُمْ.", "وَعَلَيْكُمُ السَّلَامُ.", "اِسْمِي رَفِيقٌ.",
             "مَا اسْمُكَ؟", "سَيَّارَةٌ جَدِيدَةٌ.", "اللُّغَةُ الْعَرَبِيَّةُ.", "هُوَ عَرَبِيٌّ.", "هٰذَا كِتَابٌ.", "ذَهَبُوا إِلَى الْمَسْجِدِ.",
             "الْقُرْآنُ", "أَوَّلُ يَوْمٍ", "قُوَّةٌ.", "عَلَى الطَّاوِلَةِ.", "مُسْتَشْفًى.", "أَنَا مِنْ بَنْغْلَادِيشَ."]
    for t in tests:
        print(t, "=", *transliterate(t))
