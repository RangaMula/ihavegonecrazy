# Build It in Bangla

## 103 SaaS Businesses You Can Launch with Claude in 30 to 90 Days

*A practical playbook for founders in Bangladesh and every other market the English-only software world forgot.*

First edition, September 2026

---

# How to use this book

This book has three parts.

Part 1 is the method. It explains why software built first in Bangla, or in any native language, wins markets that global products ignore, how to turn one product into many countries with a "country kit", how to build with Claude as your engineer in 30 to 90 days, what accounts and tools you need, how to find customers with no marketing budget, and how to price. Read it once, fully, before you build anything.

Part 2 is the catalogue: 103 business ideas in 14 sections. Every idea uses the same template, so you can compare them quickly. Each chapter tells you who pays, what to ship by day 30, what data and integrations you need in Bangladesh, exactly what to ask Claude for, a 30-60-90 day launch table, where the first customers are, the pricing maths, how to take the product to other languages, and the risks.

Part 3 helps you choose. It has a scoring sheet, a list of natural product bundles, and the full index of ideas.

Do not read Part 2 from start to finish. Skim the section titles, mark ten ideas that match your background or your network, read those ten chapters properly, score them with the sheet in Part 3, and build one.

A word on the numbers. Prices are in Bangladeshi taka (৳) unless stated in dollars. They are indicative, chosen so that a small team can reach a comfortable income from a few hundred customers. Market sizes are described in ranges and rough counts, because precise figures change and the point is the order of magnitude, not the decimal.

---

# Part 1: The Method

## Chapter 1: Why native-language software wins

The global software industry is built in English, priced in dollars, and designed around bank cards. That is fine for about a fifth of the world. Everyone else adapts, avoids, or goes without.

In Bangladesh a shop owner runs sales through bKash, keeps a khata for dues, sells on Facebook, and talks to customers on WhatsApp. Every one of those habits is invisible to a product designed in San Francisco. The same is true for a pharmacy in Lahore, a coaching centre in Jakarta, a wholesaler in Lagos, and a tailor in Cairo. They are not underserved because they are poor. They are underserved because nobody built for how they actually work.

That is the opportunity. A product that speaks the customer's language, accepts the customer's money, and matches the customer's daily routine has almost no competition in these markets, and the customers are not small in number. Bangladesh alone has several million small businesses, hundreds of thousands of NGOs, mosques, schools and committees, and a diaspora of millions who send money and instructions home every month.

Three things changed recently that make this the right moment.

First, AI. Claude and models like it can write the code, the copy, the translations, and the customer support. A five-person team can now ship what needed thirty people five years ago.

Second, mobile money. bKash, Nagad, M-Pesa, JazzCash and their peers give every business a payment rail with an API. You can bill a customer in taka without a bank card.

Third, global billing. Stripe and Lemon Squeezy let a company registered anywhere sell to the world, handle sales tax, and get paid in dollars. The same product can charge a shop in Khulna ৳499 and an agency in Ohio $49.

The ideas in this book all follow one rule: win in Bangla first, because that is where you understand the customer, then ship the same product to every other language that global software forgot.

## Chapter 2: The country kit

A country kit is the small set of things you change when you take a product to another language and market. If the kit is small, your five-person team can add a country in weeks. If the kit is large, you have built a product that only works in one place.

A country kit has four parts.

1. **Language pack.** Every string in the interface, every notification template, every report, every help page. Build the product multilingual from day one with a translation file, never with text inside the code. Numbers, dates and currency symbols come from the language pack too. Bangla uses its own numerals; Urdu and Arabic read right to left.
2. **Payment rail.** bKash and Nagad in Bangladesh, JazzCash in Pakistan, M-Pesa in Kenya, Paystack in Nigeria, Xendit in Indonesia. Keep the billing core on Stripe or Lemon Squeezy so cards work everywhere, and plug the local wallet in as a payment method.
3. **The two local integrations that matter.** For a pharmacy tool that is the drug database. For an import tool it is the tariff schedule. For a coaching tool it is the curriculum. For a seller tool it is the courier companies. Name them before you start. If a product needs more than two or three, it will be slow to port.
4. **One reseller.** A local accountant, agency, association or consultant who earns 25 to 30 percent and brings the first fifty customers. You cannot sell door to door in a country you do not live in.

Everything else stays the same: the code, the database, the AI features, the onboarding, the pricing structure. Price in the local currency at roughly one hour of the customer's revenue per month. That rule holds from Dhaka to Nairobi.

The first port for a Bangla product needs no new language at all. West Bengal in India and the Bangladeshi diaspora in the UK, the Gulf, the US and Malaysia are Bangla-speaking markets with different payment rails. Start there.

## Chapter 3: The 30 to 90 day method

You will use Claude as your engineer, designer, copywriter, translator and analyst. That does not mean you type "build me an app" and wait. It means you work in short, specific steps and you review everything. Here is the calendar that every idea in Part 2 assumes.

**Days 1 to 5: Decide and define.** Pick one idea. Talk to ten people who fit the customer description; WhatsApp calls are fine. Write down what they do today, what they hate, and what they would pay. Ask Claude to turn your notes into a one-page product definition: the customer, the five features that matter, what is deliberately left out, and the pricing. Do not skip the ten conversations. Everything else depends on them.

**Days 6 to 10: Design the data and the screens.** Ask Claude for the database schema, the list of screens, and the flow between them. Ask it to draw each screen in words, then generate simple HTML mockups. Show the mockups to three of your ten people. Fix what confuses them.

**Days 11 to 25: Build the MVP.** Set up the stack from Chapter 4. Work feature by feature. For each one, ask Claude for the code, run it, test it with real data, and ask Claude to fix what breaks. Keep the Bangla text in a translation file from the first day. Add payments in the third week. Add the AI feature, if the idea has one, in the fourth week, after the plain workflow works.

**Days 26 to 30: Onboard the first five customers by hand.** Sit with them, on the phone or in the shop. Enter their data yourself. Watch what they do. Do not charge them yet. Fix the three biggest problems.

**Days 31 to 60: Sell to the first fifty.** Start the zero-budget channels from Chapter 5. Charge from customer six onwards. Use Claude to write every outreach message, every help article, every reply. Ship a fix or an improvement every week and tell your customers about it in their language.

**Days 61 to 90: Make it repeatable.** Write the onboarding so a new customer can start without you. Add the reseller plan. Record a five-minute Bangla demo video. Prepare the first country kit. By day 90 the goal is one hundred paying customers, or twenty if the product is high-ticket, and a clear view of the next ninety days.

Three rules keep this on track. Ship something usable every single week. Never build a feature that a paying customer has not asked for. Keep a written log of every decision, because the log is what you will hand to Claude when you ask it to write the next feature.

## Chapter 4: The standard stack and the accounts you need

Most ideas in this book use the same stack. Change it only when a chapter says so.

| Layer | Default choice | Why |
|---|---|---|
| Web app | Next.js (or Laravel if your team knows PHP) | Fast to build, easy to host, Claude writes it well |
| Database | PostgreSQL (Supabase or a managed instance) | Reliable, handles money correctly, free tier to start |
| Mobile | Flutter for Android first, iOS later | One codebase, good Bangla text rendering, offline support |
| AI | Claude API with structured outputs | Reads receipts and documents, classifies, drafts Bangla text, powers chat |
| Hosting | Cloudflare Pages or a small VPS in Singapore | Cheap, close to Bangladesh, easy to scale later |
| Local payments | bKash merchant API, Nagad, SSLCommerz or aamarPay for cards | Customers pay how they already pay |
| Global payments | Stripe for cards and subscriptions; Lemon Squeezy as merchant of record when you sell outside your home country | Tax handled, dollars in |
| Messaging | An SMS gateway (any licensed Bangladesh aggregator), WhatsApp Business API through a provider, Telegram bot where useful | Customers live on their phones |
| Files | Object storage (Cloudflare R2 or S3) | Photos and documents are most of your data |

Accounts to open before day 11, because some take weeks:

- A bKash merchant account, or a payment gateway that includes bKash and Nagad, for taka billing.
- A Stripe account and, if you sell abroad, Lemon Squeezy. Both need a registered company; a US or UK entity is the common choice for founders who want global reach, and it works fine alongside a Bangladeshi company.
- An SMS gateway account with sender ID approval.
- WhatsApp Business API access through a provider, which needs Meta business verification.
- A Google Play developer account for the Android app. Organisation accounts now need a company identifier, so apply early.
- A domain, a business email, and a separate domain for outreach email so your main domain's reputation stays clean.

Money rules that save you later: store all amounts as integers in the smallest unit (paisa, cents). Keep every automated action with its source and timestamp. Back up the database daily and test the restore once.

## Chapter 5: Customers with no marketing budget

Every idea in this book assumes you have no money for advertising. That is not a handicap if you use the channels that actually work for small businesses in Bangladesh and markets like it.

**Google Maps as your customer list.** Almost every business you want is on Google Maps with a category, a phone number, a review count and often a website field. Build a list per city and category. Use it to find who has no website, who has unanswered reviews, who is open and active. Use it for outreach by WhatsApp and email, and use it to pre-build something for them (an audit, a page, a quote) so the first message shows value, not a pitch. Be careful: bulk scraping breaks Google's terms, so do it from disposable infrastructure, never from accounts tied to your company, and keep only business data, never personal data.

**Facebook groups.** Bangladesh's business conversations happen in Facebook groups: sellers, importers, pharmacists, tutors, farmers, freelancers. Join the groups for your customer. Post useful things weekly, in Bangla, with screenshots. Answer questions. Never spam. One genuinely helpful post a week beats a hundred ads.

**Associations and committees.** Every trade has one: pharmacy owners, transport owners, coaching centres, market committees, garment subcontractors. One presentation to a committee reaches hundreds of members, and the committee's endorsement is worth more than any advertisement.

**Search and AI answers.** People search in Bangla for how to do things, and get bad answers. Write the good answer. Build pages for every common question in your niche, in Bangla and English, with clear structure so search engines and AI assistants can quote them. This is called answer engine optimisation, and it compounds for years.

**Email outreach, done right.** Business-to-business cold email is legal in the United States and most of Asia with a real address and an opt-out. It is far stricter in Europe. Use a separate sending domain, warm it up for three weeks, send fewer than fifty a day per address, personalise every message with something true about the business, and make the first message useful.

**Resellers.** Accountants, agencies, consultants and shop-supply distributors already visit your customers. Give them 25 to 30 percent and a dashboard. They will sell for you in places you will never visit.

**The referral loop.** Build sharing into the product: a customer's own customers see your name on an SMS, a receipt, a report or a status page. Give the customer a reason to invite others, such as a free month for every referral that pays.

## Chapter 6: Pricing and the maths of a small team

A five-person team in Dhaka needs roughly ৳3 lakh a month to be comfortable, which is about $2,500. Every chapter in Part 2 tells you how many customers at the mid price reach that number. Most ideas need 100 to 300 paying customers. High-ticket ideas need 20 to 40. That is the entire financial plan for your first year.

Pricing rules that work in these markets:

- Price at roughly one hour of the customer's monthly revenue. A tailor pays ৳300, a jeweller pays ৳3,000, a developer pays ৳10,000.
- Offer a free tier that solves one real problem, then a paid tier that saves the customer money or time visibly. The upgrade should feel obvious, never forced.
- Bill yearly with two months free. Cash today is worth more than a promise of twelve payments.
- Add a lifetime option only for products with near-zero recurring costs, and cap how many you sell.
- Charge per seat, per site, per employee or per location when the customer's own size grows, so your revenue grows with them.
- Keep global prices around three to four times local prices. The product is the same; the customer's revenue is not.

Cost of goods stays low in all these businesses. A Claude call to read a receipt or draft a reply costs a fraction of a taka. An SMS costs about a third of a taka. Hosting for the first thousand customers costs less than one customer pays. Gross margins above 80 percent are normal, which is why a small team can live on a few hundred customers.

## Chapter 7: The Claude prompt pack

These ten prompts are used across every chapter. Copy them, fill in the brackets, and paste them into Claude. Always give Claude your decision log and your customer notes first, so it works from facts.

**1. Product definition**
```
You are my product manager. Here are my notes from ten customer conversations: [paste notes].
Write a one-page product definition for [idea] in Bangladesh: the customer, their current
workaround, the five features that matter most, what we deliberately leave out for the first
version, and a pricing table in BDT with a free tier. Be specific and short.
```

**2. Database schema**
```
Design a PostgreSQL schema for [product]. Entities: [list]. Money is stored as integer paisa.
Every table has created_at, updated_at and an organisation_id for multi-tenant isolation.
Include an audit_log table. Output SQL with comments, then a one-paragraph explanation.
```

**3. Screens and flow**
```
List every screen for the [product] Android app and web dashboard. For each screen give the
purpose, the fields, the primary button, and what happens next. Bangla is the default
interface language; give the Bangla label for every button and field next to the English.
```

**4. Feature code**
```
Implement [feature] in [Next.js / Flutter]. Context: schema is [paste], the screen is [paste].
Requirements: [list]. Use a translation file for all text with keys in English and values in
Bangla and English. Write the code, then the test cases, then a checklist for me to verify.
```

**5. Bangla interface copy**
```
Translate this interface text into natural Bangladeshi Bangla for a [type of user], polite but
short. Keep product names in English. Return a JSON file with the original English keys.
Text: [paste].
```

**6. AI extraction feature**
```
Write a prompt and a JSON schema for extracting [fields] from a photo of a [receipt / invoice /
form] that may be in Bangla, English or both, with Bangla numerals. Include a confidence score
per field and a rule that anything under 0.8 goes to a review queue. Then write the code that
calls the Claude API with structured outputs and saves the result.
```

**7. Outreach message**
```
Write a WhatsApp message in Bangla, under 60 words, to the owner of [business type] in
[city]. I have noticed [true, specific observation from their listing]. Offer [free thing]
and ask for a reply, no link in the first message. Give three variants.
```

**8. Help article and answer pages**
```
Write a help article in Bangla and English titled "[question customers ask]". Structure it
with a direct answer in the first two sentences, then steps, then a short FAQ. Add schema.org
FAQ markup so search engines and AI assistants can quote it.
```

**9. Pricing page**
```
Write the pricing page for [product] with these plans: [paste]. Explain each plan in one
sentence a shop owner understands. Bangla first, English toggle. Add a comparison table and
three short customer objections with answers.
```

**10. Country kit checklist**
```
We are taking [product] from Bangladesh to [country]. List everything that must change:
language and script, numerals and dates, currency and payment rail, the local datasets or
integrations we need, legal or regulatory forms, and the type of reseller to recruit. Mark
each item as one day, one week, or one month of work.
```

## Chapter 8: Company, payments and the rules

You can start with a Bangladeshi sole proprietorship and a bKash merchant account. When you want to sell abroad, a US or UK company gives you Stripe, Lemon Squeezy and a dollar bank account. Many founders run both: the foreign company owns the software and bills global customers, the local company employs the team and bills local customers.

Stripe accepts a sole proprietor with a personal tax number and a registered company with its tax ID. Lemon Squeezy acts as merchant of record, meaning it is the legal seller and handles sales tax and VAT everywhere, in exchange for a higher fee. Use it for global sales until your volume justifies handling tax yourself.

Three rules to respect from the first day. Keep customer data in your own database with backups, and tell customers what you store. Do not scrape or store personal data of individuals; business listings are fine. Send SMS and email only to people who have a business relationship with you or with your customer, and always include a way to stop.

None of this is legal advice. Spend one hour with a local accountant and one with a lawyer before you take your first payment.
