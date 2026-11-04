# -*- coding: utf-8 -*-
"""Generator for Brahmi-family (Indic) books: vowels + consonants, vowel signs, a consonant that
carries a hidden vowel. A language file supplies the data; this builds the LANG dict the engine uses."""
import os

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")


def fontset(disp, dprefix, text, tprefix):
    out = []
    for fam, pre in ((disp, dprefix), (text, tprefix)):
        for w in (400, 700, 800):
            f = f"{pre}-{w}-normal.woff2"
            if os.path.exists(os.path.join(FONTS, f)):
                out.append((fam, w, "normal", f, None))
    return out


def vowel(letter, name_tr, sound, sign, sign_name, word, tr, meaning, pic, args=None, name=None, note=None):
    return dict(letter=letter, name_native=name or letter, name_en=name_tr, sound=sound, sign=sign, sign_name=sign_name,
                word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {}, note=note)


def cons(letter, name_tr, sound, word, tr, meaning, pic, args=None, name=None, note=None, phon=None):
    return dict(letter=letter, name_native=name or letter, name_en=name_tr, sound=sound, word=word, translit=tr,
                meaning=meaning, pic=pic, pic_args=args or {}, note=note, phon=phon)


def _span(t):
    return f'<span class="nt">{t}</span>'


def build(d):
    """d: the language data dict (see languages/pa.py for the keys)."""
    base, vir, inh, inh_tr = d["base"], d["virama"], d["inherent"], d["inherent_tr"]
    lang = d["name"]
    examples = d.get("examples", {})

    def ex_of(sign):
        return examples.get(sign, base + sign)

    vitems = []
    for v in d["vowels"]:
        if v["sign"]:
            ex = ex_of(v["sign"])
            phon = (f'<div class="nt" style="font-size:17pt">◌{v["sign"]} <span class="small" style="font-family:Nunito">'
                    f'({v["sign_name"]})</span></div>'
                    f'<div class="nt" style="font-size:17pt">{base} + ◌{v["sign"]} = {ex}</div>')
        elif v is d["vowels"][0]:
            phon = (f'<div style="font-size:11.5pt">No sign! {_span(v["letter"])} hides inside every consonant: '
                    f'{_span(base + " = " + base + vir + " + " + v["letter"])}</div>')
        else:
            phon = '<div style="font-size:11.5pt">A special letter — it has no vowel sign of its own.</div>'

        vitems.append(dict(v, phon=phon, phon_label=f"{lang} phonetics · vowel sign"))

    citems = []
    for c in d["consonants"]:
        ph = c["phon"] or f'{c["letter"]}{vir} + {inh} = {c["letter"]}'
        citems.append(dict(c, phon=f'<div class="nt" style="font-size:19pt">{ph}</div>',
                           phon_label=f"{lang} phonetics · how it is built"))

    rows = "".join(
        f'<tr><td class="ntd" style="font-size:20pt">{v["letter"]}</td><td class="tr">{v["name_en"]}</td>'
        f'<td class="nt" style="font-size:15pt">{("◌" + v["sign"]) if v["sign"] else "—"}</td>'
        f'<td class="nt" style="font-size:15pt">{ex_of(v["sign"]) if v["sign"] else base}</td></tr>' for v in vitems)
    nv, nc = len(vitems), len(citems)
    vintro = f"""<p>Vowels are the sounds you make with your mouth open: <i>{inh_tr}, aa, i, ee, u, oo…</i> This book has <b>{nv} vowels</b>.</p>
<p>A vowel has <b>two shapes</b>. At the start of a word it is a full letter. After a consonant it becomes a small
<b>vowel sign</b> that holds on to the consonant: {_span(base + " + ◌" + vitems[1]["sign"] + " = " + ex_of(vitems[1]["sign"]))}.
{d.get("vowel_extra", "")}</p>
<table style="width:100%;border-collapse:collapse;margin-top:0.08in;text-align:center" class="vt">
<tr style="font:600 10.5pt Fredoka"><th>Vowel</th><th>Name</th><th>Sign</th><th>With {_span(base)}</th></tr>{rows}</table>
<style>.vt td,.vt th{{border-bottom:1.5px solid #bbb;padding:1px 4px}}</style>"""
    fam = ""
    if d.get("families"):
        fam = ('<div class="box" style="margin:0.1in 0"><h3>Families of five</h3>The first consonants come in families, each made in a '
               'different part of the mouth:<div class="nt" style="font-size:17pt;line-height:1.65;margin-top:4px">' +
               "<br>".join(f'{row} — <span class="small" style="font-family:Nunito">{where}</span>' for row, where in d["families"]) +
               "</div></div>")
    cintro = f"""<p>Consonants are the sounds made by stopping or squeezing the air: <i>k, g, ch, j, t, d, p, b…</i>
This book has <b>{nc} consonants</b>.{d.get("cons_extra", "")}</p>
<div class="box" style="margin:0.1in 0"><h3>The hidden vowel</h3>Every consonant secretly carries a short vowel <i>({inh_tr})</i>.
That is why {_span(base)} is said <i>{d["base_tr"]}</i>, not just <i>{d["base_tr"][:-len(inh_tr)] or d["base_tr"]}</i>:
<div class="nt" style="font-size:22pt;text-align:center;margin-top:2px">{base}{vir} + {inh} = {base}</div>
<div style="text-align:center">{d["virama_note"]}</div></div>
{fam}{d.get("cons_box", "")}"""

    L = dict(d)
    L["sections"] = [
        dict(key="vowels", label="VOWEL", chip="PART 1", title="The Vowels", native=d["vowels_native"], native_tr=d["vowels_tr"],
             chart_title="vowels", chart_cols=d.get("vowel_cols", 7), warmup_title="the vowels", warmup_cols=4,
             intro_html=vintro, items=vitems),
        dict(key="consonants", label="CONSONANT", chip="PART 2", title="The Consonants", native=d["cons_native"],
             native_tr=d["cons_tr"], chart_title="consonants", chart_cols=d.get("cons_cols", 7),
             warmup_title="the consonants", warmup_cols=6 if nc <= 42 else 7, intro_html=cintro, items=citems),
    ]
    L.setdefault("phon_explain",
                 f"The box marked <i>{lang} phonetics</i> shows how the sound is built the way {lang} children learn it, "
                 f"for example {_span(base + vir + ' + ' + inh + ' = ' + base)}, or a vowel sign added to a consonant.")
    L.setdefault("chart_note", "Read the alphabet left to right, row by row — the same order as in this book.")
    n = nv + nc
    L["subtitle"] = f"A Coloring Book to Learn, Trace & Say the {n} {lang} Letters with English Phonetics"
    L["title"] = f"My First {lang} Alphabet"
    sample = d["sample_words"]  # [(word, tr, meaning)] x3
    sw = ", ".join(f"{_span(w)} <i>{t}</i> {m}" for w, t, m in sample[:2])
    swk = ", ".join(f"{w} <i>{t}</i> ({m})" for w, t, m in sample)
    L["cover"] = dict(
        title_html=f"My First {lang}<br>Alphabet", tiles=d["tiles"], pics=d["cover_pics"],
        title_size=d.get("title_size", 50),
        blurb=f"{d['speakers_blurb']} This big, friendly coloring book introduces young children to <b>{n} letters</b> of the "
              f"{lang} alphabet <b>through English</b> — no {lang} needed at home.",
        bullets=[f"<b>Every letter on its own page</b> — a giant letter to color, its name in {lang} <i>and</i> English letters",
                 f"<b>Easy English sound guides</b> plus {lang} phonetics ({_span(base + vir + ' + ' + inh + ' = ' + base)})",
                 f"<b>A word and picture for every letter</b>: {sw}…",
                 "<b>Pencil tracing rows</b> and warm-up pages for vowels and consonants",
                 f"<b>Map to color</b>, {lang} numbers {_span(d['digits'][0][0] + '–' + d['digits'][9][0])}, first phrases and a certificate",
                 "<b>Single-sided coloring pages</b> so markers never ruin the next picture"])
    L["kdp"] = dict(
        market=d.get("market", "Amazon.com (also Amazon.co.uk and Amazon.ca)"),
        desc_intro=f"{d['speakers_blurb']} This big, friendly coloring book introduces young children to <b>{n} letters</b> of the "
                   f"{lang} alphabet <b>through English</b>, so no {lang} is needed at home.",
        desc_bullets=[f"<b>Every letter on its own page:</b> a giant letter to color, with its name written in {lang} <i>and</i> in English letters",
                      f"<b>Easy English sound guides</b> plus simple {lang} phonetics ({base}{vir} + {inh} = {base}, and the vowel signs)",
                      f"<b>A word and a picture for every letter</b> to color and say: {swk}…",
                      "<b>Pencil tracing rows</b> on every page, plus warm-up pages for the vowels and consonants",
                      f"<b>Meet the language:</b> where {lang} is spoken, a map to color, the whole alphabet on one page, the numbers "
                      f"{d['digits'][0][0]}–{d['digits'][9][0]} and first friendly phrases"],
        categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                    "Children's Books › Education & Reference › Foreign Language Study",
                    "Children's Books › Religions › Islam"],
        keywords=d["keywords"])
    L["series_line"] = (f"<b>Book {d['series_no']} is {lang}</b>. More languages of the subcontinent are in the series, "
                        "in shā’ Allāh.")
    return L


COMMON_NOTES = [
    "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
    "<b>h after a letter</b> (<i>kh, gh, th, dh, bh</i>) means “add a puff of breath” — hold a tissue in front of your mouth "
    "and watch it move! It never means the English “th” of “the”.",
]
