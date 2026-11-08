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
