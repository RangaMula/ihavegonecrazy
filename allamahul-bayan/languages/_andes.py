# -*- coding: utf-8 -*-
"""Shared helpers for the Andean / southern-cone books: Quechua (82), Aymara (84), Mapudungun (88).

These alphabets are Latin letters plus letter groups: aspirated (chh kh ph qh th), ejective (ch' k' p' q' t')
and other digraphs (ch ll ng tr). Baloo 2 (latin + latin-ext) and Nunito cover every character used,
including Ñ ñ, Ä Ï Ü ä ï ü and the apostrophe ’ (U+2019) that marks the ejective "popping" sounds.
"""
from generic import letter, fontset

FONTS = fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext")
GLYPH_FONTS = ["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"]
FONT_CREDIT = "Baloo 2, Nunito"


def maker(phon_label, vowels):
    """Return L(cap, small, name, name_tr, sound, word, tr, meaning, pic, ...).
    The big letter is "Aa" for a single letter and "Ch ch" / "K’ k’" for letter groups.
    The phonetics box shows the letter's name and its syllables (cha · chi · chu), the way these
    alphabets are taught in school."""
    def L(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
        big = cap + small if len(cap) == 1 else f"{cap} {small}"
        if row is None:
            row = "" if vowel else " · ".join(small + v for v in vowels)
        phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
                + (f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>' if row else "")
                + (f'<div class="small">{rule}</div>' if rule else ""))
        return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, phon_label, args, note)
    return L


ASPIRATE = "with a strong puff of air after it"
EJECTIVE = "a “popping” sound: hold your breath in your throat, then let it pop"
