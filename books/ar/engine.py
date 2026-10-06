# -*- coding: utf-8 -*-
"""Page engine for the ভাষার দরজা series (7 x 10 in, no bleed). Content modules call page() in order;
build.py numbers the pages, fills the table of contents and writes book.html."""
import html as _html

BOOK_TITLE_BN = "আরবি ভাষার দরজা"
PAGES = []          # list of dicts: {html, cls, bg, folio_style, head, anchor}
ANCHORS = {}        # anchor -> page index (filled at build)

import re as _re
_AR = "\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF"
_AR_RUN = _re.compile("[%s](?:[%s\\s\u060C\u061F\u061B.!:()«»0-9\u0660-\u0669-]*[%s])?" % (_AR, _AR, _AR))
def E(s):
    """Escape text and wrap every Arabic run in an isolated right-to-left span (correct font, size and bidi)."""
    return _AR_RUN.sub(lambda m: '<span class="ar">%s</span>' % m.group(0), _html.escape(s or "", quote=False))

BN_DIG = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
def bn(n):
    return str(n).translate(BN_DIG)

def roman(n):
    vals = [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s; n -= v
    return out

BEFORE_FIXED_PAGE = []   # callbacks run before a page is added from outside the flow engine

def page(inner, cls="", bg=None, head=None, anchor=None, folio=True, front=False, anchors=None, _from_flow=False):
    if not _from_flow:
        for cb in BEFORE_FIXED_PAGE:
            cb()
    PAGES.append(dict(html=inner, cls=cls, bg=bg, head=head, anchor=anchor, anchors=anchors or [], folio=folio, front=front))

# ---------------------------------------------------------------- components
def fr(s):
    return '<span class="frw">%s</span>' % E(s)

def tr_table(items, tick=False, compact=False, start=1, numbered=True, show_note=True):
    """The Triple Row as a 5-column table."""
    rows = []
    for i, it in enumerate(items, start):
        note = ('<div class="note">%s</div>' % E(it.get("note_bn"))) if (show_note and it.get("note_bn")) else ""
        num = ('<td class="n">%s</td>' % bn(i)) if numbered else ""
        box = '<td class="tk">☐</td>' if tick else ""
        rows.append('<tr>%s%s<td class="c-fr">%s</td><td class="c-bp">%s</td><td class="c-ep">%s</td>'
                    '<td class="c-bn">%s%s</td><td class="c-en">%s</td></tr>' % (
                        box, num, E(it["fr"]), E(it["bn_pron"]), E(it["en_pron"]), E(it["bn"]), note, E(it["en"])))
    headn = '<th></th>' if numbered else ""
    headt = '<th></th>' if tick else ""
    w = ([0.2] if tick else []) + ([0.32] if numbered else [])
    rest = 5.56 - sum(w)
    w += [rest * f for f in (0.19, 0.23, 0.2, 0.2, 0.18)]
    cg = "<colgroup>%s</colgroup>" % "".join('<col style="width:%.2fin">' % x for x in w)
    return ('<table class="tr%s" style="table-layout:fixed;">' + cg + '<thead><tr>%s%s<th>العربية</th><th>বাংলা উচ্চারণ</th><th>Pronunciation</th>'
            '<th>বাংলা অর্থ</th><th>English</th></tr></thead><tbody>%s</tbody></table>') % (
                " compact" if compact else "", headt, headn, "".join(rows))

def tr_line(it, big=False):
    """A single Triple Row as a stacked block (for sentences and dialogue lines)."""
    return ('<div class="trl%s"><div class="l1">%s</div><div class="l2"><span class="bp">%s</span>'
            '<span class="ep">%s</span></div><div class="l3">%s <span class="en">/ %s</span></div></div>') % (
                " big" if big else "", E(it["fr"]), E(it["bn_pron"]), E(it["en_pron"]), E(it["bn"]), E(it["en"]))

def box(kind, title, body):
    icons = {"tip": "💡", "warn": "⚠️", "culture": "🌍", "link": "🔗", "know": "✨", "mission": "🎯"}
    return '<div class="box %s"><div class="bt">%s %s</div><div class="bb">%s</div></div>' % (
        kind, icons.get(kind, ""), E(title), body)

def star_svg(size=26):
    return ('<svg width="%d" height="%d" viewBox="0 0 40 40" aria-hidden="true"><rect x="9" y="9" width="22" height="22" '
            'fill="none" stroke="#b8892d" stroke-width="2"/><rect x="9" y="9" width="22" height="22" fill="none" '
            'stroke="#b8892d" stroke-width="2" transform="rotate(45 20 20)"/><circle cx="20" cy="20" r="4" '
            'fill="#174d33"/></svg>') % (size, size)

def h2(title):
    return '<h2>%s<span>%s</span></h2>' % (star_svg(22), title)

def chapter_title(no, title_bn, title_en):
    return ('<div class="chhead"><div class="chno">অধ্যায় %s</div><h1>%s</h1><div class="chen">%s</div></div>'
            % (bn(no), E(title_bn), E(title_en)))

def part_opener(no_bn, title_bn, title_en, purpose_bn, chapters, art=""):
    lis = "".join('<li><span class="cn">%s</span>%s</li>' % (E(a), E(b)) for a, b in chapters)
    return ('<div class="partop"><div class="pk">পর্ব %s</div><div class="pt">%s</div><div class="pe">%s</div>'
            '%s<div class="pp">%s</div><ul class="pl">%s</ul></div>') % (no_bn, E(title_bn), E(title_en), art, purpose_bn, lis)

# ---------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:"BnSerif";src:url(assets/fonts/noto-serif-bengali-bengali-400-normal.woff2);font-weight:400;}
@font-face{font-family:"BnSerif";src:url(assets/fonts/noto-serif-bengali-bengali-700-normal.woff2);font-weight:700;}
@font-face{font-family:"BnSans";src:url(assets/fonts/noto-sans-bengali-bengali-400-normal.woff2);font-weight:400;}
@font-face{font-family:"BnSans";src:url(assets/fonts/noto-sans-bengali-bengali-600-normal.woff2);font-weight:600;}
@font-face{font-family:"BnSans";src:url(assets/fonts/noto-sans-bengali-bengali-700-normal.woff2);font-weight:700;}
@font-face{font-family:"Lat";src:url(assets/fonts/noto-serif-latin-400-normal.woff2);font-weight:400;font-style:normal;}
@font-face{font-family:"Lat";src:url(assets/fonts/noto-serif-latin-700-normal.woff2);font-weight:700;font-style:normal;}
@font-face{font-family:"Lat";src:url(assets/fonts/noto-serif-latin-400-italic.woff2);font-weight:400;font-style:italic;}
@font-face{font-family:"LatX";src:url(assets/fonts/noto-serif-latin-ext-400-normal.woff2);font-weight:400;}
@font-face{font-family:"LatX";src:url(assets/fonts/noto-serif-latin-ext-700-normal.woff2);font-weight:700;}
@font-face{font-family:"Arabic";src:url(assets/fonts/amiri-arabic-400-normal.woff2);font-weight:400;}
@font-face{font-family:"Arabic";src:url(assets/fonts/amiri-arabic-700-normal.woff2);font-weight:700;}
:root{--ink:#22302d;--muted:#5d6b69;--brand:#174d33;--brand-l:#e7f0ea;--gold:#b8892d;--gold-l:#f6ecd6;
  --accent:#8b3a1a;--accent-l:#f7ebe3;--paper:#fbf7ef;--line:#d9cbb0;}
@page{size:7in 10in;margin:0;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{background:#9a9a9a;}
body{font-family:"Lat","LatX","BnSerif","Arabic",serif;color:var(--ink);font-size:11.2pt;line-height:1.6;}
.page{width:7in;height:10in;background:var(--paper);position:relative;overflow:hidden;margin:0 auto 0.25in;
  padding:0.78in 0.72in 0.82in;display:flex;flex-direction:column;page-break-after:always;}
@media print{html,body{background:none;}.page{margin:0;}}
p{margin:0 0 0.08in;text-align:justify;}
b,strong{font-weight:700;color:var(--brand);}
.frw{font-family:"Arabic",serif;color:var(--accent);font-weight:700;direction:rtl;unicode-bidi:isolate;font-size:1.18em;}
.ar{font-family:"Arabic",serif;direction:rtl;unicode-bidi:isolate;font-size:1.15em;line-height:1.4;}
.frw .ar,.c-fr .ar,.l1 .ar,.ar .ar{font-size:1em;}
.runhead{position:absolute;top:0.36in;left:0.72in;right:0.72in;display:flex;justify-content:space-between;
  font-family:"BnSans";font-weight:600;font-size:8.3pt;color:var(--muted);border-bottom:0.75pt solid var(--line);padding-bottom:0.04in;}
.folio{position:absolute;bottom:0.36in;left:0;right:0;text-align:center;font-family:"BnSans","Lat";font-weight:600;font-size:9pt;color:var(--gold);}
.folio::before,.folio::after{content:"";display:inline-block;width:0.5in;height:0.75pt;background:var(--line);vertical-align:middle;margin:0 0.12in;}
h1{font-family:"BnSans";font-weight:700;font-size:25pt;line-height:1.25;color:var(--brand);}
h2{font-family:"BnSans";font-weight:600;font-size:15pt;color:var(--brand);display:flex;align-items:center;gap:0.1in;margin:0.1in 0 0.07in;line-height:1.3;}
h2 span{flex:none;max-width:90%;}
h2::after{content:"";flex:1;height:0.75pt;background:linear-gradient(90deg,var(--gold),transparent);}
h3{font-family:"BnSans";font-weight:600;font-size:12.5pt;color:var(--accent);margin:0.08in 0 0.05in;}
.chhead{margin:0.06in 0 0.14in;padding-bottom:0.08in;border-bottom:2pt solid var(--gold);}
.chno{font-family:"BnSans";font-weight:600;color:var(--gold);font-size:11pt;}
.chen{font-family:"Lat";font-style:italic;color:var(--muted);font-size:11.5pt;}
.lead{font-size:12.2pt;line-height:1.65;}
.dropcap::first-letter{font-family:"BnSans";font-weight:700;float:left;font-size:32pt;line-height:1;color:var(--gold);padding:0.05in 0.08in 0 0;}
/* Triple Row table */
table.tr{width:100%;border-collapse:collapse;font-size:9.6pt;line-height:1.35;margin:0.04in 0 0.1in;}
table.tr th{font-family:"BnSans","Lat";font-weight:600;font-size:8pt;color:#fff;background:var(--brand);padding:0.04in 0.05in;text-align:left;}
table.tr td{padding:0.035in 0.05in;border-bottom:0.6pt solid var(--line);vertical-align:top;overflow-wrap:anywhere;}
table.tr tr:nth-child(even) td{background:#fffdf8;}
table.tr td.n{color:var(--gold);font-family:"BnSans";font-weight:600;width:0.25in;}
table.tr td.tk{width:0.18in;color:var(--muted);}
table.tr td.c-fr{font-family:"Arabic",serif;font-weight:700;color:var(--accent);direction:rtl;text-align:right;font-size:13.2pt;line-height:1.45;padding-top:0.01in;padding-bottom:0.01in;}
table.tr td.c-bp{font-family:"BnSerif";}
table.tr td.c-ep{font-family:"Lat";font-style:italic;color:var(--muted);font-size:8.8pt;}
table.tr td.c-en{font-family:"Lat";color:var(--muted);font-size:9pt;}
table.tr .note{font-size:8pt;color:var(--muted);font-family:"BnSans";}
table.tr.compact{font-size:9pt;}
table.tr.compact td.c-fr{font-size:12.5pt;}
table.tr.compact td{padding:0.025in 0.045in;}
/* Triple Row line */
.trl{border-left:3pt solid var(--accent);background:#fff;padding:0.045in 0.11in;margin:0 0 0.05in;border-radius:0 3pt 3pt 0;}
.trl .l1{font-family:"Arabic",serif;font-weight:700;color:var(--accent);font-size:15pt;line-height:1.55;direction:rtl;text-align:right;}
.trl .l2{font-size:10pt;line-height:1.4;}
.trl .l2 .bp{font-family:"BnSerif";margin-right:0.14in;}
.trl .l2 .ep{font-family:"Lat";font-style:italic;color:var(--muted);font-size:9.3pt;}
.trl .l3{font-size:10.3pt;line-height:1.45;}
.trl .l3 .en{font-family:"Lat";color:var(--muted);font-size:9.3pt;}
.trl.big .l1{font-size:19pt;}
/* boxes */
.box{border-radius:3pt;padding:0.08in 0.13in 0.05in;margin:0.05in 0 0.09in;}
.box .bt{font-family:"BnSans";font-weight:600;font-size:10.5pt;margin-bottom:0.03in;}
.box .bb{font-size:10.4pt;line-height:1.55;}
.box .bb p{margin-bottom:0.05in;}
.box.tip{background:var(--brand-l);} .box.tip .bt{color:var(--brand);}
.box.warn{background:#fbe9e4;} .box.warn .bt{color:#9a3b22;}
.box.culture{background:var(--accent-l);} .box.culture .bt{color:var(--accent);}
.box.link{background:var(--gold-l);} .box.link .bt{color:#8a6420;}
.box.know{background:#fff;border:1pt solid var(--gold);} .box.know .bt{color:#8a6420;}
.box.mission{background:#fff;border:1.5pt dashed var(--brand);} .box.mission .bt{color:var(--brand);}
/* part opener */
.partop{flex:1;display:flex;flex-direction:column;justify-content:center;text-align:center;}
.partop .pk{font-family:"BnSans";font-weight:600;color:var(--gold);font-size:14pt;}
.partop .pt{font-family:"BnSans";font-weight:700;color:var(--brand);font-size:34pt;line-height:1.25;margin:0.06in 0;}
.partop .pe{font-family:"Lat";font-style:italic;color:var(--muted);font-size:14pt;margin-bottom:0.25in;}
.partop .pp{font-size:12pt;line-height:1.75;margin:0.2in 0.3in;}
.partop .pl{list-style:none;margin:0.15in auto 0;text-align:left;font-family:"BnSans";font-size:12pt;width:80%;}
.partop .pl li{padding:0.06in 0;border-bottom:1pt dashed var(--line);}
.partop .pl .cn{display:inline-block;width:0.95in;color:var(--gold);font-weight:600;}
/* cards grid */
.cards{display:grid;grid-template-columns:1fr 1fr;gap:0.09in;margin:0.03in 0 0.08in;}
.card{background:#fff;border:0.75pt solid var(--line);border-top:3pt solid var(--gold);border-radius:3pt;padding:0.07in 0.11in 0.05in;}
.card .ct{font-family:"BnSans";font-weight:600;color:var(--brand);font-size:12pt;line-height:1.35;margin-bottom:0.03in;}
.card .cb{font-size:10.2pt;line-height:1.5;text-align:left;}
.card .ci{font-size:16pt;float:right;margin-left:0.06in;}
.small{font-size:9.5pt;color:var(--muted);line-height:1.55;}
.center{text-align:center;}
.spacer{flex:1;}
.cards.c3{grid-template-columns:1fr 1fr 1fr;gap:0.08in;}
.qz2{column-count:2;column-gap:0.2in;margin-bottom:0.04in;}
.qz2 > div{break-inside:avoid;}
.ans{transform:rotate(180deg);font-size:7.4pt;color:var(--muted);line-height:1.4;border-top:1pt solid var(--line);padding-top:0.03in;margin:0.04in 0 0.1in;}
"""

EXTRA_CSS = []

def render(extra_css=""):
    extra_css = extra_css + "".join(EXTRA_CSS)
    out = []
    main_no = 0
    front_no = 0
    for i, p in enumerate(PAGES):
        if p["front"]:
            front_no += 1; label = roman(front_no)
        else:
            main_no += 1; label = bn(main_no)
        p["label"] = label
        for a in ([p["anchor"]] if p["anchor"] else []) + p.get("anchors", []):
            ANCHORS[a] = label
    for p in PAGES:
        body = p["html"]
        if callable(body):
            body = body()
        for k, v in ANCHORS.items():
            body = body.replace("{{%s}}" % k, v)
        head = ('<div class="runhead"><span>%s</span><span>%s</span></div>' % (E(p["head"]), BOOK_TITLE_BN)) if p["head"] else ""
        fol = ('<div class="folio">%s</div>' % p["label"]) if p["folio"] else ""
        style = (' style="background:%s"' % p["bg"]) if p["bg"] else ""
        out.append('<div class="page %s"%s>%s%s%s</div>' % (p["cls"], style, head, body, fol))
    return ('<!DOCTYPE html><html lang="bn"><head><meta charset="utf-8"><title>%s — Introduction to Arabic</title>'
            '<style>%s%s</style></head><body>%s</body></html>') % (BOOK_TITLE_BN, CSS, extra_css, "".join(out))
