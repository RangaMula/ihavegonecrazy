# KDP Publishing Guide — My First Bengali Alphabet (Allamahul Bayan Series, Book 1)

Upload files (both in `output/`):

| File | What it is | Spec |
|---|---|---|
| `interior.pdf` | Manuscript (interior) | 120 pages · 8.5 × 11 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | Full-wrap paperback cover | 17.5202 × 11.25 in · 0.125 in bleed · spine 0.2702 in (120 pp × 0.002252, white paper) |

> If the page count ever changes, rebuild — the spine width is recalculated automatically.

---

## 1. Paperback details (KDP page 1)

- **Language:** English
- **Book title:** My First Bengali Alphabet
- **Subtitle:** A Coloring Book to Learn, Trace & Say the 50 Bangla Letters with English Phonetics
- **Series:** Allamahul Bayan Series — **Series number:** 1
- **Edition number:** 1
- **Author:** Hafez Abdullah Muhammad Minhaz Reza
- **Contributors:** none. KDP's "Illustrator" role needs a person's name; the AI assistance is
  declared in the AI-content questions instead (section 3).
- **Description** (paste into the HTML box):

```html
<p><b>Color your way into Bengali — one letter at a time!</b></p>
<p>Bengali (Bangla) is spoken by about 270 million people in Bangladesh, India and all over the world. This big, friendly coloring book introduces young children to all <b>50 letters</b> of the Bengali alphabet <b>through English</b>, so no Bengali is needed at home.</p>
<ul>
<li><b>Every letter on its own page:</b> a giant letter to color, with its name written in Bengali <i>and</i> in English letters</li>
<li><b>Easy English sound guides</b> plus simple Bengali phonetics (ক্ + অ = ক)</li>
<li><b>A word and a picture for every letter</b> to color and say: আম <i>aam</i> (mango), নৌকা <i>noukaa</i> (boat), শাপলা <i>shaaplaa</i> (water lily)…</li>
<li><b>Pencil tracing rows</b> on every page, plus warm-up pages for the vowels and consonants</li>
<li><b>Meet the language:</b> where Bengali is spoken, a map to color, the whole alphabet on one page, the numbers ০–৯ and first friendly phrases</li>
<li><b>Single-sided coloring pages</b>, so markers never spoil the next picture</li>
<li>A <b>certificate</b> to cut out and frame at the end</li>
</ul>
<p>All pictures show objects, plants and nature only, which makes the book suitable for Muslim homes, schools and madrasas.</p>
<p><b>The Allamahul Bayan Series</b> takes its name from Surah Ar-Raḥmān: <i>“He taught him clear expression”</i> (55:4). Each book helps children thank Allah for the gift of language by meeting a new one: its letters, its sounds and the people who speak it.</p>
<p>Perfect for ages 3–7, heritage-language families, homeschoolers and teachers.</p>
```

- **Publishing rights:** I own the copyright and I hold the necessary publishing rights.
- **Primary audience:** Sexually explicit content = No · **Reading age:** 3 to 7
- **Primary marketplace:** Amazon.com (also consider Amazon.co.uk for UK Bengali families)
- **Categories** (choose up to 3):
  1. Children's Books › Activities, Crafts & Games › Coloring Books
  2. Children's Books › Education & Reference › Foreign Language Study
  3. Children's Books › Religions › Islam
- **Keywords** (7 boxes, each ≤ 50 characters, no words already in the title):
  1. bangla alphabet book for kids
  2. learn bengali for children
  3. bangla letters tracing workbook
  4. bengali language learning toddlers
  5. muslim kids activity book
  6. islamic coloring book for children
  7. heritage language gift bangladesh

## 2. Paperback content (KDP page 2)

- **Print ISBN:** see the ISBN note below.
- **Publication date:** leave blank (= the day it goes live).
- **Print options:** Black & white interior · **White** paper · Trim **8.5 × 11 in** · Bleed: **No bleed** ·
  Cover finish: **Matte** (better for coloring books; glossy also fine).
- **Manuscript:** upload `output/interior.pdf`.
- **Book cover:** "Upload a cover you already have" → `output/cover.pdf`.
- **Launch Previewer:** check every page; it should report no errors. Expect a note that some pages are
  blank — these are the backs of the coloring pages and are intentional.

### ISBN — important

- **Free KDP ISBN:** the "Imprint" on Amazon will show **"Independently published"**, not Maktabatu Kunujul Akhirah.
- **To show Maktabatu Kunujul Akhirah as publisher**, use an ISBN that you own. In Bangladesh, ISBNs are issued free
  by the **National ISBN Agency (Archives & Libraries Directorate, Dhaka)**. Enter it on KDP with imprint
  "Maktabatu Kunujul Akhirah". Also add it to `BOOK["isbn"]` in `tools/content.py` and rebuild, so it
  appears on the copyright page.

## 3. AI-generated content disclosure (required)

KDP asks whether the book contains AI-generated content. Answer honestly:

- **Images:** Yes — *AI-generated*. The line art was generated with AI assistance (as code) and reviewed and
  edited by the author.
- **Text:** the text was drafted with AI from the author's brief, so declare it as **AI-generated**, with
  substantial human editing. KDP only exempts text that *you* wrote and then polished with AI. The Arabic
  book was declared the same way.

## 4. Pricing (verify in KDP's calculator)

- Black & white, 120 pages, 8.5 × 11: printing cost ≈ **US $2.44** (KDP formula: $1.00 + 120 × $0.012).
- Suggested list price **US $8.99** → royalty ≈ 60% × 8.99 − 2.44 ≈ **$2.95 per copy**.
  ($9.99 → ≈ $3.55). Most competing alphabet coloring books sell between $6.99 and $9.99.

## 5. Must-do before you press Publish

1. **Qur'an check:** have a ḥāfiẓ or scholar verify the Arabic, harakāt, transliteration and English meaning of
   55:1–4, 30:22 and 49:13 on pages 4–5 (house rule).
2. **Bengali check:** have a native speaker read the letter names, words, transliterations and phrases.
3. **Order a printed proof copy.** Check that markers do not bleed through, that the gutter (inner margin) is
   comfortable, and that the cover colours look right.
4. Decide on the **ISBN** (above).
