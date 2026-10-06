# আরবি ভাষার দরজা — Arabic book: language style guide and data format

Every writer (human or agent) of Arabic-book content follows this file. The series rules are in
`series-standard/BOOK-STRUCTURE.md` and `series-standard/PLAYBOOK.md`; this file makes them concrete for Arabic.

## 1. Reader and register

- Adult Bangla speakers (mostly Bangladesh): Qur'an readers who want to *understand*, Gulf workers, students
  (Madinah, al-Azhar, Qatar), Hajj and Umrah pilgrims, professionals and curious readers.
- Instruction language: standard চলিত Bangla, Bangladesh usage and Bangla Academy spelling (পানি, গোসল, নামাজ…).
  Address the reader as **আপনি**. Warm, respectful, never childish.
- **Arabic taught: Modern Standard Arabic (الفصحى)**, the language of news, books, signs and formal speech,
  which is also the closest living form to the Qur'an's Arabic.
  - Where everyday **spoken Gulf Arabic** (Saudi Arabia, UAE, Qatar, Kuwait, Oman: where most Bangladeshi workers live) differs strongly
    for a common item, add it in `note_bn` as «উপসাগরীয় কথ্য: …» (Arabic script + Bangla pronunciation).
    Example: كَيْفَ حَالُكَ؟ → note «উপসাগরীয় কথ্য: شْلُونَك؟ (শলূːনাক)». Use this for perhaps 1 item in 10, only where it really helps.
  - Egyptian or Levantine forms only in a culture story, if at all.
- **No pork or alcohol items** in vocabulary, dialogues or examples. Food culture is shown through halal Arab dishes
  (كَبْسَة، مَنْدِي، حُمُّص، فَلَافِل، شَاوَرْمَا، مَنْسَف، كُسْكُس، كُنَافَة، تَمْر، قَهْوَة عَرَبِيَّة، شَاي بِالنَّعْنَاع…).
- Islam is the native ground of this language. Religious words are welcome where natural, but this is a **language book**:
  the journey must also cover shops, hospitals, offices, travel, nature, science, feelings and so on, like any language.
  Respect every reader; never mock or criticise any faith, sect or country.

## 2. The Triple Row (every Arabic item)

Every Arabic word, phrase or sentence is stored as an object with five fields. **The key is `fr`** (series-wide name for
"target-language text"; the engine reads `fr`; do not rename it).

```json
{"fr": "كِتَاب", "bn_pron": "কিতাːব", "en_pron": "kitāb", "bn": "বই", "en": "book", "note_bn": "পুং · বহুবচন: كُتُب (কুতুব)"}
```

| Field | Content |
|---|---|
| `fr` | Arabic script, **fully vowelled (every letter carries its haraka, shadda, sukun or tanwin)**. See §5 for the form of each word type. |
| `bn_pron` | Bangla-script pronunciation, following §3 exactly |
| `en_pron` | Simplified ALA-LC romanization, following §4 |
| `bn` | Bangla meaning (short) |
| `en` | English meaning (short) |
| `note_bn` | Optional, but **required for nouns and verbs** (see §5). One short Bangla line |

## 3. Bangla pronunciation rules (series notation applied to Arabic)

**Nukta (়)** marks a consonant Bangla does not have. **ː** marks a long vowel. Two raised signs mark the throat stops:
**ʿ** for ع and **ʾ** for a hamza in the middle or at the end of a word (they are also used in the English column, so the reader learns them once).

### 3.1 Consonants

| Letter | Sound | Bangla | Example (Arabic = Bangla = English) |
|---|---|---|---|
| ء | glottal stop | **ʾ** (not written at the start of a word) | سَأَلَ = সাʾআলা = saʾala |
| ب | b | ব | بَاب = বাːব = bāb |
| ت | t (dental, like Bangla ত) | ত | تَمْر = তামর = tamr |
| ث | th as in *think* | **থ়** | ثَلَاثَة = থ়ালাːথ়াহ = thalāthah |
| ج | j | জ | جَمِيل = জামীːল = jamīl |
| ح | strong breathy h from the middle of the throat | **হ়** | حَلِيب = হ়ালীːব = ḥalīb |
| خ | rough kh from the back (like Scottish *loch*) | **খ়** | خُبْز = খ়ুবজ় = khubz |
| د | d (dental, like Bangla দ) | দ | دَار = দাːর = dār |
| ذ | th as in *this* | **দ়** | ذَهَب = দ়াহাব = dhahab |
| ر | rolled / tapped r (like Bangla র) | র | رَجُل = রাজুল = rajul |
| ز | z | **জ়** | زَيْت = জ়াইত = zayt |
| س | s | স | سَمَك = সামাক = samak |
| ش | sh | শ | شَمْس = শামস = shams |
| ص | heavy s (tongue low, mouth full) | **স়** | صَبَاح = স়াবাːহ় = ṣabāḥ |
| ض | heavy d | **ড** | ضَيْف = ডাইফ় = ḍayf |
| ط | heavy t | **ট** | طَالِب = টাːলিব = ṭālib |
| ظ | heavy *th as in this* | **য** | ظُهْر = যুহর = ẓuhr |
| ع | throat squeeze (voiced, from the middle of the throat) | **ʿ** + vowel | عَيْن = ʿআইন = ʿayn |
| غ | gargled g/r from the back of the throat (like French r) | **গ়** | غَزَال = গ়াজ়াːল = ghazāl |
| ف | f | **ফ়** | فِيل = ফ়ীːল = fīl |
| ق | deep k from the back of the throat | **ক়** | قَلْب = ক়ালব = qalb |
| ك | k | ক | كَلْب = কালব = kalb |
| ل | l | ল | لَيْل = লাইল = layl |
| م | m | ম | مَاء = মাːʾ = māʾ |
| ن | n | ন | نُور = নূːর = nūr |
| ه | light h | হ | هُنَا = হুনাː = hunā |
| و | w | ও / ওয় | وَلَد = ওয়ালাদ = walad |
| ي | y | ইয় / য় | يَد = ইয়াদ = yad |

- The heavy letters (ص ض ط ظ, and also ق خ غ) make the next vowel sound deeper: **a** sounds nearer to "অ/আ" from the back of the mouth.
  This is explained once in Ch. 5. Do not invent extra marks for it.
- **ض = ড, ط = ট:** these Bangla "heavy" letters are the closest a Bangla speaker already has. Ch. 5 teaches the true Arabic sound.

### 3.2 Vowels

| Arabic | Sound | Bangla | English | Example |
|---|---|---|---|---|
| fatḥa ـَ | short a | া (initial আ) | a | قَلَم = ক়ালাম = qalam |
| kasra ـِ | short i | ি (initial ই) | i | مِن = মিন = min |
| ḍamma ـُ | short u | ু (initial উ) | u | قُلْ = ক়ুল = qul |
| ـَا / ـَى | long ā | **াː** (initial আː) | ā | بَاب = বাːব = bāb |
| ـِي | long ī | **ীː** (initial ঈː) | ī | فِيل = ফ়ীːল = fīl |
| ـُو | long ū | **ূː** (initial ঊː) | ū | نُور = নূːর = nūr |
| ـَيْ | ay | াই | ay | بَيْت = বাইত = bayt |
| ـَوْ | aw | াও | aw | يَوْم = ইয়াওম = yawm |

- **Short a is always া, never অ.** Bangla অ (ɔ) is a different sound.
- Sukun (no vowel) = no vowel sign in Bangla, and join the consonant to the next one: كَتَبْتُ = কাতাবতু.
- **Shadda (doubled letter)** = write the consonant twice using a Bangla conjunct: مُدَرِّس = মুদাররিস, أُمّ = উম্ম.

### 3.3 Joins and endings

- **The article ال:** write «আল-» with a hyphen. With the 14 sun letters (ت ث د ذ ر ز س ش ص ض ط ظ ل ن), the l is
  absorbed and the letter doubles: الشَّمْس = আশ-শামস = ash-shams, النُّور = আন-নূːর = an-nūr.
  After a vowel, the a of the article drops: فِي الْبَيْتِ = ফ়িল-বাইতি = fil-bayti.
- **Tā marbūṭa ة at a pause** = **াহ / ah**: مَدْرَسَة = মাদরাসাহ = madrasah. Inside a construct phrase it is **t**:
  مَدْرَسَةُ الْبَنَاتِ = মাদরাসাতুল-বানাːত.
- **Pause rule:** the **last word of a word list item or of a sentence is pronounced in pause form** (no final short vowel,
  no tanwin; -an tanwin after alif becomes ā): كِتَابٌ at a pause = কিতাːব. Inside a sentence, case endings are pronounced.
- Separate words with spaces exactly as in the Arabic. Use the Arabic question mark ؟ and comma ، in `fr`; Bangla
  punctuation in `bn_pron` and `bn`.

## 4. English column: simplified ALA-LC

| Letter | Roman | | Letter | Roman |
|---|---|---|---|---|
| ء | ʾ (not at the start) | | ض | ḍ |
| ث | th | | ط | ṭ |
| ح | ḥ | | ظ | ẓ |
| خ | kh | | ع | ʿ |
| ذ | dh | | غ | gh |
| ش | sh | | ق | q |
| ص | ṣ | | و / ي | w / y |

- Vowels a i u, long ā ī ū, diphthongs ay aw. Doubled letters written twice (mudarris).
- Article: al-kitāb; sun letters assimilated (ash-shams); elided after a vowel (fil-bayti).
- Tā marbūṭa at a pause = -ah; in construct = -at. Pause rule as in §3.3.
- **All lowercase** (no capitals; Arabic has none), except proper names written in English meaning columns.
- Use the real characters ʿ (U+02BF) and ʾ (U+02BE), never quote marks or apostrophes.

## 5. How each word type is given

| Type | `fr` form | `note_bn` must contain |
|---|---|---|
| Noun | Indefinite singular **without** the final case vowel or tanwin (كِتَاب, مَدْرَسَة). Plurals of people or things only where the item *is* a plural. | gender (পুং / স্ত্রী) and the **plural** (Arabic + Bangla pronunciation), e.g. «স্ত্রী · বহুবচন: مَدَارِس (মাদাːরিস)». Write «বহুবচন নেই» for mass nouns. |
| Adjective | Masculine singular, no case ending (كَبِير) | the feminine (كَبِيرَة) and, if useful, the plural |
| Verb | Past tense, he-form, with final fatha (كَتَبَ). `bn` gives the Bangla verb noun (লেখা), `en` "to write" | the present he-form + its pronunciation, e.g. «বর্তমান: يَكْتُبُ (ইয়াকতুবু)» |
| Phrase or sentence | Fully vowelled with case endings; last word paused in the pronunciation | optional |
| Proper name | Fully vowelled (القَاهِرَة, مَكَّة الْمُكَرَّمَة) | optional |

- Don't write the case ending on a word in a word list; do write case endings in sentences.
- Pronunciation columns always show **exactly what is said** (with the pause rule).

## 6. Culture content rules

- **Breadth (all 22 Arab League countries plus the wider Arabic world):** Saudi Arabia (Makkah, Madinah, Riyadh, AlUla/Hegra, the Empty Quarter),
  UAE, Qatar, Kuwait, Bahrain, Oman (Muscat, Nizwa, frankincense, dhows), Yemen (Sanaa, Shibam), Jordan (Petra, Wadi Rum, the Dead Sea),
  Palestine and al-Quds, Lebanon, Syria (Damascus, Aleppo), Iraq (Baghdad, Basra, the two rivers), Egypt (Cairo, al-Azhar, the Nile, the pyramids),
  Sudan (Meroë), Libya, Tunisia (Kairouan, Zaytuna), Algeria, Morocco (Fez and al-Qarawiyyin, Marrakesh, Chefchaouen), Mauritania (Chinguetti manuscripts),
  Somalia, Djibouti, the Comoros; plus al-Andalus (Córdoba, Granada), Zanzibar, and Arabic as the language of Islamic learning everywhere.
- **The golden age of Arabic science** is fair culture content: Bayt al-Ḥikma, al-Khwārizmī (algorithm, algebra), Ibn Sīnā, Ibn al-Haytham (optics),
  al-Idrīsī's map, Ibn Baṭṭūṭa (who visited Bengal: Chittagong and Sylhet, 1346), Fāṭima al-Fihriyya (al-Qarawiyyin).
- **Bangla links are gold.** Bangla holds over a thousand Arabic-origin words (কিতাব, কলম, দুনিয়া, খবর, হিসাব, আদালত…).
  Use `link_bn` to point them out, and show meaning shifts where they exist (غَرِيب "stranger" → গরিব "poor"; فَصْل "season" → ফসল "crop").
  **Do not reuse the Ch. 4 list in §8** in the journey.
- Every **জানেন কি?** (`story_bn`) line is one Bangla sentence of wonder that you are **certain** is true. If unsure, leave it out.
  Add `source_hint` (a short English pointer, e.g. "UNESCO World Heritage list") so the fact can be verified.
- Qur'an and hadith: only short, very well-known texts with exact references (sura:ayah; hadith collection + number).
  Never quote a hadith unless you are certain of its wording and its source; if unsure, leave it out.
- Show peoples as they see themselves; no stereotypes; no politics beyond neutral facts.
- `icon`: one emoji per culture word.

## 7. Data files (UTF-8 JSON in `books/ar/data/`)

The shapes are the same as the French book's files in `books/fr-2e/data/` (read them as the model), with these changes:

### `journey_1_10.json`, `journey_11_20.json`
Exactly as in the French `STYLE.md` §6 (`books/fr-2e/STYLE.md`), except that the milestone key `title_fr` holds the **Arabic** title.

### `part2.json` (Ch. 5–7 for Arabic)
- `ch5`: `intro_bn[]`; `bins` {`same`, `close`, `new`} each a list of {`sound`, `explain_bn`, `examples`[2–3 Triple Rows]};
  boxes as Bangla strings: `throat_bn` (ع ح خ غ ق ه), `heavy_bn` (ص ض ط ظ and the deep vowels), `th_bn` (ث ذ ظ),
  `length_bn` (short and long vowels change meaning), `shadda_bn` (doubled letters), `sun_moon_bn` (the article al-), `stress_bn`;
  `advantages_bn[]`, `mistakes_bn[]`, `minimal_pairs`[12 × {`a`, `b`, `note_bn`}] (e.g. قَلْب / كَلْب, سَيْف / صَيْف, عَالِم / عَلِمَ…).
- `ch6`: `intro_bn[]` (right-to-left, 28 letters, joined writing, letter shapes change by position, 6 letters never join to the left);
  `groups[]` by shape family, each {`title_bn`, `intro_bn`, `letters[]`}. Each letter:
  `{"letter": "ب", "name_fr": "بَاء", "name_bn_pron": "বাːʾ", "sound_bn": "ব", "forms": {"isolated": "ب", "initial": "بـ", "medial": "ـبـ", "final": "ـب"},
    "words": [5 Triple Rows, using the letter at the start, middle and end], "watch_bn": "optional warning"}`.
  All 28 letters plus hamza (ء) appear. Then `accents[]` = the **ḥarakāt**: fatḥa, kasra, ḍamma, sukūn, shadda, tanwīn (3), madda,
  dagger alif, each {`mark`, `name_fr` (Arabic name, vowelled), `use_bn`, `examples`[3–4 Triple Rows]}.
  Then `combinations[]` = special spellings: لا (lām-alif), ة, ى, hamza seats (أ إ ؤ ئ), ال with sun and moon letters, hamzat al-waṣl,
  each {`spelling`, `sound_bn`, `examples`[3–4 Triple Rows]}.
- `ch7`: `syllables[]` ({`fr`, `bn_pron`}, 30 items, e.g. بَ بِ بُ بَا بِي بُو), `words[]` (30 Triple Rows), `phrases[]` (12),
  `signs[]` (12 real Arab-world signs: مَخْرَج، مَدْخَل، مِصْعَد، دَوْرَة الْمِيَاه، مَسْجِد، صَيْدَلِيَّة… each with `where_bn`), `menu[]` (12), `form[]` (12 form fields: الِاسْم، الْجِنْسِيَّة، رَقْم الْجَوَاز…), `medicine[]` (10).
- `writing1[8]`, `checkpoint2` {`read_aloud`[10 Triple Rows], `quiz`[10 {q_bn, a}]} as in French.

### `part3.json` (Ch. 8–11 for Arabic)
- `ch8`: `intro_bn[]`, `numbers[]` (0–20, 30…100, 1000; each Triple Row + `n` + optional `note_bn`), box strings `digits_bn`
  (the Arabic-Indic digits ٠١٢٣٤٥٦٧٨٩, written left to right, and their shared Indian origin with Bangla digits) and `gender_bn`
  (numbers 3–10 take the opposite gender of the noun), `ordinals[]`, `uses[]` ({`title_bn`, `examples`[]}: prices, phone numbers, age, ages, floors).
- `ch9`: `days[]`, `months[]` (**the 12 Hijri months**; put the Gregorian names in `months_greg[]`), `seasons[]`, `parts_of_day[]`, `time_words[]`,
  `time_telling[]`, `date_examples[]`, `festivals[]` ({`name` Triple Row, `when_bn`, `story_bn`}: Ramadan, Eid al-Fitr, Eid al-Adha, Hajj days,
  Laylat al-Qadr, the Hijri new year, national days such as Saudi National Day, UAE National Day, Qatar National Day, Oman National Day, Kuwait, Morocco, Egypt…).
- `ch10`: as in French: `intro_bn[]`, `word_order_bn`, 12 `patterns` (the nominal sentence هٰذَا كِتَاب; the idāfa; adjective agreement;
  إِنَّ-free simple predicates; فِي/عَلَى/مِن place phrases; عِنْدِي = I have; هَل questions; question words; the past tense; the present tense; negation لَا / مَا / لَيْسَ / لَمْ;
  أُرِيدُ أَنْ… = I want to), each with `explain_bn`, `bangla_compare_bn`, `model`, `table` (substitution grid), `examples`; `previews[]`.
- `ch11`: `intro_bn[]`, `greetings[]`, `ant_anti_bn` (أَنْتَ / أَنْتِ / أَنْتُم: "you" changes with gender and number), `address[]` (يَا أَخِي، يَا أُخْتِي، يَا شَيْخ، أُسْتَاذ، حَضْرَتُك…),
  `customs[]` (hospitality, coffee and dates, the right hand, greeting between men and women, Friday, hospitality at home, gifts, and so on).
- `writing2[8]`, `checkpoint3` {`build`[8 × {`words`[], `answer`}], `quiz`[10]} as in French.

### `part5.json`
As in French: `dialogues[20]`, `readings[6]`, `literature[10]` (each with `bangla_pair`), `writing3[8]`, `selftest[60]`, `can_do[25]`, `road{}`.
For Arabic, `literature` draws on: proverbs, short poetry lines (al-Mutanabbī, Imruʾ al-Qays's opening line, Aḥmad Shawqī, Jubrān, al-Shāfiʿī),
one or two famous sayings, and **one** Qur'an verse and **one** hadith (well known, exact reference). Every quotation must be one you are certain of.

## 8. Ch. 4 list: Arabic words Bangla already knows (do NOT reuse these in the journey)

دُنْيَا দুনিয়া · آخِرَة আখিরাত · عَدَالَة আদালত · حَاكِم হাকিম · إِنْصَاف ইনসাফ · خَبَر খবর · تَارِيخ তারিখ · حِسَاب হিসাব ·
قَانُون কানুন · عِزَّة ইজ্জত · دَوْلَة দৌলত · عَقْل আক্কেল · قِسْمَة কিসমত · مُشْكِل মুশকিল · نَصِيب নসিব · حَقّ হক · بَاقِي বাকি ·
أَصْل আসল · نَقْل নকল · جَوَاب জবাব · سُؤَال সওয়াল · وَعْد ওয়াদা · خَيَال খেয়াল · قِصَّة কিসসা · مَالِك মালিক · أَمِير আমির ·
وَكِيل উকিল · حُكْم হুকুম · مَجْلِس মজলিস · مَحَلَّة মহল্লা · وَزْن ওজন · أَدَب আদব · طَاقَة তাকত · هَوَاء হাওয়া · عِمَارَة ইমারত ·
فَقِير ফকির · غَرِيب গরিব · خَالِي খালি · عَجَب আজব · مَوْسِم মৌসুম · فَصْل ফসল · طَرَف তরফ · مَحَبَّة মহব্বত · بَدَل বদল ·
نَظَر নজর · حَاضِر হাজির · غَائِب গায়েব · شُرُوع শুরু · خَتْم খতম · مُعَاف মাফ · سَفَر সফর · مُسَافِر মুসাফির · وَقْت ওয়াক্ত ·
قَبْر কবর · رَحْمَة রহমত · دَلِيل দলিল · خَزِينَة খাজনা · مَنْفَعَة মুনাফা · نَقْد নগদ · دُعَاء দোয়া · عَادَة আদত · كُرْسِي কুরসি ·
مِيزَان মিজান · أَمَانَة আমানত · خِدْمَة খেদমত · مَعْلُوم মালুম · شَرْط শর্ত · تَعْلِيم তালিম · عِلْم ইলম

(Core everyday nouns that are *also* Bangla words, such as كِتَاب কিতাব, قَلَم কলম, دُكَّان দোকান, are **not** on this list:
the journey may teach them, with a `link_bn` note.)
