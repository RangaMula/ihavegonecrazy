# Allamahul Bayan Series — alphabet coloring books for the languages of South Asia

Published by **Maktabatu Kunujul Akhirah** (an imprint of the Kunujul Akhirah Charitable Trust) ·
written by **Hafez Abdullah Muhammad Minhaz Reza** · illustrations AI-assisted.

The series is named after Surah Ar-Raḥmān 55:4, *ʿallamahul-bayān*: “He taught him clear expression.”
Every book teaches one language's alphabet **through English**, with its own coloring line art.

Each book is KDP-ready: an 8.5 × 11 in black-and-white interior with no bleed, a full-colour wrap cover
with the spine sized to the page count, and a `KDP-PUBLISHING-GUIDE.md` with the description,
keywords, categories, price and AI disclosure.

## Status

| # | Book | Script | Letters | Pages | Folder |
|---|---|---|---|---|---|
| 1 | Bengali | Bengali | 50 | 120 | `book-01-bengali/` |
| 2 | Hindi | Devanagari | 51 | 122 | `book-02-hindi/` |
| 3 | Urdu | Perso-Arabic (Nastaliq), right-to-left | 38 | 94 | `book-03-urdu/` |
| 4 | Punjabi | Gurmukhi | 48 | 116 | `book-04-punjabi/` |
| 5 | Gujarati | Gujarati | 49 | 118 | `book-05-gujarati/` |
| 6 | Marathi | Devanagari | 49 | 118 | `book-06-marathi/` |
| 7 | Tamil | Tamil | 36 | 92 | `book-07-tamil/` |
| 8 | Telugu | Telugu | 50 | 120 | `book-08-telugu/` |
| 9 | Kannada | Kannada | 49 | 118 | `book-09-kannada/` |
| 10 | Malayalam | Malayalam | 51 | 122 | `book-10-malayalam/` |
| 11 | Odia | Odia | 49 | 116 | `book-11-odia/` |
| 12 | Assamese | Assamese (Bengali-Assamese) | 50 | 120 | `book-12-assamese/` |
| 13 | Nepali | Devanagari | 49 | 118 | `book-13-nepali/` |
| 14 | Sinhala | Sinhala | — | — | *not started: needs a native-speaker word list* |
| 15 | Sindhi | Perso-Arabic | — | — | *not started* |
| 16 | Pashto | Perso-Arabic | — | — | *not started* |
| 17 | Dhivehi | Thaana, right-to-left | — | — | *not started* |

Later candidates: Kashmiri, Konkani, Maithili, Santali (Ol Chiki), Manipuri (Meitei Mayek), Dogri, Bodo, Balochi.

**None of these books is ready to publish without two human checks.** First, a ḥāfiẓ or scholar must review
the Qur'an pages (pp. 4–5, the same in every book). Second, a native speaker must proofread each book's letter
names, sound guides, words and transliterations. Each book's KDP guide lists the points to check
first. Odia and Assamese were drafted from less source material than the others and need the most careful review.

## House rules (Maktabatu Kunujul Akhirah)

- Pictures show objects, plants and nature only: no people, no animals, no faces.
- Every word appears three ways: native script, transliteration (doubled vowels are long) and English meaning.
- Every Qur'an quote carries its surah:verse and a superscript that resolves on the References page.
- Each coloring page is on the right with a blank back. The certificate is on an odd page with a blank back.
- Maps show coastlines only, with no political borders, plus a dashed area around the region where the
  language is spoken. Bengali is the exception: it uses the Bangladesh–India borders.

## How it is built

```
allamahul-bayan/
  build.py            python3 build.py hi ur …   or   python3 build.py all
  engine/             shared generator: book.py (interior), cover.py, guide.py, indic.py (Indic-script helper),
                      glyphs.py (HarfBuzz-shaped letter outlines), illos.py (≈110 object drawings), brand.py,
                      series.py (series facts + Qur'an quotes), render.mjs, make_map.mjs
  languages/          one data file per book: bn hi ur pa gu mr ta te kn ml or as ne (+ _southasia.py map helper)
  fonts/              all SIL Open Font License (Baloo family per script, Noto Sans per script, Fredoka, Nunito, Amiri …)
  book-NN-<name>/     output/interior.pdf, output/cover.pdf, KDP-PUBLISHING-GUIDE.md
```

Setup, run once:

```bash
cd allamahul-bayan/engine && npm install
```

```bash
pip install fonttools brotli skia-pathops uharfbuzz pypdf
```

Rebuild everything (needs Playwright with Chromium):

```bash
cd allamahul-bayan && python3 build.py all
```

To fix a word, edit `languages/<code>.py` and rebuild that book. To add a language, copy the closest file:
`hi.py` or `pa.py` for an Indic script, `ur.py` for a Perso-Arabic one. Any picture key the library lacks
is added in `engine/illos.py`.
