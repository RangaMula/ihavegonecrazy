# Series Standard — Foundation Book of a World Language for Bangla-Speaking Adults

**One book per language. One method for every book.**
Instruction language: **বাংলা**. Bridge language: **English**. Target language: varies by book.

> Working series name (placeholder): **ভাষার দরজা — The Door to a Language**
> Per-book title pattern: **[ভাষা] ভাষার দরজা — Introduction to [Language] for Bangla Speakers**
> e.g. *আরবি ভাষার দরজা*, *জাপানি ভাষার দরজা*, *স্প্যানিশ ভাষার দরজা*

This standard reuses the production method of the *Introduction to Arabic* KDP series: a fixed page
budget, a frozen target-language layer, one data pack per edition, 3-layer review, human gates and a
certificate at the end. It changes three things on purpose:

| | KDP kids series (existing) | This series |
|---|---|---|
| Reader | Children aged 4–6, read aloud by a parent | **Adults** learning on their own: students, migrant workers, professionals, travellers, people who read for interest |
| Instruction | One language per edition, plus a separate mirror-page trilingual edition | **Bangla throughout, with English inside every learning item** (no mirror pages) |
| Goal | A fun first meeting with the language | Reader finishes at **A1 level (CEFR)** with real foundations, ready for intermediate grammar, vocabulary, speaking and literature |

---

## 1. Promise to the reader (identical in every book)

> এই বই শেষ করলে আপনি — [ভাষা] পড়তে পারবেন, এর ধ্বনিগুলো চিনবেন, ৫০০টি প্রয়োজনীয় শব্দ জানবেন,
> সহজ বাক্য নিজে বানাতে পারবেন, ২০টি বাস্তব পরিস্থিতিতে কথা বলতে পারবেন এবং এই ভাষার
> সাহিত্য ও সংস্কৃতির প্রথম স্বাদ পাবেন। এরপর আপনি মধ্যম স্তরের পথে যাত্রার জন্য প্রস্তুত।

Every book uses the same fixed quantities so the series feels like one product:

| Unit | Fixed count |
|---|---|
| Core vocabulary | **500 words**: 16 themes × 25 + 50 verbs + 50 adjectives (master list: `vocabulary/CORE-500.md`) |
| Sentence patterns | **12** |
| Real-life dialogues | **20** (2 pages each) |
| Graded reading texts | **6** |
| Writing tasks (লেখার অনুশীলন) | **24** (8 each in Parts 2, 3 and 4) + a tracing row on every script page |
| Proverbs / famous lines | **12** |
| Self-test | **60 questions** with answer key |
| Can-do checklist | **25 statements** (CEFR A1) |

---

## 2. The trilingual convention: the series' signature feature

**Rule:** explanations are in Bangla. English never explains anything. It sits beside every item as
a second key, so a reader who knows some English can check their understanding from two directions.
That works the way the English page does in the kids' trilingual edition, but the English is built
into each line.

### 2.1 The Triple Row: every word, phrase and sentence

| Target | বাংলা উচ্চারণ | English romanization | বাংলা অর্থ | English meaning |
|---|---|---|---|---|
| ありがとう | আরিগাতোউ | arigatō | ধন্যবাদ | thank you |
| شُكْرًا | শুকরান | shukran | ধন্যবাদ | thank you |
| gracias | গ্রাসিয়াস | GRAH-syahs | ধন্যবাদ | thank you |
| 谢谢 | শিয়ে-শিয়ে | xièxie | ধন্যবাদ | thank you |

- **Non-Latin scripts** (Arabic, Japanese, Chinese, Korean, Russian, Hindi, Thai and so on): the English column
  gives the **official romanization** for that language. Pinyin, Hepburn, Revised Romanization,
  ALA-LC/ISO 233 and ISO 9 are fixed per language in the language pack.
- **Latin scripts** (Spanish, French, German, Turkish and so on): romanizing would just repeat the word, so the English
  column gives an **English-style respelling with the stressed syllable in CAPITALS** (GRAH-syahs).
- On small layouts (cards, dialogue bubbles) the row collapses to three lines:
  target → বাংলা উচ্চারণ · romanization → বাংলা অর্থ / *English meaning*.

### 2.2 Bangla pronunciation notation (series-wide, defined once)

The Bangla-script transcription has to show sounds that Bangla does not have. Every book uses the same symbols,
explained on the front-matter page "উচ্চারণ-চিহ্নের চাবি":

| Need | Convention | Example |
|---|---|---|
| f / v / z (absent in Bangla) | Bangla letter + nukta: **ফ়, ভ়, জ়** | ফ়োন (phone), ভ়েরি (very) |
| Long vowel | colon-like mark **ː** after the vowel | শুকরাːন |
| Throat / guttural sounds (Arabic ع, ح, خ, غ; German ch) | Underlined letter, explained in Ch.5 | <u>হ</u>াবীব |
| Stress | **Bold syllable** | গ্রা**সি**য়াস |
| Tones (Chinese, Thai, Vietnamese…) | Arrow after the syllable: **→ ↗ ↘↗ ↘** | মা→, মা↗ |
| Sounds with no Bangla equivalent at all (French u, German ü) | Nearest Bangla letter + **°**, with a mouth-position note | ই° |

The Bangla transcription is the reader's starting point. The romanization stays the reference, and
the audio (QR code, §6) has the final say.

### 2.3 What stays in which language

| Element | Language |
|---|---|
| Chapter titles | Bangla title + English subtitle (`৫. ধ্বনির জগৎ — The Sound System`) |
| All explanations, stories, tips, instructions | Bangla only |
| Every target-language item | Full Triple Row |
| Glossary, index | Trilingual (target · Bangla · English) |
| Certificate | Bangla + English + one line in the target language |

---

## 3. The standard book structure

Recommended trim size: **7 × 10 in**. Five-column tables need the width that 6 × 9 lacks.
Page budget: **about 260 pages**, enforced with page-number asserts in the build script, as in the
kids series.

### FRONT MATTER (pp. i–xii)

| # | Page | Purpose |
|---|---|---|
| i | Title page | Bangla title, English title, target-language title in its own script |
| ii | Copyright & imprint | Maktabatu Kunujul Akhirah. Sources and licences |
| iii–iv | **ভূমিকা — A Word Before We Begin** | Why the series exists: the world through Bangla eyes |
| v–vi | **বইটি কীভাবে পড়বেন — How to Use This Book** | Study rhythm: one chapter a week, about 30 minutes a day. How to use the audio QR codes |
| vii | **তিন ভাষার চাবি — The Trilingual Key** | Explains the Triple Row with an annotated example |
| viii | **উচ্চারণ-চিহ্নের চাবি — Pronunciation Key** | The §2.2 symbols |
| ix–x | সূচিপত্র — Contents | |
| xi–xii | **আপনার যাত্রার মানচিত্র — Your Journey Map** | One-page visual of the 4 parts and the A1 finish line |

---

### PART ১ — ভাষাটিকে চিনুন · Meet the Language (about 24 pp)
*Purpose: capture the imagination before teaching anything. Story first, data second.*

| Ch | Title | Pages | Standard content |
|---|---|---|---|
| 1 | **গল্পের শুরু — How [Language] Was Born** | 4 | Opens on one vivid historical moment (scene-setting, like the Gindibu inscription in the Arabic book). Origins, key eras, oldest written record, how the script was born, 3 "did you know?" boxes |
| 2 | **কারা এই ভাষায় কথা বলে — Who Speaks It Today** | 4 | World map with countries shaded, speaker numbers (native and total), dialects and the standard variety this book teaches, **the Bangladeshi/Bengali diaspora link** (workers in the Gulf, students in Japan/Korea/Germany, communities in the UK/US) |
| 3 | **কেন শিখবেন — Why Learn It** | 4 | 8 reason cards. One is always **about Bangla speakers specifically**: jobs, migration, study, religion, trade, scholarships |
| 4 | **ভাষার পরিবার ও বাংলার আত্মীয়তা — Family Tree & Its Bond with Bangla** | 6 | Language family tree with Bangla placed on the same chart. Shared ancestry or contact history. **"আপনি আগে থেকেই জানেন" — 30 words you already know** (loanwords and cognates shared by Bangla and the target, e.g. Arabic কিতাব, Portuguese চাবি/জানালা, Persian দরজা, English চেয়ার). This chapter turns "foreign" into "familiar" |
| — | **Part 1 checkpoint** | 2 | 10-question quiz + "What surprised you?" reflection box |

---

### PART ২ — ধ্বনি ও লিপি · Sounds & Script (about 70 pp)
*Purpose: the reader can pronounce and read anything in the language, slowly but correctly.*

| Ch | Title | Pages | Standard content |
|---|---|---|---|
| 5 | **ধ্বনির জগৎ — The Sound System** | 10 | Every sound sorted into **three bins compared with Bangla**: ✅ the same as Bangla, 〰 close to Bangla, 🆕 new sound. New sounds get mouth-position diagrams. Vowel length, stress, tone or pitch accent where relevant. Minimal pairs. **Bangla speakers' advantages** (aspirates, retroflexes, etc.) and **typical Bangla-speaker mistakes** |
| 6 | **লিপি পরিচয় — The Writing System** | 40 (flexible, see §4) | **One letter or character group per page**, the kids-series letter format adapted for adults: the letter in all its forms, stroke order, name, sound (Triple Row), **5 everyday adult words** (Triple Row), one "watch out" note, and **a tracing row (dotted guide letters) plus 2 blank rows to write the letter and one of its words**. Ends with a full alphabet chart |
| 7 | **প্রথম পড়া — Reading Drills** | 12 | Syllables → words → short phrases → **real-world reading**: street signs, airport boards, shop signs, a menu, a medicine label, a form. Photos or redrawn signs |
| ✍️ | **লেখার অনুশীলন ১ — লিপিতে লেখা · Writing Practice 1: Script** | 4 | 8 tasks: copy 10 words from the Core list · write your own name and city in the script · write the 30 "words you already know" from Ch. 4 · dictation (listen to 10 words on the QR audio, write them) · complete half-written words · fill the blanks on 4 real signs · sort words by script feature (e.g. letter forms, kana type) · write a 5-word shopping list |
| — | **Part 2 checkpoint** | 4 | Read-aloud test (QR audio answer key), 15-question script quiz |

---

### PART ৩ — ভাষার ইট-পাথর · Building Blocks (about 84 pp)
*Purpose: words and patterns. A grammar **preview**, not a grammar course; full grammar is for intermediate.*

| Ch | Title | Pages | Standard content |
|---|---|---|---|
| 8 | **সংখ্যা — Numbers** | 10 | 0–20, tens, 100, 1,000, lakh vs million (**compared with Bangla's লাখ-কোটি**), ordinals. Real use: prices, phone numbers, ages, addresses, money and currency |
| 9 | **সময় ও পঞ্জিকা — Time & Calendar** | 10 | Days, months (plus a local calendar if one exists: Hijri, Japanese era, Chinese zodiac), seasons, telling time, dates, "yesterday/today/tomorrow". Includes a cultural calendar of festivals |
| 10 | **প্রয়োজনীয় ৫০০ শব্দ — The Core 500** | 30 | Every word in a Triple Row. **16 themes × 25:** pronouns & little words · questions & key expressions · people & family · body & health · food & drink · home & household · city & directions · transport & travel · shopping & money · work & professions · education & communication · nature, weather & animals · time words · feelings & character · religion, culture & festivals · documents, safety & emergency. **Plus 50 verbs and 50 adjectives.** Numbers and calendar words are in Ch. 8–9, not counted here. Full list: `vocabulary/CORE-500.md` |
| 11 | **বাক্যের কাঠামো — The Sentence Skeleton** | 20 | **12 core patterns**, each one compared with Bangla word order (e.g. Bangla SOV vs English SVO) and taught with a **substitution table**: (1) X is Y, (2) I have, (3) there is, (4) I want/need, (5) present action, (6) past action, (7) future action, (8) negation, (9) yes/no questions, (10) wh-questions, (11) can/must, (12) polite request. Plus one-page previews of gender, plurals, formality and cases as "what intermediate will teach you" |
| 12 | **ভদ্রতা ও সংস্কৃতি — Politeness & Culture** | 8 | Greetings by time and situation, forms of address (formal and informal, honorifics compared with Bangla আপনি/তুমি/তুই), gestures, gifts, table manners, taboos, religious sensitivities, business etiquette |
| ✍️ | **লেখার অনুশীলন ২ — শব্দ থেকে বাক্য · Writing Practice 2: Words to Sentences** | 4 | 8 tasks: write prices, phone numbers and dates in words · write today's date and your daily timetable · fill a personal-details form (name, age, address, profession, nationality) · write 2 sentences with each of the 12 patterns · turn 5 statements into questions and 5 into negatives · describe your family in 5 sentences · describe your home or room in 5 sentences · translate 5 short Bangla sentences |
| — | **Part 3 checkpoint** | 2 | Build-your-own-sentences exercise + 15-question quiz |

---

### PART ৪ — ভাষাটি ব্যবহার করুন · Use the Language (about 54 pp)
*Purpose: the reader **performs** the language. This is where they start to feel "I know it."*

| Ch | Title | Pages | Standard content |
|---|---|---|---|
| 13 | **২০টি বাস্তব সংলাপ — 20 Real-Life Conversations** | 40 | Same 20 scenes in every book, so the series feels unified: (1) greeting & introducing yourself, (2) airport & immigration, (3) taxi / ride-share, (4) hotel check-in, (5) asking directions, (6) restaurant, (7) shopping & bargaining, (8) money exchange / bank, (9) mobile SIM & internet, (10) doctor, (11) pharmacy, (12) renting a room, (13) first day at work, (14) job interview, (15) phone call, (16) university / admin office, (17) place of worship or cultural site, (18) making a friend & small talk, (19) emergency & police, (20) farewell & keeping in touch. **Format per scene:** page 1 = dialogue in Triple Rows, speaker bubbles (learner = "আপনি"); page 2 = 6 key phrases, 1 culture note, a "your turn" role-play prompt with blanks |
| 14 | **প্রথম পাঠ — Your First Reading** | 6 | 6 graded texts: a text message, a notice, a short email, a shopping list, a 1-page short story, a short news-style paragraph. Each has a full Triple-Row gloss and 3 comprehension questions |
| 15 | **সাহিত্যের প্রথম স্বাদ — A Taste of Literature** | 4 | 12 proverbs and famous lines (classical poetry, sacred text, a famous author), each paired with **a Bangla proverb or line with the same spirit** (e.g. a Japanese haiku beside a Rabindranath line). This is the bridge to literature at intermediate |
| ✍️ | **লেখার অনুশীলন ৩ — বাস্তব জীবনের লেখা · Writing Practice 3: Real-Life Writing** | 4 | 8 tasks, each tied to a dialogue scene: an arrival / landing card · a text message to a friend · a message to an employer (late, sick, leave) · a short email booking a room or appointment · a note to a neighbour or landlord · a postcard or greeting for a festival · a 60-word self-introduction (job interview) · a short diary entry about your first day in the new country |

---

### BACK MATTER (about 16 pp)

| Page | Title | Standard content |
|---|---|---|
| 16 | **মধ্যম স্তরের পথে — Your Road to Intermediate** | A 90-day plan after this book. The intermediate roadmap in 5 tracks: **grammar · vocabulary & word meaning · listening & speaking · pronunciation · literature**. Recognized exams (JLPT, HSK, TOPIK, DELE, DELF, Goethe, TORFL, etc.) with what level this book equals. Learning resources available in Bangladesh: institutes, embassies' cultural centres, apps |
| — | **নিজেকে যাচাই করুন — Self-Assessment** | 60-question final test + answer key + **model answers for all 24 writing tasks** + **25 can-do statements (CEFR A1)**, e.g. "আমি নিজের পরিচয় দিতে পারি", "আমি দাম জিজ্ঞেস করে বুঝতে পারি" |
| — | **ত্রিভাষিক শব্দকোষ — Trilingual Glossary** | Every word in the book: target · উচ্চারণ · romanization · বাংলা · English, sorted by the target language's own order |
| — | **তথ্যসূত্র — References** | Every fact, map, quotation and translation, with a source |
| — | **নোটের পাতা — Notes** | 4 lined practice pages, with a script practice grid where relevant |
| — | **সনদপত্র — Certificate of Completion** | "[ভাষা] ভাষার দরজা — ভিত্তি স্তর সম্পন্ন (Foundation Level / A1)", on a recto page with a blank back, signed as in the kids series. One congratulation line in the target language |

---

## 4. How chapter 6 (script) adapts to each language type

The 40 pages are a budget, not a fixed count. The structure changes by writing system and the rest of the book stays the same.

| Script type | Examples | Ch.6 layout |
|---|---|---|
| Alphabet, Latin | English, Spanish, French, German, Turkish, Indonesian | Letters in **sound groups** rather than A–Z (letters that match Bangla, then new ones, then digraphs and accents). About 1 page per 2 letters |
| Alphabet, other | Russian (Cyrillic), Greek | 1 page per letter, with "false friends" (letters that look Latin but sound different) |
| Abjad | Arabic, Persian, Urdu, Hebrew | 1 page per letter (same as the kids book): isolated/initial/medial/final forms, vowel marks, right-to-left reading |
| Abugida | Hindi, Nepali, Thai, Tamil, Burmese, Amharic | Compared directly with **Bangla, which is an abugida too**: vowel signs, conjuncts. Usually the shortest chapter for Bangla readers |
| Featural | Korean (Hangul) | Building-block logic: 14 consonants + 10 vowels + syllable-block assembly |
| Syllabary + logographs | Japanese | Hiragana (46) → Katakana (46) → the 100 most useful kanji |
| Logographic | Chinese | Pinyin and tones first, then 50 radicals, then the 150 most useful characters |

---

## 5. Tone and design rules for adult readers

- **Register:** warm, respectful, conversational Bangla (*আপনি* form). Talk to the reader as an intelligent adult: no childish
  emoji walls, no "Yay!". Use emoji only as small icons on cards and in key-phrase boxes.
- **Story before rule.** Every chapter opens with a scene, a surprise or a question, never a table.
- **Bangla as the anchor.** Every new concept is compared with how Bangla does it. This is what makes the book
  feel made *for* Bangla speakers rather than translated *to* them.
- **Always one practical win per page.** The reader should be able to *use* something from every spread.
- **Visual system:** one accent colour per book (taken from the culture of the language), a fixed layout grid,
  consistent boxes: 💡 টিপস · ⚠️ সাবধান · 🌏 সংস্কৃতি · 🔗 বাংলার সাথে মিল.
- **Fonts:** a professional Bangla body font (e.g. Noto Serif Bengali / Kalpurush), Noto Sans for English, and the
  matching Noto font for the target script. Verify each font renders, as the kids series does.

---

## 6. Audio companion (strongly recommended)

A Bangla speaker cannot learn pronunciation from print alone. Each chapter in Parts 2–4 gets a **QR code**
linking to native-speaker audio for every Triple Row on that page. The eBook can embed the audio. The Bangla
transcription helps the reader get started, but the native-speaker audio is the reference for correct pronunciation.

---

## 7. Production method (inherited from the KDP series)

| Element | Rule |
|---|---|
| **Template** | One frozen build script for the whole series (`build_book.py`), parameterized by a **language pack** per book |
| **Language pack** (`langpack_<code>.py`) | Script inventory, sound bins, romanization system, Bangla-transcription table, 500 words, 12 patterns, 20 dialogues, 6 readings, 12 proverbs, 30 shared words, country list, calendar, quiz and answers |
| **Fixed layer** | Bangla instruction text (shared across books, with language-specific inserts in marked slots) |
| **Variable layer** | Target-language content + English column |
| **Page asserts** | Each Part starts on a fixed page number; the build fails if the budget breaks |
| **3-layer review** | (1) Target → Bangla accuracy and coherence; (2) triangulation: target → English vs target → Bangla must land on the same meaning; (3) web verification against credible sources: dictionaries, official romanization standards, and recognized translations for sacred or literary quotes |
| **Human gates** | Native target-language speaker review · Bangla editor review · pronunciation check against audio · ISBN · AI disclosure · proof copy |
| **Status file** | `EDITION-STATUS.md` + `REVIEW-REPORT.md` per book, same format as the kids series |
| **Formats** | Print interior PDF (7×10), full-wrap cover, fixed-layout or reflowable EPUB with audio links |

---

## 8. Book order

The full, ordered list of books (18 books in 4 waves, plus later candidates), with the reason for each
position, is in **`SERIES-ROADMAP.md`**.

---

## Page budget summary (7×10 in, about 260 pp)

| Section | Pages |
|---|---|
| Front matter | 12 |
| Part 1 — Meet the Language | 24 |
| Part 2 — Sounds & Script (incl. 4 pp writing) | 70 |
| Part 3 — Building Blocks (incl. 4 pp writing) | 84 |
| Part 4 — Use the Language (incl. 4 pp writing) | 54 |
| Back matter | 16 |
| **Total** | **≈ 260** |

---

## 9. Writing practice (লেখার অনুশীলন): standard design

Writing runs through Parts 2–4 as three blocks of 8 tasks each, moving from **script → sentences → real-life texts**.
Part 1 has no writing task, because the reader has not met the script yet.

| Rule | Detail |
|---|---|
| Instructions | In Bangla, with one worked example per task |
| What the reader writes | **Only the target script** from Part 2 onward. Romanization or Bangla-script transcription is never accepted as an answer |
| Layout | Writing lines sized for the script: wide grid boxes for Chinese and Japanese, four-line guides for Latin script, baseline-and-dot guides for Arabic-type scripts |
| Help levels | Each task is marked ★ (copy), ★★ (fill in) or ★★★ (write freely), so the reader can see the progression |
| Model answers | Every task has a model answer in the back matter. Free-writing tasks give one sample answer plus a "check yourself" list (e.g. "Did you use a greeting? A date? A polite closing?") |
| Audio link | The dictation tasks use the same QR audio as the rest of the chapter |
| Real-life focus | Every Part 4 task matches a dialogue scene in Ch. 13, so the reader writes what they would actually need to write abroad |
