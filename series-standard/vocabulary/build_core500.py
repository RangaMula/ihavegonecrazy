# -*- coding: utf-8 -*-
"""Master concept list for Ch. 10 'প্রয়োজনীয় ৫০০ শব্দ'. Language-neutral: each language pack
translates these 500 concepts (Bangla + English are fixed). Run to regenerate CORE-500.md and core500.csv."""
import csv

THEMES = [
("T01","সর্বনাম ও ছোট শব্দ","Pronouns & little words",
 "আমি|I; তুমি / আপনি|you; সে (পুরুষ)|he; সে (নারী)|she; আমরা|we; তারা|they; এটা|this; ওটা|that; এখানে|here; সেখানে|there; এবং|and; কিন্তু|but; অথবা|or; কারণ|because; সাথে|with; ছাড়া|without; ভেতরে|in / inside; ওপরে|on / above; নিচে|under / below; হ্যাঁ|yes; না|no / not; খুব|very; আরও|also / more; শুধু|only; সব|all"),
("T02","প্রশ্ন ও দরকারি কথা","Questions & key expressions",
 "কী|what; কে|who; কোথায়|where; কখন|when; কেন|why; কীভাবে|how; কত|how much / how many; কোনটা|which; শুভেচ্ছা (হ্যালো)|hello; বিদায়|goodbye; দয়া করে|please; ধন্যবাদ|thank you; দুঃখিত|sorry; মাফ করবেন|excuse me; স্বাগতম|welcome; ঠিক আছে|okay; অবশ্যই|of course; হয়তো|maybe; অভিনন্দন|congratulations; সুপ্রভাত|good morning; শুভরাত্রি|good night; আবার দেখা হবে|see you; সমস্যা নেই|no problem; আমি বুঝতে পারছি না|I don't understand; আবার বলুন|please say it again"),
("T03","মানুষ ও পরিবার","People & family",
 "মানুষ|person; পুরুষ|man; নারী|woman; শিশু|child; ছেলে|boy / son; মেয়ে|girl / daughter; বাবা|father; মা|mother; ভাই|brother; বোন|sister; স্বামী|husband; স্ত্রী|wife; দাদা / নানা|grandfather; দাদি / নানি|grandmother; চাচা / মামা|uncle; চাচি / খালা|aunt; চাচাতো-মামাতো ভাইবোন|cousin; বন্ধু|friend; প্রতিবেশী|neighbour; অতিথি|guest; পরিবার|family; নাম|name; বয়স|age; আত্মীয়|relative; সহকর্মী|colleague"),
("T04","শরীর ও স্বাস্থ্য","Body & health",
 "মাথা|head; চোখ|eye; কান|ear; নাক|nose; মুখ|mouth; দাঁত|tooth; হাত|hand / arm; পা|foot / leg; পেট|stomach; বুক|chest; পিঠ|back; হৃদপিণ্ড|heart; রক্ত|blood; জ্বর|fever; ব্যথা|pain; কাশি|cough; সর্দি|cold (illness); অসুখ|illness; ওষুধ|medicine; ডাক্তার|doctor; হাসপাতাল|hospital; নার্স|nurse; অ্যালার্জি|allergy; ইনজেকশন|injection; ঘুম|sleep"),
("T05","খাবার ও পানীয়","Food & drink",
 "পানি|water; ভাত|rice (cooked); রুটি|bread; মাংস|meat; মুরগি|chicken; মাছ|fish; ডিম|egg; সবজি|vegetable; ফল|fruit; দুধ|milk; চা|tea; কফি|coffee; চিনি|sugar; লবণ|salt; তেল|oil; ডাল|lentils; আলু|potato; পেঁয়াজ|onion; মরিচ|chilli; সকালের নাশতা|breakfast; দুপুরের খাবার|lunch; রাতের খাবার|dinner; খাবার|food; রস|juice; হালাল|halal"),
("T06","বাড়ি ও সংসার","Home & household",
 "বাড়ি|house / home; ঘর|room; দরজা|door; জানালা|window; রান্নাঘর|kitchen; বাথরুম|bathroom; বিছানা|bed; টেবিল|table; চেয়ার|chair; চাবি|key; বাতি|light / lamp; পাখা|fan; ফ্রিজ|fridge; কাপড়|clothes; জুতা|shoes; সাবান|soap; তোয়ালে|towel; থালা|plate; গ্লাস|glass; চামচ|spoon; ছুরি|knife; ভাড়া|rent; বাড়িওয়ালা|landlord; ঠিকানা|address; তলা|floor (storey)"),
("T07","শহর ও পথনির্দেশ","City & directions",
 "শহর|city; গ্রাম|village; রাস্তা|road / street; দোকান|shop; বাজার|market; ব্যাংক|bank; ফার্মেসি|pharmacy; রেস্তোরাঁ|restaurant; হোটেল|hotel; পার্ক|park; থানা|police station; ডাকঘর|post office; অফিস|office; ডানে|right; বামে|left; সোজা|straight ahead; কাছে|near; দূরে|far; সামনে|in front; পেছনে|behind; মোড়|corner / turn; সেতু|bridge; মানচিত্র|map; পাশে|next to; ভবন|building"),
("T08","যানবাহন ও ভ্রমণ","Transport & travel",
 "গাড়ি|car; বাস|bus; ট্রেন|train; বিমান|airplane; বিমানবন্দর|airport; স্টেশন|station; ট্যাক্সি|taxi; জাহাজ|ship; সাইকেল|bicycle; টিকিট|ticket; ব্যাগ|bag; লাগেজ|luggage; ভ্রমণ|trip / journey; আগমন|arrival; প্রস্থান|departure; দেরি|delay; আসন|seat; চালক|driver; গেট|gate; প্ল্যাটফর্ম|platform; বাস স্টপ|bus stop; পর্যটক|tourist; বুকিং|reservation; পথ|route / way; সীমান্ত|border"),
("T09","কেনাকাটা ও টাকা","Shopping & money",
 "টাকা|money; দাম|price; নগদ|cash; কার্ড|card; রসিদ|receipt; ছাড়|discount; বিক্রেতা|seller; ক্রেতা|customer; মাপ|size; রং|colour; কেজি|kilogram; লিটার|litre; প্যাকেট|packet; খুচরা|change (money); মুদ্রা|currency; বিনিময়|exchange; বিল|bill; কর|tax; বেতন|salary; ধার|debt / loan; দর কষাকষি|bargaining; ফেরত|refund / return; লাইন|queue; মোট|total; জোড়া|pair"),
("T10","কাজ ও পেশা","Work & professions",
 "কাজ|work; চাকরি|job / employment; কর্মী|worker; মালিক|owner / boss; ম্যানেজার|manager; কোম্পানি|company; কারখানা|factory; নির্মাণ|construction; কৃষক|farmer; প্রকৌশলী|engineer; রাঁধুনি|cook (person); পরিচ্ছন্নতাকর্মী|cleaner; নিরাপত্তারক্ষী|security guard; বিক্রয়কর্মী|salesperson; দর্জি|tailor; মিস্ত্রি|mechanic; বিদ্যুৎমিস্ত্রি|electrician; ওভারটাইম|overtime; ছুটি|leave / day off; চুক্তি|contract; সাক্ষাৎকার|interview; অভিজ্ঞতা|experience; দক্ষতা|skill; শিফট|shift; নিয়োগকর্তা|employer"),
("T11","শিক্ষা ও যোগাযোগ","Education & communication",
 "বিদ্যালয়|school; বিশ্ববিদ্যালয়|university; শিক্ষক|teacher; ছাত্র / ছাত্রী|student; বই|book; খাতা|notebook; কলম|pen; পাঠ|lesson; পরীক্ষা|exam; প্রশ্ন|question; উত্তর|answer; ভাষা|language; শব্দ|word; বাক্য|sentence; অক্ষর|letter (of alphabet); ফোন|phone; ফোন নম্বর|phone number; ইন্টারনেট|internet; বার্তা|message; ইমেইল|email; ছবি|picture / photo; কম্পিউটার|computer; চার্জার|charger; পাসওয়ার্ড|password; ক্লাস|class"),
("T12","প্রকৃতি, আবহাওয়া ও প্রাণী","Nature, weather & animals",
 "সূর্য|sun; চাঁদ|moon; তারা|star; আকাশ|sky; বৃষ্টি|rain; বাতাস|wind; মেঘ|cloud; তুষার|snow; আবহাওয়া|weather; তাপমাত্রা|temperature; নদী|river; সমুদ্র|sea; পাহাড়|mountain; গাছ|tree; ফুল|flower; মাটি|soil / ground; আগুন|fire; পাথর|stone; কুকুর|dog; বিড়াল|cat; পাখি|bird; গরু|cow; ঘোড়া|horse; বন|forest; পৃথিবী|world / earth"),
("T13","সময়ের শব্দ","Time words",
 "সময়|time; আজ|today; আগামীকাল|tomorrow; গতকাল|yesterday; এখন|now; পরে|later / after; আগে|before / earlier; সকাল|morning; দুপুর|noon; বিকেল|afternoon; সন্ধ্যা|evening; রাত|night; দিন|day; সপ্তাহ|week; মাস|month; বছর|year; ঘণ্টা|hour; মিনিট|minute; সবসময়|always; কখনো না|never; মাঝে মাঝে|sometimes; প্রায়ই|often; শীঘ্রই|soon; এখনো|still / yet; সপ্তাহান্ত|weekend"),
("T14","অনুভূতি ও চরিত্র","Feelings & character",
 "আনন্দ|joy; দুঃখ|sadness; ভয়|fear; রাগ|anger; ভালোবাসা|love; দুশ্চিন্তা|worry; ক্ষুধা|hunger; তৃষ্ণা|thirst; ক্লান্তি|tiredness; লজ্জা|shyness / shame; আশা|hope; ধৈর্য|patience; সম্মান|respect; বিশ্বাস|trust / faith; সাহস|courage; শান্তি|peace; একাকীত্ব|loneliness; দেশের জন্য মন খারাপ|homesickness; হাসি|smile / laughter; কান্না|crying; কৃতজ্ঞতা|gratitude; সততা|honesty; দয়া|kindness; বিনয়|humility; স্বপ্ন|dream"),
("T15","ধর্ম, সংস্কৃতি ও উৎসব","Religion, culture & festivals",
 "ধর্ম|religion; আল্লাহ / সৃষ্টিকর্তা|God; মসজিদ|mosque; মন্দির|temple; গির্জা|church; নামাজ / প্রার্থনা|prayer; রোজা|fasting; দান|charity; উৎসব|festival; ঈদ|Eid; ছুটির দিন|holiday; বিয়ে|wedding; জন্মদিন|birthday; উপহার|gift; ঐতিহ্য|tradition; গান|song; নাচ|dance; খেলা|game / sport; সিনেমা|film / movie; গল্প|story; কবিতা|poem; শিল্পকলা|art; ঐতিহ্যবাহী পোশাক|traditional dress; দাওয়াত|invitation; অভিবাদন|greeting"),
("T16","কাগজপত্র, নিরাপত্তা ও জরুরি","Documents, safety & emergency",
 "পাসপোর্ট|passport; ভিসা|visa; পরিচয়পত্র|ID card; ফরম|form; স্বাক্ষর|signature; আবেদন|application; অনুমতিপত্র|permit; দূতাবাস|embassy; অভিবাসন|immigration; কাস্টমস|customs; পুলিশ|police; সাহায্য|help; বিপদ|danger; দুর্ঘটনা|accident; দমকল|fire brigade; অ্যাম্বুলেন্স|ambulance; চোর|thief; হারানো জিনিস|lost property; জরুরি অবস্থা|emergency; নিয়ম|rule; জরিমানা|fine (penalty); আইন|law; আইনজীবী|lawyer; বীমা|insurance; জন্মতারিখ|date of birth"),
("V","প্রয়োজনীয় ৫০টি ক্রিয়া","50 essential verbs",
 "হওয়া|to be; থাকা|to stay / to live; থাকা (মালিকানা)|to have; যাওয়া|to go; আসা|to come; খাওয়া|to eat; পান করা|to drink; ঘুমানো|to sleep; দেখা|to see; শোনা|to hear / listen; বলা|to say / speak; কথা বলা|to talk; পড়া|to read; লেখা|to write; জানা|to know; বোঝা|to understand; চাওয়া|to want; দরকার হওয়া|to need; পারা|can / to be able; করা|to do; বানানো|to make; দেওয়া|to give; নেওয়া|to take; কেনা|to buy; বিক্রি করা|to sell; টাকা দেওয়া|to pay; কাজ করা|to work; শেখা|to learn; শেখানো|to teach; খোলা|to open; বন্ধ করা|to close; শুরু করা|to start; শেষ করা|to finish; অপেক্ষা করা|to wait; খোঁজা|to look for; পাওয়া|to find / get; পছন্দ করা|to like; ভাবা|to think; মনে রাখা|to remember; ভুলে যাওয়া|to forget; জিজ্ঞেস করা|to ask; সাহায্য করা|to help; ফোন করা|to call (phone); বসা|to sit; দাঁড়ানো|to stand; হাঁটা|to walk; রান্না করা|to cook; ধোয়া|to wash; পাঠানো|to send; ফিরে আসা|to return"),
("A","প্রয়োজনীয় ৫০টি বিশেষণ","50 essential adjectives",
 "ভালো|good; খারাপ|bad; বড়|big; ছোট|small; নতুন|new; পুরোনো|old (thing); বয়স্ক|old (person); তরুণ|young; গরম|hot; ঠান্ডা|cold; লম্বা|long / tall; খাটো|short; অনেক|many / much; কম|few / little; সুন্দর|beautiful; সহজ|easy; কঠিন|difficult; দ্রুত|fast; ধীর|slow; সস্তা|cheap; দামি|expensive; পরিষ্কার|clean; নোংরা|dirty; খালি|empty; ভরা|full; খোলা|open; বন্ধ|closed; সঠিক|correct; ভুল|wrong; ব্যস্ত|busy; ফাঁকা|free (available); খুশি|happy; দুঃখী|sad; ক্লান্ত|tired; অসুস্থ|sick; সুস্থ|healthy / well; ক্ষুধার্ত|hungry; নিরাপদ|safe; গুরুত্বপূর্ণ|important; প্রথম|first; শেষ|last; ভিন্ন|different; ভারী|heavy; মিষ্টি|sweet; ঝাল|spicy; লাল|red; সাদা|white; কালো|black; নীল|blue; সবুজ|green"),
]

rows, n = [], 0
for code, bn, en, data in THEMES:
    items = [x.strip().split("|") for x in data.split(";")]
    want = 50 if code in ("V", "A") else 25
    assert len(items) == want, (code, len(items))
    for i, (b, e) in enumerate(items, 1):
        n += 1
        rows.append((n, code, bn, en, i, b.strip(), e.strip()))
assert n == 500, n
ens = [r[6] for r in rows]
dups = sorted({e for e in ens if ens.count(e) > 1})
assert not dups, dups

with open("core500.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "theme_code", "theme_bn", "theme_en", "no_in_theme", "bangla", "english", "target_script", "bangla_pronunciation", "romanization", "notes"])
    for r in rows:
        w.writerow(list(r) + ["", "", "", ""])

def bn_digits(x): return str(x).translate(str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯"))
md = ["# প্রয়োজনীয় ৫০০ শব্দ — The Core 500 (master list)", "",
      "Generated from `build_core500.py`. **Do not edit by hand.** Edit the script and re-run it.", "",
      "This is the language-neutral list of 500 concepts every book teaches in Ch. 10. The Bangla and English",
      "columns are fixed for the whole series; each language pack fills in the target script, Bangla",
      "pronunciation and romanization columns of `core500.csv`.", "",
      "**Shape:** 16 themes × 25 words = 400, plus 50 verbs and 50 adjectives = **500**.",
      "Numbers, days, months and seasons are taught in Ch. 8–9 and are **not** counted here.", "",
      "## Localization rules (per language pack)", "",
      "| Rule | Detail |", "|---|---|",
      "| Fixed core | The concept list is the same in every book, so a reader who learns a second language finds the same 500 slots |",
      "| Up to 10 swaps per book | A language pack may replace up to 10 of the 500 concepts with culturally essential ones (e.g. chopsticks for Japanese, kimchi for Korean), recorded in the `notes` column |",
      "| One meaning per slot | When a Bangla word has two meanings (e.g. ভাড়া = rent / fare), the English column decides which one is taught |",
      "| Kinship | Where the target language splits a relation further than Bangla, or merges what Bangla splits (e.g. চাচা vs মামা), the pack teaches the target-language distinction and explains it in a note |",
      "| Verbs | Taught in dictionary form, with one example sentence in present tense |",
      "| Adjectives | Taught in base form; gender or agreement forms go in a note |", ""]
for code, bn, en, data in THEMES:
    sub = [r for r in rows if r[1] == code]
    md += [f"## {code} · {bn} — {en} ({len(sub)})", "", "| # | বাংলা | English |", "|---|---|---|"]
    md += [f"| {bn_digits(r[4])} | {r[5]} | {r[6]} |" for r in sub]
    md.append("")
open("CORE-500.md", "w", encoding="utf-8").write("\n".join(md))
print("ok", n, "concepts")
