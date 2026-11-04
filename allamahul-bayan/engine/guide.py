# -*- coding: utf-8 -*-
"""Writes the per-book KDP-PUBLISHING-GUIDE.md (metadata to paste into KDP)."""
from series import SERIES


def write(L, path, pages, spine, W):
    K = L["kdp"]
    cost = 1.00 + 0.012 * pages
    roy = lambda p: 0.6 * p - cost
    bullets = "\n".join(f"<li>{b}</li>" for b in K["desc_bullets"])
    kw = "\n".join(f"  {i}. {k}" for i, k in enumerate(K["keywords"], 1))
    cats = "\n".join(f"  {i}. {c}" for i, c in enumerate(K["categories"], 1))
    txt = f"""# KDP Publishing Guide — {L['title']} ({SERIES['name']}, Book {L['series_no']})

Upload files (both in `output/`):

| File | What it is | Spec |
|---|---|---|
| `interior.pdf` | Manuscript (interior) | {pages} pages · 8.5 × 11 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | Full-wrap paperback cover | {W:.4f} × 11.25 in · 0.125 in bleed · spine {spine} in ({pages} pp × 0.002252, white paper) |

## 1. Paperback details

- **Language:** English · **Book title:** {L['title']}
- **Subtitle:** {L['subtitle']}
- **Series:** {SERIES['name']} — **Series number:** {L['series_no']} · **Edition:** 1
- **Author:** {SERIES['author']} · **Contributors:** none (the AI assistance is declared in the AI-content questions)
- **Description** (HTML box):

```html
<p><b>Color your way into {L['name']} — one letter at a time!</b></p>
<p>{K['desc_intro']}</p>
<ul>
{bullets}
<li><b>Single-sided coloring pages</b>, so markers never spoil the next picture, and a <b>certificate</b> to cut out and frame</li>
</ul>
<p>All pictures show objects, plants and nature only, which makes the book suitable for Muslim homes, schools and madrasas.</p>
<p><b>The Allamahul Bayan Series</b> takes its name from Surah Ar-Raḥmān: <i>“He taught him clear expression”</i> (55:4). Each book helps children thank Allah for the gift of language by meeting a new one: its letters, its sounds and the people who speak it.</p>
<p>Perfect for ages 3–7, heritage-language families, homeschoolers and teachers.</p>
```

- **Reading age:** 3 to 7 · **Primary marketplace:** {K['market']}
- **Categories:**
{cats}
- **Keywords** (7 boxes):
{kw}

## 2. Paperback content

- Black & white interior · **White** paper · Trim **8.5 × 11 in** · **No bleed** · Matte cover
- Manuscript: `output/interior.pdf` · Cover: "Upload a cover you already have" → `output/cover.pdf`
- Blank pages flagged by the previewer are the intentional backs of the coloring pages.
- **ISBN:** a free KDP ISBN shows the imprint as "Independently published". To show
  **{SERIES['publisher']}**, use your own ISBN (Bangladesh: National ISBN Agency, Archives & Libraries
  Directorate), put it in `isbn` in `languages/{L['code']}.py` and rebuild.

## 3. AI-generated content disclosure

Images: **AI-generated** (line art made with AI assistance, reviewed by the author).
Text: **AI-generated**, with substantial human editing.

## 4. Pricing (verify in KDP's calculator)

Printing ≈ **US ${cost:.2f}** ($1.00 + {pages} × $0.012). At **$8.99** royalty ≈ **${roy(8.99):.2f}**; at **$9.99** ≈ **${roy(9.99):.2f}**.

## 5. Must-do before publishing

1. A ḥāfiẓ or scholar checks the Qur’an text on pages 4–5.
2. **A native {L['name']} speaker proofreads every letter name, sound guide, word, transliteration and phrase.**
   {L.get('review_note', '')}
3. Order a printed proof copy.
"""
    open(path, "w", encoding="utf-8").write(txt)
