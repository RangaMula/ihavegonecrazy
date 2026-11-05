> **REVIEW DRAFT.** This book prints a “review draft” notice on its title and copyright pages. Have a native speaker check it, then set `draft=False` in the language file and rebuild before uploading.

# KDP Publishing Guide — My First Arabic Alphabet (Allamahul Bayan Series, Book 27)

Upload files (both in `output/`):

| File | What it is | Spec |
|---|---|---|
| `interior.pdf` | Manuscript (interior) | 74 pages · 8.5 × 11 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | Full-wrap paperback cover | 17.4166 × 11.25 in · 0.125 in bleed · spine 0.1666 in (74 pp × 0.002252, white paper) |

## 1. Paperback details

- **Language:** English · **Book title:** My First Arabic Alphabet
- **Subtitle:** A Coloring Book to Learn, Trace & Say the 28 Arabic Letters with English Phonetics
- **Series:** Allamahul Bayan Series — **Series number:** 27 · **Edition:** 1
- **Author:** Hafez Abdullah Muhammad Minhaz Reza · **Contributors:** none (the AI assistance is declared in the AI-content questions)
- **Description** (HTML box):

```html
<p><b>Color your way into Arabic — one letter at a time!</b></p>
<p>Arabic is the language of the Qur’an and is spoken by about 380 million people across North Africa and West Asia. This big, friendly coloring book introduces young children to <b>28 letters</b> of Arabic <b>through English</b>, so no Arabic is needed at home.</p>
<ul>
<li><b>Every letter on its own page:</b> a giant letter to color, with its name written in Arabic <i>and</i> in English letters</li>
<li><b>Easy English sound guides</b> plus the letter’s <b>joined shapes</b> and its sounds with the vowel marks <b>fatḥa, kasra and ḍamma</b></li>
<li><b>A word and a picture for every letter</b> to color and say: قَلَم <i>qalam</i> (pen), مَسْجِد <i>masjid</i> (mosque), كِتَاب <i>kitaab</i> (book)…</li>
<li><b>Pencil tracing rows</b> on every page, plus warm-up tracing pages</li>
<li><b>Meet the language:</b> where Arabic is spoken, a map to color, the whole alphabet on one page, the numbers ٠–٩ and first friendly phrases</li>
<li><b>Single-sided coloring pages</b>, so markers never spoil the next picture, and a <b>certificate</b> to cut out and frame</li>
</ul>
<p>All pictures show objects, plants and nature only, which makes the book suitable for Muslim homes, schools and madrasas.</p>
<p><b>The Allamahul Bayan Series</b> takes its name from Surah Ar-Raḥmān: <i>“He taught him clear expression”</i> (55:4). Each book helps children thank Allah for the gift of language by meeting a new one: its letters, its sounds and the people who speak it.</p>
<p>Perfect for ages 3–7, heritage-language families, homeschoolers and teachers.</p>
```

- **Reading age:** 3 to 7 · **Primary marketplace:** Amazon.com (also Amazon.co.uk and Amazon.ca)
- **Categories:**
  1. Children's Books › Activities, Crafts & Games › Coloring Books
  2. Children's Books › Education & Reference › Foreign Language Study
  3. Children's Books › Religions › Islam
- **Keywords** (7 boxes):
  1. arabic alphabet book for kids
  2. learn arabic letters for children
  3. arabic alphabet coloring book
  4. huroof hijaiyah tracing workbook
  5. harakat fatha kasra damma for kids
  6. islamic coloring book for children
  7. quran arabic letters preschool

## 2. Paperback content

- Black & white interior · **White** paper · Trim **8.5 × 11 in** · **No bleed** · Matte cover
- Manuscript: `output/interior.pdf` · Cover: "Upload a cover you already have" → `output/cover.pdf`
- Blank pages flagged by the previewer are the intentional backs of the coloring pages.
- **ISBN:** a free KDP ISBN shows the imprint as "Independently published". To show
  **Maktabatu Kunujul Akhirah**, use your own ISBN (Bangladesh: National ISBN Agency, Archives & Libraries
  Directorate), put it in `isbn` in `languages/ar.py` and rebuild.

## 3. AI-generated content disclosure

Images: **AI-generated** (line art made with AI assistance, reviewed by the author).
Text: **AI-generated**, with substantial human editing.

## 4. Pricing (verify in KDP's calculator)

Printing ≈ **US $1.89** ($1.00 + 74 × $0.012). At **$8.99** royalty ≈ **$3.51**; at **$9.99** ≈ **$4.11**.

## 5. Must-do before publishing

1. A ḥāfiẓ or scholar checks the Qur’an text on pages 4–5.
2. **A native Arabic speaker proofreads every letter name, sound guide, word, transliteration and phrase.**
   Check every voweled word and letter name (especially the endings: words are shown in pause form, without a final case vowel), the transliterations, ضَوْء for ض and غَيْمَة for غ, and the Qur’an references on the letter pages (each names one verse where the word appears). Speaker number (about 380 million) needs a current Ethnologue check.
3. Order a printed proof copy.
