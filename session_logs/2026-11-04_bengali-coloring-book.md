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

---

## Part 2: "Continue to create for all available indian subcontinent languages"

### Decisions
- Scope: 17 major South Asian languages with their own alphabet and official status (table in
  `allamahul-bayan/README.md`). Smaller languages (Kashmiri, Konkani, Maithili, Santali and others) are listed for later.
- Built one shared engine (`allamahul-bayan/engine/`) with one data file per language (`allamahul-bayan/languages/`).
  The Bengali book was rebuilt through it and came out identical (120 pp).
- Maps for the new books show coastlines only, with no political borders (avoids Kashmir and Nepal border
  disputes), plus a dashed area for the region. Bengali keeps its Bangladesh–India border map.
- Every picture is object-only; about 60 new drawings were added (pomegranate, kite, kaaba, tasbih, ewer for wudu, olive …).
- Urdu: right-to-left letter order and tracing, joined forms (start, middle, end) for each letter, Nastaliq words.
- Rare letters (ङ ञ and similar) get a short note explaining their modern spelling.

### Built (all checked for page count, trim size and odd-page/blank-back parity)
1 Bengali 120 pp · 2 Hindi 122 · 3 Urdu 94 · 4 Punjabi 116 · 5 Gujarati 118 · 6 Marathi 118 · 7 Tamil 92 ·
8 Telugu 120 · 9 Kannada 118 · 10 Malayalam 122 · 11 Odia 116 · 12 Assamese 120 · 13 Nepali 118

### Not built yet
14 Sinhala, 15 Sindhi, 16 Pashto, 17 Dhivehi. The engine is ready, but the word lists need a native speaker.

### Next steps (owner)
1. Native-speaker proofread for every book (Odia and Assamese first), plus the scholar check of pp. 4–5.
2. Decide on ISBNs (own ISBNs → imprint shows as Maktabatu Kunujul Akhirah).
3. Upload to KDP one by one, then order proof copies.
4. Mirror `allamahul-bayan/` to G: and E: (this cloud session cannot reach them).
