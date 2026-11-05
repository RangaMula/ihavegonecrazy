# -*- coding: utf-8 -*-
"""Shared helpers for the African Latin-script books (Swahili, Hausa, Yoruba, Igbo).

Fonts: Baloo 2 (display) and Nunito (text) do not cover every African letter on their own:
  - Baloo 2 latin-ext lacks the hooked letters (ɓ ɗ ƙ ƴ) and the dotted vowels (ẹ ọ ị ụ);
  - the dotted vowels and the combining tone marks live in the *vietnamese* subset;
  - ɓ ɗ ƴ come from Nunito latin-ext, ƙ (and ǹ) only from Noto Sans latin-ext.
So the faces below build one composite family each, with unicode-range so every character is
taken from a file that really contains it (later faces win in the browser).
"""
from generic import letter

LATEXT = "U+0100-02AF,U+02BC,U+1E00-1E9F"
VIET = "U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9"
HOOKS = "U+0181,U+018A,U+01B3-01B4,U+0253,U+0257"   # Ɓ Ɗ Ƴ ƴ ɓ ɗ  (Nunito latin-ext)
NOTO = "U+0198-0199,U+01F8-01F9"                       # Ƙ ƙ Ǹ ǹ      (Noto Sans latin-ext)


def afro_fonts():
    out = []
    for w in (400, 700, 800):
        out += [("Baloo 2", w, "normal", f"baloo-2-latin-{w}-normal.woff2", None),
                ("Baloo 2", w, "normal", f"baloo-2-latin-ext-{w}-normal.woff2", LATEXT),
                ("Baloo 2", w, "normal", f"baloo-2-vietnamese-{w}-normal.woff2", VIET),
                ("Baloo 2", w, "normal", f"nunito-latin-ext-{w}-normal.woff2", HOOKS),
                ("Baloo 2", w, "normal", f"noto-sans-latin-ext-{w}-normal.woff2", NOTO),
                ("Nunito", w, "normal", f"nunito-vietnamese-{w}-normal.woff2", VIET),
                ("Nunito", w, "normal", f"noto-sans-latin-ext-{w}-normal.woff2", NOTO)]
    return out


# the big coloring letters: the engine takes the first file that has every character
GLYPH_FONTS = ["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2",
               "baloo-2-vietnamese-800-normal.woff2", "nunito-latin-ext-800-normal.woff2",
               "noto-sans-latin-ext-800-normal.woff2"]
FONT_CREDIT = "Baloo 2, Noto Sans"

# ten phrase rows (greeting + reply) need a little less height than the engine default
EXTRA_CSS = '.ntd[style*="font-size:19pt"]{font-size:17pt !important;line-height:1.3 !important}' 


def maker(phon_label, vowels, vowel_examples="b d k m n"):
    """Return L(cap, small, name, name_tr, sound, word, tr, meaning, pic, ...) for one book.
    The phonetics box shows the letter's name and its syllable row (ba be bi bo bu), which is how
    children in these languages learn to read."""
    def syl(c):
        return " · ".join(c + v for v in vowels)

    def L(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
        big = cap + small if len(cap) == 1 else f"{cap} {small}"
        if row is None:
            row = (" · ".join(c + small for c in vowel_examples.split()) if vowel else syl(small))
        phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
                f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>'
                + (f'<div class="small">{rule}</div>' if rule else ""))
        return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, phon_label, args, note)
    return L
