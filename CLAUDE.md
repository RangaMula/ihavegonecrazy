# ভাষার দরজা — language book series (Maktabatu Kunujul Akhirah)

This repo produces one Bangla-instruction language book per language for adult readers.

**Before doing anything, read `series-standard/PLAYBOOK.md`.** It holds the author's decisions, the production
workflow, how to brief agents, the data formats, the layout engine rules, the lessons learned and the QA checklist.

Quick facts:
- Spec: `series-standard/BOOK-STRUCTURE.md` · book order: `series-standard/SERIES-ROADMAP.md` · vocabulary design: `series-standard/vocabulary/WORD-JOURNEY.md`
- Reference implementation: `books/fr-2e/` (compact layout, preferred). `books/fr/` is the 1st edition, kept for comparison.
- Publisher spelling: «মাকতাবাতু কুনুজুল আখিরাহ». The author's foreword is Bangla-only and identical in every book.
- Build a book: `cd books/<code> && ./make.sh out.pdf` → must print `no overflow`.
- Commit and push after every meaningful step, and tell the author what was saved.
