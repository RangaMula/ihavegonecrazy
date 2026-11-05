# -*- coding: utf-8 -*-
"""Shared helpers for the Ethiopic-script (Ge'ez fidel) books: Book 56 Amharic (am) and Book 57 Tigrinya (ti).

Each letter page teaches one consonant family through its base (1st-order) form; the phonetics box shows the
family's seven orders with their sounds, and marks the order that starts (or appears in) the page's word."""
import re
from generic import letter

ORDER_EN = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]
VOWELS = ["e", "u", "i", "a", "é", "(i)", "o"]            # sound of each order, after the consonant
ORDER_NAMES = [("ግዕዝ", "ge'ez"), ("ካዕብ", "ka'ib"), ("ሣልስ", "salis"), ("ራብዕ", "rabi'"),
               ("ኃምስ", "hamis"), ("ሳድስ", "sadis"), ("ሳብዕ", "sabi'")]
VOWEL_GUIDE = ["‘e’ as in “the”", "‘u’ as in “rule”", "‘i’ as in “ski”", "‘a’ as in “father”",
               "‘é’ as in “café”", "a quick ‘i’ as in “sit”, or no vowel", "‘o’ as in “go”"]

CSS = """
.fam { display:grid; grid-template-columns:repeat(7,1fr); gap:3px; margin-top:5px }
.fam > div { border:1.5px solid #aaa; border-radius:7px; text-align:center; padding:1px 0 3px }
.fam > div.b { border:2.6px solid #111 }
.fam > div.w { background:#e6e6e6 }
.fam .g { font:700 19pt 'Noto Sans Ethiopic',sans-serif; line-height:1.3 }
.fam .s { font:italic 8pt 'Nunito',sans-serif; line-height:1.05; white-space:nowrap; letter-spacing:-.02em }
.fam .o { font:600 6.5pt 'Fredoka',sans-serif; color:#555; line-height:1.1 }
.famnote { font-size:10pt; line-height:1.3; margin-top:6px }
table.fidel { border-collapse:collapse; width:100%; margin:0.06in 0 0.1in; text-align:center }
table.fidel td, table.fidel th { border:1.5px solid #111; padding:1px 2px }
table.fidel th { font:600 9pt 'Fredoka','Noto Sans Ethiopic',sans-serif; background:#eee; line-height:1.2 }
table.fidel td.g { font:700 21pt 'Noto Sans Ethiopic',sans-serif; line-height:1.3 }
table.fidel td.k { font:600 10pt 'Fredoka',sans-serif; background:#eee }
table.fidel .s { display:block; font:italic 8.5pt 'Nunito',sans-serif; line-height:1 }
"""


def orders(base):
    """The seven orders of a family: in Unicode they follow the base letter one after another."""
    return [chr(ord(base) + i) for i in range(7)]


def sounds(cons, vowels=None):
    v = list(vowels or VOWELS)
    if cons == "":                                   # glottal families (አ): the vowel alone
        v[5] = "i"
    return [cons + x for x in v]


def fam_html(base, cons, mark=None, vowels=None):
    """Seven boxes: glyph, sound, order. The base form gets a bold border; the order used in the word is shaded."""
    g, s = orders(base), sounds(cons, vowels)
    cells = []
    for i in range(7):
        cls = " ".join(c for c in ("b" if i == 0 else "", "w" if i == mark and i != 0 else "") if c)
        cells.append(f'<div class="{cls}"><div class="g">{g[i]}</div><div class="s">{s[i]}</div>'
                     f'<div class="o">{ORDER_EN[i]}</div></div>')
    return '<div class="fam">' + "".join(cells) + "</div>"


def make_L(label):
    def L(base, cons, name_native, name_en, sound, word, tr, meaning, pic, args=None, note=None,
          vowels=None, key=None, inside=False):
        g = orders(base)
        plain = re.sub(r"<[^>]+>", "", word)
        key = key or next((ch for ch in plain if ch in g), None)
        mark = g.index(key) if key in g else None
        s = sounds(cons, vowels)
        if mark is None:
            where = ""
        else:
            pos = "starts" if plain[0] == key and not inside else "is found inside"
            where = (f'<span class="nt">{key}</span> <i>{s[mark].replace("(i)", "i")}</i>, the <b>{ORDER_EN[mark]}</b> '
                     f'sound of this family, {pos} the word <span class="nt">{plain}</span>.')
        phon = (fam_html(base, cons, mark, vowels)
                + f'<div class="famnote">{where}</div>')
        return letter(base, name_native, name_en, sound, word, tr, meaning, pic, phon, label.format(base), args, note)
    return L


def grid_table(rows, vowels=None):
    """rows: [(base, cons)] -> a fidel grid with the seven vowel columns."""
    head = "".join(f'<th>{ORDER_EN[i]}<br><span class="nt">{ORDER_NAMES[i][0]}</span></th>' for i in range(7))
    v = list(vowels or VOWELS)
    vrow = "".join(f'<td class="k">-{x}</td>' for x in v)
    body = "".join("<tr>" + "".join(f'<td class="g">{g}<span class="s">{s}</span></td>'
                                    for g, s in zip(orders(b), sounds(c, vowels))) + "</tr>" for b, c in rows)
    return f'<table class="fidel"><tr>{head}</tr><tr>{vrow}</tr>{body}</table>'
