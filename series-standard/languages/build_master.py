# -*- coding: utf-8 -*-
"""Generate MASTER-LANGUAGE-LIST.md from master_languages.csv. Run: python3 build_master.py"""
import csv, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "master_languages.csv"), encoding="utf-8")))
regions = collections.OrderedDict()
for r in rows:
    regions.setdefault(r["region"], []).append(r)
tiers = collections.Counter(r["tier"] for r in rows)
out = []
w = out.append
w("# Master language list — every language a ভাষার দরজা book can be delivered for\n")
w("Generated from `languages/master_languages.csv` by `languages/build_master.py`. Edit the CSV, not this file.\n")
w("## Tiers (honest capability rating)\n")
w("| Tier | Meaning | Count |\n|---|---|---|")
w("| **A** | I can write the whole book (sounds, script, grammar, 2,000-word journey, culture, dawah chapter) to a high standard. The standard human gates (native proofread, Bangla editor, audio) still apply. | %d |" % tiers["A"])
w("| **B** | I can write the whole book well, but there is less reference material, so expect more native-reviewer corrections. Budget a longer review. | %d |" % tiers["B"])
w("| **C** | Possible only with a native co-author. My output would be a structured first draft, not a finished book. | %d |" % tiers["C"])
w("| **Total** | | **%d** |\n" % len(rows))
w("**Not offered:** languages with no settled written standard or very little written material (most of the world's ~7,000 languages, e.g. small oral languages of Papua New Guinea, the Amazon and Central Africa); sign languages (they need video, not print); extinct or liturgical-only languages, apart from Latin and Sanskrit.\n")
w("## Source flags\n")
w("- **R**: already in the ভাষার দরজা roadmap (`SERIES-ROADMAP.md`)\n- **K**: a KDP *Introduction to Arabic* edition exists for it on Drive\n- **S**: in the KDP `SCHEDULE.md` Phase 2 queue\n- **M**: in `KDP-Language-Opportunity-Matrix.csv`\n- **✓**: book built (French)\n")
n = 0
for reg, rs in regions.items():
    w("## %s (%d)\n" % (reg, len(rs)))
    w("| # | Language | বাংলা নাম | Script | Tier | Sources | Note for Bangla readers |\n|---|---|---|---|---|---|---|")
    for r in rs:
        n += 1
        w("| %d | %s | %s | %s | **%s** | %s | %s |" % (n, r["en"], r["bn"], r["script"], r["tier"], r["flags"] or "—", r["note"]))
    w("")
open(os.path.join(HERE, "..", "MASTER-LANGUAGE-LIST.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(rows), dict(tiers))
