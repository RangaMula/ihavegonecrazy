# Pronunciation schemes

The pronunciation line is **generated** from the fully vowelled Arabic by `engine/phon.py` (Arabic → phonemes) and
`engine/scripts.py` (phonemes → script). Fix errors there, never by hand in a book.

## Reading rules (all scripts)

| Rule | Example |
|---|---|
| Sun letters assimilate the article; moon letters keep l; hyphen after the article | الشَّمْس *ash-shams*, الْقَمَر *al-qamar* |
| Allah never takes a hyphen | بِسْمِ اللَّهِ *bismillāh*, رَسُولُ اللَّهِ *rasūlullāh* |
| Hamzat al-waṣl drops after a vowel, gets a helping *i* after a consonant, is said *a/i/u* after a pause | فِي الْبَيْتِ *fil-bayt*; عَنِ ابْنِ *ʿanibni* |
| Pause (waqf) before . ، ؛ : ؟ ! » and at the end: no final short vowel; *-an* → *ā*; ة → *h*; *-iyy* → *ī* | مَالِكٍ، → *mālik*; الأَنْصَارِيُّ → *al-anṣārī* |
| Unwritten long ā restored | هَذَا *hādhā*, ذَلِكَ *dhālika*, لَكِنْ *lākin* |
| The unvowelled ﷺ formula in the source is read in full | صلى الله عليه وسلم → *ṣallallāhu ʿalayhi wa sallam* |
| Words with no vowel marks in the source are shown in Arabic and flagged | 28 words in 16 entries |

## Schemes

| Code | Script | Consonants that need a sign | Long vowels | ʿayn / hamza | Used by |
|---|---|---|---|---|---|
| `latn` | Latin, simplified ALA-LC | th ḥ kh dh sh ṣ ḍ ṭ ẓ gh q | ā ī ū | ʿ ʾ | the base for all 92 Latin-script languages |
| `bn` | Bengali, `books/ar/STYLE.md` §3 | থ় হ় খ় দ় জ় স় ড ট য গ় ফ় ক় | াː ীː ূː | ʿ ʾ | Bengali (and the model for Assamese) |
| `hi` | Devanagari, Hindi-Urdu conventions | क़ ख़ ग़ ज़ फ़ (ث س ص = स; ذ ز ض ظ = ज़; ط ت = त; ح ه = ह) | ा ी ू | ʿ ʾ; halant ् marks a vowelless consonant | Hindi; base for Marathi, Nepali, Sanskrit, Maithili, Konkani |
| `ja` | Katakana, Japanese Islamic-literature conventions | not distinguished (ḥ/h/kh → ハ行, s/ṣ/th → サ行, z/dh/ẓ → ザ行, r/l → ラ行) | ー | not written | Japanese |
| `ar-vowelled` | none: the vowelled Arabic is the guide | | | | Urdu, Persian, Pashto, Sindhi, Kashmiri, Uyghur, Punjabi (Shahmukhi) |

**Japanese:** katakana cannot show ḥ/ʿ/emphatics or r versus l. The book's introduction says so and tells the reader that
the Arabic line is authoritative. Gemination is written ッ (ン before m/n): アッラー, ムハンマド, アッサラーム.

## Adding a script

1. Write `<code>_word(tokens)` in `engine/scripts.py`, using `units()` to get consonant+vowel units, and register it in
   `SCHEMES`.
2. Use the language's own Muslim conventions where they exist (how Muslim publishers in that language write
   *bismillāh*, *rasūlullāh*, *ṣallallāhu ʿalayhi wa sallam*).
3. Run `python3 tools/check_pron.py <code>` over all 1,860 entries: no exceptions, and a sample read by a native reader.
4. Set `pron_status` to `ready` in `tools/build_registry.py`.

Still to write: Cyrillic (10 languages), the other Indic scripts (Assamese, Odia, Gurmukhi, Gujarati, Tamil, Telugu,
Kannada, Malayalam, Sinhala), Thai, Lao, Khmer, Myanmar, Hangul, Han (Pinyin/Jyutping readings), Greek, Armenian,
Georgian, Hebrew, Ethiopic, Tibetan, Thaana, Ol Chiki, Meetei Mayek, Tifinagh.
