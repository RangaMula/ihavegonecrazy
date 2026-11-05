> **REVIEW DRAFT.** This book prints a “review draft” notice on its title and copyright pages. Have a native speaker check it, then set `draft=False` in the language file and rebuild before uploading.

# KDP Publishing Guide — My First Vai Syllables (Allamahul Bayan Series, Book 61)

Upload files (both in `output/`):

| File | What it is | Spec |
|---|---|---|
| `interior.pdf` | Manuscript (interior) | 144 pages · 8.5 × 11 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | Full-wrap paperback cover | 17.5743 × 11.25 in · 0.125 in bleed · spine 0.3243 in (144 pp × 0.002252, white paper) |

## 1. Paperback details

- **Language:** English · **Book title:** My First Vai Syllables
- **Subtitle:** A Coloring Book to Learn, Trace & Say the 56 Vai Syllables with English Phonetics
- **Series:** Allamahul Bayan Series — **Series number:** 61 · **Edition:** 1
- **Author:** Hafez Abdullah Muhammad Minhaz Reza · **Contributors:** none (the AI assistance is declared in the AI-content questions)
- **Description** (HTML box):

```html
<p><b>Color your way into Vai — one letter at a time!</b></p>
<p>Vai is spoken by more than 100,000 people in Liberia and Sierra Leone, and has its own West African script. This big, friendly coloring book introduces young children to <b>56 syllables</b> of Vai <b>through English</b>, so no Vai is needed at home.</p>
<ul>
<li><b>Every letter on its own page:</b> a giant letter to color, with its name written in Vai <i>and</i> in English letters</li>
<li><b>Easy English sound guides</b> plus the whole row of the Vai chart for every syllable (ꕒ ba sits between ꔬ bi and ꕸ bɔ)</li>
<li><b>A word and a picture for every letter</b> to color and say: ꕙꔤ <i>VAH-ee</i> (Vai), ꕒ <i>bah</i> (the syllable ba), ꕮ <i>mah</i> (the syllable ma)…</li>
<li><b>Pencil tracing rows</b> on every page, plus warm-up tracing pages</li>
<li><b>Meet the language:</b> where Vai is spoken, a map to color, the whole alphabet on one page, the numbers ꘠–꘩ and first friendly phrases</li>
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
  1. vai script book for kids
  2. learn vai syllabary for children
  3. liberia language coloring book
  4. west african script tracing workbook
  5. muslim kids activity book
  6. islamic coloring book for children
  7. african heritage language gift

## 2. Paperback content

- Black & white interior · **White** paper · Trim **8.5 × 11 in** · **No bleed** · Matte cover
- Manuscript: `output/interior.pdf` · Cover: "Upload a cover you already have" → `output/cover.pdf`
- Blank pages flagged by the previewer are the intentional backs of the coloring pages.
- **ISBN:** a free KDP ISBN shows the imprint as "Independently published". To show
  **Maktabatu Kunujul Akhirah**, use your own ISBN (Bangladesh: National ISBN Agency, Archives & Libraries
  Directorate), put it in `isbn` in `languages/vai.py` and rebuild.

## 3. AI-generated content disclosure

Images: **AI-generated** (line art made with AI assistance, reviewed by the author).
Text: **AI-generated**, with substantial human editing.

## 4. Pricing (verify in KDP's calculator)

Printing ≈ **US $2.73** ($1.00 + 144 × $0.012). At **$8.99** royalty ≈ **$2.67**; at **$9.99** ≈ **$3.27**.

## 5. Must-do before publishing

1. A ḥāfiẓ or scholar checks the Qur’an text on pages 4–5.
2. **A native Vai speaker proofreads every letter name, sound guide, word, transliteration and phrase.**
   This is the thinnest draft in the series. (1) We found no reliable Vai example word for 55 of the 56 syllables, so those pages show the syllable on a slate with a note; a Vai speaker should supply one picturable word per syllable (object, plant or nature) and replace the slate. (2) The everyday phrases (my name is, thank you, mother/father, brother/sister, yes/no, I am learning Vai) are left as write-in lines, and the number words are left out; please supply them. (3) Check the Vai spellings of the Arabic phrases (Assalamu alaikum, Wa alaikum assalam, Jazakallahu khairan, Mashallah), the choice of core rows (b t k l m s n) and the column order ɛ i a ɔ u o e. (4) Noto Sans Vai has only one (regular) weight, so the big coloring signs are thinner than in other books.
3. Order a printed proof copy.
