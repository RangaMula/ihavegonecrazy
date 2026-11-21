# Publishing guide — Muwatta Imam Malik: Arabic–Japanese Bilingual Edition, Volume 1: The Times of Prayer

**Publisher:** Maktabatu Kunujul Akhirah (an imprint of the Kunujul Akhirah Charitable Trust) · **Editor:** Hafez Abdullah Muhammad Minhaz Reza ·
**Copyright:** © 2026 Maktabatu Kunujul Akhirah. All rights reserved.

## Before you upload

- [ ] scholarly review: set `reviewed_by` in every translations/ja/book-NN.json of this volume
- [ ] paperback ISBN in standard/publishing.json (or use the store's free ISBN, see the guide)
- [ ] eBook ISBN (optional for most eBook stores, see the guide)

The files below are already in their final store format. When the items above are done, rebuild with
`python3 tools/build_release.py ja --volume 1`: the ISBNs appear on the copyright page, an EAN-13 barcode is drawn on
the back cover, and the review-draft notices disappear once every book of the volume has `reviewed_by`.

## Files

| File | Use | Spec |
|---|---|---|
| `interior.pdf` | paperback interior (KDP, IngramSpark, Lulu, local printers) | 34 pages · 6 × 9 in · no bleed · black & white · fonts embedded |
| `cover.pdf` | paperback full-wrap cover | 12.3266 × 9.25 in · 0.125 in bleed · spine 0.0766 in (34 pp × 0.002252, white paper) · barcode area 2 × 1.2 in at the bottom right of the back |
| `ebook.epub` | eBook (Kindle via KDP, Google Play Books, Apple Books, Kobo, Draft2Digital) | EPUB 3, validated with EPUBCheck, fonts embedded (Japanese text uses the reader’s own fonts) |
| `ebook-cover.jpg` | eBook cover | 1600 × 2560 px |
| `metadata.json` | every listing field below, machine-readable | |

## ISBNs (space is reserved)

- Each **format** needs its own ISBN: paperback, eBook, and hardcover if you make one. Each language edition and each volume also needs its own.
- To show **Maktabatu Kunujul Akhirah** as the publisher everywhere, buy ISBNs in the publisher's name. In Bangladesh they come from the
  National ISBN Agency (Archives & Libraries Directorate). Enter them in `standard/publishing.json` → `editions.ja.isbn`.
- KDP and IngramSpark offer free ISBNs, but KDP's then lists the imprint as "Independently published" and can only be used on Amazon.
  Google Play Books, Apple Books and Kobo do not require an ISBN for eBooks.
- KDP adds the barcode itself if you leave the white box empty. IngramSpark needs the barcode on the cover, so enter the ISBN and rebuild.

## Listing details (all stores)

- **Title:** イマーム・マーリクの『ムワッタア』
- **Subtitle:** アラビア語・日本語対訳 — 第1巻: 礼拝の時刻の書
- **English title (for international listings / IngramSpark):** Muwatta Imam Malik: Arabic–Japanese Bilingual Edition, Volume 1: The Times of Prayer
- **Series:** 『ムワッタア』対訳シリーズ · **Number:** 1 · **Edition:** 1
- **Contributors:** Author — Imam Malik ibn Anas · Editor — Hafez Abdullah Muhammad Minhaz Reza
- **Publisher / imprint:** Maktabatu Kunujul Akhirah
- **Language:** Japanese (with Arabic) · **Audience:** adult / general
- **Copyright:** © 2026 Maktabatu Kunujul Akhirah. All rights reserved. · **Publishing rights:** "I own the copyright and hold the necessary publishing rights" — the
  Arabic original is public domain; the translation, pronunciation, notes and design belong to the publisher.
- **Categories (BISAC):**
- REL037020 RELIGION / Islam / Koran & Sacred Writings
- REL037030 RELIGION / Islam / Law
- REL037040 RELIGION / Islam / Rituals & Practice
- **Keywords (KDP has 7 boxes):**
1. ムワッタア
2. ハディース 日本語訳
3. イスラーム法
4. マーリク派
5. アラビア語 対訳
6. 礼拝 イスラーム
7. muwatta japanese
- **Description:** `description_html` in `metadata.json` (in Japanese); `description_en_html` for English-language stores.
- **AI disclosure (KDP asks this):** Text — **AI-generated** (the translation from Arabic was made with AI assistance), edited by the
  editor and checked by the named scholarly reviewer. Images — none (cover is typographic).
- **Suggested prices:** {"paperback_jpy": 1980, "ebook_jpy": 800, "paperback_usd": 12.99, "ebook_usd": 4.99} — check each store's printing-cost calculator first.

## Store by store

1. **Amazon KDP** (kdp.amazon.com), for the paperback and the Kindle eBook on every Amazon marketplace.
   - Paperback: black & white interior, white paper, 6 × 9 in, no bleed, matte cover. Upload `interior.pdf` and `cover.pdf`.
     Turn on **Expanded Distribution** for bookstores and libraries, unless you use IngramSpark.
   - Kindle eBook: upload `ebook.epub` and `ebook-cover.jpg`. Choose worldwide territories (you hold worldwide rights).
   - Check that Japanese is on KDP's current list of supported languages for each format. Where a format is not supported, sell it
     through the stores below.
2. **IngramSpark** (ingramspark.com), for the paperback (and hardcover) in bookstores worldwide (40,000+ retailers and libraries).
   - Upload the same `interior.pdf`. Make the cover with IngramSpark's cover template generator for the exact page count, or reuse
     `cover.pdf` if its spine matches their calculator.
3. **Google Play Books** (play.google.com/books/publish): upload `ebook.epub` and the cover JPG. Sold in 75+ countries.
4. **Apple Books** (authors.apple.com): upload `ebook.epub` with Apple Books for Authors.
5. **Kobo Writing Life** (kobo.com/writinglife): upload `ebook.epub`. This reaches Rakuten Kobo, including Japan.
6. **Draft2Digital** (draft2digital.com), optional: one upload of `ebook.epub` distributes to many smaller stores and libraries.
7. **Amazon.co.jp** is covered by KDP; also consider **BookWalker** and **honto** for Japanese eBooks (through a distributor that accepts EPUB).

## Proof before release

1. Order one printed proof from KDP (or IngramSpark) and read it cover to cover.
2. Open `ebook.epub` in Kindle Previewer (Amazon's free tool) and in Apple Books or Thorium Reader. Check the Arabic,
   the Japanese text, the pronunciation line and ﷺ.
