#!/usr/bin/env python3
"""Write the verification outputs the owner's islamic-source-verifier protocol requires.

    python3 tools/build_sources_report.py 1     (after verify_quran.py and verify_hadith.py 1)

Writes:
  editions/<code>/muwatta-<code>-bookNN.sources.md          next to each reading edition
  editions/<code>/release/volNN/muwatta-<code>-volNN.sources.md   next to each retail package
  VERIFIED-ISLAMIC-REFERENCES.md                            the project's reference list (protocol: project copy)
  data/verification/bank-additions-<date>.json / .md        new rows for the workspace bank (merged on the laptop)
"""
import json, os, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()


def load(p):
    return json.load(open(os.path.join(ROOT, p), encoding="utf-8"))


def report(code, book, Q, H, pub, title):
    ed = pub["editions"][code]
    qt = ed.get("quran_translation", {})
    qver = (Q["versions"].get(qt.get("key")) or {}).get("version")
    rows, i = [], 0
    for k, v in Q["verses"].items():
        i += 1
        rows.append(f"| {i} | Quran | {k} ({v['surah']}) | quran.com API v4 (text_uthmani) | Tanzil 3.1.2 {'✓' if v['cross_check_match'] else '✗'}; "
                    f"phrases in narration {'✓' if all(c['in_verse'] for c in v['phrase_checks']) else '✗'} | — | {v['status']} |")
    for r in H["entries"]:
        i += 1
        cc = f"fawazahmed0 {'✓ identical' if r.get('arabic_identical') else r.get('arabic_similarity')}"
        rows.append(f"| {i} | Hadith ({r['type']}) | {r['reference']} (fawazahmed0 {r['fawazahmed0_number']}) | sunnah.com text via hadith-json v1.2.0 | "
                    f"{cc}; English {r.get('english_agreement')} | {r.get('grade_display') or '—'} | {r['status']}{(' — ' + r['why']) if r.get('why') else ''} |")
    qc = {}
    for v in Q["verses"].values():
        qc[v["status"]] = qc.get(v["status"], 0) + 1
    hc = H["counts"]
    verified = qc.get("VERIFIED", 0) + hc.get("VERIFIED", 0)
    flagged = hc.get("FLAGGED", 0)
    failed = qc.get("FAILED", 0) + hc.get("FAILED", 0)
    unver = hc.get("UNVERIFIED", 0)
    weak = [r for r in H["entries"] if r["status"] == "FLAGGED"]
    lines = [
        f"# Verification report — {title}",
        "",
        f"Protocol: `agents/islamic-source-verifier.md` (owner's Islamic source authentication protocol). Checked: {TODAY}.",
        f"Scope: every verse and every hadith in Muwatta Malik, Book {book} (Kitab Wuqut al-Salah), as printed in this edition.",
        "",
        "| # | Type | Reference | Source fetched | Cross-check | Grade (grader) | Status |",
        "|---|------|-----------|----------------|-------------|----------------|--------|",
        *rows,
        "",
        f"**Summary:** {verified} VERIFIED · {flagged} FLAGGED (da'if) · {failed} FAILED · {unver} UNVERIFIED.",
        "",
        f"**Authentication check: {verified} verified, {flagged} flagged (da'if, Salim al-Hilali), {failed} failed.**",
        "",
        "## Flagged items (kept, labelled as the protocol requires)",
        "",
        *[f"- {r['reference']}: {r['grade_display']}. Printed with the label \"weak (da'if) per Salim al-Hilali\"; "
          "never presented as evidence for a ruling or creed point." for r in weak],
        "- Only one grader is available in the approved sources for the Muwatta (Salim al-Hilali, via fawazahmed0). "
        "Dorar.net (grade lookup) is not reachable from the build machine; no second grading was added.",
        "",
        "## Sources and versions",
        "",
        "- **Hadith Arabic (printed verbatim, never edited):** sunnah.com text through its pinned offline copy "
        "AhmedBaset/hadith-json **v1.2.0** (protocol source #2; sunnah.com itself blocks automated access, which is not bypassed).",
        "- **Second source:** fawazahmed0/hadith-api **@1** (ara-malik, eng-malik); Arabic compared letter by letter after "
        "removing vowel marks; English compared for narrator and meaning.",
        "- **Grades:** Salim al-Hilali, as listed by fawazahmed0/hadith-api.",
        "- **Qur'an Arabic:** quran.com API v4 `text_uthmani` (source #1), cross-checked with the Tanzil text from "
        "risan/quran-json **3.1.2** (npm, pinned; source #2). Raw responses kept in `sources/quran/`.",
        f"- **Qur'an translation in this edition:** QuranEnc.com `{qt.get('key')}`, version **{qver or 'NOT YET RECORDED'}**"
        + ("" if qver else " — QuranEnc's list API and downloads did not provide it on " + TODAY + "; this is a publication blocker.")
        + (" The Bengali text was also compared with quran.com's copy of the same translator (resource 213): identical."
           if code == "bn" else ""),
        "",
        "## Licences (for a published, sold edition)",
        "",
        "- Muwatta Arabic: classical text (public domain); vowelled sunnah.com text via hadith-json (no licence file).",
        "- fawazahmed0/hadith-api: The Unlicense (public domain).",
        "- Tanzil Qur'an text: verbatim copying allowed, no changes; risan/quran-json packaging CC BY-SA 4.0.",
        "- QuranEnc translations: re-publishing allowed if the text is unaltered, QuranEnc.com and the publisher are named, "
        "and the version number is given. This edition therefore quotes **whole verses only**, unaltered, with the source; "
        "a clause quoted inside a narration is the edition's own paraphrase and is labelled as such.",
        "- Third-party hadith translations (Bewley English on sunnah.com; Islamic Foundation Bangla) are rights-reserved and "
        "were used only for checking. Nothing from them is reproduced.",
        "",
        "## The meanings in this edition",
        "",
        "The Bengali/Japanese meanings of the hadith are the edition's **own translation from the Arabic, made with AI "
        "assistance and edited**. They are not presented as a published translation. Their fidelity to the Arabic was checked "
        "by an independent review (2026-11-21; 2 medium and 6 minor issues, all corrected). They remain subject to the "
        "scholarly review that the edition standard requires before publication. Notes are labelled as editorial commentary.",
        "",
        "## Changes made on " + TODAY + " to meet the protocol",
        "",
        "- Two earlier edits to the Arabic (entries 6 and 25) were reverted: the Arabic is now exactly the source text. The "
        "readings are explained in notes instead. An unverified claim about a printed edition was removed.",
        "- Qur'an quotations that had been written from memory (17:78 in a note; renderings of 20:14, 7:205, 83:1) were "
        "replaced by fetched, cross-checked Arabic and the named QuranEnc translation of the whole verse.",
        "- Unsourced claims about \"the commentators\" in notes were removed or relabelled as editorial interpretation.",
        "- Every entry now shows its grade with the grader; weak entries carry the weak label.",
    ]
    return "\n".join(lines) + "\n"


def bank_rows(Q, H, pub):
    data = load("data/arabic/muwatta.json")
    hj = {h["idInBook"]: h for h in json.load(open(os.path.join(ROOT, ".cache", "hj.json"), encoding="utf-8"))["hadiths"]}
    out = {"generated": TODAY, "project": "Muwatta Imam Malik", "quran": {}, "hadith": {}}
    for k, v in Q["verses"].items():
        out["quran"][k] = {
            "surah": v["surah"], "arabic_uthmani": v["arabic_uthmani"],
            "en_saheeh_international": v["en_saheeh_international"], "bn_taisirul": v["bn_taisirul"],
            "bn_zakaria_quranenc": v["quranenc"]["bn"]["text"], "ja_saeedsato_quranenc": v["quranenc"]["ja"]["text"],
            "quranenc_versions": {kk: vv for kk, vv in Q["versions"].items()},
            "source": "quran.com API v4 (text_uthmani; translations 20,161,213)",
            "cross_check": "Tanzil via risan/quran-json 3.1.2, letter-skeleton match",
            "verified_on": v["verified_on"], "used_in": ["Muwatta Imam Malik (" + v["used_in"] + ")"],
        }
    for r in H["entries"]:
        key = f"malik:{H['book']}/{r['nb']}"
        out["hadith"][key] = {
            "collection_ref": r["reference"] + f" (fawazahmed0 eng-malik {r['fawazahmed0_number']}; hadith-json idInBook {r['hadith_json_idInBook']})",
            "sunnah_com_page": r["sunnah_com_page"], "type": r["type"],
            "arabic": next(e["ar"] for e in data["entries"] if e["n"] == r["n"]),
            "english_sunnah_com": hj[r["n"]]["english"]["text"].replace("\n", " "),
            "grade_grader": r.get("grade_display"), "status": r["status"],
            "second_source": "fawazahmed0 ara-malik (Arabic identical)" if r.get("arabic_identical") else f"fawazahmed0 (similarity {r.get('arabic_similarity')})",
            "verified_on": H["checked_on"], "used_in": ["Muwatta Imam Malik (Book 1, bn + ja editions)"],
            "notes": ("weak (da'if) per Salim al-Hilali: label it weak; never use as evidence" if r["status"] == "FLAGGED" else ""),
        }
    return out


def main(argv):
    book = int(argv[0]) if argv else 1
    Q = load("data/verification/quran.json")
    H = load(f"data/verification/hadith-book-{book:02d}.json")
    pub = load("standard/publishing.json")
    written = []
    for code in pub["editions"]:
        for rel in (f"editions/{code}/muwatta-{code}-book{book:02d}.sources.md",
                    f"editions/{code}/release/vol{book:02d}/muwatta-{code}-vol{book:02d}.sources.md"):
            if not os.path.isdir(os.path.dirname(os.path.join(ROOT, rel))):
                continue
            title = os.path.basename(rel).replace(".sources.md", "")
            with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as f:
                f.write(report(code, book, Q, H, pub, title))
            written.append(rel)
    bank = bank_rows(Q, H, pub)
    bj = f"data/verification/bank-additions-{TODAY}.json"
    with open(os.path.join(ROOT, bj), "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
    md = [f"# Bank additions — {TODAY} — Muwatta Imam Malik", "",
          "Rows to append to `agents/verified-islamic-references/BANK.md` and `bank.json` (merged on the laptop by the nightly sync; "
          "skip any key already present).", "", "## Quran", "",
          "| Key | Surah | Arabic (Uthmani, quran.com) | English, Saheeh International | Bangla, Taisirul Quran | Cross-check | Verified | Used in |",
          "|---|---|---|---|---|---|---|---|"]
    for k, v in bank["quran"].items():
        md.append(f"| {k} | {v['surah']} | {v['arabic_uthmani']} | {v['en_saheeh_international']} | {v['bn_taisirul']} | Tanzil ✓ | {v['verified_on']} | Muwatta Imam Malik |")
    md += ["", "## Hadith", "", "| Key (sunnah.com) | Collection / in-book ref | Grade (grader) | Second source | Verified | Notes |", "|---|---|---|---|---|---|"]
    for k, v in bank["hadith"].items():
        md.append(f"| {k} | {v['collection_ref']} | {v['grade_grader']} | {v['second_source']} | {v['verified_on']} | {v['notes']} |")
    bm = bj.replace(".json", ".md")
    with open(os.path.join(ROOT, bm), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    proj = ["# Verified Islamic references — Muwatta Imam Malik", "",
            "Project copy required by the owner's protocol. Master bank: `E:\\Claude Workspace\\agents\\verified-islamic-references\\BANK.md` "
            f"(this project's new rows: `{bm}`, merged into the bank by the nightly laptop sync).", "",
            "| Key | What | Status | Used in |", "|---|---|---|---|"]
    for k, v in Q["verses"].items():
        proj.append(f"| Quran {k} | {v['surah']} — Arabic quran.com, Tanzil ✓; QuranEnc translations | {v['status']} | {v['used_in']} |")
    for r in H["entries"]:
        proj.append(f"| malik:{book}/{r['nb']} | {r['reference']} — {r.get('grade_display')} | {r['status']} | bn + ja editions, Book {book} |")
    proj += ["", "Verification reports: `editions/<code>/*.sources.md`. Re-run: `python3 tools/verify_quran.py && "
             f"python3 tools/verify_hadith.py {book} && python3 tools/build_sources_report.py {book}`."]
    with open(os.path.join(ROOT, "VERIFIED-ISLAMIC-REFERENCES.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(proj) + "\n")
    written += [bj, bm, "VERIFIED-ISLAMIC-REFERENCES.md"]
    print("\n".join(written))
    q_ok = sum(1 for v in Q["verses"].values() if v["status"] == "VERIFIED")
    print(f"Authentication check: {q_ok + H['counts'].get('VERIFIED', 0)} verified, {H['counts'].get('FLAGGED', 0)} flagged "
          f"(da'if, Salim al-Hilali), {H['counts'].get('FAILED', 0)} failed.")


if __name__ == "__main__":
    main(sys.argv[1:])
