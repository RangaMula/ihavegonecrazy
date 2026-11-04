# -*- coding: utf-8 -*-
"""Full-wrap KDP paperback cover: build/cover.html -> output/cover.pdf (via render.mjs cover).

Size = bleed + back + spine + front + bleed. Spine width uses KDP's white-paper, black-ink
factor (0.002252 in per page). The barcode area (2 x 1.2 in, bottom right of the back) is
left empty white for Amazon's ISBN barcode.
Run after build_book.py (it reads build/pagecount.json).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from content import BOOK
from illos import svg as pic
from glyphs import letter_svg
from brand import mark_svg

PAGES = json.load(open(os.path.join(ROOT, "build", "pagecount.json")))["pages"]
TRIM_W, TRIM_H, BLEED = 8.5, 11.0, 0.125
SPINE = round(PAGES * 0.002252, 4)
W = BLEED * 2 + TRIM_W * 2 + SPINE
H = TRIM_H + BLEED * 2
BACK_X = BLEED                    # back panel trim starts here
SPINE_X = BLEED + TRIM_W
FRONT_X = SPINE_X + SPINE
SAFE = 0.45                       # keep text this far from trim edges (KDP min 0.125 + margin)

TEAL, YEL, CORAL, GREEN, PINK, BLUE, CREAM, INK = "#0E5E6F", "#F9C74F", "#F3722C", "#43AA8B", "#F28AB2", "#5AA9E6", "#FFF8E7", "#1d1d1d"
COLS = {  # colour roles per picture: a b c d e
    "mango": (YEL, YEL, GREEN, YEL, YEL), "boat": ("#fff", "#C8743C", "#E9B872", YEL, YEL),
    "lily": (PINK, PINK, GREEN, YEL, PINK), "mosque": ("#fff", "#9AD1D4", GREEN, BLUE, YEL),
    "rainbow": (CORAL, YEL, GREEN, BLUE, PINK), "flower": (PINK, PINK, GREEN, YEL, CORAL),
    "palette": ("#F5DEB3", CORAL, GREEN, BLUE, YEL), "sun": (YEL, YEL, YEL, YEL, CORAL),
    "eid": ("#fff", CORAL, YEL, YEL, YEL), "book": ("#fff", BLUE, GREEN, YEL, PINK),
}

def cpic(key, width):
    a, b, c, d, e = COLS[key]
    return (f'<div style="width:{width}in">' +
            pic(key, style=f"--a:{a};--b:{b};--c:{c};--d:{d};--e:{e}") + "</div>")

FONTS = "../assets/fonts/"
CSS = f"""
@font-face{{font-family:'Baloo Da 2';font-weight:800;src:url({FONTS}baloo-da-2-bengali-800-normal.woff2)}}
@font-face{{font-family:'Noto Sans Bengali';font-weight:400;src:url({FONTS}noto-sans-bengali-bengali-400-normal.woff2)}}
@font-face{{font-family:'Noto Sans Bengali';font-weight:700;src:url({FONTS}noto-sans-bengali-bengali-700-normal.woff2)}}
@font-face{{font-family:'Fredoka';font-weight:600;src:url({FONTS}fredoka-latin-600-normal.woff2)}}
@font-face{{font-family:'Fredoka';font-weight:400;src:url({FONTS}fredoka-latin-400-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:400;src:url({FONTS}nunito-latin-400-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:700;src:url({FONTS}nunito-latin-700-normal.woff2)}}
@font-face{{font-family:'Nunito';font-weight:800;src:url({FONTS}nunito-latin-800-normal.woff2)}}
@font-face{{font-family:'Amiri';font-weight:700;src:url({FONTS}amiri-arabic-700-normal.woff2)}}
@page {{ size:{W + 0.05}in {H}in; margin:0 }}
* {{ box-sizing:border-box }}
html,body {{ margin:0; padding:0 }}
body {{ width:{W + 0.05}in; height:{H}in; position:relative; overflow:hidden; background:{CREAM};
        font-family:'Nunito','Noto Sans Bengali',sans-serif; color:{INK} }}
.abs {{ position:absolute }}
.fd {{ font-family:'Fredoka',sans-serif; font-weight:600 }}
.bnd {{ font-family:'Baloo Da 2',sans-serif; font-weight:800 }}
.ar {{ font-family:'Amiri',serif; font-weight:700 }}
.ill {{ display:block; width:100% }}
.ill * {{ stroke:{INK}; stroke-width:3.2; stroke-linejoin:round; stroke-linecap:round }}
.ill .a{{fill:var(--a,#fff)}} .ill .b{{fill:var(--b,#fff)}} .ill .c{{fill:var(--c,#fff)}} .ill .d{{fill:var(--d,#fff)}} .ill .e{{fill:var(--e,#fff)}}
.ill .n{{fill:none}} .ill .t{{stroke-width:2}}
.ill text{{font-family:'Baloo Da 2';font-weight:800;fill:#fff}} .ill text.lbl{{fill:{INK};stroke:none}}
.badge {{ border-radius:999px; padding:0.06in 0.2in; font:600 15pt 'Fredoka'; color:#fff; display:inline-block }}
.dots {{ background-image:radial-gradient({TEAL}22 2px, transparent 2.5px); background-size:0.28in 0.28in }}
"""

def letter_tile(ch, color, size):
    return f'<div style="width:{size}in;height:{size}in">{letter_svg(ch, color, min_box=650, pad=0.04)}</div>'

def build():
    fx = FRONT_X
    tiles = [("অ", CORAL), ("আ", YEL), ("ক", GREEN), ("খ", BLUE), ("গ", PINK), ("ম", "#9B5DE5")]
    tile_html = "".join(letter_tile(c, col, 1.3) for c, col in tiles)
    front = f"""
<div class="abs dots" style="left:{fx}in;top:0;width:{TRIM_W + BLEED + 0.05}in;height:{H}in"></div>
<div class="abs" style="left:{fx}in;top:0;width:{TRIM_W + BLEED + 0.05}in;height:{BLEED + 1.25}in;background:{TEAL}"></div>
<div class="abs" style="left:{fx + SAFE}in;top:{BLEED + 0.3}in;width:{TRIM_W - 2*SAFE}in;display:flex;justify-content:space-between;align-items:center;color:#fff">
  <div class="fd" style="font-size:15pt;letter-spacing:.12em">ALLAMAHUL BAYAN SERIES · BOOK 1</div>
  <div class="ar" style="font-size:24pt">{BOOK['series_ar']}</div>
</div>
<div class="abs" style="left:{fx + SAFE}in;top:{BLEED + 1.5}in;width:{TRIM_W - 2*SAFE}in;text-align:center">
  <div class="fd" style="font-size:50pt;line-height:1.02;color:{TEAL}">My First Bengali<br>Alphabet</div>
  <div class="bnd" style="font-size:31pt;color:{CORAL};margin-top:0.06in">আমার প্রথম বাংলা বর্ণমালা</div>
  <div style="display:inline-block;margin-top:0.12in" class="badge"><span style="background:{GREEN};border-radius:999px;padding:0.06in 0.25in">COLORING BOOK · Learn · Trace · Say</span></div>
</div>
<div class="abs" style="left:{fx + 2.0}in;top:{BLEED + 4.3}in;width:{TRIM_W - 4.0}in;display:grid;grid-template-columns:repeat(3,1fr);gap:0.22in;justify-items:center">{tile_html}</div>
<div class="abs" style="left:{fx + 0.4}in;top:{BLEED + 4.3}in">{cpic('mango', 1.3)}</div>
<div class="abs" style="left:{fx + TRIM_W - 1.7}in;top:{BLEED + 4.3}in">{cpic('lily', 1.3)}</div>
<div class="abs" style="left:{fx + 0.4}in;top:{BLEED + 5.95}in">{cpic('boat', 1.3)}</div>
<div class="abs" style="left:{fx + TRIM_W - 1.7}in;top:{BLEED + 5.95}in">{cpic('mosque', 1.3)}</div>
<div class="abs" style="left:{fx + SAFE}in;top:{BLEED + 7.75}in;width:{TRIM_W - 2*SAFE}in;text-align:center">
  <span class="badge" style="background:{CORAL}">50 letters to color</span>
  <span class="badge" style="background:{TEAL}">English phonetics</span>
  <span class="badge" style="background:{GREEN}">{BOOK['ages']}</span>
</div>
<div class="abs" style="left:{fx + SAFE}in;top:{BLEED + 8.6}in;width:{TRIM_W - 2*SAFE}in;text-align:center">
  <div class="fd" style="font-size:20pt;color:{TEAL}">{BOOK['author']}</div>
</div>
<div class="abs" style="left:{fx + SAFE}in;top:{BLEED + 9.35}in;width:{TRIM_W - 2*SAFE}in;display:flex;justify-content:center;align-items:center;gap:0.15in">
  <div style="width:0.75in">{mark_svg()}</div>
  <div class="fd" style="font-size:13pt;text-align:left;line-height:1.2">{BOOK['publisher']}<br><span class="ar" style="font-size:14pt">{BOOK['publisher_ar']}</span></div>
</div>"""

    spine = f"""
<div class="abs" style="left:{SPINE_X}in;top:0;width:{SPINE}in;height:{H}in;background:{TEAL}"></div>
<div class="abs" style="left:{SPINE_X + SPINE/2}in;top:{H/2}in;transform:translate(-50%,-50%) rotate(90deg);white-space:nowrap;
     color:#fff;font:600 8.5pt 'Fredoka';letter-spacing:.06em">MY FIRST BENGALI ALPHABET &nbsp;·&nbsp; ALLAMAHUL BAYAN SERIES 1 &nbsp;·&nbsp; MINHAZ REZA</div>"""

    bx = BACK_X
    back = f"""
<div class="abs" style="left:0;top:0;width:{BLEED + TRIM_W}in;height:{H}in;background:{TEAL}"></div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + 0.55}in;width:{TRIM_W - 2*SAFE}in;color:#fff">
  <div class="fd" style="font-size:27pt;line-height:1.15">Color your way into Bengali —<br>one letter at a time!</div>
  <p style="font-size:13.5pt;line-height:1.5;margin-top:0.18in">Bengali (Bangla) is spoken by about 270 million people in
  Bangladesh, India and all over the world. This big, friendly coloring book introduces young children to all
  <b>50 letters</b> of the Bengali alphabet <b>through English</b> — no Bengali needed at home.</p>
  <div style="font-size:13.5pt;line-height:1.55;margin-top:0.1in">
  ✓ <b>Every letter on its own page</b> — a giant letter to color, its name in Bengali <i>and</i> English letters<br>
  ✓ <b>Easy English sound guides</b> plus Bengali phonetics (ক্ + অ = ক)<br>
  ✓ <b>A word and picture for every letter</b> to color and say: আম <i>aam</i> mango, নৌকা <i>noukaa</i> boat…<br>
  ✓ <b>Pencil tracing rows</b> and warm-up pages for vowels and consonants<br>
  ✓ <b>Map to color</b>, Bengali numbers ০–৯, first phrases and a certificate<br>
  ✓ <b>Single-sided coloring pages</b> so markers never ruin the next picture</div>
  <div style="margin-top:0.2in;padding:0.14in 0.2in;border:2px solid #ffffff88;border-radius:16px;font-size:12pt;line-height:1.45">
  <b>The Allamahul Bayan Series</b> takes its name from Surah Ar-Raḥmān: <i>“He taught him clear expression”</i>
  (55:4). Each book helps children thank Allah for the gift of language by meeting a new one — its letters,
  its sounds and the people who speak it.</div>
  <div style="margin-top:0.16in;font-size:11.5pt;line-height:1.45"><b>About the author.</b> {BOOK['author']} is a
  ḥāfiẓ of the Qur’an and holds a BSS and MSS in Economics from the University of Dhaka. A father of two, he founded
  the Kunujul Akhirah Charitable Trust and its publishing imprint, Maktabatu Kunujul Akhirah.</div>
</div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + 8.05}in;display:flex;gap:0.15in">
  {cpic('rainbow', 1.15)}{cpic('flower', 1.15)}{cpic('palette', 1.15)}{cpic('book', 1.15)}</div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + TRIM_H - 1.25}in;color:#fff;display:flex;align-items:center;gap:0.12in">
  <div style="width:0.75in;background:#fff;border-radius:10px;padding:4px">{mark_svg()}</div>
  <div class="fd" style="font-size:12pt;line-height:1.25">{BOOK['publisher']}<br>
  <span style="font-family:Nunito;font-weight:400;font-size:10pt">{BOOK['publisher_note']}</span></div></div>
<div class="abs" style="left:{bx + TRIM_W - 0.25 - 2.0}in;top:{BLEED + TRIM_H - 0.25 - 1.2}in;width:2.0in;height:1.2in;background:#fff"></div>"""

    html = (f'<!doctype html><html><head><meta charset="utf-8"><title>{BOOK["title"]} — cover</title>'
            f'<style>{CSS}</style></head><body>{back}{spine}{front}</body></html>')
    open(os.path.join(ROOT, "build", "cover.html"), "w", encoding="utf-8").write(html)
    json.dump(dict(pages=PAGES, spine_in=SPINE, width_in=round(W, 4), height_in=H),
              open(os.path.join(ROOT, "build", "cover_dims.json"), "w"), indent=1)
    print(f"cover: {W:.4f} x {H} in, spine {SPINE} in for {PAGES} pages")


def crop_pdf():
    """Chromium rounds page sizes to whole pixels, so the page is rendered 0.05 in wider and
    cropped here to the exact KDP size."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    src = os.path.join(ROOT, "output", "cover.pdf")
    r = PdfReader(src); w = PdfWriter()
    p = r.pages[0]
    top = float(p.mediabox.top)
    box = RectangleObject([0, top - H * 72, W * 72, top])
    p.mediabox = box; p.cropbox = box; p.trimbox = box; p.bleedbox = box
    w.add_page(p); w.write(src)
    print(f"cropped cover.pdf to {W*72:.2f} x {H*72:.2f} pt")

if __name__ == "__main__":
    crop_pdf() if "--crop" in sys.argv else build()
