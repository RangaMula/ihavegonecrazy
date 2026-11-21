# How the Arabic of the Muwaṭṭaʾ is carried into English, Urdu, Persian, Hindi, Bengali and Japanese

**Method.** The sunnah.com Arabic was aligned entry by entry with the English (Bewley), Urdu (Waḥīd al-Zamān's text) and
Bengali (Islamic Foundation Bangladesh) translations distributed by `fawazahmed0/hadith-api`, and every feature in the table
below was counted over all 1,858 entries (`tools/compare.py` reproduces the counts). For Persian, Hindi and Japanese no
machine-readable text exists. Their profiles come from the published editions' own descriptions and from comparable texts
(see `01-sources-and-translations.md`).

> Short quotations of the third-party translations appear here for study only. They are copyrighted and are **not** used
> in our edition, which is translated afresh from the Arabic.

## 1. The map, element by element

| Arabic element | Count in the Arabic | English (Bewley) | Urdu (Waḥīd al-Zamān) | Bengali (IFB) |
|---|---|---|---|---|
| **Chain of narrators** (*isnād*): وَحَدَّثَنِي يَحْيَى، عَنْ مَالِكٍ، عَنْ … | in almost every entry | **Kept in short form**: "Yahya related to me from Malik from Zayd ibn Aslam from…" (1,531 entries) | **Dropped**; only the last narrator kept: "عطاء بن یسار سے روایت ہے" (999 entries open this way; 87 keep Yaḥyā/Mālik) | **Dropped**; only the last narrator kept: "আতা ইবন ইয়াসার (রহঃ) হইতে বর্ণিত" |
| **The ﷺ formula**: صلى الله عليه وسلم | 871 entries | Translated in full: "may Allah bless him and grant him peace" (881) | Kept in Arabic: صلی اللہ علیہ وسلم (576) | Transliterated in full: সাল্লাল্লাহু আলাইহি ওয়াসাল্লাম (846) |
| **Honorifics for Companions / scholars** | **none in the Arabic** | Not added (4 exceptions) | **Added**: رضی اللہ تعالیٰ عنہ (466), حضرت (403) | **Added**: (রাঃ) (1,297), (রহঃ) (1,214), (আঃ) for angels and prophets |
| **Allah** | | "Allah" (1,045; "God" once) | اللہ, with جل جلالہ / تعالیٰ added | আল্লাহ্, often with তা'আলা added |
| **Ritual terms** (*ṣalāt, wuḍūʾ, ghusl, zakāt, sunna*, prayer names) | | **Left in Arabic**: wudu (72), ghusl (45), zakat (47), sunna (49), asr, isha, subh; "prayer" for *ṣalāt* (salat 0) | **Naturalised Persian-Urdu words**: نماز (308; صلوۃ once), وضو | **Naturalised Perso-Urdu words**: নামায (376; সালাত 14), ওযু, যোহর, আসর |
| **Mālik's legal formulas**: الأَمْرُ عِنْدَنَا (85), الأَمْرُ الْمُجْتَمَعُ عَلَيْهِ عِنْدَنَا, لاَ أَرَى بِذَلِكَ بَأْسًا | 285 *qāla Mālik* | "The situation with us is…", "The generally agreed-upon way of doing things among us…", "he thought there was no harm". **Inconsistent**: at least 5 different renderings | "کہا مالک نے" (143); "ہمارے نزدیک یہ حکم اتفاقی ہے"; "کچھ قباحت نہیں" | "মালিক (রহঃ) বলেন" (409); "আমাদের ফয়সালা এই", "আমাদের কাছে ইহা একটি মতভেদহীন মাসআলা" |
| **The gloss يَعْنِي** ("meaning…", a narrator's or Mālik's own explanation) | | "i.e.", "meaning" | یعنی (67) | অর্থাৎ (188, many of them the translator's own glosses) |
| **Translator's explanations** | | In parentheses (330) | In parentheses (110), but also **woven into the text without brackets** | Parentheses in almost every entry (1,732) |
| **Qurʾān quotations** {…} | 102 | Quoted, with no reference | Paraphrased as "…جو فرمایا اللہ جل جلالہ نے" | Usually given in Arabic, then in Bengali |
| **Units and measures** (*farsakh, ṣāʿ, mudd, wasq*) | | Kept (farsakh) | **Converted**: 3 farsakh → "نو میل" (nine miles) | Kept (ফরসখ) |
| **Register** | | Plain modern English | 19th-century Urdu, verb-first Arabic word order ("فرمایا رسول اللہ ﷺ نے") | Old literary Bengali (*sādhu bhāṣā*): হইতে, বলিলেনঃ, করিয়াছেন |
| **Numbering** | sunnah.com running number + per-book number | per-book | per-book (many entries empty or merged) | "রেওয়ায়ত n" (1,705 entries), restarting per book; **misaligned** after some books |

### Persian (al-Muṣaffā; Rostamī 2014)

- *al-Muṣaffā* is translation plus commentary, not a bare translation. It reorders material and sets the Ḥanafī and
  Shāfiʿī positions beside Mālik's, so the reader gets the law, not just the text.
- Rostamī's modern translation follows Yaḥyā's order and glosses difficult words after each ḥadīth.
- Persian keeps the Arabic legal vocabulary almost untouched (نماز, وضو, غسل, سنت, زکات) and writes the eulogies in Arabic
  (صلی الله علیه وسلم, رضی الله عنه).
- Pronunciation help is unnecessary for Persian readers, who read Arabic script. What they need is the vowel marks, which
  the Arabic line already has.

### Hindi (no Muwaṭṭaʾ exists; conventions from Hindi Qurʾān and Bukhārī translations)

- Devanagari with nukta letters (क़ ख़ ग़ ज़ फ़).
- Urdu religious vocabulary (नमाज़, वुज़ू, रसूल, सुन्नत) in a Hindi frame.
- The formula transliterated as सल्लल्लाहु अलैहि व सल्लम.
- Companion honorifics in short form: (रज़ि.)
- Usually no chains.

### Japanese (no Muwaṭṭaʾ exists; the precedent is 『日訳サヒーフ・ムスリム』)

- Chain cut to the first narrator.
- ﷺ formula and Companion eulogies **omitted** because they are so frequent.
- Notes marked （注）.
- アッラー, アッラーの使徒.
- Ritual terms translated with a Japanese word, with the Arabic in katakana where needed: 礼拝 (サラー), 清め (ウドゥー).

## 2. One ḥadīth through every language (Book 1, entry 3: the time of the dawn prayer)

Arabic, the ḥadīth core only:

> جَاءَ رَجُلٌ إِلَى رَسُولِ اللَّهِ ﷺ فَسَأَلَهُ عَنْ وَقْتِ صَلاَةِ الصُّبْحِ … ثُمَّ قَالَ "أَيْنَ السَّائِلُ عَنْ وَقْتِ الصَّلاَةِ" … فَقَالَ "مَا بَيْنَ هَذَيْنِ وَقْتٌ"

**English:**
- Keeps the chain.
- "the time of the subh prayer": *ṣubḥ* left in Arabic.
- Adds "The Messenger of Allah … did not answer him", which turns فَسَكَتَ ("he was silent") into an interpretation.

**Urdu:**
- No chain.
- "پوچھا آپ ﷺ سے نماز صبح کا وقت": Arabic word order, *ṣubḥ* → صبح.
- **Adds** a gloss: "اندھیرے منہ صبح صادق نکلتے ہی" ("in the dark, as soon as true dawn rose").
- "پھر تیسرے روز" ("on the third day") is an interpretation not in the Arabic, which says مِنَ الْغَدِ ("the next day").

**Bengali:**
- No chain.
- "ফজর নামাযের সময়": *ṣubḥ* → ফজর.
- Adds "(সূবহ-এ সাদিক)" and "(ভোরের আলো)" in brackets.
- Translates مَا بَيْنَ هَذَيْنِ وَقْتٌ ("between these two is a time") as "এতদুভয়ের মধ্যবর্তী মুহুর্তগুলিই ফজর নামাযের সময়"
  ("the moments between these two are the time of the Fajr prayer"), which makes the implied word explicit.

**What the Arabic does that all three soften:**
- The narrative's rhythm of فَ … ثُمَّ … ثُمَّ ("and so… then… then").
- The terse verbless punchline مَا بَيْنَ هَذَيْنِ وَقْتٌ.
- The Prophet teaching by **doing**: he answers only by praying twice.

A faithful translation keeps the terse punchline and puts any explanation in a note.

## 3. Errors and drifts found while aligning

1. **Bengali রেওয়ায়ত ৩০** (Book 1; it sits in data row 31, which also holds the next ḥadīth): الثُّوم (garlic) is translated as **পিয়াজ (onion)**: "পিয়াজের গন্ধ আমাদের কষ্ট দিবে". The Arabic
   says *garlic*.
2. **Bengali alignment:** entries are merged and numbered per book, so from some books on the Bengali text describes a
   different ḥadīth from the Arabic at the same position. For example, at position 1309 (Book 31) the Bengali is about
   pledges (*rahn*) while the Arabic is about selling fruit. The Bengali cannot be used as a parallel text without
   re-alignment.
3. **Urdu omissions:** 275 rows are empty, and Mālik's statements are sometimes left out entirely (entry 39 drops "قال
   مالك الأمر عندنا…").
4. **Urdu interpolations:**
   - additions without brackets: "ساتھ رسول اللہ ﷺ کے مدینہ میں" ("with the Messenger ﷺ in Madinah"), entry 10;
   - unit conversion: 3 farsakh → nine miles.
5. **English inconsistency:** at least five renderings of *al-amr ʿindanā*. A reader cannot tell that one fixed technical
   formula is behind them.

## 4. What this means for our bilingual edition (decisions)

| # | Decision | Why |
|---|---|---|
| 1 | **The Arabic is printed complete**, chain included, fully vowelled, with the ﷺ formula vowelled as well. | You asked for the full Arabic. The chain is part of the book. |
| 2 | **The pronunciation line covers the whole Arabic** and is generated by rule (`engine/`), not written by hand. | Consistent across 1,860 entries and every language. It follows your existing Bengali notation (`books/ar/STYLE.md`), so a reader of your Arabic book already knows it. |
| 3 | **Meaning:** the chain is given as a compact line of names (ইয়াহ়য়া ← মালিক ← যায়দ ইবনু আসলাম ← আতা ইবনু ইয়াসার), then the text is translated in full. | Combines Bewley's fidelity (the chain kept) with the Urdu/Bengali/Japanese readability (no repeated "related to me from…"). |
| 4 | **Mālik's commentary is separated and labelled** (e.g. «ইমাম মালিকের মন্তব্য»). | 26% of the book is Mālik's own voice. Every existing translation runs it into the ḥadīth text, so readers cannot tell the Prophet's words from the imam's ruling. |
| 5 | **One fixed rendering per formula**, kept in `standard/glossary.json`: *al-amr ʿindanā* = "the practice among us [in Madinah]", *al-amr al-mujtamaʿ ʿalayhi ʿindanā* = "the agreed practice among us", *lā arā bi-dhālika baʾsan* = "I see no harm in that". | Fixes the inconsistency found in English. |
| 6 | **No interpolation.** Words the Arabic implies go in [square brackets]. Explanations, units ("farsakh ≈ 5.5 km") and context go in numbered notes. | Avoids the Urdu and Bengali habit of weaving glosses into the text. |
| 7 | **Honorifics follow each language's Muslim convention, never added to the meaning line as if they were in the Arabic:** ﷺ after the Prophet's name; Companion eulogies are each language profile's choice (Bengali: (রা.)/(রহ.), the modern short form; Japanese: omitted, following the Ṣaḥīḥ Muslim precedent). | The Arabic has no Companion eulogies. Readers expect them in Bengali and Urdu; Japanese Muslim practice omits them. |
| 8 | **Modern standard register** (Bengali চলিত with Bangla Academy spelling: নামাজ, অজু, গোসল; plain modern Japanese with です/ます avoided in narrative). | The existing Bengali is in *sādhu bhāṣā*, a style few readers use today. |
| 9 | **Ritual terms:** each language's naturalised Muslim word (Bengali নামাজ, Hindi नमाज़, Japanese 礼拝), with the Arabic term in the glossary. | That is what readers of each language already use. The Arabic line keeps the original word anyway. |
| 10 | **Grades are shown** (Salim al-Hilālī, via hadith-api) as data, not as the editor's verdict. | Transparency. Mālik himself did not grade. |
| 11 | **Every language edition is a REVIEW DRAFT** until a qualified scholar fluent in that language has checked it. | Your series rule. For ḥadīth this is not optional. |
