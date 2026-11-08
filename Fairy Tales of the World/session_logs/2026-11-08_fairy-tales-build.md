# Session log — 2026-11-08 — Fairy Tales of the World

## Request (user's words)
"Find out ১০০ উপকথা/রূপকথা per country or ethnicity-wise, that are open ended (not attached to any
intellectual property rights) and can be translated in every language of the world without any legal and
ethical barrier. Search, copy and save it country and ethnicity-wise folder in a new workspace folder
called 'Fairy Tales of the World'." Mid-task: "use open router" → then "ok, dont use open router".

## Decisions
- OpenRouter was not used (user withdrew it; the key also had a $1/month cap). No AI-generated text:
  every tale is copied verbatim from a public-domain book.
- Gutenberg, Wikisource and Archive.org were blocked from the cloud sandbox; Project Gutenberg texts were
  fetched through its GitHub mirror (GITenberg, raw.githubusercontent.com).
- Copyright rule: keep a book only if every named author/collector/translator died ≤ 1955 (life + 70 →
  PD worldwide in 2026); illustrators ignored (no images copied). Books failing the rule were removed.
  Tales whose translator death date is unrecorded are kept but labelled "PD in USA".
- Saved in the GitHub repo (rangamula/ihavegonecrazy, branch claude/relaxed-goodall-y0pseq); the
  G:\ Drive workspace and E:\ backup are not reachable from a cloud session.

## Deliverables
- `Fairy Tales of the World/` — 4,608 tales, 81 tradition folders, `index.csv`, per-folder `_README.md`.
- `_tools/` — scripts to rebuild.

## Next steps
- Pull the branch locally and copy the folder into `G:\My Drive\Claude Workspace\` + mirror to `E:\Claude Backup`.
- Fill gaps (Ainu, Brazil, Africa, Latin America, Middle East) from Wikisource/Archive.org on a machine with access.
- Editorial pass on outdated terminology before translation for children.

---

# Session log (continued) — translation kit + filling the gaps

## Requests (user's words)
1. "Record and organize the stories in a format that you can easily translate and do whatever u needed."
2. "fill the gaps from internet. specially u left a large gap not covering africa....use online blogs, nespapers
   and journels that record the stories as text or free pdf." / "u can also search the country-wise 'Bangla Academy'
   type organization that puts in effort to preserve their culture."

## Decisions
- Blogs, newspapers, journals and academy publications are copyrighted, so copying them would break the user's
  original "no legal barrier" rule. Used only public-domain books and CC BY 4.0 texts. Heritage institutions
  are listed with links only (HERITAGE_ORGANISATIONS.md).
- With the user's approval, the environment allowlist gained gutenberg.org, archive.org, wikisource, africanstorybook.org,
  storyweaver.org.in and globalstorybooks.net.
- New sources: ~40 Gutenberg books (full catalogue CSV search), 14 Internet Archive OCR books (TOC-driven splitter),
  African Storybook (338 CC BY stories in ~40 languages; 10 NonCommercial ones excluded).
- Excluded for ethics: *Black Tales for White Children*, *My Dark Companions*, *Negro Myths from the Georgia Coast*;
  for copyright: Hollis (d. 1961).
- Translation kit: per-tale segmented JSON + XLIFF 1.2 per tradition + name glossaries + catalog.json;
  `_tools/apply_translation.py` rebuilds Markdown from translated JSON/XLIFF. Sample: one Bengal tale translated
  into Bengali (translations/bn/...).

## Deliverables
- 6,283 tales, 110 traditions (Africa: 1,223 tales in 38 folders, up from ~290), index.csv, README.md.
- translation-kit/ (TRANSLATING.md, catalog.json, source/, xliff/, glossary/), translations/bn/ sample.
- HERITAGE_ORGANISATIONS.md.

## Next steps
- Process the remaining PD African books (Callaway, Bleek & Lloyd, Steere, Torrend, Monteil, Maspero) by hand-tuned splitting.
- StoryWeaver CC BY folk tales (needs a free login); Wikisource Bengali and other languages.
- Copy the folder to G:\My Drive\Claude Workspace and mirror to E:\Claude Backup (not reachable from the cloud session).
