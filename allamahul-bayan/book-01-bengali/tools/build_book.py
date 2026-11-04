# -*- coding: utf-8 -*-
"""Builds the KDP interior: build/interior.html -> output/interior.pdf (via render.mjs).

Trim 8.5 x 11 in, no bleed, black & white. Every coloring page sits on a right-hand (odd)
page with a blank back so markers never bleed onto another activity.
Run:  python3 tools/build_book.py && node tools/render.mjs
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from content import BOOK, VOWELS, CONSONANTS, DIGITS, PHRASES, AYAH_RAHMAN, AYAH_RUM, AYAH_HUJURAT
from illos import svg as pic
from glyphs import letter_svg
from brand import mark_svg

FONTS = "../assets/fonts/"
CSS = f"""
@font-face{{font-family:'Baloo Da 2';font-weight:400;src:url({FONTS}baloo-da-2-bengali-400-normal.woff2)}}
@font-face{{font-family:'Baloo Da 2';font-weight:700;src:url({FONTS}baloo-da-2-bengali-700-normal.woff2)}}
@font-face{{font-family:'Baloo Da 2';font-weight:800;src:url({FONTS}baloo-da-2-bengali-800-normal.woff2)}}
@font-face{{font-family:'Noto Sans Bengali';font-weight:400;src:url({FONTS}noto-sans-bengali-bengali-400-normal.woff2)}}
@font-face{{font-family:'Noto Sans Bengali';font-weight:700;src:url({FONTS}noto-sans-bengali-bengali-700-normal.woff2)}}
@font-face{{font-family:'Fredoka';font-weight:400;src:url({FONTS}fredoka-latin-400-normal.woff2)}}
@font-face{{font-family:'Fredoka';font-weight:600;src:url({FONTS}fredoka-latin-600-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:400;src:url({FONTS}nunito-latin-400-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:400;src:url({FONTS}nunito-latin-ext-400-normal.woff2);unicode-range:U+0100-024F,U+1E00-1EFF,U+02BB-02BF}}
@font-face{{font-family:'Nunito';font-weight:700;src:url({FONTS}nunito-latin-700-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:700;src:url({FONTS}nunito-latin-ext-700-normal.woff2);unicode-range:U+0100-024F,U+1E00-1EFF,U+02BB-02BF}}
@font-face{{font-family:'Nunito';font-weight:800;src:url({FONTS}nunito-latin-800-normal.woff2)}}
@font-face{{font-family:'Nunito';font-style:italic;font-weight:400;src:url({FONTS}nunito-latin-400-italic.woff2)}}
@font-face{{font-family:'Amiri';font-weight:400;src:url({FONTS}amiri-arabic-400-normal.woff2)}}
@font-face{{font-family:'Amiri';font-weight:700;src:url({FONTS}amiri-arabic-700-normal.woff2)}}
@font-face{{font-family:'Dancing Script';font-weight:700;src:url({FONTS}dancing-script-latin-700-normal.woff2)}}

@page {{ size: 8.5in 11in; margin: 0 }}
* {{ box-sizing: border-box }}
html,body {{ margin:0; padding:0; background:#fff; color:#111 }}
body {{ font-family:'Nunito','Noto Sans Bengali',sans-serif; font-size:13pt; line-height:1.4 }}
.bn {{ font-family:'Noto Sans Bengali','Nunito',sans-serif }}
.bnd {{ font-family:'Baloo Da 2','Noto Sans Bengali',sans-serif }}
.ar {{ font-family:'Amiri',serif; direction:rtl }}
.tr {{ font-style:italic }}
.fd {{ font-family:'Fredoka','Nunito',sans-serif }}
.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always;
        padding:0.6in 0.6in 0.62in 0.8in }}
.page.even {{ padding:0.6in 0.8in 0.62in 0.6in }}
.inner {{ position:relative; width:100%; height:100% }}
.pno {{ position:absolute; bottom:0.3in; width:7.1in; text-align:center; font:600 10pt 'Fredoka',sans-serif; color:#555 }}
.page .pno {{ left:0.8in }} .page.even .pno {{ left:0.6in }}
h1,h2,h3 {{ font-family:'Fredoka','Baloo Da 2',sans-serif; font-weight:600; margin:0 }}
h1 {{ font-size:30pt; line-height:1.1 }}
h2 {{ font-size:22pt; line-height:1.15 }}
h3 {{ font-size:14pt }}
p {{ margin:0 0 0.12in }}
.frame {{ border:3px solid #111; border-radius:22px }}
.dash {{ border:2.5px dashed #111; border-radius:18px }}
.chip {{ display:inline-block; border:2px solid #111; border-radius:999px; padding:1px 12px; font:600 11pt 'Fredoka','Noto Sans Bengali',sans-serif }}
.muted {{ color:#444 }}
.small {{ font-size:10.5pt }}
.ill {{ display:block }}
.ill * {{ stroke:#111; stroke-width:3.2; stroke-linejoin:round; stroke-linecap:round }}
.ill .a,.ill .b,.ill .c,.ill .d,.ill .e {{ fill:#fff }}
.ill .n {{ fill:none }} .ill .t {{ stroke-width:2 }}
.ill text {{ font-family:'Baloo Da 2','Noto Sans Bengali',sans-serif; font-weight:800; fill:#fff; stroke-width:2.4 }}
.ill text.blk {{ stroke-width:2 }}
.ill text.lbl {{ font-weight:700; fill:#111; stroke:none }}
.glyph {{ display:block; width:100%; height:100% }}

/* ---- letter page ---- */
.lp-head {{ display:flex; justify-content:space-between; align-items:center; height:0.42in }}
.lp-top {{ display:flex; gap:0.18in; height:4.05in; margin-top:0.08in }}
.lp-letter {{ width:3.95in; height:4.05in; padding:0.12in; position:relative }}
.lp-info {{ flex:1; display:flex; flex-direction:column; gap:0.09in }}
.box {{ border:2px solid #111; border-radius:14px; padding:0.07in 0.13in }}
.lbl {{ font:600 9pt 'Fredoka','Noto Sans Bengali',sans-serif; text-transform:uppercase; letter-spacing:.06em; color:#333 }}
.lp-name {{ font:700 22pt 'Noto Sans Bengali',sans-serif; line-height:1.25 }}
.lp-pic {{ display:flex; gap:0.15in; height:3.15in; margin-top:0.16in; padding:0.1in 0.18in; align-items:center }}
.lp-pic .ill {{ width:2.9in; height:2.9in }}
.lp-word {{ flex:1; text-align:center }}
.lp-word .w {{ font:800 40pt 'Baloo Da 2',sans-serif; line-height:1.15 }}
.lp-word .t {{ font:italic 400 17pt 'Nunito',sans-serif }}
.lp-word .m {{ font:700 16pt 'Nunito',sans-serif; margin-top:2px }}
.lp-trace {{ margin-top:0.16in; height:1.42in; padding:0.06in 0.15in }}
.trow {{ display:flex; gap:0.08in; align-items:center; height:1.0in; border-top:1.5px solid #bbb; border-bottom:1.5px solid #bbb; margin-top:0.04in }}
.trow .cell {{ width:0.98in; height:0.98in }}
.trow .free {{ width:0.98in; height:0.86in; border:2px dashed #999; border-radius:10px }}
.blankmsg {{ position:absolute; bottom:0.25in; width:100%; text-align:center; font:400 8.5pt 'Nunito',sans-serif; color:#777 }}
.grid {{ display:grid; gap:0.12in }}
"""

pages = []  # list of (html, kind)

def add(html, kind="content", number=True):
    pages.append(dict(html=html, kind=kind, number=number))

def blank(note=True):
    msg = ('<div class="blankmsg">This page is left blank on purpose, so your colours don’t '
           'bleed through. ✿</div>') if note else ""
    add(msg, "blank", number=False)

def head(left, right):
    return (f'<div class="lp-head"><span class="chip">{left}</span>'
            f'<span class="small muted fd">{right}</span></div>')

def ayah_box(a, sup="¹", ar_size=21):
    return (f'<div class="frame" style="padding:0.12in 0.2in;margin:0.1in 0">'
            f'<div class="ar" style="font-size:{ar_size}pt;line-height:1.9;text-align:center">{a["ar"]}</div>'
            f'<div class="tr small" style="text-align:center;margin-top:2px">{a["tr"]}</div>'
            f'<div style="text-align:center;margin-top:4px">“{a["en"]}”</div>'
            f'<div style="text-align:center;margin-top:5px"><span class="chip" style="font-size:9.5pt">{a["ref"]}<sup>{sup}</sup></span></div>'
            f'</div>')

# =========================================================================================
# FRONT MATTER
# =========================================================================================
def title_page():
    letters = "".join(f'<div style="width:0.95in;height:0.95in">{letter_svg(c, "color", min_box=700)}</div>'
                      for c in "অআইকখগ")
    add(f"""
<div style="text-align:center;padding-top:0.15in">
  <div class="chip">{BOOK['series'].upper()} · BOOK {BOOK['series_no']}</div>
  <div class="ar" style="font-size:22pt;margin-top:0.08in">{BOOK['series_ar']}</div>
  <h1 style="font-size:40pt;margin-top:0.25in">{BOOK['title']}</h1>
  <div class="bnd" style="font-size:30pt;font-weight:800;margin-top:0.08in">{BOOK['title_bn']}</div>
  <p style="font-size:14pt;margin:0.2in 0.4in 0">{BOOK['subtitle']}</p>
  <div style="display:flex;justify-content:center;gap:0.12in;margin-top:0.45in">{letters}</div>
  <div style="margin-top:0.55in;font:600 16pt 'Fredoka'">Written by {BOOK['author']}</div>
  <div class="muted" style="margin-top:4px">Illustrations: AI-assisted, edited by the author</div>
  <div style="margin:0.55in auto 0;width:1.25in">{mark_svg()}</div>
  <div style="font:600 13pt 'Fredoka';margin-top:4px">{BOOK['publisher']}</div>
  <div class="ar" style="font-size:14pt">{BOOK['publisher_ar']}</div>
</div>""", "front", number=False)

def copyright_page():
    isbn = f"<p><b>ISBN:</b> {BOOK['isbn']}</p>" if BOOK["isbn"] else ""
    add(f"""
<div style="position:absolute;bottom:0.2in;left:0;right:0;font-size:10.5pt;line-height:1.5">
  <p><b>{BOOK['title']}</b> — {BOOK['title_bn']}<br>{BOOK['series']}, Book {BOOK['series_no']}</p>
  <p>Text copyright © {BOOK['year']} {BOOK['author']}. All rights reserved.<br>
  No part of this book may be reproduced, stored or shared in any form without written permission
  from the publisher, except that parents and teachers may copy pages for use with their own children
  or class.</p>
  <p>Published by <b>{BOOK['publisher']}</b> ({BOOK['publisher_ar']}),<br>{BOOK['publisher_note']}, Bangladesh.<br>
  Contact: {BOOK['contact']}</p>
  {isbn}
  <p>First edition, {BOOK['year']}.</p>
  <p><b>Illustrations:</b> line art created with AI assistance and reviewed by the author. In keeping with
  the publisher’s guidelines, the pictures show objects, plants and nature only — no people or animals.</p>
  <p><b>Fonts:</b> Baloo Da 2, Noto Sans Bengali, Fredoka, Nunito, Amiri and Dancing Script, all under the
  SIL Open Font License. <b>Map data:</b> Natural Earth (public domain).</p>
  <p><b>A note of respect:</b> this book contains verses of the Noble Qur’an (pages 4–5).
  Please handle it with care and keep it in a clean place.</p>
</div>""", "front", number=False)

def belongs_page():
    add(f"""
<div class="dash" style="height:100%;padding:0.5in;text-align:center;position:relative">
  <div style="width:3in;margin:0.1in auto 0">{pic('lily')}</div>
  <h1 style="margin-top:0.25in">This book belongs to</h1>
  <div class="bnd" style="font-size:22pt;font-weight:700">এই বইটি যার</div>
  <div style="border-bottom:3px solid #111;height:0.9in;margin:0.3in 0.3in 0"></div>
  <p style="margin-top:0.35in;font-size:14pt">I started learning Bengali on</p>
  <div style="border-bottom:3px solid #111;height:0.5in;margin:0 1.2in"></div>
  <div style="display:flex;justify-content:space-around;margin-top:0.5in">
    <div style="width:1.3in">{pic('star')}</div><div style="width:1.3in">{pic('moon')}</div><div style="width:1.3in">{pic('flower')}</div>
  </div>
</div>""", "front")

def series_pages():
    add(f"""
<div style="text-align:center">
  <div class="chip">ABOUT THIS SERIES</div>
  <h1 style="margin-top:0.12in">The Allamahul Bayan Series</h1>
  <div class="ar" style="font-size:40pt;line-height:1.5;margin-top:0.05in">{BOOK['series_ar']}</div>
  <div class="tr" style="font-size:14pt">ʿallamahul-bayān — “He taught him clear expression”</div>
</div>
{ayah_box(AYAH_RAHMAN, ar_size=24)}
<p style="margin-top:0.15in">Surah Ar-Raḥmān — the chapter of <i>The Most Merciful</i> — opens by naming some of
Allah’s greatest gifts to us. First, <b>He taught the Qur’an</b>. Then, <b>He created the human being</b>.
And then, <b>He taught him al-bayān</b>.</p>
<p><b>What does <i>al-bayān</i> mean?</b> It comes from an Arabic root that means <i>to make something clear</i>.
Al-bayān is the gift of speech and understanding: being able to put what is in our hearts and minds into
words, to explain, to listen, and to be understood. Animals make sounds, but only people were taught to
speak, read and write in languages. Scholars of tafsīr explain that this gift is what lets us learn,
teach and pass on guidance — including the Qur’an itself.</p>
<p>So every time a child says a new word, sounds out a letter, or writes their first line in a new language,
they are using a gift that Allah Himself says He taught. That is the heart of this series:
<b>learning languages as a way of thanking Allah for al-bayān.</b></p>
""", "front")
    add(f"""
<h2>Languages and colours: two signs of Allah</h2>
{ayah_box(AYAH_RUM, ar_size=19)}
<p>In Surah Ar-Rūm, Allah tells us that the <b>many languages</b> of people and their <b>many colours</b> are
among His signs. A coloring book that teaches a language brings both of these signs together in a
child’s hands: they meet a new language, and they fill its letters with colour.</p>
{ayah_box(AYAH_HUJURAT, ar_size=19)}
<p>Allah made us into many peoples <i>so that we may get to know one another</i>. Learning even a few letters
of someone’s language is a beautiful first step towards knowing them.</p>
<h3 style="margin-top:0.1in">How each book in the series works</h3>
<p style="margin-bottom:0.04in">Every book introduces one language <b>through English</b>:</p>
<ul style="margin:0 0 0.1in 0.2in;padding-left:0.15in">
<li>where the language is spoken, with a map to color;</li>
<li>every letter of its alphabet, with its name in the language itself <i>and</i> in English letters;</li>
<li>simple English sound guides, so a parent who has never heard the language can still help;</li>
<li>a word and picture for every letter, to color, trace and say out loud.</li>
</ul>
<p><b>Book 1 is Bengali (Bangla)</b> — the language of Bangladesh, where this series was born.
More languages will follow, in shā’ Allāh.</p>
""", "front")

def parents_page():
    add(f"""
<div class="chip">FOR PARENTS AND TEACHERS</div>
<h2 style="margin-top:0.1in">How to use this book</h2>
<p>Begin with <b>Bismillah</b>, and go <b>little and often</b>: one letter a day is plenty for a young child.
For each letter:</p>
<ol style="margin:0 0 0.12in 0.2in;padding-left:0.15in">
<li><b>Say it.</b> Read the letter’s name and its sound guide together. Say it three times.</li>
<li><b>Color it.</b> Color the big letter any way your child likes.</li>
<li><b>Trace it.</b> Trace the dotted letters with a pencil, then try one alone in the empty boxes.</li>
<li><b>Meet the word.</b> Say the word, color the picture, and talk about it in English.</li>
</ol>
<div class="box" style="margin-bottom:0.14in"><b>Marker tip:</b> every coloring page has a blank back, so colours
cannot spoil the next activity. Slip a sheet of scrap paper behind the page you are coloring anyway —
it keeps the next page clean.</div>
<h3>Reading the English sound guides</h3>
<ul style="margin:0.05in 0 0.12in 0.2in;padding-left:0.15in">
<li><b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.</li>
<li><b>o</b> is the short, open sound in “on”. Every Bengali consonant carries it: ক = <i>ko</i>.</li>
<li><b>h after a letter</b> (<i>kh, gh, th, dh, bh</i>) means “add a puff of breath” — hold a tissue in front
of your mouth and watch it move! It never means the English “th” of “the”.</li>
<li><b>Hard and soft t / d:</b> Bengali has two of each. For the <i>hard</i> ones (ট ঠ ড ঢ) curl the tongue back;
for the <i>soft</i> ones (ত থ দ ধ) touch the back of your top teeth.</li>
</ul>
<h3>Three ways to see every sound</h3>
<p>Each letter page shows the sound three ways: the letter’s <b>Bengali name</b> written in Bengali
(native phonetics), the <b>same name in English letters</b>, and an <b>English sound guide</b>.
The box marked <i>Bengali phonetics</i> shows how the sound is built the way Bengali children learn it,
for example ক্ + অ = ক.</p>
<p class="small muted">The pronunciation guides are simplified for young learners and follow the standard
spoken Bengali of Bangladesh and West Bengal.</p>
""", "front")

def hello_page():
    add(f"""
<div class="chip">MEET THE LANGUAGE</div>
<h1 style="margin-top:0.1in">Hello, Bengali! <span class="bnd" style="font-weight:800">বাংলা</span></h1>
<p class="tr" style="font-size:14pt;margin-top:2px">baanglaa — the Bengali word for the language</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.14in;margin-top:0.18in">
 <div class="box"><h3>Who speaks it?</h3>About <b>270 million people</b> speak Bengali, also called
 <b>Bangla</b>. It is one of the ten most spoken languages in the world.<sup>³</sup></div>
 <div class="box"><h3>Where?</h3>It is the national language of <b>Bangladesh</b>. In <b>India</b> it is spoken in
 <b>West Bengal</b>, <b>Tripura</b> and the <b>Barak Valley of Assam</b>, and by families all over the world.</div>
 <div class="box"><h3>How is it written?</h3>In the <b>Bengali script</b>, from <b>left to right</b>, like English.
 Most letters hang from a line along the top called <span class="bn">মাত্রা</span> <i>(maatraa)</i>.</div>
 <div class="box"><h3>How many letters?</h3><b>50</b> letters: <b>11 vowels</b>
 (<span class="bn">স্বরবর্ণ</span> <i>shorobornno</i>) and <b>39 consonants</b>
 (<span class="bn">ব্যঞ্জনবর্ণ</span> <i>byanjonbornno</i>).</div>
 <div class="box"><h3>A day for languages</h3>On <b>21 February 1952</b>, students in Dhaka stood up for the right to
 use Bengali. Today the whole world remembers them on <b>International Mother Language Day</b>.<sup>³</sup></div>
 <div class="box"><h3>Did you know?</h3>Bangladesh has <b>six seasons</b>, its national flower is the
 water lily <span class="bn">শাপলা</span> <i>(shaaplaa)</i>, and it is home to one of the largest Muslim
 communities in the world.</div>
</div>
<div style="display:flex;justify-content:center;gap:0.4in;margin-top:0.22in">
 <div style="width:1.5in">{pic('lily')}</div><div style="width:1.5in">{pic('boat')}</div><div style="width:1.5in">{pic('flag')}</div>
</div>
""", "front")

def chart_page():
    def cells(items, cols):
        return (f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:5px">' +
                "".join(f'<div class="box" style="text-align:center;padding:2px 0">'
                        f'<div class="bnd" style="font-size:24pt;font-weight:800;line-height:1.25">{d["letter"]}</div>'
                        f'<div class="tr small" style="line-height:1.1;font-size:8.5pt">{d["name_en"]}</div></div>'
                        for d in items) + "</div>")
    add(f"""
<div class="chip">THE WHOLE ALPHABET</div>
<h2 style="margin-top:0.08in">The Bengali Alphabet <span class="bnd">বর্ণমালা</span></h2>
<h3 style="margin:0.1in 0 0.05in">11 vowels — <span class="bn">স্বরবর্ণ</span></h3>
{cells(VOWELS, 6)}
<h3 style="margin:0.14in 0 0.05in">39 consonants — <span class="bn">ব্যঞ্জনবর্ণ</span></h3>
{cells(CONSONANTS, 7)}
<p class="small muted" style="margin-top:0.1in">Read the alphabet left to right, row by row — the same order as in this book.</p>
""", "front")

def map_page():
    m = json.load(open(os.path.join(ROOT, "build", "map_paths.json")))
    pts = m["points"]
    def dot(name, label, dx=12, dy=5, anchor="start", starred=False, size=22):
        x, y = pts[name]
        mk = (f'<polygon points="{" ".join(f"{x+px:.1f},{y+py:.1f}" for px,py in _star(14))}" fill="#fff" stroke="#111" stroke-width="3"/>'
              if starred else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="#111" stroke-width="3"/>')
        return mk + (f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}" font-size="{size}" '
                     f'font-family="Fredoka" font-weight="600">{label}</text>')
    def lab(x, y, t, size=30, ital=False):
        x, y = round(x), round(y)
        st = ' font-style="italic"' if ital else ""
        return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-family="Fredoka" '
                f'font-weight="600" letter-spacing="3"{st}>{t}</text>')
    countries = "".join(
        f'<path d="{m[c]}" fill="#fff" stroke="#111" stroke-width="{6 if c=="Bangladesh" else 2.5}" stroke-linejoin="round"/>'
        for c in ["China", "Nepal", "Bhutan", "Myanmar", "India", "Bangladesh"])
    bx, by = pts["dhaka"]
    svgmap = (f'<svg viewBox="0 0 1000 1000" style="width:100%;height:100%"><rect width="1000" height="1000" fill="#fff"/>'
              f'<rect x="0" y="0" width="1000" height="1000" fill="none" stroke="#111" stroke-width="4"/>{countries}'
              + lab(*pts["bd_label"], "BANGLADESH", 34) + lab(*pts["india_label"], "INDIA", 34)
              + lab(*pts["myanmar_label"], "MYANMAR", 24) + lab(*pts["nepal_label"], "NEPAL", 22)
              + lab(*pts["bhutan_label"], "BHUTAN", 22) + lab(*pts["bay"], "Bay of Bengal", 34, True)
              + dot("dhaka", "Dhaka", 18, 8, starred=True, size=26) + dot("kolkata", "Kolkata", -14, 8, "end")
              + dot("agartala", "Agartala", 14, -10) + dot("silchar", "Silchar", -12, -10, "end")
              + lab(pts["wb_label"][0], pts["wb_label"][1], "WEST BENGAL", 20)
              + lab(*pts["tripura"], "TRIPURA", 18) + lab(*pts["barak"], "ASSAM", 18) + "</svg>")
    wx, wy = m["world_bd"]
    world = (f'<svg viewBox="0 0 400 210" style="width:100%"><rect width="400" height="210" fill="#fff" stroke="#111" stroke-width="2"/>'
             f'<path d="{m["world"]}" fill="#fff" stroke="#111" stroke-width="0.8"/>'
             f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="11" fill="none" stroke="#111" stroke-width="3"/></svg>')
    add(f"""
<div style="display:flex;justify-content:space-between;align-items:flex-end">
 <div><div class="chip">COLOR THE MAP</div>
 <h2 style="margin-top:0.08in">Where is Bengali spoken?</h2></div>
 <div style="width:2.2in">{world}<div class="small" style="text-align:center">The circle shows Bangladesh on the world map.</div></div>
</div>
<div style="height:6.15in;margin-top:0.12in">{svgmap}</div>
<div class="box" style="margin-top:0.12in;font-size:11.5pt">
<b>Color it:</b> Bangladesh <b>green</b> · India <b>orange</b> · the sea <b>blue</b> · the other countries any colour you like.
<b>Find it:</b> Dhaka ★ is the capital of Bangladesh. Bengali is also spoken around Kolkata (West Bengal),
Agartala (Tripura) and Silchar (Assam) in India.
</div>""", "coloring")

def _star(r):
    import math
    return [((r if i % 2 == 0 else r * .45) * math.cos(math.radians(-90 + 36 * i)),
             (r if i % 2 == 0 else r * .45) * math.sin(math.radians(-90 + 36 * i))) for i in range(10)]

# =========================================================================================
# SECTION INTROS + TRACING WARM-UPS
# =========================================================================================
def vowel_intro():
    rows = "".join(f'<tr><td class="bnd" style="font-size:22pt;font-weight:800">{v["letter"]}</td>'
                   f'<td class="tr">{v["name_en"]}</td>'
                   f'<td class="bn" style="font-size:16pt">{("◌" + v["sign"]) if v["sign"] else "—"}</td>'
                   f'<td class="bn" style="font-size:16pt">{v.get("example","ক")}</td>'
                   f'<td class="tr">{v.get("example_tr","ko")}</td></tr>' for v in VOWELS)
    add(f"""
<div class="chip">PART 1</div>
<h1 style="margin-top:0.1in">The Vowels <span class="bnd" style="font-weight:800">স্বরবর্ণ</span></h1>
<p class="tr" style="font-size:14pt">shorobornno — “voice letters”</p>
<p>Vowels are the sounds you make with your mouth open: <i>o, aa, i, ee, u, oo…</i> Bengali has <b>11 vowels</b>.</p>
<p>A vowel has <b>two shapes</b>. At the start of a word it is written as a full letter (<span class="bn">আ</span>).
After a consonant it becomes a small <b>vowel sign</b> (<span class="bn">◌া</span>) that holds on to the consonant:
<span class="bn">ক + া = কা</span> <i>(kaa)</i>. Some signs even sit in front of the letter they belong to!</p>
<table style="width:100%;border-collapse:collapse;margin-top:0.1in;text-align:center" class="vt">
<tr class="fd" style="font-size:10.5pt"><th>Vowel</th><th>Name</th><th>Sign</th><th>With ক</th><th>Say</th></tr>
{rows}</table>
<style>.vt td,.vt th{{border-bottom:1.5px solid #bbb;padding:2px 4px}}</style>
""", "content")

def warmup(letters, title, title_bn, cols):
    cells = "".join(f'<div class="box" style="padding:3px;aspect-ratio:1">{letter_svg(d["letter"], "trace", min_box=600)}</div>'
                    for d in letters)
    add(f"""
<div class="chip">PENCIL WARM-UP</div>
<h2 style="margin-top:0.08in">Trace {title} <span class="bnd">{title_bn}</span></h2>
<p>Use a <b>pencil</b>. Say each letter’s name as you trace it.</p>
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:0.1in;margin-top:0.12in">{cells}</div>
""", "content")

def consonant_intro():
    add(f"""
<div class="chip">PART 2</div>
<h1 style="margin-top:0.1in">The Consonants <span class="bnd" style="font-weight:800">ব্যঞ্জনবর্ণ</span></h1>
<p class="tr" style="font-size:14pt">byanjonbornno</p>
<p>Consonants are the sounds made by stopping or squeezing the air: <i>k, g, ch, j, t, d, p, b…</i>
Bengali has <b>39 consonants</b>.</p>
<div class="box" style="margin:0.12in 0"><h3>The hidden vowel</h3>
Every consonant secretly carries the vowel <span class="bn">অ</span> <i>(o)</i>. That is why
<span class="bn">ক</span> is said <i>ko</i>, not just <i>k</i>. Bengali children learn it like this:
<div class="bn" style="font-size:22pt;text-align:center;margin-top:4px">ক্ + অ = ক</div>
<div style="text-align:center"><i>k + o = ko</i> — the little mark <span class="bn">্</span> (<i>hoshonto</i>) means “no vowel”.</div></div>
<div class="box" style="margin:0.12in 0"><h3>Families of five</h3>
The first 25 consonants come in five families, each made in a different part of the mouth:
<div class="bn" style="font-size:17pt;line-height:1.6;margin-top:4px">
ক খ গ ঘ ঙ — <span class="small" style="font-family:Nunito">back of the throat</span><br>
চ ছ জ ঝ ঞ — <span class="small" style="font-family:Nunito">middle of the tongue</span><br>
ট ঠ ড ঢ ণ — <span class="small" style="font-family:Nunito">tongue curled back (hard)</span><br>
ত থ দ ধ ন — <span class="small" style="font-family:Nunito">tongue on the teeth (soft)</span><br>
প ফ ব ভ ম — <span class="small" style="font-family:Nunito">the lips</span></div></div>
<div class="box"><h3>The puff test</h3>
Hold a tissue in front of your mouth and say <span class="bn">ক</span> <i>(ko)</i>, then <span class="bn">খ</span>
<i>(kho)</i>. The tissue jumps for <span class="bn">খ</span>! An <i>h</i> in the sound guide means “add a puff”.</div>
""", "content")

# =========================================================================================
# LETTER PAGES
# =========================================================================================
def letter_page(d, idx, total, kind):
    is_v = kind == "vowel"
    head_l = f'{"VOWEL" if is_v else "CONSONANT"} {idx} OF {total}'
    head_r = f'{BOOK["series"]} · Bengali'
    if is_v:
        if d["sign"]:
            phon = (f'<div class="bn" style="font-size:17pt">◌{d["sign"]} <span class="small" style="font-family:Nunito">'
                    f'({d["sign_name"]})</span></div>'
                    f'<div class="bn" style="font-size:17pt">ক + ◌{d["sign"]} = {d["example"]} '
                    f'<span class="tr" style="font-family:Nunito;font-size:12pt">({d["example_tr"]})</span></div>')
        else:
            phon = f'<div style="font-size:11.5pt"><span class="bn">{d["sign_note"]}</span></div>'
        phon_lbl = "Bengali phonetics · vowel sign"
    else:
        phon = f'<div class="bn" style="font-size:19pt">{d["breakdown"]}</div>'
        phon_lbl = "Bengali phonetics · উচ্চারণ"
    pos = ""
    if d.get("pos") == "middle":
        pos = f'<div class="small">{d["letter"]} likes the middle of words — can you find it in <span class="bn">{d["word"]}</span>?</div>'
    elif d.get("pos") == "end":
        pos = f'<div class="small">Look for {d["letter"]} at the end of <span class="bn">{d["word"]}</span>!</div>'
    trace = "".join(f'<div class="cell">{letter_svg(d["letter"], "trace", min_box=600)}</div>' for _ in range(4))
    trace += '<div class="free"></div><div class="free"></div>'
    add(f"""
{head(head_l, head_r)}
<div class="lp-top">
  <div class="lp-letter frame">{letter_svg(d['letter'], 'color', min_box=480, pad=0.06)}</div>
  <div class="lp-info">
    <div class="box"><div class="lbl">Name · নাম</div>
      <div class="lp-name">{d['name_bn']}</div>
      <div class="tr" style="font-size:15pt">{d['name_en']}</div></div>
    <div class="box"><div class="lbl">Say it · English sound guide</div>
      <div style="font-size:13pt;line-height:1.3">{d['sound']}</div></div>
    <div class="box" style="flex:1"><div class="lbl">{phon_lbl}</div>{phon}{pos}</div>
  </div>
</div>
<div class="lp-pic frame">
  {pic(d['pic'])}
  <div class="lp-word">
    <div class="lbl">{d['letter']} is for</div>
    <div class="w">{d['word']}</div>
    <div class="t">{d['translit']}</div>
    <div class="m">{d['meaning']}</div>
    <div class="small muted" style="margin-top:0.12in">Color the picture and say the word three times!</div>
  </div>
</div>
<div class="lp-trace box">
  <div class="lbl">Trace it with a pencil, then write it on your own · লেখো</div>
  <div class="trow">{trace}</div>
</div>""", "coloring")

# =========================================================================================
# BACK MATTER
# =========================================================================================
def digits_page():
    cells = "".join(f'<div class="box" style="display:flex;align-items:center;gap:0.1in;padding:0.05in 0.12in">'
                    f'<div style="width:1.25in;height:1.25in">{letter_svg(n, "color", min_box=560)}</div>'
                    f'<div><div style="font:600 22pt Fredoka">{i}</div><div class="bnd" style="font-size:18pt;font-weight:700">{bn}</div>'
                    f'<div class="tr">{tr}</div><div class="small">{en}</div></div></div>'
                    for i, (n, bn, tr, en) in enumerate(DIGITS))
    add(f"""
<div class="chip">BONUS</div>
<h2 style="margin-top:0.08in">Bengali numbers <span class="bnd">সংখ্যা</span> <span class="tr" style="font-size:14pt">(shongkhaa)</span></h2>
<p>Color the numbers and count out loud in Bengali: <i>shunno, ek, dui, tin…</i></p>
<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:0.08in">{cells}</div>
""", "coloring")

def phrases_page():
    rows = "".join(f'<div class="box" style="display:flex;justify-content:space-between;align-items:center;gap:0.2in">'
                   f'<div class="bnd" style="font-size:19pt;font-weight:700;line-height:1.3">{bn}</div>'
                   f'<div style="text-align:right"><div class="tr">{tr}</div><div class="small"><b>{en}</b></div></div></div>'
                   for bn, tr, en in PHRASES)
    add(f"""
<div class="chip">LET'S TALK</div>
<h2 style="margin-top:0.08in">My first Bengali words <span class="bnd">প্রথম কথা</span></h2>
<p>Now that you know the letters, try saying these with your family.</p>
<div class="grid" style="margin-top:0.08in">{rows}</div>
<div style="display:flex;justify-content:center;gap:0.35in;margin-top:0.3in">
<div style="width:1.35in">{pic('mosque')}</div><div style="width:1.35in">{pic('rice')}</div><div style="width:1.35in">{pic('gift')}</div></div>
""", "content")

def references_page():
    add(f"""
<div class="chip">REFERENCES & SOURCES</div>
<h2 style="margin-top:0.08in">Where our facts come from</h2>
<p><sup>¹</sup> <b>The Noble Qur’an</b> — Surah Ar-Raḥmān 55:1–4, Surah Ar-Rūm 30:22 and Surah Al-Ḥujurāt 49:13.
Arabic text and meanings checked against <b>Quran.com</b>; the English meanings in this book are simplified
for children.</p>
<p><sup>²</sup> <b>Map</b> — country outlines from <b>Natural Earth</b> (public domain), via the <i>world-atlas</i> data set.</p>
<p><sup>³</sup> <b>Language facts</b> — speaker numbers from <b>Ethnologue</b> (SIL International);
International Mother Language Day from <b>UNESCO</b>.</p>
<div class="box" style="margin-top:0.25in"><h3>What’s next?</h3>
You have met all <b>50 Bengali letters</b>! Keep practising by reading signs, books and food packets
written in Bengali, and look out for the next book in the <b>Allamahul Bayan Series</b>, in shā’ Allāh.</div>
<div class="box" style="margin-top:0.15in"><h3>Enjoyed this book?</h3>
A short review on Amazon helps other families find it — <i>jazākumullāhu khayran!</i></div>
<div style="display:flex;justify-content:center;gap:0.3in;margin-top:0.3in">
<div style="width:1.4in">{pic('book')}</div><div style="width:1.4in">{pic('palette')}</div></div>
""", "content")

def certificate_page():
    add(f"""
<div class="frame" style="height:100%;padding:0.18in;border-width:5px">
<div class="dash" style="height:100%;padding:0.35in 0.4in;text-align:center;position:relative">
  <div style="display:flex;justify-content:center;gap:0.3in"><div style="width:0.75in">{pic('star')}</div><div style="width:0.75in">{pic('moon')}</div><div style="width:0.75in">{pic('star')}</div></div>
  <h1 style="font-size:34pt;margin-top:0.1in">Certificate of Achievement</h1>
  <div class="bnd" style="font-size:24pt;font-weight:800">মাশাআল্লাহ! খুব ভালো!</div>
  <div class="tr">maashaa-allaah! khub bhaalo! — Well done, very good!</div>
  <p style="margin-top:0.3in;font-size:15pt">This certifies that</p>
  <div style="border-bottom:3px solid #111;height:0.6in;margin:0 0.5in"></div>
  <p style="margin-top:0.25in;font-size:14pt">has learned, traced and colored<br><b>all 50 letters of the Bengali alphabet</b>.</p>
  <div style="display:flex;justify-content:space-between;margin-top:0.55in;padding:0 0.2in;text-align:center">
    <div style="width:2.3in"><div style="border-bottom:2px solid #111;height:0.45in"></div><div class="small">Date</div></div>
    <div style="width:2.3in"><div style="border-bottom:2px solid #111;height:0.45in"></div><div class="small">Grown-up’s signature</div></div>
  </div>
  <div style="margin-top:0.35in"><div style="font:700 26pt 'Dancing Script'">Minhaz Reza</div>
    <div class="small">{BOOK['author']}, author</div></div>
  <div style="display:flex;align-items:center;justify-content:center;gap:0.15in;margin-top:0.2in">
    <div style="width:0.7in">{mark_svg()}</div>
    <div style="text-align:left" class="small"><b>{BOOK['publisher']}</b> — Publisher<br>{BOOK['publisher_note']}<br>
    <span class="ar" style="font-size:12pt">{BOOK['publisher_ar']}</span></div></div>
  <div class="small muted" style="position:absolute;bottom:0.12in;left:0;right:0">✂ Cut out and frame it — the back of this page is blank.</div>
</div></div>""", "coloring", number=False)

# =========================================================================================
def build():
    title_page(); copyright_page(); belongs_page()
    series_pages()                      # p4-5 (a spread)
    parents_page(); hello_page()        # p6, p7
    chart_page()                        # p8
    map_page(); blank()                 # p9 color, p10 back
    vowel_intro(); warmup(VOWELS, "the vowels", "স্বরবর্ণ", 4)   # p11, p12 (pencil)
    for i, v in enumerate(VOWELS, 1):
        letter_page(v, i, len(VOWELS), "vowel"); blank()
    consonant_intro(); warmup(CONSONANTS, "the consonants", "ব্যঞ্জনবর্ণ", 6)
    for i, c in enumerate(CONSONANTS, 1):
        letter_page(c, i, len(CONSONANTS), "consonant"); blank()
    digits_page(); blank()
    phrases_page(); references_page()
    certificate_page(); blank(note=False)

    # ---- layout guarantees ----
    n = len(pages)
    for i, p in enumerate(pages, 1):
        if p["kind"] == "coloring":
            assert i % 2 == 1, f"coloring page {i} must be a right-hand (odd) page"
            assert i == n or pages[i]["kind"] == "blank", f"coloring page {i} needs a blank back"
    assert pages[3]["kind"] == "front" and pages[4]["kind"] == "front"   # series spread p4-5
    assert n % 2 == 0 and 24 <= n <= 828, n

    body = []
    for i, p in enumerate(pages, 1):
        side = "odd" if i % 2 else "even"
        pno = f'<div class="pno">{i}</div>' if p["number"] and p["kind"] != "blank" else ""
        body.append(f'<section class="page {side}"><div class="inner">{p["html"]}</div>{pno}</section>')
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{BOOK["title"]} — interior</title>'
            f'<style>{CSS}</style></head><body>{"".join(body)}</body></html>')
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    open(os.path.join(ROOT, "build", "interior.html"), "w", encoding="utf-8").write(html)
    json.dump({"pages": n}, open(os.path.join(ROOT, "build", "pagecount.json"), "w"))
    print(f"interior: {n} pages")

if __name__ == "__main__":
    build()
