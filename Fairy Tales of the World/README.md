# Fairy Tales of the World — উপকথা ও রূপকথা

A collection of **6,283 traditional folk tales, fairy tales, fables and legends** from
**110 countries, regions and peoples (ethnic groups)**, one folder per tradition (up to 100
tales each), including **1,223 tales from 25 African traditions**.
Every tale is either **public domain** or published under an **open licence (CC BY 4.0)**, so it can be
read, shared, adapted and **translated into any language** without asking permission.

Last rebuilt: 8 November 2026.

## Folder layout

```
Fairy Tales of the World/
├── <Continent>/<Country, region or people>/
│     ├── _README.md            ← sources, licence and list of tales for this folder
│     └── 001 - <Title>.md      ← one tale per file, with a source/copyright header
├── translation-kit/            ← the same tales split into numbered segments, ready for translation (see TRANSLATING.md)
├── translations/<language>/    ← finished translations, same layout as the originals
├── HERITAGE_ORGANISATIONS.md   ← Bangla Academy–type institutions per country (links only)
├── index.csv                   ← every tale: continent, tradition, title, file, source, credits, status
└── _tools/                     ← scripts to rebuild everything
```

## Where the tales come from

| Source | What | Licence |
|---|---|---|
| Project Gutenberg (gutenberg.org, and its GitHub mirror GITenberg) | Folk-tale books published 1700s–1930 | Public domain |
| Internet Archive (archive.org) | Scanned 1868–1922 collections, mostly African: Hausa, Angola, Basotho, Kongo, Ronga, Kabyle, Berber, Egyptian, Malagasy, Somali, Sahel (Frobenius) | Public domain (OCR text, lightly cleaned) |
| African Storybook (africanstorybook.org) | Traditional African tales retold for children, in ~40 African languages plus English, French and Portuguese | **CC BY 4.0**: credit the authors and illustrators named in each file |

Blogs, newspapers, journal articles and the publications of national academies were **not** copied:
they are protected by copyright and would break the "no legal barrier" rule.
`HERITAGE_ORGANISATIONS.md` lists those institutions so you can find tales and ask permission.

## Legal status of every file (shown in each tale's header)

- **Public domain worldwide: 4,598 tales.** Every named author, collector and translator died in or before
  1955. Most countries protect a text for the author's life plus 70 years, so these are free everywhere.
- **Public domain in the USA: 1,421 tales.** Published long ago, but one contributor's death date isn't recorded, so the
  life+70 test couldn't be confirmed. The traditional story is free either way. Only if you will republish
  this exact wording in a life+70 country is it worth checking that translator.
- **CC BY 4.0: 264 tales** (African Storybook). Free for any use, commercial included, if you credit the
  people named in the file and link to https://creativecommons.org/licenses/by/4.0/. Items marked NonCommercial were
  left out.
- **Removed:** books whose author or translator died after 1955 (e.g. Josef Cohen, Elsie Spicer Eells, Mabel Powers,
  Maive Stokes, A. C. Hollis).

Project Gutenberg's licence and trademark text was removed. Only the public-domain story text remains, with
a citation.

## Ethical notes before translating

- Most texts were written down in 1850–1930, often by colonial officials and missionaries. Some use outdated or
  offensive terms for peoples (e.g. "Kaffir", "Hottentot", "Eskimo") or a colonial point of view. Modernise the
  wording, especially for children. A few books were left out entirely because their titles or framing are
  demeaning (e.g. *Black Tales for White Children*, *My Dark Companions*).
- Many Indigenous stories (Native American, Aboriginal Australian, Māori, Hawaiian, San, etc.) are sacred
  narratives. Credit the people they come from, and where possible consult present-day community
  organisations before publishing a retelling.
- OCR-sourced tales (marked in their header) may contain small recognition errors. Proofread before
  publishing. About 11 African Storybook texts in Lugbarati, Anii and a few other languages keep some
  garbled accent characters that were already damaged on the source website.

## Contents (110 traditions, 33 with the full 100 tales)

| Continent | Tradition (country / region / people) | Tales |
|---|---|---|
| Europe | England | 100 |
| Europe | Cornwall (Cornish people) | 100 |
| Europe | Scotland | 100 |
| Europe | Ireland | 100 |
| Europe | Wales | 100 |
| Europe | Isle of Man (Manx people) | 42 |
| Europe | Celtic peoples (pan-Celtic) | 50 |
| Europe | Germany | 100 |
| Europe | Austria (Tyrol) | 100 |
| Europe | Switzerland | 40 |
| Europe | Netherlands | 21 |
| Europe | Belgium (Flemish people) | 29 |
| Europe | France | 100 |
| Europe | Brittany (Breton people) | 100 |
| Europe | Basque people | 26 |
| Europe | Spain | 100 |
| Europe | Portugal | 21 |
| Europe | Italy | 100 |
| Europe | Greece (Aesop and folk tales) | 100 |
| Europe | Norway | 100 |
| Europe | Sweden | 83 |
| Europe | Denmark | 100 |
| Europe | Finland | 59 |
| Europe | Russia | 100 |
| Europe | Ukraine (Cossack tales) | 27 |
| Europe | Poland | 7 |
| Europe | Czech lands (Bohemia, Moravia) | 56 |
| Europe | Slavic peoples (pan-Slavic) | 92 |
| Europe | Serbia | 100 |
| Europe | South Slavs (Yugoslav tales) | 15 |
| Europe | Hungary (Magyar people) | 100 |
| Europe | Romania | 100 |
| Europe | Jewish people | 34 |
| Europe | Estonia | 47 |
| Europe | Iceland | 24 |
| Europe | Catalonia (Catalan people) | 52 |
| Asia | Armenia | 40 |
| Asia | Georgia | 38 |
| Asia | Caucasus peoples | 9 |
| Asia | Arab peoples (Arabian Nights) | 100 |
| Asia | Persia (Iran) | 5 |
| Asia | Turkey | 50 |
| Asia | India | 100 |
| Asia | Bengal (Bengali people) | 39 |
| Asia | Punjab (Punjabi people) | 47 |
| Asia | Deccan (Marathi people) | 20 |
| Asia | Santal people | 100 |
| Asia | Khasi people | 32 |
| Asia | Kachari (Bodo) people | 23 |
| Asia | Sri Lanka (Sinhalese people) | 100 |
| Asia | Burma (Myanmar) | 7 |
| Asia | Shan people | 9 |
| Asia | Laos | 50 |
| Asia | China | 100 |
| Asia | Korea | 88 |
| Asia | Mongolia (Kalmyk people) | 2 |
| Asia | Japan | 100 |
| Asia | Ainu people | 0 |
| Asia | Philippines | 100 |
| Africa | Nigeria (Efik, Ibibio and Ikom peoples) | 73 |
| Africa | South Africa | 100 |
| Africa | Khoikhoi people | 8 |
| Africa | San people | 78 |
| Africa | Swahili people (Zanzibar, Tanzania) | 20 |
| Africa | Hausa people (Nigeria, Niger) | 59 |
| Africa | Ghana (Akan peoples, Anansi tales) | 100 |
| Africa | Sierra Leone (Temne, Mende peoples) | 50 |
| Africa | Gabon and Cameroon (Benga, Mpongwe peoples) | 62 |
| Africa | Congo (Kongo and Vili peoples) | 92 |
| Africa | Angola (Mbundu people) | 47 |
| Africa | Lesotho (Basotho people) | 23 |
| Africa | Mozambique (Ronga, Tsonga and Tswa peoples) | 96 |
| Africa | Zulu people | 24 |
| Africa | Xhosa people | 23 |
| Africa | Southern Africa (regional tales) | 62 |
| Africa | Kabyle people (Algeria) | 100 |
| Africa | Berber (Amazigh) peoples of North Africa | 20 |
| Africa | Egypt (Arabic folk tales) | 7 |
| Africa | Madagascar (Malagasy people) | 10 |
| Africa | Mali and the Sahel (Soninke, Fulani, Bambara peoples) | 100 |
| Africa | Somalia (Somali people) | 33 |
| Africa | East Africa (Uganda, Kenya, Ethiopia) | 7 |
| Africa | Benin | 3 |
| Africa | Africa (various, origin not stated) | 26 |
| Americas | United States (settler legends) | 100 |
| Americas | Canada | 26 |
| Americas | Squamish people (Legends of Vancouver) | 16 |
| Americas | Mexico | 20 |
| Americas | Chile | 90 |
| Americas | Peru | 27 |
| Americas | Caribbean (Suriname and the Dutch Antilles) | 93 |
| Americas | Alaska Native peoples | 60 |
| Americas | Brazil | 1 |
| Americas | Dakota-Lakota (Sioux) people | 99 |
| Americas | Blackfoot (Siksika) people | 60 |
| Americas | Iroquois (Haudenosaunee) people | 56 |
| Americas | Wabanaki (Algonquian) peoples | 55 |
| Americas | Ojibwe and Algonquin peoples | 73 |
| Americas | Cherokee people | 100 |
| Americas | Navajo (Dine) people | 20 |
| Americas | Pawnee people | 26 |
| Americas | Western Apache people | 13 |
| Americas | Modoc people | 58 |
| Americas | Pima (Akimel O'odham) people | 20 |
| Americas | Inuit (Eskimo) peoples | 83 |
| Americas | Native North America (various nations) | 100 |
| Oceania | New Zealand (Maori people) | 44 |
| Oceania | New Caledonia (Kanak people) | 5 |
| Oceania | Australia (Aboriginal peoples) | 31 |
| Oceania | Hawaii (Native Hawaiian people) | 100 |

## Remaining gaps

- **Still thin or empty:** Brazil, Ainu, parts of East Africa (Ethiopia, Kenya, Uganda), Central Asia, the
  Middle East outside the Arab and Persian classics, South-East Asia (Vietnam, Cambodia, Malaysia, Indonesia),
  Central America and the Pacific outside Hawaiʻi and Aotearoa.
- **Collected but not yet processed** (their OCR layout needs manual work): Callaway's *Zulu Nursery Tales*
  (1868), Bleek & Lloyd's *Specimens of Bushman Folklore* (1911), Steere's *Swahili Tales* (1870), Torrend's
  *Bantu Folk-lore from Northern Rhodesia* (1921), Monteil's *Contes soudanais* (1905), Maspero's *Contes
  populaires de l'Égypte ancienne*. All are public domain and on Internet Archive.
- **Next sources to add:** StoryWeaver (CC BY 4.0, needs a free login), Wikisource in Bengali/Hindi/Arabic/Chinese,
  more Frobenius *Atlantis* volumes (12 in total), Rattray's *Akan-Ashanti Folk-Tales* (1930).
- **Bengali originals:** *Thakurmar Jhuli* (Dakshinaranjan Mitra Majumder, d. 1957) is public domain in Bangladesh and
  India, and worldwide from 1 January 2028.

## Rebuilding

See `_tools/` (`catalog.py` maps sources to folders; `build.py` holds the copyright rules; `prep_extra.py`
adds the Internet Archive and African Storybook sources; `make_kit.py` regenerates the translation kit).
