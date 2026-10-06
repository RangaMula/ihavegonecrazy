# ভাষার দরজা — Series Playbook

**Read this first.** It holds everything learned while making the first book of the series
(*ফরাসি ভাষার দরজা · La porte du français*), so the next book (or the next session or agent)
starts with the full plan and none of the old mistakes.

| Document | What it holds |
|---|---|
| **PLAYBOOK.md** (this file) | Author's decisions, workflow, agent briefs, file formats, lessons learned, QA checklist |
| `BOOK-STRUCTURE.md` | The book's chapter-by-chapter specification |
| `SERIES-ROADMAP.md` | The order in which books are made (18 languages in 4 waves) |
| `MASTER-LANGUAGE-LIST.md` | All 143 deliverable languages, tiered A/B/C (supersedes `KDP-ARABIC-LANGUAGES.md`) |
| `vocabulary/WORD-JOURNEY.md` | The 2,000-word journey: 6 stages, 20 sections, 80 sets |
| `foreword/` | The author's Bangla foreword (identical in every book) |
| `brand/` | Publisher logos |
| `books/fr-2e/` | **The reference implementation.** Copy it to start a new book |

---

## 1. The author's decisions (do not change without asking the author)

These are the author's own instructions, given while the first book was made.

### Reader and language
1. **One book per language**, all following one method. Readers are **adults**: students, migrant workers,
   professionals, curious readers. (The author's Amazon KDP Arabic books are for children; this series is not.)
2. **Instruction language is Bangla** (Bangladeshi চলিত, আপনি form).
3. **English is always present as the third language**: every target-language item is a *Triple Row*
   (target · বাংলা উচ্চারণ · English pronunciation · বাংলা অর্থ · English meaning).
4. **Purpose:** introduce a language *and* a culture: exotic places, new people, their food, festivals,
   history and wonder words. The book must capture the imagination, not just list survival words.
5. **No standard-exam requirements.** Do not shape content to fit JLPT, DELF, TOPIK and so on. They are only mentioned as a next step.

### Fixed content
6. **লেখকের কথা (Author's Foreword)** is **Bangla only**, the same text in every book, with the author's vector signature
   and the Bangla logo. Source: `foreword/foreword.html`. Only the running head changes per book.
7. **Dawah:** every book has **Ch. 16 «আমার বিশ্বাসের পরিচয়» (Introducing My Faith)**:
   - **70%**: introduce your faith in first-person target-language sentences: the manner of dawah (16:125), the salam, «I am a Muslim», the six articles of faith, the five pillars, values, and Surah al-Ikhlas with a recognised target-language translation.
   - **30%**: an FAQ, «প্রতিবেশী বা সহকর্মী জানতে চাইলে», with 12 questions.
   - Smaller supporting touches elsewhere: Word Journey set 14a «Islam in everyday words», dialogues 17 (mosque and salam) and 18 (fasting and iftar invitation), one Qur'an verse and one hadith in Ch. 15, and an Eid or Ramadan writing task.
   - Tone: warm, never preachy, never argumentative, and respectful of every faith.
8. **Vocabulary = 2,000 words** as the **শব্দের যাত্রা (Word Journey)**: 20 sections of 100 words, and
   **each section must give a sense of accomplishment**:
   - an opening goal
   - a word counter
   - a tick box for every word
   - «এখনই বলুন» sentences
   - a mission
   - a quiz
   - a passport stamp
   Each of the 6 stages ends with a **milestone story** written only in words already taught.
   About 1,300 fixed words are the same in every book; about 700 culture words are chosen fresh for each language.
9. **Writing practice** (24 tasks in 3 blocks) is included.

### Brand
10. **Publisher name spelling: «মাকতাবাতু কুনুজুল আখিরাহ»** (Maktabatu Kunujul Akhirah). The trust is «কুনুজুল আখিরাহ চ্যারিটেবল ট্রাস্ট».
    Never invent a different transliteration.
11. **Author line:** হাফেজ আবদুল্লাহ মুহাম্মদ মিনহাজ রেজা. The titles under the signature are
    «স্বত্বাধিকারী, মাকতাবাতু কুনুজুল আখিরাহ · প্রতিষ্ঠাতা, কুনুজুল আখিরাহ চ্যারিটেবল ট্রাস্ট» (still awaiting the author's confirmation).
12. **Logos** (in `brand/`):
    - Bangla: title page, foreword, certificate
    - English: copyright page
    - Arabic: the language passport cover

### Layout and content limits
13. **Layout: use the space.** The author rejected half-empty pages. Use the **2nd-edition compact composition** (`books/fr-2e/`): continuous flow, about 89% average page fill. Never leave large blank areas, and never jumble content.
14. **No pork or alcohol** in vocabulary, dialogues or examples. The only exception is the halal explanation in Ch. 16.
15. **Ask before adding** anything the author has not seen when it is personal to them (forewords, statements in their name).
    Show drafts first.

---

## 2. Production workflow for a new book

Work in this order and commit after every step. The author's own save rule says: commit and push early and often, and state what was saved.

| Step | What | Who |
|---|---|---|
| 0 | Read this playbook, `BOOK-STRUCTURE.md`, `WORD-JOURNEY.md` and the target row of `SERIES-ROADMAP.md` | Lead session |
| 1 | `cp -r books/fr-2e books/<code>`, then delete `data/*.json`, `book.html`, the PDFs and `data/.measure_cache.json` | Lead |
| 2 | Write `books/<code>/STYLE.md` (see §4): the Bangla pronunciation table and the English column standard for this language | Lead (this is the most important file) |
| 3 | Set the per-book constants: `engine.BOOK_TITLE_BN`, the accent colour (`--accent`), and the title and copyright text in `front.py` | Lead |
| 4 | Write **Part 1** (`part1.py`): the history hook, who speaks it, why learn it, the family tree and Bangla links, and the «words you already know» list | Lead (needs care and verified facts) |
| 5 | Adapt **Ch. 16** (`ch16.py`): translate all sentences, pick the recognised Qur'an translation for this language, and check the Islamic terms the local community uses | Lead |
| 6 | Launch **content agents in parallel** (§3): Parts 2+3, Part 5, journey sections 1–10, journey sections 11–20 | Agents |
| 7 | Validate every data file (§5) and fix any failures **before** layout | Lead |
| 8 | Build with `./make.sh out.pdf`, then check fill with `fill.js` (§6) | Lead |
| 9 | Visual QA on contact sheets of sample pages (§6) | Lead |
| 10 | Commit and push, then send the PDF to the author | Lead |
| 11 | Human gates before print: native-speaker editor, Bangla editor, scholar review (Ch. 16 and every Qur'an and hadith line), fact check of the «জানেন কি?» lines | Author |

---

## 3. Content agents: how to brief them (and what went wrong)

Four agents wrote the French content in parallel. Their briefs are the model to reuse. Each brief must contain:
- the paths of `STYLE.md`, `BOOK-STRUCTURE.md` and `WORD-JOURNEY.md`, which the agent must read first;
- the exact **JSON shape** (copy it from §5);
- exact counts (25 words per set, 20 dialogues, and so on);
- the content limits (adult register, Bangladeshi Bangla, no pork or alcohol, respectful of all faiths, breadth across the whole language area);
- "only facts you are certain of; add `source_hint`";
- "validate with Python before reporting";
- "do not commit";
- **"use your own scratch folder: `scratchpad/<task-name>/`"**.

**Lessons learned with French (these must not happen again):**

| Problem | What happened | Rule now |
|---|---|---|
| **Duplicates across the two journey halves** | The writer of sections 11–20 couldn't see sections 1–10, so 82 words were repeated | Write sections 1–10 **first**, then give the 11–20 agent the finished file and require a zero-overlap check against it. Or run them in parallel and do a dedupe pass straight after. Always run the cross-file check yourself (§5). |
| **Shared scratch folder** | Two agents used `scratchpad/fr/`, and one overwrote the other's build script | Give each agent its own scratch folder by name |
| **A message arrived after an agent had finished** | A follow-up request reached an agent that had already completed | After an agent reports back, check the file yourself. If the fix isn't in it, send the request again (this resumes the agent with its context). |
| **Moving an agent's file while it was writing** | The lead moved a data file during a test build | Never touch an agent's output file until its completion notice arrives. To build without a part, use `SKIP=part4 ./make.sh` |
| **Uncertain quotations** | Agents correctly dropped quotations whose wording they couldn't confirm | Keep this rule. A misquoted famous line is worse than none. |
| **Overlap with the Part 1 list** | Journey section 19b repeated loanwords from Ch. 4 | Give the agent the Ch. 4 «words you already know» list as a no-reuse list |

---

## 4. Writing `STYLE.md` for a new language

Copy `books/fr/STYLE.md` and rewrite §3–§5 for the new language.

1. **Bangla pronunciation table.** Map **every** sound of the language to Bangla script using the series notation:
   - **nukta (়)** for a consonant Bangla lacks (ফ় f, ভ় v, জ় z, ঝ় ʒ, র় for a throat r and similar);
   - **°** after a syllable whose vowel is rounded or otherwise has no Bangla equivalent;
   - **chandrabindu (ঁ)** for nasal vowels;
   - tones (Chinese, Thai, Vietnamese): arrows after the syllable (→ ↗ ↘↗ ↘);
   - long vowels: ː.
   Give one example word per row. **Every agent follows this table literally**, so make it complete and unambiguous.
   Put the nukta *before* the vowel sign (ঝ়ে, not ঝে়).
2. **English column:**
   - Non-Latin scripts use the official romanization (Pinyin, Hepburn, Revised Romanization, ALA-LC and so on).
   - Latin scripts use an English respelling with the stressed syllable in CAPS.
3. **Content rules:**
   - the countries and regions to cover;
   - the Bangla links to look for (loanwords, shared roots, historical contact with Bengal);
   - culture specifics, such as which foods are halal-friendly showcases.

---

## 5. Data formats (the contract between agents and the engine)

All files live in `books/<code>/data/`, as UTF-8 JSON. The **Triple Row** object is used everywhere:

```json
{"fr": "Bonjour", "bn_pron": "বোঁঝ়ুর়", "en_pron": "bohn-ZHOOR", "bn": "শুভ দিন", "en": "hello", "note_bn": "optional"}
```
(The key `fr` holds the **target-language text** for every language; the engine reads `fr`. Keep the name.)

| File | Contents |
|---|---|
| `journey_1_10.json`, `journey_11_20.json` | `sections[]`: no, stage, title_bn/en, scene_bn, can_do_bn[3], sets[4 × {code, kind F/C, title_bn/en, words[25]}], say_now[5], mission_bn, quiz[10 {q_bn, a}], stamp{label_bn, icon}. `milestones[]`: after_section, total, title_bn/fr, celebration_bn, reading[8–12]. Culture words add icon, story_bn, link_bn, source_hint. |
| `part2.json` | ch5 (sound bins same/close/new, explanations, minimal pairs), ch6 (letter groups → letters with 5 words, accents, combinations), ch7 (syllables, words, phrases, signs, menu, form, medicine), writing1[8], checkpoint2 |
| `part3.json` | ch8 numbers, ch9 time and festivals, ch10 12 patterns (with substitution tables), ch11 politeness and customs, writing2[8], checkpoint3 |
| `part5.json` | dialogues[20] (lines with who/you), readings[6], literature[10] (each with bangla_pair), writing3[8], selftest[60], can_do[25], road{} |

**Validation to run before layout** (French examples are in the commit history):
- every Triple Row has all 5 fields filled; the counts are exact;
- **no duplicate target word across all 2,000** (lowercase, strip the article and the gender tag);
- the nukta/° notation passes a scan;
- no pork or alcohol words.

---

## 6. The layout engine (`books/fr-2e/`)

| File | Role |
|---|---|
| `engine.py` | Page model, CSS, Triple Row components, render, page numbering, anchors for the contents page |
| `part23.py` | **Flow engine.** Measured, continuous composition: blocks, headings kept with the next block, tables breaking between rows (header repeated), card grids breaking between rows, writing and quiz blocks, and `FlowPages` for hand-written chapters |
| `measure.py` / `measure.js` | Every block is measured in a real browser at page width. Heights are cached in `data/.measure_cache.json` |
| `make.sh` | Builds, measures any blocks not yet measured, rebuilds (up to 4 passes), then renders the PDF and reports overflow |
| `front.py`, `part1.py`–`part5.py`, `ch16.py`, `back.py` | Content modules |
| `render.js` | PDF and PNG output plus the overflow check |

**Rules that keep pages full and clean:**
- **Never** force a page break inside a chapter. `Flow(head, anchor)` starts a new chapter or section: it continues on the current page if ≥ `MIN_START` (3 in) is free.
- Fixed full pages are used only for part openers, the title, copyright, passport and certificate.
- **Tables must use fixed column widths** (`table-layout:fixed` plus a colgroup). Otherwise rows measured alone differ from rows in the real table, and pages overflow.
- Headings (`h2`, `h3`, `.chhead`) are kept with the next block automatically through `Flow.html` / `keep=True`.
- `PAGE_H = 8.26 in` is the usable height, with a small safety margin.
- After each build, check:
  - overflow: `make.sh` must print `no overflow`;
  - page fill: `NODE_PATH=$(npm root -g) node fill.js book.html detail` should show an average of at least 88% and almost no pages under 50%, apart from intended blanks.
- Visual QA: screenshot about 12 pages from across the book and tile them into a contact sheet (with PIL) to check that pages are dense but not jumbled.

**The French results to beat:** 1st edition 534 pages at 76% fill; 2nd edition 424 pages at 89% fill.

---

## 7. Environment notes (cloud container)

- **Fonts** come from the npm registry (`npm pack @fontsource/...`). jsdelivr and Google Fonts downloads are blocked. Fonts in use: Noto Serif (latin and latin-ext), Noto Serif Bengali, Noto Sans Bengali, Amiri. Add the Noto font for the target script, for example `@fontsource/noto-sans-jp`.
- **Playwright and Chromium** are pre-installed (`NODE_PATH=$(npm root -g)`). Python: `pip install pillow numpy potracer` when needed.
- **Google Drive:** the author's Amazon KDP folder holds the earlier kids' Arabic series: build scripts, review reports and `KDP-Language-Opportunity-Matrix.csv`.
- **Never** `rm -f $VAR/*`. A safety check blocks it; use a literal path or `"${VAR:?}"/...`.
- The author's local Windows paths (`C:\...`, `G:\...`, `E:\...`) can't be reached from the cloud. Ask the author to put files on Drive or attach them in chat.

---

## 8. Publishing facts

- **KDP does not support Bengali** as a book language (paperback or eBook). The kids' series got around this by declaring
  the trilingual edition as English, but that is **not honest for a Bangla-majority book**. Options: Rokomari or printers in Bangladesh,
  Google Play Books (it accepts all languages), or an Indian print-on-demand service that handles Bengali (not yet checked).
- Trim size is **7 × 10 in**. The French 2nd edition has 424 pages.
- Before print: ISBN, AI disclosure, proof copy, and the human review gates (§2, step 11).

---

## 9. Open decisions (ask the author when resuming)

1. Which edition style is final? The 2nd (compact) is the default unless the author says otherwise.
2. The titles under the author's signature (§1.11).
3. The foreword's page count. It is currently 7 pages, with the 49:13 plate as page x so Part 1 opens on a right-hand page.
4. The publishing channel for Bangla books (§8).
5. Whether to split long books into two volumes.
6. Audio: native-speaker recordings and QR codes (planned in `BOOK-STRUCTURE.md` §6, not yet made).

---

## 10. QA checklist before sending a book to the author

- [ ] All data files validate (counts, fields, zero duplicates across the 2,000, notation, no pork or alcohol)
- [ ] `make.sh` reports `no overflow`; fill is ≥ 88% average, with almost no pages under 50%
- [ ] Contents page numbers resolve (no «—»)
- [ ] Contact-sheet visual check of about 12 pages: nothing cramped, nothing split badly, headings never orphaned
- [ ] Foreword, logo and signature present; publisher name spelled «মাকতাবাতু কুনুজুল আখিরাহ»
- [ ] Ch. 16 present with the 70/30 balance; the Qur'an translation is named and listed in References
- [ ] References page updated for this language
- [ ] Committed and pushed; the PDF sent; the open items listed for the author

---

## 11. Right-to-left books (Arabic, then Urdu and Persian)

Learned while starting `books/ar/` (Arabic). Reuse this for every Arabic-script book.

- **`engine.E()` wraps every Arabic run** in `<span class="ar">` (Amiri font, `direction:rtl`, `unicode-bidi:isolate`). So Arabic inside
  Bangla notes and paragraphs (e.g. «বহুবচন: كُتُب (কুতুব)») displays in the right order and size without any markup in the data.
- Target-text CSS (`.frw`, `td.c-fr`, `.trl .l1`, `.dl .f`, `.cc .fr`, `.faq .frq/.afr`) is switched to the Arabic font, right-aligned, and about 30% larger than the Latin size,
  because Amiri with full harakat looks small at Latin sizes. Give it a line-height of about 1.45–1.8.
- Column shares in Triple Row tables change: Arabic needs **less** width than French (fr 0.19, bp 0.23, ep 0.20, bn 0.20, en 0.18 of the free width).
- Substitution tables (Ch. 10) get `dir="rtl"`, so they read right to left.
- The letter card (Ch. 6) shows the **4 positional forms** (একা · শুরুতে · মাঝে · শেষে) under the big letter instead of a tracing line.
- The Bangla pronunciation notation for Arabic is in `books/ar/STYLE.md` §3: nukta letters থ় দ় হ় খ় গ় ক় জ় স় ফ়, ড/ট/য for ض/ط/ظ,
  ʿ for ع, ʾ for hamza, ː for long vowels, short a always া (never অ), and the pause rule. Urdu and Persian should start from this table.
- The nukta on থ দ হ খ গ ক স renders correctly in Noto Serif/Sans Bengali (a small dot below). ː falls back to a colon-like glyph, which is acceptable.
- `books/ar/validate.py` is the data validator (counts, fields, Latin letters in Arabic, duplicates across the 2,000 after stripping harakat and ال,
  reuse of the Ch. 4 list, banned words). Copy it for the next book.
