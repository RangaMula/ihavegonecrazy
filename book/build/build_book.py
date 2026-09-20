"""Assemble the book (EN or BN) from section files into one markdown and one HTML file with a TOC."""
import re, sys, pathlib, html, markdown

lang = sys.argv[1]  # en | bn
base = pathlib.Path(__file__).resolve().parent.parent
sec_dir = base / 'sections' / lang
order = ['front.md'] + [f'S{i:02d}.md' for i in range(1, 15)] + ['back.md']
parts = []
for name in order:
    p = sec_dir / name
    if not p.exists():
        import os
        if os.environ.get('ALLOW_MISSING'): print('skip', name); continue
        print('MISSING', p); sys.exit(1)
    txt = p.read_text(encoding='utf-8').strip() + '\n'
    if name.startswith('S'):
        txt = '\n---\n\n' + txt
    parts.append(txt)
md_text = '\n'.join(parts)
out_md = base / 'build' / f'book_{lang}.md'
out_md.write_text(md_text, encoding='utf-8')

# Build TOC from H1/H2 (skip the title block's H1/H2 which are the first two headings)
lines = md_text.split('\n')
toc = []
seen_title = 0
def slug(s, i):
    return 'h-%d' % i
heading_idx = 0
new_lines = []
in_code = False
for ln in lines:
    if ln.startswith('```'):
        in_code = not in_code
    m = re.match(r'^(#{1,2})\s+(.*)$', ln) if not in_code else None
    if m:
        level = len(m.group(1)); text = m.group(2).strip()
        heading_idx += 1
        anchor = slug(text, heading_idx)
        if heading_idx > 2:  # skip book title and subtitle
            toc.append((level, text, anchor))
        new_lines.append(f'{m.group(1)} <a id="{anchor}"></a>{text}')
    else:
        new_lines.append(ln)
md_text2 = '\n'.join(new_lines)
md_text2 = re.sub(r'^(\s*- )([0-9\u09e6-\u09ef]+)\. ', lambda m: m.group(1)+m.group(2)+'\\. ', md_text2, flags=re.M)
body = markdown.markdown(md_text2, extensions=['tables', 'fenced_code'])

toc_title = 'Contents' if lang == 'en' else 'সূচিপত্র'
toc_html = [f'<div class="toc"><h1>{toc_title}</h1><ul>']
for level, text, anchor in toc:
    cls = 'l1' if level == 1 else 'l2'
    toc_html.append(f'<li class="{cls}"><a href="#{anchor}">{html.escape(text)}</a></li>')
toc_html.append('</ul></div>')
# insert TOC after the title block (after first <hr>)
idx = body.find('<hr />')
body = body[:idx] + '\n'.join(toc_html) + '<div class="pb"></div>' + body[idx:] if idx > 0 else '\n'.join(toc_html) + body

font_bn = (base / 'build' / 'fonts' / 'NotoSansBengali-VF.ttf').resolve().as_uri()
font_css = f"@font-face {{ font-family: 'NotoBn'; src: url('{font_bn}') format('truetype'); font-weight: 100 900; }}"
family = "'NotoBn', 'Noto Sans', Arial, sans-serif" if lang == 'bn' else "'Liberation Sans', 'NotoBn', 'DejaVu Sans', Arial, sans-serif"
title = 'Build It in Bangla' if lang == 'en' else 'বাংলায় গড়ে তুলুন'
page = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>
<style>
{font_css}
@page {{ size: A4; margin: 18mm 16mm 20mm 16mm; }}
html, body {{ font-family: {family}; font-size: 10.5pt; line-height: 1.55; color: #1a1a1a; }}
h1 {{ font-size: 20pt; line-height: 1.3; margin: 0 0 8pt; color: #14532d; page-break-before: always; padding-top: 4pt; }}
body > h1:first-of-type {{ page-break-before: auto; font-size: 30pt; margin-top: 120pt; text-align: center; }}
body > h2:first-of-type {{ text-align: center; font-size: 15pt; color: #1a1a1a; border: none; }}
body > p:nth-of-type(-n+2) {{ text-align: center; }}
h2 {{ font-size: 14.5pt; margin: 18pt 0 6pt; color: #14532d; page-break-after: avoid; border-bottom: 1px solid #b8c4bb; padding-bottom: 3pt; }}
h3 {{ font-size: 11.5pt; margin: 12pt 0 4pt; color: #1f2937; page-break-after: avoid; }}
p {{ margin: 4pt 0; }}
ul, ol {{ margin: 3pt 0 6pt 0; padding-left: 20pt; }}
li {{ margin: 1.5pt 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9.2pt; }}
tr {{ page-break-inside: avoid; }}
th, td {{ border: 1px solid #b8c4bb; padding: 3.5pt 5pt; vertical-align: top; text-align: left; }}
th {{ background: #e6f0e8; font-weight: 700; }}
tbody tr:nth-child(even) {{ background: #f7faf7; }}
pre {{ background: #f3f4f6; border: 1px solid #d1d5db; border-radius: 4px; padding: 6pt 8pt; font-size: 8.8pt; line-height: 1.4; white-space: pre-wrap; word-wrap: break-word; font-family: 'DejaVu Sans Mono', Consolas, monospace; page-break-inside: avoid; }}
code {{ font-family: 'DejaVu Sans Mono', Consolas, monospace; font-size: 9pt; }}
hr {{ border: 0; border-top: 1px solid #b8c4bb; margin: 14pt 0; }}
.toc {{ page-break-before: always; }}
.toc h1 {{ page-break-before: auto; }}
.toc ul {{ list-style: none; padding-left: 0; column-count: 1; }}
.toc li.l1 {{ font-weight: 700; margin-top: 6pt; }}
.toc li.l2 {{ padding-left: 14pt; font-size: 9.5pt; }}
.toc a {{ color: #1a1a1a; text-decoration: none; }}
.pb {{ page-break-after: always; }}
em {{ color: #374151; }}
</style></head><body>{body}</body></html>"""
out_html = base / 'build' / f'book_{lang}.html'
out_html.write_text(page, encoding='utf-8')
print('ok', lang, 'words:', len(md_text.split()), 'toc entries:', len(toc))
