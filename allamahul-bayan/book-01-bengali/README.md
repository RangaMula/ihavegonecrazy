# Allamahul Bayan Series — Book 1: My First Bengali Alphabet

A 120-page, Amazon-KDP-ready coloring book that teaches young children the 50 letters of the Bengali
alphabet **through English**.

- **Author:** Hafez Abdullah Muhammad Minhaz Reza
- **Illustrations:** AI-assisted, reviewed by the author
- **Publisher:** Maktabatu Kunujul Akhirah (an imprint of the Kunujul Akhirah Charitable Trust)

**Ready to upload:** `output/interior.pdf` + `output/cover.pdf`. The upload steps, metadata, keywords,
pricing and pre-publication checks are in [KDP-PUBLISHING-GUIDE.md](KDP-PUBLISHING-GUIDE.md).

## What is inside (page map)

| Pages | Content |
|---|---|
| 1–3 | Title · copyright · "This book belongs to" |
| 4–5 | **About the Allamahul Bayan Series**: Surah Ar-Raḥmān 55:1–4 (*ʿallamahul-bayān*), 30:22 (languages and colours), 49:13 |
| 6 | How to use this book (parents & teachers), how to read the sound guides |
| 7 | Hello, Bengali! Who speaks it, where, the script, 50 letters, 21 February |
| 8 | The whole alphabet on one page |
| 9 | Map to color: where Bengali is spoken (Bangladesh, West Bengal, Tripura, Assam) |
| 11–12 | Vowels intro with vowel-sign table · pencil warm-up |
| 13–34 | 11 vowel pages (coloring page + blank back) |
| 35–36 | Consonants intro (the hidden vowel, families of five, the puff test) · pencil warm-up |
| 37–114 | 39 consonant pages (coloring page + blank back) |
| 115 | Bengali numbers ০–৯ to color |
| 117–118 | First Bengali phrases · references & sources |
| 119–120 | Certificate (cut out) · blank back |

Each letter page shows the letter in **three phonetic forms**: its Bengali name in Bengali script (native),
the same name in English letters, and an English sound guide. It also shows how the sound is built the
Bengali way (ক্ + অ = ক, or the vowel sign ক + া = কা). Below that are a word with a picture to color
(Bengali, transliteration and meaning) and a pencil tracing row.

## House rules followed (Maktabatu Kunujul Akhirah)

Taken from the master brief of *Introduction to the Arabic Language for Kids*:
- No people or animals: every picture is an object, a plant or a part of nature.
- Every word is given three ways: native script, italic transliteration (doubled vowels = long) and English meaning.
- Every Qur'an quote has its surah:verse and a superscript that points to the References page.
- **All religious text must be reviewed by a qualified scholar before publication.**
- The certificate is on a right-hand (odd) page with a blank back, so it can be cut out.

## Rebuilding

Built as code, so a change to the text is a one-line edit plus a rebuild:

```bash
npm install                       # map data (world-atlas, d3-geo, topojson-client)
pip install fonttools brotli skia-pathops pypdf
node tools/make_map.mjs           # map outlines -> build/map_paths.json
python3 tools/build_book.py       # -> build/interior.html (checks page parity + count)
node tools/render.mjs interior    # -> output/interior.pdf (needs Playwright + Chromium)
python3 tools/build_cover.py && node tools/render.mjs cover && python3 tools/build_cover.py --crop
```

| File | Role |
|---|---|
| `tools/content.py` | All words, phonetics, phrases, Qur'an quotes and book identity (ISBN goes here) |
| `tools/illos.py` | 50 hand-built SVG line drawings (white in the book, coloured on the cover) |
| `tools/glyphs.py` | Bengali letters → vector outlines (Baloo Da 2 ExtraBold) for coloring and dotted tracing |
| `tools/brand.py` | Maktabatu Kunujul Akhirah mark (from the official vector logo) |
| `tools/build_book.py` | Interior generator (8.5 × 11 in, no bleed, B&W) |
| `tools/build_cover.py` | Full-wrap cover (spine = pages × 0.002252 in) |
| `assets/fonts/` | Baloo Da 2, Noto Sans Bengali, Fredoka, Nunito, Amiri, Dancing Script (all SIL OFL) |

To start Book 2 in another language, copy this folder and replace `content.py` (the letters and words) and
the pictures in `illos.py`; keep the layout and build scripts as they are.
