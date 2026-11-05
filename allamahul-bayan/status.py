# -*- coding: utf-8 -*-
"""Writes SERIES-STATUS.md: one row per book, read from the language files and the last build.
usage: python3 status.py   (run after build.py)"""
import importlib, json, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(ROOT, "engine"), os.path.join(ROOT, "languages")]

rows = []
for f in sorted(os.listdir(os.path.join(ROOT, "languages"))):
    if not f.endswith(".py") or f.startswith("_"):
        continue
    code = f[:-3]
    try:
        L = importlib.import_module(code).LANG
    except Exception as e:  # report, don't crash
        rows.append((999, code, f"(failed to load: {e!r})", "", "", "", ""))
        continue
    n = sum(len(s["items"]) for s in L["sections"])
    pc = os.path.join(ROOT, "build", code, "pagecount.json")
    pages = json.load(open(pc))["pages"] if os.path.exists(pc) else "—"
    ok = os.path.exists(os.path.join(ROOT, L["folder"], "output", "interior.pdf")) and \
        os.path.exists(os.path.join(ROOT, L["folder"], "output", "cover.pdf"))
    status = ("REVIEW DRAFT" if L.get("draft") else "native review pending") if ok else "NOT BUILT"
    rows.append((L["series_no"], code, L["name"], n, pages, status, L["folder"]))

rows.sort()
out = ["# Allamahul Bayan Series — status of every book", "",
       f"{len(rows)} books. *REVIEW DRAFT* books print a “review draft” notice until `draft=False` is set in their language file "
       "and the book is rebuilt. **Every** book needs a native-speaker proofread and the scholar check of pages 4–5 before "
       "publication; each book's `KDP-PUBLISHING-GUIDE.md` lists the specific points to check.", "",
       "| # | code | language | letters | pages | status | folder |", "|---|---|---|---|---|---|---|"]
for no, code, name, n, pages, status, folder in rows:
    out.append(f"| {no} | `{code}` | {name} | {n} | {pages} | {status} | `{folder}/` |")
open(os.path.join(ROOT, "SERIES-STATUS.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{len(rows)} books written to SERIES-STATUS.md")
