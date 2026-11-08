# How to translate these tales

Every tale exists in three forms that hold the same text:

| Form | Where | Best for |
|---|---|---|
| Markdown | `<Continent>/<Tradition>/NNN - Title.md` | Reading |
| Segmented JSON | `translation-kit/source/<Continent>/<tradition-id>/<tale-id>.json` | AI translation (Claude etc.), scripts, spreadsheets |
| XLIFF 1.2 | `translation-kit/xliff/<Continent>/<tradition-id>.xlf` | Professional CAT tools: OmegaT (free), memoQ, Trados, Weblate, Crowdin, Matecat |

`translation-kit/catalog.json` lists every tale with its id, title, source language, word and segment counts,
licence status and file paths. Use it to plan a translation, e.g. by word count per tradition.

## Segment IDs

Each tale is split into **paragraphs** (`p001`, `p002`, …) and each paragraph into **segments**,
normally one sentence (`p001.s01`, `p001.s02`, …). Verse is split one line per segment. IDs stay the
same across rebuilds as long as the source text doesn't change, so translation memories keep working.

```json
{ "id": "as-bengal-bengali-people-001",
  "title": {"id": "title", "source": "Life’s Secret", "target": "জীবনের রহস্য"},
  "source_lang": "en",
  "paragraphs": [
    {"id": "p001", "type": "prose", "segments": [
      {"id": "p001.s01", "source": "There was a king who had two queens, Duo and Suo.", "target": "এক রাজার দুই রানি ছিল, দুও আর সুও।"}
    ]}
  ]}
```

Paragraph `type` is one of `prose`, `quote`, `verse`, `verse-quote`, `heading` or `break`. It is used to rebuild the
layout after translation.

## Workflow

1. Pick tales from `catalog.json` (or a whole tradition's XLIFF file).
2. Translate:
   - **JSON:** add a `"target"` next to every `"source"` (including the title) and save the file (a copy is fine).
   - **XLIFF:** open the `.xlf` in your CAT tool, translate, export the translated `.xlf`.
3. Rebuild readable stories:
   ```bash
   python3 _tools/apply_translation.py bn path/to/translated.json
   python3 _tools/apply_translation.py fr translation-kit/xliff/Africa/hausa-people-nigeria-niger.xlf
   ```
   The output goes to `translations/<lang>/<Continent>/<Tradition>/NNN - <translated title>.md`. Segments left
   untranslated keep the original text and are counted in the file header.
4. Keep names consistent with `translation-kit/glossary/<tradition-id>.csv`. It lists automatically found proper
   names (with counts and tale numbers). Fill in `keep_or_transliterate` and `target_form` once per language and
   reuse them across all tales of that tradition.

## Rules for translators (human or AI)

- Translate meaning faithfully; keep the oral-storytelling tone (repetition, refrains, songs).
- Keep segment IDs unchanged; never merge or split segments in the JSON/XLIFF.
- Transliterate personal and place names (see the glossary). Do not replace them with local equivalents.
- Keep songs and refrains as verse. Words left in the original language (e.g. Kimbundu, Hausa) may be kept and
  explained once.
- Modernise outdated or offensive ethnic terms (the README lists examples), and add a short note when you do.
- **Credit requirements:**
  - Public-domain tales: no credit is legally required, but cite the source book (good practice).
  - **CC BY 4.0 tales** (African Storybook): you must credit the original author(s), illustrator(s) and African
    Storybook, and link to https://creativecommons.org/licenses/by/4.0/. `apply_translation.py` copies the
    source licence into every output file for you.

## Example prompt for AI translation (one tale per request)

> Translate the following JSON tale into Bengali (bn). For every object that has a "source" field, add a
> "target" field with the translation, including the title. Keep all ids, types and the structure unchanged.
> Keep personal names transliterated. Keep refrains and songs poetic. Return only the JSON.
