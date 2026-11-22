# Session log — 22 Nov 2026 — Muwatta brought under the Qur'an & Hadith authentication protocol

- **Surface:** cloud (remote session `cse_01Y81j2DjP6dim7wYJkFPNSF`).
- **Request (the owner's wording):** "Update the muatta by the protocol set for Quran & Hadith". That protocol is
  `agents/islamic-source-verifier.md` plus the Verified Reference Bank.

## What was done

1. **Bank lookup first.**
   - `BANK.md` read; none of 20:14, 7:205, 17:78, 83:1 were there.
   - Its only Muwatta row is Book 21:10.
2. **Network.** The owner approved adding `api.quran.com` and `quranenc.com` to the environment's allowlist.
   sunnah.com, HadeethEnc and Dorar remain blocked. sunnah.com must not be bypassed anyway; hadith-json is its sanctioned
   offline copy.
3. **Qur'an (`tools/verify_quran.py`).** All 4 verses VERIFIED:
   - quran.com text_uthmani, letter-skeleton match with Tanzil (risan/quran-json 3.1.2 from npm, pinned);
   - every phrase quoted in the narrations is inside its verse.
   - Named translations are QuranEnc `bengali_zakaria` (identical to quran.com resource 213) and `japanese_saeedsato`
     v1.0.13.
   - Raw responses are kept in `sources/quran/`.
4. **Hadith (`tools/verify_hadith.py 1`).**
   - All 31 entries: the Arabic is identical in hadith-json v1.2.0 and fawazahmed0; the English agrees.
   - 25 VERIFIED; 6 FLAGGED: entries 6, 8, 17, 18, 20, 22 are mawquf da'if per Salim al-Hilali.
   - 0 failed or unverified.
5. **Fixes to the editions.**
   - **Arabic edits reverted.** The two edits (entries 6 and 25; `corrections.json` deleted) are undone, so the Arabic is
     the source verbatim. Both sources were checked and have the same spelling. An unverified claim about the ʿAbd
     al-Bāqī edition was removed.
   - **Qur'an quotes.** Those written from memory were replaced by fetched Arabic plus the named QuranEnc translation of
     the whole verse. The clause inside entry 25 is labelled as a paraphrase.
   - **Grades.** Each entry shows its grade with the grader. Weak entries carry a red "weak (da'if) per Salim al-Hilali"
     label.
   - **Notes.** They are labelled editorial commentary. Unsourced appeals to "the commentators" were removed, and the
     grandfather relationship is now derived from the chain itself.
   - **Introductions** state that the meanings are the edition's own AI-assisted translation, not a published one.
6. **Outputs.**
   - `.sources.md` next to both reading editions and both retail packages;
   - `VERIFIED-ISLAMIC-REFERENCES.md`;
   - `data/verification/bank-additions-2026-11-22.{json,md}`, merged into the master bank by the nightly laptop sync.
     The protocol's step 6b and the scheduled-task prompt were updated for this.
7. **Edition standard** now carries the protocol rules (Arabic never edited, grade+grader, Qur'an handling, editorial
   notes, authentication gate).

**Authentication check: 29 verified, 6 flagged (da'if, Salim al-Hilali), 0 failed.**

## Still open

- **QuranEnc version of `bengali_zakaria`.**
  - It is not given by the API list, and the downloads returned HTTP 503 on 22 Nov.
  - It is a publication blocker for the Bengali edition and is listed in its release check.
  - Rerun `tools/verify_quran.py` when QuranEnc serves it.
- **Single grader.** Dorar is unreachable, so no second grading was added.
- **Scholar review** (reviewed_by) and ISBNs, as before.
- **Transcript upload** (8.7 MB is over the 3.1 MB connector limit): waiting for the owner's choice.
