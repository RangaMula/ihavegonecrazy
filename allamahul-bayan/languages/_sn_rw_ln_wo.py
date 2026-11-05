# -*- coding: utf-8 -*-
"""Shared helpers for Books 70-73 (Shona, Kinyarwanda, Lingala, Wolof). Latin script, "Aa" letter pages.

Fonts: Baloo 2 (display) + Nunito (text), as in Spanish. Baloo 2 latin-ext has Ŋ ŋ but no Ɛ ɛ Ɔ ɔ
(Lingala), and Nunito has none of those four either. So the open vowels are taken from
M PLUS Rounded 1c (display, rounded like Baloo) and Noto Sans (text) latin-ext, through unicode-range
faces added after the engine's own faces (later faces win in the browser).
"""
from generic import letter

LATEXT = "U+0100-02AF,U+1E00-1EFF"
OPEN = "U+0186,U+0190,U+0254,U+025B"          # Ɔ Ɛ ɔ ɛ


def fonts():
    out = []
    for w in (400, 700, 800):
        out += [("Baloo 2", w, "normal", f"baloo-2-latin-{w}-normal.woff2", None),
                ("Baloo 2", w, "normal", f"baloo-2-latin-ext-{w}-normal.woff2", LATEXT),
                ("Baloo 2", w, "normal", "m-plus-rounded-1c-latin-ext-800-normal.woff2", OPEN),
                ("Nunito", w, "normal", f"nunito-latin-ext-{w}-normal.woff2", LATEXT),
                ("Nunito", w, "normal", f"noto-sans-latin-ext-{w}-normal.woff2", OPEN)]
    return out


# the big coloring letters: the engine takes the first file that has every character
GLYPH_FONTS = ["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2",
               "m-plus-rounded-1c-latin-ext-800-normal.woff2", "noto-sans-latin-ext-800-normal.woff2"]


def maker(phon_label, vowels, vowel_examples="b k m n"):
    """L(cap, small, name, name_tr, sound, word, tr, meaning, pic, ...) for one book.
    The phonetics box shows the letter's name and its syllable row (ba be bi bo bu): children in
    these languages learn to read syllable by syllable."""
    def L(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
        if row is None:
            row = (" · ".join(c + small for c in vowel_examples.split()) if vowel
                   else " · ".join(small + v for v in vowels))
        phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
                f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>'
                + (f'<div class="small">{rule}</div>' if rule else ""))
        return letter(cap + small, name, name_tr, sound, word, tr, meaning, pic, phon, phon_label, args, note)
    return L


def inside(cap, word):
    """Note for a letter that rarely starts a word."""
    return f"Few words begin with {cap}. Can you find it inside <i>{word}</i>?"
