"""Build 'Fairy Tales of the World' from public-domain GITenberg books.

python3 build.py <output_root>
"""
import concurrent.futures as cf, csv, json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog import CATALOG
from resolve import load, people
from split import split_book, norm

MAX_PER_FOLDER = 100
PD_CUTOFF = 1955  # life + 70: authors/translators who died in or before 1955 are PD worldwide as of 2026

# Death years supplied from standard reference works where Gutenberg's record is blank.
KNOWN_DEATHS = {
    "Ozaki, Yei Theodora": 1932, "McLaughlin, Marie L.": 1931, "Judson, Katharine Berry": 1929,
    "Speck, F. G.": 1950, "Metelerkamp, Sanni": 1945, "Vaughan, Arthur Owen": 1919,
    "Bayliss, Clara Kern": 1948, "Friedlander, Gerald": 1923, "Owen, Elias": 1899,
    "Johnson, A. E. (Alfred Edwin)": 1941, "Stokes, Maive": 1961,
}
# Books removed because a text contributor died after 1955 (not yet PD in life+70 countries).
EXCLUDE = {3455: "Josef Cohen d. 1965", 24714: "Elsie Spicer Eells d. 1963", 21678: "Elsie Spicer Eells d. 1963",
           22096: "Mabel Powers d. 1966", 62855: "T. W. Ressler, mid-20th-century work"}
TEXT_ROLES_IGNORED = {"illustrator", "illustrators", "photographer", "author_of_introduction", "commentator", "commentators", "contributor"}

NOT_TALES = re.compile(r"^(how to get into this book|notes? and references|afterword|epilogue|prologue|"
                       r"conclusion|addenda|postscript|a word to|to the children|to my|note on|key to|"
                       r"list of|explanatory|abbreviations|authorities|sources|the author|the storyteller'?s?)\b", re.I)


def pd_status(meta):
    persons = [(r, n, KNOWN_DEATHS.get(n, d)) for r, n, b, d in people(meta) if r not in TEXT_ROLES_IGNORED]
    persons = [p for p in persons if p[1] not in ("Anonymous", "Unknown", "Various")]
    deaths = [p[2] for p in persons]
    if any(d and int(d) > PD_CUTOFF for d in deaths):
        return "excluded", persons
    if persons and all(d for d in deaths):
        return "worldwide", persons
    return "us", persons


def credit(persons):
    out = []
    for r, n, d in persons:
        out.append(f"{n} ({r.rstrip('s')}{', d. ' + str(d) if d else ''})")
    return "; ".join(out) or "Anonymous / traditional"


def safe(name, n=90):
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', " ", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name[:n].rstrip(" .") or "Untitled"


def titlecase(t):
    if t.isupper() or t.islower():
        small = {"a", "an", "the", "and", "of", "in", "on", "to", "for", "with", "at", "by", "or"}
        words = t.lower().split()
        t = " ".join(w if (i and w in small) else w[:1].upper() + w[1:] for i, w in enumerate(words))
    return t


def tale_key(t):
    k = norm(t)
    k = re.sub(r"^(the |a |an )?(story|tale|history|legend) of (the )?", "", k)
    k = re.sub(r"^(the|a|an) ", "", k)
    return k.replace(" ", "")


def prepare(gid):
    if gid in EXCLUDE:
        return gid, None, None, [], EXCLUDE[gid]
    repo, meta = load(gid)
    status, persons = pd_status(meta)
    if status == "excluded":
        return gid, repo, meta, [], "contributor died after 1955: " + credit(persons)
    try:
        tales = split_book(repo, meta)
    except Exception as e:  # noqa
        return gid, repo, meta, [], f"split error {e}"
    return gid, repo, meta, tales, status


def main(root):
    gids = sorted({g for ids in CATALOG.values() for g in ids})
    with cf.ThreadPoolExecutor(12) as ex:
        books = {r[0]: r for r in ex.map(prepare, gids)}
    index_rows, report = [], []
    for (cont, folder), ids in CATALOG.items():
        out_dir = os.path.join(root, cont, safe(folder))
        os.makedirs(out_dir, exist_ok=True)
        seen, picked, used = set(), [], []
        for gid in ids:
            _, repo, meta, tales, status = books[gid]
            if status not in ("worldwide", "us"):
                report.append(f"{folder}: skipped #{gid} ({status})")
                continue
            n0 = len(picked)
            for t in tales:
                if len(picked) >= MAX_PER_FOLDER:
                    break
                title = titlecase(t["title"])
                if NOT_TALES.match(title) or (len(norm(title)) < 25 and norm(title) in norm(folder)):
                    continue
                k = tale_key(title)
                if not k or k in seen:
                    continue
                seen.add(k)
                picked.append((title, t["text"], gid, meta, status))
            if len(picked) > n0:
                used.append((gid, meta, status, len(picked) - n0))
            if len(picked) >= MAX_PER_FOLDER:
                break
        # write tales
        for i, (title, text, gid, meta, status) in enumerate(picked, 1):
            _, persons = pd_status(meta)
            fn = f"{i:03d} - {safe(title)}.md"
            lic = ("Public domain worldwide: the text was published long ago and every named author/translator "
                   f"died in or before {PD_CUTOFF}." if status == "worldwide" else
                   "Public domain in the USA (Project Gutenberg). The underlying folk tale is traditional and free for anyone; "
                   "this particular English wording's status outside the USA depends on the translator's death date, which is not recorded.")
            hdr = (f"# {title}\n\n"
                   f"- **Tradition:** {folder} ({cont})\n"
                   f"- **Source book:** *{meta.get('title','').strip()}*\n"
                   f"- **Author / collector / translator:** {credit(persons)}\n"
                   f"- **Original language of this text:** {meta.get('language')}\n"
                   f"- **Source:** Project Gutenberg eBook #{gid} — https://www.gutenberg.org/ebooks/{gid} (copied via the GITenberg mirror)\n"
                   f"- **Copyright status:** {lic}\n\n---\n\n")
            with open(os.path.join(out_dir, fn), "w", encoding="utf-8") as f:
                f.write(hdr + text.strip() + "\n")
            index_rows.append([cont, folder, i, title, fn, gid, meta.get("title", "").strip(), credit(persons), status])
        # folder README
        with open(os.path.join(out_dir, "_README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {folder}\n\nContinent: {cont}  \nTales in this folder: **{len(picked)}**"
                    f"{'' if len(picked) >= MAX_PER_FOLDER else (f' (fewer than {MAX_PER_FOLDER}: every distinct tale found in the public-domain sources below is included)' if picked else ' — no worldwide-public-domain source text could be extracted for this tradition yet; see the top-level README, section Gaps')}\n\n"
                    "## Sources\n\n")
            for gid, meta, status, n in used:
                _, persons = pd_status(meta)
                f.write(f"- *{meta.get('title','').strip()}* — {credit(persons)} — Gutenberg #{gid} — {n} tales — "
                        f"{'PD worldwide' if status == 'worldwide' else 'PD in USA; translator death date unrecorded'}\n")
            f.write("\n## Tales\n\n")
            for i, (title, *_r) in enumerate(picked, 1):
                f.write(f"{i}. {title}\n")
        report.append(f"{cont}/{folder}: {len(picked)}")
    with open(os.path.join(root, "index.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["continent", "tradition", "no", "title", "file", "gutenberg_id", "source_book", "credits", "pd_status"])
        w.writerows(index_rows)
    json.dump(report, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.json"), "w"), indent=1)
    print("\n".join(report))
    print("TOTAL", len(index_rows))


if __name__ == "__main__":
    main(sys.argv[1])
