#!/usr/bin/env python3
"""Build the canonical Arabic dataset of al-Muwatta' (Yahya al-Laythi recension).

    python3 tools/build_dataset.py            # downloads sources into .cache/, writes data/arabic/muwatta.json

Sources (pinned):
  * PRIMARY TEXT  - AhmedBaset/hadith-json v1.2.0 (sunnah.com text, fully vowelled, 1,985 entries, 61 books).
  * GRADES + REFS - fawazahmed0/hadith-api@1 ara-malik (Unlicense; 1,858 entries; grades by Salim al-Hilali;
                    "book/hadith" reference used by sunnah.com's older USC-MSA numbering).

The third-party translations (English/Urdu/Bengali...) are fetched only by tools/compare.py for research.
They are copyrighted and are never copied into this edition.
"""
import json, os, re, sys, urllib.request, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache")
OUT = os.path.join(ROOT, "data", "arabic", "muwatta.json")

SOURCES = {
    "hj": "https://raw.githubusercontent.com/AhmedBaset/hadith-json/v1.2.0/db/by_book/the_9_books/malik.json",
    "fz": "https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions/ara-malik.json",
    "fz_en_meta": "https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions/eng-malik.min.json",
}

MARKS = re.compile(r"[ً-ْٰـ]")


def fetch(key):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, key + ".json")
    if not os.path.exists(path):
        print("downloading", SOURCES[key], file=sys.stderr)
        with urllib.request.urlopen(SOURCES[key], timeout=180) as r, open(path, "wb") as f:
            f.write(r.read())
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def skeleton(s):
    """Consonant skeleton used for matching between the two sources (no marks, unified hamza/alif)."""
    s = MARKS.sub("", s)
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    return re.sub(r"[^ء-ي]", "", s)


def clean(text):
    """Tidy the sunnah.com markup while keeping the text itself untouched."""
    t = unicodedata.normalize("NFC", text)
    t = t.replace("‏", "")              # RLM markers around punctuation
    t = re.sub(r"[ \t]*\n[ \t]*", " ", t)
    t = re.sub(r"\s+([.،؛:؟])", r"\1", t)
    t = re.sub(r"\s{2,}", " ", t).strip()
    return t


# ---------------------------------------------------------------------------------------------
# Segmentation: narration (riwaya) vs Imam Malik's own commentary (qawl Malik).
# A Malik segment starts at one of these openers when it begins the entry or follows a sentence end.
OPENERS = [
    r"(?:و)?قال يحيي:? ?(?:و)?(?:قال|سيل|سيل) مالك",   # qala Yahya [wa] qala/su'ila Malik
    r"(?:و)?قال يحيي:? ?(?:و)?سمعت مالكا",            # qala Yahya sami'tu Malikan
    r"(?:و)?قال مالك",                                 # [wa] qala Malik
    r"(?:و)?سيل مالك",                                 # [wa] su'ila Malik (hamza seat normalised)
]


def plain_with_index(text):
    """Return (plain, idx): plain is the text without marks, hamza seats unified; idx maps plain->text."""
    plain, idx = [], []
    for i, ch in enumerate(text):
        if MARKS.match(ch):
            continue
        c = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ئ": "ي", "ؤ": "و"}.get(ch, ch)
        plain.append(c)
        idx.append(i)
    return "".join(plain), idx


OPEN_RE = re.compile(r"(?:^|(?<=[.»\"]) |(?<=[.»\"])|(?<=\. ))(?:" + "|".join(OPENERS) + r")\b")


def segment(text):
    plain, idx = plain_with_index(text)
    # the match may begin on the space before the opener; cut at the opener itself
    cuts = sorted({m.start() + (1 if plain[m.start()] == " " else 0) for m in OPEN_RE.finditer(plain)})
    if not cuts or cuts[0] != 0:
        cuts = [0] + cuts
    segs = []
    for k, c in enumerate(cuts):
        start = idx[c] if c < len(idx) else len(text)
        end = idx[cuts[k + 1]] if k + 1 < len(cuts) else len(text)
        chunk = text[start:end].strip()
        if not chunk:
            continue
        is_malik = bool(re.match("(?:" + "|".join(OPENERS) + ")", plain[c:]))
        segs.append({"kind": "malik" if is_malik else "riwaya", "ar": chunk})
    # merge consecutive segments of the same kind
    out = []
    for s in segs:
        if out and out[-1]["kind"] == s["kind"]:
            out[-1]["ar"] += " " + s["ar"]
        else:
            out.append(s)
    return out


def classify(grade):
    """Entry type from al-Hilali's grade label (marfu'/mawquf/maqtu')."""
    if not grade:
        return None
    g = grade.lower()
    if g.startswith("mauquf"):
        return "mawquf"      # report from a Companion
    if g.startswith("maqtu"):
        return "maqtu"       # report from a Successor
    return "marfu"           # attributed to the Prophet (incl. mursal)


def main():
    hj, fz = fetch("hj"), fetch("fz")
    books = {c["id"]: {"n": c["id"], "ar": clean(c["arabic"]), "en": c["english"]} for c in hj["chapters"]}

    # index fawaz entries by skeleton prefix for grade/ref matching
    fz_by_key = {}
    for h in fz["hadiths"]:
        sk = skeleton(h["text"])
        if sk:
            fz_by_key.setdefault(sk[:80], h)

    # The Arabic is printed exactly as the source has it (owner's protocol: "never retype or 'fix' it").
    # Doubtful readings are explained in editorial notes in the translation files, never changed here.

    entries, per_book = [], {}
    matched = 0
    for h in hj["hadiths"]:
        text = clean(h["arabic"])
        if not text:
            continue
        b = h["chapterId"]
        per_book[b] = per_book.get(b, 0) + 1
        sk = skeleton(text)
        f = fz_by_key.get(sk[:80])
        if f is None:   # fall back: any fawaz entry whose skeleton starts our text
            for k, v in fz_by_key.items():
                if sk.startswith(k[:50]) or k.startswith(sk[:50]):
                    f = v
                    break
        grade = None
        graders = []
        ref = None
        if f is not None:
            matched += 1
            grade = (f.get("grades") or [{}])[0].get("grade")
            graders = [{"name": g.get("name"), "grade": g.get("grade")} for g in (f.get("grades") or [])]
            ref = {"fz_n": f["hadithnumber"], "book": f["reference"]["book"], "hadith": f["reference"]["hadith"]}
        segs = segment(text)
        kind = classify(grade)
        if all(s["kind"] == "malik" for s in segs):
            kind = "malik"
        entries.append({
            "n": h["idInBook"],                 # sunnah.com running number (1..1985)
            "book": b,
            "nb": per_book[b],                  # number inside the book
            "type": kind,                       # marfu | mawquf | maqtu | malik | None
            "grade": grade,                     # Salim al-Hilali (via hadith-api), None if unmatched
            "graders": graders,                 # every grade with its grader (protocol: grade AND grader)
            "ref_uscmsa": ref,
            "ar": text,
            "segments": segs,
        })

    for b in books.values():
        b["count"] = per_book.get(b["n"], 0)
    data = {
        "title_ar": "الموطأ — رواية يحيى بن يحيى الليثي",
        "title_en": "al-Muwatta' of Imam Malik ibn Anas (d. 179 AH), recension of Yahya ibn Yahya al-Laythi",
        "source": {
            "text": SOURCES["hj"] + " (sunnah.com text)",
            "grades_refs": SOURCES["fz"] + " (Unlicense; grades: Salim al-Hilali)",
        },
        "stats": {
            "entries": len(entries), "books": len(books), "graded": matched,
            "with_malik_commentary": sum(1 for e in entries if any(s["kind"] == "malik" for s in e["segments"])),
        },
        "books": [books[k] for k in sorted(books)],
        "entries": entries,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(json.dumps(data["stats"]), "->", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
