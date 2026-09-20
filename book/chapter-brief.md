# Chapter brief for writers (read fully before writing)

You are writing chapters of a practical book: "Build It in Bangla: 103 SaaS Businesses You Can Launch with Claude in 30 to 90 Days". The reader is a founder or small team in Bangladesh (or any non-English market) with little money, who will use Claude (Anthropic's AI) as their engineer, designer, copywriter and analyst. Each chapter must be enough for such a reader to build and launch that business.

Facts for every idea (pitch, wedge, port countries, moat, pricing) are in book/ideas-master.md. Use them. Do not change prices or invent statistics. Where you need a number that is not in the master file, say "roughly" or give a range and keep it plausible.

## Chapter template (use exactly these headings, in this order)

## Idea N: Title
*One-line pitch in italics.*

### Who pays and why now
2 to 3 short paragraphs. Who the customer is in Bangladesh, what they do today, why they will pay, why this moment. Mention port countries in one sentence.

### The product in 30 days (MVP)
- 5 to 7 bullet features, each one line. This is what ships by day 30.
- End with one bullet starting "Leave out:" listing 2 to 4 things not to build yet.

### Data, integrations and the Bangladesh specifics
- 3 to 6 bullets: payment rail (bKash, Nagad, SSLCommerz, Stripe, Lemon Squeezy as relevant), SMS or WhatsApp channel, any local dataset (drug database, tariff schedule, curriculum, etc.), regulatory forms, offline needs, Bangla numerals and fonts where relevant.

### Build it with Claude
A concrete, copyable plan. Include:
- The stack in one line (default: Next.js or Laravel web app, PostgreSQL, Flutter for Android when a field app is needed, Claude API for AI features, Cloudflare or a small VPS, bKash merchant API; change only when the idea needs it).
- Three to five numbered steps. Each step names what to ask Claude for and what the reader does with the answer. At least two steps must contain an actual prompt the reader can paste, written inside a fenced code block, 3 to 8 lines each, specific to this idea (schema, screens, Bangla copy, AI feature, outreach message, etc.).

### Launch in 30, 60, 90 days
A small pipe table with three rows (Day 30, Day 60, Day 90) and two columns (Milestone, Target). Targets are numbers of users, customers, revenue or activity.

### First customers with zero budget
- 4 to 6 bullets. Exactly where these customers gather (Facebook groups by type, associations, Google Maps categories to scrape, markets, WhatsApp communities), the outreach message angle, the demo that closes, and the referral loop.

### Pricing and the maths
- The price plans from the master file.
- One or two sentences on cost of goods (AI, SMS, hosting) and gross margin.
- One sentence: how many paying customers make roughly ৳3 lakh a month for a small team (compute from the mid price).

### Country kit: taking it to other languages
- 3 to 4 bullets: first port and why, what changes (language pack, payment rail, local dataset or integration, reseller), what stays the same.

### Risks and how to de-risk them
- 3 to 5 bullets, each "Risk: ... De-risk: ..." in one line.

## Style rules (strict)
- Plain English, short sentences, active voice. No em-dashes (use commas or full stops). No exclamation marks. No emoji.
- Use ৳ for taka amounts and $ for dollars. Keep the master file's prices.
- Product and company names in English as normal (bKash, Nagad, WhatsApp, Claude, Next.js, Flutter).
- Each chapter 550 to 800 words. Do not pad. Do not add sections.
- Do not mention Rabbit's Hat, the author, or this conversation. Write for any reader.
- Write the chapters for your assigned ideas in numeric order into your assigned English file, starting the file with a single H1 line for the section title given to you, then a two-sentence section intro, then the chapters.

## Bangla version rules
After the English file is complete, write the Bangla file (same path under sections/bn/). This is a faithful, natural translation in standard Bangladeshi business Bangla, not word-for-word. Rules:
- Keep the same headings structure; translate headings (e.g. "কে টাকা দেবে এবং কেন এখনই", "৩০ দিনে পণ্য (MVP)", "ডেটা, ইন্টিগ্রেশন ও বাংলাদেশের বিশেষ দিক", "Claude দিয়ে তৈরি করুন", "৩০, ৬০, ৯০ দিনে লঞ্চ", "শূন্য বাজেটে প্রথম গ্রাহক", "মূল্য ও হিসাব", "কান্ট্রি কিট: অন্য ভাষায় নেওয়া", "ঝুঁকি ও প্রতিকার").
- Use Bangla numerals (০-৯) for numbers in prose and tables, including ৳ amounts; keep digits inside code blocks and prompts in English.
- Keep product names, technical terms and code in English (bKash, WhatsApp, Claude, Next.js, PostgreSQL, API, MVP, SMS). Common tech words may be transliterated where natural (অ্যাপ, ডেটাবেস, সার্ভার).
- Keep the prompts inside code blocks in English exactly as in the English file (a builder pastes them into Claude), but add one Bangla line above each code block saying what it is for.
- Same length and completeness as English. Do not summarise.
- Write the Bangla file in several appends (one or two chapters per write) so no single write is huge.
