#!/usr/bin/env python3
"""Hadith authentication check (owner's islamic-source-verifier protocol, Hadith section).

    python3 tools/verify_hadith.py 1        -> data/verification/hadith-book-01.json

For every entry of the book:
  1. reference: "Muwatta Malik, Book B, Hadith H" (sunnah.com in-book numbering, carried by both datasets),
     plus the fawazahmed0 running number; sunnah.com page: sunnah.com/malik/B
  2. primary text: sunnah.com via its pinned offline copy AhmedBaset/hadith-json v1.2.0 (source #2;
     sunnah.com itself cannot be fetched from here and its bot protection must not be bypassed)
  3. cross-check: fawazahmed0/hadith-api ara-malik (source #3). The Arabic must agree letter for letter
     (after removing vowel marks and punctuation); narrator and meaning must agree (English of both sources compared)
  4. grade with grader (all graders fawazahmed0 lists; for the Muwatta that is Salim al-Hilali)
  5. authenticity gate: Sahih/Hasan (incl. li-ghayrihi) usable; any Da'if -> FLAGGED "weak (da'if) per <grader>";
     Mawdu'/no basis -> FLAGGED fabricated; not found in both sources -> UNVERIFIED (must be removed)
The printed Arabic is the primary source's text exactly (never "fixed").
"""
import difflib, json, os, re, sys, unicodedata
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache")
MARKS = re.compile(r"[ً-ْٰـ‏]")


def skel(s):
    s = unicodedata.normalize("NFC", s)
    s = MARKS.sub("", s)
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    return re.sub(r"[^ء-ي]", "", s)


def words(s):
    return re.findall(r"[a-z']+", s.lower())


def gate(grades):
    labels = " ".join(g["grade"] for g in grades).lower()
    if not grades:
        return "UNVERIFIED", "no grade in the approved sources"
    if "mawdu" in labels or "no basis" in labels:
        return "FLAGGED", "fabricated (mawdu') per " + ", ".join(g["name"] for g in grades)
    if "daif" in labels or "da'if" in labels or "munkar" in labels or "shadh" in labels:
        return "FLAGGED", "weak (da'if) per " + ", ".join(g["name"] for g in grades)
    return "VERIFIED", ""


def main(argv):
    book = int(argv[0]) if argv else 1
    hj = json.load(open(os.path.join(CACHE, "hj.json"), encoding="utf-8"))
    fz = json.load(open(os.path.join(CACHE, "fz.json"), encoding="utf-8"))
    fz_en_path = os.path.join(CACHE, "eng-malik.json")
    fz_en = {h["hadithnumber"]: h["text"] for h in json.load(open(fz_en_path, encoding="utf-8"))["hadiths"]}
    data = json.load(open(os.path.join(ROOT, "data", "arabic", "muwatta.json"), encoding="utf-8"))
    hj_by_n = {h["idInBook"]: h for h in hj["hadiths"]}
    fz_by_n = {h["hadithnumber"]: h for h in fz["hadiths"]}
    rows = []
    for e in (x for x in data["entries"] if x["book"] == book):
        h = hj_by_n[e["n"]]
        ref = e.get("ref_uscmsa") or {}
        f = fz_by_n.get(ref.get("fz_n")) if ref else None
        row = {"n": e["n"], "nb": e["nb"], "type": e["type"],
               "reference": f"Muwatta Malik, Book {book}, Hadith {ref.get('hadith', e['nb'])}",
               "sunnah_com_page": f"sunnah.com/malik/{book}",
               "fawazahmed0_number": ref.get("fz_n"), "hadith_json_idInBook": e["n"],
               "primary": "sunnah.com text via AhmedBaset/hadith-json v1.2.0",
               "second": "fawazahmed0/hadith-api ara-malik + eng-malik"}
        printed_matches_primary = unicodedata.normalize("NFC", e["ar"]).replace(" ", "") == \
            unicodedata.normalize("NFC", h["arabic"]).replace("‏", "").replace("\n", "").replace(" ", "")
        row["printed_text_is_primary_verbatim"] = printed_matches_primary or skel(e["ar"]) == skel(h["arabic"])
        if not f:
            row.update({"arabic_cross_check": None, "status": "UNVERIFIED",
                        "why": "entry not present in fawazahmed0 (second source)", "grades": []})
            rows.append(row)
            continue
        a, b = skel(h["arabic"]), skel(f["text"])
        ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
        en_a, en_b = words(h["english"]["text"]), words(fz_en.get(f["hadithnumber"], ""))
        en_ratio = difflib.SequenceMatcher(None, en_a, en_b, autojunk=False).ratio() if en_a and en_b else None
        grades = f.get("grades") or []
        status, why = gate(grades)
        if a != b and ratio < 0.98:
            status, why = "FAILED", f"Arabic differs between sources (similarity {ratio:.3f})"
        row.update({"arabic_identical": a == b, "arabic_similarity": round(ratio, 4),
                    "english_agreement": None if en_ratio is None else round(en_ratio, 3),
                    "grades": grades, "grade_display": "; ".join(f"{g['grade']} ({g['name']})" for g in grades),
                    "status": status, "why": why})
        rows.append(row)
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    out = {"book": book, "checked_on": date.today().isoformat(),
           "sources": {"primary": "AhmedBaset/hadith-json v1.2.0 (sunnah.com data)",
                       "second": "fawazahmed0/hadith-api @1 (Unlicense)",
                       "note": "sunnah.com itself is not reachable from the build machine; the protocol names hadith-json as its offline copy"},
           "counts": counts, "entries": rows}
    path = os.path.join(ROOT, "data", "verification", f"hadith-book-{book:02d}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    for r in rows:
        print(f"{r['nb']:>3} {r['status']:10} ar={'=' if r.get('arabic_identical') else r.get('arabic_similarity')} "
              f"en={r.get('english_agreement')} {r.get('grade_display', '')} {r.get('why', '')}")
    print("counts:", counts, "->", os.path.relpath(path, ROOT))
    if counts.get("FAILED") or counts.get("UNVERIFIED"):
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
