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


---

# Section 1: Local Business and Commerce (Part 1)

Every shop, clinic, salon and Facebook page in Bangladesh already sells, but almost none has software for the customer side of the business: being found, answering messages, taking orders and bringing people back. The seven ideas in this section attack that gap one channel at a time, from Google Maps to WhatsApp to the phone line to the SMS inbox, and each can be built by a small team with Claude in under 90 days.

## Idea 1: Local Business AI Presence
*Audit and auto-manage a local business's Google listing, give it a one-page website, and report its rank on Google Maps and in AI answers.*

### Who pays and why now
The customer is the owner of a pharmacy, restaurant, clinic or coaching centre who has a Google Maps listing but never looks at it. Reviews go unanswered, hours are wrong, there is no website. The owner has no idea whether they appear when someone in Barishal searches "pharmacy near me".

They pay because being invisible costs customers every day and nobody serves them at their price. Dhaka agencies charge ৳15,000 a month and ignore single pharmacies.

The moment is now because search is moving into AI answers built from structured web data, which almost no small business here has. The idea ports to any country and language, and agencies will white-label it.

### The product in 30 days (MVP)
- Free audit page: enter a business name, get a scored report on reviews, photos, hours and website.
- Connect the Google Business Profile with one login; AI replies to reviews in Bangla or English, approved by tap or auto-posted.
- Weekly Google post generated from a short owner note or product photo.
- One-page AEO-ready website generated from the listing, with schema markup, on a subdomain.
- Weekly rank report: Google Maps position for 5 keywords in the business's area.
- Leave out: multi-location dashboards, Facebook posting, paid ads, custom domains.

### Data, integrations and the Bangladesh specifics
- Google Business Profile API for reviews and posts; Google Places API for audits of unclaimed listings.
- Rank tracking by geo-grid search on Google Maps from a scheduled worker.
- bKash merchant API for local plans, Lemon Squeezy for agencies abroad; reports by WhatsApp in Bangla.

### Build it with Claude
Stack: Next.js, PostgreSQL, a Node worker for scraping and posting, Claude API, Cloudflare Pages, bKash merchant API.

1. Ask Claude for the data model and audit scoring, and paste it in as your first migration.
```
Design a PostgreSQL schema for a Google Business Profile management SaaS: businesses,
owners, subscriptions, reviews, review_replies, posts, rank_checks (keyword, grid point,
position, date). Add a 0 to 100 audit score from review count, unanswered reviews,
rating, photos, hours, website. Return SQL plus TypeScript.
```
2. Ask Claude for the audit page, Google OAuth connect flow and the review reply prompt.
```
Write a system prompt for an assistant replying to Google reviews for a small business
in Bangladesh. Reply in the review's language, under 60 words, thank by name, never
argue, apologise on 1 or 2 stars and invite a call to the shop. Warm shopkeeper voice,
no emoji. Include 3 example reviews and replies, one in Bangla.
```
3. Ask Claude for a one-page site template with JSON-LD LocalBusiness schema, Bangla fonts and a WhatsApp button.
4. Ask Claude for the scraper that lists businesses by city and category and pre-builds a private audit page for each.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 500 pre-built audit pages, 5 paying |
| Day 60 | 3,000 audit pages, 40 paying, 2 agencies on trial |
| Day 90 | 100 paying customers, 3 agencies, roughly ৳1 lakh a month |

### First customers with zero budget
- Scrape Google Maps for pharmacies, restaurants and diagnostic centres in two cities; build each audit page before contacting anyone.
- WhatsApp angle: "Your pharmacy has 14 unanswered Google reviews and the wrong closing time. Here is your free report."
- Facebook groups for restaurant, pharmacy and clinic owners, posting the free audit.
- The demo that closes: show the owner their listing beside a competitor's, then post one AI reply live.
- Referral loop: every generated site links to "Get your page"; agencies earn 20 percent recurring.

### Pricing and the maths
- Free audit; Starter ৳499/month ($19); Pro ৳1,499 ($49); Agency ৳4,999 ($149).
- Cost of goods is roughly ৳40 to ৳80 per business a month for AI, rank checks and hosting; gross margin stays above 85 percent.
- At the mid Pro price of ৳1,499, roughly 200 paying customers bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: English-speaking markets through agencies, because the product is identical and agencies pay in dollars.
- What changes: language pack for replies and posts, payment rail (Lemon Squeezy or Stripe), local keyword set.
- What stays the same: audit engine, Google integration, generated site and scraper.

### Risks and how to de-risk them
- Risk: Google restricts the Business Profile API. De-risk: keep replies working through the owner's own login.
- Risk: owners do not trust auto-replies. De-risk: default to approve-by-tap for two weeks, then offer auto mode.
- Risk: churn from businesses that see no new customers. De-risk: send the weekly rank report by WhatsApp so the value is visible.

## Idea 2: WhatsApp AI Receptionist and Booking
*An AI that answers customer messages on WhatsApp, Messenger and Instagram in Bangla or English, books appointments, sends reminders and collects reviews.*

### Who pays and why now
The customer is a dentist, skin clinic, salon, private tutor or physiotherapist. Patients message them on WhatsApp and Messenger at all hours. The owner replies between appointments, misses half the messages and loses bookings.

They pay because every missed message is a missed ৳500 to ৳3,000 appointment, and a receptionist costs ৳12,000 a month and still sleeps at night. Two saved bookings a month pay for the subscription.

Now is the moment because the WhatsApp Business API is open to small businesses through official providers and Claude handles mixed Bangla and English well. It ports globally through the same API.

### The product in 30 days (MVP)
- Connect one WhatsApp Business number and one Facebook page inbox.
- AI answers from a business profile: services, prices, hours, location, in the customer's language.
- Booking flow: the AI offers free slots from the calendar, confirms, and writes the appointment to the dashboard.
- Reminders the day before and two hours before, with reply options to cancel or reschedule.
- Owner dashboard: today's bookings, open chats, a "take over" button; review request after each visit.
- Leave out: Instagram DMs, payments in chat, multi-branch routing, voice notes.

### Data, integrations and the Bangladesh specifics
- WhatsApp Business API through an official provider; Meta business verification takes one to three weeks, so start on day one.
- Meta charges per conversation, so track counts per customer and cap conversations per plan.
- bKash merchant API for subscriptions; SMS fallback for customers without WhatsApp; Eid closures entered in Bangla.

### Build it with Claude
Stack: Next.js dashboard, PostgreSQL, a Node webhook service for Meta messages, Claude API with tool use, bKash merchant API.

1. Ask Claude for the schema and message flow first.
```
Design a PostgreSQL schema for a WhatsApp and Messenger AI receptionist for clinics
and salons: businesses, channels, staff, services, availability_rules, appointments,
conversations, messages, reminders. Then describe a Node webhook flow: receive Meta
message, load conversation, call Claude with tools (check_slots, book_appointment,
handoff_to_owner), send reply.
```
2. Ask Claude for the receptionist system prompt with tool definitions, then test from your own number in Bangla and Banglish.
```
Write a system prompt for a WhatsApp receptionist for a dental clinic in Dhaka.
Greet in the customer's language, answer only from the clinic profile provided, never
give medical advice, offer at most three free slots using check_slots, confirm name and
phone before book_appointment, call handoff_to_owner if the customer is upset or asks
about unlisted prices. Replies under 50 words. One example dialogue in Bangla.
```
3. Ask Claude for the dashboard screens and the reminder scheduler with Meta template messages, submitted for approval early.
4. Ask Claude for a Bangla onboarding checklist covering Meta verification.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 clinics or salons on trial, 200 conversations handled |
| Day 60 | 20 paying customers, 1,000 bookings made by the AI |
| Day 90 | 60 paying customers, roughly ৳1 lakh a month |

### First customers with zero budget
- Facebook groups for dentists, dermatologists and salon owners.
- Google Maps: scrape dental and skin clinics, salons and physiotherapy centres in Dhaka and Chattogram that list a WhatsApp number.
- Outreach angle: message the clinic's WhatsApp at 10 pm. Next morning: "Your clinic took 11 hours to reply to me. Here is what my receptionist would have said."
- The demo that closes: set up their profile in 15 minutes and let the owner message the number themselves.
- Referral loop: every reminder ends with "Booking by [product]"; one month free per referred clinic.

### Pricing and the maths
- ৳999 to ৳2,999/month ($29 to $79), tiered by monthly conversations.
- Cost of goods is roughly ৳150 to ৳400 per customer a month for Meta fees, AI and hosting; gross margin is around 75 to 85 percent.
- At the mid price of ৳1,999, roughly 150 paying customers bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: a heavy WhatsApp market such as Pakistan, Indonesia or Egypt, because the Meta integration is identical.
- What changes: the receptionist language pack, payment rail (JazzCash, GoPay, Fawry or Stripe), local holidays.
- What stays the same: webhook service, booking engine, dashboard and reminders. A local reseller handles onboarding.

### Risks and how to de-risk them
- Risk: Meta verification delays block onboarding. De-risk: start with Messenger and move to WhatsApp once verified.
- Risk: the AI gives medical advice or wrong prices. De-risk: answer only from the profile and hand off everything else.
- Risk: owners keep replying by hand and see no value. De-risk: send a weekly summary of bookings made while they slept.

## Idea 3: QR Menu and WhatsApp Ordering
*A digital menu or catalogue behind a QR code, with orders placed on WhatsApp and paid by cash on delivery or bKash, for restaurants and shops.*

### Who pays and why now
The customer is a restaurant, cafe, sweet shop or grocery that hands out a laminated paper menu and takes orders by phone. Prices change, the menu does not. Phone orders get misheard and nobody records who ordered what.

They pay because a QR menu costs less than reprinting paper, WhatsApp orders arrive in writing with the customer's number attached, and that list becomes a base for repeat offers. One extra order a week covers the price.

The moment is now because every customer has WhatsApp and a camera, and this four-week build opens the door to selling the receptionist and loyalty products in this section. It is commoditised worldwide, so speed and local payments are the game, and it ports anywhere.

### The product in 30 days (MVP)
- Menu builder: categories, items, photos, prices, variants, availability toggle, in Bangla and English.
- Public menu page per business with a printable QR code and table numbers.
- Order flow: customer picks items, adds address and notes, taps "Order on WhatsApp", and a pre-filled message opens.
- Owner order board: incoming orders, accept or reject, mark delivered, daily totals.
- bKash payment link on the order confirmation, or cash on delivery.
- Leave out: rider tracking, kitchen display screens, table reservations, multi-branch menus.

### Data, integrations and the Bangladesh specifics
- WhatsApp click-to-chat links need no API approval; upgrade to the Business API only for automated confirmations.
- bKash payment links and Nagad as the second option; SSLCommerz for card payments at larger restaurants.
- Bangla numerals and fonts on the menu, and a light page that loads on 3G in a district town.

### Build it with Claude
Stack: Next.js web app with server-rendered public pages, PostgreSQL, Cloudflare for hosting and image storage, bKash payment links.

1. Ask Claude for the schema and public menu page, and deploy a menu for a restaurant you know within a week.
```
Design a PostgreSQL schema for a QR menu and WhatsApp ordering SaaS in Bangladesh:
businesses, menu_categories, menu_items (name_bn, name_en, price, variants, photo,
available), tables, orders, order_items, payments (cod, bkash). Then write a Next.js
public menu page that renders fast on 3G and builds a WhatsApp click-to-chat URL
with the order summary in Bangla.
```
2. Ask Claude for the owner dashboard: menu editor, order board and daily totals, in Bangla.
3. Ask Claude for the order message template and Bangla customer copy.
```
Write the WhatsApp order message a customer sends to a restaurant in Bangladesh from a
QR menu. Include items with quantity and price, delivery address, notes, total, and
a bKash payment line. Keep it under 12 lines, in Bangla with numbers in English digits.
Then write the restaurant's confirmation reply in Bangla, friendly, under 40 words.
```
4. Ask Claude for a printable QR flyer and table tent so setup takes ten minutes.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 menus live, 100 orders placed through them |
| Day 60 | 40 paying businesses, 1,500 orders |
| Day 90 | 120 paying businesses, roughly ৳75,000 a month |

### First customers with zero budget
- Walk your neighbourhood: every restaurant with a paper menu is a prospect, and the owner is at the counter.
- Facebook groups for restaurant owners and home-food sellers; post a demo menu they can scan.
- Google Maps: scrape restaurants and sweet shops in one city and message those with a WhatsApp number.
- The demo that closes: build their menu from a photo of the paper one during the visit.
- Referral loop: every menu footer says "Menu by [product]"; one month free per referred shop.

### Pricing and the maths
- ৳299 to ৳999/month by number of items and orders.
- Cost of goods is under ৳30 per business a month for hosting and image storage; gross margin is above 90 percent.
- At the mid price of ৳649, roughly 460 paying businesses bring in ৳3 lakh a month, so treat it as an add-on to Ideas 2 and 95.

### Country kit: taking it to other languages
- First port: any market where you already sell the receptionist, because the menu is a one-day translation.
- What changes: language pack, currency and payment links (JazzCash, GoPay, Fawry, Stripe), local phone number format.
- What stays the same: menu builder, order flow, dashboard and QR templates.

### Risks and how to de-risk them
- Risk: free QR menu tools undercut you. De-risk: sell the WhatsApp order flow and bKash link, not the menu.
- Risk: menus go stale. De-risk: a monthly WhatsApp nudge with a one-tap "prices unchanged" reply.
- Risk: low price means high support cost. De-risk: a ten-minute self-serve setup and Bangla video help.

## Idea 4: AI Phone Answering for Local Businesses
*An AI that answers a business's phone in Bangla and English, takes messages and bookings, and sends SMS confirmations.*

### Who pays and why now
The customer is a doctor's chamber, diagnostic centre, hardware shop or car workshop. The phone rings while they are with a patient or customer, and nobody answers. Many callers are older or rural and will not use WhatsApp; they call.

They pay because a missed call is a missed patient or sale, and a receptionist costs ৳12,000 a month. Ten extra appointments a month pay for the top plan.

The moment is now because Bangla speech recognition and text-to-speech are good enough for short, structured calls, and Claude can run the conversation. Build this after the WhatsApp receptionist, since telephony costs and regulation are heavier. It ports anywhere with a telephony provider.

### The product in 30 days (MVP)
- A local number that forwards to the AI when the owner does not answer within 15 seconds.
- AI greeting in Bangla or English, answering from the business profile: hours, location, services, schedule.
- Message taking: name, number, reason, read back to confirm.
- Booking: offer free slots, confirm, write to the calendar, SMS confirmation to caller and owner.
- Owner dashboard with call log, transcripts and bookings.
- Leave out: outbound calls, payments by phone, multi-department menus, transfers to staff.

### Data, integrations and the Bangladesh specifics
- Telephony through a licensed local provider or an international voice API with a Bangladesh number; check BTRC rules on recording and IVR numbers first.
- Bangla speech models chosen by testing on real callers with regional accents and background noise.
- SMS through a local gateway with masking approval; bKash merchant API for subscriptions.

### Build it with Claude
Stack: Next.js dashboard, PostgreSQL, a Node voice service streaming audio between telephony API, speech models and Claude, SMS gateway, bKash merchant API.

1. Ask Claude for the call architecture and schema; build greeting and voicemail before adding AI.
```
Design a real-time voice assistant for a doctor's chamber in Bangladesh. Components:
telephony webhook, streaming speech-to-text, Claude with tools (get_profile,
check_slots, book_appointment, take_message), text-to-speech, SMS sender.
Give the PostgreSQL schema (businesses, calls, transcripts, bookings, messages) and
the sequence for one call with latency targets under two seconds per turn.
```
2. Ask Claude for the phone receptionist prompt, then test with ten calls from relatives with different accents.
```
Write a system prompt for a phone receptionist for a chamber in Chattogram. Speak in
the caller's language, one short sentence per turn, never give medical advice, confirm
the caller's name and number by reading them back, offer at most two free slots, and
end every call by summarising what will happen next. Include a Bangla example call.
```
3. Ask Claude for the dashboard: call log, bookings, Bangla profile editor.
4. Ask Claude for SMS templates and a guide to call forwarding on Grameenphone, Robi and Banglalink.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 chambers live, 300 calls answered |
| Day 60 | 15 paying customers, 2,000 calls, 400 bookings |
| Day 90 | 40 paying customers, roughly ৳1.3 lakh a month |

### First customers with zero budget
- Doctors' chambers above pharmacies in every town; the pharmacy owner often manages the phone.
- Facebook groups for doctors and workshop owners; sell "never miss a call", not AI.
- Google Maps: call listed chambers and workshops at 1 pm; those that do not answer are your list.
- The demo that closes: the owner calls the demo number and books an appointment in Bangla.
- Referral loop: every SMS confirmation carries the product name; a free month per referral.

### Pricing and the maths
- ৳1,499 to ৳4,999/month by call minutes and features.
- Cost of goods is roughly ৳400 to ৳1,200 per customer a month for telephony, speech models, AI and SMS; gross margin is around 65 to 75 percent.
- At the mid price of ৳3,249, roughly 90 paying customers bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan or Nigeria, where calls still dominate for older customers and telephony APIs are available.
- What changes: speech models per language, telephony provider and regulation, SMS gateway, payment rail.
- What stays the same: voice service, conversation logic, dashboard and booking engine.

### Risks and how to de-risk them
- Risk: speech recognition fails on accents and noise. De-risk: short turns, read back every detail, fall back to taking a message after two failures.
- Risk: regulation blocks numbers or recording. De-risk: a licensed local provider from day one and consent in the greeting.
- Risk: long calls eat margin. De-risk: cap calls at four minutes and price by minutes.
- Risk: callers hang up on a robot. De-risk: a warm voice and a "press 1 for the owner" escape.

## Idea 6: F-commerce AI Sales Agent
*An AI that replies to Facebook and WhatsApp inbox and comments in Bangla, confirms cash-on-delivery orders, books couriers and chases abandoned orders for page sellers.*

### Who pays and why now
The customer is a Facebook page seller: a woman selling sarees from home, a student selling gadgets, a small cosmetics brand. They get hundreds of comments and messages a day asking "price?" and answer each by thumb. Orders are confirmed by phone, written in a notebook and handed to a courier.

They pay because slow replies lose sales to the next page, cash-on-delivery returns are their biggest cost, and a staff member costs ৳10,000 a month. Hundreds of thousands of these sellers have no staff.

The moment is now because Meta's APIs and the Pathao, Steadfast and RedX courier APIs are open, and Claude reads Banglish reliably. It ports to Indonesia, Vietnam, the Philippines, Pakistan, Egypt and Nigeria with local couriers.

### The product in 30 days (MVP)
- Connect a Facebook page and WhatsApp number; catalogue with prices, variants and stock in Bangla.
- AI replies to comments and inbox with price, availability and delivery charge, and moves the buyer to inbox.
- Order capture: name, phone, address, product, quantity, confirmed in chat.
- One-tap courier booking to Steadfast, Pathao or RedX with tracking to the buyer.
- Seller dashboard: orders by status, a "take over" button for any chat.
- Leave out: ad management, agencies, returns handling, live video selling.

### Data, integrations and the Bangladesh specifics
- Meta Messenger Platform and WhatsApp Business API; page connection is instant, so lead with Messenger.
- Courier APIs from Steadfast, Pathao and RedX; delivery charges inside and outside Dhaka as catalogue rules.
- bKash merchant API for the subscription and for buyers who prefer advance payment.

### Build it with Claude
Stack: Next.js dashboard, PostgreSQL, a Node webhook service for Meta events, Claude API with tool use, courier API adapters, bKash merchant API.

1. Ask Claude for the schema, Meta webhook flow and a courier adapter so all three couriers look the same to your code.
```
Design a PostgreSQL schema for an AI sales agent for Facebook page sellers in
Bangladesh: sellers, pages, products (name_bn, price, variants, stock), conversations,
messages, orders (status: draft, confirmed, booked, delivered, returned), shipments.
Then define a TypeScript CourierAdapter interface with book, track and cancel, and
implement it for Steadfast, Pathao and RedX from their public API docs.
```
2. Ask Claude for the sales agent prompt, then test it on fifty real comments from a friend's page.
```
Write a system prompt for a sales assistant replying on a Bangladeshi Facebook page
that sells sarees. Reply in the buyer's language (Bangla, Banglish or English), quote
price and delivery charge from the catalogue only, never invent stock, ask for name,
phone and address one at a time, and call create_order when all are confirmed.
Comments get a short public reply plus an inbox message. Under 40 words per turn.
```
3. Ask Claude for the order board, catalogue editor and chat take-over screens.
4. Ask Claude for Bangla abandoned-order follow-ups sent 2 and 24 hours after a buyer goes quiet.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 pages live on trial, 500 orders captured |
| Day 60 | 40 paying sellers, 3,000 courier bookings |
| Day 90 | 120 paying sellers, roughly ৳2.4 lakh a month |

### First customers with zero budget
- Facebook groups for f-commerce sellers and women entrepreneurs, the largest business groups in the country.
- Comment sections of busy pages: every seller answering "price?" fifty times a day.
- Outreach angle: "You have 63 unanswered comments today. Here is what my agent would have replied."
- The demo that closes: connect their page in ten minutes and let it answer the next comment.
- Referral loop: sellers talk in groups; a free month per referred page.

### Pricing and the maths
- ৳999 to ৳2,999/month by monthly orders and channels.
- Cost of goods is roughly ৳200 to ৳500 per seller a month for Meta fees, AI and hosting; gross margin around 75 percent.
- At the mid price of ৳1,999, roughly 150 paying sellers bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia, because cash-on-delivery social selling is enormous there and couriers like JNE and J&T have APIs.
- What changes: language pack, courier adapters, delivery rules, payment rail (GoPay, OVO or Stripe).
- What stays the same: webhook service, agent logic, order capture, dashboard.

### Risks and how to de-risk them
- Risk: Meta restricts automated comment replies. De-risk: short public replies, selling in inbox.
- Risk: the AI quotes wrong prices or promises stock. De-risk: quote only from the catalogue and log every confirmation.
- Risk: courier APIs change or fail. De-risk: the adapter isolates each courier, with a manual fallback.
- Risk: sellers churn when sales are slow. De-risk: a weekly WhatsApp report of orders captured.

## Idea 41: Printing Press and Signboard Job Manager
*Quotes, job tickets, design approval by WhatsApp, press scheduling and dues for printing presses and sign makers.*

### Who pays and why now
The customer is a small offset or digital press, a screen printer, or a signboard maker in Fakirapool, Arambagh or a district town. They quote by phone, send proofs as WhatsApp photos and track jobs on a wall calendar. Proofs get lost, the wrong version prints, and customers dispute dues.

They pay because one reprint costs more than a year of software, and unpaid dues are why presses run out of cash. A job ticket with an approved design and agreed price ends most disputes.

The moment is now because every customer already approves designs on WhatsApp, and Claude makes a job manager cheap to build. Presses and sign makers exist everywhere, so the product ports globally.

### The product in 30 days (MVP)
- Quote builder: paper or material, size, quantity, colours, finishing, with saved price rules per press.
- Job ticket from an accepted quote, with status: design, approval, printing, finishing, ready, delivered.
- Design approval link sent by WhatsApp; the customer taps approve or requests changes, with a timestamped record.
- Press schedule board by machine and day.
- Customer ledger: advance, balance, payment history, dues reminders in Bangla.
- Leave out: stock of paper and ink, payroll, online ordering by the public, multi-branch.

### Data, integrations and the Bangladesh specifics
- WhatsApp click-to-chat and a public approval link need no API; use the Business API later for automatic reminders.
- bKash merchant API for advances and balance payments; Bangla numerals on quotes and invoices, which customers print and file.
- Standard paper sizes and local material names (PVC, flex, acrylic, SS letters) as defaults in the quote builder.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Cloudflare R2 for proof files, WhatsApp links, bKash merchant API.

1. Ask Claude for the schema and quote rules, then load one real press's price list to test.
```
Design a PostgreSQL schema for a printing press job manager in Bangladesh: shops,
customers, price_rules (material, size, quantity break, unit price), quotes, quote_items,
jobs (status enum), proofs (file, version, approved_at, approved_by), machines,
schedule_slots, payments, ledger_entries. Then write the quote calculation as a Laravel
service class with tests.
```
2. Ask Claude for the public proof approval page and the Bangla message that carries it.
```
Write the Bangla WhatsApp message a printing press sends a customer with a proof
approval link. Include job name, quantity, size, price, delivery date, and one line
telling them to tap approve or reply with changes. Under 8 lines. Then write the
approval page copy in Bangla: approve button, request changes box, version history.
```
3. Ask Claude for the job board, press schedule and customer ledger screens in Bangla.
4. Ask Claude for a dues reminder sequence in Bangla at 7, 14 and 30 days after delivery.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 presses live, 200 job tickets created |
| Day 60 | 25 paying shops, 1,500 proofs approved through the link |
| Day 90 | 70 paying shops, roughly ৳45,000 a month |

### First customers with zero budget
- Printing markets: Fakirapool, Arambagh and Paltan in Dhaka, Andarkilla in Chattogram, the press lane in every district town.
- Facebook groups for press owners and graphic designers; designers work with many presses and carry the product.
- Outreach angle: "How many reprints did you do last month because the wrong proof was approved?"
- The demo that closes: create a job ticket for their current job and send the proof link to the owner's own phone.
- Referral loop: every approval link and invoice shows the product name; a free month per referred press.

### Pricing and the maths
- ৳299 to ৳999/month by number of jobs and users.
- Cost of goods is under ৳40 per shop a month for hosting and file storage; gross margin is above 90 percent.
- At the mid price of ৳649, roughly 460 paying shops bring in ৳3 lakh a month, so pair it with Idea 95 or an accounting product to reach that faster.

### Country kit: taking it to other languages
- First port: any market where a partner already sells to print shops, since the product needs only a language pack and local material names.
- What changes: language, currency, material defaults, payment rail.
- What stays the same: quote engine, job flow, proof approval and ledger.

### Risks and how to de-risk them
- Risk: owners keep using the wall calendar. De-risk: the proof approval link is the hook; start there, and the job board follows.
- Risk: low price limits growth. De-risk: sell the proof approval and dues features to designers and agencies as a higher plan.
- Risk: proof files are large and costly to store. De-risk: compress previews and expire originals after 90 days.

## Idea 95: Local Shop Loyalty and SMS Marketing
*Points by phone number, stamp cards, birthday and festival offers in Bangla, WhatsApp broadcasts and a customer list, run from any phone at the counter.*

### Who pays and why now
The customer is a salon, restaurant, pharmacy or sweet shop that serves the same neighbourhood daily and has no idea who its regulars are. When a competitor opens across the road, it cannot reach the customers it has served for years.

They pay because a customer list is the cheapest marketing there is, an Eid offer sent to 800 past customers fills the shop for a week, and the price is less than one lunch. Hundreds of thousands of shops fit this description.

The moment is now because SMS is cheap, WhatsApp broadcasts are normal, and a counter phone can do the job without a POS. It works everywhere, and the moat is simple: the shop cannot leave without leaving its customer list behind.

### The product in 30 days (MVP)
- Counter screen on any phone: enter customer number and bill amount, points added, balance in Bangla.
- Stamp card mode: buy 9, get 1 free.
- Customer list with visit count, last visit, spend and birthday, exportable.
- Campaigns: birthday message, "we miss you" after 30 days, festival offers, by SMS or WhatsApp in Bangla.
- Redemption at the counter with a one-time code; the owner sees repeat rate.
- Leave out: customer app, cross-shop coupons, POS integration, multi-branch reporting.

### Data, integrations and the Bangladesh specifics
- Bulk SMS through a local gateway with masking approval; SMS cost is passed through as a monthly message allowance.
- WhatsApp broadcasts through the owner's own WhatsApp Business app; the API for larger shops later.
- bKash merchant API for the subscription; Bangla numerals in every message and a built-in festival calendar (Eid, Puja, Pohela Boishakh).

### Build it with Claude
Stack: Next.js progressive web app for any counter phone, PostgreSQL, SMS gateway, Claude API for campaign copy, bKash merchant API.

1. Ask Claude for the schema and counter screen, and put it on a friend's shop phone in week one.
```
Design a PostgreSQL schema for a shop loyalty SaaS in Bangladesh: shops, customers
(phone, name, birthday), visits (amount, points), stamp_cards, rewards, redemptions
(one-time code), campaigns (type, channel sms/whatsapp, sent_at), messages. Then write
a Next.js counter page that works one-handed on a cheap Android phone: number pad,
amount, add points, show balance in Bangla numerals.
```
2. Ask Claude for the Bangla campaign message library, editable per shop.
```
Write 12 short SMS templates in Bangla for a neighbourhood shop loyalty programme:
birthday wish with a gift, 30-day "we miss you", points balance reminder, Eid-ul-Fitr
offer, Eid-ul-Adha offer, Pohela Boishakh offer, new arrival, and a thank-you after a
first visit. Each under 160 characters including a {shop_name} placeholder. No emoji.
```
3. Ask Claude for the customer list, campaign scheduler and redemption screens.
4. Ask Claude for a Bangla counter poster: "Give your number, earn points", with shop name and QR code.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 15 shops live, 2,000 customer numbers collected |
| Day 60 | 80 paying shops, 20,000 customers, first festival campaign sent |
| Day 90 | 250 paying shops, roughly ৳85,000 a month |

### First customers with zero budget
- Your own street: salons, sweet shops, pharmacies and cafes within walking distance; the owner is at the counter.
- Facebook groups for salon, restaurant and pharmacy owners; post a shop's repeat-rate chart.
- Google Maps: scrape salons and restaurants in one area and message them before Eid.
- The demo that closes: enter the owner's own number, add points, and send them the Bangla welcome SMS.
- Referral loop: every SMS carries the product name; a free month per referred shop; market committees bring a whole market.

### Pricing and the maths
- ৳199 to ৳499/month by customers and messages per month.
- Cost of goods is roughly ৳50 to ৳150 per shop a month, mostly SMS; gross margin is around 70 percent.
- At the mid price of ৳349, roughly 860 paying shops bring in ৳3 lakh a month, so spread market by market and pair it with Ideas 3 and 41.

### Country kit: taking it to other languages
- First port: any market where a partner sells to shops, because the counter screen translates in a day.
- What changes: language pack, festival calendar, SMS gateway and sender rules, payment rail.
- What stays the same: counter app, points engine, campaign scheduler and customer list.

### Risks and how to de-risk them
- Risk: SMS costs rise or delivery is throttled. De-risk: push shops to WhatsApp and cap messages per plan.
- Risk: customers see messages as spam. De-risk: opt-in at the counter, one campaign a month by default, a stop reply.
- Risk: low price means support must be near zero. De-risk: five-minute self-serve setup and a Bangla help video.


---

# Section 2: Local Business and Commerce (Part 2)

The businesses in this section share one problem: a skilled owner takes orders, advances and promises on paper, then loses money to forgotten dues, disputed jobs and customers who never return. Each chapter shows how a small team can replace that paper with a cheap Bangla app, built with Claude, that pays for itself in the first month.

## Idea 22: Tailor Shop OS
*A Bangla app for tailor shops: customer measurements, order tickets with delivery dates, an Eid rush queue, SMS pickup alerts and fabric stock.*

### Who pays and why now
The customer is the owner of a neighbourhood tailor shop, from a two-machine shop in Mirpur to a twenty-worker ladies' tailoring house in Chattogram. Today the owner writes measurements in a notebook, staples a paper slip to the fabric, and promises a delivery date from memory. Before Eid, orders double, slips get lost, and the last night is spent phoning angry customers.

The owner will pay because a lost slip is a lost customer and a missed Eid delivery is a public fight in the shop. A shop that pulls up last year's measurements in five seconds keeps repeat customers. Tailors already use WhatsApp for design photos, so the jump to an app is small. The product ports to India, Pakistan, Nigeria, Indonesia and Egypt, where tailoring is equally local and festival-driven.

### The product in 30 days (MVP)
- Customer profile with measurement sheets per garment type and order history.
- Order ticket with fabric photo, design notes, price, advance, promised date and status.
- Queue sorted by delivery date, with an Eid mode showing daily capacity against promises.
- Automatic Bangla SMS when an order is ready, plus a balance-due reminder.
- Daily cash summary: advances, balances collected, dues outstanding.
- Fabric stock by roll with metres used per order.
- Leave out: online ordering, worker payroll, multi-branch reports, an iOS app.

### Data, integrations and the Bangladesh specifics
- Payment: subscription through bKash merchant API or Nagad; customer payments stay in cash, recorded manually.
- SMS: a local bulk gateway with a Bangla sender ID; keep messages under 70 Bangla characters.
- Measurement templates for panjabi, shirt, salwar and blouse, with Bangla labels and Bangla numerals.
- Offline first: the phone must work during load shedding and sync later.

### Build it with Claude
Stack: Flutter Android app with SQLite, Laravel API on a small VPS, PostgreSQL, Claude API for parsing measurements, bKash merchant API, bulk SMS gateway.

1. Ask Claude for the data model and run the migrations on day one.
```
Design a PostgreSQL schema for a tailor shop app in Bangladesh. Tables: shops, customers,
measurement_sheets (JSONB per garment type, versioned), orders (fabric photo URL, notes, price,
advance, balance, promised_date, status: received/cutting/sewing/ready/delivered), fabric_rolls,
sms_log. Index by customer phone and promised_date. Return Laravel migrations and models,
with Bangla field labels in a separate lang file.
```
2. Paste the schema and ask Claude for the Flutter screens (customer search, measurement sheet, order ticket, queue) with offline SQLite and sync. Install on a real phone the same day.
3. Add the AI feature: the tailor types or speaks one line and Claude fills the sheet.
```
You receive one line of Bangla or mixed text from a tailor, for example
"লম্বা 42 বুক 44 কোমর 38 হাতা 24 কলার 16 পাঞ্জাবি". Return JSON with garment_type and
measurements in inches as numbers, keys in English (length, chest, waist, sleeve, collar).
If a value is missing, set it to null. Never guess. Return only JSON.
```
4. Ask Claude for the Bangla SMS templates and the bKash subscription flow, then test with three real shops for two weeks.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 shops using the app daily, 300 orders recorded |
| Day 60 | 40 shops, 20 paying, one festival rush load tested |
| Day 90 | 120 shops, 70 paying, roughly ৳25,000 monthly revenue |

### First customers with zero budget
- Walk the tailoring lanes: Elephant Road, Gausia, Nurjahan Market, and the tailor row in every upazila bazaar.
- Facebook groups for ladies' tailoring and boutique owners; post a 30-second video of finding a customer's sizes.
- Outreach angle: "Never lose a slip again this Eid." First festival season free.
- The demo that closes: record the owner's last five orders on the spot and send a real SMS to their phone.
- Referral loop: one month free for every tailor they bring.

### Pricing and the maths
- Basic ৳199/month (one phone, 200 orders, SMS extra) and Pro ৳499/month (unlimited orders, 500 SMS included, fabric stock).
- Cost of goods is roughly ৳40 per shop per month in SMS and hosting, so gross margin is above 80 percent.
- At a mid price of ৳349, roughly 860 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan, because Eid tailoring demand is identical and Urdu measurement words map one to one.
- What changes: language pack, garment templates (shalwar kameez, sherwani), JazzCash or Easypaisa, a local SMS gateway.
- Reseller: a tailoring supplies wholesaler in Lahore who already visits every shop.
- What stays the same: schema, queue logic, and the measurement parser with new examples.

### Risks and how to de-risk them
- Risk: owners will not type on a phone. De-risk: one-line voice entry and a five-minute setup done by you in the shop.
- Risk: churn after Eid. De-risk: show the owner how many repeat customers returned because their sizes were on file.
- Risk: SMS costs eat the ৳199 plan. De-risk: cap SMS on Basic and sell top-ups.
- Risk: a competitor copies the app. De-risk: speed, market presence, and the data already inside each shop.

## Idea 32: Repair Shop Ticketing
*A ticketing app for mobile, electronics and AC repair shops: job tickets with photos, parts used, warranty records, SMS when ready and technician commissions.*

### Who pays and why now
The customer is the owner of a repair shop: a phone repair counter in Motalib Plaza, a TV and fridge workshop in a district town, or an AC servicing team with three technicians. Today the shop hands over a torn receipt, writes the fault on a sticker, and remembers the agreed price. Devices get mixed up, customers claim a scratch was not there before, and warranty arguments end in shouting.

The owner will pay because one lost phone costs more than a year of subscription, and because technicians quietly under-report parts and jobs. A photo at intake and an SMS ticket stop most disputes, and a shop that texts "your device is ready" wins the next repair. Repair shops exist in every market on earth, so this product ports everywhere, with only language and SMS gateway changing.

### The product in 30 days (MVP)
- Intake ticket with device model, IMEI or serial, fault notes, condition photos, estimate and advance.
- Status flow: received, diagnosed, waiting for parts, repaired, delivered, with a ticket number for the customer.
- Parts used per ticket, drawn from a simple parts stock with cost and selling price.
- Warranty record per repair with expiry date and a lookup by ticket number or phone.
- Bangla SMS when ready for pickup and a due reminder for uncollected devices.
- Technician view with jobs done and commission earned this month.
- Leave out: full accounting, online booking, customer app, multi-branch transfers.

### Data, integrations and the Bangladesh specifics
- Payment: bKash merchant API for subscriptions; customer payments recorded against the ticket as cash, bKash or Nagad.
- SMS: bulk gateway with a Bangla sender ID; the ready message carries the ticket number and balance due.
- A device model list for phones, TVs and ACs sold in Bangladesh so intake takes three taps.
- A 58 mm thermal receipt in Bangla, with Bangla numerals as a shop setting.

### Build it with Claude
Stack: Next.js web app that works on a phone browser and a shop PC, PostgreSQL, Claude API for fault-note summaries, bKash merchant API, bulk SMS gateway, Cloudflare.

1. Ask Claude for the schema and status machine.
```
Design a PostgreSQL schema for a repair shop ticketing app in Bangladesh: shops, technicians,
customers, tickets (device_type, brand, model, imei_serial, fault_notes, intake_photos[],
estimate, advance, status enum, delivered_at), ticket_parts, parts_stock, warranties (ticket_id,
months, expires_at), payments, sms_log, commissions. Write the status transition rules as a table
and generate Prisma schema plus Next.js API routes for creating and updating tickets.
```
2. Ask Claude for the intake, ticket list and technician screens, mobile first, with photo capture. Deploy to Cloudflare and test on a cheap Android phone.
3. Add the AI feature: rough technician notes become a plain Bangla diagnosis and warranty text.
```
A repair technician wrote these rough notes in Bangla or mixed language: {notes}.
Write a short customer-facing summary in plain Bangla: what was wrong, what was replaced,
and the warranty period {months} months with what it covers and excludes (water damage,
physical damage). Maximum 60 words. No technical jargon. Return only the text.
```
4. Ask Claude for the Bangla SMS templates, receipt layout and commission report, then pilot in three shops for two weeks.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 8 shops live, 500 tickets created |
| Day 60 | 35 shops, 20 paying, 3,000 tickets, first warranty lookups |
| Day 90 | 100 shops, 60 paying, roughly ৳22,000 monthly revenue |

### First customers with zero budget
- Phone repair markets: Motalib Plaza, Bashundhara City, Eastern Plaza, and the electronics lane of every district town.
- Facebook groups where technicians trade parts and ask for firmware help; they are large and active.
- Google Maps: scrape "mobile repair" and "AC servicing" listings by district and call them.
- Outreach angle: "Stop losing devices and arguments. Photo at intake, SMS when ready."
- The demo that closes: ticket the technician's own phone, photo it, and send the SMS in under a minute.
- Referral loop: a month free for each shop referred.

### Pricing and the maths
- Solo ৳199/month (one user, 150 tickets), Shop ৳399/month (three users, SMS included, parts stock), Workshop ৳599/month (unlimited users, technician commissions, warranty portal).
- Cost of goods is roughly ৳50 per shop per month for SMS, photo storage and hosting; gross margin is above 80 percent.
- At a mid price of ৳399, roughly 750 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria, where repair markets like Computer Village in Lagos are dense and SMS is the default channel.
- What changes: English or Pidgin copy, Paystack or Flutterwave for subscriptions, a Nigerian SMS gateway, local device lists.
- Reseller: a parts wholesaler who sells to hundreds of repair counters.
- What stays the same: ticket schema, status flow, photo intake and the AI summary prompt with a language switch.

### Risks and how to de-risk them
- Risk: technicians resist tracking because it exposes side income. De-risk: sell to owners and show commissions as a benefit for honest technicians.
- Risk: photo storage cost grows. De-risk: compress on upload and delete photos 90 days after delivery.
- Risk: shops stop paying in slow months. De-risk: warranty lookup and customer history keep the app in daily use.
- Risk: SMS gateway outages. De-risk: fall back to a WhatsApp message from the shop's number.

## Idea 43: Furniture and Interior Workshop Tracker
*An order tracker for furniture and interior workshops: custom specs with photos, advance and balance, production stages, delivery scheduling, and timber and hardware stock.*

### Who pays and why now
The customer is the owner of a furniture workshop or a small interior firm: the wood workshops of Bogura, the sofa makers of Panthapath and Mirpur, and the two-carpenter shops in every district town that make beds and wardrobes to order. Today the owner sketches on a scrap of paper, takes a cash advance, and promises delivery "in three weeks". The paper is lost, the customer remembers a different colour, and delivery slips by a month.

The owner will pay because every dispute over a custom order costs a day of rework and often the balance payment. A photo, a written spec and a stage tracker turn "you said walnut" into a settled fact. Apartment handovers in Dhaka keep demand high, and buyers now expect WhatsApp updates. The same made-to-order culture exists in India, Pakistan, Indonesia, Nigeria and Egypt.

### The product in 30 days (MVP)
- Order with item list, dimensions, material, finish, reference photos and the approved sketch.
- Advance and balance tracking with payment history per order.
- Production stages from design approved to delivered, with a date per stage.
- Delivery calendar showing promised dates against workshop capacity.
- Timber and hardware stock with quantities consumed per order.
- Bangla SMS or WhatsApp update at each stage and a balance-due reminder before delivery.
- Leave out: 3D design tools, worker payroll, a customer marketplace, accounting exports.

### Data, integrations and the Bangladesh specifics
- Payment: bKash merchant API for subscriptions; customer advances recorded as cash, bKash or bank against the order.
- Channel: WhatsApp for stage photos through the owner's number, with SMS as a fallback for customers without data.
- Material list with local names (segun, mehogoni, gorjon, board grades) and standard sizes in feet and inches.
- Photos compressed on upload for weak mobile data; Bangla numerals on the customer's order sheet.

### Build it with Claude
Stack: Next.js web app for the owner's phone and PC, PostgreSQL, Cloudflare R2 for photos, Claude API for spec sheets, bKash merchant API, SMS gateway.

1. Ask Claude for the schema and the stage model.
```
Design a PostgreSQL schema for a custom furniture workshop in Bangladesh: workshops, customers,
orders (promised_date, total, advance, balance), order_items (item_type, dimensions_ft_in,
material, finish, colour, notes, photos[]), production_stages (stage enum, started_at, done_at),
payments, stock_items (timber by cft, hardware by piece), stock_movements, notifications.
Generate Prisma schema, seed data with Bangla material names, and API routes for orders.
```
2. Ask Claude for the order screen with photo upload, the stage board and the delivery calendar. Deploy and enter five real orders from a friendly workshop.
3. Add the AI feature: rough notes become a bilingual spec sheet the customer signs.
```
From these workshop notes about a furniture order: {notes}, write an order specification in two
columns, Bangla and English. Include item, dimensions in feet and inches, material, finish,
colour, quantity, price, advance paid, balance due and promised delivery date. Flag any missing
field as "TBC". Keep it under 120 words per language. Return as a simple markdown table.
```
4. Ask Claude for the Bangla stage-update templates and a PDF order sheet the customer keeps.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 6 workshops live, 60 orders tracked |
| Day 60 | 25 workshops, 12 paying, 400 orders, first on-time delivery data |
| Day 90 | 70 workshops, 40 paying, roughly ৳25,000 monthly revenue |

### First customers with zero budget
- Furniture clusters: Bogura's workshop lanes, Panthapath and Mirpur sofa shops, Sylhet and Khulna timber markets.
- Facebook groups for interior designers and furniture makers, where owners post finished work daily.
- Google Maps: scrape "furniture workshop" and "interior design" listings by district and visit.
- Outreach angle: "Never lose a balance payment to a forgotten spec again."
- The demo that closes: photograph the sketch on the owner's desk, create the order, and send a stage update in front of them.
- Referral loop: timber and hardware suppliers get a commission for each workshop they sign.

### Pricing and the maths
- Starter ৳299/month (one user, 20 open orders), Workshop ৳599/month (three users, stock, WhatsApp updates), Studio ৳999/month (unlimited users, PDF spec sheets, delivery calendar sharing).
- Cost of goods is roughly ৳60 per workshop per month for photo storage, SMS and hosting; gross margin is above 80 percent.
- At a mid price of ৳649, roughly 460 paying workshops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia, where Jepara and other furniture towns run on the same made-to-order model with advances.
- What changes: Bahasa language pack, material list (teak, mahogany), metric sizes, Midtrans or Xendit for subscriptions.
- Reseller: a timber or hardware supplier serving hundreds of workshops.
- What stays the same: the order and stage schema, photo intake, and the spec-sheet prompt with a language switch.

### Risks and how to de-risk them
- Risk: carpenters cannot use the app. De-risk: only the owner or manager updates stages; carpenters never touch it.
- Risk: photo storage costs. De-risk: compress to 1,200 px and archive photos six months after delivery.
- Risk: long order cycles slow feedback. De-risk: start with sofa and bed makers whose cycles are two to three weeks.
- Risk: low willingness to pay ৳999. De-risk: anchor on the value of one saved balance payment, usually ৳10,000 or more.

## Idea 88: Vehicle Workshop Job Cards
*Job cards for car, bike and CNG garages: photos at intake, parts used, mechanic commissions, vehicle service history, SMS when ready, and dues tracking.*

### Who pays and why now
The customer is the owner of a vehicle garage: a car workshop in Tejgaon or Dholaikhal, a motorbike servicing point in any district town, or a CNG auto-rickshaw garage near a stand. Today the owner scribbles the job on a card, the mechanic pulls parts from the shelf without a record, and the vehicle leaves with "pay next time" in a notebook. At month end, parts are missing, dues are forgotten and nobody remembers what was done to a vehicle last time.

The owner will pay because untracked parts and forgotten dues cost far more than ৳649 a month. A job card with photos and a parts list also settles the complaint that a part was charged but not fitted. Motorbike ownership has grown fast, ride-share drivers service often, and every one carries a phone that receives SMS. Garages work the same way everywhere, so this ports to any country with only language and payment changes.

### The product in 30 days (MVP)
- Vehicle profile by registration number with owner phone and full service history.
- Job card with complaint, intake photos, odometer, estimate, assigned mechanic and status.
- Parts used per job from a simple stock list with cost and selling price.
- Labour lines per job with a commission percentage per mechanic.
- Dues ledger per customer with a Bangla SMS reminder.
- SMS when the vehicle is ready, with the amount due.
- Leave out: online booking, spare parts marketplace, fleet contracts, full accounting.

### Data, integrations and the Bangladesh specifics
- Payment: bKash merchant API for subscriptions; job payments recorded as cash, bKash or due.
- SMS: bulk gateway with a Bangla sender ID; keep messages under 70 Bangla characters.
- Registration number entry in both Bangla and English format (for example ঢাকা মেট্রো-হ), searchable either way.
- A starter list of service items and parts for popular bikes, CNGs and sedans; big buttons and few taps for oily hands.

### Build it with Claude
Stack: Flutter Android app with offline SQLite, Laravel API, PostgreSQL, Cloudflare R2 for photos, Claude API for service-history summaries, bKash merchant API, SMS gateway.

1. Ask Claude for the schema, including the commission calculation.
```
Design a PostgreSQL schema for a vehicle garage in Bangladesh: garages, mechanics (commission_pct),
customers, vehicles (reg_no in Bangla and Latin, type: car/bike/cng, odometer), job_cards (complaint,
intake_photos[], estimate, status, ready_at, delivered_at), job_parts, job_labour (amount,
mechanic_id), stock_items, payments, dues, sms_log. Include a SQL view that totals each mechanic's
commission for a month. Return Laravel migrations and models.
```
2. Ask Claude for the Flutter screens: find vehicle by registration, new job card with camera, parts picker, ready and deliver buttons. Install on a mechanic's phone and watch it used.
3. Add the AI feature: when a vehicle returns, Claude summarises its history and suggests what to check.
```
Here is the service history of a vehicle as JSON: {history}. Today's complaint: {complaint}.
Write, in plain Bangla, a 4-line note for the mechanic: what was done in the last two visits,
which parts are still under warranty, and two things to check based on the odometer and time
since the last service. Do not invent parts or dates not in the data.
```
4. Ask Claude for the Bangla SMS templates and a monthly commission and dues report, then pilot in three garages for two weeks.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 8 garages live, 400 job cards |
| Day 60 | 30 garages, 15 paying, 2,500 job cards, first repeat-vehicle lookups |
| Day 90 | 90 garages, 50 paying, roughly ৳30,000 monthly revenue |

### First customers with zero budget
- Garage clusters: Dholaikhal, Tejgaon, Bangla Motor, and the bike servicing lanes near every district bus stand.
- Facebook groups for motorbike riders and for garage owners and mechanics.
- Google Maps: scrape "car repair", "motorcycle repair" and "CNG garage" by district.
- Outreach angle: "Every part accounted for, every due remembered."
- The demo that closes: open a job card for the owner's own bike, add two parts and show the commission update.
- Referral loop: spare parts dealers and lubricant distributors earn a month's fee per garage signed.

### Pricing and the maths
- Bike ৳299/month (one user, 100 jobs), Garage ৳599/month (three users, stock, commissions, SMS included), Workshop ৳999/month (unlimited users, dues reports, multi-bay view).
- Cost of goods is roughly ৳60 per garage per month for SMS, photos and hosting; gross margin is above 80 percent.
- At a mid price of ৳649, roughly 460 paying garages make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya or Nigeria, where motorbike taxi fleets need constant servicing and M-Pesa or Paystack collect subscriptions.
- What changes: language pack, registration formats, local parts list, payment rail and SMS gateway.
- Reseller: a lubricant or spare parts distributor who visits every garage weekly.
- What stays the same: job card schema, photo intake, commission view and the history prompt.

### Risks and how to de-risk them
- Risk: mechanics skip recording parts. De-risk: the owner records parts at the counter, not the mechanic at the bay.
- Risk: garages will not pay ৳999. De-risk: show the dues report; one month's recovered dues usually covers a year.
- Risk: dirty hands and broken screens. De-risk: a cheap dedicated phone in a case, and voice entry for complaints.
- Risk: photo storage cost. De-risk: compress and archive after 90 days.

## Idea 92: Mobile Phone Shop EMI Ledger
*A ledger for mobile phone shops: handset stock by IMEI, instalment sales with bKash collection and reminders, guarantor records, warranty and exchange, and distributor dues.*

### Who pays and why now
The customer is the owner of a mobile phone shop that sells handsets on instalments: the counters in Bashundhara City and Motalib Plaza, and the tens of thousands of upazila shops that sell a ৳15,000 phone for ৳3,000 down and ৳1,000 a month. Today the agreement is a photocopied form with the guarantor's NID stapled to it, and collections live in a notebook. Instalments are missed, the shop forgets to call, and a handset sold on paper cannot be traced when it returns for warranty.

The owner will pay because one defaulted phone erases the profit on ten sales, and reminders sent on time cut defaults sharply. IMEI-level stock also stops quiet losses when staff sell a handset off the books. bKash collection lets the customer pay from the village without visiting. The same instalment culture exists in India, Pakistan, Nigeria, Kenya and Indonesia, where mobile money makes collections easy.

### The product in 30 days (MVP)
- Handset stock by IMEI with purchase price, distributor, and status: in stock, sold, returned, exchanged.
- Instalment sale with down payment, schedule, customer and guarantor NID photos and the signed form.
- Collection screen: mark instalment paid by cash or bKash, with receipt SMS.
- Bangla SMS reminder before and on the due date, with overdue escalation to the guarantor.
- Warranty and exchange record per IMEI.
- Distributor dues ledger with purchase invoices and payments.
- Leave out: credit scoring, a customer app, phone locking services, multi-branch stock transfer.

### Data, integrations and the Bangladesh specifics
- Payment: bKash merchant API collects instalments to the shop and matches them to the schedule; Nagad as a second rail.
- SMS: bulk gateway with a Bangla sender ID; the reminder carries the amount, due date and the shop's bKash number.
- IMEI scanning by camera with check-digit validation; NID photos stored encrypted as sensitive data.
- Bangla numerals in receipts and schedules, and a printed Bangla instalment agreement.

### Build it with Claude
Stack: Flutter Android app with offline cache, Laravel API, PostgreSQL, Cloudflare R2 for documents, Claude API for collection messages, bKash merchant API, SMS gateway.

1. Ask Claude for the schema and the instalment schedule logic.
```
Design a PostgreSQL schema for a mobile phone shop in Bangladesh that sells on instalments:
shops, distributors, handsets (imei unique, model, cost, distributor_id, status), customers
(nid_photo_url), guarantors, sales (handset_id, price, down_payment, months, interest_flat),
instalments (due_date, amount, paid_at, method), collections, distributor_invoices,
distributor_payments, warranty_events, sms_log. Include a function to generate the instalment
schedule from a sale. Return Laravel migrations, models and a service class.
```
2. Ask Claude for the Flutter screens: IMEI scan, new instalment sale with photo capture, today's collections, overdue list. Install and enter the shop's open agreements.
3. Add the AI feature: a Bangla reminder tuned to how late the customer is.
```
Write a Bangla SMS for a phone shop instalment customer. Name: {name}. Amount due: {amount} taka.
Due date: {date}. Days overdue: {days}. bKash number: {bkash}. Tone: friendly reminder if not
yet due, polite firm if 1 to 7 days late, formal with mention of the guarantor if more than 7
days late. Maximum 70 Bangla characters. Return only the message text.
```
4. Ask Claude for the bKash matching job, the distributor dues report and a printable Bangla agreement. Pilot with two shops for one collection cycle.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 6 shops live, 200 active instalment agreements |
| Day 60 | 25 shops, 15 paying, 1,000 agreements, measured drop in late payments |
| Day 90 | 70 shops, 45 paying, roughly ৳45,000 monthly revenue |

### First customers with zero budget
- Phone markets: Bashundhara City, Motalib Plaza, Eastern Plaza, and the mobile lane in every upazila bazaar.
- Facebook groups for mobile shop owners and handset resellers, where distributors post price lists.
- Distributor sales reps who visit every shop weekly; pay them a commission per signed shop.
- Outreach angle: "Collect instalments on bKash and let the app do the reminding."
- The demo that closes: enter one real overdue customer, send the reminder, and show the payment matching itself.
- Referral loop: a month free for each referred shop.

### Pricing and the maths
- Counter ৳499/month (one user, 100 active agreements), Shop ৳999/month (three users, unlimited agreements, SMS included, distributor dues), Chain ৳1,499/month (multi-branch, guarantor escalation, exports).
- Cost of goods is roughly ৳120 per shop per month for SMS, encrypted storage and hosting; gross margin is above 80 percent.
- At a mid price of ৳999, roughly 300 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, where phone financing is common and M-Pesa collection is universal.
- What changes: Swahili and English copy, M-Pesa API, local ID formats, an SMS gateway.
- Reseller: a handset distributor whose reps already visit every shop.
- What stays the same: the IMEI stock model, schedule logic, reminder prompt and warranty history.

### Risks and how to de-risk them
- Risk: shops expect credit scoring. De-risk: state clearly that the app records and reminds; the shop decides who gets credit.
- Risk: NID data leaks. De-risk: encrypt at rest, restrict downloads, delete documents after the agreement closes.
- Risk: bKash matching fails on wrong references. De-risk: unique payment reference per customer and a manual match screen.
- Risk: shops churn once defaults fall. De-risk: stock by IMEI and warranty history keep the app useful after collections.

## Idea 93: Optical Shop and Lens Lab Manager
*A Bangla manager for optical shops: eye prescriptions, frame and lens stock, lab work orders, ready-for-pickup SMS and yearly recall reminders.*

### Who pays and why now
The customer is the owner of an optical shop, from the chains around Dhaka's hospitals to the single-counter shop with a refractionist in every district town, plus the small lens labs that grind for several shops. Today the prescription lives in a notebook or on a card the customer loses, the lab order is a phone call, and nobody knows which frames are in stock. When the customer returns two years later, the shop starts from zero.

The owner will pay because a stored prescription makes the next sale a five-minute job, and a yearly recall SMS brings back customers who would otherwise buy next door. Screen time is rising, more people need glasses, and every one of them has a phone number. Optical shops in India, Pakistan, Nigeria, Indonesia and Egypt run on the same notebook system, so the product ports with a language pack and a payment change.

### The product in 30 days (MVP)
- Customer profile with prescription history: sphere, cylinder, axis, add and PD per eye, with date and examiner.
- Sale record with frame, lens type, coating, price, advance and promised date.
- Lab work order to the in-house or external lab, with status: sent, grinding, fitted, ready.
- Frame and lens stock with barcode scan, supplier and cost.
- Bangla SMS when glasses are ready and a recall SMS twelve months after the last exam.
- Daily summary: sales, advances, lab orders pending.
- Leave out: online frame store, insurance claims, multi-branch stock transfer, an iOS app.

### Data, integrations and the Bangladesh specifics
- Payment: bKash merchant API for subscriptions; sales recorded as cash, bKash or card.
- SMS: bulk gateway with a Bangla sender ID; the recall message names the shop and offers a free check.
- A prescription card PDF in Bangla and English with Bangla numerals as an option; customers still want the card.
- Frame barcodes on a cheap label printer, and a starter list of lens types and coatings.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for prescription reading and recall copy, bKash merchant API, SMS gateway, Cloudflare.

1. Ask Claude for the schema with a proper prescription model.
```
Design a PostgreSQL schema for an optical shop in Bangladesh: shops, customers, prescriptions
(per eye: sphere, cylinder, axis, add, pd, va; examiner, examined_at, notes), sales (frame_id,
lens_type, coating, price, advance, balance, promised_date), lab_orders (lab_id, status enum,
sent_at, ready_at), frames (barcode, brand, model, colour, cost, qty), lens_stock, recalls
(customer_id, due_at, sent_at), sms_log. Return Prisma schema and Next.js API routes.
```
2. Ask Claude for the prescription entry screen with a plus and minus keypad, the sale screen, the lab board and the stock screen. Deploy and enter a week of real prescriptions.
3. Add the AI feature: a photo of an old handwritten prescription becomes structured data.
```
This image is a handwritten eye prescription from a Bangladeshi optical shop. Extract for each
eye (right OD, left OS): sphere, cylinder, axis, add, and the PD if present, as numbers with
sign. Return JSON with a confidence from 0 to 1 per field and mark any unreadable field null.
Do not guess values. If the image is not a prescription, return {"error": "not_prescription"}.
```
4. Ask Claude for the Bangla SMS templates and the printable prescription card, then pilot with three shops and one lab for two weeks.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 6 shops live, 400 prescriptions stored |
| Day 60 | 25 shops, 12 paying, 2,000 prescriptions, first lab orders through the app |
| Day 90 | 70 shops, 40 paying, roughly ৳25,000 monthly revenue, first recall batch sent |

### First customers with zero budget
- Optical clusters: around Islamia Eye Hospital and Dhaka Medical, Chattogram's optical lane, and the optical row in every district town.
- Facebook groups for optometrists, refractionists and optical shop owners.
- Google Maps: scrape "optical shop" and "optician" listings by district and visit with a demo.
- Outreach angle: "Their prescription ready before they sit down, and a reminder that brings them back next year."
- The demo that closes: enter the owner's own prescription, print the card, and send the ready SMS to their phone.
- Referral loop: lens labs sign their partner shops; a month free per shop they bring.

### Pricing and the maths
- Counter ৳299/month (one user, prescriptions, ready alerts), Shop ৳599/month (three users, stock, lab orders, recall SMS included), Lab ৳999/month (lab board for partner shops, exports).
- Cost of goods is roughly ৳60 per shop per month for SMS, image processing and hosting; gross margin is above 80 percent.
- At a mid price of ৳649, roughly 460 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where independent opticians share the same prescription formats and UPI collects subscriptions.
- What changes: Hindi and regional language packs, UPI or Razorpay, Indian SMS registration, local lens supplier lists.
- Reseller: a lens or frame distributor who calls on every optician.
- What stays the same: the prescription schema, lab flow, recall logic and the image-reading prompt.

### Risks and how to de-risk them
- Risk: wrong prescription data harms a customer. De-risk: always show extracted values for human confirmation before saving.
- Risk: refractionists find entry slow. De-risk: a dedicated keypad and defaults from the last exam.
- Risk: recall SMS feels like spam. De-risk: one message a year, named shop, opt-out line.
- Risk: staff share one login. De-risk: cheap extra users and a per-user sales report the owner values.


---

# Section 3: Health (Part 1)

Health is where the paper problem in Bangladesh is most visible: prescriptions nobody can read, lab reports nobody explains, clinics run from registers. These seven ideas turn that paper into software a small team can sell, starting at the doctor's chamber and ending at the fifty-bed hospital.

## Idea 8: Doctor's Prescription Writer
*Speak or type in Bangla or English and print a clean prescription with Bangladeshi drug brands, Bangla dosing and follow-up SMS.*

### Who pays and why now
The customer is a private-chamber doctor who sees 30 to 80 patients an evening at a chamber attached to a pharmacy or diagnostic centre. Today the prescription is handwritten: patients cannot read it, pharmacies misread it, and there is no record of the last visit.

The doctor pays because the tool saves a minute per patient, looks professional and builds a searchable history. The moment is right because regulators keep pushing for printed prescriptions, cheap tablets and thermal printers are affordable, and Claude can turn Bangla dictation into a structured prescription. Port countries are Pakistan and Nepal, each with its own drug brand database.

### The product in 30 days (MVP)
- Voice or typed entry in Bangla or English: complaint, diagnosis, drugs, advice.
- Drug search over a Bangladeshi brand database with generic and strength.
- Dose patterns such as 1+0+1, before or after meals, as Bangla instructions.
- One-tap print to A4 or A5 with letterhead and a QR link.
- Patient record with past prescriptions, next visit date and Bangla follow-up SMS.
- Leave out: pharmacy ordering, lab integration, telemedicine video, insurance claims.

### Data, integrations and the Bangladesh specifics
- Drug database built from the DGDA list of registered brands, in your own table because idea 19 shares it.
- bKash merchant API for the subscription; manual bKash with a receipt screenshot for the first 50 doctors.
- A local bulk SMS gateway for Bangla follow-ups, roughly ৳0.25 to ৳0.50 per message; a Unicode Bangla font in the PDF; offline queueing because chamber internet drops.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for dictation parsing, Cloudflare plus a small VPS, bKash merchant API.

1. Ask Claude for the schema, run the migrations it returns, then import the drug CSV.
```
Design a PostgreSQL schema for a doctor prescription app in Bangladesh.
Tables: doctors, chambers, patients, visits, prescriptions, prescription_items,
drugs (brand, generic, strength, form, manufacturer, dgda_reg_no), follow_ups.
Items store dose_pattern like "1+0+1", duration_days, meal_relation and a
Bangla instruction. Add tenant_id everywhere. Output SQL and a seed CSV format.
```
2. Ask Claude to build the prescription editor with drug autocomplete, dose picker and live Bangla preview, then the A5 PDF, the SMS cron job and the bKash subscription flow.
3. Ask Claude for the dictation parser, wire it to the Claude API, match each brand_query against your drug table and let the doctor confirm every line.
```
You receive a doctor's dictation in mixed Bangla and English, for example
"রোগীর জ্বর তিন দিন, napa extend 1 plus 0 plus 1 seven days after meal".
Return JSON: complaints[], diagnosis, items[] {brand_query, dose_pattern,
duration_days, meal_relation}, advice[], follow_up_days. Do not invent drugs.
Advice in simple Bangla. Return only JSON.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: MVP live in 10 real chambers | 500 prescriptions printed |
| Day 60: paid plans open | 40 paying doctors, ৳40,000 MRR |
| Day 90: two chamber chains signed | 120 paying doctors, ৳1.2 lakh MRR |

### First customers with zero budget
- Diagnostic centres and pharmacies that host 5 to 20 chambers each; give the centre a free dashboard when its doctors sign up.
- Facebook groups such as Doctors Community Bangladesh, and medical reps, paid ৳200 per referral.
- Outreach angle: "Your patients cannot read your prescription. Print it in 60 seconds, in Bangla, on your letterhead."
- Demo that closes: sit in the chamber one evening and print the first 10 prescriptions live.
- Referral loop: the printed footer names the product; three referrals earn a free month.

### Pricing and the maths
- Solo ৳500/month (one chamber), Chamber ৳1,000/month (unlimited prescriptions, 500 SMS), Multi-chamber ৳1,500/month (three chambers, assistant login).
- Cost of goods: Claude roughly ৳1 to ৳2 per dictated prescription, SMS about ৳0.30 each, hosting about ৳3,000 a month. Gross margin above 80 percent.
- ৳3 lakh a month is roughly 300 doctors at the mid price of ৳1,000.

### Country kit: taking it to other languages
- First port: Nepal, small but with one drug regulator list and almost no competition; then Pakistan with the DRAP brand list and Urdu instructions.
- What changes: drug table, instruction language pack, SMS gateway, payment rail (eSewa in Nepal, JazzCash in Pakistan).
- What stays: schema, editor, parsing prompt, PDF engine. Reseller: a local medical-rep company or diagnostic chain.

### Risks and how to de-risk them
- Risk: a wrong drug or dose from voice parsing harms a patient. De-risk: the AI only proposes, the doctor confirms every line, the generic shows beside the brand.
- Risk: doctors will not type. De-risk: assistant login so the compounder enters and the doctor signs.
- Risk: the drug database goes stale. De-risk: a monthly DGDA refresh and a "report missing drug" button answered within a day.

## Idea 19: Pharmacy POS with Drug Database
*Barcode billing, expiry alerts and Bangla drug information for the 100,000-plus pharmacies that must now keep proper records.*

### Who pays and why now
The customer is the owner of a neighbourhood pharmacy, usually the person behind the counter, with 1,500 to 4,000 products bought on credit from 10 to 20 distributors. Today stock is checked by eye, expired strips are found by customers and supplier dues sit in a notebook.

The owner pays because expiry losses alone can exceed the subscription and supplier disputes never stop. The moment is right because the model-pharmacy programme and DGDA inspections push pharmacies towards records, owners are buying scanners anyway, and the drug database from idea 8 already exists. Port countries are Pakistan, Nepal, Nigeria and Egypt, each with its own drug database.

### The product in 30 days (MVP)
- Barcode or search-based sales screen that works keyboard-only on a cheap laptop.
- Pre-loaded drug master with brand, generic, strength and MRP.
- Purchase entry by distributor invoice with batch and expiry; alerts at 90, 60 and 30 days.
- Supplier dues ledger with payment history.
- Bangla drug information slip by print or SMS, and a daily sales and profit summary.
- Leave out: multi-branch, accounting integration, online ordering, customer loyalty.

### Data, integrations and the Bangladesh specifics
- Drug database shared with idea 8, with MRP and pack size added.
- bKash merchant API for the subscription; a payment method on each sale because customers pay by bKash too.
- SMS gateway for drug slips and alerts; a printable monthly stock register for inspectors.
- Offline first: power and internet cuts happen daily, so build a PWA with IndexedDB and background sync.

### Build it with Claude
Stack: Next.js PWA, PostgreSQL, Claude API for Bangla drug information, Cloudflare plus a small VPS, bKash merchant API, a USB barcode scanner.

1. Ask Claude for the schema and the offline design, then run the migrations.
```
Design a PostgreSQL schema and an offline-first sync plan for a pharmacy POS
in Bangladesh. Tables: pharmacies, users, drugs (shared master), pharmacy_stock
(batch_no, expiry_date, qty, purchase_price, mrp), purchases, purchase_items,
suppliers, supplier_payments, sales, sale_items. Sales must work offline in the
browser and sync later without duplicates: use UUIDs and a sync_queue table.
```
2. Ask Claude to build the sales screen: scanner input, quantity, discount, cash or bKash, print to a 58mm thermal printer. Test with a real scanner.
3. Ask Claude to generate the Bangla drug slips as a batch, have a pharmacist review 50, then cache the results. Never call the API at sale time.
```
For each generic in the attached list, write a patient information slip in
simple Bangla (max 60 words) with four parts: কী কাজে লাগে, কীভাবে খাবেন,
সাধারণ সতর্কতা, কখন ডাক্তার দেখাবেন. Do not give dosages; refer to the
doctor's instructions. Output CSV: generic, bangla_slip. Tone: respectful, plain.
```
4. Ask Claude for the expiry alert job, the supplier dues screen and the bKash subscription flow.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 10 pharmacies live | 5,000 items sold through the system |
| Day 60: paid plans open | 50 paying pharmacies, ৳50,000 MRR |
| Day 90: two districts covered | 150 paying pharmacies, ৳1.5 lakh MRR |

### First customers with zero budget
- Bangladesh Chemists and Druggists Samity local branches; attend the monthly meeting with a laptop and scanner.
- Facebook groups of pharmacy owners; Google Maps "pharmacy" by thana, best-reviewed shops first.
- Distributor sales reps visit each pharmacy weekly; pay a referral fee per signup.
- Demo that closes: scan 20 of their fast movers and show the expiry list from their own shelves.
- Referral loop: a free month per referred neighbour; pharmacies in one bazaar talk daily.

### Pricing and the maths
- Basic ৳499/month (one counter, 2,000 SKUs), Standard ৳999/month (unlimited SKUs, SMS slips, supplier ledger), Chain ৳1,499/month (three branches, owner dashboard).
- Cost of goods is near zero per sale: SMS slips about ৳0.30 each and hosting ৳3,000 to ৳5,000 a month. Gross margin above 85 percent.
- ৳3 lakh a month is roughly 300 pharmacies at the mid price of ৳999.

### Country kit: taking it to other languages
- First port: Nepal, then Pakistan. Nepal has one national drug list; Pakistan is ten times bigger with JazzCash and Easypaisa.
- What changes: drug master, currency and numerals, SMS gateway, payment rail, regulator register, language pack.
- What stays: POS, offline sync, supplier ledger, expiry engine. Reseller: pharmacy associations and scanner dealers.

### Risks and how to de-risk them
- Risk: the owner does not enter purchases, so stock is wrong. De-risk: photograph the distributor invoice, Claude extracts the lines, the owner confirms.
- Risk: a Bangla drug slip gives wrong advice. De-risk: no dosages, pharmacist review, a line that says follow the doctor.
- Risk: Excel or free POS tools compete. De-risk: the drug master and expiry alerts save real money; free tools have neither.

## Idea 25: Diagnostic Lab Report Delivery
*Lab reports by WhatsApp with a plain-Bangla explanation, a patient queue and referring-doctor commission tracking.*

### Who pays and why now
The customer is the owner of a private diagnostic centre with 5 to 40 staff running blood tests, ultrasound and X-ray. Today patients return the next day for a printed report they cannot understand. Referring doctors get a commission tracked in a notebook and paid in cash at month end, which causes disputes.

The owner pays for fewer return visits, a modern image and a clean commission statement that keeps doctors loyal. The moment is right because WhatsApp is on every patient's phone, its Business API is open to small firms, and Claude can turn a blood count into a paragraph a grandmother understands. Port countries are India, Pakistan, Nepal, Nigeria and Egypt.

### The product in 30 days (MVP)
- Patient registration with phone number, tests, referring doctor and bKash or cash payment.
- Queue board with token numbers on a TV screen.
- Report entry: PDF upload from the analyser or typed values per test.
- WhatsApp delivery of the report PDF plus a plain-Bangla summary and a "see your doctor" line.
- Referring-doctor ledger with commission per test and monthly statement; owner dashboard of tests, revenue and pending reports.
- Leave out: analyser integration, radiology image viewer, home sample collection, accounting.

### Data, integrations and the Bangladesh specifics
- WhatsApp Business API through a local provider, roughly ৳1 to ৳2 per utility message, with SMS as fallback.
- bKash merchant API and SSLCommerz for patient payments and your subscription.
- Reference ranges per test as editable data per lab, because analysers differ; Bangla fonts in the PDF.
- A printable test register for DGHS licensing; commission data stays owner-only.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Claude API for report explanations, WhatsApp Business API, Cloudflare plus a small VPS, bKash merchant API.

1. Ask Claude for the schema and run the migrations.
```
Design a PostgreSQL schema for a diagnostic lab in Bangladesh: labs, users,
patients, doctors (referring, commission_percent or fixed_per_test), tests
(name, price, reference_ranges JSON by age and sex), orders, order_items,
results (value, unit, flag), reports (pdf_url, whatsapp_status),
doctor_commissions, payments (bkash, cash, sslcommerz). Add tenant_id.
Output SQL and a monthly commission statement query.
```
2. Ask Claude for the reception screen and a full-screen queue board for a cheap Android TV box.
3. Ask Claude for the explanation feature; the technician edits the text before sending, and every message is logged.
```
You write for a Bangladeshi patient with no medical training. Given lab results
as JSON (test, value, unit, reference_range, flag), write 4 to 6 sentences in
simple Bangla: which results are within range, which are outside and what that
generally means, and a clear line to consult the referring doctor. Never
diagnose, never suggest medicines, never mention cancer or death. Plain text only.
```
4. Ask Claude for WhatsApp template registration, PDF sending with SMS fallback after 10 minutes, and the commission statement PDF.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 5 labs live | 2,000 reports delivered by WhatsApp |
| Day 60: paid plans open | 25 paying labs, ৳60,000 MRR |
| Day 90: three cities covered | 60 paying labs, ৳1.8 lakh MRR |

### First customers with zero budget
- Bangladesh Private Clinic and Diagnostic Owners Association district committees; present at a meeting.
- Google Maps: "diagnostic center" and "pathology lab" by district town; the ones with a Facebook page adopt first.
- Facebook groups of lab technologists, who influence owners; reagent salesmen, paid ৳500 per referral.
- Demo that closes: take one real report from their pile, generate the Bangla explanation and send it to the owner's WhatsApp.
- Referral loop: every WhatsApp report carries your footer; a lab that refers a sister lab gets a free month.

### Pricing and the maths
- Lab ৳1,499/month (300 reports, SMS fallback), Lab Plus ৳2,999/month (unlimited reports, WhatsApp, commission ledger), Multi-branch ৳4,999/month (four branches, central dashboard).
- Cost of goods: WhatsApp roughly ৳1.50 per report, Claude roughly ৳1 per explanation, hosting about ৳5,000 a month. Gross margin around 70 percent on Lab Plus.
- ৳3 lakh a month is roughly 100 labs at the mid price of ৳2,999.

### Country kit: taking it to other languages
- First port: Nepal or Pakistan; both have the same lab and referring-doctor structure and heavy WhatsApp use. Nigeria later.
- What changes: explanation language, reference-range defaults, payment rail, WhatsApp provider, regulator register.
- What stays: queue, reports, commission ledger, delivery engine. Reseller: reagent distributors and technologist associations.

### Risks and how to de-risk them
- Risk: an explanation frightens or misleads a patient. De-risk: technician review before sending, strict prompt rules, "consult your doctor" on every message, weekly audit.
- Risk: WhatsApp bans the account. De-risk: approved utility templates only, opt-in at registration, never send marketing.
- Risk: analyser integration requests stall sales. De-risk: sell typed and PDF upload first; add file-watch integration for the top three analysers in month four.

## Idea 56: Pharma Medical Rep CRM
*Doctor visit logs, samples, prescription feedback and Bangla daily reports for the medical reps that pharma companies still manage by phone.*

### Who pays and why now
The customer is the sales director of a mid-sized Bangladeshi pharmaceutical company with 50 to 500 medical representatives. Today reps phone their area manager every evening and fill paper call reports. Managers cannot see which doctors were visited or which brands are being prescribed.

The company pays because it spends far more on salaries and samples than on software, and a few percent more productive calls repays the tool many times over. The moment is right because every rep carries an Android phone, margins are under pressure, and the top ten firms have in-house tools the next 150 companies cannot afford. Port countries are India, Pakistan, Indonesia, Nigeria and Egypt.

### The product in 30 days (MVP)
- Doctor master per territory with specialty, chamber address and visit frequency class.
- Daily call plan and visit log with GPS check-in, brands detailed, samples and gifts given.
- Prescription feedback: which brands the doctor is prescribing, with a competitor note.
- Sample stock per rep, and distributor order capture from pharmacy visits sent by SMS.
- Manager dashboard: coverage, call average, missed doctors, an automatic Bangla daily report.
- Leave out: payroll and incentives, expense claims, e-detailing content, ERP integration.

### Data, integrations and the Bangladesh specifics
- The company brings its own doctor list; give an Excel import with de-duplication.
- Brand list from the shared drug database in ideas 8 and 19, filtered to the company's brands plus competitors.
- Companies pay by bank transfer against a VAT invoice (Mushak 6.3); bKash only for tiny firms.
- Offline-first Flutter app because reps work in areas with poor data; Bangla UI for reps.

### Build it with Claude
Stack: Flutter Android app for reps, Next.js dashboard for managers, PostgreSQL, Claude API for report summaries, a small VPS, invoice billing.

1. Ask Claude for the schema and territory model, then run the migrations.
```
Design a PostgreSQL schema for a pharma medical rep CRM in Bangladesh.
Tables: companies, territories (region > area > territory), users (rep, area
manager, regional manager, admin), doctors (specialty, class A/B/C, address,
lat, lng), call_plans, visits (check_in_at, lat, lng, brands JSON, samples
JSON, rx_feedback JSON, notes), sample_stock, distributors, orders,
order_items. Add role-based visibility. Output SQL and a monthly coverage query.
```
2. Ask Claude for the Flutter rep app: today's plan, doctor detail, a one-screen visit log, offline queue, big buttons and Bangla labels.
3. Ask Claude for the daily report generator, run at 8 pm for every rep and emailed to the area manager.
```
Given today's visits for one rep as JSON (doctor, specialty, brands detailed,
samples given, rx feedback, notes), write a daily call report in formal Bangla
for the area manager: 5 to 8 lines covering coverage against plan, key doctor
feedback, competitor mentions and tomorrow's priority. Use Bangla numerals.
Do not add anything not in the data.
```
4. Ask Claude for the manager dashboard and a two-page pilot proposal for a sales director.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: one pilot company, 20 reps | 3,000 visits logged |
| Day 60: three companies signed | 150 seats, ৳60,000 MRR |
| Day 90: six companies | 600 seats, ৳2.4 lakh MRR |

### First customers with zero budget
- Bangladesh Association of Pharmaceutical Industries member list; target companies ranked 20 to 150 by size.
- LinkedIn messages to sales directors asking for a 20-minute pilot call; Facebook groups of medical representatives, who pull managers in.
- Demo that closes: load their doctor list for one area, give five reps the app for a week, show the coverage dashboard to the director.
- Referral loop: area managers change companies often and carry the tool with them; a free month per referred company.

### Pricing and the maths
- Standard ৳299 per rep per month (visits, samples, daily reports), Pro ৳499 per rep per month (prescription analytics, distributor orders). Minimum 20 seats.
- Cost of goods: Claude roughly ৳0.50 per daily report, SMS a few taka per order, hosting about ৳5,000 a month. Gross margin above 85 percent.
- ৳3 lakh a month is roughly 750 seats at the mid price of ৳399, for example five companies of 150 reps.

### Country kit: taking it to other languages
- First port: Pakistan, which has a similar rep-heavy pharma industry; then Indonesia and Egypt.
- What changes: report language, doctor classification norms, brand list, invoicing and tax rules.
- What stays: territory model, Flutter app, offline sync, dashboards. Reseller: pharma consultants and former sales directors.

### Risks and how to de-risk them
- Risk: reps fake GPS check-ins. De-risk: mock-location detection, a photo of the chamber board on the first visit, manager spot audits.
- Risk: long enterprise sales cycles. De-risk: a paid 30-day pilot for one region at roughly ৳20,000 that converts into an annual contract.
- Risk: data leaves with a departing rep. De-risk: remote sign-out, no export for reps, the company owns all data.

## Idea 80: Medical Tourism Facilitator CRM
*Case files, hospital quotes, visa steps and Bangla family updates for the facilitators who send Bangladeshi patients to India, Thailand and Turkey.*

### Who pays and why now
The customer is a facilitator or small agency, often a former hospital coordinator or travel agent, helping 10 to 60 families a month get treatment abroad. Today reports arrive by WhatsApp, hospital quotes sit in email, visa dates live in a notebook, and nobody follows up with the patient who returned home two weeks ago.

The facilitator pays because one lost case is worth more than a year of software. The moment is right because outbound medical travel keeps rising, foreign hospitals pay facilitators through partner programmes that demand case records, and families expect WhatsApp updates. Port countries are Nigeria, Pakistan, Iraq, Afghanistan, Myanmar and Central Asia.

### The product in 30 days (MVP)
- Case file per patient: diagnosis summary, reports, passport, family contacts, destination and budget.
- Quote requests to partner hospitals by email template, compared in one table.
- Step tracker: visa, appointment, tickets, accommodation, interpreter, treatment, return.
- Payment ledger for advances, hospital deposits and commission, in taka and dollars.
- Bangla updates to the family at each step, and follow-up reminders at 7, 30 and 90 days after return.
- Leave out: flight and hotel booking engine, hospital-side portal, telemedicine, insurance.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for the subscription and patient advances; record dollar payments to hospitals, but do not process them.
- WhatsApp Business API or plain SMS for family updates; keep messages short for older relatives.
- Visa checklists per destination as editable data, updated as rules change.
- Patient files encrypted, with consent recorded on the case and a one-tap delete.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for report summaries and drafting, WhatsApp or SMS gateway, Cloudflare plus a small VPS, bKash merchant API.

1. Ask Claude for the schema and run the migrations.
```
Design a PostgreSQL schema for a medical tourism facilitator CRM in Bangladesh.
Tables: agencies, users, patients, cases (diagnosis_summary, destination_country,
status), documents, hospitals (country, specialties, contact), quotes
(hospital_id, amount, currency, inclusions, valid_until), case_steps (step,
due_date, done_at), payments (party, direction, amount, currency, method),
followups, message_log. Add tenant_id. Output SQL and an overdue-steps query.
```
2. Ask Claude for the case screen: timeline, documents, quotes and one button to update the family.
3. Ask Claude for the summary drafter; the facilitator edits both drafts before sending.
```
You receive extracted text from a Bangladeshi patient's medical reports and a
short note from the facilitator. Write (a) a one-page clinical summary in
English for a foreign hospital's international patient desk: history, current
diagnosis, key results with dates, medicines, and the question being asked;
(b) a 4-line Bangla message for the family explaining what happens next.
Do not invent findings. Mark unclear items as "to confirm".
```
4. Ask Claude for the step tracker with automatic Bangla messages, the follow-up scheduler and the dual-currency ledger.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 3 facilitators live | 40 active cases |
| Day 60: paid plans open | 15 paying facilitators, ৳75,000 MRR |
| Day 90: two hospital desks referring | 40 paying facilitators, ৳2 lakh MRR plus case fees |

### First customers with zero budget
- Facebook groups where facilitators advertise: treatment-in-India groups and Vellore, Bangkok, Apollo and Fortis patient communities.
- Google Maps: "medical tourism" and "medical visa assistance" in Dhaka, Chattogram, Sylhet and Khulna.
- Indian hospital representative offices in Dhaka, which know every serious facilitator.
- Demo that closes: take one live WhatsApp case, build the case file in 10 minutes, generate the English summary and send the family a Bangla update.
- Referral loop: a facilitator who refers a peer gets a month free.

### Pricing and the maths
- Solo ৳2,999/month (one user, 30 active cases), Agency ৳5,999/month (five users, unlimited cases, WhatsApp), Enterprise ৳9,999/month (branches, analytics), plus a per-case fee of roughly ৳200 to ৳500 above quota.
- Cost of goods: Claude roughly ৳5 to ৳10 per case, WhatsApp a few taka per case, hosting about ৳5,000 a month. Gross margin above 80 percent.
- ৳3 lakh a month is roughly 46 agencies at the mid price of ৳6,499, or fewer once case fees are added.

### Country kit: taking it to other languages
- First port: Nigeria, where outbound medical travel to India and Turkey is large and facilitators work the same way; then Pakistan and Iraq.
- What changes: family message language, visa checklists, payment rail (Paystack, JazzCash), currency pairs.
- What stays: case file, quotes, step tracker, follow-up engine, English summary. Reseller: hospital international-patient desks.

### Risks and how to de-risk them
- Risk: a patient data breach involving foreign hospitals. De-risk: encryption, expiring share links, consent recorded on the case file.
- Risk: the AI summary misses or invents a finding. De-risk: a mandatory edit step, "to confirm" markers, original reports always attached.
- Risk: hospitals build their own facilitator portals. De-risk: your value spans hospitals and includes the family side; integrate rather than compete.

## Idea 86: Rural Medical Practitioner App
*Patient records, Bangla symptom guidance, drug warnings and referral letters for the village doctors who are the first contact for most Bangladeshis.*

### Who pays and why now
The customer is the village doctor or drug seller, the palli chikitshok in a union bazaar, seeing 20 to 60 patients a day and selling the medicines he recommends. Today there are no records, dosing is from memory, nobody checks interactions, and referrals are verbal.

He pays because ৳99 to ৳299 a month is less than the margin on a few sales, and the app makes him look trained and careful in front of patients and inspectors. The moment is right because smartphones reach every bazaar, government and NGO programmes now train informal providers rather than ban them, and pharma companies want a channel to them. Port countries are India, Pakistan, Nigeria and Kenya.

### The product in 30 days (MVP)
- Patient list by phone number with age, sex, past visits and chronic conditions.
- Visit note: symptoms from a Bangla list, vitals, medicines given.
- Bangla symptom guidance: red flags to refer immediately, common causes, what not to give.
- Dose and interaction warnings from the shared drug database, with paediatric dosing help.
- Bangla referral letter to the upazila hospital, medicine stock alerts and a follow-up SMS.
- Leave out: billing and accounting, telemedicine video, lab orders, NGO reporting dashboards.

### Data, integrations and the Bangladesh specifics
- Drug database shared with ideas 8 and 19, plus interaction pairs and paediatric dose rules reviewed by a pharmacist and a doctor.
- Guidance content follows national treatment guidelines and WHO IMCI red flags, stored as editable content.
- bKash and Nagad for the subscription, with a yearly prepaid option because monthly renewals fail in rural areas.
- Offline-first Android app; an organisation account so NGOs and pharma companies can sponsor groups.

### Build it with Claude
Stack: Flutter Android app, Laravel API with PostgreSQL, Claude API for content creation (not at the point of care), a small VPS, bKash and Nagad.

1. Ask Claude for the content schema and 20 symptom entries; a doctor reviews every entry before it ships.
```
Create a JSON content schema for symptom-based guidance used by informal rural
health providers in Bangladesh. Each entry: name_bn, name_en, red_flags_bn[]
(refer immediately), common_causes_bn[], safe_first_steps_bn[], do_not_give_bn[],
refer_when_bn[]. Fill it for fever, cough, diarrhoea, vomiting, abdominal pain,
headache and 14 more common complaints. Follow Bangladesh national guidelines
and WHO IMCI red flags. Simple Bangla, no brand names.
```
2. Ask Claude for the Flutter screens: patient search, visit note with big Bangla buttons, guidance panel, referral letter. Test on a ৳10,000 phone.
3. Ask Claude for the warning rules, have a pharmacist review them, then load them as data checked on the phone.
```
From the shared drug table (generic, strength, form) produce a rules CSV:
(a) 150 common interaction pairs among drugs sold in Bangladeshi rural
dispensaries, each with a one-line Bangla warning and severity; (b) weight-based
paediatric dose ranges for paracetamol, amoxicillin, ORS, zinc and 10 more
common generics, each with a Bangla dosing sentence and the reference used.
```
4. Ask Claude for the referral letter template, the SMS scheduler and the sponsor account.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: free trial in two upazilas | 50 practitioners, 3,000 visits logged |
| Day 60: paid plans open | 300 paying practitioners, ৳60,000 MRR |
| Day 90: first sponsor signed | 1,000 paying practitioners, ৳2 lakh MRR |

### First customers with zero budget
- Facebook groups of palli chikitshok and RMP training alumni, with tens of thousands of members.
- Upazila-level practitioner associations; offer each a free group dashboard.
- Pharma distributors who supply village dispensaries, and NGO programmes that train informal providers.
- Demo that closes: on his own phone, enter one patient, show the red-flag list for a child's fever and print a referral letter.
- Referral loop: five invited colleagues earn a year free.

### Pricing and the maths
- Basic ৳99/month (records, guidance), Plus ৳199/month (drug warnings, referral letters, SMS), Pro ৳299/month (stock, sponsor reporting).
- Cost of goods is near zero: SMS about ৳0.30 each and hosting about ৳5,000 a month. Gross margin above 85 percent.
- ৳3 lakh a month is roughly 1,500 practitioners at the mid price of ৳199, or fewer with sponsors.

### Country kit: taking it to other languages
- First port: India, starting with West Bengal in Bangla and then Hindi; then Nigeria's patent medicine vendors.
- What changes: guidance language and national guidelines, drug list, referral facility list, payment rail (UPI, Paystack, M-Pesa).
- What stays: app, content schema, rule engine, sponsor accounts. Reseller: NGO health programmes and pharma distributors.

### Risks and how to de-risk them
- Risk: guidance is misused as a licence to treat. De-risk: refer-first design, red flags first, no antibiotic recommendations, medical review of all content.
- Risk: regulators object to a tool for informal providers. De-risk: align with government training curricula and partner with an NGO.
- Risk: a very low price makes support unaffordable. De-risk: community support in Facebook groups and in-app Bangla videos; no phone support on Basic.

## Idea 87: Private Clinic and Small Hospital OS
*Outpatient queue, bed board, package billing, Bangla discharge summaries and doctor share statements for 10 to 50 bed clinics.*

### Who pays and why now
The customer is the owner of a private clinic with 10 to 50 beds in a district town, usually a doctor or a group of investors, with an outpatient department, a small lab, a pharmacy counter and an operating theatre. Today there is an admission register, a handwritten discharge bill disputed item by item, and doctor shares calculated on paper at month end.

The owner pays because a clinic of this size leaks revenue daily through missed charges and unpaid bills, and hospital software sold in Bangladesh is priced for 300 beds. The moment is right because DGHS licence renewals demand records, patients pay by bKash and expect a printed bill, and the owners' children are joining with laptops. Port countries are Pakistan, Nigeria, Nepal, Indonesia, Egypt and Kenya.

### The product in 30 days (MVP)
- Outpatient registration, token queue and fee collection.
- Admission and bed board: wards, cabins, occupancy, transfers.
- Charge capture: bed days, procedures, theatre, doctor visits, pharmacy and lab items.
- Package rates such as caesarean, with inclusions and extras.
- Discharge with final bill, Bangla discharge summary and monthly doctor share statements.
- Leave out: full accounting, HR and payroll, insurance claims, radiology imaging.

### Data, integrations and the Bangladesh specifics
- bKash merchant API and SSLCommerz for patient payments; card terminals recorded by reference number.
- SMS for tokens and follow-up; drug and test masters shared with ideas 19 and 25.
- Printable admission and theatre registers in the DGHS format; Bangla discharge summary.
- A local clinic server with cloud sync, because an internet cut during an admission is unacceptable.

### Build it with Claude
Stack: Laravel web app on a local server or the cloud, PostgreSQL, Claude API for discharge summaries, a small VPS, bKash merchant API and SSLCommerz.

1. Ask Claude for the schema and run the migrations.
```
Design a PostgreSQL schema for a 10 to 50 bed private clinic in Bangladesh.
Tables: clinics, users (reception, nurse, billing, pharmacy, lab, doctor, owner),
patients, opd_visits (token, doctor, fee), admissions (bed_id, admit_at,
discharge_at), beds (ward, type, rate), charges (admission_id, type, item, qty,
rate, posted_by), packages (name, inclusions JSON, price), bills, payments,
doctor_shares (doctor_id, charge_id, share_percent, amount), discharge_summaries.
Output SQL and a monthly doctor share statement query.
```
2. Ask Claude for the bed board and charge capture screens; a nurse posts a charge in three taps.
3. Ask Claude for the discharge summary drafter; the doctor reviews and signs.
```
Write a discharge summary for a Bangladeshi private clinic from this JSON:
admission diagnosis, procedures, key findings, discharge medicines (brand, dose
pattern, duration), follow-up date, doctor. Produce (a) a formal English clinical
summary for the file; (b) patient instructions in simple Bangla: medicines and
how to take them, warning signs to return for, follow-up date. Do not add
clinical content that is not in the data.
```
4. Ask Claude for the package billing logic, the payment integrations, the doctor share PDF and an owner's daily summary SMS.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 2 clinics live | 500 patients billed |
| Day 60: paid plans open | 8 paying clinics, ৳45,000 MRR |
| Day 90: pharmacy and lab modules live | 20 paying clinics, ৳1.3 lakh MRR |

### First customers with zero budget
- Bangladesh Private Clinic and Diagnostic Owners Association district committees; ask for 15 minutes at a meeting.
- Google Maps: "private hospital", "clinic" and "nursing home" in district towns, filtered to 10 to 50 beds.
- Medical equipment and reagent suppliers who visit these clinics; pay roughly ৳2,000 per referral.
- Demo that closes: build one caesarean package bill from their real rate card and show how many items the handwritten bill missed.
- Referral loop: owners know other owners in the district; a free month per referral.

### Pricing and the maths
- Up to 10 beds ৳2,999/month, 11 to 25 beds ৳5,999/month, 26 to 50 beds ৳9,999/month, with unlimited users, plus a one-time onboarding fee of roughly ৳10,000 to ৳20,000.
- Cost of goods: hosting ৳5,000 to ৳10,000 a month, Claude a few taka per discharge, SMS about ৳0.30 each. Gross margin above 80 percent.
- ৳3 lakh a month is roughly 46 clinics at the mid price of ৳6,499.

### Country kit: taking it to other languages
- First port: Nepal, with hundreds of similar nursing homes and few affordable systems; then Pakistan and Nigeria, far larger with the same doctor-share culture.
- What changes: language pack, payment rail, regulator registers, drug and test masters, tax invoice format.
- What stays: bed board, charge capture, packages, doctor shares. Reseller: equipment dealers and hospital consultants.

### Risks and how to de-risk them
- Risk: implementation is heavy and stalls. De-risk: a fixed two-day onboarding, import templates, OPD and billing first, pharmacy and lab in week three.
- Risk: staff resist because handwritten bills allowed leakage. De-risk: sell to the owner and show the leakage report.
- Risk: the local server fails and data is lost. De-risk: hourly cloud sync, daily backups, a restore drill at onboarding.


---

# Section 4: Health (Part 2)

Health in Bangladesh is delivered by many hands outside hospitals: paravets in villages, community health workers on foot, caregivers in homes, counsellors on video, patients with glucometers, and ambulance drivers at hospital gates. The six ideas in this section give each of those groups a record-keeping system that pays for itself, and each one has a natural buyer abroad.

## Idea 50: Paravet Field App
*A phone app where a village paravet records every vaccination and treatment, keeps medicine stock, and sends farmers SMS reminders in Bangla.*

### Who pays and why now
Paravets are the livestock service providers of rural Bangladesh. Trained by the Department of Livestock Services or by NGOs, they vaccinate cattle, goats and poultry, treat sick animals and sell medicine from a bag. Their records live in a notebook or in memory. Booster doses are missed, visit fees go unpaid, and vaccines expire in the bag.

The paravet pays directly, or an NGO livestock programme pays for a hundred paravets at once because its donor wants coverage data. Vaccine and feed companies are a third buyer. The moment is right because every paravet carries an Android phone and farmers read SMS. Port countries are India, Pakistan, Kenya, Nigeria and Ethiopia.

### The product in 30 days (MVP)
- Farmer register with phone, village and animals by species, with tag or photo.
- Visit log: animal, symptoms, treatment, medicine used, fee charged, paid or due.
- Vaccination calendar per species that sets the next due date automatically.
- Bangla SMS to the farmer three days before a due date, signed with the paravet's name.
- Medicine stock with low-stock and expiry alerts.
- Weekly disease summary by village, exportable as Excel; offline first with sync.
- Leave out: AI photo diagnosis, a farmer-facing app, multi-paravet teams, a medicine marketplace.

### Data, integrations and the Bangladesh specifics
- bKash for individual paravets; NGO programmes pay by bank transfer against an annual invoice.
- Local bulk SMS gateway. Bangla Unicode uses more segments, so keep reminders under 70 characters.
- Vaccination schedule table built from the standard schedules published by the Department of Livestock Services, editable by the paravet.
- Bangla fonts and numerals, large buttons for use in a cattle shed, and a data rule: the paravet owns farmer records, a sponsoring NGO sees aggregates only.

### Build it with Claude
Stack: Flutter Android app with local SQLite, Laravel API with PostgreSQL on a small VPS, local SMS gateway, bKash for subscriptions, Claude API for Bangla report summaries.

1. Ask Claude for the offline-first data model and paste it into your Laravel migrations and the Flutter local schema.

```
Design a PostgreSQL schema plus a matching SQLite schema for a paravet field app.
Entities: paravet, farmer, animal (species, tag, photo), visit (diagnosis, treatment,
fee, paid), medicine_stock, vaccination_schedule, vaccination_due, sms_log.
Every table needs a uuid, created_at, updated_at and a sync_status column.
Explain the conflict rule when the same visit is edited on phone and server.
```

2. Ask Claude for the Flutter screens: farmer list, add visit, due list, stock. Iterate until a visit takes under one minute.
3. Ask Claude for the reminder job and message text.

```
Write a Laravel job that runs nightly, finds vaccinations due in 3 days, and queues
one Bangla SMS per farmer. Message under 70 characters, includes animal type, vaccine
name, due date in Bangla numerals and the paravet's name. Give me 3 message variants
and the Bangla text for the paravet's app notification.
```

4. Ask Claude for the sync endpoint, an NGO supervisor dashboard with coverage per village, and a Bangla WhatsApp message asking an upazila livestock officer for ten minutes at the monthly paravet meeting.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 paravets in one upazila, 500 animals registered |
| Day 60 | 60 paravets, 5,000 animals, one NGO pilot signed |
| Day 90 | 200 paying paravets or two NGO contracts, roughly ৳60,000 a month |

### First customers with zero budget
- The upazila livestock office holds the list of trained paravets and hosts a monthly meeting. Ask for ten minutes.
- NGO livestock programme managers via NGO Affairs Bureau listings and LinkedIn. Lead with the coverage report.
- Facebook groups for cattle and goat farmers, where paravets answer questions daily.
- Vaccine and feed company reps visit paravets weekly and will carry a flyer for a small referral fee.
- The demo that closes: register the paravet's own regular farmer, set a vaccine, and let the farmer receive the SMS while both watch.
- Referral loop: every SMS names the paravet, so farmers ask other paravets why they do not send reminders.

### Pricing and the maths
- ৳199 to ৳599 per month per paravet, or a per-programme price for NGOs.
- SMS is the main cost at roughly ৳0.30 to ৳0.50 per message; hosting is a few thousand taka a month. Cap reminders per plan and gross margin stays above 80 percent.
- At the mid price of ৳399, roughly 750 paying paravets make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya. Community animal health workers are organised, NGOs pay in dollars, and M-Pesa is universal.
- What changes: language pack, vaccination schedule table, payment rail, SMS gateway.
- What stays: data model, offline sync, visit workflow and reminder engine; veterinary input companies resell it.

### Risks and how to de-risk them
- Risk: paravets will not type in a shed. De-risk: dropdowns, photos and voice notes; a visit under a minute.
- Risk: individual paravets cannot pay. De-risk: NGOs and vaccine companies sponsor seats.
- Risk: SMS costs eat the margin. De-risk: cap messages per plan and shorten texts.
- Risk: an NGO claims farmer data. De-risk: write the paravet-owns rule into the contract on day one.

## Idea 69: Community Health Worker App
*An offline-first app for community health workers to record household visits, track mothers and children, send vaccination reminders and produce the programme's monthly report.*

### Who pays and why now
Tens of thousands of community health workers walk door to door in Bangladesh for NGOs, urban health projects and social enterprises. Each carries paper registers: households, pregnant women, children under five, referrals, stock. At month end a supervisor copies them into Excel for the donor. Errors are common and data arrives weeks late.

The customer is the programme, not the worker. Managers pay $5 to $10 per worker per month from donor budgets because digital reporting is now a funding condition. Donors want near real-time data, low-end Android phones cost under ৳10,000, and workers already use WhatsApp. Port countries are Pakistan with its lady health workers, Kenya, Nigeria, Ethiopia and Indonesia.

### The product in 30 days (MVP)
- Household register: members, pregnancy status, children under five, phone, location.
- Visit forms for antenatal, postnatal and child visits, with danger signs and a referral button.
- Vaccination due lists per child from the national EPI calendar, with SMS reminders to mothers.
- Referral slip to the nearest facility with follow-up status.
- Medicine and supply stock per worker.
- Supervisor dashboard: visits per worker, coverage per village, monthly export in the programme's format; offline first with sync.
- Leave out: DHIS2 integration, telemedicine, payroll, a patient-facing app.

### Data, integrations and the Bangladesh specifics
- Payment in dollars by Stripe or bank invoice; local NGOs pay by bank transfer.
- SMS to mothers in Bangla through a local gateway; workers get in-app notifications to save cost.
- The national EPI schedule as an editable data table, and report columns copied from the programme's current Excel report.
- Offline SQLite, Bangla fonts, low-memory phones, consent text in Bangla, encryption at rest and per-programme data isolation.

### Build it with Claude
Stack: Flutter Android app with SQLite, Next.js dashboard with PostgreSQL on a small VPS or Cloudflare, local SMS gateway, Stripe for programme billing, Claude API to draft monthly narrative reports in Bangla.

1. Ask Claude for a form engine, not fixed forms, because programmes change checklists often.

```
Design a JSON form schema for a community health worker app: field types text, number,
date, single choice, multi choice, photo, GPS. Support conditional questions (show
"danger signs" only if pregnant), required fields and a Bangla and English label per
field. Then write the Flutter widget that renders any form from this JSON and stores
answers offline. Include one complete antenatal visit form in Bangla as an example.
```

2. Ask Claude for the household and child models, the EPI due-date calculator and the sync API. Test the calculator against ten real birth dates.
3. Ask Claude for the supervisor dashboard.

```
Write a Next.js page for programme supervisors. Show a table of workers with visits
this month, households covered, children overdue for vaccination and referrals pending.
Add an Export button that produces an .xlsx matching these columns: [paste the programme's
report header row]. Data comes from PostgreSQL; write the SQL views too.
```

4. Ask Claude for a two-page pilot proposal in Bangla and English (60 days, 20 workers, conversion terms) and a half-day worker training script.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | One pilot programme, 20 workers, 1,000 households |
| Day 60 | Three programmes, 100 workers, first paid invoice |
| Day 90 | 300 paid worker seats, roughly $2,250 a month |

### First customers with zero budget
- NGO health programme managers and M&E officers on LinkedIn; message them about their monthly report, not your app.
- The NGO Affairs Bureau list of registered NGOs, filtered to health and nutrition projects.
- Urban health projects run by city corporations with NGO partners, and clinic chains with outreach workers.
- The demo that closes: one worker's day in the app, then the supervisor dashboard filling up live.
- Referral loop: M&E officers move between NGOs and carry the tool; ask each pilot for one introduction.

### Pricing and the maths
- $5 to $10 per worker per month, paid by the programme, minimum 20 workers.
- Costs are SMS, hosting and support visits; gross margin is above 85 percent.
- ৳3 lakh is roughly $2,500. At $7.50 per worker, roughly 330 seats, or three to four mid-sized programmes.

### Country kit: taking it to other languages
- First port: Kenya. Community health programmes are large and organised, English works, donors pay in dollars.
- What changes: language pack, EPI table, report templates, SMS gateway.
- What stays: form engine, household model, offline sync, dashboard; international NGOs resell across ports.

### Risks and how to de-risk them
- Risk: NGO procurement takes months. De-risk: a free 60-day pilot with a signed conversion clause.
- Risk: free tools such as ODK and CommCare exist. De-risk: win on Bangla forms, local support and a price a small NGO can approve.
- Risk: sensitive health data. De-risk: encryption, isolation, consent screens, a written data policy.
- Risk: workers' phones are weak. De-risk: test every release on a ৳8,000 phone.

## Idea 90: Home Care and Nursing Agency OS
*Rosters, shift check-ins and care logs for home nursing agencies, with a daily WhatsApp update to the family, including families abroad who pay in dollars.*

### Who pays and why now
Home nursing agencies in Dhaka, Chattogram and Sylhet place caregivers with elderly and post-surgery patients. The agency runs on a phone book and a WhatsApp group. Nobody knows if the caregiver arrived on time, what the blood pressure was, or whether the evening medicine was given. Hours are disputed at billing time.

The agency pays per caregiver to look professional and to end disputes. The family, often a son or daughter in London, Dubai or New York, pays a separate plan in dollars to see the care log every evening. That family plan is the wedge: emotional, and priced in a strong currency. Demand rises as parents age at home while children work abroad. Port countries are India, the Philippines, Nigeria and Pakistan, plus every diaspora.

### The product in 30 days (MVP)
- Caregiver profiles with NID, training certificates and expiry dates.
- Patient profiles with care plan, medicines, allergies, emergency contacts.
- Shift roster with tap check-in and check-out, location stamped.
- Care log by tap: vitals, medicines given, meals, mood, notes and one photo.
- Daily WhatsApp summary to the family in Bangla or English, with alerts for missed medicines or abnormal vitals.
- Shift billing: hours per patient, invoice, caregiver payout statement.
- Leave out: a caregiver marketplace, video calls, payroll deductions, device integrations.

### Data, integrations and the Bangladesh specifics
- bKash for agencies and local families; Stripe for family plans abroad, billed in dollars.
- WhatsApp Business API for summaries and alerts; template messages need Meta approval, so submit them in week one.
- Certification records: Bangladesh Nursing and Midwifery Council registration where applicable, training certificates as photos.
- Care log in Bangla with large buttons; Bangla numerals for local families, Western numerals abroad; caregiver phone numbers hidden; vital ranges set per patient by the agency, never by the app.

### Build it with Claude
Stack: Flutter Android app for caregivers, Next.js portal for agencies and families, PostgreSQL, WhatsApp Business API, bKash and Stripe, Claude API to turn the day's log into a warm two-line summary.

1. Ask Claude for the schema and roster logic, including overlapping shifts and replacement caregivers.
2. Ask Claude for the caregiver app. Every entry must work with one thumb while standing.

```
Design 4 Flutter screens for a home caregiver app in Bangla: Today's Shift (check in,
check out), Vitals Entry (BP, pulse, temperature, sugar, big numeric keypad), Medicine
Checklist (tick each dose, reason if skipped), End of Day Notes (3 chips: good day,
some concern, urgent, plus optional text and photo). Minimum touch target 48dp.
Give me the Dart code and the Bangla labels.
```

3. Ask Claude for the daily family message and alert rules.

```
Write a Node job that runs at 8 pm Dhaka time and sends one WhatsApp template message
per patient to the family. Summarise today's care log in 2 lines, in Bangla or English
per family preference, list vitals, medicines given or missed, and end with the
caregiver's first name. Add an immediate alert rule when BP or sugar is outside the
patient's set range. Show the template text for Meta approval.
```

4. Ask Claude for billing (shift hours to invoice, payout statement, agency margin) and two outreach messages: agency owners in Bangla, diaspora children in English.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 agencies, 30 caregivers, 10 families receiving daily updates |
| Day 60 | 8 agencies, 200 caregivers, 30 family plans |
| Day 90 | 20 agencies, 600 caregivers, 100 family plans, roughly ৳1 lakh a month |

### First customers with zero budget
- Google Maps: "home nursing service" and "caregiver service" in Dhaka, Chattogram and Sylhet; call each listing.
- Facebook pages of nursing agencies, where families already ask for updates in the comments.
- Diaspora Facebook groups for Bangladeshis in the UK, US, Canada and the Gulf: post the family-side screenshot.
- Hospital discharge desks and geriatric physicians who refer families to agencies.
- The demo that closes: a caregiver logs a shift and the owner's own phone receives the family message within a minute.
- Referral loop: every daily message ends with an invite link that families share with friends abroad.

### Pricing and the maths
- ৳49 to ৳99 per caregiver per month for agencies, plus family plans priced in dollars.
- WhatsApp conversation fees are the main cost, then hosting; gross margin is roughly 70 to 80 percent.
- At the mid price of ৳74, agency seats alone need roughly 4,000 caregivers for ৳3 lakh a month, so family plans carry the business: roughly 1,500 seats plus roughly 400 family plans at roughly $5 reach the same figure.

### Country kit: taking it to other languages
- First port: India. Agencies are numerous, the diaspora pattern is identical, and Stripe works from day one.
- What changes: language pack, UPI instead of bKash, nursing council reference, WhatsApp number registration.
- What stays: care log, roster, family summary, billing, Stripe family plan; diaspora organisations resell it.

### Risks and how to de-risk them
- Risk: caregivers do not log. De-risk: tie payout statements to completed logs; keep every entry to a tap.
- Risk: agencies fear families will hire caregivers directly. De-risk: hide phone numbers; agencies control what families see.
- Risk: a family treats the app as medical advice. De-risk: agency-set ranges, disclaimers, alerts that say "call the agency".
- Risk: WhatsApp fees rise. De-risk: one summary a day, alerts only on exceptions, SMS fallback.

## Idea 99: Counsellor Practice and Teletherapy
*A booking page, intake form, video room, private notes and payments in taka or dollars for counsellors who work from a Facebook page and WhatsApp today.*

### Who pays and why now
Psychologists, counsellors and psychiatrists in Bangladesh mostly run private practice from a Facebook page. Clients message on WhatsApp, the counsellor finds a slot by scrolling, sends a Zoom link by hand, and chases a bKash payment afterwards. Session notes sit in a notebook or a phone memo. A no-show costs an hour; a lost note costs trust.

The counsellor pays because the tool saves an hour of admin a day and payment at booking removes the awkward chase. A growing share of clients are Bangla speakers abroad who want therapy in their own language and pay in dollars. Demand for therapy in Bangla rose fast once the pandemic normalised video sessions. Port countries are Pakistan, India, Nigeria, Indonesia and Egypt, and every diaspora in between.

### The product in 30 days (MVP)
- Public booking page in Bangla and English with availability and session types.
- Intake and consent form in Bangla completed before the first session.
- Payment at booking: bKash for local clients, Stripe for clients abroad, with sliding-scale codes.
- Video room link per session, with a phone audio fallback.
- Private session notes with templates (presenting issue, plan, next step), encrypted.
- Reminders by SMS or WhatsApp 24 hours and 1 hour before, with a reschedule link; monthly income report.
- Leave out: a public directory, insurance claims, group sessions, AI note-taking, a mobile app.

### Data, integrations and the Bangladesh specifics
- bKash payment link for local clients, Stripe for dollars; Lemon Squeezy for the counsellor's own subscription if Stripe payouts are hard.
- Video: an embedded open-source room or a Zoom or Google Meet link, chosen per counsellor; bandwidth-light option by default.
- Reminders by SMS in Bangla, WhatsApp when the client opts in; never include session content in any message; time zones handled per client.
- Confidentiality: encryption at rest, no analytics scripts on client pages, two-factor login, an access log the counsellor can view; receipts in Bangla numerals for local clients.

### Build it with Claude
Stack: Next.js with PostgreSQL on Cloudflare or a small VPS, bKash and Stripe, a local SMS gateway, an embeddable video room, Claude API to draft the counsellor's website copy in Bangla.

1. Ask Claude for the schema (client, session, payment, note, availability) and the encryption approach for notes. Review it against a security checklist.
2. Ask Claude for the booking flow.

```
Build the client booking flow in Next.js for a counsellor: pick session type (50 min
individual, 80 min couple), pick a slot from availability stored in PostgreSQL shown in
the client's time zone, fill a short intake form in Bangla or English, then pay by bKash
(BDT) or Stripe (USD) based on country. Support a sliding-scale code that changes the
price. Send confirmation by SMS and email. Give me the pages, API routes and the Bangla copy.
```

3. Ask Claude for the intake and consent text, then have a practising counsellor review it.

```
Write a client intake form for a Bangladeshi counselling practice in simple, respectful
Bangla: contact details, emergency contact, reason for seeking help (free text), current
medicines, previous therapy, consent to teletherapy, confidentiality statement and its
limits. Keep it under 300 words. Then give an English version with the same meaning.
```

4. Ask Claude for the notes module with templates and a session timer, the monthly report page, and three outreach messages for Facebook groups, LinkedIn and a university alumni WhatsApp group.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 counsellors live, 50 sessions booked |
| Day 60 | 40 counsellors, 400 sessions, first dollar payments |
| Day 90 | 100 paying counsellors, roughly ৳1 lakh a month |

### First customers with zero budget
- Professional bodies for clinical psychologists and counsellors, and alumni groups of the psychology departments at the large public universities.
- Facebook groups where counsellors discuss practice; offer to set up their booking page free on a live call.
- Counsellors whose Facebook pages say "inbox for appointment"; message them with their own page mocked up as a booking link.
- Diaspora Facebook groups, where someone asks for "a therapist who speaks Bangla" every week.
- The demo that closes: build the counsellor's booking page in ten minutes and take a real ৳10 test payment.
- Referral loop: every booking page carries a small "for practitioners" link, and full counsellors refer peers.

### Pricing and the maths
- ৳499 to ৳1,499 per month per counsellor.
- Costs are SMS, video minutes if you use a paid room, and hosting; Stripe fees pass to the client; gross margin is roughly 80 percent.
- At the mid price of ৳999, roughly 300 paying counsellors make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Similar practice patterns, a large diaspora, and JazzCash or Easypaisa in place of bKash.
- What changes: language pack, payment rail, consent wording, professional body references.
- What stays: booking, notes, encryption, Stripe, video, reminders; counsellor training institutes resell it white-label.

### Risks and how to de-risk them
- Risk: a confidentiality breach ends the business. De-risk: encryption, two-factor login, no third-party scripts, a tested incident plan.
- Risk: the counsellor pool is small. De-risk: include psychiatrists, coaches, speech and occupational therapists.
- Risk: cross-border payouts are hard for a Bangladeshi company. De-risk: Stripe through a foreign entity or Lemon Squeezy as merchant of record.
- Risk: video fails on weak connections. De-risk: audio-only fallback and a phone call button.

## Idea 100: Chronic Care Companion in Bangla
*A Bangla app for people with diabetes and high blood pressure: log readings, get medicine reminders, eat well with rice and local food, and let a child abroad watch over a parent.*

### Who pays and why now
Bangladesh has one of the highest diabetes rates in the world, and high blood pressure is nearly as common. A patient in Rangpur writes glucometer readings in a notebook, photographs them for a daughter in Toronto, and gets diet advice written for a Western plate. The doctor sees the notebook once in three months.

The consumer pays ৳99 to ৳299 a month, but the more reliable payer is the relative abroad who worries daily and pays in dollars for a family plan. Later, pharma companies, diabetes clinics and insurers sponsor subscriptions because adherence saves them money. Parents now own smartphones, remittance families pay for services back home, and the Claude API makes personalised Bangla meal advice cheap. Port countries are India, Pakistan, Egypt, Indonesia and Mexico.

### The product in 30 days (MVP)
- Log blood sugar (fasting, after meals), blood pressure and weight by tap or Bangla voice.
- Medicine reminders using Bangladeshi brand names, with a "taken" tap and a missed-dose nudge.
- Local food database with portions (rice, ruti, dal, fish, vegetables, sweets, tea) and a daily meal suggestion in Bangla.
- Family caregiver view with alerts when readings are out of range or logs stop.
- Monthly doctor report as a Bangla PDF with charts.
- Large fonts, Bangla numerals, gentle streaks and encouragement.
- Leave out: glucometer Bluetooth pairing, telemedicine, insulin dose calculation, wearables.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad for local subscribers; Stripe for family plans paid abroad; SMS reminders as a fallback for weak data.
- Food database built from published Bangladesh food composition tables, with portions in household measures (one cup rice, one ruti, one piece fish).
- Drug brand names from the same Bangladeshi drug database used by prescription and pharmacy tools.
- Bangla numerals and fonts everywhere, high contrast, a "read aloud" button; not a medical device, so no dosing advice, clear disclaimers, ranges set by the patient's doctor.

### Build it with Claude
Stack: Flutter for Android with offline logs, Next.js API with PostgreSQL on a small VPS, Claude API for meal suggestions and report narrative, bKash, Nagad and Stripe, local SMS gateway.

1. Ask Claude for the schema: patient, reading, medicine, reminder, food item, meal log, caregiver link, report, with several caregivers per patient.
2. Ask Claude for the food and meal engine.

```
Create a food database table for Bangladeshi meals with 150 common items: name in Bangla
and English, household portion (cup, piece, spoon), carbohydrate grams, calories, and a
glycaemic note (low, medium, high). Then write a Claude API prompt that takes today's
fasting sugar, the patient's usual foods and budget level, and returns a one-day meal plan
in simple Bangla, under 120 words, always using rice or ruti as the base.
```

3. Ask Claude for the logging screens and the caregiver dashboard.

```
Design the Flutter home screen for an elderly Bangladeshi diabetes patient: one big button
"সুগার লিখুন", one "প্রেসার লিখুন", today's medicines as tickable cards, and a 7-day chart.
Font size minimum 18sp, Bangla numerals, high contrast. Then design the caregiver screen
that shows the same for a parent, with a red banner when a reading is out of range or no
log for 2 days. Give Dart code and Bangla strings.
```

4. Ask Claude for the monthly Bangla PDF report with an English summary line for the doctor, a Facebook post aimed at children abroad, and a pharmacy counter card.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 300 installs, 100 weekly active patients |
| Day 60 | 2,000 installs, 300 paying, 100 family plans |
| Day 90 | 1,000 paying subscribers, roughly ৳2 lakh a month, one sponsor conversation |

### First customers with zero budget
- Facebook groups for diabetes patients and families in Bangla, where readings and diet questions are posted daily.
- Diabetic association hospitals and diabetes centres in district towns: ask endocrinologists to hand out a card.
- Pharmacies that sell glucometer strips: a counter card with a QR code and a small referral.
- Diaspora groups where adult children ask how to look after parents from abroad.
- The demo that closes: a patient logs a reading and the child abroad gets the alert during the call.
- Referral loop: every family plan invites siblings, and every monthly report carries the app name to the doctor.

### Pricing and the maths
- ৳99 to ৳299 per month for consumers, with family plans priced in dollars for relatives abroad.
- Costs are Claude API calls (cache meal plans by profile), SMS fallback and hosting; gross margin is roughly 80 percent.
- At the mid price of ৳199, roughly 1,500 paying subscribers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, starting with West Bengal in Bangla, then Hindi. Same rice diet, huge diabetes population, UPI payments.
- What changes: food database, drug brands, language pack, payment rail.
- What stays: logging, reminders, caregiver view, reports, Stripe family plans; pharma patient-support programmes resell it.

### Risks and how to de-risk them
- Risk: consumer churn after a month. De-risk: make the paying relative abroad the anchor and reminders useful daily.
- Risk: medical liability. De-risk: no dosing, doctor-set ranges, disclaimers, alerts that say "contact your doctor".
- Risk: nobody finds the app. De-risk: doctors and pharmacies as distribution, not app store ads.
- Risk: elderly users cannot set it up. De-risk: the child abroad sets it up remotely; voice replaces typing.

## Idea 102: Private Ambulance Dispatch
*Trip intake, driver assignment, transparent fare calculation, hospital handover records and equipment logs for private ambulance operators.*

### Who pays and why now
Hundreds of private ambulance operators in Bangladesh run 2 to 30 vehicles from a phone number painted on the side. Calls come in, the owner phones a driver, the fare is agreed by argument at the door, and the oxygen cylinder's level is a guess. Hospitals want handover records; families want a fair fare; owners want to know what each vehicle earned.

The operator pays ৳999 to ৳2,999 a month to stop losing trips, to end fare disputes with an SMS receipt, and to keep hospital relationships. Hospitals that outsource ambulance service are a second buyer for the same records. Ride-hailing has taught families to expect a quoted fare and a driver's name, and fuel prices make untracked trips hurt more. Port countries are Nigeria, Pakistan, India, Kenya, Indonesia and Egypt.

### The product in 30 days (MVP)
- Trip intake from phone, WhatsApp or web form: pickup, destination, ambulance type (basic, AC, ICU, freezer), patient notes.
- Driver and vehicle assignment with status: assigned, en route, picked up, delivered, closed.
- Fare calculator: per-kilometre by map distance plus package rates for city, intercity, waiting and freezer.
- SMS to the family with driver name, vehicle number, quoted fare and a bKash payment link.
- Driver app: start and end trip, odometer photo, expenses, hospital handover record with signature photo.
- Oxygen cylinder and equipment log per vehicle, with document expiry reminders.
- Leave out: a public booking app, live GPS for families, insurance billing, a multi-operator marketplace.

### Data, integrations and the Bangladesh specifics
- bKash payment link in the SMS; cash still recorded against the trip; operator subscription by bKash.
- SMS in Bangla with Bangla numerals for the fare, under 70 characters plus the link.
- Distance from a maps API for the quote, cached per route pair to control cost.
- Vehicle documents (fitness, tax token, route permit, insurance) with expiry reminders; driver app queues and syncs on patchy intercity networks.

### Build it with Claude
Stack: Next.js dispatcher console with PostgreSQL on a small VPS, Flutter Android driver app, maps distance API, local SMS gateway, bKash payment links, Claude API to parse WhatsApp trip requests into structured fields.

1. Ask Claude for the schema and the trip state machine, including cancellation and driver reassignment.
2. Ask Claude for the dispatcher console.

```
Build a Next.js dispatcher screen for an ambulance operator. Left: incoming trips with
pickup, destination, type and patient note. Centre: available vehicles with driver, type,
oxygen level and last trip. Right: fare quote from distance (per km rate by type) plus
package rates and waiting charge, editable before sending. One button sends the Bangla SMS
to the family and assigns the driver. Write the API routes and the SMS text.
```

3. Ask Claude to turn messy WhatsApp requests into trips.

```
Write a Claude API prompt and Node handler that takes a Bangla or English WhatsApp message
such as "ধানমন্ডি ২৭ থেকে স্কয়ার হসপিটাল, রোগী স্ট্রোক, এসি লাগবে" and returns JSON with
pickup, destination, ambulance_type, urgency and notes, with a confidence score. If
pickup or destination is missing, return the Bangla question the dispatcher should ask back.
```

4. Ask Claude for the driver app (three screens, odometer photo, handover record, offline), a daily settlement report per vehicle, and a WhatsApp pitch to operators who park outside major hospitals.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 operators, 200 trips logged |
| Day 60 | 15 operators, 1,500 trips, first hospital referral |
| Day 90 | 40 paying operators, roughly ৳80,000 a month |

### First customers with zero budget
- Google Maps: "ambulance service" in Dhaka, Chattogram, Sylhet, Rajshahi and Khulna; call every listing that answers.
- Facebook pages with "ambulance service" in the name, most run by owners themselves.
- The rows of ambulances outside the largest hospitals in each city; the owners sit in tea stalls nearby.
- Ambulance owner associations and hospital administrators who field fare complaints.
- The demo that closes: type a trip, quote the fare, and the owner's phone receives the family SMS in thirty seconds.
- Referral loop: the SMS receipt carries the operator's name; hospital staff notice which operators send receipts and ask the rest.

### Pricing and the maths
- ৳999 to ৳2,999 per month per operator, by fleet size.
- Costs are SMS, maps API calls and hosting, roughly ৳100 to ৳300 per operator a month; gross margin is above 80 percent.
- At the mid price of ৳1,999, roughly 150 paying operators make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria. Lagos and Abuja have many private operators, English works, and card and bank payment links are mature.
- What changes: payment rail, SMS gateway, fare zones and currency, vehicle document types.
- What stays: dispatch console, fare engine, handover records, driver app, equipment logs; private hospital groups resell it.

### Risks and how to de-risk them
- Risk: operators like fare haggling. De-risk: show that a quoted fare wins hospital contracts and repeat families.
- Risk: drivers ignore the app. De-risk: three taps per trip, and settlement only for trips in the system.
- Risk: maps API costs grow. De-risk: cache route pairs and allow manual distance entry.
- Risk: regulation of private ambulances tightens. De-risk: keep every record exportable so compliance becomes a selling point.


---

# Section 5: Education and Training

Bangladesh spends heavily on learning outside the classroom, from coaching centres and hifz madrasas to driving schools and BCS guides, and almost all of it runs on paper, Excel and WhatsApp groups. The eight businesses in this section sell simple software to the people who run those institutions and to the learners who pay them, and each one ports to another country by swapping a curriculum, a certificate or a test bank.

## Idea 7: Coaching-Centre OS
*Batches, attendance, bKash fees with Bangla reminders to parents, AI question papers from NCTB chapters and results by SMS.*

### Who pays and why now
Coaching centres are everywhere in Bangladesh, from one tutor with thirty students in a rented room to chains with several branches in a district town. Tens of thousands of them track batches in a notebook, take fees in cash and write question papers by hand the night before an exam.

Owners will pay for fees collected on time, parents kept informed, and question papers in five minutes instead of two hours. bKash merchant payments are now normal, and Claude can write curriculum-aligned questions in Bangla from an NCTB chapter. The product ports to India by state language, starting with West Bengal, then Pakistan, Nepal, Indonesia, Vietnam and Egypt, each with its own curriculum pack.

### The product in 30 days (MVP)
- Batch setup: subject, class, schedule, teacher, monthly fee.
- Student and guardian profiles with two phone numbers.
- Tap attendance on a phone, with an absent SMS to the guardian.
- Fee ledger with a bKash link and a Bangla reminder SMS three days before the due date.
- AI question paper: pick class, subject, NCTB chapter and marks, get a Bangla paper and answer key.
- Marks entry and result SMS to parents.
- Leave out: online classes, a student app, payroll, a website builder.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API first, Nagad second, SSLCommerz if a centre wants cards.
- SMS: a local bulk gateway with a masked sender. Bangla SMS costs about double a plain one, so keep reminders short.
- Curriculum: a table of class, subject, chapter and topics for classes 6 to 12 from NCTB textbooks.
- Bangla numerals and a font such as Noto Sans Bengali on every parent message and printed paper. Attendance queues offline and syncs later.

### Build it with Claude
Stack: Next.js mobile-first web app, PostgreSQL, Claude API, bKash merchant API, bulk SMS gateway, small VPS behind Cloudflare.

1. Ask Claude for the schema and admin screens. Check that every table has a coaching_centre_id.
```
Design a PostgreSQL schema for a coaching centre management app in Bangladesh.
Tables: coaching_centres, teachers, batches, students, guardians, attendance,
fee_invoices, payments (bKash transaction id, status), exams, marks, sms_log.
Multi-tenant by coaching_centre_id. Fees are monthly per batch.
Then write Next.js (App Router) pages for: batch list, student list with
guardian phones, tap-to-mark attendance, and a fee ledger per student.
```
2. Ask Claude for the bKash payment link flow, the reminder job and four Bangla SMS templates (fee due, received, absent, result). Test with a bKash sandbox account and your own phone.
3. Build the question paper feature. Load the NCTB chapter table, then use this as the system prompt in your Claude API call, passing chapter and marks.
```
You write exam question papers for a Bangladeshi coaching centre.
Input: class, subject, NCTB chapter name, list of topics, total marks, question mix.
Output in Bangla: a question paper with numbered questions, marks per question,
a mix of MCQ, short answer and creative questions as requested, then a separate
answer key. Use Bangla numerals. Match the difficulty of SSC or HSC board exams.
Do not invent topics outside the given chapter.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: MVP live, 5 centres onboarded by hand | 300 students, first bKash fee collected |
| Day 60: SMS and question generator polished | 25 centres, 10 paying |
| Day 90: referral loop, second district | 60 centres, 35 paying, roughly ৳35,000 a month |

### First customers with zero budget
- Facebook groups for coaching owners and district teachers. Post a free paper generated from a real NCTB chapter and ask who wants one for their next exam.
- Google Maps: search "coaching centre" in one district town, list 100, call or WhatsApp each one.
- Outreach angle: "Fees on bKash with automatic Bangla reminders to parents, set up in one hour, free for the first month." The demo that closes: generate a paper for a chapter the owner names, live on a phone, in under a minute.
- Referral loop: every parent SMS carries the centre's name and a footer; a free month for any centre that brings another.

### Pricing and the maths
- ৳499/month for up to 50 students, ৳999 for up to 200, ৳1,999 for multi-branch centres.
- Cost of goods is mostly SMS (roughly ৳0.50 to ৳1 each) plus a small Claude API cost per paper; gross margin is around 80 percent with SMS capped per plan.
- At the mid price of about ৳1,249, roughly 240 paying centres bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: West Bengal, India. Same language, same coaching culture, WBBSE curriculum instead of NCTB.
- What changes: curriculum table, payment rail (UPI, JazzCash, eSewa), SMS gateway, local board exam style. Sell through a reseller who already visits centres, such as a book distributor.
- What stays: schema, attendance, fee ledger, reminders, and the prompts with language and board swapped.

### Risks and how to de-risk them
- Risk: SMS costs eat the margin. De-risk: cap SMS per plan and sell extra bundles.
- Risk: a generated question has an error and the teacher loses trust. De-risk: always show an editable draft, never print directly, and ask teachers to rate each paper.
- Risk: owners keep taking cash and skip the link. De-risk: the ledger accepts cash too, and a monthly unpaid list shows why reminders pay.

## Idea 23: Bangla AI Exam Tutor
*Adaptive practice, Bangla explanations, mock tests and daily current affairs for BCS, bank job and university admission candidates.*

### Who pays and why now
Every year millions of Bangladeshis sit competitive exams: BCS preliminary, bank recruitment, primary teacher recruitment and university admission. They pay for coaching, printed guides and Facebook groups that post questions. Most study alone with a book, and nobody tells them which topics they keep getting wrong.

Candidates will pay a small monthly fee for practice that adapts to their weak areas, explains every answer in plain Bangla and gives a realistic mock test with a rank. Claude can write clear Bangla explanations on demand, and search demand for exam questions is enormous. This is a consumer, traffic and brand play, so content velocity matters more than features. Ports are India (state exams), Pakistan (CSS), Indonesia (CPNS), Nigeria (JAMB) and Vietnam.

### The product in 30 days (MVP)
- Question bank for one exam first (BCS preliminary), tagged by subject and topic.
- Practice mode: 10 questions at a time, instant Bangla explanation for each.
- Adaptive selection: more questions from topics the user gets wrong.
- Weekly mock test with timer, score and percentile among users.
- Daily current affairs digest in Bangla, 10 items with 5 practice questions.
- Public question pages, one URL per question, for search traffic.
- Leave out: video lessons, live classes, a native app, other exams until day 60.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad for monthly plans, SSLCommerz for cards. Keep checkout to two taps.
- Question bank: past BCS preliminary questions are public record. Type or OCR them, tag by syllabus, and have Claude write original explanations. Do not copy from published guides.
- Current affairs: summarise public news each morning, and a human checks the 10 items before publishing.
- Bangla numerals, a good Bangla web font, and small pages that load on a 2G connection.

### Build it with Claude
Stack: Next.js with server-rendered public pages, PostgreSQL, Claude API, bKash and Nagad checkout, Cloudflare for caching.

1. Ask Claude for the schema and the adaptive selection logic.
```
Design a PostgreSQL schema for an exam practice app: exams, subjects, topics,
questions (Bangla text, 4 options, correct option, explanation, source_year),
users, attempts, mock_tests, mock_results, subscriptions (bKash/Nagad).
Then write a SQL query or Node function that picks the next 10 questions for a
user, weighting topics by that user's wrong-answer rate over the last 200 attempts,
with 20 percent random questions from untouched topics.
```
2. Load 1,000 past questions. Use Claude to write explanations in batches of 20 and store them as drafts a reviewer approves.
```
You are a BCS preliminary exam tutor writing in simple Bangla.
For each question below, write: the correct answer, a 3 to 5 sentence explanation
a first-time candidate can follow, one memory trick, and the topic tag from this
list: [topic list]. Use Bangla numerals. Do not copy text from any guidebook.
Return JSON with fields: question_id, answer, explanation, trick, topic.
```
3. Ask Claude for the mock test screen with a timer and a results page showing percentile and weak topics, the public question page template (title, question, hidden answer, sign-up call), and the daily current affairs pipeline: fetch headlines, summarise, generate 5 MCQs, queue for review.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: BCS bank live with 1,000 questions, free tier | 2,000 registered users |
| Day 60: paid plan, mock tests, 3,000 questions | 10,000 users, 300 paying |
| Day 90: bank job pack added, public pages indexed | 30,000 users, 1,000 paying |

### First customers with zero budget
- BCS and bank job Facebook groups. Post one hard question a day with a link to the explanation on your site.
- University campus groups and dormitory WhatsApp groups before admission season.
- Outreach angle: "Find your five weakest BCS topics in 10 minutes, free." The demo that closes: a user answers 10 questions and sees a weakness chart with Bangla explanations.
- Referral loop: a free week of paid features for each friend who joins and completes a mock test.

### Pricing and the maths
- ৳99/month basic, ৳199/month with mock tests, ৳299/month with all exam packs, or a one-time exam pack in the same range.
- Cost of goods is Claude API usage for explanations (written once, served many times), hosting and payment fees, so gross margin is roughly 85 percent once the bank is built.
- At the mid price of ৳199, roughly 1,500 paying subscribers bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: a large Indian state exam in Hindi or Bengali, where the candidate pool is huge and past papers are public.
- What changes: question bank, syllabus tags, explanation language, payment rail (UPI), exam calendar. Partner with a local content teacher who owns tagging and review for a revenue share.
- What stays: adaptive engine, mock test, current affairs pipeline, public page template.

### Risks and how to de-risk them
- Risk: wrong answers or explanations destroy trust fast. De-risk: human review before publish and a "report error" button on every question.
- Risk: the bank grows too slowly. De-risk: two part-time reviewers paid per approved question.
- Risk: copyright claims from guidebook publishers. De-risk: only public past questions and original explanations, never scanned pages.
- Risk: churn after the exam date. De-risk: cross-sell the next exam pack and keep a free tier alive so users return.

## Idea 26: Hifz and Quran Madrasa Tracker
*Memorisation progress per student, daily sabaq and revision logs, teacher notes and parent updates in Bangla for hifz madrasas.*

### Who pays and why now
Bangladesh has tens of thousands of hifz madrasas, from a room beside a mosque with fifteen boys to residential institutions with hundreds of students. A hafiz teacher tracks each student's daily sabaq (new lesson), sabqi (recent revision) and manzil (older revision) in a notebook or in memory. Parents pay monthly fees and food costs and often hear nothing for months.

The head teacher or committee pays because parents want progress, and because a clear record settles arguments about how far a boy has reached. Smartphones are in every teacher's pocket and bKash is how parents already send money. The product pairs with the mosque fund manager and the hajj agency OS into a religious-institution suite. Ports are Indonesia, Pakistan, Nigeria, Malaysia, Turkey and diaspora mosques.

### The product in 30 days (MVP)
- Student profile with guardian phone, start date and current para (juz).
- Daily log per student: sabaq surah and ayah range, sabqi, manzil, quality grade, teacher note.
- Progress view: paras completed, pace per month, expected completion date.
- Weekly Bangla SMS or WhatsApp summary to the guardian.
- Monthly fee ledger with bKash link and reminder, plus attendance and leave records.
- Leave out: audio recitation grading, certificates, hostel and meal accounting, a parent app.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API for fees and donations, Nagad second.
- Messaging: SMS for guardians without smartphones, WhatsApp for those with one, both in Bangla.
- Quran reference dataset: 30 paras, 114 surahs, ayah counts and the para-to-surah mapping, so a teacher picks from a list instead of typing.
- Arabic and Bangla fonts on one screen, tested on cheap Android phones. Offline first, since many madrasas have weak signal.

### Build it with Claude
Stack: Flutter Android app for teachers, Next.js admin for the head teacher, PostgreSQL, Claude API for parent summaries, bKash merchant API, SMS gateway, small VPS behind Cloudflare.

1. Ask Claude for the data model and the Quran reference table. Load the reference table once and never let teachers edit it.
```
Design a PostgreSQL schema for a hifz madrasa tracker: madrasas, teachers, students,
guardians, daily_logs (date, sabaq_surah, sabaq_ayah_from, sabaq_ayah_to, sabqi_para,
manzil_para, grade 1-5, note), attendance, fee_invoices, payments (bKash), messages.
Also produce a seed table quran_reference with surah number, Arabic name, Bangla name,
ayah count and para number for all 114 surahs.
```
2. Ask Claude for the Flutter daily-log screen: pick student, pick surah from a list, enter ayah range with a number pad, tap a grade, save offline. Test on a ৳10,000 Android phone. Then ask for the progress chart.
3. Ask Claude for the weekly guardian summary generator, then the bKash fee link and reminder job.
```
Write a weekly progress message in simple Bangla for the guardian of a hifz student.
Input: student name, this week's new lessons (surah and ayah range per day), revision
paras, attendance out of 6 days, teacher's note, paras completed so far out of 30.
Output: 3 short sentences, respectful tone, Bangla numerals, no religious rulings,
under 300 characters so it fits two SMS. End with the madrasa name.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: app live, 3 madrasas logging daily | 150 students logged |
| Day 60: guardian messages and fee links on | 20 madrasas, 8 paying |
| Day 90: district cluster, suite bundle | 60 madrasas, 30 paying, roughly ৳20,000 a month |

### First customers with zero budget
- District ulama and madrasa teacher associations; one respected head teacher's approval opens ten doors.
- Google Maps: search "hifz madrasa" and "madrasa" by upazila and visit after Asr prayer.
- Outreach angle: "Parents get a weekly progress message in Bangla, and you never lose a student's record." The demo that closes: log one day for three students on the teacher's phone and send the sample guardian message to the teacher's own number.
- Referral loop: the guardian message carries the madrasa name, and parents ask other madrasas for the same.

### Pricing and the maths
- ৳299/month for up to 30 students, ৳599 for up to 100, ৳999 for larger or multi-branch madrasas.
- Cost of goods is SMS plus a tiny Claude API cost per weekly summary, so gross margin is roughly 80 percent with SMS capped.
- At the mid price of about ৳649, roughly 460 paying madrasas bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia, with the largest pesantren and tahfidz network in the world and mobile payments already common.
- What changes: guardian message language (Bahasa, Urdu, Hausa, Turkish), payment rail (GoPay, JazzCash, Paystack), local terms for sabaq and manzil. Diaspora mosques in the UK and US pay in dollars once the Bangla version works.
- What stays: Quran reference table, log structure, progress logic, offline app.

### Risks and how to de-risk them
- Risk: teachers do not log daily and data goes stale. De-risk: a 20-second log flow and a head-teacher dashboard showing who has not logged today.
- Risk: institutions are cautious about outsiders. De-risk: approach through a respected head teacher, keep messages free of religious opinion.
- Risk: very low fee tolerance in small madrasas. De-risk: a free tier for up to 15 students, and let committees or donors sponsor the plan.

## Idea 38: Sports Academy Manager
*Fees via bKash, attendance, batch scheduling, player progress cards in Bangla, match calendar and parent updates for cricket and football academies.*

### Who pays and why now
Every district town now has cricket and football academies, run by former players who train children morning and evening on a rented ground. Enrolment, fees and match schedules live in a WhatsApp group and a notebook. The coach chases fees between sessions, and parents ask the same question each week: is my child improving.

Owners pay because organised fee collection alone recovers the subscription many times over, and because a printed progress card in Bangla is something parents show relatives. Youth sport has become a paid activity for middle-class families, and parents expect the same SMS and bKash convenience they get from schools. Ports are India (cricket academies), Pakistan, Nigeria (football) and Indonesia.

### The product in 30 days (MVP)
- Academy, ground, coach and batch setup with weekly schedule.
- Player profile with guardian phones, age group, position, photo.
- Tap attendance per session, absent SMS to guardian.
- Monthly fee ledger, bKash link, Bangla reminders.
- Progress card: 6 to 8 skills rated monthly by the coach, a Bangla comment generated from the ratings, exported as a shareable image.
- Match and practice calendar with SMS notice to the batch.
- Leave out: video analysis, tournament management, a shop, a player app.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API, Nagad second. Many academies take cash, so the ledger accepts manual entries with an SMS receipt.
- Messaging: SMS for notices, WhatsApp broadcast where the batch group already exists.
- Skill templates: cricket (batting, bowling, fielding, fitness, discipline) and football (dribbling, passing, shooting, positioning, fitness, teamwork), editable per academy.
- Bangla progress card with Bangla numerals and the academy logo as a PNG parents forward on WhatsApp. Date of birth drives under-12, under-14 and under-16 groups.

### Build it with Claude
Stack: Next.js mobile-first web app, PostgreSQL, Claude API for progress comments, bKash merchant API, SMS gateway, small VPS behind Cloudflare.

1. Ask Claude for the schema and screens, reusing the coaching-centre pattern with players instead of students.
```
Design a PostgreSQL schema for a sports academy manager in Bangladesh: academies,
grounds, coaches, batches (sport, age_group, weekly schedule), players, guardians,
attendance, fee_invoices, payments (bKash), skill_templates, monthly_ratings
(player, month, skill, score 1-5, coach_comment), events (match or practice).
Then write Next.js pages: today's sessions with tap attendance, player list by batch,
fee ledger, and a monthly rating entry screen with 6 to 8 sliders.
```
2. Build the progress card. Ask Claude for an HTML template rendered to PNG on the server, with ratings as bars and a comment block, then use this prompt for the comment.
```
You write monthly progress comments for a Bangladeshi sports academy.
Input: player first name, sport, age group, skill scores out of 5 for this month and
last month, coach's short note. Output: 2 to 3 encouraging sentences in simple Bangla
for the parents, naming one strength and one thing to practise at home.
Use Bangla numerals. Do not promise selection to any team. Under 250 characters.
```
3. Ask Claude for the bKash link flow, six Bangla SMS templates (fee due, received, absent, match tomorrow, practice cancelled for rain, new batch), and the calendar screen with a one-tap "send notice" button.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: live with 3 academies in one city | 200 players |
| Day 60: progress cards shared by parents | 15 academies, 8 paying |
| Day 90: second city, cricket season push | 45 academies, 25 paying, roughly ৳25,000 a month |

### First customers with zero budget
- Facebook pages of district sports associations and cricket and football academies; owners post trial dates there every month.
- Google Maps: search "cricket academy" and "football academy" in each divisional city and message the owner. One respected local coach using the product brings the rest of the town.
- Outreach angle: "Stop chasing fees on WhatsApp; parents pay on bKash and get a Bangla progress card every month." The demo that closes: rate one player live and show the card image on the coach's phone within a minute.
- Referral loop: every card carries the academy name and a small "powered by" line, and parents forward them widely.

### Pricing and the maths
- ৳499/month for up to 40 players, ৳999 for up to 120, ৳1,499 for multiple grounds and unlimited players.
- Cost of goods is SMS and a small Claude API cost per card, so gross margin is roughly 80 percent.
- At the mid price of ৳999, roughly 300 paying academies bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where cricket academies are dense and parents pay well; Hindi and Bengali packs first. Nigeria is the football-first port through a coach association.
- What changes: language pack, payment rail (UPI, JazzCash, Paystack), skill templates by sport, SMS gateway.
- What stays: schema, attendance, fee ledger, card renderer, and the comment prompt with the language swapped.

### Risks and how to de-risk them
- Risk: coaches skip monthly ratings and cards stop. De-risk: a two-minute rating screen and an automatic reminder on the 25th of each month.
- Risk: seasonal churn during exams and monsoon. De-risk: a low-priced pause plan and an annual price with two months free.
- Risk: small academies find ৳499 steep. De-risk: a free tier for up to 15 players with the academy name on cards.

## Idea 51: Driving School Manager
*Enrolment, lesson scheduling, instructor and vehicle allocation, BRTA test preparation with Bangla MCQs and licence-step tracking for driving schools.*

### Who pays and why now
Hundreds of driving schools train drivers for ride-hailing, private cars and overseas jobs where a licence means a better contract. A typical school has two to six cars, a few instructors and a register that lists who is booked for which hour. Double bookings, idle cars and students who disappear before their BRTA test are daily problems.

The owner pays because a full schedule means every car earns, and because students choose the school that helps them pass the written test. Ride-hailing and overseas recruitment have created steady demand, and BRTA processes increasingly run online, so a school that tracks steps looks professional. Ports are India, Pakistan, Indonesia, Nigeria and Egypt, each with its own test bank.

### The product in 30 days (MVP)
- Student enrolment with package, lessons purchased and licence type.
- Lesson calendar by instructor and vehicle, with conflict detection.
- Student SMS for lesson reminders and reschedules.
- Licence step tracker: learner's, lessons done, written test date, practical test date, result.
- BRTA written test practice: Bangla MCQs on signs and rules with explanations, on the student's phone.
- Fee ledger with bKash link, instalments allowed.
- Leave out: GPS tracking of cars, a public booking marketplace, payroll, fuel accounting.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API, Nagad second. Many students pay in two or three instalments.
- SMS in Bangla for reminders, WhatsApp for sharing practice links.
- Test bank: original MCQs covering the BRTA syllabus, road signs, traffic rules and basic mechanics, each with a Bangla explanation and sign images you draw or license.
- Vehicle records: registration, fitness and insurance expiry with alerts, since a car with expired papers cannot be used. Bangla numerals on all student pages.

### Build it with Claude
Stack: Next.js web app for office and students, PostgreSQL, Claude API to draft practice questions, bKash merchant API, SMS gateway, small VPS behind Cloudflare.

1. Ask Claude for the schema and the conflict-free scheduler, then the weekly calendar screen with drag to reschedule and an SMS on save.
```
Design a PostgreSQL schema for a driving school: schools, instructors, vehicles
(registration, fitness_expiry, insurance_expiry), students, packages, enrolments,
lessons (student, instructor, vehicle, start, end, status), licence_steps
(step name, date, status), fee_invoices, payments (bKash), quiz_questions,
quiz_attempts. Write a function to book a lesson that rejects overlaps for the
instructor or the vehicle and suggests the next three free slots.
```
2. Build the practice bank. Use this prompt to draft questions by topic, then have a licensed instructor review every question before it goes live.
```
Draft 20 multiple-choice questions in simple Bangla for the Bangladesh BRTA
driving licence written test on the topic: [topic, e.g. road signs, right of way,
speed limits, documents to carry]. Each question: 4 options, one correct, a 2-sentence
explanation in Bangla, and a difficulty tag. Use Bangla numerals. Mark any question
that needs a sign image with the sign name in English. Return JSON.
```
3. Ask Claude for the licence step tracker with a Bangla SMS on each step change, the vehicle document expiry alert job, and a monthly utilisation report per car and instructor.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: live with 3 schools in Dhaka | 150 students scheduled |
| Day 60: quiz live, first passes reported | 15 schools, 8 paying |
| Day 90: second city, overseas-job schools | 40 schools, 25 paying, roughly ৳25,000 a month |

### First customers with zero budget
- Google Maps: search "driving school" and "driving training centre" in Dhaka, Chattogram, Sylhet and Khulna, list them all and visit, since owners sit in the office.
- Facebook groups for ride-hailing drivers and overseas job seekers, where people ask which school to join; post the free practice quiz.
- Outreach angle: "Your cars never sit idle or double book, and your students pass the written test." The demo that closes: enter the school's cars and instructors, then show tomorrow's schedule with free slots highlighted.
- Referral loop: students share a free quiz link that carries the school name and yours.

### Pricing and the maths
- ৳499/month for up to 2 vehicles, ৳999 for up to 6, ৳1,499 for larger schools with several branches.
- Cost of goods is SMS, hosting and a one-time Claude API cost for the question bank, so gross margin is roughly 80 percent.
- At the mid price of ৳999, roughly 300 paying schools bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where driving school density is high and state RTO test banks exist; Hindi and Bengali first.
- What changes: test bank per authority (RTO, Pakistan traffic police, Indonesia SIM, Nigeria FRSC, Egypt), payment rail, language pack, vehicle document names. Sell through instructor associations and used-car dealers.
- What stays: scheduler, vehicle and instructor allocation, licence step tracker, fee ledger.

### Risks and how to de-risk them
- Risk: a wrong quiz answer leads a student to fail. De-risk: instructor review of every question and a source note for each rule.
- Risk: the schedule stays on a whiteboard. De-risk: make the calendar the fastest way to answer the daily call "when is my next lesson", with an instant SMS to the student.
- Risk: BRTA process changes. De-risk: keep licence steps configurable per school rather than hard-coded.

## Idea 79: Vocational Training Centre Manager
*Enrolment, batch scheduling, attendance, BTEB and NSDA certification steps, assessment records, job placement tracking and donor reporting for skills centres.*

### Who pays and why now
Thousands of vocational and skills training centres run across Bangladesh, funded by government programmes, NGOs and the demand for overseas jobs in construction, garments, driving, care work and IT. Trainee lists, attendance sheets, assessment scores and placement records are compiled by hand at the end of every batch, and a report that takes a week delays the next payment.

Centre managers pay because reporting is the condition for funding, and placement data is what funders ask for first. BTEB and NSDA require specific records, and a centre that produces them cleanly gets accredited faster. Donors now demand digital evidence. Ports are India (ITIs), Pakistan, Kenya, Nigeria and Indonesia.

### The product in 30 days (MVP)
- Centre, trade, batch and trainer setup with schedule.
- Trainee registration with NID, photo, guardian phone and funder tag.
- Daily attendance with an offline-capable phone screen.
- Assessment records per competency unit, pass or fail, matching BTEB and NSDA formats.
- Certification step tracker and placement tracker: employer, job, salary, start date, follow-up at 3 and 6 months.
- Donor report export: one-click PDF and Excel for a batch or a period.
- Leave out: an LMS with lessons, payroll, an employer job board, biometric hardware.

### Data, integrations and the Bangladesh specifics
- Payments: bKash for trainee fees where they exist, and stipend disbursement records. Many programmes are free to trainees, so invoicing is secondary.
- SMS in Bangla for class reminders, assessment dates and placement follow-ups.
- Trade and competency lists from BTEB and NSDA course standards, stored as templates the centre picks from.
- Report templates for common funder formats (batch summary, attendance percentage, pass rate, placement rate) in Bangla and English, with Bangla numerals on trainee documents. Offline attendance and photo capture for rural centres.

### Build it with Claude
Stack: Next.js web app for managers and funders, Flutter Android app for attendance and photos, PostgreSQL, Claude API for report narratives, bKash merchant API, SMS gateway, small VPS behind Cloudflare.

1. Ask Claude for a multi-tenant schema where an NGO sees many centres, then the Flutter attendance and photo screen, offline first.
```
Design a PostgreSQL schema for a vocational training centre manager in Bangladesh:
organisations (NGO or funder), centres, trades, competency_units, batches, trainers,
trainees (NID, photo, guardian phone, funder tag), attendance, assessments
(trainee, unit, score, result, assessor, date), certification_steps, placements
(employer, job title, salary, start date, followup_3m, followup_6m), report_exports.
Organisations can view all their centres; centres see only themselves.
```
2. Ask Claude for the report engine: PDF and Excel per batch with the standard tables, plus a narrative page funders like to read, using this prompt.
```
Write a one-page batch completion report narrative for a donor, in formal English and
then in formal Bangla. Input: centre name, trade, batch dates, enrolled, completed,
attendance percentage, assessment pass rate, number placed, average starting salary,
two trainee quotes. Use plain sentences, no marketing language, and include the
numbers exactly as given. Bangla version uses Bangla numerals.
```
3. Ask Claude for the placement follow-up job that sends a Bangla SMS at 3 and 6 months asking if the trainee is still employed, with a one-tap reply link, and the funder dashboard filtered by trade and district.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: live with 2 centres of one NGO | 120 trainees |
| Day 60: reports accepted by a funder | 10 centres, 5 paying |
| Day 90: NSDA-format assessments in use | 30 centres, 18 paying, roughly ৳35,000 a month |

### First customers with zero budget
- NGO skills programme managers, reachable through development-sector Facebook groups and LinkedIn; one NGO brings many centres.
- Google Maps: search "technical training centre" and "skills training" by district. Private centres training for overseas jobs cluster around recruitment agencies and BMET centres.
- Outreach angle: "Your donor report ready in one click, and a placement rate you can prove." The demo that closes: import one old batch from Excel and produce the funder PDF on the spot.
- Referral loop: funders who receive a clean report ask their other centres to use the same tool; ask each funder for an introduction.

### Pricing and the maths
- ৳999/month for one centre with up to 100 active trainees, ৳1,999 for up to 300, ৳2,999 for larger centres or an NGO with several centres.
- Cost of goods is SMS, photo storage and a small Claude API cost per report, so gross margin is roughly 80 percent.
- At the mid price of ৳1,999, roughly 150 paying centres bring ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, where donor-funded skills programmes are dense, English is the working language and M-Pesa is the rail. Sell to international NGOs running programmes in several countries and price in dollars.
- What changes: certification templates (TVETA in Kenya, NCVET and ITI in India, NAVTTC in Pakistan), payment rail, language pack.
- What stays: schema, attendance app, assessment records, placement tracker, report engine.

### Risks and how to de-risk them
- Risk: long sales cycles with NGOs. De-risk: start with private centres that decide fast and use them as references.
- Risk: certification formats change. De-risk: keep templates as data, not code, and update them centrally.
- Risk: trainee personal data and NID numbers. De-risk: encrypt sensitive fields, limit exports and publish a clear data policy.

## Idea 85: Online Quran and Bangla Tutor Agency
*Diaspora families book Bangladeshi tutors with time-zone scheduling, Zoom links, progress notes, Stripe subscriptions in dollars and tutor payouts in taka.*

### Who pays and why now
Bangladeshi families in the UK, US, Canada, Italy and the Gulf want their children to read Quran and speak Bangla, and a tutor in Dhaka or Sylhet costs a fraction of a local one. Thousands of tutors already teach these children over WhatsApp and Zoom, paid by informal transfers and scheduled in chat threads.

Families pay in dollars for reliability: a tutor who shows up, a replacement when one is sick, a weekly progress note and a single monthly card charge. Pakistan and Egypt already run this model at scale for Urdu and Arabic; the Bangla diaspora has no organised supply. Ports are the Urdu, Arabic and Bahasa tutor pools serving their own diasporas.

### The product in 30 days (MVP)
- Family sign-up with children, subjects (Quran reading, hifz, Bangla, Islamic studies) and preferred times in their own time zone.
- Tutor profiles with availability, sample video and a vetting checklist.
- Matching and trial class booking, with a Zoom or Google Meet link per class.
- Recurring weekly schedule with automatic time-zone conversion and reminders by WhatsApp and email.
- Stripe subscription per family, monthly tutor payout statement in taka.
- Weekly progress note from tutor to parent in English or Bangla.
- Leave out: a built-in video platform, tutor-set pricing, a mobile app, group classes.

### Data, integrations and the Bangladesh specifics
- Payments in: Stripe subscriptions in USD, GBP and EUR, or Lemon Squeezy as merchant of record if Stripe onboarding is a problem for a Bangladeshi entity.
- Payments out: bKash or bank transfer to tutors in taka, with a monthly statement per tutor.
- Scheduling: store all times in UTC, display in each user's zone, and warn both sides when daylight saving shifts a class.
- Tutor vetting: identity check, a recorded demo lesson and a reference, visible to families.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Stripe Billing, Zoom or Google Meet API, WhatsApp Business API, Claude API for progress notes, Cloudflare in front.

1. Ask Claude for the schema and the time-zone-safe scheduler, then Stripe Checkout and webhooks that pause a family's classes after two failed payments.
```
Design a PostgreSQL schema for an online tutoring agency: families (timezone,
currency), children, tutors (timezone, subjects, availability), matches, classes
(start_utc, duration, meeting_link, status), progress_notes, subscriptions (Stripe
customer and subscription ids, plan), payouts (tutor, month, amount_bdt, status).
Write a function that generates weekly recurring classes for a match, converting a
family's local 6pm on Saturdays to UTC and warning when daylight saving shifts it.
```
2. Ask Claude for the progress note helper. The tutor taps a few boxes and edits a draft.
```
Draft a weekly progress note for a parent from an online Quran and Bangla tutor.
Input: child's first name, subject, this week's lessons (e.g. surah and ayah range,
or Bangla letters covered), effort rating 1-5, one thing to practise at home,
tutor's short note. Output: 4 sentences in warm, plain English, then the same in
Bangla. No grades, no comparison to other children. Under 400 characters each.
```
3. Ask Claude for WhatsApp reminders (24 hours and 1 hour before, in the family's language), the monthly payout statement, and a landing page for diaspora parents in English with a Bangla section and a trial booking form.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 10 vetted tutors, trial classes running | 15 families on trial |
| Day 60: Stripe subscriptions live | 40 paying families, 20 tutors |
| Day 90: replacement tutors, referral programme | 100 paying families, roughly $3,000 monthly commission |

### First customers with zero budget
- Diaspora Facebook groups by city (Bangladeshis in London, Toronto, New York, Rome, Dubai) and Bangladeshi mothers' groups; ask admins to let you offer a free trial class.
- Mosques and community centres in East London and Jackson Heights that run weekend Bangla and Quran schools; offer tutors for the weekday gap.
- Outreach angle: "A vetted Bangladeshi Quran and Bangla tutor for your child, one card payment a month, weekly progress notes, replacement guaranteed." The demo that closes: a free 30-minute trial.
- Referral loop: one free class per family referred.

### Pricing and the maths
- The agency keeps 15 to 20 percent of tuition, or charges an independent agency $29/month per seat to run its own operation on the platform.
- Cost of goods is Stripe fees (roughly 3 to 4 percent), WhatsApp conversation fees and hosting, so gross margin on commission is roughly 75 percent.
- At about 17.5 percent commission, roughly $14,000 of monthly tuition, or 85 to 90 agency seats at $29, brings roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: white-label the platform to Urdu and Arabic tutor agencies in Pakistan and Egypt that have families but run on spreadsheets.
- What changes: language of notes and reminders, tutor payout rail (JazzCash, Instapay, GoPay), subject list, landing page copy.
- What stays: scheduler, Stripe billing, matching, vetting workflow, progress notes.

### Risks and how to de-risk them
- Risk: tutors take families off-platform. De-risk: pay tutors promptly, handle replacements and disputes, and make the card subscription the easy path.
- Risk: Stripe access for a Bangladeshi company. De-risk: Lemon Squeezy as merchant of record, or a partner entity abroad.
- Risk: child safety concerns. De-risk: recorded trial lessons, ID checks, parent presence encouraged and a clear complaints channel.

## Idea 94: Course Creator Platform in Local Currency
*Bangla course hosting with drip lessons, quizzes, certificates, bKash and Nagad checkout, affiliate links and student WhatsApp groups.*

### Who pays and why now
Thousands of Bangla teachers sell courses today: spoken English, freelancing, graphic design, Quran recitation, HSC chemistry, digital marketing. They post on Facebook, take bKash payments by hand and send Google Drive links, because global course platforms bill in dollars and do not accept bKash.

Creators pay because a checkout that takes bKash and Nagad and delivers the course instantly recovers more sales than any feature. They also want certificates students share, quizzes that keep students engaged, and affiliate links so students sell for them. Ports are Pakistan, Indonesia, Nigeria, Egypt and Vietnam, each with the same gap.

### The product in 30 days (MVP)
- Course builder with sections, video (your storage or unlisted YouTube), PDF and text lessons.
- Drip schedule: release lessons by day since enrolment.
- bKash and Nagad checkout with instant enrolment, plus manual payment approval as a fallback.
- Quizzes with a pass mark and a Bangla PDF certificate with the creator's name.
- Affiliate links with a percentage set by the creator and a payout report.
- WhatsApp group invite after enrolment, and a student dashboard.
- Leave out: live classes, a mobile app, community forums, a ranked marketplace homepage.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API and Nagad for consumers, SSLCommerz for cards. The platform takes its cut at settlement or invoices the creator monthly.
- Video: store on Cloudflare R2 or Bunny and stream with signed URLs so links cannot be shared.
- WhatsApp group links and an SMS enrolment confirmation. Bangla fonts on certificates and Bangla numerals on receipts.
- VAT: keep a per-sale record so creators who register for VAT can produce Mushak-compatible sales lists later.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Cloudflare R2 for video, bKash and Nagad merchant APIs, SSLCommerz, SMS gateway, Claude API for course copy and quiz drafts.

1. Ask Claude for the schema and the creator course builder, then the checkout with webhook verification and instant enrolment.
```
Design a PostgreSQL schema for a course platform: creators, courses, sections,
lessons (type video/pdf/text, drip_day), enrolments, payments (bKash, Nagad, card,
status, platform_fee), quizzes, quiz_attempts, certificates, affiliates (creator,
code, percent), affiliate_earnings, whatsapp_groups. Then write Next.js pages for a
creator to create a course, add lessons with drag ordering, and set a price in taka.
```
2. Ask Claude for signed video URLs from Cloudflare R2 with a short expiry and a player page that hides the direct link.
3. Give creators a helper that writes their sales page and quiz drafts from a lesson outline, then ask Claude for the certificate PDF, affiliate dashboard and monthly settlement report.
```
You help a Bangladeshi course creator. Input: course title, target learner,
lesson titles, what the learner can do after finishing, price in taka.
Output in Bangla: a course sales page with a headline, 5 benefit bullets, who it is
for, a short creator bio placeholder, and an FAQ of 5 questions. Then 5 quiz
questions per lesson title, 4 options each, with the correct option marked.
Use Bangla numerals. Plain language, no exaggerated claims.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 5 creators live with one course each | 200 enrolments |
| Day 60: affiliate links and certificates on | 25 creators, ৳5 lakh in course sales processed |
| Day 90: signed video and Nagad live | 60 creators, ৳15 lakh monthly sales, roughly ৳1 lakh platform revenue |

### First customers with zero budget
- Facebook groups for Bangla creators and online teachers, and pages already selling by bKash number; message the ones with a pinned "how to buy" post.
- YouTube: search Bangla tutorials in freelancing, English, design and exam prep; channels with a course link in the description are your list.
- Outreach angle: "Your students pay on bKash and get the course instantly, no more Drive links, and your video cannot be leaked." The demo that closes: upload one of the creator's lessons, set a price, and buy it with ৳10 on bKash in front of them.
- Referral loop: affiliate links mean every student can sell, and each certificate carries the platform name.

### Pricing and the maths
- 5 to 8 percent of sales, or ৳999/month flat for creators who prefer a fixed cost.
- Cost of goods is gateway fees (roughly 1.5 to 2 percent), video storage and bandwidth, SMS and hosting, so gross margin on commission is roughly 60 to 70 percent.
- At ৳999 flat, roughly 300 creators bring ৳3 lakh a month; on commission at about 6.5 percent, roughly ৳46 lakh of monthly course sales does the same.

### Country kit: taking it to other languages
- First port: Pakistan, where Urdu creators face the same dollar-billing gap and JazzCash and Easypaisa are the rails.
- What changes: payment rails (JazzCash, GoPay in Indonesia, Paystack in Nigeria, Fawry in Egypt, MoMo in Vietnam), language pack, certificate template, tax record format.
- What stays: course builder, drip, quizzes, signed video, affiliates, WhatsApp flow.

### Risks and how to de-risk them
- Risk: video bandwidth costs grow faster than revenue. De-risk: cap storage per plan, allow unlisted YouTube for free courses, use a cheap CDN.
- Risk: refund disputes between students and creators. De-risk: a clear refund window and a settlement hold of a few days.
- Risk: creators leave for a global platform once they grow. De-risk: keep the fee low and add affiliate and WhatsApp features they will not get elsewhere.


---

# Section 6: Agriculture and Food (Part 1)

Agriculture feeds Bangladesh, and most of its money still moves through paper khatas, from the input dealer's credit book to the rice mill gate and the milk collection slip. The eight businesses in this section digitise those records for the people who hold them, and each one grows from a single ledger into data that farmers, buyers and companies will pay for.

## Idea 12: Agri Input Shop Ledger
*A credit khata, stock and expiry tracker, and Bangla crop advice line for the seed, fertiliser and pesticide dealer.*

### Who pays and why now
Around 60,000 dealers sell seed, fertiliser and pesticide across Bangladesh, mostly on credit. Farmers take inputs at sowing and pay after harvest. The dealer tracks this in a paper khata and loses money to forgotten balances and expired stock.

The dealer will pay because the credit book is the business. A ৳299 a month tool that recovers one forgotten ৳2,000 balance pays for itself. Dealers also want to look like advisors: a clear Bangla answer to a farmer's crop question, forwarded in a minute, keeps that farmer.

The moment is right because dealers own smartphones, farmers are on WhatsApp and bKash, and Claude can answer a crop question in Bangla. The same shape ports to India, Pakistan, Kenya, Nigeria and Vietnam, where dealers keep the same paper khata.

### The product in 30 days (MVP)
- Farmer credit ledger: add a farmer by phone number, record credit sales and repayments, see the balance.
- Automatic Bangla SMS reminders before and after due dates, signed with the shop name.
- Stock list with batch, expiry date and low-stock alerts.
- Crop advice: type or voice-record a farmer's question, get a Bangla answer, forward it on WhatsApp.
- Reports: total dues, top debtors, expiring stock, monthly sales.
- Leave out: multi-branch, supplier purchase orders, a farmer-facing app, accounting exports.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for the subscription; dealers record farmer repayments taken in cash or personal bKash.
- Local SMS gateway for reminders; WhatsApp for forwarding advice.
- Product master seeded with common fertilisers, seed brands and pesticide names sold in Bangladesh.
- Advice grounded in the public crop calendar and extension guidance, with a fixed safety line.
- Offline first on Android with later sync; Bangla numerals in every farmer-facing SMS.

### Build it with Claude
Stack: Flutter Android app with local SQLite and sync, Laravel API, PostgreSQL, Claude API for advice, bKash merchant API, local SMS gateway, small VPS.

1. Ask Claude for the data model and sync logic. Paste:
```
Design a PostgreSQL schema for an agri input shop ledger app in Bangladesh.
Tables: shops, farmers (phone, village, crop), sales (cash/credit, items), repayments,
products (name, category, batch, expiry, quantity), sms_log.
Each row needs a client_id and updated_at for offline sync from a Flutter app.
Give me the SQL, a Laravel migration, and the sync endpoint design.
```
Review the tables, then have Claude write the Laravel models and endpoints.

2. Ask Claude for the Flutter screens: farmer list with balances, add sale, add repayment, stock with expiry colour codes, large buttons and Bangla labels.

3. Build the advice feature. Paste:
```
You answer crop questions for a Bangladeshi input dealer to forward to farmers.
Reply in simple Bangla, under 120 words. Structure: likely problem, what to do this week,
which product category to use (generic names, dose per bigha), and one safety line.
If the question needs a photo or is unclear, ask one short question instead.
Never promise yield. End with: "লেবেল পড়ুন এবং উপসহকারী কৃষি কর্মকর্তার পরামর্শ নিন।"
```
Use it as the system prompt and test with 20 real dealer questions.

4. Ask Claude for three Bangla SMS reminder templates (friendly, due today, overdue), the scheduling job, and a CSV import for an existing khata.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 dealers in one upazila using the ledger daily |
| Day 60 | 60 dealers, 5,000 farmer records, 40 paying |
| Day 90 | 200 dealers, 150 paying, ৳60,000 monthly revenue |

### First customers with zero budget
- Walk the input dealer row in one upazila bazaar on market day.
- Facebook groups for agri input traders and district fertiliser dealer association pages.
- Outreach angle: "How much do farmers owe you right now?" Then show the balance screen.
- The demo that closes: enter three farmers from their khata, send one SMS reminder, show it arriving on their own phone.
- Referral loop: one month free for every dealer who brings another; pesticide company field officers, who visit 30 dealers a week, can recommend it.

### Pricing and the maths
- Basic ৳299 a month: ledger, stock, 100 SMS. Pro ৳799 a month: unlimited SMS, crop advice, reports.
- Costs per dealer are roughly ৳30 to ৳80 a month in SMS and AI, so gross margin is around 80 percent.
- At a mid price of about ৳549, roughly 550 paying dealers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya or Nigeria, where agro-dealers sell on credit and mobile money is common; India is larger but crowded.
- What changes: language pack, product master, crop calendar, SMS gateway, payment rail, local extension source for advice.
- Reseller: an input company or agro-dealer association in each country.
- What stays the same: ledger, reminders, stock and expiry, the advice prompt structure.

### Risks and how to de-risk them
- Risk: dealers stop entering data after two weeks. De-risk: three-tap or voice entry faster than paper, and total dues on the home screen.
- Risk: wrong crop advice harms a farmer. De-risk: generic recommendations only, dose ranges, a mandatory safety line, and a "not sure" path.
- Risk: SMS costs eat margin. De-risk: cap SMS on Basic and push WhatsApp for advice.
- Risk: a big input company bundles a free app. De-risk: stay neutral across brands, which dealers prefer.

## Idea 17: Poultry and Fish Farm Manager
*Batch profit, feed conversion, mortality and vaccine reminders for small poultry and fish farms, with Bangla disease advice from a photo.*

### Who pays and why now
Bangladesh is a top-five aquaculture producer with hundreds of thousands of small poultry and fish farms. A broiler farmer runs 1,000 to 5,000 birds a batch and learns whether it made money only when the birds are sold. Fish farmers feed by habit and guess at survival.

They will pay because feed is the largest cost and a slip in feed conversion or a missed vaccine wipes out the margin. Seeing cost per kg live weight mid-batch lets a farmer change feed, sell earlier, or negotiate. Photo disease advice at 6 am, in Bangla, is worth a month's fee alone.

The moment: feed and hatchery companies want digital ways to keep farmers loyal and will distribute a tool that works. Ports are India, Indonesia, Vietnam, Nigeria and Egypt.

### The product in 30 days (MVP)
- Batch setup: birds or fish stocked, date, price paid, target sale date.
- Daily log: feed given, mortality, weight sample, medicines; under 30 seconds to fill.
- Live batch dashboard: feed conversion ratio, cost per kg, projected profit at today's price.
- Vaccine and treatment calendar with SMS reminders.
- Photo advice: photograph a sick bird, dropping or fish, get likely causes and next steps in Bangla.
- Buyer price alerts from farmer-entered local prices.
- Leave out: hatchery ordering, feed dealer credit ledger, IoT sensors, a marketplace.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad for the subscription; a feed company or dealer may pay for its farmers.
- SMS for vaccine reminders; WhatsApp for sharing batch reports with dealers.
- Reference growth and feed tables for broiler, Sonali, layer, tilapia, pangas and carp; farm data replaces them over time.
- Vaccine schedules from the Department of Livestock Services, editable per farm.
- Offline daily log with sync; Bangla numerals and local units (kg, piece, decimal for pond size).

### Build it with Claude
Stack: Flutter Android app, Laravel API, PostgreSQL, Claude API with vision for photo advice, bKash merchant API, SMS gateway, small VPS.

1. Ask Claude for the domain model and the FCR maths. Paste:
```
Model a poultry and fish farm app for Bangladesh. Entities: farm, pond_or_shed, batch
(species, breed, count, start_date, cost), daily_log (feed_kg, mortality, avg_weight_g,
medicine, cost), sale, vaccine_schedule, price_report (area, species, price_per_kg).
Write SQL, then the formulas for FCR, survival rate, cost per kg live weight, and
projected profit given a market price. Show worked examples with 1,000 broilers.
```
Check the examples against a real farmer's numbers.

2. Ask Claude for a Flutter daily log screen for wet hands and low light: big number pad, yesterday's values prefilled, one save button.

3. Build the photo advice. Paste:
```
You are a poultry and fish health assistant for small farmers in Bangladesh.
Input: a photo plus species, age in days, mortality today, and a short Bangla note.
Reply in simple Bangla: 2 to 3 likely causes ranked, what to do in the next 24 hours,
when to call a vet, and which signs would change your view. Under 150 words.
Never name a specific antibiotic dose; say to confirm with a registered vet or paravet.
```
Test with 30 real photos from farmer groups.

4. Ask Claude for vaccine calendar templates as JSON, a job that schedules Bangla SMS, and a one-page benchmark report a farmer can share with a feed dealer.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 25 farms logging daily in one district |
| Day 60 | 150 farms, 60 paying, one feed dealer distributing |
| Day 90 | 500 farms, 200 paying, one feed company pilot |

### First customers with zero budget
- Facebook poultry and fish farming groups have hundreds of thousands of members; post batch profit screenshots and answer questions daily.
- Feed dealers in poultry belts such as Gazipur, Mymensingh and Bogura, plus paravets and hatchery field staff; give them free accounts and referral codes.
- Outreach angle: "Do you know your cost per kg for the batch running right now?"
- The demo that closes: enter their current batch, show projected profit at today's price, then send one photo for advice.
- Referral loop: farmers who invite five neighbours get a free month; dealers who onboard 20 farms get a dealer dashboard.

### Pricing and the maths
- Basic ৳299 a month: one shed or pond, logs, calendar. Pro ৳999 a month: unlimited batches, photo advice, benchmarks, dealer sharing.
- Costs per farm run roughly ৳40 to ৳120 a month in SMS and vision calls; gross margin around 80 percent.
- At a mid price of about ৳649, roughly 460 paying farms make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia or Vietnam, both large aquaculture markets with small farms and mobile payments.
- What changes: language pack, species and breed reference curves, vaccine schedule source, payment rail, SMS gateway.
- Reseller: a feed company or hatchery in each country, since they already reach farmers.
- What stays the same: batch model, FCR maths, daily log, photo advice prompt.

### Risks and how to de-risk them
- Risk: wrong disease advice leads to losses. De-risk: ranked possibilities not diagnoses, no drug doses, and clear "call a vet" triggers.
- Risk: farmers fill logs for a week then stop. De-risk: prefilled values, a daily SMS nudge, and projected profit as the reward.
- Risk: feed companies build their own app. De-risk: partner early; be the neutral tool that works with any feed brand.
- Risk: price alerts are gamed by buyers. De-risk: show the median of several reports and the reporter count.

## Idea 27: Qurbani Cattle Fattening and Marketplace
*Weight, feed and cost per kg gained for fattening farms, plus video listings with bKash deposits and Eid delivery slots.*

### Who pays and why now
Millions of animals are sold in Bangladesh each Eid-ul-Adha. Thousands of small fattening farms buy months before Eid, feed, and sell in the last two weeks, judging weight by eye and cost from memory. Buyers in Dhaka and Chattogram increasingly want to pick an animal online, pay a deposit, and get delivery before Eid.

Farms pay for two things. The fattening record shows cost per kg gained and what price is a profit. The marketplace gives a farm with 40 animals its own listing page with videos, live weight and a deposit button. Buyers pay nothing but leave a bKash deposit, which carries the commission.

The season is a hard deadline, which helps: open listings two months before Eid and peak in the last 20 days. The same pattern exists in Pakistan, India, Indonesia, Nigeria and Egypt.

### The product in 30 days (MVP)
- Animal register: tag, breed, purchase date and price, photos, estimated weight from girth.
- Feed and medicine log per animal or group, with daily cost.
- Fattening dashboard: monthly weight gain, cost per kg gained, break-even sale price per animal.
- Listing page per farm: video, photos, live weight, asking price, location, bKash deposit button.
- Buyer flow: pick an animal, pay a deposit, get SMS confirmation and a delivery slot.
- Leave out: livestock loans, vet booking, auctions, a general livestock marketplace.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for deposits, held and paid out to the farm after delivery; Nagad as a second rail.
- SMS confirmations to buyers and farms; a WhatsApp share link per animal.
- Girth-to-weight tables as a starting estimate, corrected by scale weights where available.
- Delivery zones for Dhaka and Chattogram with the last two days before Eid filling first.
- Bangla numerals on listings with an English toggle for buyers abroad; the Eid date drives all countdowns.

### Build it with Claude
Stack: Next.js web app for listings and buyers, Flutter Android app for the farm, PostgreSQL, Cloudflare for video and images, Claude API for listing copy, bKash merchant API.

1. Ask Claude for the schema and the fattening maths. Paste:
```
Design a schema for a cattle fattening and Eid marketplace app in Bangladesh: farms,
animals (tag, breed, sex, purchase_date, purchase_price, girth_cm, est_weight_kg),
weight_logs, feed_logs (item, kg, cost), listings (status, asking_price, videos),
deposits (bkash_trx_id, amount, status), deliveries (zone, slot, address).
Write the formulas for monthly weight gain, cost per kg gained and break-even sale
price, and a girth-to-weight estimate function with a note on its accuracy.
```
Verify the maths against two farms' real animals.

2. Ask Claude for the Flutter farm screens: animal register with photo, monthly weigh-in, group feed log, dashboard.

3. Ask Claude for the Next.js listing page with fast video and a bKash deposit button, then generate the copy. Paste:
```
Write a Bangla listing for a Qurbani animal from these fields: breed, colour, age,
live weight, feed type, farm district, asking price, delivery zones.
Tone: honest and warm, no exaggeration, no religious claims about the animal.
Three lines plus a bullet list of facts. Add an English version below.
```

4. Ask Claude for the bKash deposit flow with webhooks, a buyer status page, SMS templates, and a posting calendar counting back from Eid.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 15 farms tracking 300 animals |
| Day 60 | 60 farms, 1,500 animals listed, 40 paying |
| Day 90 (Eid season) | 200 deposits taken, ৳1.5 lakh commission plus ৳30,000 subscriptions |

### First customers with zero budget
- Facebook cattle fattening groups, where farms already post videos; offer them a proper listing page.
- Farms in the Manikganj, Pabna, Sirajganj and Kushtia belts; visit on a Friday.
- Outreach angle: "Here is your own page with a deposit button, free until Eid."
- The demo that closes: register one animal with girth, show the break-even price, then create and share its listing.
- Buyer side: post listings in Dhaka housing society and office groups, and reach Bangladeshis abroad.
- Referral loop: commission waived on one sale for every farm a farm brings.

### Pricing and the maths
- ৳499 a month per farm for fattening records and listings, plus 1 to 2 percent on marketplace sales through the deposit flow.
- Costs are video hosting, bKash fees and SMS, roughly ৳50 to ৳150 per farm a month; gross margin around 75 percent.
- ৳3 lakh a month needs roughly 600 farms on subscription, or about 150 farms plus ৳1 crore of yearly Eid sales through the deposit flow.

### Country kit: taking it to other languages
- First port: Pakistan, a very large Qurbani market, with Urdu content and JazzCash or Easypaisa as the payment rail.
- What changes: language, payment rail, breed list and girth tables, delivery zones, Eid calendar.
- Reseller: a cattle feed company or a large online Qurbani seller.
- What stays the same: fattening maths, listing page, deposit and delivery flow.

### Risks and how to de-risk them
- Risk: a farm takes deposits and fails to deliver. De-risk: hold deposits until delivery is confirmed, and verify farms by visit or video call.
- Risk: revenue is seasonal. De-risk: fattening records run all year; add goat and beef farms.
- Risk: weight estimates are wrong. De-risk: label estimates clearly, show weigh-in photos, allow a small refund rule.
- Risk: bKash limits block large deposits. De-risk: deposits of 10 to 20 percent, balance on delivery.

## Idea 34: Wholesale Arot Ledger
*Daily lots, farmer payouts, buyer dues and commission statements for commission agents in fish, vegetable and fruit markets, with Bangla voice entry.*

### Who pays and why now
An arotdar receives produce from farmers, sells it to buyers on the market floor, takes a commission, and pays the farmer. Thousands work in Karwan Bazar, Shyambazar, fish landing centres and district markets. A mid-size arot moves lakhs of taka a day, written in a paper khata at 4 am.

They pay because the money and the errors are large. A buyer who owes ৳3 lakh across 40 days, a farmer who disputes a payout, a clerk who leaves with the khata: each costs more than a year of software. Arotdars already pay clerks, so paying for help is normal.

The moment: bKash and bank transfers now carry part of the cash, so a digital trail exists. Mandi arhtiyas in India and arhtis in Pakistan run the identical model, as do markets in Nigeria and Indonesia.

### The product in 30 days (MVP)
- Lot entry: farmer or supplier, item, grade, quantity, arrival time; Bangla voice entry for the floor.
- Sale entry per lot: buyer, quantity, rate, amount; several buyers per lot.
- Automatic commission, labour and transport deductions, and a farmer payout statement.
- Buyer ledger with dues, payments, and a daily list to chase.
- Farmer ledger with advances, payouts and balances.
- Leave out: multi-market, a buyer app, cold storage, accounting exports.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for the subscription; bKash, bank and cash payments recorded against ledgers with a cash drawer view.
- Bangla SMS payout statements to farmers when a lot sells; due balance SMS to buyers.
- Bangla speech to text for entry, since clerks cannot type while weighing.
- Local units (maund, kg, piece, dozen, cage); Bangla numerals on statements; Bluetooth thermal payout slips.
- Offline capable tablet app; markets have poor signal at dawn.

### Build it with Claude
Stack: Flutter Android tablet app with offline SQLite and Bluetooth printing, Laravel API, PostgreSQL, Claude API for voice parsing, bKash merchant API, SMS gateway.

1. Ask Claude for the domain model. Paste:
```
Design a PostgreSQL schema for a wholesale commission agent (arot) in Bangladesh.
Tables: arots, farmers, buyers, lots (farmer, item, grade, qty, unit, arrived_at),
lot_sales (buyer, qty, rate, amount), deductions (commission_pct, labour, transport),
farmer_payouts, buyer_payments, cash_book. Units include maund and kg.
Include how to compute a farmer statement and a buyer due list. Write the SQL.
```
Review it with one arotdar's clerk and rename fields to their words.

2. Ask Claude to build the voice entry. Paste:
```
Parse a Bangla spoken sentence from a wholesale market into JSON.
Example input: "রহিম মিয়ার রুই বিশ কেজি, করিম স্টোর, দুইশো ষাট টাকা"
Output: {"farmer":"রহিম মিয়া","item":"রুই","qty":20,"unit":"kg","buyer":"করিম স্টোর","rate":260}
Handle Bangla number words, maund and kg, missing fields as null, and return a
confidence field. Give me the prompt and a Laravel endpoint that calls Claude.
```
Test with recordings from a real floor, including noise and slang.

3. Ask Claude for the tablet screens: today's lots as cards, tap to add sales, swipe to close and print the farmer slip.

4. Ask Claude for Bangla SMS templates, a thermal receipt layout with a Bangla font, a day-end PDF, and a weekend migration plan for the paper khata.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 arots in one market running daily alongside paper |
| Day 60 | 15 arots, 8 paying |
| Day 90 | 40 arots across 3 markets, 25 paying, ৳70,000 monthly revenue |

### First customers with zero budget
- Go to the market at 4 am; arotdars are all in one place and the clerk is your first user.
- Market committees and arotdar samity offices; one introduction covers a market.
- Facebook arotdar and wholesale market groups are small but exact.
- Outreach angle: "Which buyer owes you the most right now, and since when?" Then show the due list.
- The demo that closes: enter this morning's lots by voice while the clerk watches, then print one farmer slip.
- Referral loop: farmers who get SMS statements ask other arots for the same; give the referring arot a free month.

### Pricing and the maths
- Standard ৳1,499 a month: one arot, unlimited lots, SMS to 200 farmers. Premium ৳4,999 a month: voice entry, several clerks, buyer due SMS, priority support.
- Costs per arot are roughly ৳150 to ৳400 a month in SMS and voice parsing; gross margin about 85 percent.
- At a mid price of about ৳3,249, roughly 90 paying arots make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where mandi arhtiyas run the same lot and commission model and UPI is universal; Pakistan second.
- What changes: language pack, units such as quintal, commission rules, payment rail and SMS gateway.
- Reseller: a market association or traders' software distributor in each city.
- What stays the same: lot, sale, deduction and ledger model, voice entry, statements.

### Risks and how to de-risk them
- Risk: clerks resist because paper hides things. De-risk: sell to the owner, make the clerk's job faster, run paper in parallel for two weeks.
- Risk: voice parsing fails on the noisy floor. De-risk: always show the parsed form for a one-tap confirm, and fall back to a number pad.
- Risk: fear of data loss. De-risk: nightly PDF export to the owner's WhatsApp and a printed day-end.
- Risk: a high ticket means slow sales. De-risk: one market at a time, committee endorsement, a 30-day free run.

## Idea 54: Rice Mill Management
*Paddy procurement by farmer with moisture and weight, milling yield per batch, by-product sales, buyer dues and storage lots for husking and auto rice mills.*

### Who pays and why now
Thousands of husking mills and hundreds of auto rice mills buy paddy, dry and mill it, and sell rice, bran and husk. The owner knows roughly what he paid and sold. He does not know which lot gave 64 percent rice and which gave 60, or which buyer's dues quietly crossed ৳20 lakh.

Mill owners pay well for anything that protects margin; a ৳2,999 to ৳9,999 monthly fee is small next to one bad lot. Auto mills also need clean procurement records for bank finance and government contracts.

The moment: moisture meters and digital scales are now standard at the gate, so the data exists and only needs capturing. Ports are India, Pakistan, Vietnam, Thailand, Indonesia and Nigeria.

### The product in 30 days (MVP)
- Gate entry: supplier, paddy variety, gross weight, tare, moisture percent, rate, deductions, net payable.
- Supplier ledger with advances, payments and balances.
- Storage lots: which paddy sits in which godown, with quantity and average moisture.
- Milling batch: paddy in, rice out by grade, bran, husk, broken; yield percent per batch and per source.
- Sales and buyer dues for rice, bran and husk, with SMS due reminders.
- Owner dashboard: stock, yield trend, dues, cash.
- Leave out: boiler and drier controls, payroll, transport fleet, accounting integration.

### Data, integrations and the Bangladesh specifics
- bKash for the subscription; bank, bKash and cash payments recorded, with a gate cash book.
- Bangla SMS receipts to farmers at the gate with weight, moisture, deduction and net amount, which builds trust.
- Paddy variety list for Bangladesh (BRRI dhan and local names) and standard moisture deduction tables, editable per mill.
- Government procurement season exports: farmer lists, quantities and payments in the format the food office asks for.
- Maund and kg with Bangla numerals on receipts; thermal or A5 printing at the gate; offline entry because godowns sit outside town.

### Build it with Claude
Stack: Laravel web app for the office, Flutter Android for the gate and godown, PostgreSQL, Claude API for yield analysis in Bangla, bKash merchant API, SMS gateway, small VPS.

1. Ask Claude for the schema and yield logic. Paste:
```
Design a schema for a rice mill in Bangladesh. Tables: mills, suppliers (farmer or trader),
paddy_receipts (variety, gross_kg, tare_kg, moisture_pct, deduction_kg, rate, net_amount),
storage_lots, milling_batches (lot ids, paddy_kg in), batch_outputs (rice grade, bran,
husk, broken, kg), buyers, sales, payments. Write SQL and a query that gives yield
percent by batch, by variety and by supplier over a date range.
```
Run the yield query on one mill's last month, entered by hand, to prove the value.

2. Ask Claude for the gate app: fast receipt entry with the scale reading typed in, moisture deduction auto-applied, print and SMS in one tap.

3. Ask Claude for the office web screens: storage lots, milling batch entry, sales with dues, and the owner dashboard.

4. Add the AI analyst. Paste:
```
You are an analyst for a Bangladeshi rice mill owner. Given a JSON of batches with
variety, supplier, moisture, paddy in and outputs by grade, write a short Bangla
note (under 150 words): which suppliers or varieties give the best and worst yield,
whether moisture explains it, and two actions for next week. Use Bangla numerals.
Do not invent data; if the sample is small, say so.
```
Send it weekly on WhatsApp, and ask Claude for the food office export format.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 mills entering gate receipts daily |
| Day 60 | 12 mills, 6 paying |
| Day 90 | 30 mills, 18 paying, ৳1 lakh monthly revenue |

### First customers with zero budget
- Rice mill clusters: Naogaon, Dinajpur, Kushtia, Bogura, Ashuganj, Ishwardi; each has an owners' association.
- Auto and husking mill owners' association district branches; ask to present at a monthly meeting.
- Outreach angle: "What was your rice yield last week, by variety?" Nobody knows, and they want to.
- The demo that closes: enter five receipts and one milling batch from their notebook and show yield percent and dues on screen.
- Referral loop: a free month per referred mill, and a free yield report for any mill that shares a month of data.

### Pricing and the maths
- Husking ৳2,999 a month: gate, ledgers, storage, two users. Auto ৳9,999 a month: milling batches, yield analytics, unlimited users, procurement exports, the weekly AI note.
- Costs per mill are roughly ৳200 to ৳600 a month in SMS and AI; gross margin around 90 percent.
- At a mid price of about ৳6,499, roughly 46 paying mills make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, especially West Bengal and Punjab, with the same mill mix and UPI; Vietnam second.
- What changes: language, variety list, moisture deduction norms, government procurement formats, units such as quintal, payment rail.
- Reseller: rice mill machinery dealers, who visit every mill.
- What stays the same: gate receipt, lot, batch and yield model, dues, dashboards.

### Risks and how to de-risk them
- Risk: gate clerks enter wrong weights. De-risk: a photo of the scale display on each receipt, and the farmer SMS as a check.
- Risk: owners fear tax visibility. De-risk: data lives in their own account with export and delete; sell yield and dues, not accounting.
- Risk: long sales cycle. De-risk: 45 days free during the procurement season, when the pain is highest.
- Risk: no connectivity at godowns. De-risk: offline first, sync over the owner's phone hotspot.

## Idea 55: Milk Collection Centre Ledger
*Daily milk weight and fat test per farmer, ten-day bKash payment cycles, chilling stock and dispatch, and feed advances for cooperatives and chilling centres.*

### Who pays and why now
Cooperatives, chilling centres and processor collection points buy milk twice a day from hundreds of small farmers. Each delivery is weighed, fat tested and written on a slip. Every ten days someone adds up the slips, deducts advances, and pays cash. Disputes and late payments are constant, and farmers switch to whoever pays fastest.

Centres pay because payment accuracy is farmer loyalty, and loyalty is milk volume. A centre that pays on time through bKash with an SMS statement keeps its farmers. Processors also want clean volume and fat records for quality bonuses.

The moment: bKash payouts to thousands of farmers are now practical, and digital fat analysers are common. Ports are India, Pakistan, Kenya, Ethiopia and Sri Lanka, where the same cycle and slips exist.

### The product in 30 days (MVP)
- Farmer register with phone, village, cattle count and bKash number.
- Collection entry: session, litres, fat percent, optional SNF; rate from a fat-based chart.
- Instant Bangla SMS slip to the farmer after each entry.
- Feed and cash advance ledger per farmer with deduction rules.
- Ten-day payment run: statement per farmer, deductions, net pay, bKash payout, paid or failed status.
- Chilling stock and dispatch to the processor with fat average per dispatch.
- Leave out: veterinary services, AI cattle advice, processor invoicing, a farmer app.

### Data, integrations and the Bangladesh specifics
- bKash disbursement API for payouts; Nagad as a second rail; cash marked manually where a farmer has no wallet.
- Bangla SMS for every slip and statement; this is the feature farmers talk about.
- Fat-based rate charts as used by Milk Vita and processors, editable per centre and season.
- Manual capture from fat analysers and scales to start; Bluetooth later.
- Offline collection entry at dawn; Bangla numerals on slips; dispatch sheets in each processor's format.

### Build it with Claude
Stack: Flutter Android app for collection, Laravel web app for the office, PostgreSQL, bKash merchant and disbursement APIs, SMS gateway, Claude API for summaries, small VPS.

1. Ask Claude for the schema and the payment cycle logic. Paste:
```
Design a schema for a milk collection centre in Bangladesh: centres, farmers (phone,
bkash_number), collections (session am/pm, qty_litre, fat_pct, snf_pct, rate, amount),
rate_charts (fat band to rate), advances (feed or cash, amount, date), payment_cycles
(10-day periods), payment_lines (farmer, gross, deductions, net, status, trx_id),
dispatches (to processor, litres, avg_fat). Write SQL and the cycle close procedure.
```
Verify the close procedure against one cycle of real slips.

2. Ask Claude for the collection screen: farmer search, big fields for litres and fat, Bangla labels, instant SMS on save.

3. Ask Claude for the bKash disbursement integration with a retry queue for failed payouts and a manual cash fallback.

4. Ask Claude for the farmer messages. Paste:
```
Write a Bangla SMS statement template for a dairy farmer's 10-day payment, under 160
characters, with Bangla numerals: period, total litres, average fat, gross amount,
advance deduction, net paid, bKash transaction id. Then write a second template for
a daily collection slip: session, litres, fat, rate, amount. Give both as Laravel
Blade strings with placeholders.
```
Then ask for a dashboard: daily volume, average fat, farmers whose volume dropped, and a dispatch sheet PDF.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 centres, 300 farmers getting SMS slips |
| Day 60 | 8 centres, 2,000 farmers, 5 paying |
| Day 90 | 25 centres, 6,000 farmers, 15 paying, ৳30,000 monthly revenue |

### First customers with zero budget
- Dairy belts: Sirajganj, Pabna, Baghabari, Manikganj, Satkhira; centres sit on the main roads.
- Cooperative societies and Milk Vita primary societies; the secretary decides.
- Processors' procurement teams can open 50 collection points at once.
- Outreach angle: "How long does your ten-day payment take to calculate, and how many disputes?"
- The demo that closes: enter one morning's collections for 20 farmers and send the slips to their phones on the spot.
- Referral loop: farmers who get SMS slips demand it at neighbouring centres; a free cycle per referral.

### Pricing and the maths
- Small centre ৳999 a month: up to 300 farmers, slips, cycles. Large centre ৳2,999 a month: unlimited farmers, bKash payouts, dispatch, dashboards, processor sheets.
- Costs per centre are roughly ৳300 to ৳1,200 a month, mostly SMS; gross margin around 65 to 75 percent, so offer a daily summary SMS option.
- At a mid price of about ৳1,999, roughly 150 paying centres make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, where cooperatives pay through M-Pesa and smallholder dairy is large; India and Pakistan next.
- What changes: language, rate chart model (fat and SNF norms), payment rail, SMS gateway, processor formats.
- Reseller: a dairy processor or cooperative union that mandates it across its collection points.
- What stays the same: collection, advance, cycle and dispatch model, slip and statement templates.

### Risks and how to de-risk them
- Risk: SMS costs at two slips a day. De-risk: one daily SMS on the small plan, and price the large plan to cover it.
- Risk: bKash payout failures leave farmers unpaid. De-risk: retry queue, a failed list for the clerk, cash fallback recorded in the same cycle.
- Risk: fat readings are disputed. De-risk: record the analyser reading with a photo and send the slip instantly.
- Risk: centres are few and slow to decide. De-risk: sell through processors and unions, one contract covering many centres.

## Idea 89: Contract Farming Aggregator OS
*Farmer contracts, input advances, field visits, graded procurement and bKash payments for chip makers, feed mills and exporters who buy from thousands of contracted farmers.*

### Who pays and why now
Mid-size buyers such as chip makers, feed mills, vegetable exporters and seed companies contract thousands of farmers each season. They give inputs as advances, send field officers to visit, then buy the harvest at a fixed or graded price and deduct the advances. This runs on Excel, paper contracts and cash carried by field staff. Advances go missing, side-selling is invisible, and payments take weeks.

The buyer pays because the leakage is large and finance wants control. A company with 3,000 farmers and ৳5 crore in advances will pay ৳49,999 a month to see advances, visits and procurement per farmer and pay by bKash. Sales cycles are long, but tickets are high and churn is low.

The moment: exporters face traceability demands, feed mills are scaling maize contracting, and bKash disbursements make farmer payment auditable. Ports are India, Kenya, Nigeria, Vietnam, Indonesia and Ethiopia.

### The product in 30 days (MVP)
- Farmer and plot register with GPS, and a contract per season with quantity and price or grade table.
- Input advance issue with farmer OTP or photo acknowledgement, valued at cost.
- Field officer app: visit log with photos, crop stage, issues, expected harvest date.
- Procurement entry: weight, grade, rate, deductions, net payable.
- Payment run: net per farmer after advance recovery, bKash bulk payout, status tracking.
- Dashboard: advances outstanding, expected volume, procurement to date, recovery rate by field officer.
- Leave out: a farmer-facing app, crop insurance, agronomy AI, ERP integration.

### Data, integrations and the Bangladesh specifics
- bKash disbursement API for farmer payments, bank transfer export for large amounts; SSLCommerz or bank transfer for the subscription.
- Bangla SMS to farmers on advance, procurement and payment, which cuts disputes and fraud.
- Offline GPS and photo capture in the field app, syncing in the evening.
- Grade tables per crop (potato size, maize moisture) editable per buyer.
- Traceability export of farmer, plot, inputs, visits and harvest lot; Bangla contract printouts with Bangla numerals.

### Build it with Claude
Stack: Laravel web app, Flutter Android for field officers and collection points, PostgreSQL, bKash disbursement API, SMS gateway, Claude API for analytics, small VPS.

1. Ask Claude for the schema and roles. Paste:
```
Design a schema for a contract farming platform in Bangladesh used by a buyer company.
Entities: companies, users (roles: admin, finance, field_officer, collection_clerk),
farmers, plots (gps, size_decimal), seasons, contracts (farmer, plot, crop, qty, price
or grade_table), advances (item, qty, value, acknowledged_by), visits (photos, stage,
notes), procurements (weight, grade, rate, deductions), payments (net, bkash_trx, status).
Write SQL, role permissions, and the query for advance recovery rate by field officer.
```
Walk through it with one buyer's finance manager and adjust.

2. Ask Claude for the field officer app: farmer list by route, visit form with camera and GPS, advance issue with OTP, all offline capable.

3. Ask Claude for the web screens: contract creation with a Bangla PDF, procurement entry, and the bKash payment run with an exception list.

4. Add season analytics. Paste:
```
You are an analyst for a contract farming buyer in Bangladesh. Given JSON of farmers
with contracted qty, advances, visits count, delivered qty and grades, write a Bangla
and an English summary (under 200 words each): delivery rate vs contract, likely
side-selling (low delivery with normal visits), field officers with low recovery,
and three actions before next season. Use tables where helpful. Do not invent numbers.
```
Then ask for a pilot proposal and a 12-week implementation plan to send to a buyer.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 buyer pilot with 200 farmers and 3 field officers |
| Day 60 | 2 buyers, 1,500 farmers, first paid month |
| Day 90 | 4 buyers, 5,000 farmers, ৳80,000 monthly revenue |

### First customers with zero budget
- Target lists: snack makers, feed mills buying maize, vegetable and potato exporters, seed companies, and NGO value chain projects that fund such tools.
- LinkedIn and direct email to heads of procurement, then a factory visit; agro-processor and exporter association meetings.
- Outreach angle: "How much of last season's input advance did you recover, and how do you know?"
- The demo that closes: load 50 of their farmers from Excel, issue one advance with OTP, record one procurement, show the recovery dashboard.
- Referral loop: agronomists and consultants who serve several buyers, on a referral fee.

### Pricing and the maths
- Starter ৳9,999 a month: up to 500 farmers, 5 users. Growth ৳24,999 a month: up to 3,000 farmers, field app, bKash payouts. Enterprise ৳49,999 a month: unlimited farmers, traceability exports, analytics, priority support.
- Costs per buyer are roughly ৳1,000 to ৳5,000 a month in SMS and hosting; gross margin above 85 percent.
- At a mid price of about ৳29,999, roughly 10 paying buyers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, where contract farming with M-Pesa payments is established; India and Vietnam next.
- What changes: language, payment rail, grade tables, ID type, traceability format, SMS gateway.
- Reseller: agri consulting firms and development programmes that run value chain projects.
- What stays the same: contract, advance, visit, procurement and payment model, dashboards, analytics prompts.

### Risks and how to de-risk them
- Risk: long enterprise sales cycles starve cash. De-risk: paid pilots from month one, and buyers whose season starts within 60 days.
- Risk: field officers avoid the app because it exposes them. De-risk: management mandates it, and payments only flow through recorded data.
- Risk: exporters expect strong data security. De-risk: per-company isolation, an audit log, export and deletion on request.
- Risk: a buyer wants heavy custom features. De-risk: configuration over code, and a paid customisation rate.

## Idea 97: Beekeeper Management
*Hive records, migration schedule by flowering crop, honey batch traceability, moisture logs and buyer orders for migratory beekeepers, in Bangla.*

### Who pays and why now
Thousands of Bangladeshi beekeepers move their boxes from mustard fields in winter to litchi orchards, then to black cumin and coriander. A beekeeper with 100 to 300 boxes runs a serious business, recorded in a notebook: apiary, boxes, honey, moisture at harvest. Buyers, from exporters to online honey brands, increasingly demand traceability.

The beekeeper pays because a traceable batch fetches a better price and a brand buyer keeps coming back. Even ৳199 a month is covered by one better sale. Brands and exporters may pay for their suppliers, since it makes their own claims defensible.

The moment: online brands have made mustard honey and litchi honey consumer categories, and buyers want proof. Ports are India, Ethiopia, Kenya, Turkey, Vietnam and Pakistan, all with migratory or smallholder beekeeping.

### The product in 30 days (MVP)
- Apiary and hive register: location, crop in flower, dates, box count, queen status.
- Migration planner: flowering calendar by district and crop, with reminders to move.
- Inspection log: strength, brood, disease signs, feeding, treatments.
- Harvest and batch: honey per apiary, moisture reading, drum ids, a batch code and QR label.
- Buyer orders: buyer, batch, quantity, price, delivery, payment status.
- Public batch page per code: flower, district, harvest date, moisture, beekeeper name.
- Leave out: hive sensors, a marketplace, a processing plant module, export documents.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad for the subscription and for recording buyer payments.
- SMS reminders for migration dates and treatments; WhatsApp share of the batch page to buyers.
- Flowering calendar by district: mustard (November to January), litchi and black cumin (February to March), and others, as an editable table.
- Buyer moisture targets (roughly 18 to 21 percent) shown on harvest entry.
- QR labels on a cheap thermal printer; Bangla numerals and a Bangla batch page with an English toggle for exporters; offline logs in the field.

### Build it with Claude
Stack: Flutter Android app, Next.js for public batch pages, PostgreSQL, Claude API for batch descriptions and seasonal advice, bKash merchant API, SMS gateway, Cloudflare.

1. Ask Claude for the schema. Paste:
```
Design a schema for a migratory beekeeping app in Bangladesh: beekeepers, apiaries
(location, district, crop, start_date, end_date, box_count), inspections, treatments,
harvests (apiary, date, kg, moisture_pct), batches (code, drums, blended from harvests),
buyers, orders, payments, flowering_calendar (district, crop, start_month, end_month).
Write SQL and a function that generates a readable batch code like BD-MST-DNJ-2601-07.
```
Check the code format with two beekeepers and one buyer.

2. Ask Claude for the Flutter screens: apiary card with box count and days in place, quick inspection form, harvest entry with a moisture target.

3. Ask Claude for the Next.js public batch page with QR, Bangla and English, and a verified look that buyers trust.

4. Add batch copy and seasonal advice. Paste:
```
Write a Bangla product description for a honey batch from these fields: flower source,
district, harvest dates, moisture percent, beekeeper name, box count. Honest tone, no
health claims, under 80 words, Bangla numerals. Add a one-line English summary.
Then, separately, given the current month and district, list in Bangla the next two
flowering crops nearby and a suggested move date range from the calendar data I provide.
```
Then ask for a Bangla WhatsApp message beekeepers can send buyers with the batch link.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 20 beekeepers logging apiaries in the mustard season |
| Day 60 | 100 beekeepers, 300 batches with QR, 40 paying |
| Day 90 | 300 beekeepers, 150 paying, two brands buying by batch code |

### First customers with zero budget
- Facebook beekeeping groups and beekeeper association pages, where beekeepers post migration photos constantly.
- Mustard fields in Sirajganj, Pabna, Natore and Dinajpur in December; beekeepers camp beside the road.
- BSCIC and agricultural extension beekeeping training groups; trainers can recommend it.
- Outreach angle: "Which apiary gave your best honey last season, and can you prove it to a buyer?"
- The demo that closes: register this apiary, enter last week's harvest, print a QR label and open the batch page on the buyer's phone.
- Referral loop: honey brands ask their other suppliers to use it; give the brand a free buyer dashboard.

### Pricing and the maths
- Basic ৳199 a month: up to 50 boxes, logs, calendar. Pro ৳599 a month: unlimited boxes, batch QR pages, buyer orders, advice.
- Costs per beekeeper are roughly ৳20 to ৳60 a month in SMS and AI; gross margin around 85 percent.
- At a mid price of about ৳399, roughly 750 paying beekeepers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where migratory beekeeping follows mustard and litchi on a similar calendar and UPI is universal; Ethiopia and Turkey for export traceability.
- What changes: language pack, flowering calendar, moisture and grading standards, payment rail, SMS gateway.
- Reseller: honey exporters and cooperatives that need traceability from suppliers.
- What stays the same: apiary, inspection, harvest, batch and order model, the QR batch page.

### Risks and how to de-risk them
- Risk: a low price makes acquisition costly. De-risk: sell through brands and associations, and let brands sponsor their suppliers.
- Risk: beekeepers fake batch data. De-risk: photos and GPS on harvest entry, a moisture reading photo, and buyer verification marks.
- Risk: seasonal use and off-season churn. De-risk: discounted annual pricing, plus off-season orders and equipment logs.
- Risk: QR pages are copied. De-risk: unique codes, view counts, and the beekeeper's verified phone on the page.


---

# Section 7: Agriculture and Food (Part 2)

This section covers the businesses that sit around the harvest and the kitchen: cold storages, tea gardens, fishing boats, irrigation pumps, cottage food brands, tiffin kitchens and plant nurseries. Each one still runs on paper bonds, share slips and memory, and each one will pay for software that ends a dispute or shows a real profit.

## Idea 33: Cold Storage Management
*Lots, bonds, loans and temperature logs for the cold storages that hold the potato harvest.*

### Who pays and why now
Bangladesh has around 400 cold storages, most of them in the potato belt of Munshiganj, Bogura, Rangpur and Thakurgaon. Each one takes in stock from hundreds of farmers and traders between February and April, issues a paper bond per lot, and releases stock from July onwards. The manager runs it on ledgers, carbon-copy bond books and a phone full of calls.

The pain is money. Many storages lend against stock, and rent, loan and interest are settled at release from the same paper bond. Lost bonds, disputed bag counts and unrecorded partial releases cost real money every season, and the financing bank wants a clean stock report. Owners now carry smartphones and bKash settles rent at release, so the moment is right. The same model ports to Uttar Pradesh and West Bengal in India, to Pakistan and to Egypt, where potato storages run on the same bond system.

### The product in 30 days (MVP)
- Intake: farmer or trader profile, lot number, bags, weight, variety, chamber and rack.
- Bond issuance: printed Bangla bond with a QR code and terms, plus an SMS copy to the farmer.
- Loan against stock: advance, interest rule, due at release, linked to the lot.
- Release: farmer requests a date, manager approves, partial releases reduce the lot balance.
- Settlement slip: rent, loan, interest and deductions computed and printed, paid by cash or bKash.
- Temperature log per chamber with out-of-range alerts to the owner.
- Leave out: IoT sensors, bank API integration, a potato marketplace, multi-facility groups.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for rent and loan repayment at release; cash entries get a receipt SMS.
- Bangla SMS for bond confirmation, release approval and dues, because many farmers are not on WhatsApp.
- The bond layout must match what the storage already prints, with Bangla numerals for bags and amounts.
- The loading dock often has no network, so intake must queue on a tablet and sync later.
- Stock statements as PDF for the financing bank.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Flutter Android app for the dock, Claude API for Bangla text, small VPS, bKash merchant API.

1. Ask Claude for the data model and use the migrations it returns.

```
Design a PostgreSQL schema for a potato cold storage in Bangladesh. Entities: facility, chamber, farmer,
lot (bags, kg, variety, chamber, intake date), bond (number, QR token), loan_against_lot (principal,
monthly interest rate, start date), release (partial allowed), settlement (rent per bag, interest,
deductions, paid via cash or bKash), temperature_log. Give Laravel migrations and a query that
returns the balance owed per lot today.
```

2. Ask Claude for the Flutter intake app with an offline queue. Tell it the tablet is used with gloves in a cold dock, so buttons must be large and each entry must take under 30 seconds.

3. Ask Claude for the bond and release slip in Bangla, print them, and compare with the storage's current bond.

```
Write a Bangla cold storage bond (হিমাগার বন্ড) for A5 printing. Fields: facility, bond number, farmer
name and phone, lot number, bags, kg, variety, chamber, intake date, rent per bag, and 4 short terms
(rent due at release, loan interest, damage clause, lost bond procedure). Use Bangla numerals.
Then write a matching release slip (ছাড়পত্র) with rent, loan, interest, deductions and net payable.
```

4. Ask Claude to write the settlement calculator as a pure function with unit tests. Check three real bonds from a friendly storage against its output, then wire it to the release screen and the owner dashboard.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 pilot storage running intake and bonds for one chamber |
| Day 60 | 3 storages live, 5,000 lots recorded, first paid invoice |
| Day 90 | 6 paying storages, roughly ৳1.5 lakh monthly revenue |

### First customers with zero budget
- The cold storage owners' association and its district branches; ask for ten minutes at a members' meeting before intake season.
- Owners cluster in Munshiganj, Bogura and Rangpur; visit with a tablet. Google Maps "cold storage" listings give addresses and phones.
- Outreach angle: "Stop losing money on lost bonds and disputed releases. See your stock from your phone."
- The demo that closes: enter a lot, print a bond, do a partial release and show the settlement in three minutes.
- Referral loop: one month free for each referred storage that goes live, and a clean stock statement that financing banks recommend.

### Pricing and the maths
- ৳15,000 to ৳40,000 per month per facility, priced by capacity in bags.
- SMS to farmers costs roughly ৳2,000 to ৳5,000 per facility per season plus a small VPS, so gross margin is above 85 percent.
- At the mid price of ৳27,500, about 11 facilities make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Uttar Pradesh and West Bengal, with thousands of potato storages on the same bond and loan-against-stock pattern.
- Changes: Hindi and Indian Bengali language pack, UPI instead of bKash, local bond format and rent rules; then Pakistan with Urdu and JazzCash, and Egypt with Arabic.
- What stays the same: the lot, bond, loan, release and temperature model, the dock app and the owner dashboard.

### Risks and how to de-risk them
- Risk: a long sales cycle with only 400 buyers. De-risk: sign the first pilot before intake season and price so that six customers pay the team.
- Risk: managers resist because paper hides leakage. De-risk: sell to the owner and show the owner dashboard first.
- Risk: no network at the dock. De-risk: offline-first app with sync and conflict rules from day one.
- Risk: printed bonds carry legal weight. De-risk: keep the existing wording, add a QR code and an immutable audit log.

## Idea 36: Cottage Food Brand OS
*Recipe costing, batch logs, BSTI-ready labels and retailer dues for small food brands.*

### Who pays and why now
Thousands of home and small-factory food brands sell achar, chanachur, ghee, honey, cakes and spice mixes through Facebook pages and to local shops. The founder cooks, posts, packs, delivers and chases dues. Costing is a guess, batch dates live on a notebook page, and retailer credit is a WhatsApp thread nobody adds up.

They pay because three things hurt at once. Ingredient prices swing and eat the margin before anyone notices. Supermarkets and online grocers ask for proper labels with batch, expiry, net weight and BSTI fields before they list a product. Retailers take stock on credit and return unsold jars, and the brand loses track of both. A tool that prices a recipe, prints a compliant label and shows who owes what is worth a small monthly fee. The moment is now because BSTI enforcement is rising and online grocers are opening shelves to small brands. Ports are India, Pakistan, Indonesia and Nigeria, each with its own food label regulator.

### The product in 30 days (MVP)
- Recipe costing: ingredients, packaging, labour and overhead per batch, cost per unit, suggested price at a target margin.
- Batch log: batch number, date, quantity, expiry, linked to the recipe used.
- Label generator: PDF labels with product name, ingredients, net weight, MRP, batch, manufacture and expiry dates, licence number and address, in Bangla and English.
- Order book: retailer and distributor orders, delivery challan and invoice.
- Dues ledger: credit per retailer, payments, ageing, Bangla SMS reminders.
- Returns and damages recorded per batch and deducted from dues.
- Leave out: online storefront, accounting export, multi-warehouse stock, marketplace integrations.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad for retailer payments and the subscription; SSLCommerz later for card payers.
- SMS for dues reminders and delivery notices; retailers rarely read email.
- BSTI CM licence number and the mandatory label items under Bangladesh labelling rules; keep the label field list editable because rules change.
- Bangla numerals and a clean Bangla font on labels; EAN-13 barcode generation for supermarkets.
- The brand maintains its own ingredient price list; the app re-costs every recipe when a price changes.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for label copy and reminders, Cloudflare hosting, bKash merchant API.

1. Ask Claude for the schema and the costing logic together, so unit cost is always derived from the latest ingredient prices.

```
Design a PostgreSQL schema for a small food brand: ingredient (unit, current price), recipe, recipe_line
(quantity, yield), packaging_item, batch (recipe, quantity produced, expiry), product (recipe, pack size),
retailer, order, order_line, payment, return. Write a SQL view that gives cost per unit for each product
using current prices, and a Next.js API route that returns suggested price at a given margin.
```

2. Ask Claude for the label template as a printable HTML page sized for common sticker sheets (A4 with 12 or 24 labels). Print one sheet and check it against a real supermarket label.

```
Create a printable HTML label template for a Bangladeshi food product on an A4 sheet of 24 stickers.
Each label shows: product name in Bangla and English, ingredients in Bangla, net weight, MRP in ৳,
batch number, MFG and EXP dates, BSTI licence number, manufacturer address, EAN-13 barcode.
Use Bangla numerals for dates, weight and price. Keep every field editable from a JSON object.
```

3. Ask Claude for the dues ledger screens and the Bangla SMS reminder text in three tones: friendly at 7 days, firm at 21 days, final at 45 days.

4. Ask Claude for an onboarding importer that takes a pasted WhatsApp list of retailers and their balances and creates the ledger, so a brand is live in ten minutes.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 brands costing recipes on the free tier |
| Day 60 | 40 brands, 15 paying, 500 labels printed |
| Day 90 | 100 brands, 50 paying, roughly ৳50,000 monthly revenue |

### First customers with zero budget
- Facebook groups for women entrepreneurs and homemade food sellers, where members post daily about pricing and BSTI licences.
- SME Foundation fairs and Baishakhi melas, where small brands sit at stalls for a week with time to talk.
- BSTI licence consultants and packaging printers; they meet every new brand and can refer.
- Outreach angle: "Do you know your real cost per jar after this month's oil price?"
- The demo that closes: cost one of their recipes live and print a label with their name in ten minutes.
- Referral loop: a free month for each referred brand, and a small footer on the printed invoice.

### Pricing and the maths
- ৳499 to ৳1,999 per month depending on products, retailers and label volume.
- Costs are SMS and hosting, roughly ৳30 to ৳80 per brand per month, so gross margin is above 90 percent.
- At the mid price of about ৳1,249, roughly 240 paying brands make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where FSSAI label rules replace BSTI fields and UPI replaces bKash; the Hindi and Bengali packs cover a huge home-food market.
- Then Pakistan (Urdu, PSQCA fields, JazzCash), Indonesia (Bahasa, BPOM and halal fields) and Nigeria (NAFDAC fields).
- What stays the same: costing, batches, dues, returns and the label engine with a swappable field list.

### Risks and how to de-risk them
- Risk: tiny brands churn when sales dip. De-risk: keep costing free forever and charge for labels and dues.
- Risk: costing is only as good as the prices entered. De-risk: prompt for price updates on every new batch.
- Risk: label rules change. De-risk: field list lives in configuration, not code, and a monthly check of BSTI notices.
- Risk: price sensitivity. De-risk: sell on money saved per batch, not on features.

## Idea 49: Tea Garden Management
*Daily plucking weights, wages, rations and section yields for the gardens of Sylhet and Chattogram.*

### Who pays and why now
Bangladesh has around 160 tea gardens in Moulvibazar, Habiganj, Sylhet, Chattogram and Panchagarh, employing tens of thousands of pluckers. Three times a day a clerk weighs each worker's leaf at a weighing point and writes it on a sheet. The weekly wage is a base rate plus a per-kilogram extra above a daily target, minus deductions, plus rations and other entitlements. Everything is recomputed by hand in the garden office.

Owners pay because errors are expensive on both sides. Wage disputes stop plucking, leaf leakage hides in bad records, and group head offices in Dhaka and Chattogram cannot see section yields until month end. Buyers and certification auditors now ask for attendance, wage and leave registers on demand. The moment is right because mobile coverage reaches most gardens and the wage agreement has become formal enough to encode. Ports are Assam, Darjeeling and Kerala in India, then Sri Lanka, Kenya, Vietnam and Indonesia.

### The product in 30 days (MVP)
- Worker register: ID, section, category (permanent or casual), dependents and ration entitlement.
- Weight capture: clerk records kg per worker per round on a phone, offline, with section and date.
- Wage engine: daily target, base wage, per-kg extra, deductions, weekly payroll sheet in Bangla and English.
- Ration and benefit calculation per worker per week.
- Section yields: green leaf per section per day and days since last plucking round.
- Attendance and leave register with printable compliance reports.
- Leave out: factory processing, auction sales, GPS section maps, biometric attendance.

### Data, integrations and the Bangladesh specifics
- Payroll is mostly cash, so the app prints signature and thumbprint sheets; the garden pays the subscription by bank transfer.
- SMS to sardars and clerks for round summaries; workers rarely have smartphones.
- Wage and ration rates come from the collective agreement and the Bangladesh Labour Act; each garden enters its own rates.
- Bangla numerals on payroll sheets; English for head office reports.
- Sections have no network, so the clerk app must work offline all day and sync in the evening.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Flutter Android app for weighing clerks, Claude API for report text, small VPS.

1. Ask Claude for the schema and the wage engine with tests built from one real week of paper sheets.

```
Design a PostgreSQL schema for a tea garden: worker (category, section, dependents), section, weighing
(worker, date, round, kg), wage_rule (daily target kg, base wage, extra per kg, valid from), deduction,
ration_rule, attendance, leave. Then write a PHP class that computes a worker's weekly wage and ration
from these tables, with unit tests for a worker under target, at target and 12 kg over target.
```

2. Ask Claude for the Flutter weighing screen: pick section, tap worker photo or ID, type kg, next. Ask for a two-second-per-entry design with an offline queue and duplicate protection.

3. Ask Claude for the printable payroll and compliance registers in Bangla.

```
Create printable HTML templates for a Bangladeshi tea garden: (1) weekly payroll sheet with worker ID,
name, days, total kg, base wage, extra, deductions, net pay, signature or thumbprint column; (2) weekly
ration register; (3) monthly attendance and leave register. Use Bangla numerals, landscape A4, and a
header with garden name, section and week. Make them fill from a JSON payload.
```

4. Ask Claude for the head office dashboard: yield per section per day, cost per kg of green leaf, and a weekly summary email in English.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 garden pilot, one division, weights and payroll running |
| Day 60 | 2 gardens live, full payroll replacing paper for 1,500 workers |
| Day 90 | 3 to 4 paying gardens, roughly ৳1 lakh monthly revenue |

### First customers with zero budget
- The tea association's members' meetings and the Bangladesh Tea Board's events; owners and general managers attend.
- Group companies with several gardens have head offices in Dhaka and Chattogram; one meeting can open five gardens.
- Garden managers socialise in Srimangal; a manager who likes the app brings his neighbours.
- Outreach angle: "Weekly payroll in an hour, not two days, and no wage disputes at the office window."
- The demo that closes: record one round of weights for 20 workers and print the weekly payroll on the spot.
- Referral loop: a free quarter for any garden that brings a sister garden live.

### Pricing and the maths
- ৳15,000 to ৳50,000 per month per garden, priced by worker count.
- Costs are SMS and a VPS, under ৳3,000 per garden per month, so gross margin is above 85 percent.
- At the mid price of ৳32,500, roughly 9 gardens make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Assam, with hundreds of gardens on the same wage-plus-ration structure; Assamese, Bengali and Hindi packs, UPI or bank payroll.
- Then Sri Lanka (Tamil and Sinhala estates) and Kenya (Swahili, plus smallholder collection points).
- What stays the same: worker, weighing, wage engine, section yields and compliance registers; only rates and forms change.

### Risks and how to de-risk them
- Risk: very few buyers and slow decisions. De-risk: start with a group company and price so four gardens sustain the team.
- Risk: workers and unions distrust digital weighing. De-risk: print the round summary and post it at the weighing point every day.
- Risk: wage rules differ by garden. De-risk: all rates and rules live in configuration with a validity date.
- Risk: connectivity. De-risk: offline-first clerk app, end-of-day sync, and a paper fallback template that matches the app.

## Idea 66: Fishing Boat Owner Ledger
*Trip costs, catch sales and crew share settlement for trawler and boat owners on the coast.*

### Who pays and why now
Tens of thousands of mechanised boats and trawlers work out of Cox's Bazar, Chattogram, Barguna, Patuakhali, Bhola and Khulna. Before each trip the owner advances fuel, ice, food and net repairs. When the boat returns, the catch is sold at the landing centre through an arotdar, costs are deducted, and the remainder is split between owner and crew by shares, with the majhi taking more than a deckhand. Advances given to crew before the season are deducted too. All of this is settled on a slip of paper, often at night, often in dispute.

Owners with two to ten boats pay because they cannot see profit per boat per season, and because every disputed settlement costs them a crew member. A clear slip for each crew member ends the argument. The moment is right because bKash is common on the ghat, smartphones are in every pocket, and the annual fishing bans make seasonal profit a real question. Ports are India, Indonesia, the Philippines, Sri Lanka, Nigeria, Kenya and Senegal, everywhere crews are paid by share.

### The product in 30 days (MVP)
- Boat and crew register with roles (majhi, engine driver, fisher) and share weights per role.
- Trip sheet: departure, return, expenses by category (fuel, ice, food, repairs, ghat fees).
- Catch sales: species, quantity, price, arotdar and commission, entered from the sale note.
- Crew share calculator with a configurable rule per boat, producing a Bangla settlement slip per person.
- Crew advances ledger with automatic deduction at settlement.
- Season summary per boat: trips, revenue, costs, owner profit.
- Leave out: GPS tracking, a fish marketplace, arotdar loan management, licence renewals.

### Data, integrations and the Bangladesh specifics
- bKash for crew payouts and the subscription; cash still recorded with an SMS slip to each crew member.
- Share rules differ by region: Cox's Bazar and Barguna deduct costs differently and weight roles differently, so rules are configuration, not code.
- Bangla species list (ilish, loitta, chingri, rupchanda, poa) and Bangla numerals on slips.
- Offline entry on the ghat with sync later; pairs with the wholesale arot ledger (idea 34) to import sale notes.

### Build it with Claude
Stack: Flutter Android app for the owner, Laravel API with PostgreSQL, Claude API for Bangla slip text, small VPS, bKash merchant API.

1. Collect three real settlement slips from different ghats. Ask Claude to turn them into a configurable rule model and to point out where they differ.

```
Here are three fishing trip settlements from Bangladesh (pasted below). Design a JSON rule format that
can express each one: which expenses are deducted before the split, owner share percentage, role weights
(majhi, engine driver, fisher), how crew advances are deducted, and rounding. Then write a Dart function
settleTrip(rule, trip) that returns the payout per crew member, with tests reproducing all three slips.
```

2. Ask Claude for the PostgreSQL schema and Laravel API for boats, crew, trips, expenses, sales, advances and settlements, with a season summary endpoint.

3. Ask Claude for the Flutter trip screens: one screen to log expenses before departure, one to enter the sale note, one to confirm and send slips.

```
Write the Bangla text of a crew settlement slip sent by SMS (under 300 characters). Include boat name,
trip dates, total sale, total costs, crew pool, this person's role and share, advance deducted, and net
payable. Use Bangla numerals. Then write a 60-second Bangla script the owner can use to explain the
slip to crew who have never seen one.
```

4. Ask Claude for the season dashboard and a one-page PDF per boat that the owner can show an arotdar when negotiating next season's advance.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 owners at one ghat settling trips in the app |
| Day 60 | 40 owners, 15 paying, 200 trips recorded |
| Day 90 | 120 owners, 60 paying, roughly ৳60,000 monthly revenue |

### First customers with zero budget
- Boat owners' associations in Cox's Bazar, Barguna and Patuakhali; ask for time at a meeting before the season opens.
- Landing centres such as Cox's Bazar fishery ghat, Patharghata, Mohipur and Alipur; owners are there every landing day.
- Arotdars as a channel: they see every owner and gain from cleaner settlements.
- Outreach angle: "No more arguments at midnight. Every crew member gets his own slip on his phone."
- The demo that closes: settle their last trip live from the paper slip and match it to the taka.
- Referral loop: crew who receive slips ask other owners for the same, and the slip carries the app name.

### Pricing and the maths
- ৳499 to ৳1,499 per month per owner, by number of boats.
- SMS slips cost roughly ৳15 to ৳30 per trip, plus hosting, so gross margin is around 80 percent.
- At the mid price of ৳999, roughly 300 paying owners make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India's east coast, West Bengal and Odisha, where the same fish, the same share tradition and, in West Bengal, the same language apply; UPI replaces bKash.
- Then Indonesia and the Philippines, where crew share systems are widespread and boat counts are far larger.
- What stays the same: trip, sale, rule engine and slip; only rule templates, species lists and payment rails change.

### Risks and how to de-risk them
- Risk: seasonal bans pause use and payments. De-risk: annual pricing with a discount, and the season summary as the reason to stay.
- Risk: crew distrust a phone slip. De-risk: print the slip at the ghat as well, and keep the paper format familiar.
- Risk: share rules too varied. De-risk: rule templates per ghat, built from real slips, editable by the owner.
- Risk: low price and scattered customers. De-risk: sell through associations and arotdars, not one owner at a time.

## Idea 78: Office Tiffin and Catering Subscription Manager
*Menus, meal counts, pauses, routes and bKash billing for kitchens that feed office workers.*

### Who pays and why now
Hundreds of tiffin and catering kitchens feed office workers in Motijheel, Karwan Bazar, Banani, Gulshan, Uttara and Mirpur, and in Chattogram and Sylhet. A typical kitchen serves 50 to 500 lunches a day. Orders arrive on WhatsApp, pauses are announced in a group chat, the cook guesses tomorrow's quantities, and the owner collects monthly payments by chasing each subscriber.

They pay because each mistake costs cash. A missed pause means a wasted meal, a missed resume means an angry customer, a wrong count means either waste or a short delivery. Monthly collection takes days and the owner never knows who has paid. Software that gives tomorrow's exact count, a rider list per route and a bKash bill that prorates paused days pays for itself in a week. The moment is right because offices are full again, bKash payment links work for everyone, and WhatsApp is where subscribers already are. Ports are India (dabba services), Indonesia (office catering), Nigeria, Egypt and Pakistan.

### The product in 30 days (MVP)
- Subscriber profiles: office address, route, plan (lunch, lunch and snack), dietary notes.
- Weekly menu publisher that sends the Bangla menu to subscribers on WhatsApp or SMS.
- Pause and resume by the subscriber through a web link or a WhatsApp keyword before a daily cutoff.
- Daily count by route and by dish, plus a kitchen prep sheet scaled from per-portion quantities.
- Route delivery list per rider with tick-off and a missed-delivery note.
- Monthly billing prorated for paused days, bKash payment link, reminders and payment status.
- Leave out: rider GPS, a customer mobile app, marketplace listing, ingredient purchasing.

### Data, integrations and the Bangladesh specifics
- bKash payment links or merchant API for monthly bills; Nagad as the second option.
- WhatsApp Business API for menus and pauses, with SMS as the fallback while Meta verification is pending.
- Bangla menus and bills with Bangla numerals; halal by default and a Ramadan mode that switches lunch to sehri or iftar packs.
- Billing calendar that knows Friday and public holidays, so prorating matches working days.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for menu and message copy, Cloudflare hosting, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema and the two calculations that matter: tomorrow's count and this month's prorated bill.

```
Design a PostgreSQL schema for a tiffin subscription kitchen in Dhaka: subscriber (office, route, plan),
plan (price per working day), pause (start, end), menu_day (dishes), delivery (date, rider, status),
invoice, payment. Write SQL for (1) tomorrow's meal count by route and dish given pauses and cutoff,
and (2) a monthly invoice that charges only working days not paused, skipping Fridays and a holiday table.
```

2. Ask Claude for the pause flow: a WhatsApp message with the word "pause" plus a date range, parsed and confirmed in Bangla, with the same logic on a simple web link.

3. Ask Claude for the kitchen prep sheet: per-portion quantities per dish multiplied by tomorrow's count, printed in Bangla for the cook.

```
Write a Bangla WhatsApp message set for a Dhaka office tiffin service: (1) the weekly menu with day and
dishes, (2) confirmation of a pause with dates, (3) a reminder the evening before resume, (4) the monthly
bill with days served, paused days, amount and a bKash link, (5) a polite payment reminder after 3 days.
Keep each under 300 characters and use Bangla numerals.
```

4. Ask Claude for the rider route page that works on a cheap phone, with one tap per delivery and a photo option for disputes.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 kitchens running daily counts and routes |
| Day 60 | 20 kitchens, 10 paying, 2,000 meals a day tracked |
| Day 90 | 60 kitchens, 35 paying, roughly ৳35,000 monthly revenue |

### First customers with zero budget
- Facebook pages of homemade tiffin and catering services; search "tiffin service Dhaka" and message each one.
- Google Maps "catering service" and "tiffin" listings in Motijheel, Gulshan, Banani and Uttara for phone numbers.
- Office admin managers who arrange lunch; one office can bring the kitchen and 100 subscribers at once.
- Outreach angle: "Know tomorrow's exact count tonight, and collect the month in a day."
- The demo that closes: paste their WhatsApp subscriber list, publish this week's menu and show tomorrow's count.
- Referral loop: every subscriber sees the pause link and the bill footer, and kitchens talk in supplier markets.

### Pricing and the maths
- ৳499 to ৳1,499 per month per kitchen, by subscriber count.
- WhatsApp conversation fees and SMS are roughly ৳100 to ৳300 per kitchen per month, so gross margin is around 75 percent.
- At the mid price of ৳999, roughly 300 paying kitchens make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where dabba and office meal services are huge; Hindi and Marathi packs, UPI links, and a holiday table per state.
- Then Indonesia (Bahasa, GoPay or bank transfer) and Pakistan (Urdu, JazzCash).
- What stays the same: subscriber, pause, count, route and prorated billing; only language, payment rail and calendar change.

### Risks and how to de-risk them
- Risk: WhatsApp API costs and verification delays. De-risk: launch on SMS and a web link, add WhatsApp when volume justifies it.
- Risk: small kitchens close or churn. De-risk: target kitchens above 80 subscribers and charge yearly with a discount.
- Risk: subscribers ignore the cutoff. De-risk: a reminder message at 8 p.m. and a clear rule that late pauses are billed.
- Risk: generic tools compete. De-risk: the prorated bKash bill and the Bangla prep sheet are the wedge nobody else builds.

## Idea 81: Deep Tube Well Water-Selling Ledger
*Season contracts, hourly water logs, diesel costs and harvest-time collection for pump owners.*

### Who pays and why now
Hundreds of thousands of deep and shallow tube well owners sell irrigation water to neighbouring farmers, mostly for the Boro rice season from January to May, across Rajshahi, Rangpur, Bogura, Dinajpur, Mymensingh and Cumilla. The owner charges by the hour or by the bigha for the season, pays for diesel or electricity all season, and collects at harvest, often partly in paddy. The record is a khata or memory, and every harvest brings arguments about hours.

Owners pay because the ledger settles the argument and shows whether the season made money after fuel. The price is small, ৳199 to ৳499 per season, so the product wins through distribution rather than selling one pump at a time. Bundle it with the agri input shop ledger (idea 12) and the paravet field app (idea 50) as one rural pack sold through dealers. The moment is right because cheap Android phones reach every village and diesel prices move sharply. Ports are Punjab, Uttar Pradesh and Bihar in India, then Pakistan and Nepal.

### The product in 30 days (MVP)
- Farmer list with plots in bigha or katha and a season contract per plot: per-bigha rate or per-hour rate.
- Water log: date, farmer, hours or plots, entered by the operator in under fifteen seconds, offline.
- Cost log: diesel litres and price, electricity units or prepaid recharge, operator wage, repairs.
- Farmer statement at any time: hours, amount due, payments so far, printable or by Bangla SMS.
- Harvest collection: cash, bKash, or paddy by maund converted at an agreed rate.
- Season profit per pump: revenue less costs, with cost per hour of pumping.
- Leave out: farmer-facing scheduling app, water meter hardware, loans, multi-pump company dashboards.

### Data, integrations and the Bangladesh specifics
- Collection is mostly cash and paddy; bKash and Nagad where the farmer has them; the season fee paid by bKash or through the dealer.
- Bangla SMS statements, since farmers rarely use WhatsApp; Bangla numerals throughout.
- Local units and customs: bigha, katha, decimal and maund, with per-district defaults the owner can change.
- Offline first: the phone may see network only at the bazar, so all entry is local with sync when connected.
- Barind prepaid card water schemes are a separate model; skip them in version one.

### Build it with Claude
Stack: Flutter Android app with a local SQLite database, small Laravel API with PostgreSQL for sync and dealer resale, Claude API for Bangla statement text, bKash merchant API.

1. Interview five pump owners and write down how each one charges. Ask Claude to model the rate options and the in-kind paddy conversion.

```
Pump owners in Bangladesh charge irrigation water in different ways: per hour, per bigha per season,
per bigha per watering, sometimes paid partly in paddy by maund at harvest. Design a Dart data model and a
function that computes a farmer's season balance from a contract, a list of water log entries, cost-free
hours (rain days), and payments in cash or paddy at an agreed rate. Include tests for all four contract types.
```

2. Ask Claude for the Flutter screens with a quick-entry design: pick farmer from a large-button list, tap hours, done. Ask for SQLite storage and background sync.

3. Ask Claude for the Bangla farmer statement and the harvest reminder.

```
Write a Bangla SMS statement (under 300 characters) from a tube well owner to a farmer: owner name, plot,
total hours or bighas this season, rate, amount due, paid so far, balance, and a polite note that
collection is at harvest. Use Bangla numerals. Then write a second SMS reminding about harvest collection
with a bKash number, and a third thanking the farmer after payment.
```

4. Ask Claude for a dealer reseller flow: dealers buy season codes in bulk, activate a pump owner's app with a code, and see which customers use it.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 20 pumps in one upazila logging water daily |
| Day 60 | 200 pumps through 5 dealers, first paid season codes |
| Day 90 | 1,000 pumps paid for the season, roughly ৳3 lakh season revenue |

### First customers with zero budget
- Agri input dealers in the Boro districts; they know every pump owner and can sell season codes with fertiliser.
- Union Digital Centres and farmers' Facebook groups, where owners already ask about diesel prices.
- BADC and BMDA pump operator groups, whose members often also own private pumps.
- Outreach angle: "Know every hour you pumped for every plot. No arguments at harvest."
- The demo that closes: log ten hours for one farmer and send him the Bangla statement while he watches.
- Referral loop: every SMS statement carries the app name, and farmers ask other pump owners for the same.

### Pricing and the maths
- ৳199 to ৳499 per pump per season.
- SMS costs roughly ৳20 per pump per season plus hosting, so gross margin is around 80 percent.
- At the mid price of ৳349 with one paid season a year, roughly 10,000 pumps make ৳36 lakh a year, about ৳3 lakh a month, which is why dealer distribution matters.

### Country kit: taking it to other languages
- First port: Bihar and Uttar Pradesh, where informal water selling is enormous; Hindi pack, UPI, and local units (katha, bigha vary by district).
- Then Pakistani Punjab (Urdu, JazzCash, acre and canal-hour customs) and Nepal (Nepali, eSewa).
- What stays the same: contract types, water log, cost log, statements and season profit.

### Risks and how to de-risk them
- Risk: very low price per customer. De-risk: sell through dealers in bulk and bundle with ideas 12 and 50.
- Risk: owners use it one season and forget. De-risk: an SMS before Boro season with last year's profit and a renewal code.
- Risk: in-kind paddy payments complicate the maths. De-risk: agreed conversion rate stored per farmer with a simple maund entry.
- Risk: no network in the field. De-risk: local database first, sync is a bonus.

## Idea 101: Plant Nursery and Landscaping Manager
*Stock by species and size, catalogue links, project quotes and Bangla care reminders for nurseries.*

### Who pays and why now
Thousands of nurseries sell plants from Agargaon and Savar in Dhaka, the Jhikargacha belt in Jashore and every district town, while rooftop gardening has made a hobby into a daily trade on Facebook. A nursery owner answers "do you have a grafted mango in a 12-inch pot" from memory, quotes a rooftop garden project on a notebook page, and loses the customer when the plant dies at home for want of care instructions.

They pay because stock questions lose sales, quotes take an evening and dead plants bring blame. A catalogue link that answers stock questions, a quote builder for landscaping jobs and Bangla care reminders that keep plants alive turn a nursery into a brand with repeat buyers. The moment is right because Facebook Live selling and courier delivery have made distance sales normal. Ports are India, Pakistan, Indonesia, Kenya, Egypt and Nigeria.

### The product in 30 days (MVP)
- Stock by species and size: Bangla and English names, pot size or height, photo, price, seasonal availability flag.
- Shareable catalogue link with a WhatsApp order button, filtered by category (fruit, flower, indoor, herb).
- Orders and delivery: address, courier or own van, payment status, delivery note.
- Project quote builder: plants, pots, soil, labour, transport, printed as a Bangla PDF and converted to an order.
- Plant care reminders: Bangla SMS or WhatsApp to the buyer at day 3, 14 and 30, species-specific, drafted by Claude and approved by the nursery.
- Seasonal reorder prompts when winter seedlings or monsoon saplings arrive.
- Leave out: a full storefront with card checkout, seeds and fertiliser inventory, staff payroll, multiple branches.

### Data, integrations and the Bangladesh specifics
- bKash for orders and the subscription; cash on delivery recorded with an SMS receipt.
- WhatsApp for orders and care messages, SMS as fallback; Bangla numerals in catalogue prices and quotes.
- A starter species list of about 300 common plants in Bangla and English, built with Claude and checked by two nursery owners.
- A Bangladesh planting calendar: winter flowers from November, monsoon fruit saplings from June, indoor plants year round.
- Photo storage on Cloudflare R2 with automatic resizing.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for care messages and quotes, Cloudflare Pages and R2, bKash merchant API.

1. Ask Claude for the schema and the species seed data together.

```
Design a PostgreSQL schema for a plant nursery in Bangladesh: species (Bangla name, English name, category,
care profile: light, water, season), stock_item (species, size, pot, price, quantity, available flag,
photos), order, order_line, delivery, project_quote, quote_line, care_message (buyer, day offset, sent).
Then generate seed data for 300 common Bangladeshi nursery plants with Bangla and English names and a
one-line care profile each, as SQL inserts.
```

2. Ask Claude for the catalogue page: fast on a cheap phone, one photo per item, WhatsApp button with the item name prefilled, and a shareable link per nursery.

3. Ask Claude for the care message generator and review the first fifty messages with a nursery owner before enabling it.

```
Write a function that, given a species care profile and a purchase date, produces three Bangla care
messages (day 3, day 14, day 30) for a Dhaka rooftop gardener. Each under 250 characters, friendly,
specific to the plant (watering, light, fertiliser, common mistake), with Bangla numerals. Include the
nursery name and a line inviting a WhatsApp question. Show three example outputs for lemon, rose and monstera.
```

4. Ask Claude for the project quote builder: pick items, add labour and transport, print a Bangla PDF with the nursery's logo, and convert an accepted quote to an order and a delivery.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 nurseries with live catalogue links |
| Day 60 | 60 nurseries, 20 paying, 1,000 care messages sent |
| Day 90 | 150 nurseries, 70 paying, roughly ৳45,000 monthly revenue |

### First customers with zero budget
- Rooftop gardening Facebook groups, where nurseries already post stock photos.
- The nursery rows in Agargaon and Savar and the Jhikargacha belt; walk the row with a phone and sign up ten in a day.
- Google Maps "nursery" and "plant shop" listings in every district town for phone numbers.
- The annual tree fair in Dhaka, where hundreds of nurseries sit at stalls for a month.
- Outreach angle: "Answer 'do you have it' in one link, and keep your customers' plants alive."
- The demo that closes: photograph twenty plants and put a live catalogue link in their Facebook bio within ten minutes.

### Pricing and the maths
- ৳299 to ৳999 per month, by stock items and messages.
- Costs are SMS or WhatsApp messages and photo storage, roughly ৳50 to ৳150 per nursery per month, so gross margin is around 80 percent.
- At the mid price of ৳649, roughly 460 paying nurseries make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, with nursery belts around Kolkata and Pune and a similar rooftop boom; Bengali and Hindi packs, UPI, an Indian species list and planting calendar.
- Then Pakistan (Urdu, JazzCash), Indonesia (Bahasa, tropical species list) and Kenya (Swahili, M-Pesa).
- What stays the same: stock, catalogue link, quotes and the care message engine; only species data and calendar change.

### Risks and how to de-risk them
- Risk: owners will not photograph and enter stock. De-risk: onboarding where you do the first twenty items for them in the shop.
- Risk: wrong care advice kills a plant. De-risk: every message is reviewed by the nursery before the template goes live.
- Risk: demand is seasonal. De-risk: yearly pricing with a discount and reorder prompts that bring buyers back.
- Risk: low price and many small customers. De-risk: work the nursery rows and fairs where dozens sign up in a day.


---

# Section 8: Manufacturing, Trade and Industry

Bangladesh makes, moves and trades a great deal of physical goods, and almost all of the small firms doing it still run on paper registers and phone calls. The eight ideas in this section put a ledger, a tracker and a compliance file into the hands of garment subcontractors, importers, kiln owners, jewellers, distributors, artisan groups, scrap dealers and tanneries.

## Idea 18: Small Garment Factory OS
*Order, line and payroll software for subcontract garment factories below the ERP price line.*

### Who pays and why now
Beside the big export factories, Bangladesh has thousands of small ones that take subcontract orders from larger factories and buying houses, say 20,000 basic tees in three weeks. They run 2 to 8 lines and 100 to 500 workers on paper registers and Excel.

They will pay for three reasons. They learn an order is late only when the buyer's QC visits. Payroll takes two people two days a month. And when a buyer's compliance team asks for wage and attendance registers, they cannot produce them, so the next order goes elsewhere. ERP software for large factories costs lakhs a year; nothing sits below that line. Buyers now push compliance down to subcontractors, and every supervisor has a smartphone. Ports: Vietnam, Cambodia, Indonesia, Pakistan, Ethiopia and Turkey.

### The product in 30 days (MVP)
- Order book: style, buyer, quantity, size and colour breakdown, ship date, price.
- Line output entry by the supervisor on a phone, hourly or end of day.
- Status board: planned versus actual output, days ahead or behind, per order.
- Worker register, attendance by card number, payroll run with daily wage, piece rate and overtime rules.
- CM cost per piece against the quoted price.
- Leave out: cutting-room planning, fabric inventory, accounting integration, biometric hardware.

### Data, integrations and the Bangladesh specifics
- Wage disbursement through the bKash or Nagad bulk payment API, printed slip as backup.
- Labour Act rules: overtime at double the basic hourly rate, weekly holiday, editable minimum wage grades.
- Compliance pack: attendance, wage and overtime registers in the layouts auditors expect, with Bangla numerals.
- Offline entry on the floor; the phone queues entries and syncs later.

### Build it with Claude
Stack: Next.js, PostgreSQL, Flutter Android for supervisors, Claude API for reports and Bangla copy, a small VPS, bKash merchant API.

1. Ask Claude for the data model.

```
Design a PostgreSQL schema for a small garment factory: buyer, order (style, quantity, size-colour breakdown as JSON, ship_date, unit_price), production_line, daily_output (line, order, date, hour, pieces), worker (card_no, grade, wage_type: daily|piece|monthly), attendance (in_time, out_time), payroll_run, payroll_line. Output a Prisma schema and the first migration.
```

2. Paste the schema and ask for the Flutter output-entry screen, offline first, with a SQLite queue and sync service.

3. Ask Claude to encode and test the payroll rules.

```
Write a TypeScript payroll module for Bangladesh garment workers. Inputs: grade, basic wage, monthly attendance, piece counts, overtime hours. Rules: overtime at 2x basic hourly rate (basic / 208), max 2 overtime hours a day, one paid weekly holiday. Output a wage sheet row per worker in Bangla and English, plus Jest tests for 5 edge cases.
```

4. Ask for the compliance pack generator (monthly PDF registers with the column headings auditors use) and an Excel import of the existing worker list.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 factories entering output daily, 1 payroll run completed |
| Day 60 | 8 factories live, 5 paying, first compliance pack shown to a buyer QC |
| Day 90 | 15 paying factories, roughly ৳1.2 lakh monthly revenue |

### First customers with zero budget
- Gather: Facebook groups for garment merchandisers and production managers, BGMEA and BKMEA directories, Google Maps "garments" in Ashulia, Gazipur, Narayanganj and Chattogram.
- Angle: "Your buyer will ask for wage and attendance registers. Print them in one click."
- Demo: enter one line's output for an hour on a tablet, then run payroll on last month's register.
- Referral loop: merchandisers refer subcontractors in return for a read-only buyer view; one free month per referred factory that pays.

### Pricing and the maths
- ৳4,999 a month for up to 3 lines; ৳9,999 for up to 8 lines; ৳19,999 for multi-unit factories with the buyer view.
- Cost of goods is hosting and SMS, under ৳300 per factory a month; gross margin above 90 percent.
- At a mid price of about ৳12,000, roughly 25 paying factories make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Vietnam, then Cambodia. Same buyers, same subcontract structure, same compliance push.
- What changes: language pack, payroll rules, payment rail, register formats. What stays: order book, line output, status board, costing.
- Sell through a local production consultant who already visits the factories.

### Risks and how to de-risk them
- Risk: owners fear digital wage records. De-risk: sell the status board first, keep payroll optional.
- Risk: a payroll error destroys trust. De-risk: run beside the manual sheet for two months; let the factory edit the rule table.
- Risk: supervisors stop entering data. De-risk: entry under 20 seconds and a visible line ranking.

## Idea 35: Import-Export Paperwork Assistant (working name Amdani)
*HS codes, landed cost and shipping documents for small importers and exporters, in Bangla.*

### Who pays and why now
Bangladesh has tens of thousands of small importers, from Chawkbazar traders to online sellers ordering from 1688, plus small exporters in handicraft and agro. They pay a C&F agent who guesses the HS code, and a wrong guess means penalties, demurrage at Chattogram port, or a shipment stuck for weeks.

They will pay because one mis-declared shipment costs more than a year of subscription; agents will pay because the Agent plan replaces the tariff book. NBR changes duties by SRO all year, and "duty on X" searches are large and unserved. Ports: Pakistan (FBR, WeBOC), Nigeria (Form M, PAAR), Indonesia (BTKI, PIB), Egypt (ACI).

### The product in 30 days (MVP)
- HS code finder: a product name in Bangla or English returns three likely 8-digit codes with duties.
- Landed cost calculator: CD, RD, SD, VAT, AIT and AT stacked from CIF value, in taka.
- Proforma invoice, commercial invoice, packing list and a document checklist as PDF from one form.
- Shipment tracker with a C&F agent task list.
- SRO alerts by WhatsApp when the duty on a saved HS code changes.
- Leave out: ASYCUDA filing, LC bank integration, freight quotes, bonded warehouse records.

### Data, integrations and the Bangladesh specifics
- The NBR annual Customs Tariff (PDF and Excel) parsed into a table, plus SRO notices, each row with a source date.
- bKash for subscriptions and documents; Stripe for customers abroad; WhatsApp for alerts and delivery.
- Documents stay in English for banks and customs; the interface uses Bangla and Bangla numerals.
- A "verified" flag and date on each product-to-HS mapping, set when a C&F agent confirms it.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for HS search, Cloudflare Pages and Workers, bKash merchant API.

1. Ask Claude for a script that loads the tariff Excel into PostgreSQL with a full-text index.

2. Build the HS finder as keyword retrieval plus Claude.

```
You are a Bangladesh customs classification assistant. Given a product description in Bangla or English and up to 20 candidate tariff rows from keyword search, return the 3 most likely 8-digit HS codes with code, English description, a one-line Bangla explanation, and why it fits. JSON only.
```

3. Ask Claude for the landed cost engine, then confirm the calculation order with a C&F agent.

```
Write a TypeScript function landedCost(cif, rates) for Bangladesh customs. AV = CIF plus 1 percent landing charge. CD and RD on AV; SD on AV + CD + RD; VAT and AT on AV + CD + RD + SD; AIT on AV. Return each component in taka and the total as a percent of CIF, with tests.
```

4. Ask for React PDF templates for the documents, and a programmatic "duty on [product]" page per popular product for search traffic.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 500 lookups, 50 free accounts, 10 verified HS mappings |
| Day 60 | 2,000 lookups a month, 30 paying traders, 1 agent |
| Day 90 | 5,000 lookups a month, 100 paying traders, 5 agents |

### First customers with zero budget
- Gather: Facebook groups for importers and 1688 buyers, Chawkbazar and Nawabpur market associations, C&F agent associations in Chattogram and Benapole, Google Maps "C&F agent".
- Angle: "Know the duty before you pay the supplier."
- Demo: calculate the landed cost of this month's shipment live on a phone, then generate the proforma invoice.
- Referral loop: agents send traders to the free tool for an Agent plan discount; five free lookups per referred friend.

### Pricing and the maths
- Free 5 lookups a month; Trader ৳499; Trader Pro ৳1,499; Agent ৳2,999 to ৳4,999; documents ৳99 to ৳299 each on the free plan.
- Each lookup costs a few taka in Claude calls, plus hosting; gross margin roughly 85 percent.
- At the Trader Pro price of ৳1,499, roughly 200 paying traders make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. A large import economy, the same SRO culture, and FBR publishes a comparable tariff.
- What changes: tariff table and stacking rules, document set, language pack, payment rail. What stays: finder, calculator, document generator, tracker.
- Reseller: a customs agent in each country who verifies mappings and sells the Agent plan.

### Risks and how to de-risk them
- Risk: a wrong HS code or duty figure. De-risk: show the source row and date, a plain disclaimer, agent verification for paid users.
- Risk: ASYCUDA is closed to third parties. De-risk: prepare, never file; the agent files with your PDF.
- Risk: search traffic takes months. De-risk: programmatic pages from day one and daily answers in importer groups.

## Idea 40: Brick Kiln and Construction Supplier Ledger
*Truck trips, buyer dues and driver settlements for kilns and sand and stone suppliers, on a phone.*

### Who pays and why now
Bangladesh has around 7,000 brick kilns and thousands of sand and stone suppliers. A kiln fires bricks from November to May, sells to contractors on credit and sends trucks out all day. The owner or the munshi keeps a khata of trips, challans, dues and driver advances, and at season end a few lakh taka can never be traced.

They will pay because one unrecorded truck trip is ৳10,000 or more of bricks, a contractor who disputes his balance can hold back lakhs, and drivers argue about advances every week. Environmental clearance and inspections now require records too, and the munshi already owns a smartphone. Ports: India, Pakistan, Nepal, Nigeria and Egypt have the same seasonal, credit-heavy trade.

### The product in 30 days (MVP)
- Buyer accounts with credit limit, running balance and payment history.
- Truck trip entry: truck, driver, buyer, product, quantity, rate, challan number, printed challan.
- Driver settlement: trips, fare due, fuel advances, weekly payout sheet.
- Daily production log by grade (first, second, third class, picket) and stock.
- Dues reminders by SMS with a bKash link, season dashboard, compliance file with renewal alerts.
- Leave out: coal purchase accounting, labour payroll, GPS truck tracking, multi-kiln groups.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad payment links on reminders; SMS through a local aggregator.
- Department of Environment clearance and district licence renewals as dated documents with alerts.
- Trade units: bricks in thousands (hajar), sand and stone in cft, cement in bags.
- Offline Android app for the kiln office, which often has weak signal; Bangla numerals on 58 mm thermal challans.

### Build it with Claude
Stack: Laravel admin, PostgreSQL, Flutter Android, Claude API for Bangla copy and summaries, a small VPS, bKash merchant API.

1. Ask Claude for the schema with the daily views.

```
Design a PostgreSQL schema for a brick kiln ledger: buyer (name, phone, credit_limit), product (grade or material, unit: pcs|cft|bag), truck, driver, trip (date, truck, driver, buyer, product, quantity, rate, challan_no, fare, fuel_advance), payment (buyer, amount, method), production_log (date, grade, quantity), compliance_doc (type, issue_date, expiry_date, file_url). Add views for buyer balance and driver weekly settlement.
```

2. Ask for the Flutter trip entry and challan print screen, ESC/POS over Bluetooth, Bangla rendered as a bitmap.

3. Ask Claude for the reminder copy.

```
Write 4 short Bangla SMS templates (under 160 characters) for a brick kiln reminding a contractor about unpaid dues, respectful tone using আপনি. Variables: {name}, {amount}, {days}, {kiln_name}, {bkash_link}. One gentle reminder, one for 30 days overdue, one thank-you after payment, one season-end settlement. Return JSON.
```

4. Ask for a khata import (photograph a ledger page, extract rows for review) and a monthly Bangla owner summary by WhatsApp.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 kilns live, 200 trips logged, first SMS reminders sent |
| Day 60 | 10 kilns live, 6 paying, 1 sand supplier onboarded |
| Day 90 | 20 paying customers, roughly ৳1.8 lakh monthly revenue |

### First customers with zero budget
- Gather: the brick manufacturers' owners association, kiln clusters in Savar, Dhamrai, Gazipur and Narayanganj, sand ghats at Amin Bazar and Gabtoli, Google Maps "ইট ভাটা".
- Angle: "Every truck and every taka owed, on your phone, tonight."
- Demo: sit with the munshi, enter yesterday's trips from his khata, then show the owner the dues list on his phone.
- Referral loop: a season discount per referred kiln; in the off months sell to sand and stone suppliers.

### Pricing and the maths
- ৳4,999 a month for one kiln with 2 users; ৳9,999 with trucks, drivers and an SMS bundle; ৳14,999 for multi-site kilns.
- SMS at under ৳0.50 a message plus hosting, well under ৳500 a customer; gross margin around 90 percent.
- At a mid price of ৳9,999, roughly 30 paying customers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, starting with West Bengal and Bihar kilns. Same season, same credit trade, and Bangla already works.
- What changes: Hindi pack, UPI payment links, state pollution board documents. What stays: trip ledger, driver settlement, dues reminders.
- Reseller: a kiln equipment or coal supplier who visits every kiln in a district.

### Risks and how to de-risk them
- Risk: seasonal churn from June to October. De-risk: an annual price with a paused off-season, plus year-round suppliers.
- Risk: kilns close under environmental enforcement. De-risk: keep the product generic for construction suppliers and lead with the compliance file.
- Risk: the munshi resists and owners distrust cash data on a server. De-risk: khata-identical field names, an owner-only PIN, export any time.

## Idea 45: Jewellery Shop OS
*Daily gold rate, karat calculator, repair tickets and bKash gold savings schemes for jewellers.*

### Who pays and why now
Thousands of jewellery shops, from Tanti Bazar in Dhaka to the sonapatti of every district town, run gold savings schemes: a customer pays a fixed amount every month and collects gold after a year, all on a paper card. The daily rate changes often, every estimate is worked out by hand, and repairs go into a drawer with a slip.

They will pay because scheme disputes lose customers, a missed instalment is a missed sale, and a wrong rate on a busy day costs real gold. The jewellers' association is pushing hallmarking and proper receipts, and every scheme customer already has bKash. Ports: India, Pakistan, Indonesia, Nigeria, Egypt and Gulf diaspora shops.

### The product in 30 days (MVP)
- Daily gold and silver rate by karat, with history and a display page for a shop screen.
- Price calculator: weight in bhori or grams, karat, making charge, VAT, printable estimate.
- Sale invoice and item stock by tag number, with hallmark number and purity.
- Savings scheme: plan, monthly instalment by bKash or cash, SMS receipt, maturity at current rate.
- Order and repair tickets with a photo, promised date and an SMS when ready.
- Leave out: full accounting, old gold exchange valuation, online catalogue, multi-branch.

### Data, integrations and the Bangladesh specifics
- The association's daily rate is a notice, not an API; the shop enters it and attaches the screenshot.
- bKash payment links for instalments, transaction ID stored against the account; Nagad as a second rail.
- SMS gateway for receipts and reminders in Bangla with Bangla numerals.
- Bhori conversion (1 bhori is 11.664 grams, 16 ana to a bhori) and 5 percent VAT on the invoice.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for Bangla SMS and reading old scheme cards, Cloudflare, bKash merchant API.

1. Ask Claude for the schema with the scheme ledger at the centre.

```
Design a PostgreSQL schema for a jewellery shop: rate (date, metal, karat, price_per_gram), item (tag_no, metal, karat, gross_weight_g, stone_weight_g, making_charge, hallmark_no), sale, sale_line, customer, scheme_plan (monthly_amount, months, bonus_rule), scheme_account (customer, plan, start_date, status), scheme_payment (account, date, amount, method, bkash_trx_id), repair_ticket. Add a scheme balance view.
```

2. Ask for the calculator screen with bhori, ana and roti inputs and a printed estimate in Bangla.

3. Ask Claude for the scheme messages.

```
Write Bangla SMS templates for a jewellery shop's gold savings scheme, under 160 characters each, variables {name}, {shop}, {amount}, {month_no}, {total_months}, {paid_total}, {bkash_link}: (1) instalment due in 3 days, (2) payment received with running total, (3) 7 days overdue, (4) scheme matured, please visit. Respectful আপনি tone. Return JSON.
```

4. Ask for a card digitiser (photograph an old scheme card, extract payment rows for review) and a full-screen rate display page.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 shops, 100 scheme accounts digitised, SMS receipts live |
| Day 60 | 10 shops live, 6 paying, 1,000 scheme SMS sent |
| Day 90 | 30 paying shops, roughly ৳1 lakh monthly revenue |

### First customers with zero budget
- Gather: the jewellers' association district committees, Tanti Bazar and Baitul Mukarram gold markets, Facebook groups for jewellers, Google Maps "jewellery shop".
- Angle: "Every scheme customer gets an SMS receipt. No more disputes."
- Demo: digitise 10 scheme cards and send the receipts while the owner watches; do the first month's data entry for early shops.
- Referral loop: every SMS carries the shop's name, and shops in one market copy each other within weeks.

### Pricing and the maths
- ৳1,499 a month for calculator, invoices and tickets; ৳2,999 adds the scheme ledger with SMS for up to 300 accounts; ৳4,999 for unlimited accounts and the display page.
- SMS is the main cost, around ৳100 to ৳300 a shop a month; gross margin around 85 percent.
- At the mid price of ৳2,999, roughly 100 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India. Gold schemes are everywhere, hallmarking is mandatory, and West Bengal shops already read Bangla.
- What changes: tola units, GST invoice, BIS hallmark fields, UPI links, Hindi pack. What stays: calculator, scheme ledger, tickets, SMS logic.
- Reseller: a hallmarking centre or gold refiner that serves many shops.

### Risks and how to de-risk them
- Risk: shops fear customer data on a server. De-risk: encrypt at rest, owner-only export, never sell data.
- Risk: savings schemes sit in a regulatory grey zone. De-risk: the shop stays the party; you only keep records, transparent to the customer.
- Risk: a wrong rate entry. De-risk: require a second confirmation and show the attached notice on the display page.

## Idea 57: Distributor Route Sales App
*Order taking, van stock, invoices and dues collection for FMCG sales reps, in Bangla.*

### Who pays and why now
Tens of thousands of FMCG distributors, one set in every upazila, send sales reps out each morning with an order book. The rep visits 30 to 50 shops, the van delivers the next day, dues are collected on the next visit, and at night someone types the books into Excel.

They will pay because the leaks are in the field: fake orders, skimmed collections, forgotten schemes. Brand companies give some distributors an app, but it covers one company and most carry several. This is a contested market, so sell it as an add-on to an accounting or payroll product. Every rep has an Android phone, and companies now demand daily secondary sales data. Ports: India, Pakistan, Nigeria, Kenya, Indonesia and Egypt.

### The product in 30 days (MVP)
- Retailer list per route with GPS pin, phone and outstanding balance.
- Offline order taking: catalogue by company, pack size, price and active scheme.
- Van stock: morning load out, sales, returns, evening load in.
- Invoice print from a Bluetooth thermal printer in Bangla, and dues collection with an SMS receipt.
- Scheme rules and an owner's evening summary: orders, collections, retailers not visited, top rep.
- Leave out: company DMS integration, route optimisation, incentives, warehouse module.

### Data, integrations and the Bangladesh specifics
- bKash merchant payments from retailers recorded against the balance; cash stays the default; SMS receipts through a local aggregator.
- Company catalogues arrive as Excel from the territory officer; import with column mapping.
- Offline first, since rural bazaars have patchy data; the server is authoritative on dues.
- Bangla numerals on invoices; a CSV export in the company's secondary sales format.

### Build it with Claude
Stack: Flutter Android for reps, Laravel admin, PostgreSQL, Claude API for catalogue import and summaries, a small VPS, bKash merchant API.

1. Ask Claude for the schema: retailer, route, product, scheme, order, van_load, collection, plus a daily summary view per rep.

2. Ask Claude for the order screen.

```
Build a Flutter order screen for a sales rep at a retail shop, offline-first with Drift (SQLite). Search products by Bangla or English name; show pack size, price and active scheme; large quantity stepper; running total; save as pending_sync; a sync service that pushes to REST endpoints when online. Bangla labels.
```

3. Ask Claude for the scheme rules engine.

```
Write a TypeScript rules engine for FMCG trade schemes. Rule types: free goods (buy N get M of the same or another SKU), slab percent discount by invoice value, fixed discount per case, valid date range, retailer type eligibility. Input: order lines, retailer type, date. Output: applied schemes and discount lines. Include 6 unit tests and an editable JSON rule format.
```

4. Ask for ESC/POS invoice printing with Bangla rendered as a bitmap, and the owner's 6 pm WhatsApp summary in Bangla.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 distributors, 10 reps live, 500 orders taken |
| Day 60 | 8 distributors, 60 paying rep seats |
| Day 90 | 25 distributors, 250 paying rep seats, roughly ৳75,000 monthly revenue |

### First customers with zero budget
- Gather: distributor associations, company territory sales officers, Facebook groups for FMCG sales professionals, Google Maps "distributor" in upazila towns.
- Angle: "At 6 pm, know exactly what each rep sold and collected."
- Demo: load one route from the order book, ride with a rep for a morning, show the owner the summary at lunch.
- Referral loop: territory officers refer distributors because they get the data they want; reps carry the app when they move.

### Pricing and the maths
- ৳199 per rep per month for orders, dues and printing; ৳399 per rep adds schemes, van stock and exports; 8 reps cost ৳1,592 to ৳3,192.
- SMS per invoice and hosting are the costs; gross margin around 80 percent.
- At the mid price of ৳299, roughly 1,000 paying rep seats make ৳3 lakh a month, e.g. 100 distributors with 10 reps.

### Country kit: taking it to other languages
- First port: Kenya. Same routes, M-Pesa collections fit the dues flow, and the English interface needs little change.
- What changes: payment rail, catalogue import, tax receipts, later a Swahili pack. What stays: rep app, rules engine, van stock, owner summary.
- Reseller: a local accounting software vendor who already serves distributors.

### Risks and how to de-risk them
- Risk: many DMS vendors and company apps. De-risk: sell only to multi-company distributors and bundle with accounting.
- Risk: reps resist because they lose informal income. De-risk: the owner sponsors it, and the app must be faster than the book.
- Risk: offline sync conflicts on dues. De-risk: server-authoritative balances and sequence numbers on every collection.

## Idea 63: Artisan Producer Group OS
*Piece-rate work orders, QC photos, bKash payments and fair-trade records for groups of home workers.*

### Who pays and why now
Hundreds of producer groups in Bangladesh, NGO-run and private, supply handicraft, jute and clothing to exporters and fair-trade buyers in Europe and Japan. Each coordinates hundreds or thousands of home-based workers, mostly women, on piece rates. Materials go out to villages, pieces come back and are checked by eye, and payments are cash against a signature.

They will pay because buyers now demand proof: worker payment records, rates, and traceability from order to worker. A group that cannot show them loses the buyer, and NGO donors want the same numbers. European due diligence rules push traceability down the chain, and bKash makes recorded payment to a village worker possible. Ports: India, Nepal, Indonesia, Kenya and Guatemala.

### The product in 30 days (MVP)
- Worker register: name, village, skills, bKash number, ID photo, consent.
- Work orders: buyer, product, quantity, piece rate, deadline, split into batches.
- Material issue and piece collection per batch, and QC with photo and pass, fail or rework.
- Piece-rate payment calculation with bKash bulk disbursement and a payment record.
- Buyer progress view by share link, and a fair-trade audit export.
- Leave out: design catalogue, export documents, inventory accounting, e-commerce.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad bulk disbursement APIs for worker payments, transaction ID stored per payment.
- Bangla SMS to the worker on payment; WhatsApp for field coordinators.
- Offline Flutter app for village coordinators, with compressed photos for slow networks.
- Fair-trade principles as checklist fields; Bangla numerals on slips, English in the audit export.

### Build it with Claude
Stack: Next.js admin, PostgreSQL, Flutter Android for coordinators, Claude API for audit narratives, Cloudflare, bKash bulk disbursement API.

1. Ask Claude for the schema.

```
Design a PostgreSQL schema for an artisan producer group: worker (name, village, skills[], mobile_money_no, consent_at), centre, buyer, work_order (buyer, product, quantity, piece_rate, deadline), batch (work_order, centre or worker, qty_issued, qty_received, status), qc_check (batch, result: pass|fail|rework, photo_url), payment (worker, batch, pieces, rate, amount, method, trx_id, paid_at), complaint. Add views for worker earnings and order progress.
```

2. Ask for the Flutter QC screen: batch lookup, photo capture, pass or fail or rework, offline queue.

3. Ask Claude for the audit summary generator.

```
Prepare a fair-trade audit summary for a handicraft producer group in Bangladesh. From the JSON I provide (workers, orders, payments, QC results, complaints for one quarter), write a one-page English summary: active workers by gender and village, pieces produced, average and minimum piece rate, days from QC pass to payment, rework rate, complaints. Flag any worker paid below the declared minimum.
```

4. Ask for the bKash bulk payment flow (approve, call the API, store results, retry failures, send SMS) and a read-only buyer page.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 groups, 300 workers registered, 10 batches through QC |
| Day 60 | 6 groups live, 4 paying, first bKash bulk payment run |
| Day 90 | 15 paying organisations, roughly ৳45,000 monthly revenue |

### First customers with zero budget
- Gather: the fair-trade forum in Bangladesh and its member groups, NGO handicraft programmes, jute product exporters, Google Maps "handicraft exporter" in Dhaka, Kushtia and Rangpur.
- Angle: "Show your buyer every worker's payment in one report."
- Demo: enter one work order and batch, run QC, pay a worker by bKash, hand over the audit summary.
- Referral loop: sell to the exporter, who then requires it from every supplying group; certifiers recommend it during audits.

### Pricing and the maths
- ৳999 a month for a group with up to 100 workers; ৳2,499 for up to 500 workers with bKash payments; ৳4,999 for an exporter with several groups and audit exports.
- The group pays bKash disbursement fees; your costs are SMS and hosting; gross margin around 85 percent.
- At a mid price of ৳2,999, roughly 100 paying organisations make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India's West Bengal and Rajasthan handicraft clusters, then Nepal where fair-trade groups are strong.
- What changes: language pack, UPI or eSewa rail, ID types, audit checklist. What stays: work orders, batches, QC, payments, buyer view.
- Reseller: a fair-trade network or export consultant who already audits the groups.

### Risks and how to de-risk them
- Risk: workers without a phone or bKash. De-risk: allow cash with a photo of the signature, or pay via a coordinator's account.
- Risk: NGO procurement is slow and the ticket per group is low. De-risk: sell to private exporters first; NGOs follow their buyers.
- Risk: workers' personal data is sensitive. De-risk: consent screen, minimal fields, export controls per role.

## Idea 67: Scrap Dealer Ledger
*Buying by weight, collector accounts, stock by material and a shareable Bangla price board for bhangari shops.*

### Who pays and why now
Tens of thousands of bhangari shops buy plastic, iron, copper, paper and glass from collectors every day, by weight, in cash, and sell in bulk to recyclers. Prices move daily. The owner keeps a khata if anything, the price board is chalk on a wall, and nobody knows what sits in the back.

They will pay because the margin is thin and the leaks are many: a collector disputes yesterday's rate, a recycler's due is forgotten, stock walks out. A ledger that records every purchase in ten seconds saves more than ৳299 a month. Every dealer has a phone, and voice input in Bangla finally works. Ports: India's kabadiwala trade, Pakistan, Nigeria, Indonesia and Egypt.

### The product in 30 days (MVP)
- Purchase entry: collector, material, weight, rate, cash paid, with an SMS or printed slip.
- Voice entry in Bangla: say the material, weight and rate, confirm, done.
- Daily price board in Bangla, editable and shareable as an image.
- Collector accounts with advances and balance; stock by material; sales to recyclers with dues.
- Worker payments and a daily cash summary.
- Leave out: Bluetooth scale integration, multi-shop, marketplace, pickup scheduling.

### Data, integrations and the Bangladesh specifics
- bKash for recycler payments and collector payouts; cash remains the default.
- SMS slips through a local aggregator, optional, since SMS is the main cost.
- Material names in Bangla (লোহা, তামা, প্লাস্টিক, কাগজ) and Bangla numerals throughout; offline first.
- Store rates with city and date; anonymous city price data becomes an index later.

### Build it with Claude
Stack: Flutter Android, a small Laravel backend with PostgreSQL, Claude API for Bangla voice parsing, Cloudflare, bKash merchant API.

1. Ask Claude for the schema and offline model: collector, material, purchase, sale, recycler, worker_payment, price, stock view.

2. Ask Claude for the voice parser; the phone's speech-to-text supplies the text.

```
Parse a Bangla or Banglish spoken phrase from a scrap dealer into a JSON purchase entry. Examples: "লোহা বারো কেজি পঁয়ত্রিশ টাকা", "plastic 8 kg 20 taka". Output: {material, weight_kg, rate_per_kg, amount}. Materials: iron, copper, aluminium, brass, hard plastic, soft plastic, paper, glass, e-waste. If the rate is missing, use today's price board passed as JSON. If unsure, ask a short question in Bangla.
```

3. Ask Claude for the shareable price board.

```
Create a Flutter widget that renders today's scrap price board as a 1080x1350 image for WhatsApp: shop name, date in Bangla, a table of materials and rate per kg in Bangla numerals, large fonts, shop phone number at the bottom, Noto Sans Bengali. Add a share button that exports the PNG.
```

4. Ask for the collector slip (58 mm print and SMS) and the daily summary screen: bought, sold, cash, stock change.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 shops, 1,000 purchase entries, 50 price boards shared |
| Day 60 | 40 shops live, 20 paying |
| Day 90 | 100 paying shops, roughly ৳50,000 monthly revenue |

### First customers with zero budget
- Gather: the scrap clusters at Dholaikhal, Islambagh and Kamrangirchar in Dhaka and in Chattogram, Facebook groups on ভাঙ্গারি business, plastic recycler associations, Google Maps "ভাঙ্গারি দোকান".
- Angle: "Your daily price board on WhatsApp, and every kilo written down."
- Demo: enter today's purchases by voice in five minutes, then share the price board to the owner's WhatsApp.
- Referral loop: the shared board carries the app's name, collectors who see the SMS slip ask other shops for it, and recyclers recommend it.

### Pricing and the maths
- ৳299 a month for purchases and the price board; ৳599 adds collector accounts, recycler sales and SMS slips; ৳999 for multi-user, worker payments and reports.
- SMS is the only real cost, so keep it optional; gross margin around 80 percent.
- At a mid price of about ৳650, roughly 460 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India. The kabadiwala trade is huge, Bangla works in West Bengal, and Hindi covers the north.
- What changes: language and material names, UPI payments. What stays: the app, the voice parser, the price board, the ledger.
- Reseller: recycler aggregators who already collect from hundreds of shops.

### Risks and how to de-risk them
- Risk: a very low price with a support-heavy customer. De-risk: self-serve videos and a WhatsApp community, no phone support.
- Risk: a cash-only culture rejects digital payments. De-risk: never force payments; the product is records.
- Risk: churn after the first month, and Indian apps porting in. De-risk: the daily price board habit, Bangla voice, and speed.

## Idea 103: Small Leather Unit Management
*Hide lots, processing batches, chemical costs and compliance records for small tanneries and leather goods units.*

### Who pays and why now
Around the Savar tannery estate and the Bhairab footwear cluster, hundreds of small units buy raw hides by grade and weight, process them in batches and sell wet blue, crust and finished leather to exporters and shoe factories. Most hides arrive in the week after Eid-ul-Azha. Nobody tracks a batch from hide lot to finished leather, and chemical use, the largest controllable cost, is judged by eye.

They will pay because buyers now walk away without traceability. Auditors ask which lot went into which batch, which chemicals were used, and where effluent went. A unit that cannot answer loses the order, and a batch overdosed by 20 percent burns tens of thousands of taka. European traceability demands and estate compliance drives land at once. Ports: Pakistan, Ethiopia, India, Nigeria and Vietnam.

### The product in 30 days (MVP)
- Hide purchase: supplier, count, grade, weight, rate, season lot.
- Batch tracking: number, hide lot, stage, dates, output.
- Chemical usage and cost per batch from a store ledger.
- Finished stock by type and grade; buyer orders and dispatch with batch references and a traceability sheet.
- Compliance file: effluent logs, treatment plant invoices, licences, with renewal alerts.
- Leave out: full accounting, audit self-assessment, machine maintenance, export documents.

### Data, integrations and the Bangladesh specifics
- bKash and bank payments to hide traders; SMS to buyers on dispatch.
- Department of Environment and effluent treatment plant records as dated documents, tagged by audit category.
- Units: pieces, kilograms and square feet; Bangla numerals on floor screens, English on buyer sheets.
- Offline entry on the wet floor, synced later.

### Build it with Claude
Stack: Laravel admin, PostgreSQL, Flutter Android for floor entry, Claude API for anomaly notes, a small VPS, bKash merchant API.

1. Ask Claude for the schema.

```
Design a PostgreSQL schema for a small tannery: supplier, hide_lot (supplier, date, count, grade A|B|C|D, total_weight_kg, rate, season), batch (batch_no, hide_lot, stage: soaking|liming|tanning|wet_blue|crust|finished, start_date, end_date, output_qty), chemical, chemical_use (batch, chemical, qty, unit_cost), finished_stock (type, grade, sqft), buyer_order, dispatch (order, batch_refs[], qty), compliance_record (category, date, file_url, expiry_date). Add a batch cost view.
```

2. Ask for the Flutter batch screen: pick a batch, move it to the next stage, enter chemicals used, photograph the drum card.

3. Ask Claude for the chemical anomaly note.

```
Given this JSON of chemical usage per batch for the last 90 days (batch_no, total_weight_kg, chemical, qty, unit_cost), compute per-kg dosage of each chemical per batch and flag batches more than 20 percent above the median. Write a short Bangla note for the owner listing flagged batches, the likely overuse cost in taka, and one question for the foreman on each.
```

4. Ask for the compliance file (upload, categorise, SMS expiry alerts) and the traceability sheet PDF per dispatch.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 units live, 20 batches tracked |
| Day 60 | 6 units live, 4 paying, first traceability sheet sent to a buyer |
| Day 90 | 15 paying units, roughly ৳1.5 lakh monthly revenue |

### First customers with zero budget
- Gather: the tanners' and leather goods exporter associations, the Hemayetpur estate where you can walk gate to gate, the Bhairab footwear cluster, LinkedIn groups for leather professionals.
- Angle: "Batch records your buyer's auditor can read."
- Demo: track one batch from hide lot to wet blue with chemical costs and print the traceability sheet; enter the Eid hide lots for the first five units.
- Referral loop: buyers and audit consultants recommend it to units they want to keep; chemical suppliers introduce their customers.

### Pricing and the maths
- ৳4,999 a month for one unit with batches and stock; ৳9,999 adds chemical costing, compliance file and buyer orders; ৳14,999 for several units with audit exports.
- Costs are hosting and a little SMS; gross margin around 90 percent.
- At the mid price of ৳9,999, roughly 30 paying units make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Sialkot, Kasur and Karachi have hundreds of small tanneries under the same pressure.
- What changes: Urdu pack, JazzCash or Easypaisa, provincial environment bodies. What stays: batch model, chemical costing, compliance file, traceability sheet.
- Second port: Ethiopia's leather industry parks, via park management.

### Risks and how to de-risk them
- Risk: few customers and a long sales cycle. De-risk: a high ticket, founder-led selling, weekly walks of the estate.
- Risk: units avoid records that expose gaps. De-risk: owner-controlled sharing and a private mode.
- Risk: domain complexity and the Eid peak. De-risk: a retired foreman as paid adviser, and bulk hide lot import from Excel before Eid.


---

# Section 9: Property and Construction

Property is where much of Bangladesh's informal money sits: rent, instalments, service charges and construction cash all move through notebooks and personal bKash numbers. The nine businesses in this section turn those notebooks into subscriptions, from a ৳199 landlord app to a dollar-priced caretaker platform for the diaspora.

## Idea 13: Landlord App
*Rent via bKash, tenant records, police tenant forms, utility splits and Bangla notices for landlords with 3 to 30 units.*

### Who pays and why now
Urban landlords in Dhaka, Chattogram, Sylhet and every district town own a building with 3 to 30 flats. They collect rent in cash or by bKash to a personal number, track it in a notebook, split utility bills by hand and fill the police tenant form on paper, if at all.

They will pay because late rent and disputes cost far more than ৳199 a month. A landlord with ten flats can lose a month's rent a year to forgotten payments and arguments over who paid. Tenants already have bKash, and city police now ask for tenant records.

Port countries are India, Pakistan, Nigeria, Egypt and Indonesia, where the small landlord is just as informal.

### The product in 30 days (MVP)
- Buildings and units with tenant name, phone, NID, move-in date and rent.
- Monthly rent due, bKash payment link by SMS, automatic receipt on payment.
- Cash payment entry with a photo of the receipt.
- Utility split: enter the shared electricity, gas or water bill and split by unit or by rule.
- Police tenant information form as a PDF from the tenant record.
- Bangla notices (rent increase, repair, water off) by SMS or WhatsApp.
- Leave out: tenant applications, maintenance tickets, accounting exports, multi-owner roles.

### Data, integrations and the Bangladesh specifics
- bKash merchant API (Checkout URL) for rent links; Nagad second. Landlords without a merchant account start with manual entry.
- Local SMS gateway for reminders and receipts; WhatsApp for notices.
- The Dhaka Metropolitan Police tenant form fields (NID, permanent address, previous address, family members, emergency contact) become your tenant schema.
- Bangla numerals and month names on receipts; a responsive web app, no native app in month one.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for Bangla notices, Cloudflare hosting, bKash merchant API, local SMS gateway.

1. Ask Claude for the data model. Paste:
```
Design a PostgreSQL schema for a Bangladeshi landlord app: owners, buildings, units, tenants
(with NID, permanent address, emergency contact for the police tenant form), monthly rent
invoices, payments (bKash transaction id or cash with photo), shared utility bills split
across units, and notices. Add indexes and a query for "all unpaid rent this month".
```
Review it, then ask Claude for the migrations and Next.js API routes.
2. Ask Claude for three screens: building dashboard (paid, unpaid, partial), unit page, and a tenant form that mirrors the police form, with Bangla labels.
3. Ask Claude for the bKash Checkout integration with a webhook that marks the invoice paid and sends an SMS receipt. Test in the sandbox first.
4. Ask Claude for the notice generator. Paste:
```
Write a function that takes a notice type (rent_increase, repair, water_off, general), the
details and the building name, and returns a polite Bangla SMS under 300 characters in the
register a Dhaka landlord uses with tenants. Give 3 samples per type so I can check the tone.
```
Read the samples to a landlord before shipping, then ask Claude for the police form PDF with an embedded Bangla font.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 landlords, 60 units, first bKash rent collected |
| Day 60 | 50 landlords, 300 units, 20 paying |
| Day 90 | 150 landlords, 60 paying, roughly ৳25,000 monthly revenue |

### First customers with zero budget
- Facebook groups: "Dhaka Flat Rent", "To-Let Dhaka", and area groups for Mirpur, Uttara, Mohammadpur and Bashundhara, where landlords post to-let ads weekly.
- Building caretakers and to-let agents know every landlord on their street; pay ৳100 per landlord signed.
- Message: "Your tenants already use bKash. Get rent on the 5th without calling anyone, and the police form in one tap."
- Demo that closes: load their building on your phone in five minutes and send one real rent link to one tenant.
- Referral loop: every SMS receipt carries the app name; tenants whose parents are landlords arrive on their own.

### Pricing and the maths
- Basic ৳199/month up to 5 units; Standard ৳399/month up to 15 units; Plus ৳599/month up to 30 units.
- Costs are SMS (roughly ৳0.30 to ৳0.50 each) and hosting; AI use is tiny. Gross margin above 85 percent.
- At the mid price of ৳399, roughly 750 paying landlords make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. The same informal landlord, JazzCash and Easypaisa for rent, and a police tenant registration rule in Punjab that mirrors Dhaka's.
- What changes: language pack, payment rail, tenant form fields per city, SMS gateway.
- What stays: units, invoices, utility split, notice generator, the whole codebase. Sell through property agents as resellers.

### Risks and how to de-risk them
- Risk: landlords keep collecting cash and ignore the bKash link. De-risk: one-tap cash entry with photo; sell record-keeping and the police form first.
- Risk: bKash merchant onboarding is slow for individuals. De-risk: start with personal-number payments recorded manually, add the merchant API later.
- Risk: a low price needs high volume. De-risk: push the ৳599 plan to small property managers.
- Risk: tenants see the app as surveillance. De-risk: receipts only, no tenant login in the MVP.

## Idea 20: Small Contractor Job Costing
*Material purchases by photo, daily labour attendance, client bills and stage-wise payments, all in Bangla, for small construction contractors.*

### Who pays and why now
The customer is the small contractor (ঠিকাদার) who builds a house, a shop floor or a boundary wall for a private client. He buys cement, rod and sand on credit from three suppliers, pays 8 to 40 labourers daily in cash, and bills the client in stages, all tracked in a pocket notebook or his head. At the end he often cannot say whether he made money.

He will pay because the leakage is large: a missing bag of cement a day, a labourer counted twice, a supplier bill paid twice, and the profit on a ৳20 lakh job is gone. Suppliers already hand over memos he photographs, so the raw data lives on his phone.

Port countries are India, Pakistan, Nigeria, Indonesia and Egypt, where informal construction is just as large.

### The product in 30 days (MVP)
- Projects with client, site, contract value and payment stages.
- Material purchase by photo of the supplier memo; Claude reads items, the contractor confirms.
- Daily labour attendance by role (mason, helper, rod worker) with day rate and running wage total.
- Supplier ledger: purchases, payments, balance per supplier.
- Client bill per stage in Bangla with a bKash payment link.
- Project profit view: contract value minus materials, labour and other costs, updated daily.
- Leave out: BOQ estimation, drawings, multi-user roles, stock across sites.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for stage payments from clients; Nagad second. Supplier payments are recorded, not processed.
- Claude vision on memo photos; memos are handwritten Bangla or mixed, so keep a confirm step.
- Default units (bag, CFT, ton, piece, feet) and labour roles with typical Dhaka day rates the contractor can edit.
- Offline entry on site; Bangla numerals on bills with stage names like "ছাদ ঢালাই".

### Build it with Claude
Stack: Flutter Android app, Laravel API with PostgreSQL, Claude API for memo reading and bill text, small VPS, bKash merchant API.

1. Ask Claude for the Laravel migrations: projects, stages, purchases, purchase_items, labour_days, suppliers, supplier_payments, client_bills, plus the profit query.
2. Build the memo reader. Paste:
```
I am sending a photo of a handwritten Bangladeshi construction supplier memo (cement, rod,
sand, bricks). Extract a JSON list of items with name in Bangla and English, quantity, unit
(bag, CFT, ton, piece), unit price in taka and line total, plus supplier name and date.
If a value is unreadable return null and add "needs_check": true.
```
Wire it into a Laravel job and show the JSON as an editable form.
3. Ask Claude for the Flutter attendance screen: roles, plus and minus counters, day rate, a big Bangla total, offline with a local SQLite queue.
4. Generate the client bill. Paste:
```
Write a Bangla client bill template for a small construction contractor. Inputs: client name,
project, stage name, stage amount, received so far, amount due, bKash link. Formal but simple
Bangla, Bangla numerals, one A4 page as HTML for PDF export.
```
Print one and check it with a contractor, then ask Claude for a weekly Bangla SMS summary: spent, paid, client balance, top supplier owed.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 8 contractors, 12 live projects, 200 memos read |
| Day 60 | 40 contractors, 15 paying |
| Day 90 | 120 contractors, 50 paying, roughly ৳40,000 monthly revenue |

### First customers with zero budget
- Cement and rod dealers know every contractor; leave a printed card at the counter and pay ৳200 per referral.
- Facebook groups: "Civil Engineers Bangladesh", "Construction Contractor BD" and district builder groups where site supervisors are active.
- Message: "Know your profit on every job before it ends. Photograph the memo, we do the rest."
- Demo that closes: photograph one of their real memos and show the line items appear.
- Referral loop: every client bill carries a "Made with" line; clients who build again ask their contractor for it.

### Pricing and the maths
- Solo ৳499/month for 2 active projects; Team ৳999/month for 6 projects; Firm ৳1,499/month for unlimited projects and a second login.
- Costs are Claude vision (a few taka per memo), SMS and a VPS; gross margin around 80 percent.
- At the mid price of ৳999, roughly 300 paying contractors make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. The same thekedar model, JazzCash for stage payments, Urdu memos that Claude reads well.
- What changes: language pack, payment rail, units and default day rates, SMS gateway.
- What stays: memo reader, attendance, supplier ledger, profit view. Building material dealers in Lahore and Karachi as resellers.

### Risks and how to de-risk them
- Risk: memo reading errors erode trust. De-risk: always confirm, flag low-confidence values, learn supplier item names over time.
- Risk: contractors fear records clients or tax officers could see. De-risk: data is private; client bills show only stage totals.
- Risk: churn between jobs. De-risk: annual billing with a discount; supplier ledgers stay useful between projects.
- Risk: generic expense apps. De-risk: stage bills, labour roles and memo photos are construction-specific and are the wedge.

## Idea 29: Real Estate Developer and Agent CRM
*Flat and plot booking, instalment schedules with bKash reminders, buyer follow-up, land document checklists and handover tracking for developers and brokers.*

### Who pays and why now
The customer is a small or mid-size developer in Dhaka, Chattogram or Purbachal with two to ten projects, and the brokers who sell for them. Flats and plots go on 24 to 60 monthly instalments. Hundreds of buyers sit in Excel sheets kept by one accountant, reminders go out by phone, and late instalments surface weeks later.

They pay well because the money is large. A developer with 300 buyers on ৳25,000 instalments moves ৳75 lakh a month; a one percent drop in on-time payment is ৳75,000. Buyers now pay by bKash and bank transfer and expect SMS confirmation, and developers must document land title and hand over on time.

Port countries are India, Pakistan, Nigeria, Egypt and Indonesia, where instalment-based property sales are the norm.

### The product in 30 days (MVP)
- Project, building, floor and unit inventory: available, booked, sold, handed over.
- Buyer record with co-buyer, nominee, NID and a generated instalment schedule.
- Due list with Bangla SMS reminders three days before and on the day, with a bKash link for smaller amounts.
- Payment entry (bKash, bank, cheque) with receipt PDF and a running buyer statement.
- Broker lead pipeline: enquiry, site visit, negotiation, booked, with follow-up reminders.
- Land document checklist per project: deed, mutation, khatian, RAJUK approval, with uploads.
- Leave out: construction progress, accounting, buyer portal, commission calculations.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for instalments under the wallet limit; bank transfers recorded with a reference; SSLCommerz for cards if asked.
- SMS gateway for reminders and receipts; WhatsApp for statements.
- Default land checklist from RAJUK and CDA approval steps and the title chain (CS, SA, RS, BS khatian, mutation, DCR).
- Bangla numerals and dates on receipts; a Bangla and English toggle, since offices work in English sheets and talk to buyers in Bangla.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for statements and reminder text, Cloudflare hosting, bKash merchant API, SMS gateway.

1. Ask Claude for the schema. Paste:
```
Design a PostgreSQL schema for a Bangladeshi real estate developer CRM: projects, units (flat
or plot, size in sqft or katha, price), buyers with co-buyer and nominee, bookings, instalment
schedules generated from a booking (down payment, N monthly instalments, handover payment),
payments by method, leads with pipeline stages, per-project land document checklists with
uploads. Add a view for "overdue instalments by project".
```
Run the migrations and have Claude scaffold API routes and admin pages.
2. Ask Claude for the schedule generator and a nightly job that sends reminders and flags overdue.
3. Ask Claude for the Bangla copy. Paste:
```
Write Bangla SMS templates for a property developer: instalment due in 3 days, due today,
overdue by 7 days, payment received with receipt number. Under 160 characters, respectful,
Bangla numerals, a bKash link placeholder. Also a one-paragraph Bangla statement summary
for a buyer given paid, due and remaining.
```
Check the tone with a sales manager.
4. Ask Claude for the broker pipeline board, a project dashboard (sold, collected, overdue, next month due) and an Excel import script; every first customer will hand you a spreadsheet.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 developers live, 200 buyers imported, first reminders sent |
| Day 60 | 6 developers or brokers, 4 paying |
| Day 90 | 15 developers or brokers, 10 paying, roughly ৳80,000 monthly revenue |

### First customers with zero budget
- REHAB member directory and the REHAB fair; ask each stall who runs the instalment sheet.
- Facebook groups: "Flat Sale Dhaka", "Purbachal Plot", "Bashundhara Flat Buy Sell"; brokers post daily.
- Google Maps: "real estate developer" in Dhaka, Chattogram, Sylhet, Khulna; call and ask for the accounts person.
- Message: "Your accountant spends two days a month on instalment calls. We send reminders and receipts and show overdue by project in one screen."
- Demo that closes: import their Excel sheet in the meeting and show the overdue list in ten minutes.
- Referral loop: brokers who sell for several developers carry the tool between them; give brokers a free plan.

### Pricing and the maths
- Broker ৳2,999/month, 1 user, up to 50 buyers; Developer ৳7,999/month up to 500 buyers; Developer Plus ৳14,999/month, unlimited buyers and users.
- Costs are SMS (a few hundred taka a month per developer) and hosting; gross margin above 85 percent.
- At the mid price of ৳8,999, roughly 35 paying developers make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. DHA and Bahria style instalment plots sold by thousands of dealers; JazzCash and bank transfers.
- What changes: language pack, payment rail, land checklist (CDA and LDA approvals, fard, registry), SMS gateway.
- What stays: inventory, schedules, reminders, statements, pipeline. Property dealer associations in Lahore and Islamabad as resellers.

### Risks and how to de-risk them
- Risk: developers have long sales cycles. De-risk: start with brokers and the Excel import; developers arrive through their brokers.
- Risk: sensitive buyer data and land documents. De-risk: encrypted uploads, roles, audit logs, a Bangla data agreement.
- Risk: bank payments break the automatic loop. De-risk: fast manual entry, then bank statement upload with Claude parsing by day 90.
- Risk: large developers ask for ERP features. De-risk: stay with instalments and inventory; integrate with idea 98 for site progress.

## Idea 30: Budget Hotel and Guesthouse Manager
*Room board, bKash booking link, police guest register, housekeeping and a light channel manager for residential hotels and guesthouses.*

### Who pays and why now
The customer is a residential hotel with 10 to 60 rooms in Cox's Bazar, Sylhet, Kuakata, Bandarban or near Dhaka bus terminals and hospitals. The front desk keeps a paper register, takes bookings by phone and Facebook page, and collects advances by bKash to the owner's number. Rooms get double-booked in peak season and the police register is filled by hand each night.

They will pay because one double-booked room in Eid week costs more than a year of subscription, and the local thana now demands a proper guest register with NID copies. Domestic tourism has grown fast; guests expect a bKash link and a WhatsApp confirmation. Foreign hotel software costs dollars and speaks English.

Port countries are Indonesia, Vietnam, Nepal, Nigeria and Egypt, where small guesthouses keep the same paper registers.

### The product in 30 days (MVP)
- Room board by date: vacant, booked, occupied, cleaning, with drag to change dates.
- Booking with guest phone, bKash advance link, Bangla confirmation by WhatsApp or SMS.
- Check-in that photographs NID or passport and fills the police register; nightly PDF export.
- Guest folio: room, extra bed, food, laundry, printed bill.
- Housekeeping list with a "cleaned" tap from the attendant's phone.
- Public booking page with photos and prices, linked from the hotel's Facebook page.
- Leave out: OTA sync with Booking.com or Agoda, restaurant POS, accounting, dynamic pricing.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for advances and bills; Nagad second; cash recorded manually.
- WhatsApp Business API or SMS for confirmations; most guests book from Messenger, so a copy-paste text also matters.
- The thana guest register format (name, address, NID or passport, arrival, departure, purpose, from and to) as the check-in schema.
- Bangla numerals on bills, English toggle for foreign guests; cache the board locally for slow hill-district internet.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for guest messages and ID reading, Cloudflare hosting, bKash merchant API, SMS gateway.

1. Ask Claude for the schema and API: hotels, rooms, room_types, bookings, guests, folio_items, payments, housekeeping_tasks, register_entries, with an overbooking check in the database.
2. Build the room board. Paste:
```
Build a Next.js room board for a small Bangladeshi hotel: rows are rooms, columns the next
14 days, cells coloured by status (vacant, booked, occupied, cleaning). Clicking a cell opens
a booking drawer. Support drag to extend or move a booking and block overlaps. Bangla labels,
Bangla date headers, mobile friendly.
```
Test it on a phone at the desk.
3. Ask Claude for the check-in flow: photograph the NID, extract name, number and address with Claude vision, let the receptionist correct it, write the register entry, and export the nightly PDF in the thana format.
4. Ask Claude for guest messages. Paste:
```
Write Bangla and English WhatsApp templates for a budget hotel: booking confirmed with dates,
room type, advance received and balance due; check-in reminder the day before with directions;
thank-you after checkout asking for a Google review. Warm, short, Bangla numerals in the
Bangla version, placeholders for hotel, guest and amounts.
```
Then ask for the public booking page with a bKash advance and a webhook that creates the booking.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 hotels live in one town, 200 bookings recorded |
| Day 60 | 20 hotels, 10 paying |
| Day 90 | 60 hotels, 35 paying, roughly ৳60,000 monthly revenue |

### First customers with zero budget
- Walk Kolatoli and Sugandha Point in Cox's Bazar and the hotel streets near Sylhet Dargah; the owner is often at the desk.
- Facebook groups: "Cox's Bazar Hotel Booking", "Sylhet Tour", "Travellers of Bangladesh", where guesthouses post offers.
- Google Maps: "residential hotel", "guest house", "rest house" in Cox's Bazar, Sylhet, Kuakata, Bandarban, Rangamati.
- Message: "No more double booking in Eid week, and the police register prints itself every night."
- Demo that closes: enter their rooms and tonight's guests in ten minutes, then export the police register PDF.
- Referral loop: hotel owners on one street talk daily; a free month per referred hotel, and every confirmation carries the product name.

### Pricing and the maths
- Small ৳999/month up to 15 rooms; Standard ৳1,999/month up to 40 rooms; Large ৳2,999/month, unlimited rooms and the public booking page.
- Costs are messages (a few taka per booking), ID reading (pennies) and hosting; gross margin above 85 percent.
- At the mid price of ৳1,999, roughly 150 paying hotels make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nepal. Thousands of guesthouses in Pokhara, Thamel and trekking towns, a similar police register, eSewa and Khalti for payments.
- What changes: language pack, payment rail, register format, phone formats, SMS gateway.
- What stays: room board, bookings, folio, housekeeping, public page. Hotel associations and tour operators as resellers.

### Risks and how to de-risk them
- Risk: hotels want OTA sync on day one. De-risk: iCal import from Booking.com by day 60, nothing more until 20 hotels pay.
- Risk: front-desk turnover means retraining. De-risk: a two-minute Bangla video, a one-page guide, three screens only.
- Risk: register formats differ by thana. De-risk: editable export template per hotel.
- Risk: off-season churn. De-risk: annual plans with two free months, sold before Eid.

## Idea 44: Flat Owners' Association Manager
*Service charge via bKash, monthly accounts published to owners, notices, visitor and staff log, maintenance requests and AGM records, all in Bangla.*

### Who pays and why now
The customer is the managing committee of an apartment building with 8 to 80 flats in Dhaka, Chattogram or Sylhet. A volunteer treasurer collects service charge door to door, keeps a notebook, pays guards, lift service and generator diesel, and faces the same question at every AGM: where did the money go. Owners abroad or renting out pay late because nobody sends them anything.

The committee will pay because ৳999 a month is less than one flat's service charge, and transparency ends the fights. Most owners have bKash, many live overseas, and associations increasingly have a bank account and annual accounts to present.

Port countries are Pakistan, Nigeria, Egypt, Indonesia and Sri Lanka. India is skipped because that market is saturated.

### The product in 30 days (MVP)
- Building, flats, owners and tenants with a service charge per flat.
- Monthly dues generated automatically, bKash link by SMS, receipt on payment, defaulter list.
- Expense entry with bill photo (guards, lift, generator, cleaning) and a monthly Bangla statement to every owner.
- Bangla notices by SMS or WhatsApp with read count.
- Maintenance requests from owners with photo, status and cost.
- Visitor and staff log from the guard's phone.
- Leave out: online voting, accounting exports, parking allocation, facility booking.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for service charge; Nagad second; bank transfer entry for owners abroad, Stripe later for dollars.
- SMS for dues and receipts; WhatsApp broadcast for notices and the statement.
- A default expense chart (security, cleaning, lift, generator, pump, common electricity, repair fund) matching how Dhaka committees think.
- Bangla numerals and month names; the statement prints as one page for the notice board; AGM minutes templates in Bangla.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for statements and notices, Cloudflare hosting, bKash merchant API, SMS gateway.

1. Ask Claude for the schema: buildings, flats, owners, tenants, dues, payments, expense_categories, expenses (with photo), notices, maintenance_requests, visitor_logs, meetings, plus a monthly cashbook view.
2. Ask Claude for the dues cycle: generate on the 1st, send bKash links, mark paid on webhook, remind defaulters on the 10th and 20th.
3. Build the statement. Paste:
```
Write a function that takes a month's opening balance, collections by flat, expenses by
category, and closing balance, and produces a one-page Bangla accounts statement for an
apartment owners' association. Bangla numerals, a clear table, a short plain-Bangla summary
at the top. Output HTML ready for PDF.
```
Print it and show a treasurer.
4. Write the notice drafter. Paste:
```
Draft Bangla notices for a Dhaka apartment owners' committee: water tank cleaning date, lift
maintenance shutdown, service charge increase from next month with reason, AGM invitation with
date and agenda. Polite, formal, under 400 characters each, Bangla numerals, ready for WhatsApp.
Two variants of each.
```
Then ask Claude for the guard's visitor log as an offline-capable phone web page: name, flat, purpose, photo, in and out time.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 buildings live, first monthly statement sent |
| Day 60 | 25 buildings, 15 paying |
| Day 90 | 70 buildings, 50 paying, roughly ৳90,000 monthly revenue |

### First customers with zero budget
- Facebook groups for residential areas: "Bashundhara Residents", Uttara sector groups, "Mirpur DOHS", "Mohammadpur Flat Owners", where treasurers ask for advice.
- Lift and generator servicing companies visit every building; pay a referral fee per building.
- Google Maps: apartment complexes by name; the guard gives you the secretary's number.
- Message: "Every owner gets the monthly accounts on WhatsApp. The treasurer stops knocking on doors."
- Demo that closes: enter one month of their notebook and send the statement to the committee WhatsApp group live.
- Referral loop: owners who see the statement own flats elsewhere; every statement ends with "get this for your building".

### Pricing and the maths
- Small ৳999/month up to 20 flats; Standard ৳1,999/month up to 50 flats; Large ৳2,999/month, unlimited flats with guard log.
- Costs are SMS (a handful per flat per month) and hosting; gross margin above 85 percent.
- At the mid price of ৳1,999, roughly 150 paying buildings make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Apartment living in Karachi, Lahore and Islamabad has grown fast, committees run on notebooks, JazzCash and Easypaisa collect dues.
- What changes: language pack, payment rail, expense chart, registration templates, SMS gateway.
- What stays: dues, expenses, statements, notices, maintenance, guard log. Building management and lift firms as resellers.

### Risks and how to de-risk them
- Risk: committees change yearly and the new treasurer drops the tool. De-risk: owners already get statements; make handover a one-tap role transfer.
- Risk: treasurers fear transparency exposes past mess. De-risk: start from today's opening balance, no history required.
- Risk: no merchant account. De-risk: personal bKash numbers with manual matching in month one.
- Risk: low churn also means slow growth. De-risk: share code and sales with idea 58 (markets) and idea 59 (hostels).

## Idea 58: Market Committee Manager
*Shop rent, service charge, electricity sub-meter billing, generator and security dues and Bangla notices for shopping complex and bazaar committees.*

### Who pays and why now
The customer is the committee or owner running a shopping complex or bazaar with 50 to 800 shops. Each month it collects shop rent, service charge, generator and security dues, and electricity by sub-meter. A cashier walks the floors with a receipt book, meter readings go on a sheet, bills are worked out by hand, and disputes never stop.

The committee will pay because the sums are large and leakage is normal. A market with 300 shops collecting ৳3,000 each moves ৳9 lakh a month; a five percent leak is ৳45,000. Power costs have risen, so accurate sub-meter billing is a fight that software can end.

Port countries are Nigeria, Pakistan, India, Indonesia and Egypt, where market unions collect the same dues. This is the commercial twin of idea 44.

### The product in 30 days (MVP)
- Market, floors, shops with shopkeeper, phone, rent, service charge and meter number.
- Monthly meter reading by photo from the collector's phone; units and bill computed at the market's tariff.
- Combined Bangla bill per shop with a bKash link; SMS reminder and receipt.
- Collector mode: unpaid shops floor by floor, "collected in cash" tap, receipt print.
- Defaulter list and collections dashboard by floor and month.
- Notice broadcast to all shops or one floor by SMS or WhatsApp.
- Leave out: lease contracts, accounting exports, parking, CCTV integration.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for shop payments; Nagad second; cash stays large, so collector mode with a Bluetooth thermal printer is essential.
- Electricity tariff is the market's own per-unit rate plus a fixed charge, often stepped; make it editable and show the working on the bill.
- Meter photos read by Claude vision and confirmed by the collector, so disputes have a photo record.
- Bangla numerals on bills and receipts; shopkeepers file them for years.

### Build it with Claude
Stack: Next.js for the office, Flutter Android app for collectors, PostgreSQL, Claude API for meter reading and notices, small VPS, bKash merchant API, SMS gateway.

1. Ask Claude for the schema: markets, floors, shops, tenants, meters, meter_readings (with photo), tariffs, bills, bill_items, payments, notices, and a bill generation function from readings and tariff.
2. Build the meter reader. Paste:
```
I am sending a photo of an electricity sub-meter in a Bangladeshi shopping complex. Return JSON
with the reading as an integer, digits visible, a confidence from 0 to 1, and whether the last
digit is a red decimal to drop. If the image is blurry or the meter partly covered, set
confidence below 0.5 and say why.
```
Wire it into the collector app with a confirm field showing the previous reading.
3. Ask Claude for the combined Bangla bill (rent, service charge, generator, security, electricity with readings and units, bKash link) as PDF and as a 58 mm receipt, and for the offline collector screen.
4. Write the notices. Paste:
```
Write Bangla notices from a Dhaka market committee to shopkeepers: monthly bill issued with due
date, generator diesel surcharge this month with reason, market closed for a holiday, overdue
bills followed by disconnection after a date. Firm but respectful, Bangla numerals, under 300
characters each, for SMS and WhatsApp.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 markets live, 300 shops billed |
| Day 60 | 8 markets, 5 paying |
| Day 90 | 25 markets, 18 paying, roughly ৳55,000 monthly revenue |

### First customers with zero budget
- Walk into the market office at New Market, Gausia, Mouchak, Chattogram's Reazuddin Bazar and every district town's central market.
- Dokan Malik Samity (shop owners' associations) at market and district level; one committee introduces you to ten markets.
- Facebook groups of shopkeepers by market name, and "Business Owners Bangladesh" groups.
- Message: "Meter readings by photo, bills by SMS, and every taka collected in your dashboard the same day."
- Demo that closes: read three meters on one floor with your phone and print three bills in front of the committee.
- Referral loop: shopkeepers trading in two markets ask the other committee; a free month per referred market.

### Pricing and the maths
- Small ৳1,499/month up to 100 shops; Standard ৳2,999/month up to 300 shops; Large ৳4,999/month, unlimited shops and collectors.
- Costs are SMS (one or two per shop per month), meter reading (pennies) and hosting; gross margin above 85 percent.
- At the mid price of roughly ৳3,249, about 90 to 95 paying markets make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria. Market unions in Lagos and Onitsha collect dues from thousands of traders, and generator billing is universal.
- What changes: language pack (English plus Yoruba, Igbo and Hausa notices), payment rail, tariff structure, SMS gateway.
- What stays: shops, meters, bills, collector app, dashboard. Market union executives and local accountants as resellers.

### Risks and how to de-risk them
- Risk: collectors resist because leakage is their income. De-risk: sell to the committee with the dashboard; make the app faster than the receipt book.
- Risk: disputed electricity bills. De-risk: meter photo and the working on every bill.
- Risk: committee politics and elections. De-risk: annual contracts, data owned by the market, one-tap admin transfer.
- Risk: long sales cycle for big markets. De-risk: start with 50 to 150 shop markets in district towns; share code with idea 44.

## Idea 59: Student Hostel and PG Manager
*Seat allocation, rent and meal charges via bKash, guest register, meal counts, notices and parent access for private hostels and messes.*

### Who pays and why now
The customer runs a private student hostel, ladies' hostel or mess near Dhaka University, the Farmgate coaching centres, Chattogram's GEC circle, or any medical or engineering college town. They rent 20 to 200 seats, charge seat rent plus a meal charge based on meals eaten, and run it from a notebook and a meal chart on the wall. Parents pay from the village by bKash and get no confirmation.

They will pay because meal accounting alone eats hours a month and causes constant arguments, and empty seats cost money a waitlist would fill. Students and parents both have bKash, coaching hubs keep growing, and parents want to know their child is safe and fed.

Port countries are India, Pakistan, Nigeria, Indonesia and Egypt, where paying-guest and kos accommodation follows the same pattern.

### The product in 30 days (MVP)
- Hostel, rooms and seats with occupancy, waitlist, move-in and move-out dates.
- Student profile with guardian phone, NID or student ID, monthly rent.
- Daily meal count: students mark lunch and dinner on or off by 10 a.m.; the manager sees the kitchen count.
- Monthly bill: rent plus meals at the per-meal rate, bKash link to student and guardian, receipt on payment.
- Guest register for visitors and overnight guests.
- Bangla notices to students; guardian SMS for paid, due and a monthly summary.
- Leave out: attendance, complaint tickets, laundry and extras, online seat booking.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for bills; Nagad second; guardians often pay the owner's personal number from the village, so allow manual matching.
- SMS to guardians; WhatsApp broadcast for student notices.
- Mess meal rates are usually kitchen spend divided by total meals; support both a fixed and a computed rate.
- Bangla numerals; a guardian who reads only Bangla must understand the SMS; gender-specific hostels and a thana-ready resident list.

### Build it with Claude
Stack: Next.js with a mobile student view, PostgreSQL, Claude API for notices and summaries, Cloudflare hosting, bKash merchant API, SMS gateway.

1. Ask Claude for the schema: hostels, rooms, seats, students, guardians, stays, meal_days, meal_marks, kitchen_expenses, bills, payments, visitors, notices, with the meal rate as a SQL function.
2. Build meal marking. Paste:
```
Build a mobile web page for hostel students in Bangla: today's and tomorrow's lunch and dinner
with on/off toggles, a 10:00 cutoff for the same day, a running count of meals this month and
estimated cost. Also a manager view with today's lunch and dinner totals by room and who is off.
Next.js, PostgreSQL, phone login by OTP.
```
Have five students use it for a week before adding anything.
3. Ask Claude for the monthly bill job: rent plus meals times rate, bKash link to student and guardian, mark paid on webhook.
4. Write the guardian messages. Paste:
```
Write Bangla SMS templates for a student hostel to a guardian in a village: monthly bill with
rent, meals eaten, meal charge and total with a bKash link; payment received; a short monthly
summary saying the student stayed and ate normally. Simple, warm Bangla a parent with basic
literacy can read, Bangla numerals, under 160 characters.
```
Then ask for the seat board, waitlist page and thana-format resident export.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 4 hostels live, 150 students marking meals |
| Day 60 | 20 hostels, 12 paying |
| Day 90 | 70 hostels, 45 paying, roughly ৳45,000 monthly revenue |

### First customers with zero budget
- Facebook groups: "Dhaka Hostel Seat", "Ladies Hostel Dhaka", "Farmgate Mess Seat", "Chittagong Hostel", where owners post vacancies with phone numbers daily.
- Walk the lanes around Dhaka University, Nilkhet, Farmgate, Mirpur coaching hubs and medical colleges; every gate has a hostel sign with a number.
- Coaching centres point students to hostels; pay them a referral fee.
- Message: "Meal accounts done by the students themselves, bills to parents by bKash, empty seats filled from a waitlist."
- Demo that closes: set up one floor, have three students mark tomorrow's meals, show the kitchen count update.
- Referral loop: every guardian SMS carries the product name, and hostel owners in the same lane copy each other.

### Pricing and the maths
- Small ৳499/month up to 30 seats; Standard ৳999/month up to 100 seats; Large ৳1,499/month, unlimited seats and managers.
- Costs are SMS (two or three per student per month) and hosting; gross margin above 85 percent.
- At the mid price of ৳999, roughly 300 paying hostels make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, for paying-guest housing in Kota, Pune, Bengaluru and Kolkata with UPI; West Bengal takes the Bangla version almost unchanged.
- What changes: language pack, payment rail, meal culture defaults, SMS gateway.
- What stays: seats, meal marking, bills, guardian messages, guest register. Coaching institutes and PG aggregators as resellers.

### Risks and how to de-risk them
- Risk: students stop marking and the count is wrong. De-risk: default to "on", mark only to switch off, reminder at 9 a.m.
- Risk: owners fear guardians seeing the accounts. De-risk: guardians see only their child's bill.
- Risk: slow months between admissions. De-risk: annual plans and the waitlist that fills seats.
- Risk: generic rent apps. De-risk: meal accounting is the moat; nobody else does it.

## Idea 74: Expat Property Caretaker Platform
*Diaspora owners get rent via bKash, monthly photo and video inspections, repair approvals, tax and utility payments and tenant screening, paid in dollars.*

### Who pays and why now
The customer is a Bangladeshi in London, New York, Dubai or Riyadh who owns a flat, house or plot back home. A relative "looks after it". Rent arrives late, repairs are guessed at, utility bills lapse, and the owner visits every two years. Millions of families are in this position, and the owner earns in hard currency.

They will pay because $15 to $49 a month is small against a flat worth ৳1 crore, and accountability has been impossible. bKash and WhatsApp connect both sides, and a phone camera makes verified inspection cheap. You run the platform and a vetted caretaker network.

Port countries are Pakistan, India, Nigeria, the Philippines and Egypt, each with a huge property-owning diaspora.

### The product in 30 days (MVP)
- Owner dashboard in English and Bangla, paid by Stripe in dollars: properties, tenant, rent status, documents, inspection history.
- Rent collection: bKash link to the tenant, receipt to the owner by WhatsApp, monthly statement.
- Caretaker app: monthly checklist with 10 photos and a 60-second video, stamped with GPS and time.
- Repairs: caretaker uploads the issue and two quotes, owner approves in one tap, completion photos recorded.
- Utility and holding tax reminders with a paid-by-caretaker log and bill photo.
- Leave out: tenant screening scores, legal services, sale listings, automated caretaker payouts.

### Data, integrations and the Bangladesh specifics
- Stripe or Lemon Squeezy for owner subscriptions; bKash merchant API for tenant rent; bank transfers recorded manually.
- WhatsApp for owner alerts and inspection delivery; SMS to tenants.
- Holding tax and utility formats for Dhaka city corporations, DESCO, DPDC, Titas and WASA, in the format owners recognise.
- Bangla for caretakers and tenants, English dashboard with Bangla toggle; media stored with GPS and time stamps.

### Build it with Claude
Stack: Next.js, PostgreSQL, Flutter Android app for caretakers, Claude API for summaries, Cloudflare R2 for media, Stripe, bKash merchant API.

1. Ask Claude for the schema: owners, properties, tenants, rent_invoices, payments, caretakers, inspections, inspection_items (with media), repair_requests, quotes, utility_bills, subscriptions, with access rules.
2. Build the inspection app. Paste:
```
Build a Flutter screen for a property caretaker in Bangladesh: a Bangla checklist (front door,
locks, water leaks, walls, electrical, tenant present, common area), one photo per item plus a
60 second video. Stamp GPS and time on each file, compress, queue uploads for weak networks,
block submission until all items are done. Progress text in Bangla.
```
Test it with a real caretaker.
3. Ask Claude for the summariser: Bangla checklist answers and notes become a short English summary with action flags.
4. Write the outreach copy. Paste:
```
Write a WhatsApp message and a landing page hero for Bangladeshis abroad who own property in
Bangladesh. Pain: relatives collect rent late, no photos, surprise repairs. Offer: rent via
bKash to your dashboard, monthly photo and video inspection, repairs you approve, utility bills
paid and logged, from $15 a month. English, warm, no hype. Also a Bangla version.
```
Then ask for the Stripe flow with a 30-day trial and the bKash rent webhook.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 properties in Dhaka, 3 caretakers, first inspections delivered |
| Day 60 | 40 properties, 25 paying owners |
| Day 90 | 120 properties, 80 paying, roughly $2,500 monthly revenue |

### First customers with zero budget
- Facebook groups: "Bangladeshis in London", "Bangladeshi Community New York", "Probashi Bangladeshi UAE" and Sylheti groups in the UK, where property questions appear daily.
- Diaspora mosques and community centres in Tower Hamlets, Jackson Heights and Deira; a poster and a WhatsApp number.
- Remittance shops and travel agents abroad know who owns property at home; pay a referral fee.
- Message: "Your flat in Dhaka, inspected with photos every month, rent in your dashboard, repairs only when you say yes."
- Demo that closes: a sample inspection report from a real Dhaka flat, sent by WhatsApp before the call.
- Referral loop: owners forward the report to relatives with the same problem; one free month per referral.

### Pricing and the maths
- Basic $15/month per property: rent and quarterly inspection; Standard $29/month: monthly inspection and repairs; Premium $49/month: fortnightly inspection, utility and tax payments, tenant screening.
- Costs are the caretaker fee per visit (roughly ৳500 to ৳1,000), media storage and Stripe fees; gross margin around 50 to 60 percent, but paid in dollars.
- At the mid price of about $32 and roughly ৳120 per dollar, about 80 paying properties make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Overseas Pakistanis in the UK and Gulf own property in Lahore and Karachi; JazzCash collects rent.
- What changes: Urdu language pack, payment rail, utility and tax formats, a new caretaker network per city.
- What stays: dashboard, Stripe billing, inspection app, repair flow. Community organisations and remittance companies as resellers.

### Risks and how to de-risk them
- Risk: caretaker fraud. De-risk: GPS and time stamps, two quotes per repair, and pay caretakers only after the owner accepts the inspection.
- Risk: owners trust family, not strangers. De-risk: let the owner nominate a relative as caretaker; you add the accountability layer.
- Risk: handling repair money. De-risk: owners pay suppliers directly by bKash; you hold no funds in the MVP.
- Risk: rules on collecting rent for others. De-risk: rent flows tenant to owner through bKash merchant links; the terms state you are a software provider.

## Idea 98: Construction Site Daily Reporting
*Site engineers log progress with photos, material receipts, labour counts, safety checks and delays in Bangla, and developers see every site in one dashboard.*

### Who pays and why now
The customer is a developer or construction firm with 5 to 30 active sites: apartments in Dhaka and Chattogram, factory sheds in Gazipur. The managing director learns progress by phoning site engineers each evening. Deliveries are on paper chalans, labour counts are approximate, and delays surface when a buyer complains about handover.

They will pay because a week of hidden delay on one site costs far more than ৳2,999 a month, and photo-verified progress is what banks and buyers now expect. Site engineers already post photos to a WhatsApp group; the product turns that habit into a record.

Port countries are India, Pakistan, Nigeria, Egypt, Indonesia and Kenya, where mid-size developers get the same phone-call reports. This pairs with ideas 29 and 20.

### The product in 30 days (MVP)
- Daily report from the engineer's phone: Bangla progress notes, 5 to 20 photos tagged by floor or area, weather.
- Labour count by trade and contractor with a running monthly total.
- Material receipts: chalan photo, Claude reads item and quantity, engineer confirms; stock in and used.
- Safety checklist (helmets, harness, scaffolding, electrical) with a photo per failed item.
- Delay log with cause (material, labour, weather, approval, payment) and days lost.
- Head office dashboard: all sites, today's report status, last photo, open delays, monthly spend.
- Leave out: BOQ and schedule integration, subcontractor billing, drone capture, buyer-facing pages.

### Data, integrations and the Bangladesh specifics
- The developer pays the subscription by bKash merchant or bank transfer; annual invoices are common.
- WhatsApp is where engineers live; send the daily PDF to the project group automatically.
- Claude vision for chalans in mixed Bangla and English handwriting; offline first for Purbachal and Gazipur signal.
- Bangla numerals and trade names (রাজমিস্ত্রি, রডমিস্ত্রি, হেলপার) in the app; English dashboard with Bangla toggle.

### Build it with Claude
Stack: Flutter Android app, Next.js dashboard, PostgreSQL, Claude API for chalan reading and briefings, Cloudflare R2 for photos, small VPS, bKash for subscriptions.

1. Ask Claude for the schema: companies, projects, sites, users with roles, daily_reports, report_photos (area, GPS, time), labour_entries, material_receipts, receipt_items, stock_movements, safety_checks, delays, plus a query for each site's last report.
2. Build the report form. Paste:
```
Build a Flutter daily site report form for a Bangladeshi construction site engineer, in Bangla:
date and weather, progress notes with voice-to-text, photos tagged by floor and area, labour
count by trade (mason, rod worker, helper, electrician, plumber) per contractor, a safety
checklist with pass/fail and photo, a delay entry. Save offline, upload in the background,
show a green tick when head office has received it.
```
Have two engineers use it for a week.
3. Ask Claude for the chalan reader, modelled on idea 20, and the stock ledger per material.
4. Write the briefing. Paste:
```
Given today's reports from 12 construction sites (Bangla progress notes, labour counts, material
received, safety failures, delays), write a 10-line English morning briefing for the managing
director: sites with no report, safety failures, new delays with cause, sites with unusually
low labour. Plain, factual, use numbers. Then a Bangla version.
```
Send it by WhatsApp at 7 a.m., then ask Claude for the dashboard, photo timeline and a weekly PDF for banks.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 developer, 5 sites reporting daily |
| Day 60 | 4 developers, 20 sites, 10 sites paying |
| Day 90 | 10 developers, 60 sites, 40 sites paying, roughly ৳90,000 monthly revenue |

### First customers with zero budget
- REHAB member list and developers already using idea 29; same buyer, different department.
- Facebook groups: "Civil Engineers Bangladesh", "BUET Civil Alumni", "Site Engineer Job BD"; engineers trial it and carry it to their MD.
- Google Maps: "construction company", "real estate developer" in Dhaka, Chattogram, Gazipur; ask for the project director.
- Message: "Stop phoning your sites every evening. See every site's photos, labour and delays before breakfast."
- Demo that closes: set one site live in an afternoon and send the MD a real briefing the next morning.
- Referral loop: engineers change firms often and ask for it; give them a free personal account.

### Pricing and the maths
- Standard ৳1,499 per site per month up to 10 sites; Pro ৳2,999 per site per month with material stock, safety module and weekly PDFs. Annual billing with two months free.
- Costs are photo storage, Claude vision and briefings (a few hundred taka per site per month) and hosting; gross margin around 80 percent.
- At the mid price of about ৳2,249 per site, roughly 135 paying sites, or 10 to 15 developers, make about ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, starting with Kolkata developers who take the Bangla version as is, then Hindi with UPI.
- What changes: language pack, trade names and safety norms, payment rail, WhatsApp templates.
- What stays: app, dashboard, chalan reader, briefing. Construction consultants and quantity surveyors as resellers.

### Risks and how to de-risk them
- Risk: engineers see surveillance and under-report. De-risk: the record protects them in disputes; keep the form under three minutes.
- Risk: photo storage cost grows. De-risk: compress on device, originals for 90 days, thumbnails forever.
- Risk: developers want schedule and BOQ. De-risk: a simple milestone list by day 90; integrate with idea 29 rather than build an ERP.
- Risk: low signal at sites. De-risk: offline first, tested in Purbachal before launch.


---

# Section 10: Transport and Logistics

Bangladesh moves people and goods on CNG autos, buses, launches, trucks and delivery vans that are almost all run from a khata and a phone. This section covers nine software businesses that replace those khatas for owners who handle real money every day and will pay for a ledger that stops leakage.

## Idea 28: Vehicle Owner Fleet Ledger
*A phone app where the owner of 2 to 20 vehicles records daily jama from drivers, fuel and repairs, and never misses a fitness, tax token or insurance renewal.*

### Who pays and why now
The customer is a small vehicle owner: a person with three CNG autos in Mirpur, a rent-a-car owner with six microbuses, a trader with four trucks in Chattogram. Drivers pay a fixed daily jama in cash or bKash. The owner writes it in a khata or simply remembers it, and arguments about missed days, repair advances and fuel money never stop.

They will pay because the losses are concrete. One unrecorded jama is a day of income gone. One expired fitness certificate or tax token means a fine and an idle vehicle. An app at ৳199 a month pays for itself the first time it prevents either. Owners now carry smartphones, drivers already pay by bKash, and stand committees run on WhatsApp groups, which makes distribution cheap. Ports: India, Pakistan, Indonesia (ojek), Nigeria (keke) and Kenya (matatu) share the same owner-driver structure.

### The product in 30 days (MVP)
- Vehicle list with registration number, type and assigned driver.
- Daily jama entry per vehicle in two taps, cash or bKash, with a missing-day flag.
- Expense log for fuel, repairs, parts and fines, with a receipt photo.
- Driver ledger with advances, deductions and balance due, exportable as a Bangla PDF.
- Document expiry alerts for fitness, tax token, route permit, insurance and licence, by SMS 15 and 3 days before.
- Monthly profit per vehicle on one screen.
- Leave out: GPS tracking, fuel card integration, multi-owner company accounts, a driver-facing app.

### Data, integrations and the Bangladesh specifics
- bKash merchant API to accept jama directly; cash entries stay manual.
- A local SMS gateway for alerts and driver receipts; Bangla unicode SMS costs more, so keep templates short.
- A seed table of BRTA document types and typical validity periods; owners enter dates from their papers.
- Offline-first Flutter app that syncs when online, because stands often have weak data.
- Bangla numerals and month names in every driver-facing PDF and SMS.

### Build it with Claude
Stack: Flutter for Android, Laravel API, PostgreSQL, Claude API for receipt reading, a small VPS, bKash merchant API, local SMS gateway.

1. Ask Claude for the schema and migrations. Paste this:
```
Design a PostgreSQL schema for a small fleet ledger app in Bangladesh.
Tables: owners, vehicles (reg_no, type, documents with expiry dates),
drivers, daily_jama (vehicle, date, amount, method cash/bkash, missing flag),
expenses (vehicle, category, amount, receipt_url), driver_advances.
Add a view for monthly profit per vehicle. Output Laravel migrations.
```
   Review the tables, then run the migrations on your VPS.
2. Ask Claude for the Flutter screens (vehicle list, today's jama grid, expense form with camera, document dates) with offline storage and a sync queue. Test on a cheap Android phone.
3. Add receipt reading. Paste this:
```
You receive a photo of a fuel or repair receipt from Bangladesh.
Return JSON: {vendor, date (YYYY-MM-DD), amount_bdt, category
(fuel/repair/parts/fine/other), confidence}. Amounts may be in Bangla
numerals; convert to digits. If unreadable, set confidence below 0.5.
```
   Wire it to the expense form so the owner only confirms.
4. Ask Claude for the reminder cron job, six short Bangla SMS templates, and a Bangla WhatsApp message to owner associations offering a free month.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 20 owners using it daily, 100 vehicles registered |
| Day 60 | 80 owners, 40 paying, ৳15,000 monthly revenue |
| Day 90 | 250 owners, 150 paying, ৳60,000 monthly revenue |

### First customers with zero budget
- CNG auto stand committees in Dhaka and district towns; ask the stand secretary for ten minutes at the weekly meeting.
- Facebook groups for rent-a-car and truck owners (search "rent a car owners", "ট্রাক মালিক", "সিএনজি মালিক সমিতি").
- Google Maps category "car rental" in Dhaka and Chattogram; call and offer free setup.
- The demo that closes: enter the owner's vehicles and document dates in five minutes and show the next expiry on screen.
- Referral loop: a free month for every owner who brings another owner from the same stand.

### Pricing and the maths
- Basic ৳199/month for up to 3 vehicles; Standard ৳499 for up to 10; Fleet ৳799 for up to 20.
- Cost of goods is a few taka per owner per month in SMS, pennies in AI calls and one VPS. Gross margin is roughly 85 percent.
- About 600 paying owners at the ৳499 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, because matatu owners face the same daily collection and renewal problems and M-Pesa is universal.
- What changes: language pack, M-Pesa instead of bKash, the document list (NTSA), currency.
- What stays: schema, jama logic, expense capture, reminder engine.
- Reseller: matatu SACCOs play the role of the stand committee.

### Risks and how to de-risk them
- Risk: owners stop entering data after a week. De-risk: two-tap jama entry and a daily evening reminder.
- Risk: drivers dispute app records. De-risk: send the driver an SMS receipt for every jama entry.
- Risk: the low price limits revenue. De-risk: add renewal services and insurance referrals later.
- Risk: a ride-hailing player adds fleet tools. De-risk: stay focused on non-app fleets, which are the majority.

## Idea 37: Bus Counter and Trip Accounts
*Seat map and bKash ticketing for intercity bus counters, with trip settlement, wages and fuel logs, so the owner sees every trip's profit the same night.*

### Who pays and why now
The customer is an intercity bus operator with 5 to 60 buses. Their counters at Gabtoli, Sayedabad, Mohakhali and in district towns write paper tickets and phone other counters to hold seats. After each trip the supervisor hands the owner a slip with cash and fuel receipts. Nobody knows how many passengers really boarded.

Owners will pay because leakage is large and personal. Unrecorded passengers, double-sold seats and inflated fuel slips come straight out of their pocket. Online ticket sites serve the big brands only, while hundreds of mid-size operators have nothing, and passengers already pay by bKash at the counter. Ports: Indonesia, the Philippines, Nigeria, Kenya and Pakistan all have large private bus sectors on paper tickets.

### The product in 30 days (MVP)
- Routes, schedules and buses with seat layouts (2x2, 2x1, sleeper).
- Counter ticketing screen: pick seat, passenger name and phone, cash or bKash, print or SMS ticket.
- One live seat map shared by every counter on a route.
- Trip settlement: tickets sold, cash by counter, fuel, toll, driver and helper wages, net to owner.
- Counter staff logins with per-counter cash accountability.
- Owner daily summary by SMS or WhatsApp.
- Leave out: public online booking, GPS bus tracking, parcel service, dynamic pricing.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for counter payments, with the transaction ID stored on the ticket; add SSLCommerz for cards later.
- Bluetooth thermal printers on Android tablets; a Bangla SMS ticket as the fallback.
- The counter app must tolerate poor connectivity; seat conflicts are resolved by server timestamp.
- Bangla numerals for fare and date on the ticket; seat labels stay as A1, B2.

### Build it with Claude
Stack: Next.js for owner and admin, Flutter for Android counter tablets, PostgreSQL with websockets for the live seat map, Claude API for settlement summaries, small VPS, bKash merchant API.

1. Ask Claude for the schema and seat map model. Paste this:
```
Design a PostgreSQL schema for intercity bus ticketing in Bangladesh.
Tables: operators, buses (seat_layout JSON), routes, trips, counters, staff,
tickets (trip, seat, passenger_name, phone, fare, method cash/bkash,
bkash_trx_id, counter, sold_by), trip_expenses, trip_settlements.
Add a unique constraint so a seat cannot be sold twice on one trip.
```
   Apply the migrations and seed one real route from the operator.
2. Ask Claude for the Flutter counter screen with a tappable seat grid and a websocket channel that pushes seat holds to every counter. Test with two tablets at once.
3. Ask Claude for the settlement page and owner summary. Paste this:
```
Given tonight's trip data (tickets by counter, cash deposited by counter,
bKash total, fuel, toll, wages), write a 5-line Bangla summary for the
bus owner. Flag any counter where tickets sold do not match cash plus
bKash, and any fuel entry over 20 percent above the route average.
Use Bangla numerals. Plain tone, no greetings.
```
   Send it each night by WhatsApp or SMS.
4. Ask Claude for a Bangla ticket template for thermal print and SMS, a one-page counter training sheet in Bangla, and an outreach script for operator owners.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 operator live on 3 counters, 500 tickets sold |
| Day 60 | 5 operators, ৳15,000 monthly revenue |
| Day 90 | 15 operators, 60 counters, ৳75,000 monthly revenue |

### First customers with zero budget
- Walk the counters at Gabtoli, Sayedabad and Mohakhali; counter managers know which owners are frustrated.
- District bus owner associations (Bogura, Rajshahi, Khulna, Sylhet) and their Facebook groups.
- Facebook groups for bus enthusiasts in Bangladesh, where operator staff post daily.
- The demo that closes: set up one route with the real seat layout and sell a live ticket by bKash from two tablets at once.
- Referral loop: give the first operator on a route three free months in exchange for introductions to the others.

### Pricing and the maths
- Starter ৳2,999/month for up to 10 buses; Growth ৳5,999 for up to 30; Enterprise ৳9,999 for unlimited buses and counters.
- Cost of goods is SMS tickets at a few taka per message plus hosting. Gross margin is roughly 80 percent.
- About 45 to 50 paying operators at the ৳6,499 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya or Nigeria, where long-distance private buses sell counter tickets and mobile money is standard.
- What changes: language pack, M-Pesa or Paystack, seat layouts, receipt regulations.
- What stays: seat map engine, settlement logic, staff roles, summary generator.
- Reseller: a local ticketing agent or bus park association.

### Risks and how to de-risk them
- Risk: counter staff resist because the system exposes leakage. De-risk: sell to the owner, train staff on site, pay a small per-ticket bonus for the first month.
- Risk: connectivity failures at rural counters. De-risk: offline sale from a seat block allocated to each counter.
- Risk: printer hardware problems. De-risk: support two proven printer models only and keep the SMS fallback.
- Risk: large operators want features you lack. De-risk: start with mid-size operators and grow with them.

## Idea 39: Service Contract Manager for Installers
*Installers of solar, AC, generators, lifts and CCTV track every warranty and AMC, get reminded before renewal, dispatch technicians and send Bangla quotes and invoices.*

### Who pays and why now
The customer is an installation company with 3 to 30 technicians: a solar EPC firm serving factories in Gazipur, an AC dealer in Chattogram, a lift maintenance contractor in Dhaka, a CCTV installer in Sylhet. Their records live in Excel and in the lead technician's phone. Nobody knows which annual maintenance contract ends next month, so it quietly lapses and the customer calls a competitor.

They will pay because renewals are their most profitable revenue and they are losing it for free. A single lift AMC or factory solar contract is worth many times the software fee. Solar is booming under net metering, AC ownership is climbing, and every new building needs lift and generator service. Ports: Nigeria and Pakistan are in a solar boom, while India, Indonesia and Egypt have the same installer economy.

### The product in 30 days (MVP)
- Customer and site register with installed equipment, serial number and install date.
- Contract records: warranty or AMC, start and end dates, visits included, price.
- Renewal reminders to the installer at 60 and 30 days, and to the customer in Bangla by SMS or WhatsApp.
- Service tickets: complaint in, technician assigned, photo and signature on completion.
- Quote to invoice as a Bangla PDF with a VAT line.
- Technician mobile view with today's jobs and a map link.
- Leave out: spare parts inventory, GPS tracking, customer portal, payroll.

### Data, integrations and the Bangladesh specifics
- bKash merchant API and SSLCommerz for AMC payments; corporate customers still pay by cheque, so record that too.
- WhatsApp Business API for reminders and quote delivery; SMS as fallback.
- Bangla PDF templates with Bangla numerals and a Mushak-style VAT line for corporate customers.
- A seed list of equipment types with default warranty periods (inverter, panel, compressor, lift motor).
- Technician view works as a PWA on any Android phone, offline for the day's job list.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, PWA for technicians, Claude API for ticket parsing and Bangla documents, small VPS, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a service contract manager for installers
in Bangladesh. Tables: customers, sites, equipment (type, serial,
installed_at), contracts (type warranty/amc, start, end, visits_included,
price), tickets (site, equipment, problem, technician, status, photos),
quotes, invoices (with vat_percent). Add a query for contracts ending
in the next 60 days. Output Laravel migrations.
```
   Run the migrations and import the installer's Excel with a CSV upload.
2. Ask Claude for the contract list, ticket board and technician PWA screens, one screen per prompt, and assemble them.
3. Add the AI ticket parser. Paste this:
```
An installer receives complaints by phone or WhatsApp in Bangla or English.
From the message below, return JSON: {customer_hint, equipment_type,
problem_summary_bn, urgency low/medium/high, suggested_visit_within_hours}.
Keep problem_summary_bn under 20 words in plain Bangla.
Message: {{message}}
```
   Show the result as a pre-filled ticket the dispatcher confirms.
4. Ask Claude for the Bangla quote and invoice templates, and for the renewal WhatsApp message in three variants (60 days, 30 days, expired).

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 installers loaded, 300 contracts in the system |
| Day 60 | 20 installers, 12 paying, ৳20,000 monthly revenue |
| Day 90 | 60 installers, 40 paying, ৳70,000 monthly revenue |

### First customers with zero budget
- Facebook groups for solar installers and AC technicians in Bangladesh (search "solar Bangladesh", "AC technician BD").
- Google Maps categories "solar energy company", "air conditioning contractor", "elevator service" in Dhaka and Chattogram.
- Dealer networks of inverter and AC brands; their dealers are your installers.
- The demo that closes: import their Excel and show the list of contracts that already expired without anyone noticing.
- Referral loop: each renewal reminder to a customer carries the installer's brand, and installers refer other trades they meet on site.

### Pricing and the maths
- Starter ৳999/month for up to 3 technicians; Team ৳1,999 for up to 10; Business ৳2,999 for unlimited technicians and branches.
- Cost of goods is WhatsApp and SMS messages plus hosting, a small share of revenue. Gross margin is roughly 85 percent.
- About 150 paying installers at the ৳1,999 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria, where the solar and generator installer market is large and inverter dealers are organised.
- What changes: language pack, Paystack or Flutterwave, VAT format, equipment type list.
- What stays: contract engine, ticket flow, renewal reminders, quote and invoice builder.
- Reseller: inverter and solar brand distributors who want their dealers to retain customers.

### Risks and how to de-risk them
- Risk: installers do not enter old contracts. De-risk: do the first import for them from Excel or photos of paper contracts.
- Risk: technicians ignore the app. De-risk: keep the technician view to one screen and send job details by WhatsApp too.
- Risk: generic field service tools undercut you. De-risk: win on Bangla documents, bKash and renewal focus.
- Risk: slow sales cycle with companies. De-risk: start with the owner-operators who decide on the spot.

## Idea 47: Delivery Route Ledger (Water, LPG, Milk)
*Neighbourhood water-jar, LPG and milk suppliers manage subscriptions, daily routes, empty containers and monthly dues collected via bKash.*

### Who pays and why now
The customer is a neighbourhood supplier who delivers the same product to the same homes every day or week: a drinking water plant sending out hundreds of 20-litre jars, an LPG cylinder shop, a dairy delivering milk before dawn. Each delivery man keeps a khata. At month end the owner adds up dues from memory, and every second customer argues about how many empties they returned.

They will pay because containers are capital and dues are cash. A missing jar or cylinder is a real loss, and uncollected dues at month end are the difference between profit and none. Customers now pay by bKash anyway, so a payment link with an exact amount removes the argument. Ports: India, Pakistan, Nigeria, Egypt and Indonesia all have the same daily jar and cylinder economy.

### The product in 30 days (MVP)
- Customer list with address, product, price, delivery days and empties currently held.
- Daily route sheet per delivery man: tick delivered, record empties returned, note skipped.
- Monthly dues computed automatically, with a bKash payment link sent by SMS.
- Container ledger showing jars or cylinders out versus returned per customer.
- Delivery man settlement: deliveries, cash collected, shortages.
- Owner dashboard: dues outstanding and customers holding too many containers.
- Leave out: GPS route optimisation, a customer app, purchase inventory, multi-branch.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for dues, with the payment link carrying the exact amount; Nagad as a second option.
- Bangla SMS for dues reminders and receipts; keep each under 70 unicode characters.
- Offline-first Flutter app for delivery men, since routes run through areas with patchy data.
- Bangla numerals on all customer-facing messages and the monthly statement PDF.
- A one-time import from photos of the old khata using Claude, so switching costs nothing.

### Build it with Claude
Stack: Flutter for Android (delivery men), Laravel API, PostgreSQL, Claude API for khata import and messages, small VPS, bKash merchant API, local SMS gateway.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a delivery route ledger in Bangladesh
(water jars, LPG cylinders, milk). Tables: suppliers, delivery_men,
customers (address, product, unit_price, delivery_days, containers_held),
deliveries (customer, date, qty_delivered, empties_returned, skipped),
payments (customer, amount, method cash/bkash, trx_id), settlements.
Add a view for monthly dues per customer. Output Laravel migrations.
```
   Apply it and create one supplier with a real route.
2. Ask Claude for the Flutter route screen: a list of today's customers in route order with big buttons for delivered, empties and skipped, working offline.
3. Import the khata. Paste this:
```
This photo shows a handwritten Bangla delivery khata page. Extract rows
as JSON: [{customer_name, address_hint, phone, product, monthly_qty,
dues_bdt, containers_held}]. Convert Bangla numerals to digits. Mark any
uncertain value with "?" so a human can check it.
```
   Show the rows in a review table before saving.
4. Ask Claude for the dues SMS, the monthly statement PDF in Bangla, and the settlement screen for the delivery man.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 suppliers live, 1,000 customers imported |
| Day 60 | 25 suppliers, 15 paying, ৳15,000 monthly revenue |
| Day 90 | 80 suppliers, 50 paying, ৳50,000 monthly revenue |

### First customers with zero budget
- Google Maps categories "drinking water supplier", "LPG dealer" and "dairy" in Dhaka, Gazipur, Narayanganj and Chattogram.
- Facebook groups for water plant owners and LPG dealers; distributors of the big LPG brands know every shop.
- Apartment building committees, who can recommend a supplier that sends proper statements.
- The demo that closes: photograph one page of their khata, import it, and send a real dues SMS with a bKash link to one customer.
- Referral loop: a free month for each supplier referred; suppliers in nearby areas know each other from the same wholesalers.

### Pricing and the maths
- Basic ৳499/month for up to 300 customers; Standard ৳999 for up to 1,000; Pro ৳1,499 for unlimited customers and delivery men.
- Cost of goods is mostly SMS, roughly one message per customer per month, plus hosting. Gross margin is roughly 75 to 80 percent.
- About 300 paying suppliers at the ৳999 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Egypt or Pakistan, where bottled water and cylinder delivery to homes is a daily habit.
- What changes: language pack, payment rail (Fawry, JazzCash or Easypaisa), container types, SMS provider.
- What stays: route sheet, container ledger, dues engine, settlement logic.
- Reseller: bottled water franchisors and LPG distributors who want their dealers organised.

### Risks and how to de-risk them
- Risk: delivery men do not tick deliveries. De-risk: tie their settlement to the app so untracked deliveries mean unpaid commission.
- Risk: customers ignore SMS links. De-risk: the delivery man can also collect cash and record it on the spot.
- Risk: very low willingness to pay among small suppliers. De-risk: target suppliers with 300 or more customers first.
- Risk: SMS costs eat margin. De-risk: send one monthly statement, not daily messages.

## Idea 53: Used Vehicle and Motorbike Dealer Inventory
*Motorbike and used-car dealers keep stock with photos and papers, sell on instalments with a proper ledger, and post to Facebook in one click.*

### Who pays and why now
The customer is a used motorbike showroom or small car dealer: the bike shops around Bangla Motor and Mirpur, district town showrooms, and used-car yards in Dhaka. They sell on kisti, with a paper agreement, a guarantor and a monthly visit to collect. Ownership transfer at BRTA drags on for months because nobody tracks which paper is missing.

They will pay because instalment defaults and missing papers are their two biggest losses. A ledger that reminds buyers before the due date, records every bKash payment and shows exactly which document is outstanding is worth far more than ৳999 a month. Facebook Marketplace and pages are where they sell today, so a tool that writes and posts listings saves them daily effort. Ports: India, Pakistan, Nigeria, Indonesia and Kenya all have huge two-wheeler resale markets on instalments.

### The product in 30 days (MVP)
- Stock register: photos, registration, engine and chassis numbers, purchase price, papers checklist.
- Buyer record and instalment plan: down payment, monthly amount, due dates, guarantor details.
- Instalment ledger with bKash payments and automatic Bangla SMS reminders.
- Ownership transfer checklist per sale with the status of each document.
- Facebook listing text and photo set generated in Bangla, ready to copy to the page.
- Enquiry list: test rides, follow-ups, lost reasons.
- Leave out: bank financing partners, public website, auctions, full accounting.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for instalments with the transaction ID on the ledger; cash still recorded manually.
- Bangla SMS reminders three days before and on the due date, with Bangla numerals.
- A checklist template of BRTA transfer documents (smart card, tax token, fitness, insurance, sale deed, seller NID).
- Instalment agreement PDF in Bangla, printable for signature and stamp.
- Photo storage on Cloudflare R2 or similar to keep hosting costs low.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for listings and reminders, Cloudflare for hosting and image storage, bKash merchant API, local SMS gateway.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a used motorbike and car dealer in
Bangladesh. Tables: dealers, vehicles (make, model, year, reg_no,
engine_no, chassis_no, purchase_price, photos, papers JSON), buyers,
sales (vehicle, buyer, price, down_payment, instalment_amount, months),
instalments (sale, due_date, paid_at, method, trx_id), transfer_steps,
enquiries. Output Prisma schema and migrations.
```
   Apply it and add the dealer's current stock.
2. Ask Claude for the stock, sale and instalment screens in Next.js, with a mobile-friendly camera upload for photos.
3. Add the listing writer. Paste this:
```
Write a Facebook Marketplace listing in Bangla for a used vehicle.
Input: {make, model, year, km, condition_notes, price, dealer_area}.
Output: a title under 60 characters, a 6-line description in friendly
Bangladeshi Bangla with Bangla numerals, and 5 hashtags.
Never invent features that are not in the input.
```
   Add a copy button and a photo grid export.
4. Ask Claude for the instalment reminder SMS set, the Bangla agreement PDF, and a weekly default-risk summary listing buyers who are late.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 dealers live, 200 vehicles in stock |
| Day 60 | 25 dealers, 15 paying, ৳25,000 monthly revenue |
| Day 90 | 70 dealers, 45 paying, ৳80,000 monthly revenue |

### First customers with zero budget
- Facebook groups where dealers post bikes for sale (search "used bike Bangladesh", "bike showroom", "kisti bike").
- Google Maps categories "used motorcycle dealer" and "used car dealer" in Dhaka, Chattogram, Bogura and Cumilla.
- The Bangla Motor and Mirpur showroom clusters; walk in with a phone and a demo.
- The demo that closes: photograph one bike, generate the listing, and show the instalment schedule with reminder dates in two minutes.
- Referral loop: dealers trade stock with each other, so an invited dealer sees the other's listings and joins.

### Pricing and the maths
- Starter ৳999/month for up to 50 vehicles; Showroom ৳1,999 for up to 200; Group ৳2,999 for unlimited vehicles and branches.
- Cost of goods is SMS reminders, image storage and small AI calls. Gross margin is roughly 85 percent.
- About 150 paying dealers at the ৳1,999 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria or Kenya, where boda and okada bikes are sold on instalments by thousands of small dealers.
- What changes: language pack, M-Pesa or Paystack, the transfer document checklist, listing platforms (Jiji).
- What stays: stock register, instalment ledger, reminder engine, listing generator.
- Reseller: motorcycle brand distributors and microfinance lenders who fund bike purchases.

### Risks and how to de-risk them
- Risk: dealers fear digital records of cash sales. De-risk: sell the instalment reminder and papers checklist, not accounting.
- Risk: Facebook changes posting rules. De-risk: generate text and photos for copy-paste, not automated posting.
- Risk: buyers change numbers and disappear. De-risk: capture guarantor and NID at sale and remind both.
- Risk: dealers stall on price. De-risk: a free plan for 10 vehicles and paid plans from the first instalment sale.

## Idea 62: Easy-Bike Charging Garage Ledger
*Garages that charge easy-bikes and battery rickshaws overnight manage slots, monthly subscriptions, battery swaps and driver dues, and see their electricity cost per slot.*

### Who pays and why now
The customer is a charging garage owner with 20 to 150 charging points, usually a converted shed or plot on the edge of an upazila town or a Dhaka suburb. Drivers park each evening, plug in, and pay a nightly or monthly fee. The owner tracks who paid on a whiteboard, buys batteries on credit for some drivers and pays a large electricity bill without knowing which slot earns what.

They will pay because dues and electricity are the whole business. Unpaid nights, drivers who leave with a garage-financed battery, and slots that draw power without paying all come out of a thin margin. Electric three-wheelers are multiplying fast and regulators are pushing to register vehicles and garages, so a proper record is becoming a licence to operate. Ports: India (e-rickshaw), Nepal, Pakistan and Nigeria are on the same electrification curve.

### The product in 30 days (MVP)
- Slot map showing tonight's occupancy with driver and vehicle per slot.
- Driver register with phone, vehicle, battery set ID and subscription type.
- Monthly subscriptions and per-night charging, paid by bKash or cash, with a dues list.
- Battery record: purchase date, owner (driver, garage or financed), swaps and warranty.
- Electricity meter readings and cost per slot per month.
- Daily SMS to the owner: slots used, cash collected, dues outstanding.
- Leave out: smart meter hardware, a driver app, battery financing products, GPS.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant APIs for subscriptions; many drivers pay cash, so a fast cash entry matters more than the API.
- Bangla SMS receipts to drivers with Bangla numerals, one per payment.
- Offline-capable Flutter app, since garages are often in low-signal areas and the busiest hour is evening check-in.
- A simple electricity tariff table so cost per slot follows the local unit rate the owner enters.
- Battery brands and typical warranty months as a seed list for the swap record.

### Build it with Claude
Stack: Flutter for Android, Laravel API, PostgreSQL, Claude API for summaries and messages, small VPS, bKash merchant API, local SMS gateway.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for an easy-bike charging garage in Bangladesh.
Tables: garages, slots, drivers (phone, vehicle_no, subscription_type),
batteries (set_id, owner_type driver/garage/financed, purchased_at,
warranty_months), check_ins (slot, driver, date, fee, paid, method),
payments, meter_readings (date, units, unit_rate). Add a view for
electricity cost per slot per month. Output Laravel migrations.
```
   Apply it and load one garage's drivers from their whiteboard.
2. Ask Claude for the evening check-in screen: tap a slot, pick a driver from recent ones, mark paid or due, all in under three taps, working offline.
3. Add the owner summary and dues chase. Paste this:
```
Given today's garage data (slots used, cash and bKash collected, drivers
with dues over 3 nights, meter units used), write two things in Bangla
with Bangla numerals: a 4-line owner summary, and one polite SMS under
70 characters reminding a driver of dues with the amount and garage name.
No greetings, no emoji.
```
   Schedule the summary for 11pm and the driver SMS for the next morning.
4. Ask Claude for the battery swap screen, the monthly subscription renewal flow, and a Bangla flyer for the garage wall explaining bKash payment.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 garages live, 500 drivers registered |
| Day 60 | 60 garages, 35 paying, ৳20,000 monthly revenue |
| Day 90 | 200 garages, 130 paying, ৳80,000 monthly revenue |

### First customers with zero budget
- Easy-bike driver and owner associations in upazila towns; the garage owners sit on the same committees.
- Facebook groups for easy-bike and battery rickshaw owners (search "ইজিবাইক", "ব্যাটারি রিকশা গ্যারেজ").
- Battery shops and brand distributors, who know every garage that buys batteries on credit.
- The demo that closes: enter tonight's check-ins live at the garage and hand the owner a dues list before he closes.
- Referral loop: a free month for each garage referred, and a printed dues board with your name and number.

### Pricing and the maths
- Basic ৳299/month for up to 30 slots; Standard ৳599 for up to 100; Pro ৳999 for unlimited slots and branches.
- Cost of goods is SMS receipts and one VPS; keep SMS to one per payment. Gross margin is roughly 80 percent.
- About 460 paying garages at the ৳649 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where e-rickshaw charging garages in Uttar Pradesh, Bihar and West Bengal are counted in tens of thousands and West Bengal needs no translation.
- What changes: UPI instead of bKash, Hindi language pack after West Bengal, tariff table, battery brand list.
- What stays: slot map, check-in flow, battery records, dues engine.
- Reseller: battery manufacturers and e-rickshaw dealers who finance batteries.

### Risks and how to de-risk them
- Risk: owners are informal and fear records. De-risk: keep data on their own account and sell dues recovery, not compliance.
- Risk: very low price and small garages. De-risk: target garages above 50 slots and add battery finance tracking as a paid feature.
- Risk: the evening rush makes entry slow. De-risk: recent-driver shortcuts and a one-tap repeat of yesterday's check-in.
- Risk: policy changes on three-wheelers. De-risk: the same ledger serves registered fleets and formal charging hubs.

## Idea 71: Filling Station Manager
*Fuel stations record shift sales by pump, tank dips and stock, credit customers, bKash and card settlements and staffing, replacing the register book.*

### Who pays and why now
The customer is a petrol pump owner running one to five stations, franchised under Padma, Meghna or Jamuna or independent. Each shift ends with meter readings written in a register, cash counted by hand, and credit slips for transport companies stuffed in a drawer. Stock is checked with a dip stick and rarely reconciled against sales, so a leaking tank or a light-fingered attendant goes unnoticed for weeks.

Owners will pay because the numbers are large. A one percent unexplained variance on a busy station is a serious monthly loss, and credit customers who dispute slips are a constant fight. Card and bKash payments now sit alongside cash, making manual reconciliation harder every year. Ports: Nigeria, Pakistan, Indonesia, Egypt and Kenya all have thousands of stations on paper registers.

### The product in 30 days (MVP)
- Pumps and nozzles with opening and closing meter readings per shift; litres and value computed automatically.
- Tank dip entry and stock reconciliation against sales and deliveries, showing variance.
- Credit customers: slip per fill with vehicle number, monthly statement, bKash payment link.
- Shift cash-up: cash, bKash and card totals against expected, with shortage per attendant.
- Fuel delivery receipts and price changes with effective date and time.
- Owner daily summary by WhatsApp.
- Leave out: pump controller integration, lubricant shop POS, loyalty programme, accounting sync.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for credit customer payments; card settlement totals entered from the POS terminal report.
- WhatsApp Business API for owner summaries and credit statements; SMS fallback.
- Government fuel price changes are national, so a shared price table updates every station at the same time.
- Credit statements in Bangla with Bangla numerals, printable for transport company accounts.
- A tablet PWA at the cashier desk that works offline during the shift and syncs at cash-up.

### Build it with Claude
Stack: Next.js PWA on an Android tablet, PostgreSQL, Claude API for register import and anomaly summaries, small VPS, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a fuel station manager in Bangladesh.
Tables: stations, tanks (product, capacity), pumps, nozzles (tank),
shifts (station, start, end, cashier), meter_readings (nozzle, shift,
opening, closing), dips (tank, shift, litres), deliveries, prices
(product, rate, effective_from), credit_customers, credit_slips,
payments, staff. Add a view for variance per tank per shift.
```
   Apply it and set up one station with its real pumps and tanks.
2. Ask Claude for the shift screen: nozzle readings in a grid, dips, cash-up, and a credit slip form with vehicle number lookup.
3. Import the old register. Paste this:
```
This photo is a page from a handwritten Bangla fuel station shift register.
Extract JSON: {date, shift, nozzles: [{name, opening, closing}],
cash_bdt, credit_bdt, notes}. Convert Bangla numerals to digits.
Flag any nozzle where closing is less than opening.
```
   Use it to load the last month so the owner sees trends from day one.
4. Ask Claude for the nightly WhatsApp summary that flags variance above a threshold, shortages by attendant and credit customers over their limit, in plain Bangla.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 stations live, 60 shifts recorded |
| Day 60 | 10 stations, 6 paying, ৳20,000 monthly revenue |
| Day 90 | 35 stations, 25 paying, ৳80,000 monthly revenue |

### First customers with zero budget
- The petrol pump owners association and its district chapters; one presentation reaches dozens of owners.
- Google Maps category "gas station" along the Dhaka to Chattogram and Dhaka to Sylhet highways, where credit customers are transport companies.
- Facebook groups for filling station owners and dealers of the state oil companies.
- The demo that closes: enter one shift's readings from their register and show the variance against the dip in front of the owner.
- Referral loop: transport companies with credit at several stations ask the other stations for the same statement.

### Pricing and the maths
- Single ৳1,499/month for one station; Multi ৳2,999 for up to 3; Group ৳4,999 for up to 10 stations.
- Cost of goods is WhatsApp messages, a few AI calls per day and hosting. Gross margin is roughly 85 percent.
- About 90 paying station groups at the ৳3,249 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria, where independent stations are numerous and mobile payments are common.
- What changes: language pack (English first, then Hausa or Yoruba), Paystack, product list, price update rules.
- What stays: shift and variance engine, credit ledger, cash-up, summary generator.
- Reseller: independent marketers associations and fuel distributors.

### Risks and how to de-risk them
- Risk: attendants resist because variance exposes them. De-risk: sell to owners and frame it as protection for honest staff.
- Risk: owners want pump automation. De-risk: stay manual entry now and add controller integration when a partner appears.
- Risk: state oil company rolls out its own system. De-risk: target independent and franchise stations and keep credit customers as your edge.
- Risk: a 24-hour operation needs zero downtime. De-risk: the offline-first PWA keeps working when the server or internet is down.

## Idea 73: Launch and River Cargo Operator OS
*Launch and trawler operators sell tickets and cabins via bKash, keep cargo manifests, settle every trip and pay crew from one app.*

### Who pays and why now
The customer is a launch owner running the Sadarghat routes to Barishal, Bhola, Patuakhali or Chandpur, or a cargo trawler operator carrying goods between Khulna, Chandpur and Dhaka. Cabins are booked by phone through a supervisor with a notebook. Deck tickets are sold at the ghat with paper. Cargo is listed on a handwritten manifest that the consignee argues with on arrival.

Owners will pay because a launch trip is a large cash event with many hands in it. Cabins sold off the book, freight collected and not reported, fuel and ghat fees inflated: each trip leaks. A system that records every cabin, every ticket and every manifest line against a bKash transaction or a named cash collector gives the owner control from the shore. Passengers already pay by bKash, and river operators have almost no software competition. Ports: Indonesia, the Philippines, Nigeria, Myanmar and the Amazon countries all run passenger and cargo vessels on paper.

### The product in 30 days (MVP)
- Vessels with deck classes and a cabin map (single, double, VIP), and trips by date.
- Cabin and deck ticket sales with bKash or cash, and an SMS ticket in Bangla.
- Cargo manifest: consignor, consignee, item, count or weight, freight, paid or to pay.
- Trip settlement: fares plus freight, fuel, ghat fees, crew wages, net to owner.
- Crew register with wage rates and advances.
- Owner dashboard per vessel and per trip.
- Leave out: public online booking, GPS vessel tracking, insurance, port authority filings.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for cabin bookings by phone, sending the passenger a payment link and then an SMS ticket.
- Bangla SMS tickets and manifest confirmations with Bangla numerals; consignees receive an arrival SMS.
- Offline-first Flutter app for the supervisor on board, syncing at each ghat with signal.
- A seed list of ghats and typical ghat fees per route; BIWTA rules are entered by the operator as needed.
- Manifest PDF in Bangla that doubles as the consignee's delivery challan.

### Build it with Claude
Stack: Next.js for owner and office, Flutter for the on-board supervisor, PostgreSQL, Claude API for manifest capture and summaries, small VPS, bKash merchant API, local SMS gateway.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a river launch and cargo operator in
Bangladesh. Tables: operators, vessels (cabin_map JSON, deck_classes),
routes, trips, tickets (trip, cabin_or_deck, passenger, phone, fare,
method, trx_id, sold_by), manifest_lines (trip, consignor, consignee,
item, qty, weight_kg, freight, paid_status), trip_expenses, crew,
crew_payments. Add a settlement view per trip. Output Prisma schema.
```
   Apply it and load one vessel's real cabin layout.
2. Ask Claude for the cabin booking screen for the office phone operator and the deck ticket screen for the ghat, both with bKash link sending.
3. Add manifest capture. Paste this:
```
The supervisor sends a photo or a Bangla voice transcript of today's
cargo list. Return JSON manifest lines: [{consignor, consignee, phone,
item, qty, weight_kg, freight_bdt, paid_status paid/to_pay}].
Convert Bangla numerals to digits and keep item names in Bangla.
Mark uncertain lines with "check": true.
```
   Show the lines for review and then print the Bangla manifest PDF.
4. Ask Claude for the settlement screen, the crew wage sheet, and a nightly Bangla WhatsApp summary that flags cabins used but not ticketed.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 1 launch operator live, 30 trips recorded |
| Day 60 | 5 operators, ৳20,000 monthly revenue |
| Day 90 | 15 operators, 40 vessels, ৳90,000 monthly revenue |

### First customers with zero budget
- The launch owners association at Sadarghat and the cargo trawler associations in Chandpur and Khulna.
- Facebook groups for launch enthusiasts and river route passengers, where operator staff and owners are active daily.
- Ghat supervisors and booking agents, who know which owners are losing money.
- The demo that closes: book one cabin by phone with a bKash link and show the owner the seat map filling live on his phone.
- Referral loop: operators on the same route share ghats, so one visible launch brings the neighbours.

### Pricing and the maths
- Single ৳2,999/month for one vessel; Fleet ৳5,999 for up to 3; Line ৳9,999 for up to 10 vessels.
- Cost of goods is SMS tickets and hosting; AI manifest calls are small. Gross margin is roughly 80 percent.
- About 45 to 50 paying operators at the ৳6,499 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia, with thousands of inter-island ferries and cargo boats run by small operators and mobile payment everywhere.
- What changes: Bahasa language pack, payment rail (GoPay, OVO or bank transfer), port fee lists, vessel classes.
- What stays: cabin map, ticketing, manifest engine, settlement and crew logic.
- Reseller: port agents and ferry operator associations.

### Risks and how to de-risk them
- Risk: supervisors resist because leakage is exposed. De-risk: sell to the owner and offer supervisors a commission on ticketed sales.
- Risk: no signal mid-river. De-risk: offline-first app that syncs at every ghat.
- Risk: seasonal demand swings. De-risk: price per vessel per month with a pause option in the lean season.
- Risk: cargo disputes still happen. De-risk: the consignee gets a manifest SMS when goods are loaded, not on arrival.

## Idea 75: Truck and Goods Transport Agency OS
*Transport agencies book loads, match them to truck owners, issue Bangla challans and consignment notes, and track advances, balances and their own commission.*

### Who pays and why now
The customer is a goods transport agency: the brokers at Tejgaon truck stand, Khatunganj in Chattogram, Bogura and Jashore, who match a shipper's load to a truck owner's vehicle by phone and take a commission. Their records are a slip pad and a phone contact list. When a shipper disputes freight or a truck owner claims an unpaid balance, nobody has the paper.

They will pay because every load has three payments and one commission to track, and mistakes come out of the agency's pocket. A challan that prints in Bangla with the right copies, and a ledger that shows the advance from the shipper, the advance to the owner and the balance due on delivery, replaces a whole notebook. Shippers now expect a WhatsApp update when the truck loads and arrives. Ports: India, Pakistan, Nigeria, Kenya and Indonesia have the same broker-driven trucking.

### The product in 30 days (MVP)
- Load booking: shipper, origin, destination, goods, weight, truck type, freight, loading date.
- Truck owner and driver directory with truck types and preferred routes; match and confirm by call or WhatsApp.
- Bangla challan and consignment note PDF with copies for shipper, driver and agency.
- Payments: shipper advance, owner advance, balance on delivery, agency commission computed.
- Driver updates by WhatsApp or SMS: loaded, on the way, delivered.
- Ledger per shipper and per truck owner with balances.
- Leave out: live GPS, a public marketplace app, insurance, fuel cards.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for shipper advances and balances; large shippers pay by bank transfer, so record that too.
- WhatsApp Business API for load confirmations and driver status; SMS fallback for drivers on feature phones.
- Challan in Bangla with Bangla numerals, truck number, goods and both parties' phones, printable on A5.
- A seed list of standard truck types (1 ton pickup, 3 ton, 5 ton, covered van, trailer) and major routes.
- Works on the agency's Android phone as a PWA; most agencies have no computer.

### Build it with Claude
Stack: Laravel web app as a PWA, PostgreSQL, Claude API for booking capture and documents, small VPS, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema. Paste this:
```
Design a PostgreSQL schema for a goods transport agency in Bangladesh.
Tables: agencies, shippers, truck_owners, trucks (reg_no, type), drivers,
loads (shipper, origin, destination, goods, weight_kg, truck_type,
freight, loading_date, status), assignments (load, truck, driver,
owner_rate, commission), payments (load, party, direction, amount, method),
status_updates. Add a balance view per shipper and per owner.
```
   Apply it and load the agency's regular shippers and truck owners.
2. Ask Claude for the booking screen, the matching list filtered by truck type and route, and the payments panel on one load page.
3. Turn WhatsApp requests into bookings. Paste this:
```
A shipper sent this WhatsApp message in Bangla or English asking for a
truck. Return JSON: {origin, destination, goods, weight_kg, truck_type,
loading_date, notes, missing_fields}. Convert Bangla numerals to digits
and Bangla place names to standard spelling. List anything not stated
in missing_fields so the agent can ask.
```
   Pre-fill the booking form and let the agent confirm.
4. Ask Claude for the Bangla challan template, the driver status messages, and a monthly commission report per agent.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 agencies live, 150 loads booked |
| Day 60 | 15 agencies, 8 paying, ৳30,000 monthly revenue |
| Day 90 | 40 agencies, 25 paying, ৳1,00,000 monthly revenue |

### First customers with zero budget
- Truck stand committees at Tejgaon, Gabtoli and Khatunganj, and the district truck owner associations.
- Facebook groups where loads and trucks are posted daily (search "ট্রাক ভাড়া", "truck rent Bangladesh", "covered van").
- Google Maps category "trucking company" and "transport agency" in Dhaka, Chattogram and Bogura.
- The demo that closes: take a live load from their phone, generate the Bangla challan and send the shipper a WhatsApp confirmation in one minute.
- Referral loop: truck owners work with several agencies and ask the others for the same challan and payment record.

### Pricing and the maths
- Starter ৳1,999/month for up to 100 loads; Agency ৳3,999 for up to 500; Network ৳7,999 for unlimited loads and branches.
- Cost of goods is WhatsApp conversations and hosting, with small AI calls per booking. Gross margin is roughly 80 percent.
- About 60 paying agencies at the ৳4,999 mid price make roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya or Nigeria, where transport brokers match loads by phone and mobile money is universal.
- What changes: language pack, M-Pesa or Paystack, truck type list, waybill format and tax rules.
- What stays: load booking, matching, three-payment ledger, commission engine, status messages.
- Reseller: truck owner associations and freight forwarders who want organised sub-brokers.

### Risks and how to de-risk them
- Risk: agencies fear that recording deals exposes commission. De-risk: keep commission visible only to the agency and never to owners or shippers.
- Risk: drivers do not send updates. De-risk: a one-tap SMS reply and a call-back log the agent can fill.
- Risk: a funded load-matching marketplace enters. De-risk: you serve the agencies the marketplace tries to bypass, and their relationships are the moat.
- Risk: non-payment disputes still land on the agency. De-risk: the signed challan and payment record become the evidence.


---

# Section 11: Religion and Community

Bangladesh runs on institutions that nobody counts as businesses: mosques, madrasas, savings groups, orphanages, matchmakers, clubs and election campaigns. Each one moves money and trust every week, almost always on paper, and that gap is what these seven ideas fill.

## Idea 11: Mosque, Madrasa and Community Fund Manager
*Monthly chanda, zakat and donation receipts, with transparent Bangla reports donors can trust.*

### Who pays and why now
The customer is the mosque committee, the madrasa treasurer, or the community fund that pays for a graveyard or an Eid distribution. Around 300,000 mosques and committees collect monthly chanda door to door, write it in a notebook, and read totals aloud after Friday prayers.

Donors are the hidden buyer. A committee that shows a clean monthly report collects more and argues less. Committees change every few years and the notebook often leaves with the old treasurer. Digital records survive the handover.

The moment is right because bKash and Nagad sit in every donor's pocket, and remittance families want to give to the village mosque from Dubai without routing cash through a cousin. The same pattern ports to Urdu, Indonesian, Malay, Arabic, Turkish and Swahili communities.

### The product in 30 days (MVP)
- Institution profile with committee members, roles and an expense approval chain.
- Donor list with monthly chanda amount, lane, and collector assignment.
- Collection entry from a phone, source cash, bKash or Nagad, with a Bangla SMS receipt.
- Separate funds for zakat, sadaqah, general and projects, so restricted money stays restricted.
- Expense entry with a voucher photo and two-person approval.
- One-tap monthly report as PDF and a shareable Bangla web page.
- Leave out: staff payroll, event management, asset inventory, a donor mobile app.

### Data, integrations and the Bangladesh specifics
- Payment rail: bKash merchant API for online donations plus manual cash entry. Add Nagad after the first 50 institutions.
- Bangla SMS receipts through a local gateway; keep each receipt inside one segment.
- Report layout: opening balance, collections by fund, expenses by head, closing balance, in Bangla numerals with the Hijri date.
- Offline collection: entries queue on the phone and sync later, because lanes have weak signal.
- Zakat cannot pay the electricity bill. The product enforces fund walls and prints them on the report.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Flutter Android app for collectors, Claude API for report narration, Cloudflare plus a small VPS, bKash merchant API.

1. Ask Claude for the schema. Paste this, review the tables, then ask for the Prisma migration.
```
Design a PostgreSQL schema for a mosque and community fund manager.
Entities: institution, committee_member (role, approval rights), donor,
pledge (monthly amount, fund), collection (amount, source cash/bKash/Nagad,
collector, synced_at), fund (zakat, sadaqah, general, project),
expense (head, voucher_photo_url, approver_1, approver_2).
Add constraints so an expense can only draw from an allowed fund.
```
2. Ask Claude to build the collector Flutter screens: donor list by lane, one-tap collection, offline queue with sync status. Test with mobile data turned off.
3. Ask Claude for the report generator, then check the output with a real treasurer.
```
Write a Node.js function that takes one month of collections and expenses
for an institution and returns a Bangla report as HTML for PDF export.
Sections: opening balance, collections by fund, expenses by head,
closing balance, top 10 donors by consent. Use Bangla numerals (০-৯),
Bangla month names and the Hijri month. Tone: formal, for reading aloud
after Jummah. Then add a 3-sentence Bangla summary written by Claude API.
```
4. Ask Claude for the bKash integration: a donation link per institution and a webhook that records the collection and sends the receipt.
5. Ask Claude for onboarding: the treasurer uploads a photo of the notebook and Claude reads it into rows for review.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 10 institutions live in one upazila, 500 donors recorded |
| Day 60 | 60 institutions, 20 paying, first diaspora online donations |
| Day 90 | 150 institutions, 80 paying, roughly ৳40,000 monthly revenue |

### First customers with zero budget
- Start with the mosque you attend. Run one monthly report for free and read it out after Jummah with the treasurer.
- Upazila-level imam and madrasa associations meet monthly. Ask for ten minutes to show the report page.
- Facebook groups for village committees and "আমাদের গ্রাম" pages, where remittance donors already ask for accounts.
- Outreach angle: "Your donors see where every taka went, every month." Send a real report with names hidden.
- The demo that closes: type in last month's notebook live and produce the report in five minutes.
- Referral loop: every public report carries a footer, "Set up your own for free". Committees copy neighbouring committees.

### Pricing and the maths
- ৳299 to ৳999 per month per institution, by donor count. Free up to 50 donors.
- Costs are SMS receipts, hosting and a small Claude API bill; gross margin is roughly 75 to 85 percent when SMS is capped per plan.
- At a mid price of about ৳649, roughly 460 paying institutions bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia. The largest Muslim population, committee-run mosques, wallets such as GoPay and OVO.
- What changes: Bahasa language pack, payment rail, calendar labels, a reseller inside the mosque association network.
- What stays the same: fund walls, the collector app, the monthly report, the approval chain.
- Diaspora mosques in the UK and the Gulf can pay through Stripe from day one.

### Risks and how to de-risk them
- Risk: committees fear digital records invite scrutiny. De-risk: publishing is optional; start with the treasurer's private view.
- Risk: low willingness to pay. De-risk: keep a free tier and let the institution pay under a visible "software" expense head.
- Risk: SMS cost eats margin at ৳299. De-risk: cap SMS per plan and use WhatsApp receipts where donors have it.
- Risk: sensitivity over zakat handling. De-risk: consult a local alim on fund rules and print the rule on the report.

## Idea 14: Hajj and Umrah Agency OS
*Packages, pilgrim documents, bKash instalments and group broadcasts for agencies that still run on Excel.*

### Who pays and why now
The customer is a licensed hajj agency or an umrah operator, usually a family business in Dhaka, Chattogram or Sylhet with two to ten staff. Bangladesh sends over 100,000 hajj pilgrims a year plus a larger, year-round umrah flow. Each pilgrim means a passport, medical and vaccine papers, a visa, instalments, and a family that calls daily for news.

Agencies keep all this in Excel, WhatsApp and a cupboard of files. An expired passport surfaces two weeks before departure and becomes a crisis. Owners will pay because one lost pilgrim costs more than a year of software, and ministry deadlines do not move.

The moment is right because the ministry and Saudi portals now demand digital data, and pilgrims expect WhatsApp updates. The workflow ports to Indonesia, Pakistan, Malaysia, Nigeria, Turkey and India.

### The product in 30 days (MVP)
- Package builder: dates, hotel grade, flight, inclusions, price, and seat count.
- Pilgrim file: personal details, passport scan, medical and vaccine status, mahram link, group assignment.
- Document checklist per pilgrim with expiry alerts and a colour status board.
- Instalment schedule with bKash payment links, receipts in Bangla, and overdue reminders.
- Group WhatsApp broadcast for departure times, room lists and training sessions.
- Pre-departure training library: short Bangla videos and PDFs, with a viewed tick per pilgrim.
- Leave out: accounting, hotel and airline booking integrations, Saudi portal automation, a pilgrim mobile app.

### Data, integrations and the Bangladesh specifics
- Payment rail: bKash merchant API for instalments, SSLCommerz for card payments from relatives abroad, and manual entry for bank transfers.
- WhatsApp Business API for broadcasts and status updates; SMS fallback in Bangla for older pilgrims.
- Store the ministry pre-registration ID and the Saudi Nusuk reference per pilgrim as plain fields copied from the portals.
- Passport reading: Claude reads the scanned page into name, number and expiry; a staff member confirms.
- Bangla PDFs for receipts, room lists and departure letters, with Bangla numerals and Hijri dates.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Claude API for document reading and Bangla messaging, WhatsApp Business API, bKash merchant API, small VPS.

1. Ask Claude for the domain model and migrations: agency, package, pilgrim, document, instalment, payment, group, broadcast. Ask it to mark sensitive fields for encryption.
2. Ask Claude to build the pilgrim status board. Paste this and refine with the agency owner.
```
Build a Laravel Blade page "Pilgrim Board" for a hajj agency.
Rows: pilgrims in a package. Columns: passport (valid/expiring/missing),
medical, vaccine, visa, instalments paid vs due, training viewed.
Each cell is red, amber or green. Filter by package and group.
Labels in Bangla with English tooltips. Add a "send reminder" button
per red cell that queues a Bangla WhatsApp message.
```
3. Ask Claude for the instalment engine: schedule generation, bKash payment link per instalment, webhook to mark paid, Bangla receipt PDF, reminder three days before due.
4. Ask Claude to write the passport reader: send the scanned image to Claude API, get structured JSON, show a confirm screen.
5. Ask Claude for the broadcast templates.
```
Write 6 WhatsApp message templates in Bangla for a hajj agency:
instalment reminder, document missing, training session invite,
departure time and meeting point, room allocation, safe arrival notice.
Under 300 characters each, respectful tone, placeholders like {name},
{amount}, {date}. Return as JSON with a key for each template.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 agencies live with one umrah group each, 100 pilgrims on the board |
| Day 60 | 12 agencies, 6 paying, first bKash instalments collected through the system |
| Day 90 | 30 agencies, 20 paying, roughly ৳1 lakh monthly revenue before hajj season |

### First customers with zero budget
- The hajj agency association (HAAB) has a member list; its Dhaka office and district committees are where owners gather.
- Facebook groups for umrah packages are full of agency posts; comment with a demo video and message the page admins.
- Travel agency clusters in Naya Paltan, Fakirapool and Motijheel; visit with a laptop.
- Outreach angle: "See every pilgrim's passport, visa and payment status on one screen before the ministry deadline."
- The demo that closes: load one real umrah group from the agency's Excel file and show the red cells.
- Referral loop: sub-agents in districts feed pilgrims to Dhaka agencies; give them a free view of their own pilgrims.

### Pricing and the maths
- ৳2,999 to ৳9,999 per month per agency, by pilgrim count and staff seats. Umrah-only agencies start at the low end.
- Costs are WhatsApp conversation fees, hosting, and a modest Claude API bill for document reading; gross margin is roughly 80 percent.
- At a mid price of about ৳6,499, roughly 46 paying agencies bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia, the largest hajj quota in the world and a long umrah queue, with thousands of licensed travel agencies.
- What changes: Bahasa language pack, payment rail such as GoPay or bank virtual accounts, the local ministry's registration fields, and a reseller with agency association ties.
- What stays the same: the pilgrim board, document checklist, instalment engine, broadcast templates.
- Seasonal lock-in is universal: once a season's pilgrims are loaded, the agency stays.

### Risks and how to de-risk them
- Risk: agencies fear regulators seeing their data. De-risk: no data sharing, clear terms, and named hosting.
- Risk: seasonality makes revenue lumpy. De-risk: umrah runs all year, and annual plans paid before hajj smooth the cash.
- Risk: WhatsApp verification delays. De-risk: start with SMS and the agency's own WhatsApp, then migrate.
- Risk: passport data breach. De-risk: encrypt at rest, restrict downloads, and log every view.

## Idea 16: Samity and Savings-Group App
*Weekly collections, digital passbooks, SMS receipts and defaulter lists for groups that still trust a notebook.*

### Who pays and why now
The customer is a samity, a rotating savings group, a village cooperative or a small NGO branch. Tens of thousands of them collect cash every week. An officer walks door to door, writes the amount in a notebook, and members keep a paper passbook. A disputed entry can split a group.

The payer is the NGO branch or the group itself, from fees it already collects. They pay for fewer disputes, a defaulter list every Monday morning, and proof for auditors and donors. Officers spend hours totalling notebooks and will use anything that ends that.

The moment is right because every member has a phone that receives SMS, and bKash lets members working in Dhaka keep paying into the village group. The same groups exist as self-help groups in India, chama in Kenya, arisan in Indonesia, paluwagan in the Philippines and committee in Pakistan.

### The product in 30 days (MVP)
- Group setup: members, weekly amount, meeting day, officer, cycle rules for rotating payouts.
- Officer collection screen: member list, tap to collect, partial payments, offline queue.
- Digital passbook per member with balance, and a Bangla SMS receipt after every collection.
- Rotating payout schedule and draw record; loan ledger for savings-and-credit groups.
- Defaulter list by group and by officer, with weeks missed and amount due.
- Weekly branch summary in Bangla for the manager, exportable to Excel.
- Leave out: full accounting, loan interest engines with many products, member self-service app, credit scoring.

### Data, integrations and the Bangladesh specifics
- Payment rail: cash is primary. bKash merchant API for members paying remotely, mapped to the member by phone number.
- Bangla SMS receipts through a local gateway; one segment each, batched at day end to cut cost.
- Offline first: villages have no signal, so the Flutter app stores entries and syncs later with conflict rules.
- Bangla numerals and Bangla dates on passbook printouts, because members compare with the old paper book.
- For NGO branches, follow Microcredit Regulatory Authority reporting language so the summary maps onto existing forms.

### Build it with Claude
Stack: Flutter Android app for officers, Laravel API, PostgreSQL, Claude API for weekly narrative summaries, SMS gateway, bKash merchant API, small VPS.

1. Ask Claude for the schema and the sync design.
```
Design a PostgreSQL schema and an offline sync protocol for a savings
group app. Entities: branch, officer, group (weekly_amount, meeting_day,
type: rosca or savings_credit), member, collection (amount, week_no,
collected_at, device_id, synced_at), payout, loan, repayment.
Each collection must be idempotent by (member_id, week_no, device_id).
Describe how the Flutter client queues and resolves conflicts.
```
2. Ask Claude to build the officer's collection screen: today's groups, tap-to-collect, partial amount, a big total, a sync indicator.
3. Ask Claude for the defaulter engine and the SMS receipt text in Bangla, then test with a real group's numbers.
```
Write a SQL view "defaulters" that lists, per member, weeks missed in
the current cycle, amount due, and last payment date.
Then write a Bangla SMS receipt template under 160 characters:
member name, amount received, week number, new balance, group name.
Use Bangla numerals for numbers. Return both.
```
4. Ask Claude for the passbook PDF and the weekly branch summary, and to add a three-sentence Bangla narrative using Claude API.
5. Ask Claude to write the bKash webhook that matches a remote payment to a member by phone and posts the collection.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 groups in one union running weekly collections, 150 members receiving SMS |
| Day 60 | 40 groups across 2 NGO branches, first paying branch |
| Day 90 | 150 groups, 100 paying, roughly ৳35,000 monthly revenue |

### First customers with zero budget
- Small NGOs and cooperatives in your district; branch managers are listed on the Microcredit Regulatory Authority website and on signboards.
- Women's samity leaders gather at union parishad meetings and NGO training days. Ask for a ten-minute demo.
- Facebook groups for microfinance field officers, where they complain about notebook totals every week.
- Outreach angle: "Your Monday defaulter list, ready before you reach the office."
- The demo that closes: run one real weekly collection on the phone and show the member the SMS on her own handset.
- Referral loop: members who receive SMS ask their other groups for the same thing.

### Pricing and the maths
- ৳199 to ৳499 per month per group, or a branch plan by number of groups.
- Costs are SMS, hosting and a small Claude API bill; gross margin is roughly 70 to 80 percent because SMS volume per group is fixed and small.
- At a mid price of about ৳349, roughly 860 paying groups bring in ৳3 lakh a month; branch plans get there with fewer customers.

### Country kit: taking it to other languages
- First port: Kenya. Chama groups are numerous, M-Pesa is universal, and remote payments are already the norm.
- What changes: Swahili and English language pack, M-Pesa integration instead of bKash, local regulator report formats, a reseller among SACCO networks.
- What stays the same: the officer app, offline sync, passbook, defaulter list.
- India follows with self-help groups by state language and UPI collections.

### Risks and how to de-risk them
- Risk: officers keep the notebook too and the app becomes double work. De-risk: print the passbook from the app so the paper comes from the system.
- Risk: sync conflicts create wrong balances. De-risk: idempotent entries, an audit log, and a manager correction flow with reasons.
- Risk: groups will not pay. De-risk: sell to the NGO branch, which already has a software line, and price per branch.
- Risk: regulatory sensitivity around microcredit. De-risk: position as record keeping, not lending.

## Idea 61: Orphanage and Child Sponsorship Manager
*Child profiles, sponsor matching, monthly photo updates and zakat receipts, with card payments from diaspora donors on day one.*

### Who pays and why now
The customer is an orphanage, an etimkhana attached to a madrasa, or a small child welfare home. Thousands of them are funded by local zakat, monthly sponsors and relatives abroad. The director keeps a register of children, a notebook of donors, and a phone full of WhatsApp promises.

Donors are the reason it sells. A sponsor in London or Riyadh who pays for one child's food and schooling gets nothing back except a call at Eid. Institutions that send a monthly photo and note keep sponsors for years and find new ones through them. The director pays because sponsor retention is the whole budget.

The moment is right because diaspora giving is growing and Stripe card payments are now possible with some setup. The model ports to Pakistan, Indonesia, Nigeria, Turkey and Somalia, with donors in the UK, US and Gulf.

### The product in 30 days (MVP)
- Child profile: photo, age, schooling, health notes, guardian contact, with privacy levels per field.
- Sponsor profile and matching: one sponsor to one or many children, monthly amount, currency.
- Monthly update composer: staff upload a photo and two lines; Claude drafts a Bangla and English note for the sponsor.
- Donations ledger with zakat, sadaqah and general funds, and Bangla or English receipts by email and WhatsApp.
- Stripe checkout page in dollars and pounds, bKash link in taka, recurring monthly for both.
- Expense report to donors: food, education, health, staff, published monthly.
- Leave out: full accounting, volunteer management, school results tracking, a donor mobile app.

### Data, integrations and the Bangladesh specifics
- Payment rails: Stripe for cards abroad, bKash merchant API for local sponsors, SSLCommerz as a second local option. Track the 2 percent card fee share in the ledger.
- WhatsApp Business API for updates and receipts; email for diaspora sponsors who prefer it.
- Child protection: photos never public, sponsors see only their own child, blur options, guardian consent recorded.
- Zakat receipts must state the fund and the Hijri date; use Bangla numerals for local receipts and English for foreign ones.
- Department of Social Services or NGO Affairs Bureau registration numbers appear on every receipt.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for update drafting and translation, Stripe, bKash merchant API, WhatsApp Business API, Cloudflare plus a small VPS.

1. Ask Claude for the schema: institution, child, guardian_consent, sponsor, sponsorship, donation, fund, update, expense, with row-level rules so a sponsor reads only their own children.
2. Ask Claude to build the monthly update composer.
```
Build a Next.js page for orphanage staff to create a monthly sponsor update.
Inputs: child selector, one photo upload, two lines typed in Bangla about
the month (school, health, festivals). Call Claude API to draft a warm,
factual 4-sentence update in Bangla and in English, no exaggeration,
no requests for money. Show both for editing, then queue sending by
WhatsApp and email to that child's sponsors.
```
3. Ask Claude for the Stripe recurring checkout and the bKash link flow, both posting into the same donations table with fund and currency.
4. Ask Claude for the receipt generator.
```
Write a function that renders a donation receipt PDF in two variants.
Bangla variant: Bangla numerals, Hijri and Bangla dates, fund name
(zakat, sadaqah, general), institution registration number.
English variant for foreign donors: amount with currency, date, fund,
a one-line child update if sponsorship-linked. Both under one A5 page.
```
5. Ask Claude to write the public donation page copy in Bangla and English, with the monthly expense report embedded.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 institutions live, 100 children profiled, first monthly updates sent |
| Day 60 | 15 institutions, 8 paying, first Stripe recurring donations from abroad |
| Day 90 | 40 institutions, 25 paying, roughly ৳50,000 monthly revenue plus card fee share |

### First customers with zero budget
- Madrasa and etimkhana Facebook pages that post donation appeals; message the admin with a sample update for one child.
- Diaspora community groups in the UK, US and Gulf that fund homes in their home district; they will push the institution to use it.
- Local zakat committees and mosque committees from Idea 11 know which orphanages they fund.
- Outreach angle: "Your sponsors get a photo and a note every month, and they stop leaving."
- The demo that closes: create one child profile, send one update to the director's own phone, and show the Stripe page in pounds.
- Referral loop: every sponsor update carries the institution's page; sponsors share it in family groups.

### Pricing and the maths
- ৳499 to ৳1,999 per month per institution by child count, plus 2 percent on card donations.
- Costs are Stripe fees passed through, WhatsApp and email, hosting, and a small Claude API bill; gross margin on subscriptions is roughly 80 percent.
- At a mid price of about ৳1,249, roughly 240 paying institutions bring in ৳3 lakh a month, before the card fee share.

### Country kit: taking it to other languages
- First port: Pakistan. Large orphanage sector, strong UK diaspora giving, and Urdu content is easy to add.
- What changes: Urdu language pack, JazzCash or Easypaisa instead of bKash, local charity registration fields, a reseller among welfare trusts.
- What stays the same: child privacy model, sponsor matching, update composer, Stripe flow.
- Turkey and Indonesia follow, both with organised charity networks.

### Risks and how to de-risk them
- Risk: child data misuse. De-risk: consent records, private photos by default, sponsor-only views, and audit logs.
- Risk: institutions cannot open Stripe. De-risk: help with documents, or settle through a partner entity.
- Risk: fake institutions damage trust. De-risk: verify registration and visit or video-call before enabling public pages.
- Risk: WhatsApp templates rejected. De-risk: email as the default channel for foreign donors.

## Idea 70: Election Campaign Manager
*Voter lists by centre, canvassing assignments, polling agent rosters and legal expense tracking, sold per campaign and paid upfront.*

### Who pays and why now
The customer is a candidate for union parishad, municipality, upazila or parliament, or rather the election manager, a trusted relative or party worker who runs the war room. Thousands of candidates stand in each cycle, spend heavily on posters, workers, food and transport, and track it on paper slips and phone calls.

They pay because the campaign is short, the stakes are personal, and money already flows. A system that shows which households were visited, which polling agents are confirmed per centre, and spend against the legal limit costs less than one day's posters. Payment is upfront because the campaign ends on polling day.

The moment is right because voter lists come by centre as PDFs, teams live on WhatsApp, and expense rules are enforced more visibly. The same shape works in India, Pakistan, Nigeria, Indonesia and the Philippines.

### The product in 30 days (MVP)
- Voter list import per centre from PDF or Excel, with area, ward and household grouping.
- Canvassing assignments: workers get a household list, mark visited, supporter, undecided or opposed.
- Polling agent roster per centre and booth, with confirmation status and backup names.
- Expense ledger by head, mapped to the legal limit for the seat type, with receipts by photo.
- Bangla SMS and voice message broadcasts to worker and supporter lists.
- Daily dashboard for the candidate: coverage by centre, agents confirmed, spend versus limit.
- Leave out: social media management, live results, voter data purchase, donor management.

### Data, integrations and the Bangladesh specifics
- Payment rail: bKash or bank transfer for the campaign fee, invoiced upfront; no in-app collections.
- Bangla SMS through a bulk gateway registered with the campaign's identity, and a voice call API for recorded messages.
- Election Commission voter list PDFs are Bangla text or scans; Claude turns pages into rows and a worker checks samples.
- Expense heads and limits follow the Commission's conduct rules per seat type; keep the rule table editable.
- Offline canvassing: workers move through villages; the Flutter app holds the household list and syncs at night.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Flutter Android app for canvassers, Claude API for voter list parsing and message drafting, bulk SMS and voice gateway, small VPS.

1. Ask Claude for the schema: campaign, seat_type, centre, booth, household, voter, worker, assignment, visit, agent_roster, expense, limit_rule, broadcast, with indexes for a fast centre dashboard.
2. Ask Claude to build the voter list importer.
```
Write a pipeline that takes a Bangladesh Election Commission voter list
PDF for one centre (Bangla text or scanned pages) and extracts rows:
serial, name, parent or spouse name, birth year, address, voter number.
Use Claude API for scanned pages. Group voters into households by
address and parent name. Output CSV plus a confidence score per row,
and flag rows below 0.8 for human review.
```
3. Ask Claude for the canvasser Flutter screens: my households today, mark status, note, sync later. Keep it usable with one thumb.
4. Ask Claude for the expense tracker with a running meter against the seat limit and a printable statement in the Commission's format.
5. Ask Claude for the broadcast writer.
```
Write 5 Bangla SMS templates for a union parishad election campaign:
worker meeting call, polling agent confirmation request, voter reminder
with centre name and date, thank-you after polling, and a rain or delay
notice. Respectful, non-inflammatory, under 160 characters, placeholders
{name}, {centre}, {date}, {time}. Return as JSON.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 campaigns live in one upcoming local election, 20,000 voters imported |
| Day 60 | 8 campaigns paid, agent rosters complete for every centre |
| Day 90 | 20 campaigns paid across the cycle, roughly ৳5 lakh total revenue |

### First customers with zero budget
- Party offices and hopefuls gather at tea stalls near the upazila office months before the schedule; go there.
- Facebook pages of aspiring candidates; message the page manager, who is usually the campaign manager.
- Printing presses that make posters know every candidate in town; offer them a referral fee.
- Outreach angle: "Know every centre's agent and every visited household before polling day, and stay inside the expense limit."
- The demo that closes: import one centre's voter list live and show the household map in five minutes.
- Referral loop: campaign managers work several elections; a happy manager brings the next candidate.

### Pricing and the maths
- ৳9,999 to ৳49,999 per campaign, by seat type and voter count, paid upfront.
- Costs are SMS and voice minutes, hosting, and Claude API for parsing; gross margin is roughly 70 percent when SMS is metered and billed on top.
- At a mid price of about ৳29,999, roughly 10 campaigns a month during an election season bring in ৳3 lakh; plan for seasons, not months.

### Country kit: taking it to other languages
- First port: India. Panchayat and municipal elections run every year somewhere, voter lists are public, and campaign spending is large.
- What changes: state language pack, voter list format per state, expense limits per the Election Commission of India, UPI for payment, a reseller in political consulting.
- What stays the same: household canvassing, agent rosters, the spend meter, the daily dashboard.
- Nigeria and the Philippines follow, both with intense local elections.

### Risks and how to de-risk them
- Risk: misuse of voter data. De-risk: use only public lists, no sharing between campaigns, delete data after the election on request.
- Risk: seasonal revenue with long gaps. De-risk: chase local elections across the country and pair with Idea 83 for off-season income.
- Risk: political heat and accusations of bias. De-risk: serve any candidate, publish neutral terms, refuse inflammatory messaging.
- Risk: SMS gateway blocks during elections. De-risk: keep two gateways and a WhatsApp fallback.

## Idea 72: Matrimonial Bureau CRM
*Candidate profiles with privacy controls, family preferences, match shortlists and fee tracking for the town's professional matchmaker.*

### Who pays and why now
The customer is the ghotok, the professional matchmaker with a small office or a Facebook page in every district town and Dhaka neighbourhood. They hold hundreds of candidate files, know each family's preferences by memory, and run the business on WhatsApp photos and a paper register. One photo sent to the wrong family ends a client relationship.

They pay because discretion is the product they sell and every lost file is lost commission. A bureau earns a registration fee and a success fee, and forgets both without a ledger. A tool that finds matching candidates in seconds and shows fees due makes the owner faster and more trusted.

The moment is right because families expect a shortlist on WhatsApp within a day, and matchmaking apps target urban singles while leaving family-led matches to bureaus. The same bureau exists in India, Pakistan, Nigeria, Indonesia and Gulf diaspora communities.

### The product in 30 days (MVP)
- Candidate profile: personal, education, profession, family, religion and sect, location, expectations, photos with a blur toggle.
- Privacy levels per profile: internal only, shareable without photo, shareable with photo on approval.
- Match search with filters and a Claude-ranked shortlist explained in one Bangla line each.
- Shareable profile card as a PDF or link that expires, with a watermark of the bureau.
- Meeting scheduler for family introductions with reminders.
- Fee ledger: registration, monthly, success fee, with dues and bKash links.
- Leave out: a public marketplace, candidate self-signup, video calls, horoscope matching.

### Data, integrations and the Bangladesh specifics
- Payment rail: bKash merchant API for registration and success fees; manual entry for cash.
- WhatsApp Business API for sending profile cards and meeting reminders; the expiring link protects photos.
- Bangla fields for district, upazila, education levels and profession lists so search works with local spellings.
- Photo protection: watermark, no download, expiring links, and a log of who received which profile.
- Bangla numerals and dates on the profile card; families print it and pass it around.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Claude API for shortlist ranking and profile writing, WhatsApp Business API, bKash merchant API, small VPS with private object storage for photos.

1. Ask Claude for the schema: bureau, candidate, family_preference, photo (privacy_level), share_log, match_request, shortlist, meeting, fee, payment. Ask for a share_log that records recipient, time and expiry for every profile sent.
2. Ask Claude to build the profile writer.
```
Write a function that takes structured candidate data (education,
profession, family, location, expectations) and produces a respectful
Bangla profile summary of 5 sentences for a matrimonial bureau, plus an
English version. No superlatives, no assumptions about appearance, no
personal contact details. Return JSON with bangla, english and a
one-line headline for the shortlist card.
```
3. Ask Claude for the match shortlist: a SQL prefilter on hard constraints, then a Claude API call that ranks the top 20 and explains each match in one Bangla line.
4. Ask Claude for the expiring share link and watermark pipeline for profile PDFs and photos.
5. Ask Claude for the outreach and reminder copy.
```
Write Bangla WhatsApp messages for a matrimonial bureau:
1) shortlist ready, with a link that expires in 48 hours,
2) family meeting reminder with date, time and place,
3) success fee reminder after an engagement, polite and firm,
4) a monthly check-in to inactive registered families.
Each under 250 characters, formal address, placeholders in braces.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 bureaus live, 500 candidates loaded, first shortlists sent |
| Day 60 | 15 bureaus, 8 paying, fee ledger in daily use |
| Day 90 | 40 bureaus, 25 paying, roughly ৳50,000 monthly revenue |

### First customers with zero budget
- Facebook pages and groups named "ঘটক", "বিয়ের পাত্র পাত্রী" and district-level marriage media pages; the admins are the bureaus.
- Marriage media offices cluster near community centres; visit with a demo on a phone.
- Kazi offices and wedding vendors from Idea 21 know every active matchmaker.
- Outreach angle: "Send a shortlist in five minutes, never leak a photo, and collect every success fee."
- The demo that closes: load ten of their real profiles, run one match request, and show the expiring link on their own phone.
- Referral loop: bureaus exchange candidates across towns; offer a partner mode where two bureaus share a shortlist.

### Pricing and the maths
- ৳999 to ৳2,999 per month per bureau, by candidate count and staff seats.
- Costs are WhatsApp fees, photo storage, hosting and a modest Claude API bill; gross margin is roughly 80 percent.
- At a mid price of about ৳1,999, roughly 150 paying bureaus bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Family-led matchmaking is the norm, bureaus operate in every city, and Urdu content is straightforward.
- What changes: Urdu language pack, JazzCash or Easypaisa, local caste, sect and community fields, a reseller among wedding service networks.
- What stays the same: privacy model, share log, shortlist engine, fee ledger.
- Gulf diaspora bureaus serving Bangladeshi and Pakistani families pay in dollars through Stripe.

### Risks and how to de-risk them
- Risk: a photo leak destroys trust. De-risk: watermark, expiring links, no downloads, and a share log the bureau can show the family.
- Risk: bureaus fear the software will steal their database. De-risk: export any time, no cross-bureau access without both consenting.
- Risk: AI ranking makes biased suggestions. De-risk: SQL hard filters first, human review of every shortlist, no ranking on appearance.
- Risk: small bureaus will not pay ৳999. De-risk: a starter plan capped at 100 candidates, and success-fee reminders that pay for it.

## Idea 83: Association and Club Membership Manager
*Member directory, dues via bKash, verified elections, notices and event registration for associations that still count votes by hand.*

### Who pays and why now
The customer is the general secretary or treasurer of a trade association, an alumni body, a professional society, a sports club or a district welfare association. Thousands of them collect dues, publish notices, hold an AGM, and every two years run a contested election with paper ballots and arguments over who may vote.

They pay because dues collection is leaky, elections are expensive and disputed, and the secretary changes every term and takes the member list along. Bigger associations spend heavily on printed ballots, venue and polling staff; a verified hybrid vote costs far less. The moment is right because members expect to pay by bKash, read notices on their phone, and register for the reunion with a link. Associations exist everywhere, so the product ports anywhere.

### The product in 30 days (MVP)
- Member directory with categories, membership number, status and a searchable Bangla and English profile.
- Dues invoicing by membership type, bKash payment links, Bangla receipts, and an arrears list.
- Notice board with SMS or WhatsApp push and read receipts for important notices.
- Event registration with ticket types, guest counts and payment.
- Election module: nomination list, eligible voter roll frozen on a date, OTP-verified voting, live count visible to the election commission only.
- Committee and AGM records: minutes, resolutions and attendance.
- Leave out: full accounting, a mobile app, member-to-member chat, sponsorship management.

### Data, integrations and the Bangladesh specifics
- Payment rail: bKash merchant API for dues and event fees, SSLCommerz for card payments from members abroad.
- SMS OTP for voter verification through a local gateway, with WhatsApp as the notice channel.
- Bangla names, addresses and membership numbers in the directory; Bangla numerals on receipts and printed voter rolls.
- Election rules follow the association's constitution: nomination dates, eligibility cut-off, voting window, and a printed audit log for the election commission.
- RJSC or Department of Social Services registration details appear on receipts.

### Build it with Claude
Stack: Next.js web app, PostgreSQL, Claude API for notice drafting and minutes summaries, SMS gateway, bKash merchant API, Cloudflare plus a small VPS.

1. Ask Claude for the schema: association, member, membership_type, invoice, payment, notice, event, registration, election, candidate, voter_roll, ballot, audit_log, with ballots stored apart from voter identity so votes are secret but countable.
2. Ask Claude to build the election module.
```
Build a secret-ballot election module in Next.js and PostgreSQL for
an association. Steps: admin freezes the eligible voter roll, opens a
voting window, voters log in with membership number and SMS OTP, cast
one ballot per post, receive a receipt code. Store ballots without
voter identity, with a hashed receipt. Show a live count only to
election commission roles. Produce a printable Bangla result sheet.
```
3. Ask Claude for the dues engine: yearly invoices by type, bKash links, receipts, arrears list, and a reminder schedule in Bangla.
4. Ask Claude for the notice and minutes assistant.
```
Write two Claude API prompts for an association manager app.
1) Given a short note from the secretary, draft a formal Bangla notice
with subject, date, venue, agenda and signature block.
2) Given rough meeting notes, produce Bangla minutes with attendees,
resolutions numbered, and action items with owners.
Keep formal register and Bangla numerals for dates and numbers.
```
5. Ask Claude for the member import from Excel, with duplicate detection by phone number and a review screen.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 associations live, 1,500 members imported, first dues collected via bKash |
| Day 60 | 12 associations, 6 paying, first event registration run through the system |
| Day 90 | 30 associations, 20 paying, first verified election held, roughly ৳60,000 monthly revenue |

### First customers with zero budget
- Your own alumni association or professional society is the first customer; run its next dues cycle for free.
- Trade associations in market committees and business clusters; the FBCCI member association list names them by district.
- Facebook groups of alumni bodies and district welfare associations post election notices; those are leads.
- Outreach angle: "Collect dues by bKash, publish notices in a click, and hold an election nobody can dispute."
- The demo that closes: import their Excel member list and send one real notice to the committee's phones during the meeting.
- Referral loop: committee members sit on several associations; every printed receipt and notice carries the product name.

### Pricing and the maths
- ৳999 to ৳4,999 per month by member count. Elections can be an add-on fee for very large associations.
- Costs are SMS OTPs and notices, hosting and a small Claude API bill; gross margin is roughly 80 percent outside election weeks.
- At a mid price of about ৳2,999, roughly 100 paying associations bring in ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria. Trade unions, alumni associations and town unions are numerous, contested elections are common, and mobile payments are established.
- What changes: English plus local language packs, payment rail, local registration fields, a reseller among association secretariats.
- What stays the same: directory, dues engine, notices, the election module.
- Pakistan, Indonesia and diaspora associations in the UK and Gulf follow.

### Risks and how to de-risk them
- Risk: a disputed online election harms the brand. De-risk: hybrid mode with paper fallback, a published audit log, a procedure signed before voting opens.
- Risk: SMS OTP fails for members with old numbers. De-risk: a number verification drive before the roll freezes.
- Risk: slow sales because committees decide by consensus. De-risk: start with dues and notices, sell the election module later.
- Risk: member data leaks. De-risk: role-based access, export logs, and no public directory by default.


---

# Section 12: Money, Compliance and Government (Part 1)

Every business and every family in Bangladesh runs into the same walls: keeping honest books, filing the right form at the right office, and proving where money came from. The six ideas in this section turn those walls into products, with Claude doing the reading, drafting and calculating that a middleman used to charge for.

## Idea 5: Hishab: Automated Bangla Accounting
*Bangla-first accounting where bKash, Nagad and bank movements post themselves and AI reads the receipts.*

### Who pays and why now
The customer is a shop owner, a small trading firm, a service business or a district NGO with two to fifty staff. Today they keep a khata, an Excel sheet and a WhatsApp folder of receipt photos, and hand the mess to an accountant once a year. Global tools are English and card-centric.

They will pay because the books now have to exist: banks want statements, NBR wants Mushak forms, donors want fund-wise reports. The moment is right because every taka leaves an SMS trace, and Claude can read a crumpled receipt and post it. Ports: Bangla speakers in West Bengal and the diaspora first, then any mobile-money country.

### The product in 30 days (MVP)
- Cashbook with cash, bKash, Nagad and bank accounts, Bangla UI and numerals.
- Android app that reads bKash, Nagad and bank transaction SMS on the device and proposes entries.
- Receipt photo to Claude, which extracts vendor, date, amount and VAT and drafts the posting for one-tap approval.
- Organisation templates with a preset chart of accounts: Retail, Service, NGO, Trading.
- Reports (cash flow, profit and loss, party dues) to PDF and Excel; invoices with a bKash payment link.
- Leave out: payroll, inventory, multi-currency, direct bank API connections.

### Data, integrations and the Bangladesh specifics
- Payments: bKash merchant API for subscriptions and for pulling the customer's own merchant transactions, Nagad, SSLCommerz.
- SMS parsing: templates per sender (bKash, Nagad, top five banks) stored as data, so a new format is a one-line fix; statement upload as fallback.
- Compliance: Mushak 6.3 and 9.1 layouts from NBR and NGO Affairs Bureau style donor reports, all as editable templates.
- Offline-first Android with sync; a Bangla font such as Noto Sans Bengali in every PDF.

### Build it with Claude
Stack: Next.js web app, Flutter Android app, PostgreSQL, Claude API, Cloudflare plus a small VPS, bKash merchant API.

1. Ask Claude for the double-entry schema and run the migrations it returns.
```
Design a PostgreSQL schema for a double-entry accounting app for Bangladeshi SMEs and NGOs.
Tables: organisations (type: retail, service, ngo, trading), accounts, journal_entries,
journal_lines, parties, evidence (SMS text or photo URL), invoices, vat_rates.
Every entry must link to evidence. Give me migrations and a seed chart of accounts per type.
```
2. Paste ten real transaction SMS (numbers changed) and ask for a parser plus tests.
```
Here are 10 transaction SMS from bKash, Nagad, BRAC Bank and Dutch-Bangla Bank. Write a Dart
parser returning {sender, direction, amount, counterparty, reference, timestamp} for each,
as a table of templates I can extend without code changes. Add unit tests for every sample.
```
3. Ask Claude for the receipt-reading prompt and JSON schema with a confidence field; anything under 0.8 goes to the approval queue. Then ask for the Mushak 6.3 PDF layout.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: cashbook, bKash and Nagad SMS parsing, receipt AI | 100 free cashbook users |
| Day 60: bank SMS, Mushak export, accountant dashboard | 30 paying customers |
| Day 90: NGO template, referral loop | 120 paying, roughly ৳80,000 monthly revenue |

### First customers with zero budget
- Facebook groups for small entrepreneurs and F-commerce sellers, where "how do I keep accounts" is asked weekly. Answer with a screenshot.
- Income-tax practitioner groups. Offer the Accountant plan free for 90 days; each accountant brings five to ten clients.
- The demo that closes: import last month's bKash SMS and show a finished profit and loss in two minutes. For NGOs, lead with the donor report.
- Referral loop: one free month per referral; 20 percent recurring for accountants.

### Pricing and the maths
- Free cashbook; Standard ৳499/month; Business ৳999; NGO ৳1,499; Accountant ৳2,999; lifetime options.
- Cost of goods is roughly ৳1 to ৳3 per receipt read by Claude, no SMS cost and small hosting, so gross margin is near 85 percent.
- At the Business price of ৳999, roughly 300 paying customers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: West Bengal, India, because the language pack exists and UPI SMS parsing is the same idea.
- Changes: SMS templates, tax forms (GST for Mushak), payment rail (Razorpay or UPI), an accountant reseller.
- Stays the same: double-entry core, receipt AI, organisation templates, reports.

### Risks and how to de-risk them
- Risk: Google Play restricts SMS-reading permission. De-risk: use the notification listener path; keep statement upload.
- Risk: users do not trust AI postings. De-risk: every entry shows its evidence and needs one tap to post.
- Risk: NBR changes Mushak forms. De-risk: forms are templates in the database, not code.

## Idea 9: Bureaucracy Assistant
*Guided, step-by-step filing for trade licence, TIN, VAT, NID, passport and RJSC, with the documents written in Bangla.*

### Who pays and why now
The customer is anyone starting a business or fixing a government record: a shop owner who needs a trade licence, a freelancer who needs a TIN, a family correcting a misspelt NID. Today they search "ট্রেড লাইসেন্স কিভাবে করব", watch three videos, and pay a middleman ৳2,000 to ৳10,000 for a form they could have filled themselves.

They will pay a fraction of that for a clear checklist, the right fee and a filled form. The second customer is the middleman: agents and computer-compose shops who want speed. The moment is right because services now have online portals, but they are confusing and Bangla help is thin. Ports: India, Pakistan, Indonesia, Egypt and Nigeria, each with its own middleman economy.

### The product in 30 days (MVP)
- Six guided flows: trade licence, e-TIN, VAT registration (BIN), NID correction, e-passport, RJSC incorporation.
- Each flow asks five to ten questions and returns a checklist, fees, office and timeline.
- Filled application forms, affidavits and cover letters as Bangla PDFs, paid per document through bKash or Nagad.
- Bangla SEO pages for every service that lead into the flow.
- Agent dashboard: many clients, status, renewal dates.
- Leave out: submitting to portals for the user, paying government fees, live chat, a mobile app.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad for ৳99 to ৳499 micro-payments, SSLCommerz for cards, bKash recurring for agents.
- Fee tables: trade licence categories per city corporation, VAT thresholds, passport and RJSC fees, each dated with a source link.
- Forms: each office's official form as a fillable template, Bangla numerals where expected, Bangla font in every PDF.
- SMS reminders through a local bulk SMS gateway for collection dates and renewals.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API, Cloudflare, bKash merchant API.

1. Ask Claude for a flow engine where each service is a JSON file, not a feature.
```
Design a JSON schema for guided government-service flows: steps with a Bangla and English
question, answer type, branch rules, and outputs (checklist, fees, documents, office, templates).
Then write the full flow for a new trade licence at Dhaka North City Corporation for a sole
proprietor, including renewal. Mark every fee "verify" for human review.
```
2. Give Claude the fields from step 1 and ask for Bangla affidavit and cover letter templates with placeholders.
3. Ask Claude for 30 SEO articles, one per top search question, each ending in a call to the flow.
```
Write a 700-word Bangla article answering "ট্রেড লাইসেন্স করতে কি কি লাগে ২০২৬". Short
paragraphs, a numbered document list, a fee table marked "আনুমানিক", and a closing line inviting
the reader to answer 6 questions for a personal checklist. Add FAQ JSON-LD. Leave fees as {{fee}}.
```
4. Ask Claude for the agent dashboard screens and a monthly fact-check list for a local consultant.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: six flows, 20 SEO pages, payments live | 500 visitors, 40 paid documents |
| Day 60: agent dashboard, SMS reminders, 60 pages | 200 paid documents, 5 agents |
| Day 90: renewals, referral credit | 1,000 paid documents cumulative, 25 agents, roughly ৳1.5 lakh that month |

### First customers with zero budget
- Facebook groups for new entrepreneurs and F-commerce sellers, where trade licence and TIN questions appear daily. Reply with the checklist, then the link. Repeat under YouTube videos.
- Agents: computer-compose shops near city corporation, passport and tax offices, found on Google Maps and visited in person.
- The demo that closes: type in the shop's details and hand over a filled form and checklist in three minutes.
- Referral loop: ৳50 credit per friend who buys; agents get a free month per agent referred.

### Pricing and the maths
- ৳99 to ৳499 per document; ৳2,999/month for agents.
- Cost of goods is roughly ৳5 in Claude tokens per document plus hosting and SMS; gross margin is above 90 percent.
- 100 agents at ৳2,999, or roughly 1,000 documents a month at ৳299, make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, because GST, PAN, Udyam and shop licences are the same problem in twenty languages.
- Changes: flow files, fee tables, form templates, payment rail (Razorpay, UPI), language pack, a local fee-checking consultant.
- Stays the same: flow engine, document generator, SEO template, dashboard.

### Risks and how to de-risk them
- Risk: a fee or rule changes and users get a wrong guide. De-risk: dated tables, a "verified on" stamp, monthly review, a report-an-error button.
- Risk: being seen as another middleman. De-risk: publish the guides free; charge only for documents and agent tools.
- Risk: liability for wrong advice. De-risk: clear disclaimers, a source on every fee, no promised outcomes.

## Idea 10: Freelancer Money OS
*Invoices, Payoneer and Wise reconciliation, export earnings certificates and tax return prep for freelancers.*

### Who pays and why now
The customer is one of the 600,000-plus Bangladeshi freelancers on Upwork, Fiverr and direct contracts, plus the small agencies that grew out of them. Today their money arrives through Payoneer, Wise or a bank with no invoice behind it, no record of the exchange rate, and a tax return guessed at the last minute.

They will pay because the paperwork now bites: banks want proof of export earnings before issuing certificates, returns are needed for loans and visas, and a clean income history is the only way to claim the tax benefits meant for IT exporters. The moment is right because Payoneer, Wise and banks all export CSV statements, and Claude can match them to invoices and fill the return figures. Ports: Pakistan, Philippines, Nigeria, Kenya, Indonesia.

### The product in 30 days (MVP)
- Invoice generator for foreign clients in USD, sent as PDF or link.
- CSV import from Payoneer, Wise and major banks; automatic matching to invoices with taka value at the day's rate.
- Earnings dashboard by month, client and platform, exportable as a statement.
- Certificate pack: bank letter template plus transaction list for the export earnings certificate.
- Tax return prep: yearly income summary, exemption check, figures mapped to the return form, document checklist.
- Leave out: filing the return for the user, Payoneer API integration, expense tracking, agency payroll.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad for subscriptions; Stripe or Lemon Squeezy for diaspora and later ports.
- Bangladesh Bank daily exchange rates; CSV formats for Payoneer, Wise and the five banks freelancers use most.
- NBR return form fields and the IT-enabled services exemption rules kept as a dated rule table a tax practitioner reviews each year.
- SMS reminders for the return deadline; Bangla and English UI.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for statement matching and explanations, Cloudflare, bKash plus Stripe.

1. Ask Claude for the schema: clients, invoices, receipts, fx_rates, tax_years, and a matching table that links receipts to invoices with a confidence score.
2. Paste a sample Payoneer and Wise CSV (anonymised) and ask for the import and matching logic.
```
Here are anonymised CSV exports from Payoneer and Wise and one Bangladeshi bank statement.
Write a TypeScript importer that normalises each into {date, amount_usd, amount_bdt, fee,
counterparty, reference}, then matches receipts to open invoices by amount within 3 percent
and client name similarity. Return unmatched rows for manual review. Include tests.
```
3. Ask Claude for the tax-prep module, driven by a rule table you fill in with a practitioner.
```
Build a tax return prep module for a Bangladeshi individual freelancer. Input: yearly receipts,
fx rates, a rules table (exemption categories, thresholds, form field codes) I will supply.
Output: income by category, the exemption applied, the figures for each return field, and a
Bangla checklist of documents. Never hard-code a rate; read everything from the table.
```
4. Ask Claude for the Bangla onboarding copy and a short WhatsApp message for freelancer groups about the certificate pack.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: invoices, CSV import, dashboard | 200 signups, 20 paying |
| Day 60: certificate pack, tax prep beta | 100 paying |
| Day 90: return season campaign, referrals | 300 paying, roughly ৳1.8 lakh monthly revenue |

### First customers with zero budget
- Facebook groups for Bangladeshi freelancers and Upwork and Fiverr communities, where "how do I get the bank certificate" is asked daily. Answer fully, then link.
- Freelancing training centres in Dhaka and district towns; offer their alumni a free tax workshop.
- Freelancer associations and freelancing YouTube channels; give hosts a referral code.
- The demo that closes: upload their Payoneer CSV and show a year of income, in taka, matched to invoices, in five minutes.
- Referral loop: one free month per paying referral; tax practitioners get a client dashboard.

### Pricing and the maths
- ৳299 to ৳999/month.
- Cost of goods is small: Claude tokens for matching, a few SMS, hosting, so gross margin is above 90 percent.
- At the mid price of ৳599, roughly 500 paying freelancers make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan, where the same Payoneer-and-bank pattern meets its own tax return season.
- Changes: tax rule table, bank CSV formats, exchange rate source, payment rail (local wallets plus Stripe), language pack.
- Stays the same: invoicing, import and matching, dashboard, certificate pack.

### Risks and how to de-risk them
- Risk: tax rules change yearly. De-risk: rules in a dated table, reviewed by a practitioner each budget; show the version on every output.
- Risk: users read outputs as tax advice. De-risk: label everything "prep, not filing" and pair with practitioners.
- Risk: Payoneer or Wise change CSV format. De-risk: column mapping as data, plus a manual mapping screen.

## Idea 24: Legal Document Generator and Lawyer Case Diary
*Bangla deeds, affidavits, rental agreements and powers of attorney from a form, plus a case diary that reminds lawyers and clients.*

### Who pays and why now
The first customer is the public: a landlord who needs a rental agreement, a family that needs an affidavit or a power of attorney, a buyer who needs a draft deed. Today they go to a compose shop or a deed writer at the sub-registry office, who retypes an old template for ৳500 to ৳2,000. The second customer is that deed writer or junior lawyer, who keeps court dates in a paper diary.

Both pay because the current way is slow and error-prone, and one missed court date costs a client. The moment is right because search demand for "বাড়ি ভাড়া চুক্তিপত্র" is large and unserved, and Claude drafts formal Bangla from a template reliably. Ports: India by state language, Pakistan, Nepal.

### The product in 30 days (MVP)
- Fifteen Bangla templates: residential and commercial rental agreements, affidavit, general and special power of attorney, sale deed draft, gift deed, partnership deed, undertaking, NOC.
- Guided form to filled document as PDF and DOCX, with stamp paper guidance.
- Pay per document through bKash or Nagad.
- Lawyer case diary: cases, courts, next dates, notes, with SMS to lawyer and client the day before.
- Client dues ledger with receipts.
- Leave out: e-signature, notary integration, English templates, case law search.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad per document, bKash recurring for the lawyer plan, SSLCommerz for cards.
- Stamp duty and deed registration fee schedules kept as dated tables with sources; a court list for dropdowns.
- Bangla font in PDFs, Bangla numerals in documents, English digits in the diary where courts use them.
- SMS through a local bulk gateway; Bangla unicode SMS cost roughly double an English one, so keep messages short.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for template drafting, Cloudflare, bKash merchant API.

1. Ask Claude to turn each template into fields plus a Bangla document body with placeholders.
```
Here is a standard Bangla residential rental agreement (pasted below). Extract every variable
into a JSON field list with Bangla labels, types and validation (dates, taka amounts, NID).
Rewrite the agreement as a template with {{placeholders}}, keeping formal legal Bangla.
Add optional clauses for advance, notice period and utility bills that I can toggle.
```
2. Ask Claude for the case diary schema and screens: cases, hearings, clients, dues, reminders.
3. Ask Claude for the SMS copy and the reminder job.
```
Write two Bangla SMS under 70 characters each: one to a lawyer listing tomorrow's cases (case
number, court, time), one to a client reminding them of a hearing and what to bring.
Then write a nightly cron job in TypeScript that sends them for all hearings dated tomorrow.
```
4. Ask Claude for 20 SEO articles on the most searched document types, each ending with the form.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: 15 templates, payments, case diary | 100 documents sold, 10 lawyers |
| Day 60: SMS reminders, dues ledger, 20 SEO pages | 300 documents, 40 lawyers |
| Day 90: lawyer referral, more templates | 1,000 documents cumulative, 100 lawyers, roughly ৳1.5 lakh that month |

### First customers with zero budget
- District bar association Facebook groups and junior lawyer WhatsApp groups; offer the diary free for the first 90 days.
- Deed writers at sub-registry offices; visit with a laptop and produce their most common deed in three minutes.
- Landlord and "বাসা ভাড়া" Facebook groups, where the rental agreement is asked for daily.
- The demo that closes: fill the form together and hand over a printed, stamp-ready agreement.
- Referral loop: lawyers get a free month per lawyer referred; buyers get ৳50 credit per friend.

### Pricing and the maths
- ৳99 to ৳299 per document for the public; ৳999/month for lawyers.
- Cost of goods is roughly ৳3 in Claude tokens per document and ৳1 to ৳2 per SMS, so gross margin is above 90 percent.
- 300 lawyers at ৳999, or a mix of 150 lawyers and 750 documents at ৳199, make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: West Bengal, then Hindi-speaking states, because Indian rental and affidavit formats are close and only stamp rules differ by state.
- Changes: template library per legal system, stamp and fee tables, court list, payment rail (Razorpay), language pack.
- Stays the same: template engine, form builder, case diary, SMS jobs.

### Risks and how to de-risk them
- Risk: a template error harms a user. De-risk: every template reviewed by a practising lawyer, versioned, with a visible review date.
- Risk: regulators see unauthorised legal practice. De-risk: sell drafts and tools, not advice; recommend a lawyer for registration.
- Risk: lawyers copy the templates and leave. De-risk: the diary and reminders are the daily habit; templates are the door.

## Idea 48: Union Digital Centre Toolkit
*Queue, fee ledger, document templates, customer records and SMS follow-up for the entrepreneurs who run government service points and computer shops.*

### Who pays and why now
The customer is one of roughly 4,500 Union Digital Centre entrepreneurs, plus the thousands of private computer-service shops near upazila offices that do the same work: birth certificates, online applications, passport forms, printing, mobile banking. Today they run on a notebook, loose receipts and memory. Nobody knows whose passport form went in last month or who owes ৳200.

They will pay because repeat customers are the whole business, and a customer who gets an SMS saying "your document is ready" comes back and tells the village. The moment is right because every service has moved online, so the shop is busier than ever, and Claude can turn a shelf of Word templates into fill-in forms. It pairs with idea 9. Ports: India's common service centres, Pakistan, Indonesia, Nigeria.

### The product in 30 days (MVP)
- Service catalogue with fees: birth and death certificates, passport and NID forms, online applications, printing.
- Token queue and a customer record keyed by phone number, with every past job attached.
- Fee ledger with daily cash close and Bangla receipts.
- Document templates (application letters, affidavits, bio-data, CVs) filled from the customer record and printed.
- SMS follow-up: document ready, collection reminder, renewal alerts for passports and licences.
- Leave out: multi-branch, stationery inventory, full accounting, online booking.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad for the subscription; the shop's own bKash agent income is recorded as a service, not processed.
- Bulk SMS through a local gateway; Bangla unicode messages cost more, so templates stay under 70 characters.
- Works offline on the shop laptop as a PWA and syncs when the connection returns; Bangla numerals on receipts.
- Template library shared with idea 9, so a new government form appears in both products.

### Build it with Claude
Stack: Next.js PWA with local-first storage, PostgreSQL for sync, Claude API for template drafting, Cloudflare, bKash merchant API.

1. Ask Claude for the schema and the offline sync design: customers, jobs, services, payments, sms_log, templates, with a change log for sync.
2. Ask Claude to draft the service catalogue and receipt.
```
Create a seed service catalogue for a Union Digital Centre in Bangladesh: 30 common services
grouped as certificates, applications, printing, mobile banking, and training. Each with a Bangla
name, typical fee range marked "edit me", and required customer fields. Then design a 58 mm
thermal receipt in Bangla showing shop name, token, service, fee, and a "ready by" date.
```
3. Ask Claude for the template engine and five starter templates.
```
Write a Bangla template engine: templates are Markdown with {{fields}} pulled from the customer
record (name, father's name, NID, address, phone). Produce five starter templates: application
to the Union Parishad chairman, bio-data, affidavit, character certificate request, and a
general application letter. Render each to A4 PDF with a Bangla font.
```
4. Ask Claude for the SMS templates and the daily cash close screen, then for a two-minute Bangla onboarding video script.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: catalogue, queue, ledger, receipts | 20 shops in two districts |
| Day 60: SMS follow-up, templates, offline sync | 100 paying shops |
| Day 90: renewal alerts, referral loop | 300 paying shops, roughly ৳1.5 lakh monthly revenue |

### First customers with zero budget
- Facebook groups for UDC entrepreneurs, which are large and active, and district UDC WhatsApp groups. Post a receipt photo and a short video.
- Computer-service shops around upazila and passport offices; walk in with a laptop.
- District UDC associations; offer the toolkit free to the association's office bearers.
- The demo that closes: record three real customers, print receipts and send the "ready" SMS while the owner watches.
- Referral loop: one free month per shop referred; the most active shop in a district becomes a reseller.

### Pricing and the maths
- ৳299 to ৳799/month.
- Cost of goods is mostly SMS, roughly ৳1 to ৳2 per message, plus hosting and a little Claude use, so gross margin sits near 80 percent.
- At the mid price of ৳499, roughly 600 paying shops make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India's common service centres, hundreds of thousands of shops with the same queue-and-receipt problem, starting in West Bengal.
- Changes: service catalogue, templates, SMS gateway, payment rail (UPI), language pack, a state-level reseller.
- Stays the same: queue, customer record, ledger, offline sync, template engine.

### Risks and how to de-risk them
- Risk: low willingness to pay at ৳299. De-risk: sell on SMS-driven repeat business, and show the monthly report that proves it.
- Risk: the government issues its own free software. De-risk: stay the friendlier shop tool and integrate rather than compete.
- Risk: poor connectivity. De-risk: local-first design; nothing needs the internet except SMS and sync.

## Idea 60: Inheritance and Family Land Manager
*A faraiz share calculator under Islamic and civil rules, an heir tree, land partition worksheets and a mutation tracker, all in Bangla.*

### Who pays and why now
The customer is any family dividing a parent's land or savings, the lawyer or deed writer who advises them, and the relative abroad who wants to see the numbers before sending money. Today the shares are worked out by an imam, a lawyer or an uncle with a calculator, and the result is argued over for years. Inheritance is the largest source of family disputes in the country.

They will pay for a printed worksheet that names the rule behind every share, because a neutral page settles an argument that a relative cannot. The moment is right because land records are going digital, everyone searches for a "ফারায়েজ ক্যালকুলেটর", and Claude explains the rules in plain Bangla. It pairs with idea 24. Ports: Pakistan, Indonesia, Malaysia, Egypt, Nigeria, and diaspora families paying in dollars.

### The product in 30 days (MVP)
- Faraiz calculator for Sunni Hanafi rules, including the orphaned-grandchild rule under the 1961 ordinance.
- Basic Hindu and Christian succession under Bangladeshi law.
- Heir tree builder with relationships and predeceased heirs.
- Land partition worksheet: several plots (dag and khatian), share per heir in local units.
- Bangla PDF report with rule references, plus a mutation tracker with a document checklist.
- Leave out: legal opinions, court case tracking, automatic e-porcha lookup, English reports.

### Data, integrations and the Bangladesh specifics
- Payments: bKash and Nagad per report; Stripe or Lemon Squeezy for diaspora buyers.
- Land unit conversions (acre, bigha, katha, shotangsho, decimal) with regional variants; khatian types (CS, SA, RS, BS).
- Mutation steps and documents from the AC Land process, kept as a dated checklist.
- Rule tables versioned and reviewed by a faraiz scholar and a lawyer; Bangla numerals and fonts in reports.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for explanations, Cloudflare, bKash plus Stripe.

1. Ask Claude for the rule engine as pure functions with a test suite a scholar will check.
```
Write a TypeScript faraiz engine for Sunni Hanafi inheritance. Input: list of heirs with relation,
sex, and alive/predeceased. Output: share of each heir as a fraction, with the rule applied
(fixed share, residuary, exclusion, awl, radd) named for each line. Include the Bangladesh
1961 ordinance rule for children of predeceased children. Give 40 test cases with expected fractions.
```
2. Ask Claude for the heir tree and partition screens, and for the land unit conversion table.
3. Ask Claude for the report text and the rule explanations in Bangla.
```
For each rule in the engine (fixed shares, residuary, exclusion, awl, radd, the 1961 rule), write
a 2-sentence explanation in plain Bangla for a family reader, and a one-line reference to the
source. Then write the Bangla report layout: heir table, share fractions, per-plot partition, notes.
```
4. Ask Claude for 20 SEO articles on top inheritance questions and a WhatsApp message for deed writers.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30: calculator, heir tree, free result page | 2,000 free calculations |
| Day 60: paid report, partition worksheet, tracker | 300 paid reports, 20 lawyers |
| Day 90: Hindu and Christian rules, diaspora payments | 1,000 paid reports cumulative, 80 lawyers, roughly ৳2 lakh that month |

### First customers with zero budget
- Search traffic: the free calculator answers "ফারায়েজ ক্যালকুলেটর" searches; the report is the upsell.
- Facebook groups on land law, and imam and madrasa networks who are asked these questions weekly.
- Deed writers at sub-registry offices and district lawyers; the plan saves them an afternoon per case.
- Diaspora Facebook groups in the UK, US and Middle East, where the family abroad pays in dollars.
- The demo that closes: enter the family's real case and print the worksheet on the spot. Referral: ৳50 credit per friend.

### Pricing and the maths
- ৳199 to ৳499 per calculation or report; ৳999/month for lawyers and deed writers.
- Cost of goods is a few taka of Claude tokens per report plus hosting, so gross margin is above 90 percent.
- At the mid price of ৳349, roughly 860 reports a month, or 300 lawyer subscriptions, make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan, where Hanafi rules and land disputes match closely; then Malaysia and Indonesia with Shafi'i rule packs.
- Changes: rule pack per legal system, land units, mutation checklist, language pack, payment rail.
- Stays the same: heir tree, engine structure, worksheet, tracker, report layout.

### Risks and how to de-risk them
- Risk: a wrong share calculation causes real harm. De-risk: a scholar-verified test suite, rule references on every line, a visible version.
- Risk: users want the calculator to take sides. De-risk: neutral wording, a madhhab selector, and a disclaimer that courts decide.
- Risk: religious sensitivity. De-risk: partner with respected scholars and publish who reviewed each rule pack.


---

# Section 13: Money, Compliance and Government (Part 2)

The five businesses in this section sit where money moves and where a regulator or an employer wants a clean record of it: insurance agents, payroll, mobile money agents, neighbourhood ISPs and money changers. Each one replaces a notebook that already exists, so the sale is not about convincing anyone to keep records, only about making the record faster, safer and easier to show to whoever asks.

## Idea 31: Insurance Agent CRM
*A pocket policy book for life insurance agents: premium reminders in Bangla, lapse alerts, commission statements and prospect follow-up.*

### Who pays and why now
Bangladesh has hundreds of thousands of life insurance agents, most part-time, working from a diary and memory. Their income is renewal commission. When a policyholder forgets a premium and the policy lapses, that income is gone for good. Today the agent phones people one by one, if they remember at all.

Agents will pay a small fee because one saved policy pays for the app for years, and insurers are cutting commissions on poor persistency. The product ports to India, Pakistan, Indonesia and Nigeria, where agent forces are even larger.

### The product in 30 days (MVP)
- Policyholder list with policy number, plan, premium amount and frequency.
- Automatic Bangla SMS reminders 10 and 3 days before each due date, sent in the agent's name.
- Lapse alert list: every policy past its grace period, sorted by commission at risk.
- Prospect pipeline with follow-up dates and a daily call list.
- Import from Excel or from a photo of the agent's diary page read by Claude.
- Leave out: insurer API integration, online premium collection, team hierarchies, claims tracking.

### Data, integrations and the Bangladesh specifics
- Subscription via bKash and Nagad; the app never touches premiums.
- Bangla SMS through a local gateway with a masked sender ID, because policyholders trust a named sender.
- Frequencies of monthly, quarterly, half-yearly and yearly, with grace periods that differ by insurer, stored as settings.
- Offline-first Flutter app, since agents enter details at the customer's home in towns with poor data.

### Build it with Claude
Stack: Flutter for Android, Laravel API, PostgreSQL, Claude API for diary-photo import, a small VPS, a Bangla SMS gateway, bKash merchant API for subscriptions.

1. Ask Claude for the schema and the reminder job. Paste the answer into your Laravel migrations and scheduler.
```
Design a PostgreSQL schema for a life insurance agent CRM in Bangladesh:
agents, insurers (grace_period_days), policyholders, policies (plan, premium,
frequency monthly/quarterly/half-yearly/yearly, next_due_date, status
active/grace/lapsed), premium_payments, prospects, commission_rates.
Then write a Laravel scheduled command that finds policies due in 10 or 3 days
and queues a Bangla SMS to the policyholder mentioning the agent's name.
```
2. Ask Claude for the Flutter screens: policyholder list, policy detail, today's calls, lapse list. Then ask for a SQLite cache so the app works offline.
3. Ask Claude for the Bangla messages and the diary import.
```
Write 4 Bangla SMS templates (under 160 characters, Bangla numerals) for a life
insurance agent: premium due in 10 days, due in 3 days, grace period warning,
polite lapse recovery. Use placeholders {name}, {amount}, {date}, {agent_name}.
Then write a Claude API prompt that takes a photo of a handwritten Bangla policy
diary page and returns JSON rows: name, phone, policy_number, premium,
frequency, next_due_date.
```
4. Ask Claude for a one-page Bangla onboarding guide and a 60-second demo script.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 20 agents from one insurer branch, 500 policies loaded |
| Day 60 | 150 agents, 100 paying, first lapse recovered by a reminder |
| Day 90 | 400 paying agents, roughly ৳1 lakh monthly revenue |

### First customers with zero budget
- Insurer branch offices hold weekly agent meetings; ask the branch manager for 10 minutes. One branch is 30 to 100 agents.
- Outreach angle: "How many of your policies lapsed last year? Each one cost you renewal commission. This app calls them for you."
- Demo that closes: import the agent's diary page from a photo, then show the lapse list with taka at risk.
- Referral loop: an agent who brings three colleagues gets a free month.

### Pricing and the maths
- ৳199 to ৳499 per agent per month, or a plan per insurer branch.
- Costs are SMS at a few paisa per policyholder per month plus shared hosting; gross margin above 80 percent.
- At a mid price of roughly ৳350, about 860 paying agents produce roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, starting with West Bengal, which shares the language, then Hindi.
- What changes: language pack, UPI for the subscription, insurer list with local grace periods, DLT-registered SMS.
- What stays the same: schema, reminder engine, commission logic, offline sync.

### Risks and how to de-risk them
- Risk: agents fear the insurer will poach their book. De-risk: data belongs to the agent, export any time, say so on the first screen.
- Risk: SMS costs rise with volume. De-risk: WhatsApp reminders as an option and a cap of two SMS per policy per cycle.
- Risk: insurers launch their own agent app. De-risk: stay multi-insurer, since most agents sell for more than one company over a career.

## Idea 46: SME Payroll in Bangla
*Payroll for businesses with 10 to 200 staff: selfie attendance, overtime rules, advances and loans, salary to bKash or Nagad, payslips by SMS.*

### Who pays and why now
Factories, restaurants, multi-branch shops, security firms and small hospitals pay workers in cash every month from an Excel sheet. The owner spends two days counting attendance, working out overtime and deducting advances, then hands out envelopes. Disputes about days worked are constant.

They will pay because payroll is the most stressful task of the month and mobile money now makes cash unnecessary: bKash and Nagad offer bulk disbursement, and workers already have wallets. Garment buyers increasingly ask subcontractors for wage records. The model ports to Pakistan with JazzCash, Kenya with M-Pesa, Nigeria, Indonesia and Egypt.

### The product in 30 days (MVP)
- Employee register with wage type (monthly, daily, piece), wallet number and joining date.
- Android attendance app: selfie plus location check-in and check-out, with manager override.
- Overtime and late rules per business, defaulting to double rate for overtime.
- One-click monthly payroll run producing a salary sheet and a disbursement file.
- Payslips by Bangla SMS to each worker.
- Leave out: automated bKash bulk disbursement (export the file first), tax and provident fund, shift scheduling, biometric devices.

### Data, integrations and the Bangladesh specifics
- Disbursement via bKash Business and Nagad bulk payment; start with their portal upload format, then the API.
- Bangla SMS payslips, since many workers do not use email or smartphones.
- Labour Act defaults for overtime, festival bonus and weekly holiday, kept editable because practice varies.
- Offline attendance capture in Flutter for factories with poor signal.

### Build it with Claude
Stack: Next.js web app for the owner, Flutter for attendance, PostgreSQL, Claude API for copy and policy drafting, Cloudflare, bKash merchant API for billing and later disbursement.

1. Ask Claude for the data model and calculation engine. Run the tests it writes before touching the UI.
```
Design PostgreSQL tables for SME payroll in Bangladesh: companies, employees
(wage_type monthly/daily/piece, basic, house_rent, medical, wallet_provider
bkash/nagad, wallet_number), attendance (selfie_url, lat, lng, in_at, out_at),
overtime_rules, advances and loans with instalments, payroll_runs, payslips.
Write a TypeScript function computePayslip(employee, month) applying working
days, late deductions, overtime at 2x basic per hour and loan instalments,
returning a line-item breakdown. Include unit tests.
```
2. Ask Claude for the Flutter attendance screen: camera, location, one big Bangla button, an offline queue. Test it on a ৳10,000 phone.
3. Ask Claude for the owner dashboard: attendance grid, payroll wizard, and an export matching the bulk payment sheet you download from bKash Business.
4. Ask Claude for the worker-facing Bangla copy and the pitch.
```
Write a Bangla SMS payslip under 160 characters with Bangla numerals using
{name}, {month}, {days}, {ot_hours}, {gross}, {deductions}, {net}, {wallet}.
Then write a 5-line Bangla WhatsApp message to a factory owner explaining that
salaries go to workers' bKash in one click, attendance is proven by selfie,
and the first month is free for up to 20 staff.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 businesses, 150 employees on attendance, first payroll run done |
| Day 60 | 15 businesses, 800 employees, 10 paying |
| Day 90 | 40 paying businesses, 2,500 employees, roughly ৳1.8 lakh monthly revenue |

### First customers with zero budget
- Facebook groups for garment subcontractors, restaurant owners and small factory owners in Gazipur, Narayanganj and Chattogram.
- Google Maps categories to scrape: garment factories, packaging factories, private hospitals, security services.
- Outreach angle: "Your salary day takes two days and a bag of cash. Make it one click to bKash."
- Demo that closes: load one month of their Excel attendance and produce payslips in front of them.
- Referral loop: workers see the payslip SMS and ask their next employer for it.

### Pricing and the maths
- ৳49 to ৳99 per employee per month, by whether disbursement and attendance are included.
- Costs are one SMS per worker per month plus selfie storage; gross margin around 75 percent.
- At a mid price of roughly ৳75 per employee, about 4,000 employees, for example 80 businesses with 50 staff each, produce roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan, because JazzCash and Easypaisa offer bulk disbursement and small factories have the same cash payroll problem.
- What changes: Urdu language pack, the disbursement integration, labour law defaults, SMS gateway.
- What stays the same: attendance app, payroll engine, payslip logic, owner dashboard.

### Risks and how to de-risk them
- Risk: bKash Business onboarding is slow for a startup. De-risk: launch with file export to the customer's own portal and add the API later.
- Risk: workers refuse selfies over privacy. De-risk: selfies visible only to the employer and deleted after 90 days; say so in Bangla in the app.
- Risk: payroll errors destroy trust. De-risk: a preview and approval step before every run, and an audit log of edits.

## Idea 64: Mobile Money Agent Ledger
*One screen for the agent who balances bKash, Nagad, Rocket and Upay floats plus a cash drawer: daily reconciliation, commissions, recharge sales and shortage alerts.*

### Who pays and why now
Over 300,000 mobile financial service agents run from grocery shops, pharmacies and phone stalls. Each holds float in four wallets and cash in a drawer, and moves money between them dozens of times a day. At night the agent adds up SMS confirmations by hand, and a shortage of ৳500 turns into an argument with the helper.

Agents will pay because the ledger finds the shortage the same evening and shows what each wallet earned in commission. Competition between wallets means more float across more providers, so the arithmetic is harder than five years ago. The same job exists for M-Pesa agents in Kenya, POS agents in Nigeria, and agents in Pakistan, Indonesia and Ghana.

### The product in 30 days (MVP)
- Opening balance per wallet and cash, entered once each morning.
- Cash-in and cash-out entries in two taps, with amount and wallet, in Bangla.
- Automatic reading of transaction confirmation SMS on the agent's phone to pre-fill entries.
- Evening reconciliation: expected balances versus actual, with the shortage highlighted.
- Commission tracking per wallet at rates the agent enters, summed daily and monthly.
- Leave out: float top-up ordering from distributors, multi-shop dashboards, customer KYC, loans.

### Data, integrations and the Bangladesh specifics
- No wallet API is needed: the app parses the confirmation SMS that bKash, Nagad, Rocket and Upay already send to the agent's SIM, on device.
- Keep an editable SMS pattern library, because wallet message formats change without notice.
- Subscription paid through bKash or Nagad, which the agent already uses every minute.
- Works fully offline; reconciliation must finish at closing time even with weak data.

### Build it with Claude
Stack: Flutter for Android with local SQLite, a small Laravel API for backup and subscriptions, PostgreSQL, Claude API for parsing unusual SMS formats, a small VPS, bKash merchant API.

1. Ask Claude for the ledger model and reconciliation logic, and test it with a fake day of transactions.
```
Design a SQLite schema for a Bangladesh mobile money agent ledger: wallets
(bkash, nagad, rocket, upay, cash), daily_openings, transactions (type cash_in,
cash_out, transfer_between_wallets, recharge, bill_pay, float_topup; amount;
commission), closings. Write a Dart function reconcileDay(date) that returns
expected balance per wallet, actual balance entered, difference, and total
commission, and flags any wallet where the difference exceeds 50 taka.
```
2. Ask Claude for the SMS parser from real confirmation messages with numbers replaced.
```
Here are 20 anonymised transaction SMS from bKash, Nagad, Rocket and Upay
agent numbers. Write Dart regex parsers that extract wallet, type (cash in,
cash out, send money, payment), amount, commission, customer number and
transaction id. Where a message matches no pattern, write a Claude API call
that returns the same fields as JSON, and store the message text so I can add
a new pattern later.
```
3. Ask Claude for the three screens: today, reconcile, month. Every button large, Bangla, usable with one thumb.
4. Ask Claude for a Bangla Facebook post and a two-minute demo video script for agents.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 30 agents in one bazaar using it daily, SMS parsing above 90 percent |
| Day 60 | 300 installs, 120 paying, first distributor introducing the app to its agents |
| Day 90 | 500 paying agents, roughly ৳1.5 lakh monthly revenue |

### First customers with zero budget
- Every bazaar has a row of agent shops; walk it with the app installed and reconcile one agent's day for free.
- Facebook groups for bKash and Nagad agents, where shortages and commission complaints are daily topics.
- Outreach angle: "Find tonight's shortage in two minutes, not two hours."
- Demo that closes: read the agent's SMS inbox and show today's expected balances before they have counted.
- Referral loop: agents in the same bazaar copy each other; a bazaar leaderboard of shortage-free days gives them a reason to invite neighbours.

### Pricing and the maths
- ৳199 to ৳499 per month per agent shop.
- Costs are near zero per agent: on-device parsing, occasional Claude calls and backup storage; gross margin above 85 percent.
- At a mid price of roughly ৳350, about 860 paying agents produce roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya, because M-Pesa agents face the same float and shortage problem and already pay for tools.
- What changes: SMS pattern library for M-Pesa and Airtel Money, Swahili and English language pack, M-Pesa for the subscription.
- What stays the same: ledger schema, reconciliation engine, offline design, screens.

### Risks and how to de-risk them
- Risk: Android restricts SMS reading permissions. De-risk: offer manual entry and a notification-listener path, and publish outside Play Store as an APK if needed.
- Risk: wallets change SMS formats. De-risk: patterns update from the server without an app release, with Claude as the fallback.
- Risk: wallets release their own agent ledger. De-risk: no single wallet will show the others' balances; being multi-wallet is the product.

## Idea 65: Local ISP and Cable Operator Billing
*Subscriber billing for neighbourhood ISPs and cable operators: bKash auto-collection, MikroTik and OLT integration to suspend non-payers, complaint tickets and technician dispatch, in Bangla.*

### Who pays and why now
Thousands of small ISPs and cable operators serve 200 to 5,000 homes each. Collection is still a boy on a motorbike with a receipt book in the first week of the month. Operators lose roughly 10 to 20 percent of revenue to late payers and unrecorded collections, and cannot cut off non-payers without logging into the router by hand.

Operators will pay because the product collects money and stops leakage. Fibre has spread fast, bKash payment links are normal, and regulators expect subscriber records. It ports to local cable operators in India and ISPs in Pakistan, Nepal, Indonesia, Nigeria and the Philippines.

### The product in 30 days (MVP)
- Subscriber list with package, monthly fee, connection details and Bangla address.
- Monthly invoice generation with a bKash payment link sent by SMS.
- Automatic marking of paid invoices from bKash payment callbacks.
- MikroTik integration: add subscribers to a suspended address list when unpaid past a grace date, and release on payment.
- Complaint tickets from a customer WhatsApp number, assigned to a technician.
- Leave out: OLT and ONU management, bandwidth graphs, IPTV, accounting.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for payment links and callbacks; Nagad as a second option since customers vary by area.
- MikroTik RouterOS API for PPPoE and hotspot suspension; OLT integration later, per vendor.
- SMS gateway for invoices and receipts; WhatsApp for complaints where customers prefer it.
- Bangla numerals on invoices and receipts, and Bangla package names.

### Build it with Claude
Stack: Laravel web app, PostgreSQL, Flutter collector app, MikroTik RouterOS API, bKash merchant API, Cloudflare in front of a VPS.

1. Ask Claude for the billing schema and invoice cycle, and run its tests.
```
Design a PostgreSQL schema for a small ISP billing system in Bangladesh:
operators, packages, subscribers (pppoe_username, router_id, status active/
suspended/disconnected, grace_days), invoices, payments (source bkash, nagad,
cash_collector), collectors, tickets, technicians. Write a Laravel scheduled
job that generates invoices on the 1st, sends a Bangla SMS with a bKash payment
link, and lists subscribers unpaid past grace for suspension.
```
2. Ask Claude for the MikroTik integration. Test it on a spare router before touching a live one.
```
Write a PHP class MikroTikSuspender using the RouterOS API that logs in,
finds a PPPoE secret by username, changes its profile to "suspended", and
removes the active session so the change applies immediately. Add a restore()
method for payment. Handle timeouts and log every action with the router id.
Then write a Bangla SMS (under 160 characters) telling the subscriber the line
is paused and giving the bKash link to restore it.
```
3. Ask Claude for the bKash callback handler and a reconciliation page that lists payments not matched to an invoice.
4. Ask Claude for the collector app, the ticket flow and a Bangla demo script for an ISP association meeting.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 operators, 600 subscribers billed, first automatic suspension and restore |
| Day 60 | 10 operators, 5,000 subscribers, 40 percent paying through bKash links |
| Day 90 | 30 paying operators, roughly ৳75,000 monthly revenue |

### First customers with zero budget
- The local ISP association and its district chapters meet monthly; ask for a demo slot.
- Facebook groups for MikroTik users and ISP owners in Bangladesh, where billing questions appear daily.
- Outreach angle: "Stop paying a collector for a month; let bKash collect and let the router chase late payers."
- Demo that closes: import their subscriber Excel, send yourself an invoice, pay it with bKash, watch the router restore in seconds.
- Referral loop: give router distributors a referral code, since every operator buys from them.

### Pricing and the maths
- ৳999 to ৳4,999 per month by subscriber count.
- Costs are one or two SMS per subscriber per month and hosting; gross margin around 70 percent after SMS.
- At a mid price of roughly ৳3,000, about 100 paying operators produce roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: India, where tens of thousands of local cable operators have moved to broadband and share the door-to-door collection problem.
- What changes: Hindi and Bengali language pack, UPI payment links, DLT-registered SMS, local regulator export format.
- What stays the same: billing engine, MikroTik integration, collector app, ticket flow.

### Risks and how to de-risk them
- Risk: a bug suspends paying customers. De-risk: a dry-run mode that lists proposed suspensions for approval for the first two months.
- Risk: operators fear giving router access. De-risk: a read-only first step, a restricted API user on the router, and an audit log they can inspect.
- Risk: bKash merchant onboarding delays. De-risk: start with the operator's own bKash merchant account and personal payment numbers recorded by the collector app.

## Idea 96: Money Changer Ledger and Compliance
*A ledger for licensed money changers: rate board, buy and sell transactions, customer KYC records, currency stock and regulator reports, in Bangla.*

### Who pays and why now
A few hundred licensed money changers operate in Dhaka, Chattogram, Sylhet and the border towns. Each keeps a manual register of every purchase and sale, a copy of the customer's passport or NID, and a daily stock of each currency. Inspections have increased, and a messy register means a fine or a suspended licence.

They will pay because the ledger protects the licence. Rates change several times a day, the register must reconcile with cash in each currency, and monthly returns are prepared by hand. The product ports to Pakistan, Nigeria, Egypt, Nepal and Sri Lanka, each with its own report format.

### The product in 30 days (MVP)
- Rate board: buy and sell rates per currency, editable from a phone, shown on a shop screen.
- Buy and sell transactions with customer name, ID type and number, purpose and amount.
- KYC record: photo of passport or NID captured by phone and attached to the transaction.
- Currency stock per denomination with opening, movements and closing.
- Daily and monthly register in the regulator's layout, exportable to PDF and Excel.
- Leave out: online rate publishing, remittance, multi-branch consolidation, accounting.

### Data, integrations and the Bangladesh specifics
- The Bangladesh Bank reporting formats for money changers, kept as templates that the owner can adjust when a circular changes.
- Customer ID types: passport, NID and birth certificate, with NID number validation.
- Bangla numerals and Bangla labels in the register, with English copies for the regulator.
- Subscription via bKash; customers pay in cash, so no payment integration is needed in the product.

### Build it with Claude
Stack: Laravel web app that also works on a tablet, PostgreSQL, Claude API to read ID documents and to draft compliance text, a VPS in Bangladesh, bKash merchant API for the subscription.

1. Ask Claude for the schema and stock logic, and check it with a day of sample trades.
```
Design a PostgreSQL schema for a licensed money changer in Bangladesh:
currencies, rate_updates (buy, sell, effective_at), customers (id_type
passport/nid/birth_certificate, id_number, nationality), transactions (buy or
sell, currency, foreign_amount, rate, bdt_amount, purpose, id_document_url),
denomination_stock, daily_closings, reports. Write SQL that produces closing
stock per currency and denomination and flags any day where stock does not
match transactions.
```
2. Ask Claude for the tablet screens: rate board, new transaction with ID capture, day close. Insist on large numerals.
3. Ask Claude to build the ID reader and the register export.
```
Write a Claude API call that takes a photo of a Bangladeshi NID or a foreign
passport and returns JSON with name, id_number, date_of_birth, nationality and
expiry, with a confidence score. Then write a Laravel export that renders the
monthly money changer register as PDF in the layout of a table with date,
customer, id number, currency, amount bought, amount sold, rate and BDT value,
with Bangla and English headers and Bangla numerals in the Bangla copy.
```
4. Ask Claude for a Bangla one-page note on how the ledger helps in an inspection, and a WhatsApp message for money changer associations.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 money changers on the ledger, first monthly register exported |
| Day 60 | 15 users, 10 paying, one inspection passed using the printed register |
| Day 90 | 40 paying money changers, roughly ৳1.2 lakh monthly revenue |

### First customers with zero budget
- Money changer associations in Dhaka and Chattogram; their office is the fastest way to meet 50 owners.
- Google Maps: search "money exchange" in Motijheel, Gulshan, Paltan, Uttara, Sylhet and near the airport, and visit the shops in person.
- Outreach angle: "The next inspector will ask for the register. Print it in one click."
- Demo that closes: photograph a passport, enter one sale, and print the day's register in the regulator's layout in front of the owner.
- Referral loop: a free month to both sides when one shop refers a neighbour.

### Pricing and the maths
- ৳1,499 to ৳4,999 per month, by transaction volume and number of counters.
- Costs are a few Claude calls per day for ID reading plus hosting and backups; gross margin above 80 percent.
- At a mid price of roughly ৳3,250, about 90 paying money changers produce roughly ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan, where exchange companies and their branches face strict reporting and the market is several times larger.
- What changes: Urdu language pack, the regulator's report format, ID types (CNIC), JazzCash or bank transfer for the subscription.
- What stays the same: rate board, transaction flow, KYC capture, stock reconciliation.

### Risks and how to de-risk them
- Risk: regulatory formats change or you misread them. De-risk: templates are editable by the owner, and you show the export to two licensed changers before launch.
- Risk: owners fear a digital record of every trade. De-risk: sell to licensed changers only, and stress that the record protects them in an inspection.
- Risk: storing ID photos creates liability. De-risk: encrypt at rest, restrict access to the owner, and delete after the period the regulator requires.


---

# Section 14: Services, Agencies and People Businesses

The businesses in this section sell coordination: recruiters, agencies, consultants, contractors and organisers whose product is a service delivered by staff, vendors or venues. Their pain is evidence and money flow, and each idea here turns a paper register and a WhatsApp inbox into a system that clients, families and donors can see.

## Idea 15: Overseas Recruitment Agency OS
*Candidate pipeline, BMET steps, visa tracking and family status updates for manpower agencies, in Bangla.*

### Who pays and why now
Around a million Bangladeshis leave for work abroad each year, most through thousands of licensed recruiting agencies and their sub-agents. Each candidate needs a passport, medical test, BMET registration, training, visa and flight. The agency tracks this in a register, photocopies and a manager's phone.

The owner pays because lost files cost money: a medical that expires before the visa arrives means a new test and an argument. Families call daily asking where the visa is, and a status page they can open on a phone ends those calls. The moment is right because BMET is pushing digital records and remittance is a national priority. The product ports to Nepal, the Philippines, Indonesia, Pakistan and Sri Lanka, which run near-identical pipelines.

### The product in 30 days (MVP)
- Candidate profile: passport scan, photo, NID, skill, destination, sub-agent.
- Pipeline board with fixed stages: registered, medical, BMET, training, visa, ticket, departed.
- Document checklist per destination with expiry dates and colour warnings.
- Payment ledger per candidate: agreed fee, instalments, balance.
- Family status page: a private link showing the current stage in plain Bangla, with an SMS on every change.
- Leave out: online job applications, employer portal, accounting, a mobile app.

### Data, integrations and the Bangladesh specifics
- bKash merchant API for instalments; cash and bank as manual entries.
- SMS gateway with Bangla Unicode; WhatsApp later for document photos.
- A stage template per destination (Saudi Arabia, Malaysia, UAE, Qatar) with the documents each embassy asks for.
- BMET registration and smart card numbers as fields; there is no public API, so staff type them.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for document reading and Bangla copy, Cloudflare plus a small VPS, bKash merchant API, SMS gateway.

1. Ask Claude for the schema and stage engine, and review the tables before generating migrations:
```
Design a PostgreSQL schema for an overseas recruitment agency in Bangladesh.
Tables: agencies, staff, sub_agents, candidates, destinations, stages, candidate_stages,
documents (type, file_url, issue_date, expiry_date), payments, family_contacts, sms_log.
Stages are ordered per destination. Log every stage change with who and when.
Add a view listing candidates whose medical or passport expires within 30 days.
```
2. Ask Claude to build the pipeline board with drag-and-drop between stages and fire an SMS on each change.
3. Ask Claude for the family page and message copy:
```
Write Bangla copy for a family-facing status page of a recruitment agency.
Stages: registered, medical done, BMET registered, training complete, visa received, ticket issued, departed.
For each stage give a one-line Bangla status and a one-line "what happens next".
Also write a 160-character Bangla SMS per stage with placeholders {name} and {agency}. Calm tone, no date promises.
```
4. Ask Claude for a passport reader returning name, number and expiry as JSON to pre-fill the candidate form, then the bKash payment link flow.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 agencies live with 150 candidates loaded |
| Day 60 | 10 paying agencies, 2,000 family page views |
| Day 90 | 25 paying agencies, roughly ৳2 lakh monthly revenue |

### First customers with zero budget
- BAIRA, the recruiting agencies' association, and its district committees; ask a member to introduce you at a meeting.
- Facebook groups for "বিদেশ যাত্রা" and country-specific worker groups are full of sub-agents; message those who post daily.
- Scrape Google Maps for "recruiting agency" in Dhaka, Sylhet, Cumilla and Chattogram and visit the top 30 on foot.
- Outreach angle: "Your staff answer dozens of family calls a day. Give families a link instead." The demo that closes: load five real candidates and send a live SMS to the owner's phone.
- Referral loop: every family page carries a "powered by" line, and sub-agents bring their next agency.

### Pricing and the maths
- ৳4,999/month for up to 100 active candidates, ৳9,999 for up to 500, ৳14,999 unlimited with several branches.
- Cost of goods is SMS, a little Claude usage and shared hosting; gross margin above 85 percent.
- At the mid price of ৳9,999, roughly 30 paying agencies make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nepal. The pipeline is nearly identical and agencies cluster in Kathmandu.
- What changes: language pack, government steps (Department of Foreign Employment in Nepal, POEA in the Philippines), payment rail (eSewa, GCash), a local reseller.
- What stays the same: stage engine, expiry logic, family page and SMS flow.

### Risks and how to de-risk them
- Risk: agencies fear a digital trail of informal fees. De-risk: never show fee amounts on the family page.
- Risk: village sub-agents do not use computers. De-risk: a phone-browser candidate form with photo upload.
- Risk: BMET launches its own portal. De-risk: be the agency's internal system and family channel, and import from any portal.

## Idea 21: Wedding Vendor Booking
*A shared calendar, advance ledger and Bangla contract for community centres, decorators, caterers and photographers.*

### Who pays and why now
Wedding season runs from November to February, and every community centre, decorator, caterer and photographer is booked by phone and paper diary. Double bookings happen. Advances are taken in cash and noted on a slip. Per-plate quotes are redone by hand each time the guest count changes.

The vendor pays because one lost booking or one disputed advance costs more than a year of software. A centre manager who shows a family a live calendar closes faster, and a caterer who sends a Bangla contract with plate count and payment schedule ends the argument about what was agreed. The moment is right because families find vendors on Facebook and expect instant answers about dates. The model ports to India, Pakistan, Indonesia, Nigeria and Egypt, where seasons and vendor types are similar.

### The product in 30 days (MVP)
- Vendor calendar with day, lunch and dinner slots, colour-coded as enquiry, held or confirmed.
- Booking record: client name and phone, event type, guest count, venue, notes.
- Quote builder: per-plate menu items, decoration packages, extras, total in ৳.
- Advance and balance ledger with bKash payment links and a due-date reminder.
- Bangla contract PDF generated from the booking, plus an SMS confirmation to the client.
- Leave out: a public marketplace, guest RSVP, staff scheduling, chair and plate inventory.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant APIs for advances; SSLCommerz for cards from families abroad.
- SMS gateway for Bangla confirmations; WhatsApp for sending the contract PDF.
- Show the Bangla date and mark Ramadan and major holidays on the calendar.
- Bangla fonts embedded in the PDF; service charge and VAT as separate quote lines.

### Build it with Claude
Stack: Laravel, PostgreSQL, Claude API for contract and quote copy, a small VPS, bKash merchant API, SMS gateway.

1. Ask Claude for the schema: vendors, halls, slots, bookings, quote_items, payments, contracts, sms_log. Check that one venue can hold several halls.
2. Ask Claude to build month and day calendar views that work on a phone, since vendors answer calls on the move.
3. Ask Claude to write the contract and quote templates:
```
Write a Bangla wedding vendor contract template for Bangladesh with placeholders:
{vendor_name}, {client_name}, {event_date}, {slot}, {guest_count}, {per_plate_price},
{package_items}, {total}, {advance_paid}, {balance_due_date}.
Include clauses for guest count changes, cancellation and late payment in plain Bangla. One page.
Also give a 160-character Bangla SMS confirmation.
```
4. Ask Claude for the quote calculator and bKash flow:
```
In Laravel, write a QuoteService that takes guest_count, per_plate_price, package items with prices,
service_charge_percent and vat_percent, and returns a line-by-line breakdown and total.
Then write a controller that creates a bKash payment link for an advance, stores the transaction,
and marks the booking confirmed when the callback succeeds. Include tests.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 vendors in one city using the calendar daily |
| Day 60 | 40 paying vendors, 300 bookings recorded |
| Day 90 | 100 paying vendors, roughly ৳1.5 lakh monthly revenue |

### First customers with zero budget
- Scrape Google Maps for "community center" and "convention hall" in Dhaka, Chattogram, Sylhet and Rajshahi; visit managers before noon.
- Facebook wedding planner groups, city "Bibaho" groups, and decorator and photographer pages that post daily.
- Caterer and decorator associations in each city; ask for a ten-minute demo slot at a meeting.
- Outreach angle: "Never double book a Friday again, and take advances on bKash instead of chasing cash." The demo that closes: enter their next three weekends' bookings live and show the client SMS arriving.
- Referral loop: a photographer on the calendar recommends it to the decorator on the same event, since they share dates.

### Pricing and the maths
- ৳999/month for a solo vendor, ৳1,999 for a venue with several halls or a caterer with a team, ৳2,999 for a multi-branch vendor.
- Cost of goods is SMS, PDF generation and hosting, well under ৳100 per vendor per month; gross margin around 90 percent.
- At the mid price of ৳1,999, roughly 150 paying vendors make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Pakistan. Halls, caterers and decorators run the same way and the season is similar.
- What changes: language pack, payment rail (JazzCash, Easypaisa), contract clauses and the holiday calendar.
- What stays the same: slot calendar, quote builder, advance ledger, SMS reminders.

### Risks and how to de-risk them
- Risk: vendors keep the paper diary alongside the app. De-risk: make the calendar the default screen and suggest a tablet at the front desk.
- Risk: off-season churn from March to October. De-risk: annual plans plus birthday and corporate bookings.
- Risk: a large event portal enters. De-risk: own the vendor's back office; portals send leads, you manage the booking.

## Idea 42: Creator Business Kit in Bangla
*Transcripts, subtitles, titles, sponsorship invoices, brand deal contracts and income tracking for YouTube and Facebook creators.*

### Who pays and why now
Hundreds of thousands of Bangla creators publish on YouTube and Facebook, and a few thousand earn real money from AdSense, bonuses and brand deals. None has business tooling. They skip subtitles, guess at titles, agree brand deals on Messenger without a contract, and do not know what they earned last quarter.

The creator pays because one properly invoiced brand deal covers a year of subscription, and brands prefer creators who send a contract and an invoice. The moment is right because Facebook and YouTube have widened monetisation in Bangladesh and brands are moving budget to creators. The product ports to every language, since transcription, invoicing and income tracking are universal.

### The product in 30 days (MVP)
- Upload or link a video; get a cleaned Bangla transcript and an SRT subtitle file.
- Title, description and tag suggestions in Bangla and English from the transcript.
- Sponsorship invoice generator with logo, ৳ or $ amounts and a bKash or bank line.
- Brand deal contract template in Bangla with deliverables, dates, usage rights and payment terms.
- Income tracker: AdSense, Facebook, brand deals and affiliate income by month, entered or imported from CSV.
- Leave out: video editing, thumbnail generation, a brand marketplace, team roles.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad for subscriptions; SSLCommerz for cards; Stripe later for diaspora creators.
- A speech-to-text API with Bangla support for the first pass, then Claude to fix spelling and punctuation.
- Invoices need an embedded Bangla font and optional TIN and bank fields for brand accounts teams.
- Income import from AdSense and Facebook CSV exports, so no API keys are needed from the creator at launch.

### Build it with Claude
Stack: Next.js, PostgreSQL, a speech-to-text API plus Claude API for cleanup and copy, Cloudflare R2 for files, bKash merchant API.

1. Ask Claude for the schema: creators, videos, transcripts, subtitle_files, invoices, contracts, income_entries, brands. Keep media in object storage and only metadata in PostgreSQL.
2. Ask Claude to build the transcription pipeline as a background job with this cleanup step:
```
I have a raw Bangla speech-to-text transcript as JSON segments with timestamps.
Write a function that sends segments in batches to Claude with the instruction:
"Correct Bangla spelling, add punctuation, keep English words in English, do not change meaning,
keep segment boundaries and timestamps." Then output an SRT file and a plain transcript.
Split any segment over 42 characters into two subtitle lines.
```
3. Ask Claude for the title and description generator:
```
Given a cleaned Bangla transcript of a YouTube video, write 5 title options under 60 characters,
a 150-word Bangla description with a hook in the first line, 15 tags mixing Bangla and English,
and a 2-line Facebook caption. No clickbait, no exclamation marks. Return JSON.
```
4. Ask Claude for the Bangla contract and invoice templates as PDF, and an income dashboard with CSV import for AdSense and Facebook exports.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 100 creators signed up, 500 videos transcribed |
| Day 60 | 150 paying creators, 50 invoices generated |
| Day 90 | 400 paying creators, roughly ৳2.5 lakh monthly revenue |

### First customers with zero budget
- Facebook groups for Bangla YouTubers and content creators are large and active; post a free subtitle demo of a member's video.
- Creator meetups in Dhaka and Chattogram and university media clubs gather rising creators in one room.
- Message Bangla channels with 10k to 200k subscribers and no subtitles through their business email.
- Outreach angle: "Send me your last video and get free Bangla subtitles in ten minutes." The demo that closes: a finished SRT plus five titles for their own video, delivered before the conversation ends.
- Referral loop: the invoice and media kit carry a small "made with" line, and creators show each other their tools on camera.

### Pricing and the maths
- ৳299/month for 5 videos and invoices, ৳599 for 20 videos plus contracts, ৳999 for unlimited videos and a manager view of several channels.
- Cost of goods is transcription minutes and Claude tokens, roughly ৳20 to ৳60 per video; gross margin around 70 percent with plan limits.
- At the mid price of ৳649, roughly 460 paying creators make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Indonesia or Pakistan, both with large creator bases, weak tooling and speech-to-text support.
- What changes: the speech-to-text language, prompt language for titles, contract clauses, payment rail (GoPay, JazzCash) and invoice currency.
- What stays the same: the pipeline, the invoice and contract engine, the income tracker.

### Risks and how to de-risk them
- Risk: platform auto-captions improve and remove the transcription value. De-risk: sell the business layer (invoices, contracts, income) as the core and subtitles as a feature.
- Risk: transcription costs eat margin. De-risk: hard limits per plan and a cheaper model for the first pass.
- Risk: small creators will not pay. De-risk: target creators already earning, and sell to small networks and managers.

## Idea 52: Domestic Tour Operator OS
*Package builder, bKash advances, traveller documents, Bangla itineraries and group broadcasts for small tour operators.*

### Who pays and why now
Thousands of small operators sell Cox's Bazar, Sundarbans, Sajek, Saint Martin and Sylhet packages through Facebook pages. A typical operator runs two to ten trips a month, collects advances on a personal bKash, keeps traveller lists in a notebook and manages vendors by phone. When one traveller drops out, the whole trip is recalculated by hand.

The operator pays because a trip that loses one seat's advance or double-pays a hotel wipes out the profit. Travellers pay faster with a proper bKash link and a Bangla itinerary PDF. The moment is right because domestic tourism has grown fast and travel Facebook groups are enormous. The product ports to Indonesia, Nepal, Egypt, Vietnam, Sri Lanka and Kenya, where small operators sell the same way.

### The product in 30 days (MVP)
- Package builder: destination, dates, seat count, inclusions, per-person price, costing per vendor.
- Trip roster: travellers with phone, NID or passport number, emergency contact and seat.
- bKash advance and balance links per traveller with automatic status update.
- Bangla itinerary PDF with day-by-day plan, meeting point, packing list and operator contact.
- Vendor tracker for bus, hotel, boat and guide: agreed price, paid, due; plus WhatsApp broadcast templates.
- Leave out: a public booking website, hotel inventory integration, a traveller app, reviews.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant APIs for advances and balances; cash and bank recorded manually.
- WhatsApp Business API or copy-to-clipboard broadcasts for group messages; SMS for travellers without WhatsApp.
- Export the traveller list in the format Cox's Bazar and Saint Martin hotels ask for their guest register.
- Store Sundarbans Forest Department permit numbers per trip; Bangla fonts in the itinerary.

### Build it with Claude
Stack: Laravel, PostgreSQL, Claude API for itinerary copy, a small VPS, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema: operators, packages, trips, travellers, payments, vendors, vendor_costs, itineraries, broadcasts, with a trip profit view that subtracts vendor costs from collections.
2. Ask Claude to build the trip screen: roster, payments, vendor costs and profit in one view.
3. Ask Claude for the itinerary generator:
```
Write a Bangla day-by-day itinerary for a 3-day, 2-night group tour from Dhaka to Sajek Valley.
Inputs: departure time and place, bus vendor, hotel names, meals included, sightseeing stops,
return time, operator name and phone. Include a packing list and 5 safety rules in Bangla.
Return JSON with day, time, activity, note fields for PDF rendering. Clear tone, no exclamation marks.
```
4. Ask Claude for the payment and seat logic:
```
In Laravel, write the flow for a trip with N seats: create a bKash payment link per traveller for an advance,
mark the seat held on link creation and confirmed on successful callback, release the seat if unpaid after 24 hours,
and send a Bangla SMS at each step. Add a daily job listing travellers with balance due 3 days before departure.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 5 operators running their next trip on the system |
| Day 60 | 40 paying operators, 1,000 travellers recorded |
| Day 90 | 100 paying operators, roughly ৳1.8 lakh monthly revenue |

### First customers with zero budget
- Travel Facebook groups such as "Travelers of Bangladesh" and destination groups for Sajek, Saint Martin and Sundarbans, where operators post packages daily.
- Facebook pages selling packages: search "Sajek package" and "Cox's Bazar tour package" and message the admins.
- Tour operator associations such as TOAB and travel fairs in Dhaka.
- Outreach angle: "Stop losing seats to unpaid advances. Send a bKash link, get a roster, print a Bangla itinerary." The demo that closes: build their next trip live, send a bKash link to their phone, download the PDF.
- Referral loop: every itinerary PDF has an operator-branded footer, and hotels that receive clean rosters recommend it to other operators.

### Pricing and the maths
- ৳999/month for up to 5 trips a month, ৳1,999 for 15 trips and WhatsApp broadcasts, ৳2,999 unlimited with several staff.
- Cost of goods is SMS and WhatsApp messages plus hosting, roughly ৳50 to ৳150 per operator per month; gross margin around 90 percent.
- At the mid price of ৳1,999, roughly 150 paying operators make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nepal. Small trekking operators in Thamel sell by phone and Facebook and already handle permits per trip.
- What changes: language pack, payment rail (eSewa, Khalti), permit types (TIMS, national parks), vendor categories such as jeep and porter.
- What stays the same: package builder, roster, payment links, itinerary PDF, vendor tracker.

### Risks and how to de-risk them
- Risk: operators are seasonal and churn in the monsoon. De-risk: annual pricing and Eid and winter promotions.
- Risk: operators use a personal bKash and resist a merchant account. De-risk: support manual bKash entry with transaction ID and help them register as a merchant.
- Risk: WhatsApp API costs and approval delays. De-risk: launch with copy-to-clipboard broadcasts and SMS, add the API later.

## Idea 68: NGO Beneficiary and Cash-Transfer Manager
*Offline household registration, beneficiary lists with photos, distribution records and bKash cash transfers with donor-ready reconciliation.*

### Who pays and why now
Bangladesh has one of the densest NGO sectors in the world. Thousands of programmes register households, hand out cash or inputs and report to donors, yet most keep beneficiary lists in Excel, pay cash in envelopes or by manual bKash send-money, and rebuild each donor reconciliation by hand.

The programme manager pays because donors now demand an audit trail: who was registered, who received what, and proof that the money reached a verified phone. A failed audit can end a grant, so a tool that produces the report in the donor's format protects the funding, and budgets in dollars make the price modest for the buyer. The moment is right because donors are pushing digital cash and mobile money is near universal. The product ports to Kenya, Nigeria, Pakistan, Indonesia, Ethiopia and Somalia, where the same NGOs run the same programmes.

### The product in 30 days (MVP)
- Offline-first Android app for household registration in Bangla with photo, NID or birth certificate, GPS and members.
- Beneficiary list with eligibility tags, deduplication by NID and phone, and an approval step.
- Distribution rounds with receipt by QR card scan or photo signature.
- Cash transfer batch to bKash with per-beneficiary status and automatic reconciliation.
- Donor report export in PDF and Excel, and a web dashboard with role-based access.
- Leave out: case management, complaint hotline, biometrics, multi-currency budgets.

### Data, integrations and the Bangladesh specifics
- bKash disbursement (B2C) API for transfers, Nagad as second rail; cash rounds recorded manually.
- Bangla SMS to announce distribution dates and confirm receipt.
- Offline storage with sync when signal returns, since field officers work in char and haor areas.
- A generic donor template with configurable columns; Stripe or bank transfer in dollars for the subscription.

### Build it with Claude
Stack: Flutter Android app with SQLite offline storage, Laravel API, PostgreSQL, Claude API for report narrative, a small VPS, bKash disbursement API, Stripe.

1. Ask Claude for the data model and sync design:
```
Design a data model for an NGO cash-transfer programme in Bangladesh.
Entities: programmes, field_officers, households (GPS, photo, NID, phone), members, eligibility_rules,
beneficiaries, distribution_rounds, receipts, transfer_batches, transfers, audit_log.
Field officers register households offline on Android and sync later. Propose an offline-first sync strategy
with UUID keys, last_modified timestamps and conflict rules. Output PostgreSQL SQL and the SQLite schema.
```
2. Ask Claude to build the Flutter registration form in Bangla with photo, GPS and a duplicate check, then the sync service.
3. Ask Claude for the bKash disbursement batch: call the B2C API per beneficiary, store transaction IDs, retry failures, show reconciliation.
4. Ask Claude for the donor report:
```
Write a Laravel service that produces a donor distribution report for one round.
Inputs: round details, beneficiaries planned, receipts recorded, transfers succeeded and failed with reasons,
total amount, spend by union or ward. Output a PDF and an Excel file.
Then draft a 200-word English narrative from the numbers using Claude, with a section on exceptions
and follow-up actions. Do not invent figures.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 pilot programmes, 1,000 households registered |
| Day 60 | 6 paying programmes, first bKash round of 500 transfers reconciled |
| Day 90 | 15 paying programmes, roughly $2,500 monthly revenue |

### First customers with zero budget
- NGOAB's public list of registered NGOs gives names and districts; district NGO coordination meetings gather directors monthly.
- LinkedIn and Facebook groups for development professionals, where programme managers discuss cash transfer work.
- Local partners of international NGOs in Cox's Bazar, Kurigram and Sunamganj run cash programmes and answer emails.
- Outreach angle: "Your next donor audit in one click: who was registered, who received, and the bKash transaction ID for each." The demo that closes: register five households offline, sync, run a test round to staff phones, export the report.
- Referral loop: donors who receive a clean report ask their other partners to use the same tool.

### Pricing and the maths
- $49/month for one programme up to 1,000 beneficiaries, $149 up to 10,000 with cash transfers, $299 unlimited with donor portal access.
- Cost of goods is SMS, hosting and bKash disbursement fees passed through to the programme; gross margin around 85 percent.
- At the mid price of about $174 (roughly ৳20,000), roughly 15 paying programmes make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya. Cash transfers via M-Pesa are standard, NGOs concentrate in Nairobi, and English reporting needs no translation.
- What changes: disbursement rail (M-Pesa, JazzCash), ID formats, and the field app language pack.
- What stays the same: offline registration, deduplication, rounds and receipts, reconciliation and donor reports; sell through a partner who trains NGO field staff.

### Risks and how to de-risk them
- Risk: long NGO procurement cycles. De-risk: monthly pilots with a free first round, priced so a programme manager can approve it.
- Risk: data protection of beneficiary records. De-risk: encryption at rest, role-based access and a clear data processing agreement.
- Risk: bKash disbursement needs a corporate account. De-risk: the NGO uses its own disbursement account and you integrate with it.

## Idea 76: Security Guard and Manpower Company OS
*Rosters per client site, selfie attendance, shift swaps, client billing and payroll with deductions for security and cleaning contractors.*

### Who pays and why now
Hundreds of security and cleaning contractors deploy tens of thousands of staff to offices, factories, apartment buildings and banks. Rosters live in registers, attendance is signed on paper, and head office reconciles billing against those registers by hand. Clients dispute invoices when a guard was absent, and payroll takes a week with errors in deductions.

The contractor pays because attendance evidence is billing: a photo with time and location proves the shift, so the client pays without argument, and payroll from the same data stops ghost guards. The moment is right because banks, garment factories and multinationals now require documented attendance for their own audits. The product ports to India, Pakistan, Nigeria, Kenya, Indonesia and Egypt, where the same contractors keep the same registers.

### The product in 30 days (MVP)
- Client and site register with required headcount per shift.
- Roster builder per site and month, with shift swaps and replacement guards logged.
- Guard Android app: selfie check-in and check-out with GPS, working on weak signal.
- Supervisor view of who is present at each site right now, with gaps highlighted.
- Client invoice from attended shifts, and a payroll sheet per guard with overtime, advances and deductions in ৳.
- Leave out: bKash salary disbursement, licence and training records, incident reporting, client portal.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant API for the subscription; payroll disbursement to bKash in a later version.
- Bangla SMS to guards for roster changes and payslips.
- Selfie and GPS must work on cheap Android phones; supervisor check-in as fallback.
- Payroll fields for weekly rest day, overtime rate and festival bonus; photos compressed with 90-day retention.

### Build it with Claude
Stack: Flutter Android app for guards, Next.js for head office, PostgreSQL, Cloudflare R2 for photos, Claude API for roster suggestions, a small VPS, bKash merchant API.

1. Ask Claude for the schema: companies, clients, sites, shift_types, guards, rosters, roster_slots, attendance (photo_url, lat, lng, time, method), invoices, payroll_runs, deductions, plus a planned-versus-attended view per site per day.
2. Ask Claude to build the guard app:
```
Build a Flutter screen for a security guard to check in at a site. Show the assigned site and shift.
On tap, capture a selfie with the front camera, read GPS, and post to /attendance with guard_id,
roster_slot_id, photo, lat, lng, timestamp. If offline, queue locally and retry.
Show a green "উপস্থিত" badge on success. Bangla labels, large buttons, works on Android 8 and a 2GB phone.
```
3. Ask Claude for the invoice and payroll calculators:
```
In TypeScript, write buildInvoice(site, month): sum attended shifts by shift_type, apply the client's rate card
and overtime rule, return line items and total. Write buildPayroll(guard, month): sum shifts and overtime,
subtract advances and deductions, add festival bonus if flagged, return a payslip object.
Include unit tests for a guard with 26 days, 4 overtime shifts and a 2000 taka advance.
```
4. Ask Claude for the supervisor dashboard with SMS gap alerts, Bangla payslip PDFs and an English client invoice.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 companies, 300 guards checking in daily |
| Day 60 | 8 paying companies, 1,500 guards on the platform |
| Day 90 | 20 paying companies, roughly 4,000 guards, about ৳3 lakh monthly revenue |

### First customers with zero budget
- Scrape Google Maps for "security guard service" in Dhaka, Chattogram and Gazipur and call the operations managers.
- The security services owners' association and cleaning contractor groups meet regularly; ask for a ten-minute slot.
- Facebook groups for "security guard job" have supervisors and small company owners posting daily.
- Outreach angle: "Stop losing invoice disputes. Every shift has a photo, a time and a location." The demo that closes: install the app on a supervisor's phone, check in from the meeting room, and watch the invoice line update.
- Referral loop: clients who see photo-verified attendance ask their other contractors for the same.

### Pricing and the maths
- ৳49 per guard per month for attendance and rosters, ৳99 per guard per month with invoicing and payroll; minimum ৳1,999 per company.
- Cost of goods is photo storage, SMS and hosting, well under ৳10 per guard per month; gross margin around 85 percent.
- At the mid price of ৳74 per guard, roughly 4,000 guards, for example 20 companies with 200 guards each, make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Kenya or Nigeria, where private security is a large industry and clients already demand attendance proof.
- What changes: language pack (Swahili, Hausa, Urdu), payroll rules and statutory deductions, payment rail (M-Pesa, JazzCash).
- What stays the same: rosters, selfie and GPS attendance, invoice from attended shifts, payroll engine.

### Risks and how to de-risk them
- Risk: guards do not own smartphones. De-risk: supervisor check-in on one shared phone per site and a site QR code.
- Risk: fake selfies and GPS spoofing. De-risk: live capture in app, a distance check from the site, and random supervisor verification.
- Risk: head office fears losing control. De-risk: an editable roster and manual attendance corrections with an audit trail.

## Idea 77: Visa and Travel Consultancy CRM
*Document checklists per country, appointment and biometrics tracking, embassy fee ledger, WhatsApp status updates and refusal history for visa consultancies.*

### Who pays and why now
Thousands of visa consultancies in Dhaka, Chattogram and Sylhet help students, workers and tourists apply to Canada, the UK, Australia, Malaysia, Schengen countries and the Gulf. Each applicant means a folder of documents, an embassy fee, a biometrics appointment and weeks of waiting. Consultants keep paper files and answer the same "any update?" message all day.

The consultant pays because a missed appointment or an expired bank statement means a refusal, a lost fee and an angry client. A checklist that turns red when a document is missing or old, and a status link the applicant can open, protect the consultant's reputation. The moment is right because student and worker visa demand is high and embassies keep changing requirements. The product ports to India, Pakistan, Nigeria, Nepal and Sri Lanka, where consultancies serve the same destinations.

### The product in 30 days (MVP)
- Applicant profile with passport, contacts, destination, visa type and assigned consultant.
- Document checklist per destination and visa type, with upload, expiry date and status.
- Timeline: form submitted, fee paid, biometrics booked, appointment date, decision.
- Fee ledger: consultancy fee, embassy and VFS fees, courier, translations, paid and due.
- Applicant status link with a WhatsApp or SMS message at each step, and a refusal record with reason category.
- Leave out: filling embassy portals automatically, ticket booking, university applications, accounting.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant APIs for consultancy fees; embassy fees recorded manually.
- WhatsApp Business API or click-to-chat templates for status updates, with SMS fallback.
- A checklist library per destination that you maintain and consultants can copy and edit.
- Bangla applicant messages, English internal records, and Claude reading dates from passport and bank statement scans.

### Build it with Claude
Stack: Next.js, PostgreSQL, Claude API for document reading and message copy, Cloudflare R2 for files, a small VPS, bKash merchant API, WhatsApp Business API.

1. Ask Claude for the schema: consultancies, staff, applicants, destinations, visa_types, checklist_templates, checklist_items, documents, timeline_events, fees, refusals, messages, with staff seeing only their own applicants.
2. Ask Claude to draft the checklist library:
```
Create a JSON checklist template for a Bangladeshi applicant for each of: Canada study permit,
UK standard visitor, Malaysia work visa via employer, Thailand tourist, Schengen tourist, Saudi work.
For each item give: name in English and Bangla, required or optional, validity in days if it expires, and a one-line note.
Label the output "starting template, verify against the embassy website" and do not invent fees.
```
3. Ask Claude for the applicant page with checklist, timeline and fee ledger, plus a signed-URL public status page.
4. Ask Claude for the document reader and message templates:
```
Write a Node function that sends a passport or bank statement image to Claude and returns JSON:
document_type, holder_name, number_if_any, issue_date, expiry_or_statement_end_date, confidence.
Then write Bangla WhatsApp templates under 300 characters for: documents received, form submitted,
biometrics booked on {date} at {centre}, decision received (collect passport), and a gentle
"documents still missing: {list}" reminder. No promises about approval.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 consultancies live with 200 applicants loaded |
| Day 60 | 20 paying consultancies, 1,500 status messages sent |
| Day 90 | 60 paying consultancies, roughly ৳1.8 lakh monthly revenue |

### First customers with zero budget
- Scrape Google Maps for "visa consultancy" in Banani, Dhanmondi, Uttara, Chattogram and Sylhet and visit in the afternoon.
- Bangla Facebook groups for student visas and immigration have consultants answering questions daily; message the active ones.
- Education consultancy associations and the travel agents' association ATAB hold meetings and fairs.
- Outreach angle: "Your applicants message you all day for updates. Send them a link instead." The demo that closes: upload a passport photo, watch the expiry auto-fill, send a status WhatsApp to the consultant's phone.
- Referral loop: applicants see the branded status page and ask other consultants for the same.

### Pricing and the maths
- ৳1,499/month for one consultant and 50 active applicants, ৳2,999 for a team of five and 300 applicants, ৳4,999 for several branches and unlimited applicants.
- Cost of goods is messages, file storage and a little Claude usage, roughly ৳100 per consultancy per month; gross margin around 90 percent.
- At the mid price of ৳3,249, roughly 95 paying consultancies make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nepal. Kathmandu is dense with consultancies serving the same destinations.
- What changes: language pack, payment rail (eSewa, Khalti), and local document types such as a citizenship certificate instead of NID.
- What stays the same: checklist engine, timeline, fee ledger, status page; destination templates are largely shared.

### Risks and how to de-risk them
- Risk: a checklist goes out of date and a consultant blames you for a refusal. De-risk: date-stamp templates as starting points and let consultants own their edited copy.
- Risk: consultants fear applicant data leaking to competitors. De-risk: per-consultancy data isolation, no cross-tenant analytics, a clear privacy statement.
- Risk: WhatsApp API approval and cost. De-risk: start with click-to-chat and SMS, add the API once volume justifies it.

## Idea 82: Billboard and Outdoor Ad Inventory Manager
*Site inventory with photos and location, availability calendar, client bookings, proof-of-display photos and invoicing for outdoor media owners.*

### Who pays and why now
Hundreds of outdoor media owners control billboards, unipoles, bus shelters and LED screens along highways and city roads, and sell them to brands and agencies from a spreadsheet and a folder of photos. When an agency asks what is free in Gulshan in March, the owner scrolls and sends WhatsApp photos. When the campaign runs, someone drives out to photograph the poster, and the proof lives in a phone gallery.

The owner pays because empty inventory is lost revenue and slow answers lose deals. A shareable availability page closes faster, and proof photos with date and GPS stop disputes and speed up payment. The moment is right because brands demand documented campaigns and agencies buy across several owners. The product ports to India, Pakistan, Nigeria, Indonesia, Egypt and Kenya, where outdoor media is sold the same way.

### The product in 30 days (MVP)
- Site inventory: type, size, lighting, GPS, photos, rate card, landlord and permit details.
- Availability calendar per site with booked, held and free periods.
- Booking record: client, agency, campaign, sites, dates, agreed rate, artwork status.
- Proof-of-display photos from a phone with date and GPS, grouped per campaign, and a client report link.
- Invoice per booking with a VAT line and payment tracking.
- Leave out: programmatic screens, impression estimates, mounting scheduling, an agency marketplace.

### Data, integrations and the Bangladesh specifics
- bKash, Nagad and bank for client payments; most agencies pay by bank transfer, recorded with a reference.
- WhatsApp for sharing availability links and proof reports.
- City corporation permit and fee records per site with renewal reminders.
- Photos compressed into object storage with GPS and time from EXIF or the browser; English invoices with a VAT line.

### Build it with Claude
Stack: Next.js, PostgreSQL, Cloudflare R2 for photos, Claude API for report text, a small VPS, bKash merchant API.

1. Ask Claude for the schema: owners, sites, site_photos, rate_cards, clients, agencies, bookings, booking_sites, proofs, invoices, payments, permits, with a constraint so bookings cannot overlap on one site.
2. Ask Claude to build the inventory map and calendar:
```
Build a Next.js page that shows all sites on a Leaflet map with filters for city, type and availability
between two dates. Clicking a site opens a card with photos, size, rate and a 12-month availability strip.
Add a "share availability" button that creates a signed public URL listing the filtered sites,
valid for 7 days, with rates hidden unless the owner toggles them on.
```
3. Ask Claude for the proof flow: a mobile page where field staff pick the site, take a photo, and the app records time and GPS and warns if more than 200 metres away.
4. Ask Claude for the client report and invoice:
```
Write a service that generates a campaign completion report PDF for an outdoor media client.
Inputs: client, campaign name, sites with address and GPS, booking dates, proof photos with timestamps.
Layout: one site per row with thumbnail, address, first and last proof date.
Add a short English summary paragraph from the data using Claude, no marketing language.
Also generate an invoice PDF with line items per site, VAT at the given percent, and payment terms.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 2 owners with 100 sites loaded and photographed |
| Day 60 | 10 paying owners, 30 campaigns with proof photos |
| Day 90 | 30 paying owners, roughly ৳1 lakh monthly revenue |

### First customers with zero budget
- Billboards carry the owner's name and phone number at the bottom; photograph fifty in Dhaka and call the numbers.
- Media buyers at advertising agencies, reachable on LinkedIn, can name the owners they buy from.
- Facebook groups for outdoor advertising and signboard makers include small owners.
- Outreach angle: "Answer an agency's availability question in one minute, and send proof photos the day the poster goes up." The demo that closes: load ten of their sites, share an availability link to their phone, upload a proof photo from the street.
- Referral loop: agencies that receive the proof report ask their other media owners for the same.

### Pricing and the maths
- ৳1,499/month for up to 50 sites, ৳2,999 for up to 200 sites with client reports, ৳4,999 unlimited with several staff and branches.
- Cost of goods is photo storage and hosting, under ৳100 per owner per month; gross margin above 90 percent.
- At the mid price of ৳3,249, roughly 95 paying owners make ৳3 lakh a month, so plan port countries early.

### Country kit: taking it to other languages
- First port: Nigeria. Lagos has a large outdoor market sold from spreadsheets, and English needs no translation.
- What changes: currency and VAT rules, regulator permit records such as LASAA in Lagos, payment rail and address formats.
- What stays the same: inventory, calendar, bookings, proof photos, reports, invoices.

### Risks and how to de-risk them
- Risk: the market is small in Bangladesh alone. De-risk: plan the first port by day 60 and price higher tiers for large owners.
- Risk: field staff skip proof photos. De-risk: a campaign shows red until every site has a proof, visible to the owner daily.
- Risk: agencies build their own tools. De-risk: give agencies a free read-only view so they prefer owners who use you.

## Idea 84: Remote Staffing Agency OS
*Contracts, timesheets with screenshots, USD invoicing via Stripe, BDT payroll to bKash and margin per seat for VA and outsourcing agencies.*

### Who pays and why now
Hundreds of Bangladeshi agencies place virtual assistants, designers, developers and support staff with clients in the US, UK and Australia. The agency signs the client, hires the staff, bills in dollars and pays in taka, all on Google Sheets, a time tracker the client does not trust, Payoneer invoices and a monthly scramble to work out who earned what.

The owner pays because margin per seat is the whole business and nobody can see it. A client who sees hours with screenshots pays on time and stays, and staff who get a payslip and a bKash transfer on the first do not leave. The moment is right because remote hiring by Western small businesses keeps rising, and dollar-in, mobile-money-out is a flow global tools do not handle. The product ports to the Philippines, Pakistan, Kenya, Nigeria, India and Egypt.

### The product in 30 days (MVP)
- Client records with contract, seats, hourly or monthly USD rate, billing cycle and payment terms.
- Staff records with role, assigned client, BDT salary, bKash number and start date.
- Timesheet: staff log hours per day with task notes and optional screenshot uploads.
- Client portal: hours, screenshots and notes per staff member, timesheet approval, invoices.
- USD invoice with a Stripe payment link per cycle, and a BDT payroll sheet showing margin per seat.
- Leave out: recruitment pipeline, applicant tests, a desktop tracking app, currencies beyond USD and BDT.

### Data, integrations and the Bangladesh specifics
- Stripe for USD invoices and cards; Wise or Payoneer recorded manually; bKash and bank for BDT payroll.
- Record the exchange rate used for each payroll run so margin reports are honest.
- Screenshots in object storage with 60-day retention and client-level access.
- A monthly earnings summary for bank export proceeds paperwork; Bangla interface for staff, English for clients.

### Build it with Claude
Stack: Next.js, PostgreSQL, Cloudflare R2 for screenshots, Stripe, Claude API for weekly client summaries, a small VPS, bKash merchant API.

1. Ask Claude for the schema and access model:
```
Design a PostgreSQL schema for a remote staffing agency in Bangladesh serving US and UK clients.
Tables: agencies, clients, contracts (seat_count, rate_usd, rate_type hourly or monthly, billing_cycle),
staff (salary_bdt, bkash_number), assignments, timesheets, timesheet_entries, screenshots,
invoices_usd, stripe_payments, payroll_runs (fx_rate), payslips. Roles: owner, client user, staff.
Add a view margin_per_seat = USD billed minus BDT salary at the run's fx_rate.
```
2. Ask Claude for the Bangla staff timesheet screen and the English client portal with approval and comments.
3. Ask Claude to wire Stripe: create an invoice per client per cycle from approved hours, send a payment link, mark paid on webhook.
4. Ask Claude for the weekly client summary and payslip copy:
```
Write a function that takes one week of timesheet entries for a staff member (date, hours, task notes)
and asks Claude for a 120-word English summary for the client: what was done, total hours, anything blocked.
No fluff, no invented tasks. Then produce Bangla and English payslip text with month, hours,
base salary in taka, bonus, deductions, net pay and the bKash number paid to.
```

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 agencies, 40 seats, first Stripe invoice paid |
| Day 60 | 10 paying agencies, 200 seats |
| Day 90 | 20 paying agencies, roughly 400 seats, about $2,800 monthly revenue |

### First customers with zero budget
- Facebook groups for Bangladeshi freelancers and agency owners, and LinkedIn founders advertising VA services to US clients.
- Upwork and Fiverr agency profiles based in Dhaka list the owner's name; connect on LinkedIn.
- BASIS events and freelancer meetups in Dhaka, Sylhet and Rajshahi gather agency owners.
- Outreach angle: "See your margin per seat every day, and give clients a portal that gets you paid on time." The demo that closes: enter one client and two staff, upload a day of timesheets, generate the invoice, show the margin.
- Referral loop: clients who like the portal recommend the agency, and agency owners talk in the same groups.

### Pricing and the maths
- $5 per seat per month for timesheets and payroll, $9 per seat per month with client portal and Stripe invoicing; minimum $29 per agency.
- Cost of goods is screenshot storage, Stripe fees passed through and a little Claude usage; gross margin around 85 percent.
- At the mid price of $7 per seat (roughly ৳840), roughly 360 seats, for example 12 agencies with 30 seats each, make ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: the Philippines. It has the largest VA agency sector, the English interface works as is, and GCash replaces bKash.
- What changes: payroll rail (GCash, JazzCash, M-Pesa), local payslip and tax fields, staff interface language pack.
- What stays the same: contracts, timesheets, screenshots, client portal, Stripe invoicing, margin reports.

### Risks and how to de-risk them
- Risk: agencies already use a time tracker. De-risk: import its CSV and position as the money layer on top, not the tracker.
- Risk: Stripe access from Bangladesh. De-risk: support manual invoice status for Payoneer users and add Stripe where the agency has a US or UK entity.
- Risk: staff object to screenshots. De-risk: make screenshots optional per contract and blur sensitive windows.

## Idea 91: Local Event Ticketing
*bKash ticketing, QR gate scanning, seat categories and organiser settlement for concerts, fairs, matches and cultural nights.*

### Who pays and why now
Every week someone organises a concert, a fair, a football or cricket match, a cultural night or a reunion. Tickets are printed and sold from shops and friends' phones, and the gate is a table with a torn-stub box. Nobody knows how many tickets were sold, how many were fake, or how much cash each seller holds.

The organiser pays a small percentage because it replaces a bigger loss: fake tickets, sellers who do not settle, and a gate that jams. A bKash link sold from a Facebook post reaches more buyers than ten shops, the gate app refuses duplicates, and settlement arrives with a report the sponsor can read. The moment is right because bKash and Facebook are in every buyer's hand. The product ports to Indonesia, Nigeria, Pakistan, Kenya and Egypt with the local wallet.

### The product in 30 days (MVP)
- Event page in Bangla and English with date, venue, ticket categories and quantities.
- bKash and Nagad checkout with a QR ticket delivered by SMS and a web link.
- Promo codes and general admission categories; seat maps later.
- Gate scanner app: scans QR, shows green or red, works offline with a synced list.
- Organiser dashboard with sales by category, gate check-ins, refunds and a settlement statement per event.
- Leave out: numbered seat maps, resale, shop printing, multi-day passes.

### Data, integrations and the Bangladesh specifics
- bKash and Nagad merchant APIs for checkout; SSLCommerz for cards; cash sales recorded by the organiser with a QR issued.
- Bangla SMS delivery of the ticket link; WhatsApp optional.
- The scanner downloads valid tickets before the event and syncs scans afterwards, since venues have weak signal.
- Fields for police permission and venue letter numbers, which large events must show.

### Build it with Claude
Stack: Next.js, PostgreSQL, Flutter scanner app, Claude API for event copy, Cloudflare, bKash and Nagad merchant APIs, SMS gateway.

1. Ask Claude for the schema: organisers, events, ticket_types, orders, tickets with a signed QR token, payments, scans, settlements, promo_codes, with a constraint so a token cannot be used twice.
2. Ask Claude to build checkout and delivery:
```
Build a Next.js checkout for an event: choose ticket type and quantity, enter name and phone,
pay via bKash merchant API. On successful callback create tickets with an HMAC-signed QR token,
send a Bangla SMS with a short ticket link, and show the QR on the page.
Handle duplicate callbacks idempotently. Cap 10 tickets per order and stop sales when a type sells out.
```
3. Ask Claude to build the gate scanner:
```
Build a Flutter app for event gate staff. Log in with an event code and download valid ticket tokens to local storage.
Scan a QR, verify the HMAC locally, check the token exists and is unused, mark it used with a timestamp,
and show a full-screen green tick or red cross with the reason: already used, wrong event, invalid.
Sync scans to the server whenever online. Bangla labels.
```
4. Ask Claude for the organiser dashboard, the settlement statement, and Bangla event page copy templates.

### Launch in 30, 60, 90 days
| Milestone | Target |
|---|---|
| Day 30 | 3 events ticketed, 1,500 tickets sold and scanned |
| Day 60 | 12 events, ৳25 lakh in ticket sales |
| Day 90 | 30 events, ৳75 lakh in ticket sales, roughly ৳3 lakh in fees |

### First customers with zero budget
- University cultural clubs and alumni associations in Dhaka, Chattogram, Rajshahi and Sylhet run events monthly and post in Facebook groups.
- Concert promoters and band pages announce shows on Facebook; message them before tickets go on sale.
- District sports associations and fair committees, reachable through local press and Facebook pages.
- Outreach angle: "Sell tickets from your Facebook post with bKash, and know at the gate exactly who paid." The demo that closes: create their event page in five minutes, buy a ৳10 test ticket on the organiser's phone, scan it at the table.
- Referral loop: every ticket carries the platform name, and attendees who bought once find the next event on the same site.

### Pricing and the maths
- 3 percent per ticket for organisers selling over ৳5 lakh, 5 percent below that, minimum ৳999 per event; the organiser can pass the fee to the buyer.
- Cost of goods is bKash merchant fees, SMS per ticket and hosting; gross margin around 70 percent after payment fees.
- At the mid rate of 4 percent, roughly ৳75 lakh a month in ticket sales, for example 15 events selling ৳5 lakh each, makes ৳3 lakh a month.

### Country kit: taking it to other languages
- First port: Nigeria. Lagos has a huge live event scene, tickets are sold by WhatsApp and bank transfer, and English needs no translation.
- What changes: payment rail (Paystack, Flutterwave, M-Pesa, JazzCash), SMS provider, currency and local permit fields.
- What stays the same: event pages, QR tickets, offline gate scanner, dashboard, settlement.

### Risks and how to de-risk them
- Risk: bKash merchant onboarding for many small organisers. De-risk: hold the merchant account yourself and settle to organisers after the event.
- Risk: organisers who cancel events. De-risk: settle after the event, verify organisers, hold a reserve for refunds.
- Risk: gate congestion with slow phones. De-risk: offline scanning, several gate devices, and manual lookup by phone number.

# Part 3: Choosing, Bundling and the Index

## Chapter 9: How to choose your first idea

Score each idea you are considering from 1 to 5 on the six questions below. Multiply by the weight. The highest total is your first build. Do this honestly, with your own situation, not the market's.

| Question | Weight | What a 5 looks like |
|---|---|---|
| Do I know this customer personally? | 3 | I have worked in or around this trade, or my family has |
| Can I reach 100 of them in 30 days without money? | 3 | They are in groups, associations or on Google Maps and I can get introductions |
| Will they pay in the first month? | 2 | The product replaces a cost they already pay or a loss they already feel |
| Can I ship the MVP in 30 days with Claude? | 2 | No hard integration, no regulatory approval before launch |
| Is the country kit small? | 1 | Language pack plus payment rail, at most one local dataset |
| Does it pay in dollars, now or later? | 1 | Diaspora, NGOs, agencies or global users are natural customers |

A score above 45 out of 60 is a strong first product. Between 35 and 45, it works if you have a reseller or association lined up. Below 35, choose another.

Two more filters. Prefer the idea where the customer's own revenue depends on your product working, because those customers do not churn. And prefer the idea that produces data nobody else has, because that is the moat that survives the next AI model.

## Chapter 10: Bundles that sell together

Many ideas in this book share a customer or a channel. Building two or three of them as one suite raises the price, lowers churn, and gives a reseller more to sell. These are the natural bundles.

- **Local business suite:** Local Business AI Presence (1), WhatsApp AI Receptionist (2), Local Shop Loyalty (95), QR Menu and Ordering (3). One shop, one login, four problems solved.
- **Seller suite:** F-commerce AI Sales Agent (6), Cottage Food Brand OS (36), Course Creator Platform (94), Hishab accounting (5).
- **Health suite:** Doctor's Prescription Writer (8), Pharmacy POS (19), Diagnostic Lab Report Delivery (25), Private Clinic OS (87), all sharing one drug database.
- **Rural stack:** Agri Input Shop Ledger (12), Paravet Field App (50), Deep Tube Well Ledger (81), Poultry and Fish Farm Manager (17), Milk Collection Centre (55), sold through feed and input companies.
- **Religious institution suite:** Mosque Fund Manager (11), Hifz Madrasa Tracker (26), Hajj and Umrah Agency OS (14), Orphanage Sponsorship Manager (61).
- **Property suite:** Landlord App (13), Flat Owners' Association (44), Market Committee Manager (58), Student Hostel Manager (59), Expat Property Caretaker (74).
- **Families abroad suite:** Expat Property Caretaker (74), Online Quran and Bangla Tutor Agency (85), Home Care Agency OS (90), Chronic Care Companion (100), Orphanage Sponsorship (61), all paid in dollars through Stripe.
- **Paperwork suite:** Bureaucracy Assistant (9), Legal Document Generator (24), Inheritance and Land Manager (60), Union Digital Centre Toolkit (48), Import-Export Assistant (35).
- **People-business suite:** SME Payroll (46), Security and Manpower OS (76), Remote Staffing Agency OS (84), Home Care Agency OS (90), all priced per person.
- **Transport suite:** Vehicle Owner Fleet Ledger (28), Vehicle Workshop Job Cards (88), Used Vehicle Dealer (53), Filling Station Manager (71), Easy-Bike Charging Ledger (62).

## Chapter 11: A closing note

Every idea in this book is a small business first. None of them needs venture capital. Most of them can reach a comfortable income for a small team within a year from a few hundred customers who pay because the product saves them money they can see.

What they need is someone who knows the customer, ships every week, listens more than they pitch, and uses Claude for everything that does not require being in the room. That is a new kind of company: five people, one language at a time, one country kit at a time, a hundred customers at a time.

Build one. Then build the country kit. Then build the next one.

## Chapter 12: Index of the 103 ideas

Ideas are listed by section with their number, so you can find any chapter in Part 2.


**Local Business and Commerce**

- 1. Local Business AI Presence
- 2. WhatsApp AI Receptionist and Booking
- 3. QR Menu and WhatsApp Ordering
- 4. AI Phone Answering for Local Businesses
- 6. F-commerce AI Sales Agent
- 22. Tailor Shop OS
- 32. Repair Shop Ticketing
- 41. Printing Press and Signboard Job Manager
- 43. Furniture and Interior Workshop Tracker
- 88. Vehicle Workshop Job Cards
- 92. Mobile Phone Shop EMI Ledger
- 93. Optical Shop and Lens Lab Manager
- 95. Local Shop Loyalty and SMS Marketing

**Health**

- 8. Doctor's Prescription Writer
- 19. Pharmacy POS with Drug Database
- 25. Diagnostic Lab Report Delivery
- 50. Paravet Field App
- 56. Pharma Medical Rep CRM
- 69. Community Health Worker App
- 80. Medical Tourism Facilitator CRM
- 86. Rural Medical Practitioner App
- 87. Private Clinic and Small Hospital OS
- 90. Home Care and Nursing Agency OS
- 99. Counsellor Practice and Teletherapy
- 100. Chronic Care Companion in Bangla
- 102. Private Ambulance Dispatch

**Education and Training**

- 7. Coaching-Centre OS
- 23. Bangla AI Exam Tutor
- 26. Hifz and Quran Madrasa Tracker
- 38. Sports Academy Manager
- 51. Driving School Manager
- 79. Vocational Training Centre Manager
- 85. Online Quran and Bangla Tutor Agency
- 94. Course Creator Platform in Local Currency

**Agriculture and Food**

- 12. Agri Input Shop Ledger
- 17. Poultry and Fish Farm Manager
- 27. Qurbani Cattle Fattening and Marketplace
- 33. Cold Storage Management
- 34. Wholesale Arot Ledger
- 36. Cottage Food Brand OS
- 49. Tea Garden Management
- 54. Rice Mill Management
- 55. Milk Collection Centre Ledger
- 66. Fishing Boat Owner Ledger
- 78. Office Tiffin and Catering Subscription Manager
- 81. Deep Tube Well Water-Selling Ledger
- 89. Contract Farming Aggregator OS
- 97. Beekeeper Management
- 101. Plant Nursery and Landscaping Manager

**Manufacturing, Trade and Industry**

- 18. Small Garment Factory OS
- 35. Import-Export Paperwork Assistant (working name Amdani)
- 40. Brick Kiln and Construction Supplier Ledger
- 45. Jewellery Shop OS
- 57. Distributor Route Sales App
- 63. Artisan Producer Group OS
- 67. Scrap Dealer Ledger
- 103. Small Leather Unit Management

**Property and Construction**

- 13. Landlord App
- 20. Small Contractor Job Costing
- 29. Real Estate Developer and Agent CRM
- 30. Budget Hotel and Guesthouse Manager
- 44. Flat Owners' Association Manager
- 58. Market Committee Manager
- 59. Student Hostel and PG Manager
- 74. Expat Property Caretaker Platform
- 98. Construction Site Daily Reporting

**Transport and Logistics**

- 28. Vehicle Owner Fleet Ledger
- 37. Bus Counter and Trip Accounts
- 39. Service Contract Manager for Installers
- 47. Delivery Route Ledger (Water, LPG, Milk)
- 53. Used Vehicle and Motorbike Dealer Inventory
- 62. Easy-Bike Charging Garage Ledger
- 71. Filling Station Manager
- 73. Launch and River Cargo Operator OS
- 75. Truck and Goods Transport Agency OS

**Religion and Community**

- 11. Mosque, Madrasa and Community Fund Manager
- 14. Hajj and Umrah Agency OS
- 16. Samity and Savings-Group App
- 61. Orphanage and Child Sponsorship Manager
- 70. Election Campaign Manager
- 72. Matrimonial Bureau CRM
- 83. Association and Club Membership Manager

**Money, Compliance and Government**

- 5. Hishab: Automated Bangla Accounting
- 9. Bureaucracy Assistant
- 10. Freelancer Money OS
- 24. Legal Document Generator and Lawyer Case Diary
- 31. Insurance Agent CRM
- 46. SME Payroll in Bangla
- 48. Union Digital Centre Toolkit
- 60. Inheritance and Family Land Manager
- 64. Mobile Money Agent Ledger
- 65. Local ISP and Cable Operator Billing
- 96. Money Changer Ledger and Compliance

**Services, Agencies and People Businesses**

- 15. Overseas Recruitment Agency OS
- 21. Wedding Vendor Booking
- 42. Creator Business Kit in Bangla
- 52. Domestic Tour Operator OS
- 68. NGO Beneficiary and Cash-Transfer Manager
- 76. Security Guard and Manpower Company OS
- 77. Visa and Travel Consultancy CRM
- 82. Billboard and Outdoor Ad Inventory Manager
- 84. Remote Staffing Agency OS
- 91. Local Event Ticketing
