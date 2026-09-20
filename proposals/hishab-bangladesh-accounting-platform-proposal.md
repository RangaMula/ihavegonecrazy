# Hishab (হিসাব) — End-to-End Automated Accounting for Bangladeshi SMEs

**Proposal · Rabbit's Hat · 20 September 2026 · Working name, pending trademark check**

---

## 1. Executive summary

Bangladesh has millions of small businesses, NGOs and service firms that keep their books in a paper khata, a WhatsApp thread, or a spreadsheet, because every accounting product available to them was designed for an accountant, in English, around bank cards. Their real money moves through bKash, Nagad, Rocket and cash, and their receipts are photos.

Hishab is a cloud and mobile accounting platform, Bangla-first, that removes data entry as the core job. Money movements arrive automatically from mobile financial services (MFS) and banks through APIs where they exist and through transaction SMS everywhere else. Receipts, invoices, bank slips and even handwritten khata pages are photographed or forwarded, read by AI, translated between Bangla and English, and posted as proper double-entry journal entries. The owner reviews exceptions instead of typing transactions.

Under the hood there is one rigorous double-entry ledger. On top of it there are organisation-type setups: choose "retail shop", "service firm", "NGO / non-profit" or "trading business" during onboarding and the chart of accounts, document types, vocabulary and reports change to match, while the accounting stays standard and audit-ready.

The product should feel as simple as a cashbook app on day one, and grow into full VAT, tax and donor reporting without the user ever seeing a debit or credit unless they want to.

---

## 2. The market and the problem

**Who we are building for**

- Retail and stationery shops, pharmacies, small groceries, mobile and electronics shops.
- Service firms: software houses, agencies, consultancies, clinics, coaching centres, freelancers.
- NGOs, charitable trusts, madrasa and school committees, clubs, waqf and community funds.
- Small trading and wholesale businesses buying on credit and selling on credit.

**What their day looks like**

- Payments come in over bKash or Nagad personal or merchant wallets, some cash, some bank transfer. Each one triggers an SMS. Nobody records it in a ledger.
- Purchases produce a thermal receipt, a handwritten cash memo, or a Mushak-6.3 VAT invoice. It goes in a drawer or a WhatsApp group.
- A part-time accountant comes monthly, reconstructs the month from those scraps, and files VAT or tax returns from a spreadsheet.
- Owners think in Bangla, write amounts in Bangla numerals, and mix English product names into Bangla sentences.
- NGOs must report to donors by project and to the NGO Affairs Bureau on FD forms, and most do it by hand.

**Why existing tools fail them**

- QuickBooks, Xero, Zoho: English only, foreign pricing in dollars, no MFS awareness, built for card-and-bank economies.
- Local ERP and accounting products: desktop era, accountant-centric, heavy implementation, weak mobile.
- Cashbook apps: excellent simplicity, but single-entry, no VAT, no reports an accountant or donor will accept.

The gap is a product that is as easy as a cashbook, as correct as an accountant, and that understands how money actually moves in Bangladesh.

---

## 3. Product principles

1. **Bangla is the default, not a translation.** UI, notifications, reports and help are written in Bangla first, with English as a one-tap switch per user. Every user chooses their own language. Data can be entered in either language, or mixed, and is stored so both interfaces read it correctly.
2. **Zero-entry accounting.** The system should capture at least 80% of transactions without a human typing them: feeds, SMS, uploaded documents, natural language, voice.
3. **Fit the organisation, not the accountant.** Users pick what they are. The app shows the books that organisation needs, in its own vocabulary, and hides the rest.
4. **Same engine underneath.** One double-entry ledger, one audit trail, one report generator. Templates configure it, they never fork it.
5. **Mobile and low-bandwidth first.** Android is where the customer is. Everything must work offline and sync later.
6. **Trust through transparency.** Every automated entry shows its source (SMS, API, photo) and confidence. Nothing is hidden from the accountant.

---

## 4. What the product does

### 4.1 Automated money capture

| Source | How Hishab captures it | Coverage |
|---|---|---|
| bKash, Nagad, Rocket, Upay merchant accounts | Official merchant APIs: payment callbacks, transaction query, settlement reports | Any business with a merchant wallet |
| bKash, Nagad, Rocket, Upay personal wallets | Transaction SMS read by the Android app and parsed on-device | Every wallet in the country, no API needed |
| Banks with APIs (a handful of private banks expose fintech APIs; Bangladesh Bank's open-banking work is expanding this) | Direct feed adapters, one per bank, added as access is granted | Grows over time |
| All other banks | Transaction alert SMS parsing; monthly statement PDF or CSV upload read by AI | Universal fallback |
| Payment gateways (SSLCommerz, aamarPay, ShurjoPay, Stripe for export businesses) | Webhook feeds | Online sellers |
| Cash | Quick cash-in / cash-out screen, voice entry, cash counter close | Everyone |

Every captured movement lands in an **inbox** as a proposed entry with a suggested counterparty and account. Rules and machine learning categorise it. High-confidence items post automatically. The rest wait for a one-tap confirmation.

The SMS path matters most. Every MFS and bank in Bangladesh sends an SMS for every transaction, so SMS parsing gives complete coverage from day one, before any API partnership is signed. Parsing runs on the phone, and only the structured result (amount, counterparty, reference, balance) leaves the device.

### 4.2 AI document reading

Users photograph, upload, or forward via WhatsApp or Telegram any of:

- Printed receipts and thermal slips
- Handwritten cash memos and khata pages
- Mushak-6.3 VAT invoices and purchase challans
- Bank deposit slips, cheque images, MFS screenshots
- Supplier invoices as PDF, utility bills, rent receipts
- Salary sheets and donor fund release letters (NGO)

The AI pipeline:

1. **Read.** A vision-capable model extracts vendor, date, line items, subtotal, VAT amount and rate, total, payment method, and reference numbers. Bangla and English text, Bangla numerals (০-৯), the ৳ sign, and Bangla dates are all normalised.
2. **Translate.** The extracted record is stored once and rendered in either language, so an English-speaking accountant and a Bangla-speaking owner see the same entry.
3. **Classify.** The vendor and line items are mapped to the organisation's chart of accounts using the template's rules, the business's own history, and the model.
4. **Match.** If a captured money movement already exists (an SMS or API payment of the same amount to the same party around the same date), the document attaches to it instead of creating a duplicate.
5. **Post.** Above a confidence threshold the journal entry posts with the image attached as evidence. Below it, the entry waits in the inbox with the uncertain fields highlighted.

Every posting keeps the original image, the extracted JSON, the confidence, and who confirmed it. That is the audit trail an auditor or donor asks for.

### 4.3 Natural language and voice entry

Typing "রহিমকে দোকান ভাড়া ৫০০০ টাকা বিকাশে দিলাম" or "paid Rahim 5000 shop rent via bKash" produces the same entry: debit Rent, credit bKash wallet, counterparty Rahim. Voice input in Bangla and English uses on-device or cloud speech recognition. This is the cashbook experience owners already expect, but it lands in a real ledger.

### 4.4 The accounting core

- Full double-entry general ledger with immutable journal and reversal-only corrections
- Cash and bank and wallet accounts with running balances and reconciliation
- Receivables and payables with ageing, reminders by SMS or WhatsApp, and partial payments
- Sales invoices and quotes with Bangla or English or bilingual layouts, Mushak-6.3 compliant when VAT is enabled
- Purchases, bills, expense claims, recurring entries
- Simple inventory for retail and trading templates
- Fixed assets and depreciation
- Basic payroll for small teams, with tax deduction at source
- Multi-user roles: owner, staff, accountant, auditor read-only, donor read-only (NGO)
- Financial year July to June by default, configurable; Bangla and Gregorian calendar display
- Base currency BDT; foreign currency invoices and FX gain or loss for exporters and NGOs receiving foreign funds
- Period locking, audit log, full data export

### 4.5 Bangladesh compliance built in

- **VAT (NBR):** Mushak-6.3 tax invoices, 6.1 purchase and 6.2 sales registers, monthly Mushak-9.1 return preparation, turnover tax handling for businesses below the VAT registration threshold, input VAT credit tracking
- **Income tax:** tax deduction at source on salaries, rent and vendor payments; advance income tax records; year-end schedules an accountant needs for the return
- **NGO Affairs Bureau:** project-wise and donor-wise fund accounting, restricted versus unrestricted funds, budget versus actual by project, FD-form-ready reports
- **Company records:** statutory registers and RJSC filing reminders for limited companies

The compliance layer is data-driven so rate and form changes ship as configuration, not code releases.

---

## 5. Organisation-type setups

Onboarding asks one question: "আপনার প্রতিষ্ঠান কী ধরনের?" (What kind of organisation are you?). The answer loads a template. Templates change what the user sees. The engine underneath is identical.

| Template | Who | Chart of accounts emphasis | Documents and screens | Key reports |
|---|---|---|---|---|
| **Retail shop** (দোকান) | Stationery, grocery, pharmacy, electronics | Sales, cost of goods, stock, supplier credit, daily cash | Daily cash counter, quick sale, stock in, supplier due, customer khata | Daily sales and cash, stock value, supplier and customer dues, profit per month, VAT summary |
| **Service firm** (সেবা প্রতিষ্ঠান) | Software company, agency, consultancy, clinic, coaching | Revenue by service or client, salaries, subscriptions, receivables | Quotes, invoices, retainers, timesheet-lite, expense claims, payroll | Receivables ageing, revenue by client, profit and loss, TDS schedule, export earnings |
| **NGO / non-profit** (এনজিও / অলাভজনক) | NGOs, trusts, foundations, school and mosque committees, clubs | Funds, projects, donors, grants, programme versus admin costs | Donation receipts, fund release, project budgets, advance and settlement, beneficiary payments | Receipts and payments, fund balance by donor, budget versus actual by project, FD-form reports, statement of financial position |
| **Trading / wholesale** (ট্রেডিং) | Distributors, wholesalers, importers | Purchases, stock, credit sales, LC and import costs | Purchase orders, delivery challans, credit sale ledger, collection tracking | Party ledgers, stock ageing, gross margin by product, dues collection |

A fifth "General business" template is the fallback with everything visible. Users can switch templates later; the ledger is preserved and only the presentation changes.

Each template also carries its own Bangla vocabulary. A shop sees "বাকি" (dues) where an NGO sees "অগ্রিম" (advance), and an accountant can always toggle to standard terminology.

---

## 6. Platform and experience

- **Android app** (first): offline-first, SMS reading with explicit permission, camera capture, voice entry, push reminders. Works on entry-level phones and slow networks.
- **Web app** (progressive web app): full accountant workspace, reports, bulk review, multi-company for accounting firms.
- **iOS app** (second phase): capture and review, same codebase as Android.
- **Messaging capture:** a WhatsApp Business and Telegram bot that accepts photos and short messages and posts them to the inbox, because that is where receipts already are.
- **Bangla typography and input:** Noto Sans Bengali or an equivalent well-hinted Bangla font, correct conjunct rendering, Bangla numeral display toggle, Avro-style phonetic input supported natively by the phone.
- **Accountant portal:** one login, many client companies, exception queues across all of them, export to the formats local audit firms use.

---

## 7. Architecture

**Shape:** multi-tenant SaaS with a single relational ledger database per region, an event-driven ingestion pipeline, and a separate AI service layer.

| Layer | Choice | Why |
|---|---|---|
| Mobile | Flutter (Android first, iOS from the same code) | Offline sync, good Bangla text rendering, single team |
| Web | React or Next.js PWA | Accountant workspace, shared component library with mobile where sensible |
| API | TypeScript (NestJS) or Python (FastAPI) | Strong typing for money, large hiring pool in Dhaka |
| Ledger database | PostgreSQL with row-level tenant isolation, append-only journal tables | Correctness and auditability |
| Ingestion | Message queue (SQS or RabbitMQ) with idempotent workers per source | Feeds, SMS, documents all flow through one pipeline with dedup |
| AI | Claude vision and structured outputs for document extraction and classification; Bengali OCR fallback; Bangla and English speech-to-text | Accuracy on mixed Bangla and English and handwriting; JSON schema outputs post directly |
| Integrations | Adapter per source (bKash merchant, Nagad, SSLCommerz, each bank) behind one interface | Add banks without touching the core |
| Files | Object storage with per-tenant encryption; every document keeps its original | Evidence retention |
| Hosting | Start in Singapore or Mumbai regions for latency; local data-centre option for enterprise and NGO customers who require in-country data | Cost now, compliance later |

**Design rules**

- Money is stored as integers in paisa. No floating point anywhere near the ledger.
- Every automated posting carries `source`, `confidence`, `evidence_id` and `posted_by` (system or user).
- Deduplication key across sources: amount, counterparty, reference, time window. An SMS, an API callback and a receipt photo of the same payment become one entry with three evidences.
- Templates are data: chart of accounts, vocabulary, screen visibility, report set, all stored per organisation and versioned.
- Compliance rules (VAT rates, TDS rates, form layouts) are configuration with effective dates.

**Security**

- Encryption in transit and at rest, per-tenant keys for documents
- Phone-number login with OTP plus optional PIN or biometric; email and password for accountants
- Role-based access, IP and device logs, immutable audit trail
- Daily encrypted backups, point-in-time recovery, tested restore
- SMS parsing is on-device; message bodies never leave the phone unless the user opts in for debugging

---

## 8. Business model and pricing (indicative, BDT)

| Plan | Monthly | Yearly | Lifetime | Includes |
|---|---|---|---|---|
| **Free cashbook** | ৳0 | ৳0 | — | 1 user, cash and wallet book, SMS capture, 30 AI document reads per month, basic reports |
| **Standard** | ৳499 | ৳4,999 | ৳14,999 | Any template, 3 users, unlimited AI reads, invoices, dues, VAT summary |
| **Business** | ৳999 | ৳9,999 | ৳29,999 | 10 users, inventory, payroll, full Mushak set, bank feeds, accountant seat |
| **NGO** | ৳1,499 | ৳14,999 | — | Fund and project accounting, donor portal, FD reports, unlimited read-only donor users |
| **Accountant** | ৳2,999 | ৳29,999 | — | Multi-client workspace, up to 25 companies, white-label reports |

Notes

- Lifetime plans follow the pay-once approach discussed earlier: the price covers roughly three years of subscription and excludes the recurring-cost features (bank API feeds beyond SMS, and AI reads above a monthly cap) which are sold as add-ons.
- Subscriptions are collected in BDT via bKash, Nagad and SSLCommerz. International customers, such as export software firms and diaspora-funded NGOs, pay by card through Stripe under the Rabbit's Hat account.
- AI cost per document is well under ৳1 at current model pricing, so unlimited reads on paid plans are sustainable.

---

## 9. Go-to-market

1. **Accountants as the channel.** Most SMEs already pay a part-time accountant. Give accountants a free multi-client workspace and a revenue share. They bring their clients and they set up the templates correctly.
2. **NGO networks.** A handful of NGO federations and donor programmes reach thousands of small NGOs that all face the same FD-form burden. One partnership can seed the NGO template.
3. **Trade associations and markets.** Stationery, pharmacy and electronics associations in Dhaka and Chattogram; on-site onboarding days.
4. **Facebook and YouTube in Bangla.** The customer lives there. Short videos showing "photograph a receipt, it's in your books" convert.
5. **Free cashbook as the top of funnel.** It replaces the paper khata on day one and upgrades the moment the owner wants an invoice or a VAT report.

---

## 10. Roadmap

| Phase | Duration | Scope | Exit criteria |
|---|---|---|---|
| **0. Discovery** | 6 to 8 weeks | 40 customer interviews across the four segments; bKash and Nagad merchant API access; collect 2,000 real receipts and SMS samples for AI evaluation; legal and trademark | Templates validated, AI extraction above 90% field accuracy on the sample set |
| **1. MVP** | 4 to 5 months | Android app and web; Retail and Service templates; SMS capture; AI receipt and invoice reading; cashbook, invoices, dues; Bangla and English UI; free and Standard plans | 500 active businesses, 70% of entries created without typing |
| **2. Compliance and NGO** | 3 to 4 months | NGO template with fund accounting and FD reports; full VAT Mushak set; bKash and Nagad merchant feeds; first bank API adapters; accountant portal; WhatsApp bot | First 50 NGOs; accountants managing 200 companies |
| **3. Scale** | ongoing | Trading template, inventory and payroll depth, iOS, more bank adapters, donor portal, open API, lifetime plan launch, in-country hosting option | Paid conversion above 15%, monthly churn under 3% |

---

## 11. Team and budget (rough order of magnitude)

Core MVP team of six for six months: product lead, two full-stack engineers, one mobile engineer, one AI and data engineer, one designer with Bangla typography experience. Part-time: a chartered accountant for chart-of-accounts and compliance design, and a Bangla content writer for UI copy.

Estimated MVP cost, including salaries, cloud, AI usage, design and legal, is in the range of ৳50 to 80 lakh (roughly USD 45,000 to 70,000) depending on seniority and whether hiring is in Dhaka only. This is a planning number, to be replaced by a proper budget after discovery.

---

## 12. Risks and mitigations

| Risk | Mitigation |
|---|---|
| MFS and bank API access is slow or restricted to large partners | SMS parsing gives full coverage without any partnership; APIs are an accuracy upgrade, not a dependency |
| AI misreads handwritten Bangla | Confidence thresholds, human review queue, continuous evaluation on real samples, learn from each correction per business |
| Owners distrust automation with money | Every entry shows its evidence and source; accountant review role; reversal-only corrections; monthly reconciliation prompts |
| Android SMS permission policy changes | Notification-listener fallback, statement upload fallback, MFS merchant APIs |
| Regulatory changes in VAT and tax | Rules as dated configuration; a compliance advisor on retainer |
| Free tier abuse and AI cost | Monthly read caps on free plan, rate limits, cheap OCR pre-pass to reject junk images |
| Pay-once revenue stalls | Lifetime plans capped by cohort and excluded from recurring-cost features |

---

## 13. Success metrics

- Share of transactions posted without manual typing (target 80% by end of Phase 2)
- Median time from money movement to ledger entry (target under 5 minutes for SMS and API sources)
- AI field-level extraction accuracy on the live sample (target 95% printed, 85% handwritten)
- Weekly active businesses and accountant-managed companies
- Free to paid conversion, monthly churn, revenue per company
- Compliance outcomes: Mushak-9.1 returns prepared in-app, NGO FD reports generated

---

## 14. Decisions needed to start

1. Confirm the four launch templates: Retail, Service, NGO, Trading, plus General fallback.
2. Confirm Bangla as default UI with per-user English switch, and bilingual data entry.
3. Approve Discovery phase budget and the recruitment of the chartered accountant advisor.
4. Choose the working brand name and run the trademark search (Hishab is a placeholder).
5. Decide the initial hosting region and whether an in-country option is required at launch for NGO customers.
6. Confirm pricing posture: subscription-first with a capped lifetime plan, as proposed.

---

*Prepared for Rabbit's Hat. Figures marked indicative or rough are planning estimates and will be revised after discovery.*
