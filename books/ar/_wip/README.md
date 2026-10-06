# Work in progress (paused)

The Arabic book was paused at the author's request. These folders hold the content agents' partial drafts (Python scripts that build
the data JSON files), so the next session can resume instead of starting over:

| Folder | Target file | State when paused |
|---|---|---|
| `ar-journey-1-10/` | `data/journey_1_10.json` | Sections 1–4 drafted (`s01_02.py`, `s03_04.py`); 5–10 not started |
| `ar-journey-11-20/` | `data/journey_11_20.json` | Sections 11–13 drafted (`s11.py`–`s13.py`); 14–20 not started |
| `ar-parts23/` | `data/part2.json`, `data/part3.json` | Ch. 5, 6, 7, 8–9, 10 drafted; Ch. 11, writing 2, checkpoints remaining |
| `ar-part5/` | `data/part5.json` | 20 dialogues drafted; readings in progress; literature, writing 3, self-test, can-do, road remaining |

Each folder has its own `translit.py` (Arabic → Bangla/English pronunciation following `../STYLE.md` §3–4).
To resume: brief new agents with the same instructions (see PLAYBOOK §3) and tell them to continue from these drafts,
then run `python3 validate.py`, build with `./make.sh`, and do the QA checklist.
