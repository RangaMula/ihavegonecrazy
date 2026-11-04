# -*- coding: utf-8 -*-
"""Build one or more Allamahul Bayan books.   usage:  python3 build.py bn hi ur   (or: all)

For each language file languages/<code>.py this writes
  book-NN-<name>/output/interior.pdf, cover.pdf  and  book-NN-<name>/KDP-PUBLISHING-GUIDE.md
"""
import importlib, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(ROOT, "engine"), os.path.join(ROOT, "languages")]
import book, cover, guide

def run(*cmd):
    subprocess.run(cmd, check=True, cwd=ROOT)

def build(code):
    L = importlib.import_module(code).LANG
    bdir = os.path.join(ROOT, "build", code); os.makedirs(bdir, exist_ok=True)
    out = os.path.join(ROOT, L["folder"], "output"); os.makedirs(out, exist_ok=True)
    M = L["map"]
    cfg = dict(frame=M["frame"], land=M.get("land", True), countries=M.get("countries", []),
               points=M["points"], world_marker=M["world_marker"])
    json.dump(cfg, open(os.path.join(bdir, "map_config.json"), "w"))
    run("node", "engine/make_map.mjs", f"build/{code}/map_config.json", f"build/{code}/map_paths.json")
    pages = book.Book(L).build()
    dims = cover.build(L, pages)
    run("node", "engine/render.mjs", f"build/{code}/interior.html", f"{L['folder']}/output/interior.pdf",
        f"build/{code}/cover.html", f"{L['folder']}/output/cover.pdf")
    cover.crop(os.path.join(out, "cover.pdf"), dims["W"], dims["H"])
    guide.write(L, os.path.join(ROOT, L["folder"], "KDP-PUBLISHING-GUIDE.md"), pages, dims["spine"], dims["W"])
    from pypdf import PdfReader
    r = PdfReader(os.path.join(out, "interior.pdf")); c = PdfReader(os.path.join(out, "cover.pdf"))
    b, cb = r.pages[0].mediabox, c.pages[0].mediabox
    assert len(r.pages) == pages and round(float(b.width) / 72, 3) == 8.5 and round(float(b.height) / 72, 3) == 11
    assert abs(float(cb.width) / 72 - dims["W"]) < 0.001
    print(f"✓ {L['name']}: {pages} pages, cover {dims['W']:.4f} x 11.25 in (spine {dims['spine']} in)")

if __name__ == "__main__":
    codes = sys.argv[1:]
    if codes == ["all"]:
        codes = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "languages")) if f.endswith(".py") and not f.startswith("_"))
    for c in codes:
        build(c)
