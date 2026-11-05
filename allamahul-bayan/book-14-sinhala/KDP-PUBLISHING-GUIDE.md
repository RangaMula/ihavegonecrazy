> **REVIEW DRAFT.** This book prints a “review draft” notice on its title and copyright pages. Have a native speaker check it, then set `draft=False` in the language file and rebuild before uploading.

# KDP Publishing Guide — My First Sinhala Alphabet (Allamahul Bayan Series, Book 14)

Upload files (both in `output/`):

| File | What it is | Spec |
|---|---|---|
| `interior.pdf` | Manuscript (interior) | 120 pages · 8.5 × 11 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | Full-wrap paperback cover | 17.5202 × 11.25 in · 0.125 in bleed · spine 0.2702 in (120 pp × 0.002252, white paper) |

## 1. Paperback details

- **Language:** English · **Book title:** My First Sinhala Alphabet
- **Subtitle:** A Coloring Book to Learn, Trace & Say the 50 Sinhala Letters with English Phonetics
- **Series:** Allamahul Bayan Series — **Series number:** 14 · **Edition:** 1
- **Author:** Hafez Abdullah Muhammad Minhaz Reza · **Contributors:** none (the AI assistance is declared in the AI-content questions)
- **Description** (HTML box):

```html
<p><b>Color your way into Sinhala — one letter at a time!</b></p>
<p>Sinhala is spoken by about 17 million people as their first language, in Sri Lanka and around the world. This big, friendly coloring book introduces young children to <b>50 letters</b> of the Sinhala alphabet <b>through English</b>, so no Sinhala is needed at home.</p>
<ul>
<li><b>Every letter on its own page:</b> a giant letter to color, with its name written in Sinhala <i>and</i> in English letters</li>
<li><b>Easy English sound guides</b> plus simple Sinhala phonetics (ක් + අ = ක, and the vowel signs)</li>
<li><b>A word and a picture for every letter</b> to color and say: පොල් <i>pol</i> (coconut), සඳ <i>sanda</i> (moon), අඹ <i>amba</i> (mango)…</li>
<li><b>Pencil tracing rows</b> on every page, plus warm-up pages for the vowels and consonants</li>
<li><b>Meet the language:</b> where Sinhala is spoken, a map to color, the whole alphabet on one page, the numbers 0–9 and first friendly phrases</li>
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
  1. sinhala alphabet book for kids
  2. learn sinhala for children
  3. sinhala letters tracing workbook
  4. sinhala hodiya coloring book
  5. muslim kids activity book
  6. islamic coloring book for children
  7. sri lankan heritage language gift

## 2. Paperback content

- Black & white interior · **White** paper · Trim **8.5 × 11 in** · **No bleed** · Matte cover
- Manuscript: `output/interior.pdf` · Cover: "Upload a cover you already have" → `output/cover.pdf`
- Blank pages flagged by the previewer are the intentional backs of the coloring pages.
- **ISBN:** a free KDP ISBN shows the imprint as "Independently published". To show
  **Maktabatu Kunujul Akhirah**, use your own ISBN (Bangladesh: National ISBN Agency, Archives & Libraries
  Directorate), put it in `isbn` in `languages/si.py` and rebuild.

## 3. AI-generated content disclosure

Images: **AI-generated** (line art made with AI assistance, reviewed by the author).
Text: **AI-generated**, with substantial human editing.

## 4. Pricing (verify in KDP's calculator)

Printing ≈ **US $2.44** ($1.00 + 120 × $0.012). At **$8.99** royalty ≈ **$2.95**; at **$9.99** ≈ **$3.55**.

## 5. Must-do before publishing

1. A ḥāfiẓ or scholar checks the Qur’an text on pages 4–5.
2. **A native Sinhala speaker proofreads every letter name, sound guide, word, transliteration and phrase.**
   Check every letter name (-yanna names, mahaapraana / sanyaka / muurdhaja / dantaja / taaluja), the pilla (vowel-sign) names, and these words: ශාඛාව (branch, for ඛ), ඝනකය (cube, for ඝ), දඬුව (stick, for ඬ), ෂඩස්‍රය (hexagon, for ෂ), තෛලය (oil, for ඓ), භෝජනය (meal), ඡත්‍රය (umbrella), රථය (cart), ෆුට්බෝල් (football). Confirm the Sinhala spellings of the Muslim phrases (අස්සලාමු අලෛකුම්, ජසාකල්ලාහු ඛයිරන්) and the choice of letters (50 of the ~60-letter hodiya).
3. Order a printed proof copy.
