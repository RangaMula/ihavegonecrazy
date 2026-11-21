# -*- coding: utf-8 -*-
"""Renderers: phoneme stream (engine/phon.py) -> pronunciation in a target script.

    from scripts import pronounce
    pronounce("قَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم", "bn")

Implemented schemes (see standard/TRANSLITERATION.md for the tables and the reasons):
  latn   simplified ALA-LC (scholarly Latin; the base for every Latin-script language)
  bn     Bengali - exactly the notation of books/ar/STYLE.md §3 (nukta letters, ː for long vowels, ʿ ʾ)
  hi     Hindi / Devanagari - Hindi-Urdu nukta conventions, halant on vowelless consonants
  ja     Japanese katakana - Japanese Islamic-literature conventions (アッラー, ムハンマド), ー for long vowels
New scripts: add a renderer function and register it in SCHEMES.
"""
from phon import analyse

# ---------------------------------------------------------------- helpers
def units(toks):
    """Group a word's tokens into units: ("CV", code, gem, v) | ("C", code, gem) | ("V", v) | ("-",)."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t[0] == "C":
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if nxt and nxt[0] == "V":
                out.append(("CV", t[1], t[2], nxt[1])); i += 2; continue
            out.append(("C", t[1], t[2]))
        elif t[0] == "V":
            out.append(("V", t[1]))
        else:
            out.append(("-",))
        i += 1
    return out


QUOTES = {"latn": ("“", "”"), "ja": ("「", "」")}

def walk(items, render_word, punct, space=" ", raw=lambda w: w, quotes=("“", "”")):
    out = []
    q_open = False
    for it in items:
        if it[0] == "P" and it[1] == '"':
            if not q_open:
                out.append(quotes[0])
            else:
                while out and out[-1] == space:
                    out.pop()
                out.append(quotes[1])
            q_open = not q_open
            continue
        if out and out[-1] == space and len(out) > 1 and out[-2] == quotes[0] and q_open:
            out.pop()
        if it[0] == "S":
            out.append(space)
        elif it[0] == "P":
            out.append(punct.get(it[1], it[1]))
        elif it[0] == "RAW":
            out.append(raw(it[1]))
        else:
            w = render_word(it[1])
            if len(it) > 2 and it[2] == "joined":
                while out and out[-1] == space:
                    out.pop()
            out.append(w)
    s = "".join(out)
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip()


PUNCT_LATN = {"،": ",", "؛": ";", "؟": "?", "{": "“", "}": "”", "«": "“", "»": "”", "*": ""}

# ---------------------------------------------------------------- Latin, simplified ALA-LC
LATN = {"'": "ʾ", "b": "b", "t": "t", "T": "th", "j": "j", "H": "ḥ", "x": "kh", "d": "d", "D": "dh", "r": "r",
        "z": "z", "s": "s", "S": "sh", "c": "ṣ", "Q": "ḍ", "X": "ṭ", "Z": "ẓ", "E": "ʿ", "g": "gh", "f": "f",
        "q": "q", "k": "k", "l": "l", "m": "m", "n": "n", "h": "h", "w": "w", "y": "y"}
LATN_V = {"a": "a", "i": "i", "u": "u", "A": "ā", "I": "ī", "U": "ū"}

def latn_word(toks):
    s = []
    for k, t in enumerate(toks):
        if t[0] == "C":
            if t[1] == "'" and (k == 0 or toks[k - 1] == ("-",)):
                continue                      # no hamza sign at the start of a word or after al-
            c = LATN[t[1]]
            s.append(c * 2 if t[2] else c)
        elif t[0] == "V":
            s.append(LATN_V[t[1]])
        else:
            s.append("-")
    return "".join(s)

# ---------------------------------------------------------------- Bengali (books/ar/STYLE.md)
NUK = "়"
BN = {"b": "ব", "t": "ত", "T": "থ" + NUK, "j": "জ", "H": "হ" + NUK, "x": "খ" + NUK, "d": "দ", "D": "দ" + NUK,
      "r": "র", "z": "জ" + NUK, "s": "স", "S": "শ", "c": "স" + NUK, "Q": "ড", "X": "ট", "Z": "য",
      "g": "গ" + NUK, "f": "ফ" + NUK, "q": "ক" + NUK, "k": "ক", "l": "ল", "m": "ম", "n": "ন", "h": "হ"}
BN_SIGN = {"a": "া", "i": "ি", "u": "ু", "A": "াː", "I": "ীː", "U": "ূː"}
BN_IND = {"a": "আ", "i": "ই", "u": "উ", "A": "আː", "I": "ঈː", "U": "ঊː"}
YA = "য" + NUK  # য়
HAS = "্"

def bn_word(toks):
    U = units(toks)
    s = []
    prev = None   # previous unit
    for k, u in enumerate(U):
        if u[0] == "-":
            s.append("-"); prev = u; continue
        if u[0] == "V":
            s.append(BN_IND[u[1]]); prev = u; continue
        code, gem = u[1], u[2]
        v = u[3] if u[0] == "CV" else None
        prev_v = prev[3] if prev and prev[0] == "CV" else (prev[1] if prev and prev[0] == "V" else None)
        if code in ("'", "E"):
            mark = "ʾ" if code == "'" else "ʿ"
            if code == "'" and (k == 0 or U[k - 1] == ("-",)):
                mark = ""
            s.append(mark * (2 if gem else 1))
            if v:
                s.append(BN_IND[v])
            prev = u; continue
        if code == "y":
            if v is None:                       # coda: diphthong ay or plain i
                s.append("ই"); prev = u; continue
            if gem:
                s.append("ই" + YA + HAS + "য" if prev_v != "i" else YA + HAS + "য")
                s.append(BN_SIGN[v]); prev = u; continue
            s.append("ইয়" if prev is None else YA)   # word-initial ইয়, elsewhere য়
            s.append(BN_SIGN[v]); prev = u; continue
        if code == "w":
            if v is None:
                s.append("ও"); prev = u; continue
            s.append("ওয়")                     # also geminate ww (as in the ভাষার দরজা Arabic book)
            s.append(BN_SIGN[v]); prev = u; continue
        b = BN[code]
        if gem:
            s.append(b + b if (NUK in b or code == "r") else b + HAS + b)
        else:
            s.append(b)
        if v:
            s.append(BN_SIGN[v])
        prev = u
    out = "".join(s)
    # diphthongs: া + ই / ও  ->  াই / াও  are already produced by the coda rule
    return out.replace("ইয়", "ইয়")

PUNCT_BN = dict(PUNCT_LATN, **{".": "।"})

# ---------------------------------------------------------------- Hindi / Devanagari
DV = {"b": "ब", "t": "त", "T": "स", "j": "ज", "H": "ह", "x": "ख़", "d": "द", "D": "ज़", "r": "र", "z": "ज़",
      "s": "स", "S": "श", "c": "स", "Q": "ज़", "X": "त", "Z": "ज़", "g": "ग़", "f": "फ़", "q": "क़", "k": "क",
      "l": "ल", "m": "म", "n": "न", "h": "ह", "w": "व", "y": "य"}
DV_SIGN = {"a": "", "i": "ि", "u": "ु", "A": "ा", "I": "ी", "U": "ू"}
DV_IND = {"a": "अ", "i": "इ", "u": "उ", "A": "आ", "I": "ई", "U": "ऊ"}
VIR = "्"

def hi_word(toks):
    U = units(toks)
    s = []
    for k, u in enumerate(U):
        if u[0] == "-":
            # sun letter: written joined (अस्सलाम); moon letter: keep the hyphen (अल्-अन्सारी)
            nx = U[k + 1] if k + 1 < len(U) else None
            pv = U[k - 1] if k else None
            if nx and pv and len(nx) > 1 and len(pv) > 1 and nx[1] != pv[1]:
                s.append("-")
            continue
        if u[0] == "V":
            s.append(DV_IND[u[1]]); continue
        code, gem = u[1], u[2]
        v = u[3] if u[0] == "CV" else None
        prev = U[k - 1] if k else None
        prev_v = prev[3] if prev and prev[0] == "CV" else None
        if code in ("'", "E"):
            mark = "ʾ" if code == "'" else "ʿ"
            if code == "'" and (k == 0 or U[k - 1] == ("-",)):
                mark = ""
            s.append(mark)
            if v:
                s.append(DV_IND[v])
            continue
        if v is None and code in ("y", "w") and (prev_v == "a" or (prev and prev[0] in ("V", "CV") and s and s[-1] == "अ")) and not gem:
            # diphthong: replace the bare consonant of the previous syllable with ै / ौ
            if s and s[-1] == "अ":
                s[-1] = "ऐ" if code == "y" else "औ"
            else:
                s.append("ै" if code == "y" else "ौ")
            continue
        d = DV[code]
        if gem:
            s.append(d + VIR)
        s.append(d)
        if v:
            s.append(DV_SIGN[v])
        else:
            s.append(VIR)                         # halant: no vowel (also word-final)
    return "".join(s)

PUNCT_HI = dict(PUNCT_LATN, **{".": "।"})

# ---------------------------------------------------------------- Japanese katakana
KANA_ROWS = {
    "b": "バビブ", "t": ("タ", "ティ", "トゥ"), "X": ("タ", "ティ", "トゥ"), "T": ("サ", "スィ", "ス"),
    "s": ("サ", "スィ", "ス"), "c": ("サ", "スィ", "ス"), "j": ("ジャ", "ジ", "ジュ"), "H": "ハヒフ", "h": "ハヒフ",
    "x": "ハヒフ", "d": ("ダ", "ディ", "ドゥ"), "Q": ("ダ", "ディ", "ドゥ"), "D": ("ザ", "ズィ", "ズ"),
    "z": ("ザ", "ズィ", "ズ"), "Z": ("ザ", "ズィ", "ズ"), "r": "ラリル", "l": "ラリル", "S": ("シャ", "シ", "シュ"),
    "E": "アイウ", "'": "アイウ", "g": "ガギグ", "f": ("ファ", "フィ", "フ"), "q": "カキク", "k": "カキク",
    "m": "マミム", "n": "ナニヌ", "w": ("ワ", "ウィ", "ウ"), "y": ("ヤ", "イ", "ユ"),
}
KANA_CODA = {"b": "ブ", "t": "ト", "X": "ト", "T": "ス", "s": "ス", "c": "ス", "j": "ジュ", "H": "フ", "h": "フ",
             "x": "フ", "d": "ド", "Q": "ド", "D": "ズ", "z": "ズ", "Z": "ズ", "r": "ル", "l": "ル", "S": "シュ",
             "E": "", "'": "", "g": "グ", "f": "フ", "q": "ク", "k": "ク", "m": "ム", "n": "ン", "w": "ウ", "y": "イ"}
VI = {"a": 0, "i": 1, "u": 2, "A": 0, "I": 1, "U": 2}

def ja_word(toks):
    U = [u for u in units(toks) if u[0] != "-"]
    s = []
    for k, u in enumerate(U):
        last = k == len(U) - 1
        if u[0] == "V":
            s.append("アイウ"[VI[u[1]]] + ("ー" if u[1] in "AIU" else "")); continue
        code, gem = u[1], u[2]
        if gem and code in ("y", "w"):
            pv = U[k - 1][3] if k and U[k - 1][0] == "CV" else None
            if (code == "y" and pv == "i") or (code == "w" and pv == "u"):
                s.append("ー")                        # nabiyy -> ナビーイ, quwwa -> クーワ
            else:
                s.append("イ" if code == "y" else "ウ")   # sayyid -> サイイド, awwal -> アウワル
        elif gem and code not in ("E", "'"):
            s.append("ン" if code in ("m", "n") else "ッ")
        if u[0] == "CV":
            v = u[3]
            s.append(KANA_ROWS[code][VI[v]])
            if v in "AIU":
                s.append("ー")
        else:
            if code == "h" and last and k > 0 and U[k - 1][0] in ("CV", "V"):
                continue                          # final -ah / -āh: マディーナ, アッラー
            nxt = U[k + 1] if k + 1 < len(U) else None
            if nxt and nxt[0] in ("CV", "C") and nxt[1] == code and code not in ("E", "'"):
                s.append("ン" if code in ("m", "n") else ("イ" if code == "y" else ("ウ" if code == "w" else "ッ")))
                continue
            prev = U[k - 1] if k else None
            pv = prev[3] if prev and prev[0] == "CV" else None
            if code in ("y", "w") and pv == "a":
                s.append("イ" if code == "y" else "ウ"); continue
            s.append(KANA_CODA[code])
    return "".join(s)

PUNCT_JA = {"،": "、", ".": "。", "؛": "；", "؟": "？", ":": "：", "{": "「", "}": "」", "«": "「", "»": "」",
            "\"": "", "*": "", "-": "—"}

# ---------------------------------------------------------------- registry
SCHEMES = {
    "latn": (latn_word, PUNCT_LATN, " "),
    "bn": (bn_word, PUNCT_BN, " "),
    "hi": (hi_word, PUNCT_HI, " "),
    "ja": (ja_word, PUNCT_JA, " "),
}


def pronounce(arabic, scheme, warnings=None):
    word, punct, space = SCHEMES[scheme]
    items, warns = analyse(arabic)
    if warnings is not None:
        warnings.extend(warns)
    s = walk(items, word, punct, space, quotes=QUOTES.get(scheme, ("“", "”")))
    if scheme == "ja":
        for a, b in ((" 。", "。"), (" 、", "、"), ("「 ", "「"), (" 」", "」"), ("。 ", "。"), ("、 ", "、")):
            s = s.replace(a, b)
    return s
