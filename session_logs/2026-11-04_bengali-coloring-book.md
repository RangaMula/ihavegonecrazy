# Session log — 4 Nov 2026 — Allamahul Bayan Series, Book 1 (Bengali coloring book)

Surface: Claude Code on the web (cloud container). Repo: RangaMula/ihavegonecrazy,
branch `claude/sweet-euler-11udki`. Project folder: `allamahul-bayan/book-01-bengali/`.

## Requests (in the user's words)
- "Create Kids Coloring Book that contains language learning, specifically letters of a language, introduced by
  english language and phonetics presented in that native language + english language … Create the first one
  introducing bengali language"
- "formatted in a way to be able to published in amazon. writer is me, illustrator - AI assisted and publisher is
  MAktabatu Kunujul Akhirah"
- "Introduce the series as Allamahul Bayan Series and in the introduction in english, tell about the Allah's ayat
  in quran 'Allamahul Bayan' and what it means and how it inspires the language learning series."
- Picture style: "find the maktabatu kunujul akhirah publishing or creating principal. Its available in your workspace"

## Decisions
- Publishing rules taken from Drive → `REGENERATION-PROMPT.md` (Introduction to the Arabic Language for Kids):
  no people or animals with faces; every item = script + transliteration + English; cite every Qur'an quote
  (¹ on the References page); scholar review before publishing; certificate on an odd page with a blank back;
  build as code (Python → HTML → headless Chromium → PDF).
  → Every picture is an object, a plant or nature (no animals at all), e.g. শাপলা, মসজিদ, জায়নামাজ, খেজুর.
- Author name = "Hafez Abdullah Muhammad Minhaz Reza" (as on the Arabic book); publisher block +
  logo mark from Drive `maktabatu-logo-english.svg`.
- Format: 8.5 × 11 in, black & white, white paper, no bleed, 120 pages; each coloring page is odd with a blank back.
- Series intro (pp 4–5): 55:1–4 (ʿallamahul-bayān = clear expression), 30:22 (languages + colours =
  signs → coloring + language), 49:13 (to know one another).
- Phonetics in 3 forms per letter: Bengali name in Bengali, the name transliterated, an English sound guide,
  plus native phonetics (ক্ + অ = ক / vowel sign ক + া = কা).

## Deliverables
- `allamahul-bayan/book-01-bengali/output/interior.pdf` (120 pp, 8.5×11)
- `allamahul-bayan/book-01-bengali/output/cover.pdf` (17.5202 × 11.25 in, spine 0.2702 in)
- `KDP-PUBLISHING-GUIDE.md` (metadata, description HTML, keywords, categories, ISBN note, AI disclosure, price)
- `README.md` + build tools (`tools/`), fonts (`assets/fonts/`, OFL)

## Next steps (owner)
1. Scholar/ḥāfiẓ review of the ayāt on pages 4–5; native-Bengali proofread.
2. Decide on the ISBN. A free KDP ISBN shows the imprint as "Independently published"; an own ISBN from the
   BD National ISBN Agency lets the imprint show as Maktabatu Kunujul Akhirah.
3. Upload to KDP, then order a proof copy.
4. Mirror this folder to `G:\My Drive\Claude Workspace\Maktabatu Kunujul Akhirah\` + `E:\Claude Backup`. This cloud
   session cannot reach the local drives; pull the branch from GitHub.
