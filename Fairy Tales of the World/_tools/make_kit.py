"""Build the translation kit from the tale Markdown files.

python3 make_kit.py            (run from anywhere; paths are relative to this file)

Creates, under  Fairy Tales of the World/translation-kit/ :
  catalog.json                       every tale: id, title, tradition, language, words, segments, paths
  source/<Continent>/<tradition-id>/<tale-id>.json   one tale, split into paragraphs -> sentence segments
  xliff/<Continent>/<tradition-id>.xlf               XLIFF 1.2 (one <file> per tale) for CAT tools
  glossary/<tradition-id>.csv        auto-extracted proper names to keep consistent across a translation
"""
import csv, html, json, os, re, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../Fairy Tales of the World
KIT = os.path.join(ROOT, "translation-kit")
CONTINENTS = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
CONT_CODE = {"Africa": "af", "Americas": "am", "Asia": "as", "Europe": "eu", "Oceania": "oc"}

ABBREV = {"mr", "mrs", "ms", "dr", "st", "mt", "jr", "sr", "prof", "rev", "capt", "col", "gen", "lt", "sgt",
          "no", "vol", "cf", "viz", "i.e", "e.g", "etc", "vs", "p", "pp", "ch", "ff"}
SENT_SPLIT = re.compile(r"(?<=[.!?…])([”\"’')\]]*)\s+(?=[“\"‘'(\[¿¡]?[A-ZÀ-ÖØ-ÞĀ-ſ0-9])")


def _is_abbrev(text_before):
    m = re.search(r"([\w.]+)\.$", text_before)
    if not m:
        return False
    w = m.group(1).lower()
    return w in ABBREV or (len(w) == 1 and w.isalpha())  # initials such as "J."


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)


def sentences(text):
    parts, last = [], 0
    for m in SENT_SPLIT.finditer(text):
        if not m.group(1) and _is_abbrev(text[last:m.start()]):
            continue
        end = m.start() + len(m.group(1))
        parts.append(text[last:end].strip())
        last = m.end()
    parts.append(text[last:].strip())
    return [p for p in parts if p]


def parse_md(path):
    raw = open(path, encoding="utf-8").read()
    head, body = raw.split("\n---\n", 1)
    title = head.splitlines()[0].lstrip("# ").strip()
    meta = dict(re.findall(r"^- \*\*(.+?):\*\* (.*)$", head, re.M))
    paras = []
    for block in re.split(r"\n{2,}", body.strip()):
        b = block.strip()
        if not b:
            continue
        if b in ("* * *", "*****", "* * * * *"):
            paras.append({"type": "break", "segments": []})
            continue
        if b.startswith("### "):
            paras.append({"type": "heading", "segments": [b[4:].strip()]})
            continue
        quote = all(l.startswith(">") for l in b.splitlines())
        if quote:
            b = "\n".join(l.lstrip("> ").rstrip() for l in b.splitlines())
        if "\n" in b:  # verse / song: one segment per line
            paras.append({"type": "verse-quote" if quote else "verse", "segments": [l.strip() for l in b.splitlines() if l.strip()]})
        else:
            b = re.sub(r"\s+", " ", b)
            paras.append({"type": "quote" if quote else "prose", "segments": sentences(b)})
    return title, meta, paras


def lang_of(meta):
    l = meta.get("Original language of this text", "en")
    m = re.findall(r"[a-z]{2,3}", l)
    return m[-1] if len(m) > 1 and m[0] != "en" else (m[0] if m else "en")  # bilingual books: text is the non-English side? keep first
    # (books tagged ['en','fr'] etc. are English translations printed with originals; first code is used)


def main():
    catalog, glossary_src = [], defaultdict(Counter)
    glossary_tales = defaultdict(lambda: defaultdict(set))
    for cont in CONTINENTS:
        cdir = os.path.join(ROOT, cont)
        if not os.path.isdir(cdir):
            continue
        for trad in sorted(os.listdir(cdir)):
            tdir = os.path.join(cdir, trad)
            if not os.path.isdir(tdir):
                continue
            tslug = slug(trad)
            files = sorted(f for f in os.listdir(tdir) if re.match(r"^\d{3} - .*\.md$", f))
            xl_files = []
            for f in files:
                num = f[:3]
                tid = f"{CONT_CODE[cont]}-{tslug}-{num}"
                title, meta, paras = parse_md(os.path.join(tdir, f))
                lang = re.findall(r"[a-z]{2,3}", meta.get("Original language of this text", "en"))
                lang = lang[0] if lang else "en"
                seg_count, words, n = 0, 0, 0
                for pi, p in enumerate(paras, 1):
                    p["id"] = f"p{pi:03d}"
                    p["segments"] = [{"id": f"p{pi:03d}.s{si:02d}", "source": s} for si, s in enumerate(p["segments"], 1)]
                    for s in p["segments"]:
                        seg_count += 1
                        words += len(s["source"].split())
                        # proper-name candidates: capitalised words not at sentence start
                        toks = re.findall(r"[\w’'-]+", s["source"])
                        for t in toks[1:]:
                            if t[:1].isupper() and len(t) > 2 and not t.isupper():
                                glossary_src[tslug][t] += 1
                                glossary_tales[tslug][t].add(num)
                rec = {
                    "id": tid,
                    "title": {"id": "title", "source": title},
                    "tradition": trad, "continent": cont, "source_lang": lang,
                    "source_book": meta.get("Source book", "").strip("*"),
                    "credits": meta.get("Author / collector / translator", ""),
                    "gutenberg": meta.get("Source", ""),
                    "copyright": meta.get("Copyright status", ""),
                    "markdown_file": f"{cont}/{trad}/{f}",
                    "stats": {"paragraphs": len(paras), "segments": seg_count, "words": words},
                    "paragraphs": paras,
                }
                rel = os.path.join("source", cont, tslug, tid + ".json")
                os.makedirs(os.path.join(KIT, os.path.dirname(rel)), exist_ok=True)
                with open(os.path.join(KIT, rel), "w", encoding="utf-8") as fh:
                    json.dump(rec, fh, ensure_ascii=False, indent=1)
                catalog.append({"id": tid, "title": title, "continent": cont, "tradition": trad, "tradition_id": tslug,
                                "source_lang": lang, "words": words, "segments": seg_count,
                                "pd_status": "worldwide" if "worldwide" in rec["copyright"] else "us",
                                "json": rel.replace(os.sep, "/"), "markdown": rec["markdown_file"]})
                xl_files.append(rec)
            # XLIFF 1.2 per tradition
            if xl_files:
                xdir = os.path.join(KIT, "xliff", cont)
                os.makedirs(xdir, exist_ok=True)
                with open(os.path.join(xdir, tslug + ".xlf"), "w", encoding="utf-8") as x:
                    x.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                            '<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">\n')
                    for rec in xl_files:
                        e = html.escape
                        x.write(f' <file original="{rec["id"]}" source-language="{rec["source_lang"]}" datatype="plaintext">\n'
                                f'  <header><note>{e(rec["title"]["source"])} — {e(rec["tradition"])} — {e(rec["source_book"])} — {e(rec["copyright"][:60])}</note></header>\n  <body>\n'
                                f'   <trans-unit id="title"><source>{e(rec["title"]["source"])}</source></trans-unit>\n')
                        for p in rec["paragraphs"]:
                            if not p["segments"]:
                                continue
                            x.write(f'   <group id="{p["id"]}" restype="{p["type"]}">\n')
                            for s in p["segments"]:
                                x.write(f'    <trans-unit id="{s["id"]}"><source>{e(s["source"])}</source></trans-unit>\n')
                            x.write("   </group>\n")
                        x.write("  </body>\n </file>\n")
                    x.write("</xliff>\n")
    # glossary: names seen >= 3 times in a tradition, excluding very common capitalised words
    common = set("""The And But For Then When There This That They She His Her Him Its What Who How Why Where Now
        Once One Two Three God Lord King Queen Prince Princess Sir Lady Mother Father Brother Sister Old Little Great
        Good Well Yes Oh Ah Come Let Go So If As At In On Of To By With From Not No All Some Every Each Our Your
        Mrs Mr Then Upon After Before While Into Out Over Under About Here Thou Thee Thy Ye You We Monday Sunday""".split())
    gdir = os.path.join(KIT, "glossary")
    os.makedirs(gdir, exist_ok=True)
    for tslug, cnt in glossary_src.items():
        rows = [(w, c, " ".join(sorted(glossary_tales[tslug][w])[:15])) for w, c in cnt.most_common() if c >= 3 and w not in common]
        with open(os.path.join(gdir, tslug + ".csv"), "w", newline="", encoding="utf-8") as fh:
            wr = csv.writer(fh)
            wr.writerow(["name_or_term", "occurrences", "tale_numbers", "keep_or_transliterate", "target_form", "note"])
            for r in rows:
                wr.writerow([*r, "", "", ""])
    with open(os.path.join(KIT, "catalog.json"), "w", encoding="utf-8") as fh:
        json.dump({"tales": catalog,
                   "totals": {"tales": len(catalog), "words": sum(c["words"] for c in catalog),
                              "segments": sum(c["segments"] for c in catalog)}}, fh, ensure_ascii=False, indent=1)
    print(len(catalog), "tales;", sum(c["words"] for c in catalog), "words;", sum(c["segments"] for c in catalog), "segments")


if __name__ == "__main__":
    main()
