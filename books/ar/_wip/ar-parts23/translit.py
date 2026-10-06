# -*- coding: utf-8 -*-
"""Vowelled Arabic -> Bangla pronunciation (STYLE §3) and simplified ALA-LC (STYLE §4), with the pause rule."""
import re

FATHA, DAMMA, KASRA, SUKUN, SHADDA = "َ", "ُ", "ِ", "ْ", "ّ"
FATHATAN, DAMMATAN, KASRATAN, DAGGER, MADDA = "ً", "ٌ", "ٍ", "ٰ", "ٓ"
MARKS = {FATHA, DAMMA, KASRA, SUKUN, SHADDA, FATHATAN, DAMMATAN, KASRATAN, DAGGER, MADDA}
TATWEEL = "ـ"
N = "়"  # nukta

CONS = {
    "ب": ("ব", "b"), "ت": ("ত", "t"), "ث": ("থ" + N, "th"), "ج": ("জ", "j"), "ح": ("হ" + N, "ḥ"),
    "خ": ("খ" + N, "kh"), "د": ("দ", "d"), "ذ": ("দ" + N, "dh"), "ر": ("র", "r"), "ز": ("জ" + N, "z"),
    "س": ("স", "s"), "ش": ("শ", "sh"), "ص": ("স" + N, "ṣ"), "ض": ("ড", "ḍ"), "ط": ("ট", "ṭ"),
    "ظ": ("য", "ẓ"), "غ": ("গ" + N, "gh"), "ف": ("ফ" + N, "f"), "ق": ("ক" + N, "q"), "ك": ("ক", "k"),
    "ل": ("ল", "l"), "م": ("ম", "m"), "ن": ("ন", "n"), "ه": ("হ", "h"),
}
HAMZAS = set("ءأإؤئ")
SUN = set("تثدذرزسشصضطظلن")
# vowel -> (sign after consonant, independent, roman)
V = {"a": ("া", "আ", "a"), "i": ("ি", "ই", "i"), "u": ("ু", "উ", "u"),
     "ā": ("াː", "আː", "ā"), "ī": ("ীː", "ঈː", "ī"), "ū": ("ূː", "ঊː", "ū"),
     "ay": ("াই", "আই", "ay"), "aw": ("াও", "আও", "aw")}
SHORTEN = {"ā": "a", "ī": "i", "ū": "u"}
YA = "য" + N


def letters(word):
    """[(base, set(marks))]"""
    out = []
    for ch in word:
        if ch == TATWEEL:
            continue
        if ch in MARKS and out:
            out[-1][1].add(ch)
        elif ch in MARKS:
            continue
        else:
            out.append([ch, set()])
    # precomposed madda
    res = []
    for b, m in out:
        if b == "آ":
            res.append(["أ", {FATHA}]); res.append(["ا", set()])
        else:
            res.append([b, m])
    return res


def short_of(m):
    if FATHA in m or FATHATAN in m: return "a"
    if KASRA in m or KASRATAN in m: return "i"
    if DAMMA in m or DAMMATAN in m: return "u"
    return None


def segments(word, pause):
    """Turn one word into a list of segments: ('C', key, double) consonant, ('V', v) vowel, ('N',) tanwin n.
    key: arabic consonant letter, or 'ʿ', 'ʾ', 'w', 'y', 't' (ta marbuta), 'h' (ta marbuta at pause)."""
    L = letters(word)
    segs = []
    i = 0
    n = len(L)
    while i < n:
        b, m = L[i]
        nxt = L[i + 1] if i + 1 < n else None
        last = (i == n - 1)
        prevv = segs[-1][1] if segs and segs[-1][0] == "V" else None
        # long vowels / diphthongs / silent letters
        if b == "ا" and not (m - {DAGGER}):
            if i == 0:
                # hamzat al-wasl with no mark: default i
                segs.append(("V", "i")); i += 1; continue
            if prevv == "a":
                segs[-1] = ("V", "ā"); i += 1; continue
            if segs and segs[-1][0] == "N":   # alif after fathatan
                if pause and last:
                    segs.pop(); segs[-1] = ("V", "ā") if segs[-1][0] == "V" else segs[-1]
                i += 1; continue
            if prevv == "ū":   # -ūā verb alif
                i += 1; continue
            i += 1; continue
        if b == "ا" and short_of(m) and i == 0:   # اِ اُ at start (wasl written with vowel)
            segs.append(("V", short_of(m))); i += 1; continue
        if b == "ى":
            if prevv == "a" or prevv is None:
                if segs and segs[-1][0] == "V": segs[-1] = ("V", "ā")
                else: segs.append(("V", "ā"))
            elif segs and segs[-1][0] == "N":
                pass
            i += 1; continue
        if b == "ي" and not short_of(m) and SHADDA not in m and prevv in ("i", "a"):
            if prevv == "i": segs[-1] = ("V", "ī")
            else: segs[-1] = ("V", "ay")
            i += 1; continue
        if b == "و" and not short_of(m) and SHADDA not in m and prevv in ("u", "a"):
            if prevv == "u": segs[-1] = ("V", "ū")
            else: segs[-1] = ("V", "aw")
            i += 1; continue
        # consonants
        if b in HAMZAS:
            key = "ʾ"
        elif b == "ع":
            key = "ʿ"
        elif b == "و":
            key = "w"
        elif b == "ي":
            key = "y"
        elif b == "ة":
            key = "t"
        elif b in CONS:
            key = b
        else:
            i += 1; continue
        dbl = SHADDA in m
        sv = short_of(m)
        # final -iyy at pause -> ī
        if key == "y" and dbl and last and pause and prevv == "i":
            segs[-1] = ("V", "ī"); i += 1; continue
        if key == "t":
            if pause and last or not sv:
                segs.append(("C", "h", False)); i += 1; continue
        if b == "أ" or b == "إ":
            if not sv:
                sv = "i" if b == "إ" else ("a" if FATHA in m else sv)
        segs.append(("C", key, dbl))
        if DAGGER in m:
            segs.append(("V", "ā"))
        elif sv:
            tan = (FATHATAN in m) or (DAMMATAN in m) or (KASRATAN in m)
            if last and pause and not (FATHATAN in m and nxt and nxt[0] == "ا"):
                if FATHATAN in m and key == "h":
                    pass
                # drop final short vowel / tanwin
                pass
            else:
                segs.append(("V", sv))
                if tan:
                    segs.append(("N",))
        i += 1
    # pause: alif after fathatan handled above (segs end with V ā)
    return segs


def render(segs, initial=True):
    """segments -> (bangla, roman). initial: the first vowel of the chunk is word-initial."""
    bn, en = [], []
    prev = None  # 'start', 'C', 'V', 'mark' (ʿ ʾ)
    state = "start" if initial else "V"
    k = 0
    while k < len(segs):
        s = segs[k]
        if s[0] == "V":
            v = s[1]
            if state in ("start", "mark", "V"):
                bn.append(V[v][1])
            else:
                bn.append(V[v][0])
            en.append(V[v][2]); state = "V"
        elif s[0] == "N":
            bn.append("ন"); en.append("n"); state = "C"
        else:
            key, dbl = s[1], s[2]
            nextv = segs[k + 1][1] if k + 1 < len(segs) and segs[k + 1][0] == "V" else None
            if key in ("ʿ", "ʾ"):
                if key == "ʾ" and state == "start":
                    pass  # initial hamza not written
                else:
                    bn.append(key * (2 if dbl else 1)); en.append(key * (2 if dbl else 1))
                state = "start" if (key == "ʾ" and state == "start") else "mark"
            elif key in ("w", "y"):
                r = key
                if dbl:
                    # closing half
                    pv = segs[k - 1][1] if k and segs[k - 1][0] == "V" else None
                    if key == "y":
                        if pv == "a": bn.append("ই")
                        elif pv == "i": bn.append(YA + "্")
                        else: bn.append("ই")
                    else:
                        bn.append("ও")
                    en.append(r)
                    after_close = True
                else:
                    after_close = False
                if nextv is None:
                    if not dbl:
                        bn.append("ও" if key == "w" else "ই"); en.append(r)
                    state = "C"
                else:
                    if key == "y":
                        if after_close:
                            bn.append(YA)
                        elif state == "start" or state == "C" or state == "mark":
                            bn.append("ই" + YA)
                        else:
                            bn.append(YA)
                    else:
                        if after_close:
                            bn.append(YA if nextv in ("a", "ā") else "")
                        elif nextv in ("a", "ā", "ay", "aw"):
                            bn.append("ও" + YA)
                        else:
                            bn.append("")
                    en.append(r)
                    # vowel after w/y consonant
                    v = nextv
                    if key == "w" and not (nextv in ("a", "ā", "ay", "aw")) and not after_close:
                        bn.append(V[v][1])  # উ, ঊː, ই ...
                        if v in ("i", "ī"):
                            bn[-1] = "উ" + V[v][1]
                    elif key == "w" and after_close and nextv not in ("a", "ā"):
                        bn.append(V[v][1])
                    else:
                        bn.append(V[v][0])
                    en.append(V[v][2]); state = "V"; k += 2; continue
            elif key == "h" and s[1] == "h" and False:
                pass
            else:
                if key == "t":
                    c_bn, c_en = "ত", "t"
                elif key == "h":
                    c_bn, c_en = "হ", "h"
                else:
                    c_bn, c_en = CONS[key]
                if dbl:
                    if key == "ر":
                        bn.append(c_bn + c_bn)
                    else:
                        bn.append(c_bn + "্" + c_bn)
                    en.append(c_en + c_en)
                else:
                    bn.append(c_bn); en.append(c_en)
                state = "C"
        k += 1
    return "".join(bn), "".join(en)


def strip_punct(w):
    return w.strip("؟،.!:؛?,«»\"'()")


ART = re.compile("^[اٱ][َ]?ل")


def split_article(L):
    """Detect (prefix_letters, article, sun) in letter list. Returns (prefix_len, art_start, rest_start, sun) or None."""
    def is_alif(x):
        return x[0] in ("ا", "ٱ") and not (x[1] - {FATHA})
    # bare article
    for p in (0, 1):
        if len(L) > p + 2 and is_alif(L[p]) and L[p + 1][0] == "ل":
            if p == 1 and not (L[0][0] in "وفبكل" and short_of(L[0][1])):
                continue
            lam = L[p + 1]
            nxt = L[p + 2]
            if SHADDA in nxt[1] and nxt[0] in SUN and SUKUN not in lam[1] and not short_of(lam[1]):
                return (p, p + 2, True)
            if SUKUN in lam[1] or (not lam[1] and nxt[0] not in SUN) or (not lam[1] and nxt[0] in SUN and SHADDA not in nxt[1]):
                if short_of(lam[1]):
                    continue
                return (p, p + 2, False)
    # lil- : لِلْ / لِل + shadda
    if len(L) > 3 and L[0][0] == "ل" and KASRA in L[0][1] and L[1][0] == "ل":
        nxt = L[2]
        if SUKUN in L[1][1]:
            return (1, 2, False, "lil")
        if not L[1][1] and SHADDA in nxt[1] and nxt[0] in SUN:
            return (1, 2, True, "lil")
    return None


def word_plain(w):
    return "".join(c for c in w if c not in MARKS and c != TATWEEL)


def pron(text, pause=True):
    """Return (bn_pron, en_pron) for a vowelled Arabic item."""
    b, e = _pron(text, pause)
    b = b.replace(YA + "্" + YA, YA + "্য")
    return b, e


def _pron(text, pause=True):
    raw = text.replace("ـ", "")
    toks = raw.split()
    # pause points: before punctuation and at the end
    words = []
    for t in toks:
        pz = bool(re.search("[؟،.!:؛]$", t))
        w = strip_punct(t)
        if w:
            words.append([w, pz])
    if words:
        words[-1][1] = pause
    out_bn, out_en = [], []
    for wi, (w, pz) in enumerate(words):
        plain = word_plain(w)
        prev_open = bool(out_bn) and not words[wi - 1][1] and _ends_vowel(out_en[-1])
        if (bool(out_bn) and not words[wi - 1][1] and out_en[-1].endswith("n")
                and (_lastmarks(words[wi - 1][0]) & {FATHATAN, DAMMATAN, KASRATAN})
                and word_plain(w)[:2] in ("ال", "ٱل")):
            out_bn[-1] += "ি"; out_en[-1] += "i"; prev_open = True
        # Allah
        if plain in ("الله", "اللهم"):
            tail_bn, tail_en = ("ল্লাːহ", "llāh") if plain == "الله" else ("ল্লাːহুম্মা", "llāhumma")
            if not pz and plain == "الله":
                sv = short_of(letters(w)[-1][1])
                if sv:
                    tail_bn, tail_en = "ল্লাːহ" + V[sv][0], "llāh" + sv
            if prev_open:
                out_bn[-1] = _shorten_bn(out_bn[-1]) + tail_bn; out_en[-1] = _shorten_en(out_en[-1]) + tail_en
            else:
                out_bn.append("আ" + tail_bn); out_en.append("a" + tail_en)
            continue
        if plain in ("لله",):
            sv = short_of(letters(w)[-1][1])
            tb, te = "লিল্লাːহ", "lillāh"
            if sv and not pz:
                tb, te = tb + V[sv][0], te + sv
            out_bn.append(tb); out_en.append(te); continue
        L = letters(w)
        art = split_article(L)
        if art:
            p, rs, sun = art[0], art[1], art[2]
            lil = len(art) > 3
            rest = "".join(b + "".join(sorted(m)) for b, m in L[rs:])
            rsegs = segments(rest, pz)
            if sun:
                # drop doubling on first consonant of rest; doubling shown across hyphen
                c = rsegs[0]
                rsegs[0] = ("C", c[1], False)
            rb, re_ = render(rsegs, initial=True)
            if sun:
                cb, ce = CONS[rsegs[0][1]]
                link_bn, link_en = cb + "-", ce + "-"
            else:
                link_bn, link_en = "ল-", "l-"
            if lil:
                out_bn.append("লি" + link_bn + rb); out_en.append("li" + link_en + re_); continue
            if p == 1:
                pb, pe = render(segments("".join(b + "".join(sorted(m)) for b, m in L[:1]), False), initial=True)
                out_bn.append(pb + link_bn + rb); out_en.append(pe + link_en + re_); continue
            if prev_open:
                out_bn[-1] = _shorten_bn(out_bn[-1]) + link_bn + rb
                out_en[-1] = _shorten_en(out_en[-1]) + link_en + re_
            else:
                out_bn.append("আ" + link_bn + rb); out_en.append("a" + link_en + re_)
            continue
        # hamzat al-wasl in a non-article word after an open syllable
        if L[0][0] in ("ا", "ٱ") and not (L[0][1] - {FATHA, KASRA, DAMMA}) and prev_open and len(L) > 1 and SUKUN in L[1][1]:
            rest = "".join(b + "".join(sorted(m)) for b, m in L[1:])
            rb, re_ = render(segments(rest, pz), initial=False)
            out_bn[-1] = _shorten_bn(out_bn[-1]) + rb; out_en[-1] = _shorten_en(out_en[-1]) + re_
            continue
        b_, e_ = render(segments(w, pz), initial=True)
        out_bn.append(b_); out_en.append(e_)
    return " ".join(out_bn), " ".join(out_en)


def _lastmarks(w):
    L = letters(w)
    if len(L) > 1 and L[-1][0] in ("ا", "ى") and not L[-1][1]:
        return L[-2][1]
    return L[-1][1]


def _ends_vowel(en):
    return bool(en) and en[-1] in "aiuāīū"


def _shorten_en(s):
    if s and s[-1] in SHORTEN:
        return s[:-1] + SHORTEN[s[-1]]
    return s


def _shorten_bn(s):
    for lng, sh in (("াː", "া"), ("ীː", "ি"), ("ূː", "ু"), ("আː", "আ"), ("ঈː", "ই"), ("ঊː", "উ")):
        if s.endswith(lng):
            return s[:-len(lng)] + sh
    return s


if __name__ == "__main__":
    tests = ["سَأَلَ", "بَاب", "تَمْر", "ثَلَاثَة", "جَمِيل", "حَلِيب", "خُبْز", "دَار", "ذَهَب", "رَجُل", "زَيْت", "سَمَك", "شَمْس",
             "صَبَاح", "ضَيْف", "طَالِب", "ظُهْر", "عَيْن", "غَزَال", "فِيل", "قَلْب", "كَلْب", "لَيْل", "مَاء", "نُور", "هُنَا",
             "وَلَد", "يَد", "قَلَم", "مِن", "قُلْ", "بَيْت", "يَوْم", "كَتَبْتُ", "مُدَرِّس", "أُمّ", "الشَّمْس", "النُّور",
             "فِي الْبَيْتِ", "مَدْرَسَة", "مَدْرَسَةُ الْبَنَاتِ", "كِتَابٌ", "كَيْفَ حَالُكَ؟", "شُكْرًا", "سَيَّارَة", "عَرَبِيَّة",
             "عَرَبِيّ", "أَوَّل", "قُوَّة", "هٰذَا كِتَابٌ.", "الْأَحَد", "رَبِيعُ الْأَوَّل", "جُمَادَى الْأُولَى", "ذُو الْحِجَّة",
             "بِسْمِ اللّٰهِ", "الْحَمْدُ لِلّٰهِ", "إِنْ شَاءَ اللّٰهُ", "مَا اسْمُكَ؟", "قُرْآن", "رَأْس", "بِئْر", "لُؤْلُؤ", "شَاطِئ",
             "سُؤَال", "وُجُوه", "حَيَوَان", "مُعَلِّم", "بِالْقَلَمِ", "وَالسَّلَامُ", "لِلْبَيْتِ", "اِسْم", "اِثْنَان", "أَهْلًا وَسَهْلًا",
             "مَرْحَبًا", "كَتَبُوا", "عَلَى", "مُسْتَشْفَى", "السَّلَامُ عَلَيْكُمْ", "وَعَلَيْكُمُ السَّلَامُ", "مِينَاء", "شَاي", "زَاي", "وَاو",
             "يَاء", "مَرْيَم", "مُوَظَّف", "أُسْبُوع", "آبَار", "مَسْؤُول", "ذٰلِكَ", "لٰكِنَّ", "سَبْع", "بَعْد", "تِسْعَةَ عَشَرَ"]
    for t in tests:
        print(t, "|", *pron(t), sep=" ")
