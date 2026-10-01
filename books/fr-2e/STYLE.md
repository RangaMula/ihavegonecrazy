# ফরাসি ভাষার দরজা — French book: language style guide and data format

Every writer (human or agent) of French-book content follows this file. The series rules are in
`series-standard/BOOK-STRUCTURE.md`; this file makes them concrete for French.

## 1. Reader and register

- Adult Bangla speakers (mostly Bangladesh): students, migrant workers, professionals, curious readers.
- Instruction language: standard চলিত Bangla, Bangladesh usage and Bangla Academy spelling (পানি, not জল; গোসল where natural).
  Address the reader as **আপনি**. Warm, respectful, never childish. No emoji walls.
- French taught: standard French of France, with notes for Belgium, Switzerland, Québec and Africa where they differ.
- The author is a Muslim scholar; content is welcoming to every reader. **No pork or alcohol items** in vocabulary,
  dialogues or examples (no vin, bière, jambon, porc, saucisson…). Food culture is shown through halal-friendly
  items (baguette, croissant, crêpe, ratatouille, couscous, tajine, fromage, café…).

## 2. The Triple Row (every French item)

Every French word, phrase or sentence is stored as an object with five fields:

```json
{"fr": "Bonjour", "bn_pron": "বোঁঝ়ুর়", "en_pron": "bohn-ZHOOR", "bn": "শুভ দিন / হ্যালো", "en": "hello / good day"}
```

| Field | Content |
|---|---|
| `fr` | Correct French with all accents. Nouns **with article**: `le pain`, `la maison`, `l'eau (f.)`, `les gens (m. pl.)`. Adjectives in masculine form (feminine in `note_bn`). Verbs in the infinitive. |
| `bn_pron` | Bangla-script pronunciation, following §3 exactly |
| `en_pron` | English-reader respelling, following §4 |
| `bn` | Bangla meaning (short) |
| `en` | English meaning (short) |
| `note_bn` | Optional. One short Bangla note (gender, feminine form, irregularity, usage) |

## 3. Bangla pronunciation rules (series notation applied to French)

| French sound | Spelling in French | Bangla notation | Example |
|---|---|---|---|
| f | f, ph | **ফ়** | café = কাফ়ে |
| v | v, w (rare) | **ভ়** | vous = ভ়ু |
| z | z, s between vowels | **জ়** | maison = মেজ়োঁ |
| ʒ (as in "measure") | j, g before e/i/y | **ঝ়** | bonjour = বোঁঝ়ুর়, rouge = র়ুঝ় |
| French r (throat r) | r | **র়** (always) | merci = মের়সি |
| ʃ | ch | শ | chat = শা |
| ɲ | gn | ন্য | montagne = মোঁতান্য |
| wa | oi | ওয়া | moi = মোয়া, trois = ত্র়োয়া |
| ɥi | ui | উই | nuit = নুই |
| a | a, à, â | আ / া | ami = আমি |
| e / ɛ | é, è, ê, er, ez, ai, et | এ / ে | été = এতে |
| i | i, î, y | ই / ি | merci = মের়সি |
| o / ɔ | o, ô, au, eau | ও / ো | beau = বো |
| u | ou, où | উ / ু | vous = ভ়ু |
| **y** (French u) | u, û | **ই° / ি°** (say ই with lips rounded as for উ) | tu = তি°, rue = র়ি° |
| **ø / œ / ə** | eu, œu, e (in le, je, de) | **এ° / ে°** (say এ with rounded lips) | deux = দে°, le = লে°, je = ঝ়ে° |
| ɑ̃ (nasal) | an, am, en, em | **আঁ / াঁ** | enfant = আঁফ়াঁ |
| ɔ̃ (nasal) | on, om | **ওঁ / োঁ** | bon = বোঁ |
| ɛ̃ / œ̃ (nasal) | in, im, ain, ein, un, um | **অ্যাঁ / ্যাঁ** | pain = প্যাঁ, vin = ভ়্যাঁ, un = অ্যাঁ |

- **°** is written right after the syllable whose vowel is rounded. **Nukta (়)** marks a consonant Bangla does not have.
  **Chandrabindu (ঁ)** marks nasal vowels: a sound Bangla speakers already have, which the book points out as an advantage.
- Silent letters are **not** written (final -s, -t, -d, -x, -e, -ent of verbs; h is always silent).
- Show obligatory liaison: les amis = লে জ়ামি, vous avez = ভ়ু জ়াভ়ে. Show elision as spoken: je m'appelle = ঝ়ে° মাপেল.
- Separate words with spaces exactly as in French.

## 4. English respelling rules

Simple respelling an English reader can say, syllables joined by hyphens, **final syllable of each word or phrase in CAPS**
(French stress falls on the last syllable of a phrase).

| Sound | Respelling | Example |
|---|---|---|
| ʒ | zh | bonjour = bohn-ZHOOR |
| y (French u) | ü | tu = TÜ |
| ø, œ, ə | uh | deux = DUH, le = luh |
| nasal ɑ̃ / ɔ̃ / ɛ̃ | ahn / ohn / ehn | enfant = ahn-FAHN, bon = BOHN, pain = PEHN |
| r | r (always the throat r, explained once in Ch. 5) | merci = mehr-SEE |
| e / ɛ | ay / eh | été = ay-TAY, mère = MEHR |

## 5. Culture content rules

- Breadth: France and its regions, Belgium, Switzerland, Luxembourg, Monaco, Québec/Canada, West and Central Africa
  (Sénégal, Côte d'Ivoire, Mali, Cameroun, RD Congo…), the Maghreb (Maroc, Algérie, Tunisie), Haïti and the Caribbean,
  the Indian Ocean (Maurice, La Réunion, Madagascar), and French India (Pondichéry, **Chandernagor / চন্দননগর in Bengal**,
  a direct link to Bengali history).
- Bangla links are gold: French words already in Bangla (রেস্তোরাঁ, ক্যাফে, বুফে, মেনু, ব্যালে, কুপন, শেফ, গ্যারেজ, শোফার…).
- Every **জানেন কি?** (`story_bn`) line is one Bangla sentence of wonder that you are **certain** is true. If unsure, leave it out.
  Add `source_hint` (a short English pointer, e.g. "UNESCO World Heritage list") so the fact can be verified.
- Show cultures as their own people see them. No stereotypes. Religion is described accurately and respectfully.
- `icon`: one emoji per culture word, used as a small icon on the card (adult design: one icon, never a row of emoji).

## 6. Data files (UTF-8 JSON in `books/fr/data/`)

### `journey_1_10.json` and `journey_11_20.json`

```json
{"sections": [{
  "no": 1, "stage": 1,
  "title_bn": "প্রথম শব্দ", "title_en": "First words",
  "scene_bn": "Two or three Bangla sentences that open the section like a scene in a story.",
  "can_do_bn": ["…", "…", "…"],
  "sets": [{"code": "1a", "kind": "F", "title_bn": "…", "title_en": "…",
            "words": [ {Triple Row + optional note_bn}, … 25 items ]},
           {"code": "1d", "kind": "C", "title_bn": "…", "title_en": "…",
            "words": [ {Triple Row + "icon": "🥐", "story_bn": "…", "link_bn": "optional link to Bangla", "source_hint": "…"}, … 25 ]}],
  "say_now": [ {Triple Row}, … 5 sentences using only words taught up to this section ],
  "mission_bn": "One 5-minute real-life task, in Bangla.",
  "quiz": [ {"q_bn": "…", "a": "…"}, … 10 ],
  "stamp": {"label_bn": "…", "icon": "🗼"}
}],
 "milestones": [{"after_section": 4, "total": 400, "title_bn": "…", "title_fr": "…",
   "celebration_bn": "…",
   "reading": [ {Triple Row}, … 8–12 sentences, only words already taught ]}]}
```

- Each section has exactly **4 sets of 25 words**; set kinds (F fixed / C culture) follow `series-standard/vocabulary/WORD-JOURNEY.md`.
- No French word appears twice in the 2,000. Numbers, days and months are **not** in the journey (they are in Ch. 8–9).

### `part2.json`, `part3.json`, `part5.json`

Structures are given in the task brief of each file; all French items use the Triple Row.
