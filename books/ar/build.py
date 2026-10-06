# -*- coding: utf-8 -*-
"""Build book.html for আরবি ভাষার দরজা. Then run render.js to get the PDF and overflow report."""
import os, sys
import engine
from engine import page, PAGES
import front, part1

HERE = os.path.dirname(os.path.abspath(__file__))

def recto(fill=None):
    """Make the next page a right-hand page (odd number) by adding a quiet filler page if needed."""
    import part23; part23.close_flow()
    main = sum(1 for p in PAGES if not p["front"])
    if main % 2 == 1:
        page(fill or '<div class="spacer"></div><div class="center small">এই পাতাটি ইচ্ছা করে ফাঁকা রাখা হয়েছে · notes</div><div class="spacer"></div>', folio=False)

front.build()
part1.build()
recto()
SKIP = set(os.environ.get("SKIP", "").split(","))
for mod in ("part2", "part3", "part4", "part5", "back"):
    if mod in SKIP:
        continue
    if os.path.exists(os.path.join(HERE, mod + ".py")):
        __import__(mod).build(); recto()

import measure
miss = measure.missing()
if miss:
    mh = "".join('<div class="m" data-k="%s" style="display:flow-root;">%s</div>' % (k, v) for k, v in miss.items())
    open(os.path.join(HERE, "measure.html"), "w", encoding="utf-8").write(
        engine.render(front.FOREWORD_CSS).split("<body>")[0] + '<body><div class="page" style="height:auto;display:block;">' + mh + "</div></body></html>")
    print("NEEDS_MEASURE", len(miss))
html = engine.render(front.FOREWORD_CSS)
import re
html = re.sub(r"\{\{[a-z0-9_]+\}\}", "—", html)
open(os.path.join(HERE, "book.html"), "w", encoding="utf-8").write(html)
print("pages:", len(PAGES), "(front %d, main %d)" % (sum(p["front"] for p in PAGES), sum(not p["front"] for p in PAGES)))
