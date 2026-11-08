"""Turn translated kit files back into readable Markdown tales.

Usage:
  python3 apply_translation.py <lang-code> <file> [<file> ...]

<file> can be:
  * a tale JSON from translation-kit/source/... in which you (or a translator / AI) filled a "target"
    field next to every "source" (and "title": {"target": ...});
  * an XLIFF 1.2 file from translation-kit/xliff/... with <target> elements filled in by a CAT tool.

Output: Fairy Tales of the World/translations/<lang-code>/<Continent>/<Tradition>/NNN - <translated title>.md
Segments without a target keep the source text and are listed as untranslated in the output header.
"""
import html, json, os, re, sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "translation-kit")
NS = {"x": "urn:oasis:names:tc:xliff:document:1.2"}


def safe(name, n=90):
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', " ", name)
    return re.sub(r"\s+", " ", name).strip(" .")[:n] or "Untitled"


def source_record(tale_id):
    cat = json.load(open(os.path.join(KIT, "catalog.json"), encoding="utf-8"))
    for t in cat["tales"]:
        if t["id"] == tale_id:
            return json.load(open(os.path.join(KIT, t["json"]), encoding="utf-8"))
    raise SystemExit(f"tale id {tale_id} not found in catalog.json")


def render(rec, lang):
    missing = 0
    def tgt(seg):
        nonlocal missing
        t = (seg.get("target") or "").strip()
        if not t:
            missing += 1
            return seg["source"]
        return t
    title = tgt(rec["title"])
    blocks = []
    for p in rec["paragraphs"]:
        if p["type"] == "break":
            blocks.append("* * *")
        elif p["type"] == "heading":
            blocks.append("### " + " ".join(tgt(s) for s in p["segments"]))
        elif p["type"] in ("verse", "verse-quote"):
            lines = [tgt(s) for s in p["segments"]]
            blocks.append("\n".join(("> " if p["type"] == "verse-quote" else "") + l for l in lines))
        else:
            txt = " ".join(tgt(s) for s in p["segments"])
            blocks.append(("> " + txt) if p["type"] == "quote" else txt)
    total = 1 + sum(len(p["segments"]) for p in rec["paragraphs"])
    hdr = (f"# {title}\n\n"
           f"- **Original title:** {rec['title']['source']}\n"
           f"- **Tradition:** {rec['tradition']} ({rec['continent']})\n"
           f"- **Translated into:** {lang}  ·  translated from: {rec['source_lang']}\n"
           f"- **Source text:** *{rec['source_book']}* — {rec['credits']}\n"
           f"- **Source licence:** {rec['copyright']}\n"
           f"- **Translation status:** {total - missing}/{total} segments translated\n\n---\n\n")
    num = rec["id"].rsplit("-", 1)[-1]
    out_dir = os.path.join(ROOT, "translations", lang, rec["continent"], rec["tradition"])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{num} - {safe(title)}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(hdr + "\n\n".join(blocks) + "\n")
    return path, missing


def from_xliff(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    if re.search(r"<!(DOCTYPE|ENTITY)", raw, re.I):  # refuse entity tricks (XXE / billion laughs) in files from outside
        raise SystemExit(f"{path}: XLIFF with DOCTYPE/ENTITY declarations is not accepted")
    tree = ET.ElementTree(ET.fromstring(raw))
    recs = []
    for fe in tree.getroot().findall("x:file", NS):
        rec = source_record(fe.get("original"))
        targets = {}
        for tu in fe.iter("{urn:oasis:names:tc:xliff:document:1.2}trans-unit"):
            t = tu.find("x:target", NS)
            if t is not None and (t.text or "").strip():
                targets[tu.get("id")] = t.text
        rec["title"]["target"] = targets.get("title", "")
        for p in rec["paragraphs"]:
            for s in p["segments"]:
                s["target"] = targets.get(s["id"], "")
        recs.append(rec)
    return recs


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    lang = sys.argv[1]
    for f in sys.argv[2:]:
        recs = from_xliff(f) if f.endswith((".xlf", ".xliff")) else [json.load(open(f, encoding="utf-8"))]
        for rec in recs:
            path, missing = render(rec, lang)
            print(("OK  " if not missing else f"{missing:3d} untranslated  ") + os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
