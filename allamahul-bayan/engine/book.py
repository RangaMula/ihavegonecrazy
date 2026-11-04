# -*- coding: utf-8 -*-
"""Allamahul Bayan Series - generic interior builder (any language file in ../languages/).

Trim 8.5 x 11 in, no bleed, black & white. Every coloring page sits on a right-hand (odd) page
with a blank back, so markers never bleed onto another activity.
"""
import json, math, os
from illos import svg as _pic
from glyphs import letter_svg as _letter
from brand import mark_svg
from series import SERIES, AYAH_RAHMAN, AYAH_RUM, AYAH_HUJURAT

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FONTS = "../../fonts/"

FONT_FACES = [  # family, weight, style, file, unicode-range
    ("Fredoka", 400, "normal", "fredoka-latin-400-normal.woff2", None),
    ("Fredoka", 600, "normal", "fredoka-latin-600-normal.woff2", None),
    ("Nunito", 400, "normal", "nunito-latin-400-normal.woff2", None),
    ("Nunito", 400, "normal", "nunito-latin-ext-400-normal.woff2", "U+0100-024F,U+1E00-1EFF,U+02BB-02BF"),
    ("Nunito", 700, "normal", "nunito-latin-700-normal.woff2", None),
    ("Nunito", 700, "normal", "nunito-latin-ext-700-normal.woff2", "U+0100-024F,U+1E00-1EFF,U+02BB-02BF"),
    ("Nunito", 800, "normal", "nunito-latin-800-normal.woff2", None),
    ("Nunito", 400, "italic", "nunito-latin-400-italic.woff2", None),
    ("Amiri", 400, "normal", "amiri-arabic-400-normal.woff2", None),
    ("Amiri", 700, "normal", "amiri-arabic-700-normal.woff2", None),
    ("Dancing Script", 700, "normal", "dancing-script-latin-700-normal.woff2", None),
]

def font_css(L):
    faces = FONT_FACES + L["fonts"]
    out = []
    for fam, w, st, f, rng in faces:
        r = f";unicode-range:{rng}" if rng else ""
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url({FONTS}{f}){r}}}")
    return "\n".join(out)

def base_css(L):
    D, T = L["disp_family"], L["text_family"]
    rtl = L.get("dir") == "rtl"
    return f"""
{font_css(L)}
@page {{ size: 8.5in 11in; margin: 0 }}
* {{ box-sizing: border-box }}
html,body {{ margin:0; padding:0; background:#fff; color:#111 }}
body {{ font-family:'Nunito','{T}',sans-serif; font-size:13pt; line-height:1.4 }}
.nt {{ font-family:'{T}','Nunito',sans-serif; {'direction:rtl;unicode-bidi:isolate;' if rtl else ''} }}
.ntd {{ font-family:'{D}','{T}',sans-serif; font-weight:800; {'direction:rtl;unicode-bidi:isolate;' if rtl else ''} }}
.ar {{ font-family:'Amiri',serif; direction:rtl }}
.tr {{ font-style:italic }}
.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always;
        padding:0.6in 0.6in 0.62in 0.8in }}
.page.even {{ padding:0.6in 0.8in 0.62in 0.6in }}
.inner {{ position:relative; width:100%; height:100% }}
.pno {{ position:absolute; bottom:0.3in; width:7.1in; text-align:center; font:600 10pt 'Fredoka',sans-serif; color:#555 }}
.page .pno {{ left:0.8in }} .page.even .pno {{ left:0.6in }}
h1,h2,h3 {{ font-family:'Fredoka','{D}',sans-serif; font-weight:600; margin:0 }}
h1 {{ font-size:30pt; line-height:1.15 }}
h2 {{ font-size:22pt; line-height:1.2 }}
h3 {{ font-size:14pt }}
p {{ margin:0 0 0.12in }}
.frame {{ border:3px solid #111; border-radius:22px }}
.dash {{ border:2.5px dashed #111; border-radius:18px }}
.chip {{ display:inline-block; border:2px solid #111; border-radius:999px; padding:1px 12px; font:600 11pt 'Fredoka','{T}',sans-serif }}
.muted {{ color:#444 }}
.small {{ font-size:10.5pt }}
.ill {{ display:block }}
.ill * {{ stroke:#111; stroke-width:3.2; stroke-linejoin:round; stroke-linecap:round }}
.ill .a,.ill .b,.ill .c,.ill .d,.ill .e {{ fill:#fff }}
.ill .n {{ fill:none }} .ill .t {{ stroke-width:2 }}
.ill text {{ font-family:'{D}','{T}',sans-serif; font-weight:800; fill:#fff; stroke-width:2.4 }}
.ill text.blk {{ stroke-width:2 }}
.ill text.lbl {{ font-weight:700; fill:#111; stroke:none }}
.glyph {{ display:block; width:100%; height:100% }}
.lp-head {{ display:flex; justify-content:space-between; align-items:center; height:0.42in }}
.lp-top {{ display:flex; gap:0.18in; height:4.05in; margin-top:0.08in }}
.lp-letter {{ width:3.95in; height:4.05in; padding:0.12in; position:relative }}
.lp-info {{ flex:1; display:flex; flex-direction:column; gap:0.09in }}
.box {{ border:2px solid #111; border-radius:14px; padding:0.07in 0.13in }}
.lbl {{ font:600 9pt 'Fredoka','{T}',sans-serif; text-transform:uppercase; letter-spacing:.06em; color:#333 }}
.lp-name {{ font:700 22pt '{T}',sans-serif; line-height:1.35 }}
.lp-pic {{ display:flex; gap:0.15in; height:3.15in; margin-top:0.16in; padding:0.1in 0.18in; align-items:center }}
.lp-pic .ill {{ width:2.9in; height:2.9in }}
.lp-word {{ flex:1; text-align:center }}
.lp-word .w {{ font-size:40pt; line-height:1.35 }}
.lp-word .t {{ font:italic 400 17pt 'Nunito',sans-serif }}
.lp-word .m {{ font:700 16pt 'Nunito',sans-serif; margin-top:2px }}
.lp-trace {{ margin-top:0.16in; height:1.42in; padding:0.06in 0.15in }}
.trow {{ display:flex; gap:0.08in; align-items:center; height:1.0in; border-top:1.5px solid #bbb; border-bottom:1.5px solid #bbb; margin-top:0.04in; {'flex-direction:row-reverse;' if rtl else ''} }}
.trow .cell {{ width:0.98in; height:0.98in }}
.trow .free {{ width:0.98in; height:0.86in; border:2px dashed #999; border-radius:10px }}
.blankmsg {{ position:absolute; bottom:0.25in; width:100%; text-align:center; font:400 8.5pt 'Nunito',sans-serif; color:#777 }}
.grid {{ display:grid; gap:0.12in }}
ul,ol {{ margin:0 0 0.12in 0.2in; padding-left:0.15in }}
{L.get("extra_css", "")}
"""


class Book:
    def __init__(self, L):
        self.L = L
        self.pages = []
        self.font = L["glyph_font"]

    # ---------- helpers ----------
    def pic(self, key, **args):
        return _pic(key, **args)

    def glyph(self, text, mode="color", **kw):
        return _letter(text, self.font, mode, **kw)

    def add(self, html, kind="content", number=True):
        self.pages.append(dict(html=html, kind=kind, number=number))

    def blank(self, note=True):
        msg = ('<div class="blankmsg">This page is left blank on purpose, so your colours don’t '
               'bleed through. ✿</div>') if note else ""
        self.add(msg, "blank", number=False)

    def ayah_box(self, a, sup="¹", ar_size=21):
        return (f'<div class="frame" style="padding:0.12in 0.2in;margin:0.1in 0">'
                f'<div class="ar" style="font-size:{ar_size}pt;line-height:1.9;text-align:center">{a["ar"]}</div>'
                f'<div class="tr small" style="text-align:center;margin-top:2px">{a["tr"]}</div>'
                f'<div style="text-align:center;margin-top:4px">“{a["en"]}”</div>'
                f'<div style="text-align:center;margin-top:5px"><span class="chip" style="font-size:9.5pt">{a["ref"]}<sup>{sup}</sup></span></div>'
                f'</div>')

    # ---------- front matter ----------
    def title_page(self):
        L = self.L
        letters = "".join(f'<div style="width:0.95in;height:0.95in">{self.glyph(c, min_box=700)}</div>' for c in L["title_letters"])
        self.add(f"""
<div style="text-align:center;padding-top:0.15in">
  <div class="chip">{SERIES['name'].upper()} · BOOK {L['series_no']}</div>
  <div class="ar" style="font-size:22pt;margin-top:0.08in">{SERIES['ar']}</div>
  <h1 style="font-size:40pt;margin-top:0.25in">{L['title']}</h1>
  <div class="ntd" style="font-size:30pt;margin-top:0.08in;line-height:1.5">{L['title_native']}</div>
  <p style="font-size:14pt;margin:0.2in 0.4in 0">{L['subtitle']}</p>
  <div style="display:flex;justify-content:center;gap:0.12in;margin-top:0.4in;{'flex-direction:row-reverse;' if L.get('dir')=='rtl' else ''}">{letters}</div>
  <div style="margin-top:0.5in;font:600 16pt 'Fredoka'">Written by {SERIES['author']}</div>
  <div class="muted" style="margin-top:4px">Illustrations: AI-assisted, edited by the author</div>
  <div style="margin:0.5in auto 0;width:1.25in">{mark_svg()}</div>
  <div style="font:600 13pt 'Fredoka';margin-top:4px">{SERIES['publisher']}</div>
  <div class="ar" style="font-size:14pt">{SERIES['publisher_ar']}</div>
</div>""", "front", number=False)

    def copyright_page(self):
        L, S = self.L, SERIES
        isbn = f"<p><b>ISBN:</b> {L['isbn']}</p>" if L.get("isbn") else ""
        self.add(f"""
<div style="position:absolute;bottom:0.2in;left:0;right:0;font-size:10.5pt;line-height:1.5">
  <p><b>{L['title']}</b> — <span class="nt">{L['title_native']}</span><br>{S['name']}, Book {L['series_no']}</p>
  <p>Text copyright © {S['year']} {S['author']}. All rights reserved.<br>
  No part of this book may be reproduced, stored or shared in any form without written permission
  from the publisher, except that parents and teachers may copy pages for use with their own children
  or class.</p>
  <p>Published by <b>{S['publisher']}</b> ({S['publisher_ar']}),<br>{S['publisher_note']}, Bangladesh.<br>
  Contact: {S['contact']}</p>
  {isbn}
  <p>First edition, {S['year']}.</p>
  <p><b>Illustrations:</b> line art created with AI assistance and reviewed by the author. In keeping with
  the publisher’s guidelines, the pictures show objects, plants and nature only — no people or animals.</p>
  <p><b>Fonts:</b> {L['font_credit']}, Fredoka, Nunito, Amiri and Dancing Script, all under the
  SIL Open Font License. <b>Map data:</b> Natural Earth (public domain).</p>
  <p><b>A note of respect:</b> this book contains verses of the Noble Qur’an (pages 4–5).
  Please handle it with care and keep it in a clean place.</p>
</div>""", "front", number=False)

    def belongs_page(self):
        L = self.L
        self.add(f"""
<div class="dash" style="height:100%;padding:0.5in;text-align:center;position:relative">
  <div style="width:3in;margin:0.1in auto 0">{self.pic(L['belongs_pic'])}</div>
  <h1 style="margin-top:0.25in">This book belongs to</h1>
  <div class="ntd" style="font-size:22pt;line-height:1.5">{L['belongs_native']}</div>
  <div style="border-bottom:3px solid #111;height:0.9in;margin:0.3in 0.3in 0"></div>
  <p style="margin-top:0.35in;font-size:14pt">I started learning {L['name']} on</p>
  <div style="border-bottom:3px solid #111;height:0.5in;margin:0 1.2in"></div>
  <div style="display:flex;justify-content:space-around;margin-top:0.5in">
    <div style="width:1.3in">{self.pic('star')}</div><div style="width:1.3in">{self.pic('moon')}</div><div style="width:1.3in">{self.pic('flower')}</div>
  </div>
</div>""", "front")

    def series_pages(self):
        L = self.L
        self.add(f"""
<div style="text-align:center">
  <div class="chip">ABOUT THIS SERIES</div>
  <h1 style="margin-top:0.12in">The Allamahul Bayan Series</h1>
  <div class="ar" style="font-size:40pt;line-height:1.5;margin-top:0.05in">{SERIES['ar']}</div>
  <div class="tr" style="font-size:14pt">ʿallamahul-bayān — “He taught him clear expression”</div>
</div>
{self.ayah_box(AYAH_RAHMAN, ar_size=24)}
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
        self.add(f"""
<h2>Languages and colours: two signs of Allah</h2>
{self.ayah_box(AYAH_RUM, ar_size=19)}
<p>In Surah Ar-Rūm, Allah tells us that the <b>many languages</b> of people and their <b>many colours</b> are
among His signs. A coloring book that teaches a language brings both of these signs together in a
child’s hands: they meet a new language, and they fill its letters with colour.</p>
{self.ayah_box(AYAH_HUJURAT, ar_size=19)}
<p>Allah made us into many peoples <i>so that we may get to know one another</i>. Learning even a few letters
of someone’s language is a beautiful first step towards knowing them.</p>
<h3 style="margin-top:0.1in">How each book in the series works</h3>
<p style="margin-bottom:0.04in">Every book introduces one language <b>through English</b>:</p>
<ul>
<li>where the language is spoken, with a map to color;</li>
<li>every letter of its alphabet, with its name in the language itself <i>and</i> in English letters;</li>
<li>simple English sound guides, so a parent who has never heard the language can still help;</li>
<li>a word and picture for every letter, to color, trace and say out loud.</li>
</ul>
<p>{L['series_line']}</p>
""", "front")

    def parents_page(self):
        L = self.L
        bullets = "".join(f"<li>{b}</li>" for b in L["sound_notes"])
        self.add(f"""
<div class="chip">FOR PARENTS AND TEACHERS</div>
<h2 style="margin-top:0.1in">How to use this book</h2>
<p>Begin with <b>Bismillah</b>, and go <b>little and often</b>: one letter a day is plenty for a young child.
For each letter:</p>
<ol>
<li><b>Say it.</b> Read the letter’s name and its sound guide together. Say it three times.</li>
<li><b>Color it.</b> Color the big letter any way your child likes.</li>
<li><b>Trace it.</b> Trace the dotted letters with a pencil, then try one alone in the empty boxes.</li>
<li><b>Meet the word.</b> Say the word, color the picture, and talk about it in English.</li>
</ol>
<div class="box" style="margin-bottom:0.14in"><b>Marker tip:</b> every coloring page has a blank back, so colours
cannot spoil the next activity. Slip a sheet of scrap paper behind the page you are coloring anyway —
it keeps the next page clean.</div>
<h3>Reading the English sound guides</h3>
<ul style="margin-top:0.05in">{bullets}</ul>
<h3>Three ways to see every sound</h3>
<p>Each letter page shows the sound three ways: the letter’s <b>{L['name']} name</b> written in {L['name']}
(native phonetics), the <b>same name in English letters</b>, and an <b>English sound guide</b>.
{L['phon_explain']}</p>
<p class="small muted">The pronunciation guides are simplified for young learners and follow {L['standard']}.</p>
""", "front")

    def hello_page(self):
        L = self.L
        boxes = "".join(f'<div class="box"><h3>{t}</h3>{h}</div>' for t, h in L["hello"])
        pics = "".join(f'<div style="width:1.5in">{self.pic(k, **a)}</div>' for k, a in L["hello_pics"])
        self.add(f"""
<div class="chip">MEET THE LANGUAGE</div>
<h1 style="margin-top:0.1in">Hello, {L['name']}! <span class="ntd">{L['native']}</span></h1>
<p class="tr" style="font-size:14pt;margin-top:2px">{L['native_tr']} — the {L['name']} word for the language</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.14in;margin-top:0.18in">{boxes}</div>
<div style="display:flex;justify-content:center;gap:0.4in;margin-top:0.22in">{pics}</div>
""", "front")

    def chart_page(self):
        L = self.L
        n_total = sum(len(s["items"]) for s in L["sections"])
        big = n_total <= 45
        def cells(items, cols):
            fs = 24 if big else 21
            return (f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:5px;{"direction:rtl;" if L.get("dir")=="rtl" else ""}">' +
                    "".join(f'<div class="box" style="text-align:center;padding:2px 0">'
                            f'<div class="ntd" style="font-size:{fs}pt;line-height:1.35">{d["letter"]}</div>'
                            f'<div class="tr small" style="line-height:1.1;font-size:8.5pt;direction:ltr">{d["name_en"]}</div></div>'
                            for d in items) + "</div>")
        body = "".join(f'<h3 style="margin:0.12in 0 0.05in">{len(s["items"])} {s["chart_title"]} — <span class="nt">{s["native"]}</span></h3>'
                       f'{cells(s["items"], s["chart_cols"])}' for s in L["sections"])
        self.add(f"""
<div class="chip">THE WHOLE ALPHABET</div>
<h2 style="margin-top:0.08in">The {L['name']} Alphabet <span class="ntd">{L['alphabet_native']}</span></h2>
{body}
<p class="small muted" style="margin-top:0.1in">{L['chart_note']}</p>
""", "front")

    def map_page(self):
        L, M = self.L, self.L["map"]
        m = json.load(open(os.path.join(ROOT, "build", L["code"], "map_paths.json")))
        pts = m["points"]
        def star(x, y, r=14):
            return " ".join(f"{x+(r if i%2==0 else r*.45)*math.cos(math.radians(-90+36*i)):.1f},"
                            f"{y+(r if i%2==0 else r*.45)*math.sin(math.radians(-90+36*i)):.1f}" for i in range(10))
        out = []
        if m.get("land"):
            out.append(f'<path d="{m["land"]}" fill="#fff" stroke="#111" stroke-width="3" stroke-linejoin="round"/>')
        for c, d in m.get("countries", {}).items():
            out.append(f'<path d="{d}" fill="#fff" stroke="#111" stroke-width="{6 if c == M.get("bold") else 2.5}" stroke-linejoin="round"/>')
        for key, rx, ry, rot in M.get("areas", []):
            x, y = pts[key]
            out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" transform="rotate({rot} {x:.1f} {y:.1f})" '
                       f'fill="none" stroke="#111" stroke-width="5" stroke-dasharray="18 12"/>')
        for key, label, dx, dy, anchor, starred in M["cities"]:
            x, y = pts[key]
            mk = (f'<polygon points="{star(x, y)}" fill="#fff" stroke="#111" stroke-width="3"/>' if starred
                  else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="#111" stroke-width="3"/>')
            out.append(mk + f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}" font-size="24" '
                            f'font-family="Fredoka" font-weight="600" paint-order="stroke" stroke="#fff" stroke-width="6">{label}</text>')
        for key, text, size, ital in M["labels"]:
            x, y = pts[key]
            st = ' font-style="italic"' if ital else ""
            out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-size="{size}" font-family="Fredoka" '
                       f'font-weight="600" letter-spacing="3"{st} paint-order="stroke" stroke="#fff" stroke-width="6">{text}</text>')
        svgmap = (f'<svg viewBox="0 0 1000 1000" style="width:100%;height:100%"><rect width="1000" height="1000" fill="#fff"/>'
                  + "".join(out) + '<rect width="1000" height="1000" fill="none" stroke="#111" stroke-width="4"/></svg>')
        wx, wy = m["world_marker"]
        world = (f'<svg viewBox="0 0 400 210" style="width:100%"><rect width="400" height="210" fill="#fff" stroke="#111" stroke-width="2"/>'
                 f'<path d="{m["world"]}" fill="#fff" stroke="#111" stroke-width="0.8"/>'
                 f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="{M.get("world_r", 11)}" fill="none" stroke="#111" stroke-width="3"/></svg>')
        self.add(f"""
<div style="display:flex;justify-content:space-between;align-items:flex-end">
 <div><div class="chip">COLOR THE MAP</div>
 <h2 style="margin-top:0.08in">Where is {L['name']} spoken?</h2></div>
 <div style="width:2.2in">{world}<div class="small" style="text-align:center">{M['world_caption']}</div></div>
</div>
<div style="height:6.15in;margin-top:0.12in">{svgmap}</div>
<div class="box" style="margin-top:0.12in;font-size:11.5pt">{M['legend']}</div>""", "coloring")

    # ---------- sections ----------
    def section_intro(self, s):
        self.add(f'<div class="chip">{s["chip"]}</div>'
                 f'<h1 style="margin-top:0.1in">{s["title"]} <span class="ntd">{s["native"]}</span></h1>'
                 f'<p class="tr" style="font-size:14pt">{s["native_tr"]}</p>{s["intro_html"]}', "content")

    def warmup(self, s):
        cols = s["warmup_cols"]
        cells = "".join(f'<div class="box" style="padding:3px;aspect-ratio:1">{self.glyph(d["letter"], "trace", min_box=600)}</div>'
                        for d in s["items"])
        self.add(f"""
<div class="chip">PENCIL WARM-UP</div>
<h2 style="margin-top:0.08in">Trace {s['warmup_title']} <span class="ntd">{s['native']}</span></h2>
<p>Use a <b>pencil</b>. Say each letter’s name as you trace it.</p>
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:0.1in;margin-top:0.12in;{'direction:rtl;' if self.L.get('dir')=='rtl' else ''}">{cells}</div>
""", "content")

    def letter_page(self, d, idx, total, label):
        L = self.L
        trace = "".join(f'<div class="cell">{self.glyph(d["letter"], "trace", min_box=600)}</div>' for _ in range(4))
        trace += '<div class="free"></div><div class="free"></div>'
        note = f'<div class="small" style="margin-top:4px">{d["note"]}</div>' if d.get("note") else ""
        self.add(f"""
<div class="lp-head"><span class="chip">{label} {idx} OF {total}</span>
<span class="small muted" style="font-family:Fredoka">{SERIES['name']} · {L['name']}</span></div>
<div class="lp-top">
  <div class="lp-letter frame">{self.glyph(d['letter'], min_box=480, pad=0.06)}</div>
  <div class="lp-info">
    <div class="box"><div class="lbl">Name · {L['name_word']}</div>
      <div class="lp-name nt">{d['name_native']}</div>
      <div class="tr" style="font-size:15pt">{d['name_en']}</div></div>
    <div class="box"><div class="lbl">Say it · English sound guide</div>
      <div style="font-size:13pt;line-height:1.3">{d['sound']}</div></div>
    <div class="box" style="flex:1"><div class="lbl">{d['phon_label']}</div>{d['phon']}{note}</div>
  </div>
</div>
<div class="lp-pic frame">
  {self.pic(d['pic'], **d.get('pic_args', {}))}
  <div class="lp-word">
    <div class="lbl"><span class="nt">{d['letter']}</span> is for</div>
    <div class="w ntd">{d['word']}</div>
    <div class="t">{d['translit']}</div>
    <div class="m">{d['meaning']}</div>
    <div class="small muted" style="margin-top:0.12in">Color the picture and say the word three times!</div>
  </div>
</div>
<div class="lp-trace box">
  <div class="lbl">Trace it with a pencil, then write it on your own · {L['write_word']}</div>
  <div class="trow">{trace}</div>
</div>""", "coloring")

    # ---------- back matter ----------
    def digits_page(self):
        L = self.L
        cells = "".join(f'<div class="box" style="display:flex;align-items:center;gap:0.1in;padding:0.05in 0.12in">'
                        f'<div style="width:1.25in;height:1.25in">{self.glyph(n, min_box=560)}</div>'
                        f'<div><div style="font:600 22pt Fredoka">{i}</div><div class="ntd" style="font-size:18pt;line-height:1.4">{w}</div>'
                        f'<div class="tr">{tr}</div><div class="small">{en}</div></div></div>'
                        for i, (n, w, tr, en) in enumerate(L["digits"]))
        self.add(f"""
<div class="chip">BONUS</div>
<h2 style="margin-top:0.08in">{L['name']} numbers <span class="ntd">{L['numbers_native']}</span> <span class="tr" style="font-size:14pt">({L['numbers_tr']})</span></h2>
<p>Color the numbers and count out loud in {L['name']}: <i>{', '.join(t for _, _, t, _ in L['digits'][:4])}…</i></p>
<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:0.08in">{cells}</div>
""", "coloring")

    def phrases_page(self):
        L = self.L
        rows = "".join(f'<div class="box" style="display:flex;justify-content:space-between;align-items:center;gap:0.2in">'
                       f'<div class="ntd" style="font-size:19pt;font-weight:700;line-height:1.45">{w}</div>'
                       f'<div style="text-align:right"><div class="tr">{tr}</div><div class="small"><b>{en}</b></div></div></div>'
                       for w, tr, en in L["phrases"])
        self.add(f"""
<div class="chip">LET'S TALK</div>
<h2 style="margin-top:0.08in">My first {L['name']} words <span class="ntd">{L['phrases_native']}</span></h2>
<p>Now that you know the letters, try saying these with your family.</p>
<div class="grid" style="margin-top:0.08in">{rows}</div>
<div style="display:flex;justify-content:center;gap:0.35in;margin-top:0.3in">
<div style="width:1.35in">{self.pic('mosque')}</div><div style="width:1.35in">{self.pic('teacup')}</div><div style="width:1.35in">{self.pic('gift')}</div></div>
""", "content")

    def references_page(self):
        L = self.L
        n = sum(len(s["items"]) for s in L["sections"])
        self.add(f"""
<div class="chip">REFERENCES & SOURCES</div>
<h2 style="margin-top:0.08in">Where our facts come from</h2>
<p><sup>¹</sup> <b>The Noble Qur’an</b> — Surah Ar-Raḥmān 55:1–4, Surah Ar-Rūm 30:22 and Surah Al-Ḥujurāt 49:13.
Arabic text and meanings checked against <b>Quran.com</b>; the English meanings in this book are simplified
for children.</p>
<p><sup>²</sup> <b>Map</b> — outlines from <b>Natural Earth</b> (public domain), via the <i>world-atlas</i> data set.</p>
<p><sup>³</sup> <b>Language facts</b> — {L['facts_source']}</p>
<div class="box" style="margin-top:0.25in"><h3>What’s next?</h3>
You have met all <b>{n} {L['name']} letters</b>! Keep practising by reading signs, books and food packets
written in {L['name']}, and look out for the other books in the <b>Allamahul Bayan Series</b>, in shā’ Allāh.</div>
<div class="box" style="margin-top:0.15in"><h3>Enjoyed this book?</h3>
A short review on Amazon helps other families find it — <i>jazākumullāhu khayran!</i></div>
<div style="display:flex;justify-content:center;gap:0.3in;margin-top:0.3in">
<div style="width:1.4in">{self.pic('book', **L['book_pic'])}</div><div style="width:1.4in">{self.pic('palette')}</div></div>
""", "content")

    def certificate_page(self):
        L, S = self.L, SERIES
        n = sum(len(s["items"]) for s in L["sections"])
        self.add(f"""
<div class="frame" style="height:100%;padding:0.18in;border-width:5px">
<div class="dash" style="height:100%;padding:0.35in 0.4in;text-align:center;position:relative">
  <div style="display:flex;justify-content:center;gap:0.3in"><div style="width:0.75in">{self.pic('star')}</div><div style="width:0.75in">{self.pic('moon')}</div><div style="width:0.75in">{self.pic('star')}</div></div>
  <h1 style="font-size:34pt;margin-top:0.1in">Certificate of Achievement</h1>
  <div class="ntd" style="font-size:24pt;line-height:1.5">{L['cheer'][0]}</div>
  <div class="tr">{L['cheer'][1]} — {L['cheer'][2]}</div>
  <p style="margin-top:0.3in;font-size:15pt">This certifies that</p>
  <div style="border-bottom:3px solid #111;height:0.6in;margin:0 0.5in"></div>
  <p style="margin-top:0.25in;font-size:14pt">has learned, traced and colored<br><b>all {n} letters of the {L['name']} alphabet</b>.</p>
  <div style="display:flex;justify-content:space-between;margin-top:0.5in;padding:0 0.2in;text-align:center">
    <div style="width:2.3in"><div style="border-bottom:2px solid #111;height:0.45in"></div><div class="small">Date</div></div>
    <div style="width:2.3in"><div style="border-bottom:2px solid #111;height:0.45in"></div><div class="small">Grown-up’s signature</div></div>
  </div>
  <div style="margin-top:0.35in"><div style="font:700 26pt 'Dancing Script'">{S['author_short']}</div>
    <div class="small">{S['author']}, author</div></div>
  <div style="display:flex;align-items:center;justify-content:center;gap:0.15in;margin-top:0.2in">
    <div style="width:0.7in">{mark_svg()}</div>
    <div style="text-align:left" class="small"><b>{S['publisher']}</b> — Publisher<br>{S['publisher_note']}<br>
    <span class="ar" style="font-size:12pt">{S['publisher_ar']}</span></div></div>
  <div class="small muted" style="position:absolute;bottom:0.12in;left:0;right:0">✂ Cut out and frame it — the back of this page is blank.</div>
</div></div>""", "coloring", number=False)

    # ---------- assemble ----------
    def build(self):
        L = self.L
        self.title_page(); self.copyright_page(); self.belongs_page()
        self.series_pages()
        self.parents_page(); self.hello_page()
        self.chart_page()
        self.map_page(); self.blank()
        for s in L["sections"]:
            self.section_intro(s); self.warmup(s)
            for i, d in enumerate(s["items"], 1):
                self.letter_page(d, i, len(s["items"]), s["label"]); self.blank()
        self.digits_page(); self.blank()
        self.phrases_page(); self.references_page()
        self.certificate_page(); self.blank(note=False)

        n = len(self.pages)
        for i, p in enumerate(self.pages, 1):
            if p["kind"] == "coloring":
                assert i % 2 == 1, f"coloring page {i} must be a right-hand (odd) page"
                assert i == n or self.pages[i]["kind"] == "blank", f"coloring page {i} needs a blank back"
        assert self.pages[3]["kind"] == "front" and self.pages[4]["kind"] == "front"
        assert n % 2 == 0 and 24 <= n <= 828, n

        body = []
        for i, p in enumerate(self.pages, 1):
            side = "odd" if i % 2 else "even"
            pno = f'<div class="pno">{i}</div>' if p["number"] and p["kind"] != "blank" else ""
            body.append(f'<section class="page {side}"><div class="inner">{p["html"]}</div>{pno}</section>')
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{L["title"]} — interior</title>'
                f'<style>{base_css(L)}</style></head><body>{"".join(body)}</body></html>')
        out = os.path.join(ROOT, "build", L["code"])
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "interior.html"), "w", encoding="utf-8").write(html)
        json.dump({"pages": n}, open(os.path.join(out, "pagecount.json"), "w"))
        return n
