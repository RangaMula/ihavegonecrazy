# -*- coding: utf-8 -*-
"""Shared helpers for Books 66-69 (Somali, Oromo, Zulu, Xhosa): Latin-script books on the es.py model.
Big letter = capital + small ("Bb"); digraphs are drawn "Dh dh".

The phonetics box shows the letter's name and its syllable row (ba be bi bo bu), the way children in
these languages learn to read. In a word, [x] marks the letter(s) to underline (e.g. "isi[c]athulo")."""
import re
from generic import letter, fontset

FONTS = fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext")
GLYPH_FONTS = ["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"]

# underline for the letter inside the word (Zulu/Xhosa words start with a prefix such as i-, u-, isi-)
CSS = """
.hl { text-decoration: underline; text-decoration-thickness: 0.07em; text-underline-offset: 0.14em; }
"""


def mark(word):
    """'isi[c]athulo' -> 'isi<span class="hl">c</span>athulo'"""
    return re.sub(r"\[([^\]]+)\]", r'<span class="hl">\1</span>', word)


def plain(word):
    return word.replace("[", "").replace("]", "")


def maker(phon_label, vowels="a e i o u"):
    vs = vowels.split()

    def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, row=None, vowel=False):
        small = cap.lower()
        big = cap + small if len(cap) == 1 else f"{cap} {small}"
        if row is None:
            row = ("" if vowel else " · ".join(small + v for v in vs))
        phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
                + (f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>' if row else "")
                + (f'<div class="small">{rule}</div>' if rule else ""))
        return letter(big, name, name_tr, sound, mark(word), tr, meaning, pic, phon, phon_label, args, note)
    return L
