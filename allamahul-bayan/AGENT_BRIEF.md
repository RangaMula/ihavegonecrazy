# Brief for parallel book agents — Allamahul Bayan Series

You are one of ~27 agents working **at the same time in the same checkout**
(`/home/user/ihavegonecrazy/allamahul-bayan`). Each agent writes one or more children's alphabet coloring books.
Each book is a single data file that the shared engine turns into KDP-ready PDFs.

## 1. Read these first (5 minutes)
- `README.md`: the series, house rules and layout.
- One complete example close to your script:
  - **Latin-script** languages: `languages/es.py` (generic builder, "Aa" capital+small letter pages)
  - **Indic / Brahmic** scripts: `languages/pa.py` or `languages/hi.py` (indic builder, vowels + consonants)
  - **Arabic-script**, right-to-left: `languages/ur.py` (joined forms, `dir="rtl"`)
- `engine/generic.py`, `engine/indic.py`, `engine/maps.py` (`region_map`), `engine/pics/README.md`.

For any other script (Greek, Cyrillic, Ethiopic, Hangul, kana, Thai, syllabaries…) use `engine/generic.py`: build the
`sections` yourself (one section, or several, e.g. vowels/consonants, or one per syllable row) with `letter()` items.
`letter` is the text drawn big (it may be several characters, e.g. "Aa", "ሀ", "あ"). `phon` is native-phonetics HTML,
for example the letter's name in its own script, its joined forms, or its row in the syllable grid.

## 2. House rules (non-negotiable)
1. **Pictures: objects, plants and nature only.** No people, no animals, no faces, no religious symbols of other faiths.
   Pick words whose picture already exists (`python3 -c "import sys;sys.path.insert(0,'engine');from illos import PICS;print(sorted(PICS))"`)
   or draw new ones in **your own file** `engine/pics/<code>.py`, with keys prefixed `<code>_`. Follow
   `engine/pics/README.md` and draw clean, child-friendly line art in a 200×200 viewBox, every closed shape with class a–e.
2. Every item appears three ways: **native script + simple English transliteration** (doubled vowels = long; CAPS may mark
   stress) **+ English meaning**.
3. Keep `draft=True` in every language file you create (this prints the "REVIEW DRAFT" notice). Put honest notes
   about your uncertainties in `review_note`.
4. **Neutral, child-friendly facts** only: no politics, no disputed borders or claims. Maps are coastline-only
   (`region_map`, `land=True`), with city dots and an optional dashed area. Speaker numbers: round, cite Ethnologue in
   `facts_source`.
5. The phrases page keeps the Muslim greeting pair (Assalamu alaikum / Wa alaikum assalam) and "Jazakallahu khairan",
   written in the language's script, plus everyday phrases (my name is, thank you, mother/father, brother/sister,
   yes/no, "I am learning X!"). Include `cheer` = "Mashallah! Well done!" in the language.
6. Rare letters that never start a word: use a word where the letter sits inside, and add a `note`.
7. Pages 4–5 (the Qur'an pages) are shared engine text. Do **not** change them.

## 3. Fonts
Every agent uses **its own** npm folder, so parallel installs don't collide:
```bash
mkdir -p /tmp/claude-0/-home-user-ihavegonecrazy/779101f5-42f5-5386-9cd0-63b280f33047/scratchpad/agent-<code>/npm
cd that folder && npm init -y >/dev/null && npm install @fontsource/noto-sans-<script>   # e.g. noto-sans-ethiopic, noto-sans-georgian
```
Copy the needed `*-<subset>-{400,700,800}-normal.woff2` files into `allamahul-bayan/fonts/` (never overwrite or delete
existing files). Use `fontset(display_family, display_prefix, text_family, text_prefix)` from `indic.py` / `generic.py`.
- `glyph_font` (the big coloring letters) may be **one file or a list of files**: the engine picks the first file that
  contains every character. Prefer a bold, round font (Baloo family where one exists for your script; otherwise Noto
  Sans 700/800, or the boldest weight available).
- **Check coverage before writing pages**: every letter, digit and word character must exist in your fonts
  (`fontTools.ttLib.TTFont(f).getBestCmap()`).
- If no fontsource package exists for a script, try `@fontsource/noto-sans-<name>`, `@fontsource/noto-serif-<name>`,
  or another OFL font on npm. Only use OFL/Apache-licensed fonts, and name them in `font_credit`.

## 4. Build and check — one book at a time
```bash
cd /home/user/ihavegonecrazy/allamahul-bayan && python3 build.py <code>
```
This writes `book-NN-<name>/output/interior.pdf`, `cover.pdf` and `KDP-PUBLISHING-GUIDE.md` and asserts sizes and parity.
**Never run `build.py all`.** Only render one book at a time; 27 agents share this machine's memory.

Then **look at it**. Rasterize a few pages at low resolution into your own scratch folder, for example
`pdftoppm -f 13 -l 13 -r 40 -png …/interior.pdf <scratch>/agent-<code>/p13`, and view them with the Read tool:
title page, a letter page, a section intro, the map and the cover. Fix clipping, missing glyphs (tofu boxes) and
overlaps in **your language file** (`extra_css` is allowed).

## 5. Shared files — do not edit
Do **not** modify `engine/*.py` (except creating your own `engine/pics/<code>.py`), other agents' language files,
`README.md` or `build.py`. Do **not** run any git command that writes (no add/commit/push/checkout/stash). The lead
agent commits everything. If you find an engine bug you cannot work around in your language file, describe it in your
final report.

## 6. Book numbers (fixed; do not change)
| no | code | language | script |  | no | code | language | script |
|---|---|---|---|---|---|---|---|---|
| 14 | si | Sinhala | Sinhala | | 52 | su | Sundanese | Sundanese |
| 15 | sd | Sindhi | Arabic (RTL) | | 53 | ban | Balinese | Balinese |
| 16 | ps | Pashto | Arabic (RTL) | | 54 | chr | Cherokee | Cherokee syllabary |
| 17 | dv | Dhivehi | Thaana (RTL) | | 55 | iu | Inuktitut | Canadian syllabics |
| 18 | ks | Kashmiri | Arabic (RTL) | | 56 | am | Amharic | Ethiopic |
| 19 | bal | Balochi | Arabic (RTL) | | 57 | ti | Tigrinya | Ethiopic |
| 20 | sat | Santali | Ol Chiki | | 58 | zgh | Tamazight | Tifinagh |
| 21 | mni | Manipuri | Meitei Mayek | | 59 | nqo | Manding (Bambara) | N'Ko (RTL) |
| 22 | kok | Konkani | Devanagari | | 60 | ff | Fula | Adlam (RTL) |
| 23 | mai | Maithili | Devanagari | | 61 | vai | Vai | Vai syllabary |
| 24 | doi | Dogri | Devanagari | | 62 | sw | Swahili | Latin |
| 25 | brx | Bodo | Devanagari | | 63 | ha | Hausa | Latin (ɓ ɗ ƙ ƴ) |
| 26 | dz | Dzongkha | Tibetan | | 64 | yo | Yoruba | Latin (ẹ ọ ṣ) |
| 27 | ar | Arabic | Arabic (RTL) | | 65 | ig | Igbo | Latin |
| 28 | fa | Persian | Arabic (RTL) | | 66 | so | Somali | Latin |
| 29 | ug | Uyghur | Arabic (RTL) | | 67 | om | Oromo | Latin |
| 30 | ckb | Kurdish (Sorani) | Arabic (RTL) | | 68 | zu | Zulu | Latin |
| 31 | ms | Malay | Jawi (RTL) | | 69 | xh | Xhosa | Latin |
| 32 | he | Hebrew | Hebrew (RTL) | | 70 | sn | Shona | Latin |
| 33 | syr | Assyrian Neo-Aramaic | Syriac (RTL) | | 71 | rw | Kinyarwanda | Latin |
| 34 | el | Greek | Greek | | 72 | ln | Lingala | Latin |
| 35 | hy | Armenian | Armenian | | 73 | wo | Wolof | Latin |
| 36 | ka | Georgian | Georgian | | 74 | mg | Malagasy | Latin |
| 37 | ru | Russian | Cyrillic | | 75 | tw | Twi (Akan) | Latin |
| 38 | uk | Ukrainian | Cyrillic | | 76 | af | Afrikaans | Latin |
| 39 | bg | Bulgarian | Cyrillic | | 77 | st | Sesotho | Latin |
| 40 | sr | Serbian | Cyrillic | | 78 | tn | Setswana | Latin |
| 41 | kk | Kazakh | Cyrillic | | 79 | lg | Luganda | Latin |
| 42 | tt | Tatar | Cyrillic | | 80 | es | Spanish | Latin (done: example) |
| 43 | tg | Tajik | Cyrillic | | 81 | pt | Portuguese | Latin |
| 44 | mn | Mongolian | Cyrillic | | 82 | qu | Quechua | Latin |
| 45 | ko | Korean | Hangul | | 83 | gn | Guaraní | Latin |
| 46 | ja | Japanese | Hiragana | | 84 | ay | Aymara | Latin |
| 47 | th | Thai | Thai | | 85 | nah | Nahuatl | Latin |
| 48 | lo | Lao | Lao | | 86 | quc | K'iche' | Latin |
| 49 | km | Khmer | Khmer | | 87 | ht | Haitian Creole | Latin |
| 50 | my | Burmese | Myanmar | | 88 | arn | Mapudungun | Latin |
| 51 | jv | Javanese | Javanese (Hanacaraka) | | | | | |

Folder name: `book-NN-<english-name-lowercase-with-hyphens>` (e.g. `book-56-amharic`). The Python file is
`languages/<code>.py`. If the code is a Python keyword, that is fine: the builder imports by string.

## 7. Final report (your last message)
For each book, give: code · pages · number of letters · the folder path. Then list fonts added, new picture keys,
and **the specific things a native speaker must check** (uncertain words, names, transliterations). Keep it short.
