#!/usr/bin/env python3
"""Build a bilingual edition (Arabic + one language) as HTML and PDF.

    python3 tools/build_book.py bn                 # every book that has a translation, local fonts, HTML + PDF
    python3 tools/build_book.py ja --books 1       # only Book 1
    python3 tools/build_book.py bn --fonts google  # HTML that loads Google Fonts (for sharing as a web page)

Output: editions/<code>/muwatta-<code>[-bookNN].html / .pdf
Needs: `cd tools && npm install` (fonts) and the preinstalled Playwright + Chromium (for the PDF).
"""
import argparse, html, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))
from scripts import pronounce, SCHEMES  # noqa: E402

FONT_CSS = {   # family -> fontsource css files (local) / Google Fonts family spec
    "Amiri": (["amiri/arabic-400.css", "amiri/arabic-700.css", "amiri/latin-400.css"], "Amiri:wght@400;700"),
    "Noto Serif Bengali": (["noto-serif-bengali/bengali-400.css", "noto-serif-bengali/bengali-700.css"],
                           "Noto+Serif+Bengali:wght@400;700"),
    "Noto Sans Bengali": (["noto-sans-bengali/bengali-400.css", "noto-sans-bengali/bengali-600.css"],
                          "Noto+Sans+Bengali:wght@400;600"),
    "Noto Serif JP": (["noto-serif-jp/400.css", "noto-serif-jp/700.css"], "Noto+Serif+JP:wght@400;700"),
    "Noto Sans JP": (["noto-sans-jp/400.css", "noto-sans-jp/500.css"], "Noto+Sans+JP:wght@400;500"),
    "Noto Serif": (["noto-serif/latin-400.css", "noto-serif/latin-ext-400.css", "noto-serif/latin-700.css",
                    "noto-serif/latin-400-italic.css"], "Noto+Serif:ital,wght@0,400;0,700;1,400"),
}

TYPE_KEYS = ("marfu", "mawquf", "maqtu", "malik")
e = html.escape


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def digits(s, prof):
    d = prof.get("digits", "0123456789")
    return str(s).translate(str.maketrans("0123456789", d))


def arabic_display(ar):
    """Arabic for print: straight quotes -> « » (alternating), no space inside the guillemets."""
    out, opened = [], False
    for part in re.split(r'(")', ar):
        if part == '"':
            out.append("»" if opened else "«")
            opened = not opened
        else:
            out.append(part)
    t = "".join(out)
    return re.sub(r"«\s+", "«", re.sub(r"\s+»", "»", t))


def font_links(families, mode):
    if mode == "google":
        q = "&".join("family=" + FONT_CSS[f][1] for f in families)
        return f'<link rel="preconnect" href="https://fonts.googleapis.com">\n' \
               f'<link href="https://fonts.googleapis.com/css2?{q}&display=swap" rel="stylesheet">'
    base = os.path.join(ROOT, "tools", "node_modules", "@fontsource")
    if not os.path.isdir(base):
        sys.exit("fonts missing: run `cd tools && npm install`")
    links = []
    for f in families:
        for css in FONT_CSS[f][0]:
            p = os.path.join(base, css)
            if os.path.exists(p):
                links.append(f'<link rel="stylesheet" href="file://{p}">')
    return "\n".join(links)


def pron_key(scheme, prof):
    samples = ["بَا", "تَا", "ثَا", "جَا", "حَا", "خَا", "دَا", "ذَا", "رَا", "زَا", "سَا", "شَا", "صَا", "ضَا",
               "طَا", "ظَا", "عَا", "غَا", "فَا", "قَا", "كَا", "لَا", "مَا", "نَا", "هَا", "وَا", "يَا", "أَا"]
    cells = "".join(f'<div class="k"><span class="ar">{e(s)}</span><span class="kp">{e(pronounce(s, scheme))}</span></div>'
                    for s in samples[:-1])
    rules = ["بِي", "بُو", "بَيْت", "يَوْم", "الشَّمْس", "الْقَمَر", "فِي الْبَيْتِ", "بِسْمِ اللَّهِ", "مَدْرَسَة"]
    rows = "".join(f'<div class="k wide"><span class="ar">{e(s)}</span><span class="kp">{e(pronounce(s, scheme))}</span></div>'
                   for s in rules)
    return f'<div class="key">{cells}</div><div class="key">{rows}</div>'


def entry_html(ent, tr, prof, scheme, warnings):
    lab = prof["labels"]
    segs = ent["segments"]
    riwaya = " ".join(s["ar"] for s in segs if s["kind"] == "riwaya")
    malik = " ".join(s["ar"] for s in segs if s["kind"] == "malik")
    head_bits = []
    if ent.get("type") in TYPE_KEYS:
        head_bits.append(f'<span class="badge t-{ent["type"]}">{e(lab["types"][ent["type"]])}</span>')
    graders = ent.get("graders") or ([{"name": None, "grade": ent["grade"]}] if ent.get("grade") else [])
    for gr in graders:   # protocol: every grade is shown with its grader
        g = prof.get("grades", {}).get(gr["grade"], gr["grade"])
        who = prof.get("graders", {}).get(gr["name"], gr["name"]) if gr["name"] else ""
        head_bits.append(f'<span class="badge g">{e(lab["grade"])}: {e(g)}{(" — " + e(who)) if who else ""}</span>')
        low = gr["grade"].lower()
        if "daif" in low or "munkar" in low or "shadh" in low:
            head_bits.append(f'<span class="badge weak">{e(prof["weak_label"].replace("{grader}", who))}</span>')
        if "mawdu" in low:
            head_bits.append(f'<span class="badge weak">{e(prof["fabricated_label"].replace("{grader}", who))}</span>')
    out = [f'<article class="entry" id="e{ent["n"]}">',
           f'<header><span class="num">{digits(ent["nb"], prof)}</span>{"".join(head_bits)}</header>']

    def block(ar, meaning, chain=None):
        b = []
        if ar:
            b.append(f'<p class="ar" lang="ar" dir="rtl">{e(arabic_display(ar))}</p>')
            if scheme in SCHEMES:
                w = []
                b.append(f'<p class="pron">{e(pronounce(ar, scheme, w))}</p>')
                warnings.extend(f"entry {ent['n']}: {x}" for x in w)
        if chain:
            b.append(f'<p class="chain"><span class="lbl">{e(lab["chain"])}:</span> {" ← ".join(e(c) for c in chain)}</p>')
        if meaning:
            for para in meaning.split("\n"):
                b.append(f'<p class="mean">{e(para)}</p>')
        return "".join(b)

    if riwaya:
        out.append(block(riwaya, tr.get("text"), tr.get("chain")))
    if malik:
        out.append(f'<section class="malik"><h4>{e(lab["malik"])}</h4>{block(malik, tr.get("malik"))}</section>')
    if tr.get("notes"):
        items = "".join(f"<li>{e(n)}</li>" for n in tr["notes"])
        out.append(f'<p class="notes-lbl">{e(lab["notes"])}</p><ol class="notes" aria-label="{e(lab["notes"])}">{items}</ol>')
    out.append("</article>")
    return "\n".join(out)


CSS = """
@page { size: A5; margin: 16mm 14mm 18mm 14mm; }
:root { --ink:#1d1b18; --muted:#6b645a; --pron:#7a4b12; --rule:#d9d2c5; --accent:#0f5c4d; --bg:#fffdf8; --malik:#f4efe4; }
* { box-sizing: border-box; }
html { background: var(--bg); }
body { margin: 0 auto; max-width: 46rem; padding: 0 16px 48px; color: var(--ink); background: var(--bg);
       font-family: var(--text-font); font-size: 11pt; line-height: 1.6; }
.title { min-height: 92vh; display: flex; flex-direction: column; justify-content: center; text-align: center; break-after: page; }
.title .ar-title { font-family: Amiri, serif; font-size: 34pt; line-height: 1.5; color: var(--accent); }
.title h1 { font-size: 22pt; margin: .3em 0; }
.title .sub { color: var(--muted); }
.draft { margin: 2em auto 0; padding: .6em 1em; border: 1.5px solid #a33; color: #a33; font-size: 9.5pt; max-width: 30em; }
.intro { break-after: page; }
.intro h2, .book-head h2 { color: var(--accent); }
.key { display: grid; grid-template-columns: repeat(auto-fill, minmax(5.2em, 1fr)); gap: 4px 8px; margin: .6em 0 1em; }
.key .k { display: flex; flex-direction: column; align-items: center; border-bottom: 1px solid var(--rule); padding: 2px 0; }
.key .k.wide { grid-column: span 2; }
.key .ar { font-family: Amiri, serif; font-size: 15pt; line-height: 1.4; }
.key .kp { font-family: var(--pron-font); color: var(--pron); font-size: 9.5pt; }
.book-head { text-align: center; margin: 1.2em 0 1.4em; break-before: page; }
.book-head .ar { font-family: Amiri, serif; font-size: 22pt; color: var(--accent); margin: 0; }
.book-head h2 { margin: .2em 0 0; }
.entry { border-top: 1px solid var(--rule); padding: .9em 0 .6em; break-inside: auto; }
.entry header { display: flex; flex-wrap: wrap; gap: .4em; align-items: center; margin-bottom: .3em; }
.num { font-weight: 700; color: #fff; background: var(--accent); border-radius: 999px; min-width: 1.9em; height: 1.9em;
       display: inline-flex; align-items: center; justify-content: center; font-size: 9.5pt; padding: 0 .4em; }
.badge { font-size: 8.5pt; color: var(--muted); border: 1px solid var(--rule); border-radius: 4px; padding: 0 .45em; }
p { margin: .35em 0; }
p.ar { font-family: Amiri, serif; font-size: 15.5pt; line-height: 2.05; text-align: justify; margin: .2em 0 .4em; }
p.pron { font-family: var(--pron-font); color: var(--pron); font-size: 9.6pt; line-height: 1.65; }
p.chain { font-size: 9pt; color: var(--muted); }
p.chain .lbl { font-weight: 700; }
p.mean { font-size: 11pt; }
.malik { background: var(--malik); border-left: 3px solid var(--accent); padding: .3em .8em .4em; margin: .6em 0; break-inside: avoid-page; }
.malik h4 { margin: .2em 0; font-size: 9.5pt; color: var(--accent); letter-spacing: .02em; }
.notes { font-size: 8.8pt; color: var(--muted); margin: .4em 0 0; padding-left: 1.4em; }
.notes-lbl { font-size: 7.8pt; color: var(--muted); margin: .5em 0 0; font-weight: 700; letter-spacing: .02em; }
.badge.weak { color: #a33; border-color: #e0b0b0; font-weight: 700; }
.notes li { margin: .1em 0; }
@media screen and (max-width: 520px) { p.ar { font-size: 14pt; } body { font-size: 10.5pt; } }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --ink:#ece6da; --muted:#a69d8f; --pron:#e0b070; --rule:#3a362f; --accent:#6cc4ad; --bg:#171512; --malik:#221f1a; }
}
:root[data-theme="dark"] { --ink:#ece6da; --muted:#a69d8f; --pron:#e0b070; --rule:#3a362f; --accent:#6cc4ad; --bg:#171512; --malik:#221f1a; }
@media print { body { max-width: none; padding: 0; background: #fff; } :root { --bg:#fff; } }
"""


def build(code, books_filter, font_mode, make_pdf):
    prof = load(os.path.join(ROOT, "standard", "profiles", code + ".json"))
    data = load(os.path.join(ROOT, "data", "arabic", "muwatta.json"))
    tdir = os.path.join(ROOT, "translations", code)
    files = sorted(f for f in os.listdir(tdir) if re.fullmatch(r"book-\d\d\.json", f))
    trs = [load(os.path.join(tdir, f)) for f in files]
    if books_filter:
        trs = [t for t in trs if t["book"] in books_filter]
    if not trs:
        sys.exit("no translations for %s" % code)
    scheme = prof["pron_scheme"]
    books = {b["n"]: b for b in data["books"]}
    warnings, problems = [], []
    body = []
    body.append(f'''<section class="title">
<div class="ar-title" lang="ar" dir="rtl">الْمُوَطَّأ</div>
<h1>{e(prof["title"])}</h1>
<div class="sub">{e(prof["subtitle"])}</div>
<div class="sub">{e(data["title_en"])}</div>
<div class="draft">{e(prof["draft_notice"])}</div>
</section>''')
    intro = prof.get("intro")
    if intro:
        paras = "".join(f"<p>{e(p)}</p>" for p in intro["paras"])
        body.append(f'<section class="intro"><h2>{e(intro["heading"])}</h2>{paras}'
                    f'<h3>{e(prof["labels"]["pron"])}</h3>{pron_key(scheme, prof) if scheme in SCHEMES else ""}</section>')
    for t in trs:
        b = books[t["book"]]
        ar_entries = [x for x in data["entries"] if x["book"] == t["book"]]
        tmap = {x["n"]: x for x in t["entries"]}
        missing = [x["n"] for x in ar_entries if x["n"] not in tmap]
        extra = [n for n in tmap if n not in {x["n"] for x in ar_entries}]
        if missing or extra:
            problems.append(f"book {t['book']}: missing {missing} extra {extra}")
        body.append(f'<section class="book-head"><p class="ar" lang="ar" dir="rtl">{e(b["ar"])}</p>'
                    f'<h2>{e(prof["labels"]["book"])} {digits(t["book"], prof)}: {e(t["title"])}</h2></section>')
        for x in ar_entries:
            tr = tmap.get(x["n"], {})
            if tr and tr.get("nb") != x["nb"]:
                problems.append(f"entry {x['n']}: nb {tr.get('nb')} != {x['nb']}")
            if any(s["kind"] == "malik" for s in x["segments"]) and not tr.get("malik"):
                problems.append(f"entry {x['n']}: Malik's commentary not translated")
            body.append(entry_html(x, tr, prof, scheme, warnings))
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1)

    fams = ["Amiri", prof["fonts"]["text"], prof["fonts"]["pron"], "Noto Serif"]
    fams = list(dict.fromkeys(f for f in fams if f in FONT_CSS))
    text_stack = f'"{prof["fonts"]["text"]}", "Noto Serif", Amiri, serif'
    pron_stack = f'"{prof["fonts"]["pron"]}", "Noto Serif", Amiri, sans-serif'
    title = f'{prof["title"]} — {prof["name"]}'
    doc = f'''<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(prof.get("short_title", prof["title"]))}</title>
{font_links(fams, font_mode)}
<style>:root {{ --text-font: {text_stack}; --pron-font: {pron_stack}; }}{CSS}</style>
</head>
<body>
{chr(10).join(body)}
</body>
</html>'''
    outdir = os.path.join(ROOT, "editions", code)
    os.makedirs(outdir, exist_ok=True)
    suffix = "" if not books_filter else "-book" + "-".join("%02d" % b for b in sorted(books_filter))
    if font_mode == "google":
        suffix += "-web"
    base = os.path.join(outdir, f"muwatta-{code}{suffix}")
    with open(base + ".html", "w", encoding="utf-8") as f:
        f.write(doc)
    print("html:", os.path.relpath(base + ".html", ROOT), f"({len(warnings)} pronunciation warnings)")
    for w in warnings[:10]:
        print("  ", w)
    if make_pdf and font_mode == "local":
        footer = prof["draft_notice"].split(" · ")[0]
        js = os.path.join(ROOT, "tools", "render_pdf.cjs")
        subprocess.run(["node", js, base + ".html", base + ".pdf", footer], check=True)
        print("pdf: ", os.path.relpath(base + ".pdf", ROOT))
    return title


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("code")
    ap.add_argument("--books", default="")
    ap.add_argument("--fonts", choices=["local", "google"], default="local")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    books = {int(x) for x in a.books.split(",") if x.strip()}
    build(a.code, books, a.fonts, not a.no_pdf)


if __name__ == "__main__":
    main()
