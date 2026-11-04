# -*- coding: utf-8 -*-
"""Full-wrap KDP paperback cover for any language book.

Size = bleed + back + spine + front + bleed. Spine width uses KDP's white-paper, black-ink factor
(0.002252 in per page). The barcode area (2 x 1.2 in, bottom right of the back) stays empty white.
Chromium rounds page sizes to whole pixels, so the page is rendered 0.05 in wider and then cropped
to the exact size by crop().
"""
import os
from illos import svg as pic
from glyphs import letter_svg
from brand import mark_svg
from series import SERIES
from book import font_css, ROOT

TRIM_W, TRIM_H, BLEED, SAFE = 8.5, 11.0, 0.125, 0.45
TEAL, YEL, CORAL, GREEN, PINK, BLUE, PURPLE, CREAM, INK = (
    "#0E5E6F", "#F9C74F", "#F3722C", "#43AA8B", "#F28AB2", "#5AA9E6", "#9B5DE5", "#FFF8E7", "#1d1d1d")
TILE_COLOURS = [CORAL, YEL, GREEN, BLUE, PINK, PURPLE]
COLS = {  # colour roles a b c d e per picture
    "mango": (YEL, YEL, GREEN, YEL, YEL), "boat": ("#fff", "#C8743C", "#E9B872", YEL, YEL),
    "lily": (PINK, PINK, GREEN, YEL, PINK), "mosque": ("#fff", "#9AD1D4", GREEN, BLUE, YEL),
    "rainbow": (CORAL, YEL, GREEN, BLUE, PINK), "flower": (PINK, PINK, GREEN, YEL, CORAL),
    "palette": ("#F5DEB3", CORAL, GREEN, BLUE, YEL), "sun": (YEL, YEL, YEL, YEL, CORAL),
    "eid": ("#fff", CORAL, YEL, YEL, YEL), "book": ("#fff", BLUE, GREEN, YEL, PINK),
    "kite": (YEL, BLUE, GREEN, CORAL, PINK), "pomegranate": ("#fff", BLUE, GREEN, PINK, "#E63946"),
    "pen": ("#fff", BLUE, YEL, CORAL, PINK), "kaaba": ("#fff", "#333", GREEN, YEL, YEL),
    "tasbih": ("#fff", GREEN, GREEN, YEL, CORAL), "teacup": ("#fff", CORAL, GREEN, "#C8743C", YEL),
    "corn": ("#fff", BLUE, GREEN, YEL, YEL), "carrot": ("#fff", BLUE, GREEN, YEL, CORAL),
    "globe": ("#fff", BLUE, GREEN, YEL, YEL), "tomato": ("#fff", BLUE, GREEN, YEL, "#E63946"),
    "grapes": ("#fff", PURPLE, GREEN, YEL, PINK), "balloon": ("#fff", CORAL, GREEN, YEL, YEL),
    "ship": ("#fff", BLUE, GREEN, YEL, CORAL), "umbrella": ("#fff", CORAL, BLUE, YEL, YEL),
}

def cpic(key, width, **args):
    a, b, c, d, e = COLS[key]
    return (f'<div style="width:{width}in">' +
            pic(key, style=f"--a:{a};--b:{b};--c:{c};--d:{d};--e:{e}", **args) + "</div>")


def build(L, pages):
    spine = round(pages * 0.002252, 4)
    W = BLEED * 2 + TRIM_W * 2 + spine
    H = TRIM_H + BLEED * 2
    SX, FX = BLEED + TRIM_W, BLEED + TRIM_W + spine
    C = L["cover"]
    rtl = L.get("dir") == "rtl"
    tiles = "".join(f'<div style="width:1.3in;height:1.3in">{letter_svg(c, L["glyph_font"], TILE_COLOURS[i], min_box=650, pad=0.04)}</div>'
                    for i, c in enumerate(C["tiles"]))
    p = C["pics"]  # four keys: top-left, top-right, bottom-left, bottom-right
    n = sum(len(s["items"]) for s in L["sections"])
    D, T = L["disp_family"], L["text_family"]
    css = f"""
{font_css(L)}
@page {{ size:{W + 0.05}in {H}in; margin:0 }}
* {{ box-sizing:border-box }} html,body {{ margin:0; padding:0 }}
body {{ width:{W + 0.05}in; height:{H}in; position:relative; overflow:hidden; background:{CREAM};
        font-family:'Nunito','{T}',sans-serif; color:{INK} }}
.abs {{ position:absolute }} .fd {{ font-family:'Fredoka',sans-serif; font-weight:600 }}
.ntd {{ font-family:'{D}','{T}',sans-serif; font-weight:800 }} .nt {{ font-family:'{T}',sans-serif }}
.ar {{ font-family:'Amiri',serif; font-weight:700 }}
.ill {{ display:block; width:100% }}
.ill * {{ stroke:{INK}; stroke-width:3.2; stroke-linejoin:round; stroke-linecap:round }}
.ill .a{{fill:var(--a,#fff)}} .ill .b{{fill:var(--b,#fff)}} .ill .c{{fill:var(--c,#fff)}} .ill .d{{fill:var(--d,#fff)}} .ill .e{{fill:var(--e,#fff)}}
.ill .n{{fill:none}} .ill .t{{stroke-width:2}}
.ill text{{font-family:'{D}';font-weight:800;fill:#fff}} .ill text.lbl{{fill:{INK};stroke:none}}
.badge {{ border-radius:999px; padding:0.06in 0.2in; font:600 15pt 'Fredoka'; color:#fff; display:inline-block }}
.dots {{ background-image:radial-gradient({TEAL}22 2px, transparent 2.5px); background-size:0.28in 0.28in }}
"""
    front = f"""
<div class="abs dots" style="left:{FX}in;top:0;width:{TRIM_W + BLEED + 0.05}in;height:{H}in"></div>
<div class="abs" style="left:{FX}in;top:0;width:{TRIM_W + BLEED + 0.05}in;height:{BLEED + 1.25}in;background:{TEAL}"></div>
<div class="abs" style="left:{FX + SAFE}in;top:{BLEED + 0.3}in;width:{TRIM_W - 2*SAFE}in;display:flex;justify-content:space-between;align-items:center;color:#fff">
  <div class="fd" style="font-size:15pt;letter-spacing:.12em">ALLAMAHUL BAYAN SERIES · BOOK {L['series_no']}</div>
  <div class="ar" style="font-size:24pt">{SERIES['ar']}</div>
</div>
<div class="abs" style="left:{FX + SAFE}in;top:{BLEED + 1.45}in;width:{TRIM_W - 2*SAFE}in;text-align:center">
  <div class="fd" style="font-size:{C.get('title_size', 50)}pt;line-height:1.02;color:{TEAL}">{C['title_html']}</div>
  <div class="ntd" style="font-size:{C.get('native_size', 31)}pt;color:{CORAL};margin-top:0.04in;line-height:1.45">{L['title_native']}</div>
  <div style="margin-top:0.08in"><span class="badge" style="background:{GREEN}">COLORING BOOK · Learn · Trace · Say</span></div>
</div>
<div class="abs" style="left:{FX + 2.0}in;top:{BLEED + 4.3}in;width:{TRIM_W - 4.0}in;display:grid;grid-template-columns:repeat(3,1fr);gap:0.22in;justify-items:center;{'direction:rtl;' if rtl else ''}">{tiles}</div>
<div class="abs" style="left:{FX + 0.4}in;top:{BLEED + 4.3}in">{cpic(p[0], 1.3)}</div>
<div class="abs" style="left:{FX + TRIM_W - 1.7}in;top:{BLEED + 4.3}in">{cpic(p[1], 1.3)}</div>
<div class="abs" style="left:{FX + 0.4}in;top:{BLEED + 5.95}in">{cpic(p[2], 1.3)}</div>
<div class="abs" style="left:{FX + TRIM_W - 1.7}in;top:{BLEED + 5.95}in">{cpic(p[3], 1.3)}</div>
<div class="abs" style="left:{FX + SAFE}in;top:{BLEED + 7.75}in;width:{TRIM_W - 2*SAFE}in;text-align:center">
  <span class="badge" style="background:{CORAL}">{n} letters to color</span>
  <span class="badge" style="background:{TEAL}">English phonetics</span>
  <span class="badge" style="background:{GREEN}">{SERIES['ages']}</span>
</div>
<div class="abs fd" style="left:{FX + SAFE}in;top:{BLEED + 8.6}in;width:{TRIM_W - 2*SAFE}in;text-align:center;font-size:20pt;color:{TEAL}">{SERIES['author']}</div>
<div class="abs" style="left:{FX + SAFE}in;top:{BLEED + 9.35}in;width:{TRIM_W - 2*SAFE}in;display:flex;justify-content:center;align-items:center;gap:0.15in">
  <div style="width:0.75in">{mark_svg()}</div>
  <div class="fd" style="font-size:13pt;text-align:left;line-height:1.2">{SERIES['publisher']}<br><span class="ar" style="font-size:14pt">{SERIES['publisher_ar']}</span></div>
</div>"""
    spine_html = f"""
<div class="abs" style="left:{SX}in;top:0;width:{spine}in;height:{H}in;background:{TEAL}"></div>
<div class="abs" style="left:{SX + spine/2}in;top:{H/2}in;transform:translate(-50%,-50%) rotate(90deg);white-space:nowrap;
     color:#fff;font:600 8.5pt 'Fredoka';letter-spacing:.06em">{L['title'].upper()} &nbsp;·&nbsp; ALLAMAHUL BAYAN SERIES {L['series_no']} &nbsp;·&nbsp; {SERIES['author_short'].upper()}</div>"""
    bx = BLEED
    bullets = "<br>\n".join(f"✓ {b}" for b in C["bullets"])
    back = f"""
<div class="abs" style="left:0;top:0;width:{BLEED + TRIM_W}in;height:{H}in;background:{TEAL}"></div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + 0.55}in;width:{TRIM_W - 2*SAFE}in;color:#fff">
  <div class="fd" style="font-size:27pt;line-height:1.15">Color your way into {L['name']} —<br>one letter at a time!</div>
  <p style="font-size:13.5pt;line-height:1.5;margin-top:0.18in">{C['blurb']}</p>
  <div style="font-size:13.5pt;line-height:1.55;margin-top:0.1in">{bullets}</div>
  <div style="margin-top:0.2in;padding:0.14in 0.2in;border:2px solid #ffffff88;border-radius:16px;font-size:12pt;line-height:1.45">
  <b>The Allamahul Bayan Series</b> takes its name from Surah Ar-Raḥmān: <i>“He taught him clear expression”</i>
  (55:4). Each book helps children thank Allah for the gift of language by meeting a new one — its letters,
  its sounds and the people who speak it.</div>
  <div style="margin-top:0.16in;font-size:11.5pt;line-height:1.45"><b>About the author.</b> {SERIES['author']} is a
  ḥāfiẓ of the Qur’an and holds a BSS and MSS in Economics from the University of Dhaka. A father of two, he founded
  the Kunujul Akhirah Charitable Trust and its publishing imprint, Maktabatu Kunujul Akhirah.</div>
</div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + 8.05}in;display:flex;gap:0.15in">
  {cpic('rainbow', 1.15)}{cpic('flower', 1.15)}{cpic('palette', 1.15)}{cpic('book', 1.15, **L['book_pic'])}</div>
<div class="abs" style="left:{bx + SAFE}in;top:{BLEED + TRIM_H - 1.25}in;color:#fff;display:flex;align-items:center;gap:0.12in">
  <div style="width:0.75in;background:#fff;border-radius:10px;padding:4px">{mark_svg()}</div>
  <div class="fd" style="font-size:12pt;line-height:1.25">{SERIES['publisher']}<br>
  <span style="font-family:Nunito;font-weight:400;font-size:10pt">{SERIES['publisher_note']}</span></div></div>
<div class="abs" style="left:{bx + TRIM_W - 0.25 - 2.0}in;top:{BLEED + TRIM_H - 0.25 - 1.2}in;width:2.0in;height:1.2in;background:#fff"></div>"""
    html = (f'<!doctype html><html><head><meta charset="utf-8"><title>{L["title"]} — cover</title>'
            f'<style>{css}</style></head><body>{back}{spine_html}{front}</body></html>')
    out = os.path.join(ROOT, "build", L["code"], "cover.html")
    open(out, "w", encoding="utf-8").write(html)
    return dict(spine=spine, W=W, H=H)


def crop(pdf_path, W, H):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    r = PdfReader(pdf_path); w = PdfWriter()
    p = r.pages[0]
    top = float(p.mediabox.top)
    box = RectangleObject([0, top - H * 72, W * 72, top])
    p.mediabox = box; p.cropbox = box; p.trimbox = box; p.bleedbox = box
    w.add_page(p); w.write(pdf_path)
