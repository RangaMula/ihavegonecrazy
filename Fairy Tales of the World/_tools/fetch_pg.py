"""Fetch books straight from gutenberg.org (HTML, else text) and write GITenberg-style metadata
so split.py / build.py can use them.   python3 fetch_pg.py ID [ID ...]"""
import csv, json, os, re, sys, urllib.request, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
META, BOOKS = os.path.join(HERE, "meta"), os.path.join(HERE, "books")
ROLE = {"translator": "translator", "editor": "editor", "compiler": "compiler", "illustrator": "illustrator",
        "author of introduction, etc.": "author_of_introduction", "commentator": "commentator",
        "contributor": "contributor", "annotator": "editor", "adapter": "editor", "photographer": "photographer"}
_CAT = None


def catalog():
    global _CAT
    if _CAT is None:
        _CAT = {r["Text#"]: r for r in csv.DictReader(open(os.path.join(HERE, "pg_catalog.csv"), encoding="utf-8"))}
    return _CAT


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")[:60]


def parse_authors(a):
    creator, contrib = {}, {}
    for part in [p.strip() for p in a.split(";") if p.strip()]:
        role = "author"
        m = re.search(r"\[([^\]]+)\]\s*$", part)
        if m:
            role = ROLE.get(m.group(1).strip().lower(), m.group(1).strip().lower().replace(" ", "_"))
            part = part[: m.start()].strip()
        dm = re.search(r",\s*(?:active )?(\d{1,4})\??(?: BCE)?-(\d{1,4})?\??(?: BCE)?\s*$", part)
        death = None
        if dm:
            death = int(dm.group(2)) if dm.group(2) else None
            part = part[: dm.start()].strip()
        name = part
        target = creator if role == "author" else contrib
        target.setdefault(role, []).append({"agent_name": name, "deathdate": death})
    return creator, contrib


def fetch(gid):
    gid = str(gid)
    r = catalog()[gid]
    repo = f"PG-{slug(r['Title'])}_{gid}"
    mpath = os.path.join(META, repo + ".json")
    creator, contrib = parse_authors(r["Authors"])
    meta = {"title": r["Title"].replace("\n", " "), "language": r["Language"], "creator": creator,
            "contributor": contrib, "subjects": r["Subjects"].split("; "), "tableOfContents": ""}
    json.dump(meta, open(mpath, "w"), ensure_ascii=False)
    # remove any GITenberg meta with the same id so the IDMAP resolves to this one
    for f in os.listdir(META):
        if f.endswith(f"_{gid}.json") and f != repo + ".json":
            os.remove(os.path.join(META, f))
    if not (os.path.exists(os.path.join(BOOKS, repo + ".htm")) or os.path.exists(os.path.join(BOOKS, repo + ".txt"))):
        for url, ext in ((f"https://www.gutenberg.org/cache/epub/{gid}/pg{gid}-images.html", ".htm"),
                         (f"https://www.gutenberg.org/cache/epub/{gid}/pg{gid}.txt", ".txt")):
            try:
                with urllib.request.urlopen(url, timeout=90) as resp:
                    data = resp.read().decode("utf-8", "replace")
                open(os.path.join(BOOKS, repo + ext), "w", encoding="utf-8").write(data)
                break
            except Exception as e:  # noqa
                print("fail", url, e)
    return repo


if __name__ == "__main__":
    with cf.ThreadPoolExecutor(6) as ex:
        for repo in ex.map(fetch, sys.argv[1:]):
            print(repo)
