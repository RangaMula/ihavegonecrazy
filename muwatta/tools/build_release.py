#!/usr/bin/env python3
"""Build the retail package of one language edition / volume for print-on-demand and eBook stores.

    python3 tools/build_release.py bn            # volume 1 of the Bengali edition
    python3 tools/build_release.py ja --volume 1

Writes editions/<code>/release/vol01/:
  interior.pdf        print interior: 6 x 9 in trim, no bleed, mirrored margins, fonts embedded, even page count
  cover.pdf           full-wrap paperback cover: bleed 0.125 in, spine from page count, barcode area on the back
  ebook.epub          EPUB 3 (fonts embedded) for Kindle/KDP, Google Play Books, Apple Books, Kobo, Draft2Digital
  ebook-cover.jpg     1600 x 2560 px eBook cover
  metadata.json       everything a store listing asks for
  PUBLISHING-GUIDE.md step-by-step for each store, with the upload specs

Publisher, editor, copyright and ISBNs come from standard/publishing.json. Fill an ISBN there and rebuild:
it is printed on the copyright page, and an EAN-13 barcode is drawn on the back cover.

The "REVIEW DRAFT" notice stays on until every book in the volume has `reviewed_by` set in its translation file
(standard/EDITION-STANDARD.md §5). The guide lists exactly what is still missing before upload.
"""
import argparse, html, io, json, os, re, shutil, subprocess, sys, uuid, zipfile
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_book as BB  # noqa: E402
from scripts import SCHEMES  # noqa: E402

e = html.escape
FS = os.path.join(ROOT, "tools", "node_modules", "@fontsource")


def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------ ISBN + EAN-13
def isbn_digits(isbn):
    if not isbn:
        return None
    d = re.sub(r"[^0-9]", "", isbn)
    if len(d) != 13 or not d.startswith(("978", "979")):
        sys.exit(f"ISBN {isbn!r}: must be 13 digits starting 978/979")
    if sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(d)) % 10:
        sys.exit(f"ISBN {isbn!r}: check digit is wrong")
    return d


L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
PARITY = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]


def ean13_svg(isbn, hyphenated):
    d = isbn_digits(isbn)
    bits = "101" + "".join((L if p == "L" else G)[int(c)] for p, c in zip(PARITY[int(d[0])], d[1:7])) + "01010" \
           + "".join(R[int(c)] for c in d[7:]) + "101"
    m = 1.0  # module width in viewBox units; 95 modules + quiet zones
    x0, bars = 11, []
    for i, b in enumerate(bits):
        if b == "1":
            guard = i < 3 or 45 <= i < 50 or i >= 92
            bars.append(f'<rect x="{x0 + i * m}" y="13" width="{m}" height="{48 if guard else 43}"/>')
    txt = (f'<text x="58.5" y="9.5" font-size="7.2" text-anchor="middle">ISBN {e(hyphenated or d)}</text>'
           f'<text x="4" y="64" font-size="8">{d[0]}</text>'
           f'<text x="35.5" y="64" font-size="8" text-anchor="middle" letter-spacing="1.4">{d[1:7]}</text>'
           f'<text x="81.5" y="64" font-size="8" text-anchor="middle" letter-spacing="1.4">{d[7:]}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 117 70" style="width:100%;height:100%">'
            f'<rect width="117" height="70" fill="#fff"/><g fill="#000">{"".join(bars)}</g>'
            f'<g fill="#000" font-family="Noto Serif, serif">{txt}</g></svg>')


# ------------------------------------------------------------------ shared pieces
def digits(s, prof):
    return BB.digits(s, prof)


def vol_label(ed, n, prof):
    lab = ed["volume_label"]
    return lab.replace("{n}", digits(n, prof)) if "{n}" in lab else f"{lab} {digits(n, prof)}"


def quranenc_version(key):
    p = os.path.join(ROOT, "data", "verification", "quran.json")
    if not os.path.exists(p):
        return None
    return (json.load(open(p, encoding="utf-8")).get("versions", {}).get(key) or {}).get("version")


def quran_credit(ed):
    qt = ed["quran_translation"]
    return qt["credit"].replace("{version}", quranenc_version(qt["key"]) or qt["version_missing"])


def status(code, vol, trs, ed):
    missing = []
    qt = ed.get("quran_translation")
    if qt and not quranenc_version(qt["key"]):
        missing.append(f"QuranEnc version number of the Qur'an translation `{qt['key']}` (QuranEnc's terms require it; "
                       "its list API and downloads did not provide it on 2026-11-22). Rerun tools/verify_quran.py when available")
    if not all(t.get("reviewed_by") for t in trs):
        missing.append("scholarly review: set `reviewed_by` in every translations/%s/book-NN.json of this volume" % code)
    if not ed["isbn"].get("paperback"):
        missing.append("paperback ISBN in standard/publishing.json (or use the store's free ISBN, see the guide)")
    if not ed["isbn"].get("ebook"):
        missing.append("eBook ISBN (optional for most eBook stores, see the guide)")
    return missing


def saw(htm):
    """Set the ﷺ glyph in the Arabic font wherever it appears in non-Arabic text."""
    return htm.replace("ﷺ", '<span class="saw">ﷺ</span>')


def copyright_block(code, ed, pub, prof, trs, fmt):
    lab = ed["labels"]
    year = pub["year"]
    reviewers = sorted({t["reviewed_by"] for t in trs if t.get("reviewed_by")})
    isbn_pb = ed["isbn"].get("paperback")
    isbn_eb = ed["isbn"].get("ebook")
    rows = [
        f'<p><b>{e(ed["title"])}</b> — {e(ed["subtitle"])}<br>{e(pub["series"].get(code, pub["series"]["en"]))}</p>',
        f'<p>{e(lab["author"])}: {e(pub["author"].get(code, pub["author"]["en"]))}<br>'
        f'{e(lab["editor"])}: <b>{e(pub["editor"].get(code, pub["editor"]["en"]))}</b><br>'
        f'{e(lab["translation"])}: {e(ed["translation_credit"])}<br>'
        f'{e(lab["review"])}: {e(", ".join(reviewers)) if reviewers else e(lab["review_pending"])}</p>',
        f'<p>{e(lab["publisher"])}: <b>{e(pub["publisher"]["name"].get(code, pub["publisher"]["name"]["en"]))}</b>'
        f' ({e(pub["publisher"]["imprint_of"].get(code, pub["publisher"]["imprint_of"]["en"]))})<br>'
        f'{e(pub["publisher"]["address"])}<br>{e(pub["publisher"]["website"])}'
        + (f' · {e(pub["publisher"]["contact_email"])}' if pub["publisher"].get("contact_email") else "") + "</p>",
        f'<p>{e(lab["edition"])}: {digits(year, prof)} ({digits(pub["year_hijri"], prof)} AH)</p>',
        f'<p>{e(ed["copyright"].replace("{year}", digits(year, prof)))}</p>',
        f'<p>{e(lab["isbn_pb"])}: {e(isbn_pb) if isbn_pb else e(lab["isbn_pending"])}<br>'
        f'{e(lab["isbn_eb"])}: {e(isbn_eb) if isbn_eb else e(lab["isbn_pending"])}</p>',
        f'<p class="src">{e(ed["sources_note"])}</p>',
        f'<p class="src">{e(quran_credit(ed))}</p>' if ed.get("quran_translation") else "",
    ]
    return "\n".join(rows)


def book_sections(code, data, trs, prof, scheme, warnings):
    books = {b["n"]: b for b in data["books"]}
    out = []
    for t in trs:
        b = books[t["book"]]
        ar_entries = [x for x in data["entries"] if x["book"] == t["book"]]
        tmap = {x["n"]: x for x in t["entries"]}
        if {x["n"] for x in ar_entries} != set(tmap):
            sys.exit(f"book {t['book']}: translation entries do not match the Arabic (run build_book.py for details)")
        sec = [f'<section class="book-head"><p class="ar" lang="ar" dir="rtl">{e(b["ar"])}</p>'
               f'<h2>{e(prof["labels"]["book"])} {digits(t["book"], prof)}: {e(t["title"])}</h2></section>']
        for x in ar_entries:
            sec.append(BB.entry_html(x, tmap[x["n"]], prof, scheme, warnings))
        out.append((t, "\n".join(sec)))
    return out


def intro_html(prof, scheme):
    intro = prof.get("intro")
    if not intro:
        return ""
    paras = "".join(f"<p>{e(p)}</p>" for p in intro["paras"])
    key = BB.pron_key(scheme, prof) if scheme in SCHEMES else ""
    return f'<h2>{e(intro["heading"])}</h2>{paras}<h3>{e(prof["labels"]["pron"])}</h3>{key}'


# ------------------------------------------------------------------ print interior
PRINT_CSS = """
@page { size: 6in 9in; margin: 0.65in 0.55in 0.75in 0.55in;
        @bottom-center { content: counter(page); font-family: "Noto Serif", serif; font-size: 8.5pt; color: #555; } }
@page :left  { margin-left: 0.55in; margin-right: 0.8in; }
@page :right { margin-left: 0.8in; margin-right: 0.55in; }
@page front { @bottom-center { content: none; } }
html, body { background: #fff !important; }
body { max-width: none; padding: 0; font-size: 10.5pt; }
.front { page: front; }
.title-pg { height: 7.5in; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; break-after: page; }
.title-pg .ar-title { font-family: Amiri, serif; font-size: 40pt; line-height: 1.4; color: #0b3d24; }
.title-pg .by-ar { font-family: Amiri, serif; font-size: 15pt; color: #555; }
.title-pg h1 { word-break: keep-all; line-break: strict; font-size: 22pt; margin: .25em 0 .1em; color: #0b3d24; }
.title-pg .sub { font-size: 11.5pt; color: #444; }
.title-pg .vol { margin-top: .9em; font-size: 13pt; font-weight: 700; color: #8a6a1f; }
.title-pg .vol-ar { font-family: Amiri, serif; font-size: 15pt; color: #8a6a1f; }
.title-pg .ed { margin-top: 1.4em; font-size: 10.5pt; }
.title-pg .ed b { font-size: 12pt; }
.title-pg .logo { width: 1.05in; margin-top: 1.2em; }
.title-pg .pubname { font-size: 9.5pt; color: #444; }
.title-pg .draft { margin-top: 1em; font-size: 8.5pt; }
.copyright-pg { height: 7.5in; display: flex; flex-direction: column; justify-content: flex-end; font-size: 8.3pt; line-height: 1.55; break-after: page; }
.copyright-pg p { margin: .45em 0; text-align: left; }
.copyright-pg .logo { width: .8in; margin-bottom: .5em; }
.copyright-pg .src { color: #555; }
.intro-pg { break-after: page; }
.about-pg { break-before: page; height: 7.4in; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
.about-pg .logo { width: 1.3in; margin-bottom: 1em; }
.saw { font-family: Amiri, serif; }
p.ar { font-size: 14.5pt; }
.entry { break-inside: auto; }
.malik { break-inside: auto; }
"""


def print_interior(code, vol, ed, pub, prof, data, trs, draft, outdir):
    scheme = prof["pron_scheme"]
    warnings = []
    secs = book_sections(code, data, trs, prof, scheme, warnings)
    volt = pub["volumes"][str(vol)]["title"]
    logo = os.path.join(ROOT, pub["publisher"]["logo_bn" if code == "bn" else "logo"])
    logo_en = os.path.join(ROOT, pub["publisher"]["logo"])
    draft_line = (prof["draft_notice"].split(" — ")[0] + " · REVIEW DRAFT") if draft else ""
    title = f'''<section class="front title-pg">
<div class="ar-title" lang="ar" dir="rtl">الْمُوَطَّأ</div>
<div class="by-ar" lang="ar" dir="rtl">لِلْإِمَامِ مَالِكِ بْنِ أَنَسٍ</div>
<h1>{e(ed["title"])}</h1>
<div class="sub">{e(ed["subtitle"])}</div>
<div class="vol">{e(vol_label(ed, vol, prof))} · {e(volt[code])}</div>
<div class="vol-ar" lang="ar" dir="rtl">{e(volt["ar"])}</div>
<div class="ed">{e(ed["labels"]["editor"])}<br><b>{e(pub["editor"][code])}</b></div>
<img class="logo" src="file://{logo}" alt="">
<div class="pubname">{e(pub["publisher"]["name"][code])} · {e(pub["publisher"]["city"][code])}</div>
{f'<div class="draft">{e(prof["draft_notice"])}</div>' if draft else ""}
</section>'''
    copyr = (f'<section class="front copyright-pg"><img class="logo" src="file://{logo_en}" alt="">'
             f'{copyright_block(code, ed, pub, prof, trs, "print")}</section>')
    intro = f'<section class="front intro-pg">{intro_html(prof, scheme)}</section>'
    body_secs = "".join(f'<div class="{"draft-pages" if draft else ""}">{s}</div>' for _, s in secs)
    about = (f'<section class="about-pg"><img class="logo" src="file://{logo}" alt="">'
             f'<h3>{e(ed["labels"]["about_publisher"])}</h3><p>{e(ed["about_publisher"])}</p>'
             f'<p>{e(pub["publisher"]["website"])}</p></section>')
    fams = list(dict.fromkeys(["Amiri", prof["fonts"]["text"], prof["fonts"]["pron"], "Noto Serif"]))
    css_vars = (f':root {{ --text-font: "{prof["fonts"]["text"]}", "Noto Serif", Amiri, serif; '
                f'--pron-font: "{prof["fonts"]["pron"]}", "Noto Serif", Amiri, sans-serif; }}')
    draft_css = (f'.draft-pages {{ page: draft; }} @page draft {{ @bottom-center {{ content: counter(page); font-size: 8.5pt; color: #555; }} '
                 f'@bottom-left {{ content: "{draft_line}"; font-size: 6.5pt; color: #a33; white-space: nowrap; }} }}') if draft else ""
    doc = f'''<!doctype html><html lang="{code}"><head><meta charset="utf-8"><title>{e(ed["title"])}</title>
{BB.font_links(fams, "local")}
<style>{css_vars}{BB.CSS}{PRINT_CSS}{draft_css}</style></head>
<body>{title}{copyr}{intro}{saw(body_secs)}{about}</body></html>'''
    path_html = os.path.join(outdir, "interior.html")
    with open(path_html, "w", encoding="utf-8") as f:
        f.write(doc)
    pdf = os.path.join(outdir, "interior.pdf")
    subprocess.run(["node", os.path.join(ROOT, "tools", "render_pdf.cjs"), path_html, pdf, "", "print"], check=True)
    # even page count (print-on-demand requirement): add a blank last page if needed
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(pdf)
    n = len(r.pages)
    if n % 2:
        w = PdfWriter(clone_from=r)
        w.add_blank_page(width=432, height=648)
        with open(pdf, "wb") as f:
            w.write(f)
        n += 1
    os.remove(path_html)
    return n, warnings


# ------------------------------------------------------------------ cover
COVER_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #0b3d24; }
.wrap { position: relative; display: flex; width: var(--w); height: var(--h); background: #0b3d24; color: #f3ead2; overflow: hidden; }
.panel { position: relative; height: 100%; }
.back { width: var(--panel); padding: calc(var(--bleed) + 0.55in) 0.6in calc(var(--bleed) + 0.5in) calc(var(--bleed) + 0.55in); }
.front { width: var(--panel); padding: calc(var(--bleed) + 0.5in) calc(var(--bleed) + 0.5in) calc(var(--bleed) + 0.5in) 0.5in;
         display: flex; flex-direction: column; align-items: center; text-align: center; }
.spine { width: var(--spine); background: #082f1b; display: flex; align-items: center; justify-content: center; }
.spine span { writing-mode: vertical-rl; font-size: 10pt; color: #d9b65f; white-space: nowrap; }
.frame { position: absolute; inset: calc(var(--bleed) + 0.28in); border: 1.5pt solid #c9a24a; pointer-events: none; }
.frame::after { content: ""; position: absolute; inset: 5pt; border: .6pt solid #c9a24a; }
.front .ar { font-family: Amiri, serif; font-size: 64pt; line-height: 1.25; color: #e6c66e; margin-top: .35in; }
.front .by { font-family: Amiri, serif; font-size: 17pt; color: #d9c9a0; }
.front h1 { word-break: keep-all; line-break: strict; font-family: var(--title-font); font-size: 27pt; line-height: 1.25; margin-top: .25in; color: #fbf4e0; }
.front .sub { font-family: var(--title-font); font-size: 12.5pt; color: #e8dcbc; margin-top: .06in; }
.front .vol { margin-top: .28in; display: inline-block; border: 1pt solid #c9a24a; border-radius: 3pt; padding: .05in .22in;
              font-family: var(--title-font); font-size: 14pt; color: #e6c66e; }
.front .vol-ar { font-family: Amiri, serif; font-size: 17pt; color: #e6c66e; margin-top: .04in; }
.front .feat { font-family: var(--title-font); font-size: 9.5pt; color: #d9c9a0; margin-top: .22in; max-width: 4.2in; }
.front .spacer { flex: 1; display: flex; align-items: center; justify-content: center; }
.front .orn { width: 1.35in; height: 1.35in; opacity: .9; }
.front .ed { font-family: var(--title-font); font-size: 10pt; color: #d9c9a0; }
.front .ed b { display: block; font-size: 13pt; color: #fbf4e0; }
.front .logo { width: 0.95in; margin-top: .14in; }
.front .draft { position: absolute; top: calc(var(--bleed) + 0.36in); left: 0; right: var(--bleed); text-align: center;
                font-family: var(--title-font); font-size: 7.5pt; color: #ffb3a7; }
.back h2 { font-family: var(--title-font); font-size: 13pt; color: #e6c66e; line-height: 1.4; margin-bottom: .12in; }
.back .desc { font-family: var(--title-font); font-size: 9.2pt; line-height: 1.55; color: #f3ead2; }
.back .desc p { margin-bottom: .08in; } .back .desc ul { margin: 0 0 .08in 1.1em; } .back .desc li { margin-bottom: .03in; }
.back .ar { font-family: Amiri, serif; font-size: 15pt; color: #e6c66e; direction: rtl; line-height: 1.8; margin: .1in 0; }
.back .pub { position: absolute; left: calc(var(--bleed) + 0.55in); bottom: calc(var(--bleed) + 0.5in); display: flex; align-items: center; gap: .12in;
             font-family: var(--title-font); font-size: 8.5pt; color: #d9c9a0; }
.back .pub img { width: .75in; }
.barcode { position: absolute; right: calc(0.25in); bottom: calc(var(--bleed) + 0.25in); width: var(--bw); height: var(--bh); background: #fff; }
.saw { font-family: Amiri, serif; }
/* eBook cover (front only) */
.ebook .front { width: 100%; padding: 0.5in; }
.ebook .frame { inset: 0.28in; }
.ebook .front .draft { top: 0.36in; right: 0; }
"""


def cover_front(code, vol, ed, pub, prof, draft, logo):
    volt = pub["volumes"][str(vol)]["title"]
    return f'''<div class="panel front"><div class="frame"></div>
{f'<div class="draft">{e(prof["draft_notice"].split(" · ")[0])}</div>' if draft else ""}
<div class="ar" lang="ar" dir="rtl">الْمُوَطَّأ</div>
<div class="by" lang="ar" dir="rtl">لِلْإِمَامِ مَالِكِ بْنِ أَنَسٍ</div>
<h1>{e(ed["title"])}</h1>
<div class="sub">{e(ed["subtitle"])}</div>
<div class="vol">{e(vol_label(ed, vol, prof))} · {e(volt[code])}</div>
<div class="vol-ar" lang="ar" dir="rtl">{e(volt["ar"])}</div>
<div class="feat">{e(ed["cover_features"])}</div>
<div class="spacer"><svg class="orn" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<g fill="none" stroke="#c9a24a"><rect x="25" y="25" width="70" height="70" stroke-width="2.2"/>
<rect x="25" y="25" width="70" height="70" stroke-width="2.2" transform="rotate(45 60 60)"/>
<circle cx="60" cy="60" r="22" stroke-width="1.2"/><circle cx="60" cy="60" r="16" stroke-width="0.8"/>
<rect x="38" y="38" width="44" height="44" stroke-width="0.8" transform="rotate(22.5 60 60)"/>
<rect x="38" y="38" width="44" height="44" stroke-width="0.8" transform="rotate(67.5 60 60)"/></g>
<circle cx="60" cy="60" r="4" fill="#c9a24a"/></svg></div>
<div class="ed">{e(ed["labels"]["editor"])}<b>{e(pub["editor"][code])}</b></div>
<img class="logo" src="file://{logo}" alt="">
</div>'''


def build_cover(code, vol, ed, pub, prof, pages, draft, outdir):
    pr = pub["print"]
    tw, th = pr["trim_in"]
    bleed = pr["bleed_in"]
    spine = round(pages * pr["spine_in_per_page"][pr["paper"]], 4)
    W, H = round(2 * tw + spine + 2 * bleed, 4), round(th + 2 * bleed, 4)
    logo = os.path.join(ROOT, pub["publisher"]["logo"])
    text_font = prof["fonts"]["text"]
    fams = list(dict.fromkeys(["Amiri", text_font, "Noto Serif"]))
    isbn = ed["isbn"].get("paperback")
    barcode = ean13_svg(isbn, isbn) if isbn else ""
    spine_txt = ""
    if pages >= pr["spine_text_min_pages"]:
        spine_txt = f'<span>{e(ed["title"])} · {e(vol_label(ed, vol, prof))} · {e(pub["publisher"]["name"][code])}</span>'
    back = f'''<div class="panel back">
<h2>{e(ed["title"])} — {e(ed["subtitle"])}</h2>
<div class="desc">{saw(ed["description_html"])}</div>
<div class="pub"><img src="file://{logo}" alt=""><div>{e(pub["publisher"]["name"][code])}<br>{e(pub["publisher"]["website"])}</div></div>
<div class="barcode">{barcode}</div>
</div>'''
    vars_ = (f':root {{ --w:{W}in; --h:{H}in; --panel:{tw + bleed}in; --spine:{spine}in; --bleed:{bleed}in; '
             f'--bw:{pr["barcode_box_in"][0]}in; --bh:{pr["barcode_box_in"][1]}in; --title-font:"{text_font}", "Noto Serif", serif; }}')
    doc = f'''<!doctype html><html lang="{code}"><head><meta charset="utf-8"><title>cover</title>
{BB.font_links(fams, "local")}<style>{vars_}{COVER_CSS}@page {{ size: {W}in {H}in; margin: 0; }}</style></head>
<body><div class="wrap">{back}<div class="panel spine">{spine_txt}</div>{cover_front(code, vol, ed, pub, prof, draft, logo)}</div></body></html>'''
    p = os.path.join(outdir, "cover.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(doc)
    subprocess.run(["node", os.path.join(ROOT, "tools", "render_pdf.cjs"), p, os.path.join(outdir, "cover.pdf"), "", "cover"],
                   check=True)
    # Chromium rounds the page to whole CSS pixels; set the exact computed size (the difference is outer bleed only)
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    cp = os.path.join(outdir, "cover.pdf")
    w = PdfWriter(clone_from=PdfReader(cp))
    pg = w.pages[0]
    pg.mediabox = RectangleObject([0, float(pg.mediabox.top) - H * 72, W * 72, float(pg.mediabox.top)])
    pg.cropbox = pg.mediabox
    pg.trimbox = RectangleObject([bleed * 72, float(pg.mediabox.top) - (H - bleed) * 72, (W - bleed) * 72,
                                  float(pg.mediabox.top) - bleed * 72])
    pg.bleedbox = pg.mediabox
    with open(cp, "wb") as f:
        w.write(f)
    # eBook cover: front panel only, 1600 x 2560 px
    ebook = f'''<!doctype html><html lang="{code}"><head><meta charset="utf-8"><title>ebook cover</title>
{BB.font_links(fams, "local")}<style>{vars_.replace(f"--w:{W}in", "--w:6in").replace(f"--h:{H}in", "--h:9.6in")}{COVER_CSS}</style></head>
<body><div class="wrap ebook">{cover_front(code, vol, ed, pub, prof, draft, logo)}</div></body></html>'''
    pe = os.path.join(outdir, "ebook-cover.html")
    with open(pe, "w", encoding="utf-8") as f:
        f.write(ebook)
    subprocess.run(["node", os.path.join(ROOT, "tools", "render_pdf.cjs"), pe, os.path.join(outdir, "ebook-cover.png"), "",
                    "shot:576x921.6"], check=True)
    from PIL import Image
    im = Image.open(os.path.join(outdir, "ebook-cover.png")).convert("RGB").resize((1600, 2560), Image.LANCZOS)
    im.save(os.path.join(outdir, "ebook-cover.jpg"), quality=92)
    os.remove(os.path.join(outdir, "ebook-cover.png"))
    os.remove(p)
    os.remove(pe)
    return {"width_in": W, "height_in": H, "spine_in": spine, "spine_text": bool(spine_txt)}


# ------------------------------------------------------------------ EPUB 3
EPUB_CSS = """
body { font-family: TextFont, LatinFont, serif; line-height: 1.6; margin: 0 4%; }
h1, h2, h3 { color: #0b3d24; line-height: 1.3; }
.ar { font-family: ArabicFont, serif; text-align: right; font-size: 1.35em; line-height: 2.0; }
p.ar { margin: .3em 0 .4em; }
.pron { font-family: PronFont, LatinFont, sans-serif; color: #7a4b12; font-size: .9em; }
.chain { font-size: .85em; color: #555; }
.chain .lbl { font-weight: bold; }
.mean { margin: .35em 0; }
.entry { border-top: 1px solid #ccc; padding-top: .7em; margin-top: .8em; }
.entry header { margin-bottom: .2em; }
.num { font-weight: bold; color: #0b3d24; margin-right: .5em; }
.badge { font-size: .75em; color: #666; margin-right: .6em; }
.malik { border-left: 3px solid #0b3d24; padding-left: .8em; margin: .6em 0; background: #f6f1e6; }
.malik h4 { margin: .2em 0; font-size: .85em; color: #0b3d24; }
.notes { font-size: .82em; color: #555; }
.notes-lbl { font-size: .75em; color: #555; font-weight: bold; margin: .5em 0 0; }
.badge.weak { color: #a33; font-weight: bold; }
.book-head { text-align: center; margin: 1.5em 0; }
.book-head .ar { text-align: center; font-size: 1.6em; color: #0b3d24; }
.key { overflow: hidden; }
.key .k { display: inline-block; width: 5.5em; text-align: center; margin: 0 .2em .4em 0; vertical-align: top; }
.key .k.wide { width: 11.4em; }
.key .k .ar { display: block; text-align: center; font-size: 1.2em; line-height: 1.6; }
.key .kp { display: block; font-family: PronFont, LatinFont, sans-serif; color: #7a4b12; font-size: .8em; }
.title { text-align: center; margin-top: 2em; }
.title .ar-title { font-family: ArabicFont, serif; font-size: 2.6em; color: #0b3d24; }
.title .logo { width: 30%; max-width: 160px; margin: 1em auto; display: block; }
.draft { border: 1px solid #a33; color: #a33; padding: .4em; font-size: .85em; margin: 1em 0; }
.copyright { font-size: .85em; }
.copyright .logo { width: 22%; max-width: 110px; display: block; margin: 0 0 1em; }
.saw { font-family: ArabicFont, serif; }
"""


def woff2_to_ttf(src, dst, merge_with=None):
    from fontTools.ttLib import TTFont
    if merge_with:
        from fontTools.merge import Merger
        tmp = []
        for s in [src] + merge_with:
            f = TTFont(s)
            f.flavor = None
            t = dst + f".part{len(tmp)}.ttf"
            f.save(t)
            tmp.append(t)
        Merger().merge(tmp).save(dst)
        for t in tmp:
            os.remove(t)
    else:
        f = TTFont(src)
        f.flavor = None
        f.save(dst)


def epub_fonts(code):
    """-> list of (family, weight, filename, source(s))"""
    f = [("ArabicFont", 400, "amiri-400.ttf", ["amiri/files/amiri-arabic-400-normal.woff2"]),
         ("ArabicFont", 700, "amiri-700.ttf", ["amiri/files/amiri-arabic-700-normal.woff2"]),
         ("LatinFont", 400, "notoserif-latin-400.ttf", ["noto-serif/files/noto-serif-latin-400-normal.woff2",
                                                         "noto-serif/files/noto-serif-latin-ext-400-normal.woff2"]),
         ("LatinFont", 700, "notoserif-latin-700.ttf", ["noto-serif/files/noto-serif-latin-700-normal.woff2",
                                                         "noto-serif/files/noto-serif-latin-ext-700-normal.woff2"])]
    if code == "bn":
        f += [("TextFont", 400, "notoserifbengali-400.ttf", ["noto-serif-bengali/files/noto-serif-bengali-bengali-400-normal.woff2"]),
              ("TextFont", 700, "notoserifbengali-700.ttf", ["noto-serif-bengali/files/noto-serif-bengali-bengali-700-normal.woff2"]),
              ("PronFont", 400, "notosansbengali-400.ttf", ["noto-sans-bengali/files/noto-sans-bengali-bengali-400-normal.woff2"])]
    return f   # Japanese: e-readers ship full CJK fonts, so none are embedded (keeps the file small)


def xhtml(code, title, body, extra_head=""):
    return (f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{code}" xml:lang="{code}">\n'
            f'<head><meta charset="utf-8"/><title>{e(title)}</title><link rel="stylesheet" type="text/css" href="../css/style.css"/>'
            f'{extra_head}</head>\n<body>\n{body}\n</body>\n</html>\n')


def to_xhtml(fragment):
    """HTML fragment from build_book -> XHTML-safe (void elements closed)."""
    return re.sub(r"<(img|br|hr|meta|link)([^>]*?)(?<!/)>", r"<\1\2/>", fragment)


def build_epub(code, vol, ed, pub, prof, data, trs, draft, outdir):
    scheme = prof["pron_scheme"]
    warnings = []
    secs = book_sections(code, data, trs, prof, scheme, warnings)
    volt = pub["volumes"][str(vol)]["title"]
    isbn = ed["isbn"].get("ebook")
    ident = f"urn:isbn:{isbn_digits(isbn)}" if isbn else \
        "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, f"https://{pub['publisher']['website']}/muwatta/{code}/vol{vol}"))
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fonts = epub_fonts(code)
    tmp = os.path.join(outdir, "_epub")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(os.path.join(tmp, "fonts"))
    for fam, wt, fn, srcs in fonts:
        woff2_to_ttf(os.path.join(FS, srcs[0]), os.path.join(tmp, "fonts", fn), [os.path.join(FS, s) for s in srcs[1:]] or None)
    font_css = "".join(f'@font-face {{ font-family: {fam}; font-weight: {wt}; font-style: normal; src: url(../fonts/{fn}); }}\n'
                       for fam, wt, fn, _ in fonts)
    if code == "ja":
        font_css += "body { font-family: serif; } .pron { font-family: sans-serif; }\n"
    logo_src = os.path.join(ROOT, pub["publisher"]["logo_bn" if code == "bn" else "logo"])
    logo_en = os.path.join(ROOT, pub["publisher"]["logo"])
    files = {}   # path in OEBPS -> (bytes, media-type, id, properties)
    files["css/style.css"] = ((font_css + EPUB_CSS).encode(), "text/css", "css", None)
    files["images/cover.jpg"] = (open(os.path.join(outdir, "ebook-cover.jpg"), "rb").read(), "image/jpeg", "cover-img", "cover-image")
    files["images/logo.png"] = (open(logo_src, "rb").read(), "image/png", "logo", None)
    if logo_en != logo_src:
        files["images/logo-en.png"] = (open(logo_en, "rb").read(), "image/png", "logo-en", None)
    for fam, wt, fn, _ in fonts:
        files["fonts/" + fn] = (open(os.path.join(tmp, "fonts", fn), "rb").read(), "font/ttf", "f-" + fn.replace(".", "-"), None)
    logo_en_ref = "../images/logo-en.png" if logo_en != logo_src else "../images/logo.png"
    files["text/cover.xhtml"] = (xhtml(code, ed["title"], '<div style="text-align:center"><img src="../images/cover.jpg" alt="'
                                       + e(ed["title"]) + '" style="max-width:100%;height:auto"/></div>').encode(),
                                 "application/xhtml+xml", "cover", None)
    title_body = (f'<section class="title" epub:type="titlepage"><div class="ar-title" lang="ar" dir="rtl">الْمُوَطَّأ</div>'
                  f'<h1>{e(ed["title"])}</h1><p>{e(ed["subtitle"])}</p><p><b>{e(vol_label(ed, vol, prof))} · {e(volt[code])}</b></p>'
                  f'<p class="ar" lang="ar" dir="rtl" style="text-align:center">{e(volt["ar"])}</p>'
                  f'<p>{e(ed["labels"]["editor"])}: <b>{e(pub["editor"][code])}</b></p>'
                  f'<img class="logo" src="../images/logo.png" alt="{e(pub["publisher"]["name"][code])}"/>'
                  f'<p>{e(pub["publisher"]["name"][code])}</p>'
                  + (f'<p class="draft">{e(prof["draft_notice"])}</p>' if draft else "") + "</section>")
    files["text/title.xhtml"] = (xhtml(code, ed["title"], title_body).encode(), "application/xhtml+xml", "title", None)
    copy_body = (f'<section class="copyright" epub:type="copyright-page"><img class="logo" src="{logo_en_ref}" alt="{e(pub["publisher"]["name"]["en"])}"/>'
                 f'{to_xhtml(copyright_block(code, ed, pub, prof, trs, "ebook"))}</section>')
    files["text/copyright.xhtml"] = (xhtml(code, "©", copy_body).encode(), "application/xhtml+xml", "copyright", None)
    intro = prof.get("intro", {})
    files["text/intro.xhtml"] = (xhtml(code, intro.get("heading", ""), f'<section epub:type="introduction">{to_xhtml(intro_html(prof, scheme))}</section>').encode(),
                                 "application/xhtml+xml", "intro", None)
    toc = [("text/title.xhtml", ed["title"]), ("text/copyright.xhtml", "©"), ("text/intro.xhtml", intro.get("heading", ""))]
    for t, s in secs:
        fn = f"text/book-{t['book']:02d}.xhtml"
        body = to_xhtml(saw(s))
        files[fn] = (xhtml(code, t["title"], f'<section epub:type="chapter">{body}</section>').encode(),
                     "application/xhtml+xml", f"book{t['book']:02d}", None)
        toc.append((fn, f'{prof["labels"]["book"]} {digits(t["book"], prof)}: {t["title"]}'))
    nav_items = "".join(f'<li><a href="{os.path.basename(p)}">{e(lbl)}</a></li>' for p, lbl in toc)
    nav = (f'<nav epub:type="toc" id="toc"><h1>{e(ed["labels"]["contents"])}</h1><ol>{nav_items}</ol></nav>'
           f'<nav epub:type="landmarks" hidden="hidden"><ol><li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
           f'<li><a epub:type="bodymatter" href="{os.path.basename(toc[3][0])}">Start</a></li></ol></nav>')
    files["text/nav.xhtml"] = (xhtml(code, ed["labels"]["contents"], nav).encode(), "application/xhtml+xml", "nav", "nav")
    # package document
    manifest = "".join(f'<item id="{i}" href="{p}" media-type="{mt}"' + (f' properties="{pr}"' if pr else "") + "/>\n"
                       for p, (_, mt, i, pr) in files.items())
    spine_ids = ["cover", "title", "copyright", "intro"] + [f"book{t['book']:02d}" for t, _ in secs]
    spine = "".join(f'<itemref idref="{i}"/>\n' for i in spine_ids)
    series = pub["series"].get(code, pub["series"]["en"])
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{code}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{ident}</dc:identifier>
<dc:title id="t1">{e(ed["title"])}</dc:title>
<meta refines="#t1" property="title-type">main</meta>
<dc:title id="t2">{e(ed["subtitle"])} — {e(vol_label(ed, vol, prof))}: {e(volt[code])}</dc:title>
<meta refines="#t2" property="title-type">subtitle</meta>
<dc:creator id="aut">{e(pub["author"].get(code, pub["author"]["en"]))}</dc:creator>
<meta refines="#aut" property="role" scheme="marc:relators">aut</meta>
<meta refines="#aut" property="file-as">Malik ibn Anas</meta>
<dc:contributor id="edt">{e(pub["editor"][code])}</dc:contributor>
<meta refines="#edt" property="role" scheme="marc:relators">edt</meta>
<meta refines="#edt" property="file-as">{e(pub["editor"]["en"])}</meta>
<dc:publisher>{e(pub["publisher"]["name"]["en"])}</dc:publisher>
<dc:rights>© {pub["year"]} {e(pub["copyright_holder"])}. All rights reserved.</dc:rights>
<dc:language>{code}</dc:language>
<dc:language>ar</dc:language>
<dc:date>{pub["year"]}</dc:date>
<dc:subject>Hadith</dc:subject>
<dc:subject>Islamic law (Maliki)</dc:subject>
<dc:description>{e(re.sub("<[^>]+>", " ", ed["description_html"]).strip())}</dc:description>
<meta property="belongs-to-collection" id="series">{e(series)}</meta>
<meta refines="#series" property="collection-type">series</meta>
<meta refines="#series" property="group-position">{vol}</meta>
<meta property="dcterms:modified">{modified}</meta>
<meta name="cover" content="cover-img"/>
</metadata>
<manifest>
{manifest}</manifest>
<spine page-progression-direction="ltr">
{spine}</spine>
</package>
'''
    container = ('<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                 '<rootfiles><rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>\n')
    out = os.path.join(outdir, "ebook.epub")
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/package.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        for p, (b, _, _, _) in files.items():
            z.writestr("OEBPS/" + p, b, compress_type=zipfile.ZIP_DEFLATED)
    shutil.rmtree(tmp, ignore_errors=True)
    return ident


# ------------------------------------------------------------------ metadata + guide
BISAC_NAMES = {"REL037020": "RELIGION / Islam / Koran & Sacred Writings", "REL037030": "RELIGION / Islam / Law",
               "REL037040": "RELIGION / Islam / Rituals & Practice"}


def write_meta_and_guide(code, vol, ed, pub, prof, trs, pages, cover, missing, outdir):
    volt = pub["volumes"][str(vol)]["title"]
    meta = {
        "language_edition": code,
        "volume": vol,
        "books_of_muwatta": pub["volumes"][str(vol)]["books"],
        "title": ed["title"],
        "subtitle": f'{ed["subtitle"]} — {vol_label(ed, vol, prof)}: {volt[code]}',
        "title_english": f'{ed["title_en"]}, Volume {vol}: {volt["en"]}',
        "series": pub["series"].get(code, pub["series"]["en"]), "series_number": vol,
        "author": pub["author"]["en"], "author_local": pub["author"].get(code),
        "editor": pub["editor"]["en"], "editor_local": pub["editor"].get(code),
        "publisher": pub["publisher"]["name"]["en"], "imprint": pub["publisher"]["name"]["en"],
        "copyright": f'© {pub["year"]} {pub["copyright_holder"]}. All rights reserved.',
        "publication_year": pub["year"], "edition": pub["edition"],
        "languages": [code, "ar"],
        "isbn": ed["isbn"],
        "description_html": ed["description_html"], "description_en_html": ed["description_en_html"],
        "keywords": ed["keywords"],
        "bisac": [{"code": c, "name": BISAC_NAMES.get(c, "")} for c in ed["bisac"]],
        "audience": "General / adult", "contains_ai_generated_text": True,
        "price_suggestion": ed.get("price_suggestion"),
        "print": {"trim": "6 x 9 in", "pages": pages, "interior": "black & white, no bleed", "paper": pub["print"]["paper"],
                  "cover_pdf_in": [cover["width_in"], cover["height_in"]], "spine_in": cover["spine_in"]},
        "ebook": {"format": "EPUB 3", "cover": "1600 x 2560 px JPG"},
        "ready_for_upload": not missing, "missing": missing,
    }
    with open(os.path.join(outdir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    kw = "\n".join(f"{i}. {k}" for i, k in enumerate(ed["keywords"], 1))
    bis = "\n".join(f"- {c} {BISAC_NAMES.get(c, '')}" for c in ed["bisac"])
    miss = "\n".join(f"- [ ] {m}" for m in missing) if missing else "- nothing: ready to upload"
    lang_name = prof["name_en"]
    guide = f"""# Publishing guide — {meta['title_english']}

**Publisher:** {pub['publisher']['name']['en']} ({pub['publisher']['imprint_of']['en']}) · **Editor:** {pub['editor']['en']} ·
**Copyright:** {meta['copyright']}

## Before you upload

{miss}

The files below are already in their final store format. When the items above are done, rebuild with
`python3 tools/build_release.py {code} --volume {vol}`: the ISBNs appear on the copyright page, an EAN-13 barcode is drawn on
the back cover, and the review-draft notices disappear once every book of the volume has `reviewed_by`.

## Files

| File | Use | Spec |
|---|---|---|
| `interior.pdf` | paperback interior (KDP, IngramSpark, Lulu, local printers) | {pages} pages · 6 × 9 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | paperback full-wrap cover | {cover['width_in']} × {cover['height_in']} in · 0.125 in bleed · spine {cover['spine_in']} in ({pages} pp × {pub['print']['spine_in_per_page'][pub['print']['paper']]}, {pub['print']['paper']} paper) · barcode area 2 × 1.2 in at the bottom right of the back |
| `ebook.epub` | eBook (Kindle via KDP, Google Play Books, Apple Books, Kobo, Draft2Digital) | EPUB 3, validated with EPUBCheck, fonts embedded{' (Japanese text uses the reader’s own fonts)' if code == 'ja' else ''} |
| `ebook-cover.jpg` | eBook cover | 1600 × 2560 px |
| `metadata.json` | every listing field below, machine-readable | |

## ISBNs (space is reserved)

- Each **format** needs its own ISBN: paperback, eBook, and hardcover if you make one. Each language edition and each volume also needs its own.
- To show **{pub['publisher']['name']['en']}** as the publisher everywhere, buy ISBNs in the publisher's name. In Bangladesh they come from the
  National ISBN Agency (Archives & Libraries Directorate). Enter them in `standard/publishing.json` → `editions.{code}.isbn`.
- KDP and IngramSpark offer free ISBNs, but KDP's then lists the imprint as "Independently published" and can only be used on Amazon.
  Google Play Books, Apple Books and Kobo do not require an ISBN for eBooks.
- KDP adds the barcode itself if you leave the white box empty. IngramSpark needs the barcode on the cover, so enter the ISBN and rebuild.

## Listing details (all stores)

- **Title:** {meta['title']}
- **Subtitle:** {meta['subtitle']}
- **English title (for international listings / IngramSpark):** {meta['title_english']}
- **Series:** {meta['series']} · **Number:** {vol} · **Edition:** {pub['edition']}
- **Contributors:** Author — {pub['author']['en']} · Editor — {pub['editor']['en']}
- **Publisher / imprint:** {pub['publisher']['name']['en']}
- **Language:** {lang_name} (with Arabic) · **Audience:** adult / general
- **Copyright:** {meta['copyright']} · **Publishing rights:** "I own the copyright and hold the necessary publishing rights" — the
  Arabic original is public domain; the translation, pronunciation, notes and design belong to the publisher.
- **Categories (BISAC):**
{bis}
- **Keywords (KDP has 7 boxes):**
{kw}
- **Description:** `description_html` in `metadata.json` (in {lang_name}); `description_en_html` for English-language stores.
- **AI disclosure (KDP asks this):** Text — **AI-generated** (the translation from Arabic was made with AI assistance), edited by the
  editor and checked by the named scholarly reviewer. Images — none (cover is typographic).
- **Suggested prices:** {json.dumps(ed.get('price_suggestion'), ensure_ascii=False)} — check each store's printing-cost calculator first.

## Store by store

1. **Amazon KDP** (kdp.amazon.com), for the paperback and the Kindle eBook on every Amazon marketplace.
   - Paperback: black & white interior, {pub['print']['paper']} paper, 6 × 9 in, no bleed, matte cover. Upload `interior.pdf` and `cover.pdf`.
     Turn on **Expanded Distribution** for bookstores and libraries, unless you use IngramSpark.
   - Kindle eBook: upload `ebook.epub` and `ebook-cover.jpg`. Choose worldwide territories (you hold worldwide rights).
   - Check that {lang_name} is on KDP's current list of supported languages for each format. Where a format is not supported, sell it
     through the stores below.
2. **IngramSpark** (ingramspark.com), for the paperback (and hardcover) in bookstores worldwide (40,000+ retailers and libraries).
   - Upload the same `interior.pdf`. Make the cover with IngramSpark's cover template generator for the exact page count, or reuse
     `cover.pdf` if its spine matches their calculator.
3. **Google Play Books** (play.google.com/books/publish): upload `ebook.epub` and the cover JPG. Sold in 75+ countries.
4. **Apple Books** (authors.apple.com): upload `ebook.epub` with Apple Books for Authors.
5. **Kobo Writing Life** (kobo.com/writinglife): upload `ebook.epub`. This reaches Rakuten Kobo{', including Japan' if code == 'ja' else ''}.
6. **Draft2Digital** (draft2digital.com), optional: one upload of `ebook.epub` distributes to many smaller stores and libraries.
{'7. **Rokomari** (rokomari.com) and other Bangladeshi stores: supply printed copies (from a local printer using `interior.pdf`/`cover.pdf`) through the publisher seller account.' if code == 'bn' else '7. **Amazon.co.jp** is covered by KDP; also consider **BookWalker** and **honto** for Japanese eBooks (through a distributor that accepts EPUB).'}

## Proof before release

1. Order one printed proof from KDP (or IngramSpark) and read it cover to cover.
2. Open `ebook.epub` in Kindle Previewer (Amazon's free tool) and in Apple Books or Thorium Reader. Check the Arabic,
   the {lang_name} text, the pronunciation line and ﷺ.
"""
    with open(os.path.join(outdir, "PUBLISHING-GUIDE.md"), "w", encoding="utf-8") as f:
        f.write(guide)


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("code")
    ap.add_argument("--volume", type=int, default=1)
    a = ap.parse_args()
    code, vol = a.code, a.volume
    pub = load("standard/publishing.json")
    ed = pub["editions"].get(code) or sys.exit(f"no edition '{code}' in standard/publishing.json")
    prof = load(f"standard/profiles/{code}.json")
    data = load("data/arabic/muwatta.json")
    books = pub["volumes"][str(vol)]["books"]
    trs = []
    for b in books:
        p = os.path.join(ROOT, "translations", code, f"book-{b:02d}.json")
        if not os.path.exists(p):
            sys.exit(f"volume {vol} needs translations/{code}/book-{b:02d}.json")
        trs.append(load(os.path.relpath(p, ROOT)))
    for k in ("paperback", "ebook", "hardcover"):
        isbn_digits(ed["isbn"].get(k))   # validate any ISBN given
    missing = status(code, vol, trs, ed)
    draft = any("scholarly review" in m for m in missing)
    outdir = os.path.join(ROOT, "editions", code, "release", f"vol{vol:02d}")
    os.makedirs(outdir, exist_ok=True)
    pages, warns = print_interior(code, vol, ed, pub, prof, data, trs, draft, outdir)
    cover = build_cover(code, vol, ed, pub, prof, pages, draft, outdir)
    ident = build_epub(code, vol, ed, pub, prof, data, trs, draft, outdir)
    write_meta_and_guide(code, vol, ed, pub, prof, trs, pages, cover, missing, outdir)
    print(f"{code} vol {vol}: interior {pages} pp, cover {cover['width_in']}x{cover['height_in']} in (spine {cover['spine_in']} in), "
          f"epub {ident}, pronunciation warnings {len(warns)}")
    print("ready for upload:", "YES" if not missing else "no — " + "; ".join(missing))
    print("->", os.path.relpath(outdir, ROOT))


if __name__ == "__main__":
    main()
