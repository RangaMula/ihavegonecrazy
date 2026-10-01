# -*- coding: utf-8 -*-
"""SEED LIST, not a build target. The first 300 fixed concepts (Bangla + English), written before the
2,000-word journey design (see WORD-JOURNEY.md). They will be redistributed into the fixed sets of
sections 1-10. The CULTURE examples below feed the culture sets. Running this only validates the data."""
import csv

CORE = [
('C1','সর্বনাম ও ছোট শব্দ','Pronouns & little words',
 'আমি|I; তুমি / আপনি|you; সে (পুরুষ)|he; সে (নারী)|she; আমরা|we; তারা|they; এটা|this; ওটা|that; এখানে|here; সেখানে|there; এবং|and; কিন্তু|but; অথবা|or; কারণ|because; সাথে|with; ছাড়া|without; ভেতরে|in / inside; ওপরে|on / above; নিচে|under / below; হ্যাঁ|yes; না|no / not; খুব|very; আরও|also / more; শুধু|only; সব|all'),
('C2','প্রশ্ন ও দরকারি কথা','Questions & key expressions',
 "কী|what; কে|who; কোথায়|where; কখন|when; কেন|why; কীভাবে|how; কত|how much / how many; কোনটা|which; শুভেচ্ছা (হ্যালো)|hello; বিদায়|goodbye; দয়া করে|please; ধন্যবাদ|thank you; দুঃখিত|sorry; মাফ করবেন|excuse me; স্বাগতম|welcome; ঠিক আছে|okay; অবশ্যই|of course; হয়তো|maybe; অভিনন্দন|congratulations; সুপ্রভাত|good morning; শুভরাত্রি|good night; আবার দেখা হবে|see you; সমস্যা নেই|no problem; আমি বুঝতে পারছি না|I don't understand; আবার বলুন|please say it again"),
('C3','মানুষ ও পরিবার','People & family',
 'মানুষ|person; পুরুষ|man; নারী|woman; শিশু|child; ছেলে|boy / son; মেয়ে|girl / daughter; বাবা|father; মা|mother; ভাই|brother; বোন|sister; স্বামী|husband; স্ত্রী|wife; দাদা / নানা|grandfather; দাদি / নানি|grandmother; চাচা / মামা|uncle; চাচি / খালা|aunt; চাচাতো-মামাতো ভাইবোন|cousin; বন্ধু|friend; প্রতিবেশী|neighbour; অতিথি|guest; পরিবার|family; নাম|name; বয়স|age; আত্মীয়|relative; সহকর্মী|colleague'),
('C4','শরীর ও স্বাস্থ্য','Body & health',
 'মাথা|head; চোখ|eye; কান|ear; নাক|nose; মুখ|mouth; দাঁত|tooth; হাত|hand / arm; পা|foot / leg; পেট|stomach; বুক|chest; পিঠ|back; হৃদপিণ্ড|heart; রক্ত|blood; জ্বর|fever; ব্যথা|pain; কাশি|cough; সর্দি|cold (illness); অসুখ|illness; ওষুধ|medicine; ডাক্তার|doctor; হাসপাতাল|hospital; নার্স|nurse; অ্যালার্জি|allergy; ইনজেকশন|injection; ঘুম|sleep'),
('C5','বাড়ি, খাবার ও দৈনন্দিন জীবন','Home, food & daily life',
 'পানি|water; ভাত|rice (cooked); রুটি|bread; মাংস|meat; মাছ|fish; ডিম|egg; সবজি|vegetable; ফল|fruit; দুধ|milk; চা|tea; লবণ|salt; খাবার|food; সকালের নাশতা|breakfast; রাতের খাবার|dinner; হালাল|halal; বাড়ি|house / home; ঘর|room; দরজা|door; জানালা|window; বিছানা|bed; চাবি|key; কাপড়|clothes; জুতা|shoes; ঠিকানা|address; ভাড়া|rent'),
('C6','শহর, ভ্রমণ ও পথ','City, travel & directions',
 'শহর|city; রাস্তা|road / street; দোকান|shop; বাজার|market; ব্যাংক|bank; ফার্মেসি|pharmacy; রেস্তোরাঁ|restaurant; হোটেল|hotel; ডানে|right; বামে|left; সোজা|straight ahead; কাছে|near; দূরে|far; গাড়ি|car; বাস|bus; ট্রেন|train; বিমান|airplane; বিমানবন্দর|airport; স্টেশন|station; ট্যাক্সি|taxi; টিকিট|ticket; ব্যাগ|bag; ভ্রমণ|trip / journey; মানচিত্র|map; পর্যটক|tourist'),
('C7','কাজ, পড়াশোনা ও টাকা','Work, study & money',
 'কাজ|work; চাকরি|job / employment; কোম্পানি|company; মালিক|owner / boss; ছুটি|leave / day off; বেতন|salary; চুক্তি|contract; টাকা|money; দাম|price; নগদ|cash; কার্ড|card; রসিদ|receipt; বিল|bill; মুদ্রা|currency; বিদ্যালয়|school; বিশ্ববিদ্যালয়|university; শিক্ষক|teacher; ছাত্র / ছাত্রী|student; বই|book; কলম|pen; পরীক্ষা|exam; ভাষা|language; ফোন|phone; ইন্টারনেট|internet; বার্তা|message'),
('C8','সময়, প্রকৃতি ও নিরাপত্তা','Time, nature & safety',
 'সময়|time; আজ|today; আগামীকাল|tomorrow; গতকাল|yesterday; এখন|now; সকাল|morning; রাত|night; দিন|day; সপ্তাহ|week; বছর|year; সূর্য|sun; বৃষ্টি|rain; আবহাওয়া|weather; নদী|river; গাছ|tree; পাসপোর্ট|passport; ভিসা|visa; পরিচয়পত্র|ID card; ফরম|form; পুলিশ|police; সাহায্য|help; দুর্ঘটনা|accident; অ্যাম্বুলেন্স|ambulance; জরুরি অবস্থা|emergency; দূতাবাস|embassy'),
('V','প্রয়োজনীয় ৫০টি ক্রিয়া','50 essential verbs',
 'হওয়া|to be; থাকা|to stay / to live; থাকা (মালিকানা)|to have; যাওয়া|to go; আসা|to come; খাওয়া|to eat; পান করা|to drink; ঘুমানো|to sleep; দেখা|to see; শোনা|to hear / listen; বলা|to say / speak; কথা বলা|to talk; পড়া|to read; লেখা|to write; জানা|to know; বোঝা|to understand; চাওয়া|to want; দরকার হওয়া|to need; পারা|can / to be able; করা|to do; বানানো|to make; দেওয়া|to give; নেওয়া|to take; কেনা|to buy; বিক্রি করা|to sell; টাকা দেওয়া|to pay; কাজ করা|to work; শেখা|to learn; শেখানো|to teach; খোলা|to open; বন্ধ করা|to close; শুরু করা|to start; শেষ করা|to finish; অপেক্ষা করা|to wait; খোঁজা|to look for; পাওয়া|to find / get; পছন্দ করা|to like; ভাবা|to think; মনে রাখা|to remember; ভুলে যাওয়া|to forget; জিজ্ঞেস করা|to ask; সাহায্য করা|to help; ফোন করা|to call (phone); বসা|to sit; দাঁড়ানো|to stand; হাঁটা|to walk; রান্না করা|to cook; ধোয়া|to wash; পাঠানো|to send; ফিরে আসা|to return'),
('A','প্রয়োজনীয় ৫০টি বিশেষণ','50 essential adjectives',
 'ভালো|good; খারাপ|bad; বড়|big; ছোট|small; নতুন|new; পুরোনো|old (thing); বয়স্ক|old (person); তরুণ|young; গরম|hot; ঠান্ডা|cold; লম্বা|long / tall; খাটো|short; অনেক|many / much; কম|few / little; সুন্দর|beautiful; সহজ|easy; কঠিন|difficult; দ্রুত|fast; ধীর|slow; সস্তা|cheap; দামি|expensive; পরিষ্কার|clean; নোংরা|dirty; খালি|empty; ভরা|full; খোলা|open; বন্ধ|closed; সঠিক|correct; ভুল|wrong; ব্যস্ত|busy; ফাঁকা|free (available); খুশি|happy; দুঃখী|sad; ক্লান্ত|tired; অসুস্থ|sick; সুস্থ|healthy / well; ক্ষুধার্ত|hungry; নিরাপদ|safe; গুরুত্বপূর্ণ|important; প্রথম|first; শেষ|last; ভিন্ন|different; ভারী|heavy; মিষ্টি|sweet; ঝাল|spicy; লাল|red; সাদা|white; কালো|black; নীল|blue; সবুজ|green'),
]

# Culture slots: (code, bangla, english, what goes in it, Arabic examples, Japanese examples)
CULTURE = [
("K1","দেশ, শহর ও বিস্ময়কর স্থান","Lands, cities & wonders",
 "Countries and regions where it is spoken, great cities, rivers, deserts and mountains, famous landmarks: the places a reader dreams of visiting",
 "مَكَّة Makkah · البَتْرَاء Petra · النِّيل the Nile · الرُّبْع الخَالِي the Empty Quarter",
 "富士山 Fuji-san · 京都 Kyoto · 北海道 Hokkaido · 新幹線 Shinkansen"),
("K2","রান্নাঘরের স্বাদ","Tastes of the kitchen",
 "Signature dishes, street food, spices and ingredients, drinks, utensils and table customs",
 "كَبْسَة kabsa · حُمُّص hummus · قَهْوَة عَرَبِيَّة Arabic coffee · تَمْر dates",
 "寿司 sushi · おにぎり onigiri · 弁当 bento · 箸 chopsticks"),
("K3","মানুষ, নাম ও সম্বোধন","People, names & forms of address",
 "Common first names, naming customs, honorifics and titles, how to address elders, strangers and teachers, the peoples and communities of the region",
 "أَبُو / أُمّ Abu- / Umm- (kunya) · يَا أَخِي ya akhi · أُسْتَاذ ustadh · بَدْو Bedouin",
 "〜さん -san · 先生 sensei · 先輩 senpai · アイヌ Ainu"),
("K4","উৎসব, বিশ্বাস ও ঐতিহ্য","Festivals, faith & traditions",
 "Religious and seasonal festivals, rites of passage, everyday customs and the words that go with them",
 "رَمَضَان Ramadan · إِفْطَار iftar · الحَجّ Hajj · عِيد الأَضْحَى Eid al-Adha",
 "花見 hanami · お盆 Obon · お正月 New Year · 神社 Shinto shrine"),
("K5","পোশাক, শিল্প ও কারুকাজ","Dress, arts & crafts",
 "Traditional clothing, music and instruments, calligraphy and visual arts, crafts, traditional sports and games",
 "ثَوْب thobe · عُود oud · خَطّ calligraphy · فُرُوسِيَّة horsemanship",
 "着物 kimono · 折り紙 origami · 書道 shodō · 相撲 sumo"),
("K6","ইতিহাস, বীর ও কিংবদন্তি","History, heroes & legends",
 "Great eras, famous people (scholars, travellers, poets, inventors), legends and folk heroes, inventions given to the world",
 "ابن بطوطة Ibn Battuta · بَيْت الحِكْمَة House of Wisdom · الخوارزمي al-Khwarizmi · ألف ليلة وليلة One Thousand and One Nights",
 "侍 samurai · 明治 Meiji era · 桃太郎 Momotarō · 浮世絵 ukiyo-e"),
("K7","মূল্যবোধ ও মনের কথা","Values & the heart",
 "Virtues and social values the culture prizes, etiquette words, feelings the culture talks about in its own way",
 "كَرَم generosity · ضِيَافَة hospitality · صَبْر patience · أَدَب good manners",
 "おもてなし omotenashi (hospitality) · 和 wa (harmony) · 我慢 gaman (endurance) · 恩 on (debt of gratitude)"),
("K8","অনুবাদ-অযোগ্য শব্দ ও আজকের জীবন","Untranslatable words & life today",
 "Wonder words with no single Bangla equivalent, plus everyday modern life: shops, transport cards, pop culture, technology the country is known for",
 "طَرَب tarab (music-induced rapture) · مَجْلِس majlis · إِنْ شَاءَ اللّٰه in shā' Allāh · سُوق souq",
 "木漏れ日 komorebi (sunlight through leaves) · 侘寂 wabi-sabi · コンビニ konbini · 漫画 manga"),
]

rows, n = [], 0
for code, bn, en, data in CORE:
    items = [x.strip().split("|") for x in data.split(";")]
    want = 50 if code in ("V", "A") else 25
    assert len(items) == want, (code, len(items))
    for i, (b, e) in enumerate(items, 1):
        n += 1
        rows.append((n, code, bn, en, i, b.strip(), e.strip()))
assert n == 300, n
ens = [r[6] for r in rows]
dups = sorted({e for e in ens if ens.count(e) > 1})
assert not dups, dups
assert len(CULTURE) == 8

print("seed ok:", n, "fixed concepts;", len(CULTURE), "culture slot examples")
