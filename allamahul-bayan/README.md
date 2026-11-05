# Allamahul Bayan Series — alphabet coloring books for the languages of the world

Published by **Maktabatu Kunujul Akhirah** (an imprint of the Kunujul Akhirah Charitable Trust) ·
written by **Hafez Abdullah Muhammad Minhaz Reza** · illustrations AI-assisted.

The series is named after Surah Ar-Raḥmān 55:4, *ʿallamahul-bayān*: “He taught him clear expression.”
Every book teaches one language's alphabet **through English**: each letter is shown in its own script, with an
English transliteration and sound guide, a picture word to color, and tracing rows. Every book is KDP-ready:
an 8.5 × 11 in black-and-white interior with no bleed, a full-colour wrap cover with the spine sized to the page
count, and a `KDP-PUBLISHING-GUIDE.md`.

**→ The list of all 88 books, with page counts and review status, is in [SERIES-STATUS.md](SERIES-STATUS.md).**

| Range | Region |
|---|---|
| 1–26 | South Asia: Bengali, Hindi, Urdu, Punjabi, Gujarati, Marathi, Tamil, Telugu, Kannada, Malayalam, Odia, Assamese, Nepali, Sinhala, Sindhi, Pashto, Dhivehi, Kashmiri, Balochi, Santali, Manipuri, Konkani, Maithili, Dogri, Bodo, Dzongkha |
| 27–33 | Arabic script and the Middle East: Arabic, Persian, Uyghur, Kurdish (Sorani), Malay (Jawi), Hebrew, Assyrian (Syriac) |
| 34–44 | Greek, Armenian, Georgian and the Cyrillic alphabets: Russian, Ukrainian, Bulgarian, Serbian, Kazakh, Tatar, Tajik, Mongolian |
| 45–53 | East and Southeast Asia: Korean, Japanese, Thai, Lao, Khmer, Burmese, Javanese, Sundanese, Balinese |
| 54–55 | North American syllabaries: Cherokee, Inuktitut |
| 56–61 | African scripts: Amharic, Tigrinya, Tamazight (Tifinagh), Bambara (N'Ko), Fula (Adlam), Vai |
| 62–79 | African Latin-script languages: Swahili, Hausa, Yoruba, Igbo, Somali, Oromo, Zulu, Xhosa, Shona, Kinyarwanda, Lingala, Wolof, Malagasy, Twi, Afrikaans, Sesotho, Setswana, Luganda |
| 80–88 | Latin America and the Caribbean: Spanish, Portuguese, Quechua, Guaraní, Aymara, Nahuatl, K'iche', Haitian Creole, Mapudungun |

Chinese is not included because it has no alphabet.

## Before publishing any book

1. **Native-speaker proofread.** Books 1–13 were written first and checked by eye. Books 14–88 were drafted by
   parallel AI agents, often without access to dictionaries, and print a **REVIEW DRAFT** notice on the title and copyright
   pages. Each book's `review_note`, which is repeated in its KDP guide, lists exactly what to check.
2. **Qur'an check.** A ḥāfiẓ or scholar must review pages 4–5, which are the same in every book.
3. After review, set `draft=False` in `languages/<code>.py`, run `python3 build.py <code>`, and order a printed proof.

## House rules (Maktabatu Kunujul Akhirah)

- Pictures show objects, plants and nature only: no people, no animals, no faces, and no religious symbols of other faiths.
- Every word appears three ways: native script, transliteration and English meaning.
- Every Qur'an quote has its surah:verse and a superscript that points to the References page.
- Each coloring page is on the right with a blank back. The certificate is on an odd page with a blank back.
- Maps show coastlines only, with no political borders and no disputed names. Bengali is the exception: it uses the Bangladesh–India borders.
- Facts are neutral and child-friendly. The phrases page always includes the Muslim greeting pair and *Jazakallahu khairan*.

## How it is built

```
allamahul-bayan/
  build.py          python3 build.py <code> [<code> …]   or   python3 build.py all
  status.py         python3 status.py  -> SERIES-STATUS.md
  AGENT_BRIEF.md    the instructions every book agent followed
  engine/           book.py (interior), cover.py, guide.py, glyphs.py (HarfBuzz letter outlines),
                    indic.py (Brahmic scripts), generic.py (all other alphabets), maps.py, illos.py (picture library),
                    pics/ (picture plug-ins added per language), brand.py, series.py, render.mjs, make_map.mjs
  languages/        one data file per book (<code>.py) + shared helpers (_*.py)
  fonts/            SIL Open Font License fonts for every script
  book-NN-<name>/   output/interior.pdf, output/cover.pdf, KDP-PUBLISHING-GUIDE.md
```

Setup, run once:

```bash
cd allamahul-bayan/engine && npm install
```

```bash
pip install fonttools brotli skia-pathops uharfbuzz pypdf
```

To rebuild every book (needs Playwright with Chromium):

```bash
cd allamahul-bayan && python3 build.py all && python3 status.py
```

To fix a word, edit `languages/<code>.py` and rebuild that book. To add a language, copy the closest existing file.
