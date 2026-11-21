# al-Muwaṭṭaʾ of Imām Mālik: the Arabic original and its credible translations

Researched November 2026. Statements checked directly against the machine-readable texts are marked **[checked]**.
Statements taken from catalogues or reviews carry a source link. **[unverified]** means the item could not be confirmed
from this environment (sunnah.com, shamela.ws and some university sites were unreachable). Check those items before
citing them in print.

## 1. The book

- **Author:** Imām Mālik ibn Anas (93–179 AH / 711–795 CE), the imam of Madinah and founder of the Mālikī school.
- **What it is:** the oldest surviving written collection of Islamic law and ḥadīth. Each chapter mixes four kinds of material:
  - ḥadīth of the Prophet ﷺ (with a full chain, or *mursal*, where the chain skips the Companion);
  - reports of the Companions (*mawqūf*);
  - reports of the Successors (*maqṭūʿ*);
  - Mālik's own legal statements (*qāla Mālik…*, *suʾila Mālik…*). These state the practice of Madinah (*al-amr ʿindanā*,
    "the position with us") and his reasoning.
- **Recension used here: Yaḥyā ibn Yaḥyā al-Laythī** (d. 234/848, al-Andalus).
  - He heard the book in Mālik's last year. This is the most widely circulated recension, the one read in North and West
    Africa and al-Andalus, and the one sunnah.com and the hadith apps carry.
  - Abū Bakr al-Abharī's classic breakdown: 600 *musnad*, 222 *mursal*, 613 *mawqūf*, 285 Successor sayings, about 1,720 in
    all (https://islamqa.info/en/answers/81160). Counts vary with how Mālik's statements and split entries are counted.
- **Other recensions:**
  - **Abū Muṣʿab al-Zuhrī** (d. 242): complete; about 77% overlaps with Yaḥyā, but in a different order.
  - **Ibn Bukayr** (d. 231, Egypt): complete.
  - **al-Shaybānī** (d. 189): an Iraqi/Ḥanafī version with his own and Abū Ḥanīfa's opinions added; only about 10% is verbatim
    the same as the vulgate.
  - **Suwayd al-Ḥadathānī**: fragments only.
  - **al-Qaʿnabī**: one surviving manuscript.

  Sources: https://knowledge.uchicago.edu/record/6671/files/Ur-Muwa%E1%B9%AD%E1%B9%ADa-and-Its-Recensions.pdf,
  https://kitab-project.org/A-Tale-of-3-Versions/

### Printed editions of Yaḥyā's recension

| Edition | Notes |
|---|---|
| **Muḥammad Fuʾād ʿAbd al-Bāqī**, Cairo 1951, 2 vols | The standard printed text (the "vulgate"). Its 61 *kutub* are the division used by sunnah.com and by this project. Numbering restarts in each book. |
| **Muḥammad Muṣṭafā al-Aʿẓamī**, Abu Dhabi: Zāyid Foundation, 2004, 8 vols | Critical edition that compares the recensions; 4 vols of text, plus an introduction volume and 3 index volumes. https://ketabonline.com/ar/books/3472 |
| **Royal Moroccan edition**, Casablanca: Ministry of Endowments, 2013 | Based on six old Maghribī/Andalusian manuscripts. The base text of the Harvard English translation. |
| Bashshār ʿAwwād Maʿrūf (Dār al-Gharb) | Widely used. **[unverified]** whether the 1993 2-vol edition is Yaḥyā's or Abū Muṣʿab's recension. |

### The text used in this project **[checked]**

- `data/arabic/muwatta.json`, built by `tools/build_dataset.py`.
- **Text:** the sunnah.com Arabic, fully vowelled, via `AhmedBaset/hadith-json` v1.2.0.
  - 1,860 non-empty entries in 61 books.
  - It contains every entry of the fawazahmed0 hadith-api text, plus 30 entries that file leaves blank.
- **Grades and references:** `fawazahmed0/hadith-api` (Unlicense). The grades are credited to Salim al-Hilālī; the edition
  they come from is **[unverified]**. Grades were matched to 1,830 of the 1,860 entries.
- **Segmentation:** 335 entries end with Mālik's own commentary, which was split off by rule (the openers
  *qāla Mālik / qāla Yaḥyā qāla Mālik / suʾila Mālik*). Another 23 entries are wholly his words. Mālik's words make up about
  26% of the text.
- **Known gaps:**
  - 28 words in 16 entries carry no vowel marks in the source; the pronunciation line shows them in Arabic, flagged.
  - Chapter (*bāb*) headings are not in the source, only book (*kitāb*) titles.
  - The sunnah.com running numbers (1–1,985) are that site's own sequence, not a printed edition's numbering. Our entries
    keep the number of each entry inside its book (`nb`), which matches ʿAbd al-Bāqī's per-book numbering where entries
    are not split.

### Classical commentaries (where "the commentary" of a ḥadīth comes from)

- **Ibn ʿAbd al-Barr** (d. 463): *al-Tamhīd*, arranged by Mālik's teachers and focused on chains; *al-Istidhkār*, which follows
  the book's order and focuses on law.
- **al-Bājī** (d. 474): *al-Muntaqā*.
- **al-Suyūṭī**: *Tanwīr al-ḥawālik*.
- **al-Zurqānī** (d. 1122): *Sharḥ*.
- **Shāh Walī Allāh Dihlawī** (d. 1176): *al-Muṣaffā* (Persian) and *al-Musawwā* (Arabic).
- **Kāndhlawī**: *Awjaz al-masālik*.

> Our edition presents **only Mālik's own commentary**, the part that is inside the book itself. Later commentators'
> explanations are not added unless a scholar-editor supplies them, so that nothing is put in Mālik's mouth.

## 2. English

| Translation | Credibility | Approach |
|---|---|---|
| **Mohammad Fadel & Connell Monette**, *al-Muwaṭṭaʾ, the Royal Moroccan Edition*, Harvard Law School Program in Islamic Law / Harvard UP, 2019 (Harvard Series in Islamic Law 8) | **The most scholarly.** Fadel is a University of Toronto law professor specialising in Mālikī law. Reviewed as high quality. https://islamiclaw.blog/2019/09/20/recent-scholarship-fadel-and-monette-on-the-english-translation-of-the-muwatta-of-imam-malik-b-anas/ | Contemporary English legal terminology, an explicit methodology, and some deliberately non-literal renderings (*ṣalāt al-khawf* = "Prayer of Danger"). Follows the 2013 Moroccan text, so **its numbering does not match sunnah.com**. **[unverified]** how it treats chains and the ﷺ formula. |
| **Aisha Abdurrahman Bewley**, *Al-Muwatta of Imam Malik ibn Anas: The First Formulation of Islamic Law*, Kegan Paul 1989; Diwan Press revised ed. 2014 (earlier Diwan version with Yaʿqub Johnson) | The text on sunnah.com and in most apps. Bewley is a prolific translator of classical Arabic. A 1990 review criticised the many untranslated terms. https://diwanpress.com/shop/authors/aishbewley/al-muwatta | Plain, fairly literal; see the mapping study. |
| **Muhammad Rahimuddin**, *Muwatta' Imam Malik*, Sh. Muhammad Ashraf, Lahore (preface 1979); reprinted Kitab Bhavan (New Delhi) and Darussalam | A former English professor at Osmania University. An older style. | "(may peace be upon him)", with explanatory footnotes. |
| Mohammed Abdurrahman & Abdassamad Clarke, *The Muwatta of Imam Muhammad*, Turath 2004 | Al-Shaybānī recension, so a different book. | |

## 3. Urdu

- **Waḥīd al-Zamān (Ahl-i Ḥadīth), *Kashf al-Mughaṭṭā*** (Delhi c. 1879; Lahore 1309 AH; New Delhi: Iʿtiqād Publishing, 1986).
  - The dominant classic Urdu translation. Urdu scholars describe it as "قدیم اور لفظی" (old and literal).
  - The online/app Urdu text has its fingerprints **[checked, attribution inferred]**:
    - no chain;
    - a "…سے روایت ہے" opening in 999 entries;
    - Arabic word order kept.
  - Catalogues: https://search.library.wisc.edu/catalog/9913220893902121, https://forum.mohaddis.com/threads/7784/
- Later Urdu editions with *takhrīj* and notes:
  - Rafīq Atharī;
  - Imran Ayub Lahori's *taḥqīq* edition.
  - **[unverified]**: ʿAbd al-Ḥakīm Akhtar Shāhjahānpūrī, and the Dar-us-Salam and Maktaba Raḥmāniyya editions.

## 4. Persian

- **Shāh Walī Allāh Dihlawī, *al-Muṣaffā sharḥ al-Muwaṭṭaʾ*** (18th c.).
  - A Persian translation with commentary that reorganises the material and gives the Ḥanafī and Shāfiʿī positions next to
    Mālik's. Its Arabic twin is *al-Musawwā*.
  - Printings: Delhi, Maṭbaʿ Fārūqī 1293 AH; Karachi 1980; Iran: ed. Dāwūd Nārūyī, Nashr-e Eḥsān, 2 vols.
  - https://library.jamiahamdard.ac.in/bib/121046, https://openlibrary.org/books/OL3933268M
- **Ḥosein Rostamī, *Tarjome-ye fārsī-ye al-Muwaṭṭaʾ*** (Yaḥyā's recension), Hosseini-Asl, Urmia, 1393 SH (2014/15), 972 pp.
  - A modern Persian translation that glosses difficult words after each ḥadīth.
  - http://www.lib.ir/book/62897942/ **[single source cluster]**
- No Afghan translation was found.

## 5. Hindi

- **No credible published Hindi translation of the Muwaṭṭaʾ was found.** The only lead is one unattributed PDF listing.
- Conventions were taken instead from comparable Hindi Islamic texts:
  - Hindi Qurʾān translations (quranenc.com);
  - *Mukhtaṣar Ṣaḥīḥ al-Bukhārī* in Hindi (islamhouse.com).

  What they share:
  - Devanagari with the nukta letters क़ ख़ ग़ ज़ फ़, used inconsistently (नमाज़/नमाज);
  - Perso-Arabic religious vocabulary (अल्लाह, रसूल, ईमान, नमाज़) mixed with Sanskritic words;
  - the ﷺ formula transliterated as सल्लल्लाहु अलैहि व सल्लम.
- **This means an Arabic→Hindi edition would be the first.** That is an opportunity, but also a reason for careful scholarly
  review.

## 6. Bengali (bonus: your first target language)

- **Islamic Foundation Bangladesh, *মুয়াত্তা ইমাম মালিক (রহ.)***, 2 vols (vol. 1 1982, vol. 2 1987 per the Rajshahi
  University catalogue). Translator: **Muhammad Rezaul Karim Islamabadi**. https://archive.org/details/20210721_20210721_1421
- Mina Book House, Dhaka, tr. Allāma Azizul Haque, © 2017.
- Online reader: https://hadithbd.net/hadith/sections/?book=29

## 7. Japanese

- **No Japanese translation of the Muwaṭṭaʾ exists**; encyclopedias only name it (『ムワッタア』). An Arabic→Japanese edition would also be a first.
- The closest precedent: **『日訳サヒーフ・ムスリム』**, tr. 磯崎定基・飯森嘉助・小笠原良治 (日本サウディアラビア協会 1987;
  日本ムスリム協会 2001). Its preface **[read on archive.org]** states:
  - it is translated from ʿAbd al-Bāqī's Arabic text;
  - **the chain is cut to the first narrator only**;
  - the ﷺ formula and Companion eulogies are **omitted because they are so frequent**;
  - notes are marked （注）;
  - it uses アッラー and アッラーの使徒.
- Qurʾān: 三田了一, 『日亜対訳・注解 聖クルアーン』 (日本ムスリム協会, rev. 1982), which uses アッラー.
- 牧野信也's Bukhārī (『ハディース イスラーム伝承集成』, 中公文庫 2001) is the academic precedent. **[unverified]** whether it
  writes 神 or アッラー.
- Katakana conventions:
  - long vowels with ー;
  - name parts joined with ・;
  - ʿayn and hamza not marked;
  - *ibn* written ブン or イブン.
