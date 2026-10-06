# -*- coding: utf-8 -*-
"""Ch. 16 — আমার বিশ্বাসের পরিচয় · Introducing My Faith (70% introduce your faith, 30% FAQ), Arabic book.
Qur'an and hadith quotations: verify against Quran.com and Sunnah.com before print; scholar review gate applies (BOOK-STRUCTURE §7)."""
from part23 import FlowPages
page = FlowPages()
from engine import E, bn, box, h2, tr_line, tr_table, chapter_title, EXTRA_CSS

HEAD = "১৬ · আমার বিশ্বাসের পরিচয়"

def T(fr, bp, ep, b, e, note=None):
    d = {"fr": fr, "bn_pron": bp, "en_pron": ep, "bn": b, "en": e}
    if note:
        d["note_bn"] = note
    return d

def lines(items):
    out = ""
    for it in items:
        out += tr_line(it)
        if it.get("note_bn"):
            out += '<div class="small" style="margin:-0.04in 0 0.07in 0.15in;">💬 %s</div>' % E(it["note_bn"])
    return out

def ayah(ar, bn_txt, ref, pron=None):
    pl = ('<div style="text-align:center;font-size:10pt;margin-top:0.04in;color:var(--muted);">%s</div>' % pron) if pron else ""
    return ('<div style="border:1.2pt solid var(--gold);background:#fff;border-radius:3pt;padding:0.14in 0.2in 0.1in;margin:0.06in 0 0.14in;">'
            '<div class="ar" style="font-size:20pt;line-height:1.85;text-align:center;color:var(--brand);display:block;">%s</div>%s'
            '<div style="text-align:center;font-size:11pt;margin-top:0.05in;">%s</div>'
            '<div style="text-align:center;font-family:BnSans;font-weight:600;font-size:9pt;color:var(--gold);margin-top:0.04in;">%s</div></div>') % (E(ar), pl, bn_txt, ref)

def pr(bp, ep):
    return '%s · <i style="font-family:Lat,LatX;">%s</i>' % (E(bp), E(ep))

SALAM = [
    T("السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللّٰهِ وَبَرَكَاتُهُ", "আস-সালাːমু ʿআলাইকুম ওয়া রাহ়মাতুল্লাːহি ওয়া বারাকাːতুহ",
      "as-salāmu ʿalaykum wa raḥmatullāhi wa barakātuh", "আপনাদের ওপর শান্তি, আল্লাহর রহমত ও বরকত বর্ষিত হোক।", "Peace be upon you, and the mercy of God and His blessings."),
    T("وَعَلَيْكُمُ السَّلَامُ وَرَحْمَةُ اللّٰهِ وَبَرَكَاتُهُ", "ওয়া ʿআলাইকুমুস-সালাːমু ওয়া রাহ়মাতুল্লাːহি ওয়া বারাকাːতুহ",
      "wa ʿalaykumus-salāmu wa raḥmatullāhi wa barakātuh", "আপনাদের ওপরও শান্তি, আল্লাহর রহমত ও বরকত।", "And upon you be peace, and the mercy of God and His blessings."),
    T("تَحِيَّتُنَا دُعَاءٌ بِالسَّلَامِ", "তাহ়িয়্যাতুনাː দুʿআːʾউন বিস-সালাːম", "taḥiyyatunā duʿāʾun bis-salām",
      "আমাদের অভিবাদন হলো শান্তির দোয়া।", "Our greeting is a prayer for peace."),
]
INTRO = [
    T("أَنَا مُسْلِمٌ.", "আনাː মুসলিম", "anā muslim", "আমি মুসলিম (পুরুষ)।", "I am a Muslim (man)."),
    T("أَنَا مُسْلِمَةٌ.", "আনাː মুসলিমাহ", "anā muslimah", "আমি মুসলিম (নারী)।", "I am a Muslim (woman).", "নারী নিজের কথা বললে ة যোগ হয়: مُسْلِمَة।"),
    T("أَنَا مِنْ بَنْغْلَادِيش، وَأَكْثَرُ أَهْلِهَا مُسْلِمُونَ.", "আনাː মিন বানগ়লাːদীːশ, ওয়া আকথ়ারু আহলিহাː মুসলিমূːন",
      "anā min banghlādīsh, wa aktharu ahlihā muslimūn", "আমি বাংলাদেশের মানুষ, আর সেখানকার বেশিরভাগ মানুষ মুসলমান।", "I am from Bangladesh, and most of its people are Muslims."),
    T("الْإِسْلَامُ مِنَ السَّلَامِ، وَمَعْنَاهُ الِاسْتِسْلَامُ لِلّٰهِ.", "আল-ইসলাːমু মিনাস-সালাːম, ওয়া মাʿনাːহুল-ইস্তিসলাːমু লিল্লাːহ",
      "al-islāmu minas-salām, wa maʿnāhul-istislāmu lillāh", "ইসলাম শব্দটি এসেছে ‘সালাম’ (শান্তি) থেকে, আর এর অর্থ আল্লাহর কাছে আত্মসমর্পণ।",
      "Islam comes from 'salām' (peace), and it means submission to God.", "দুটি শব্দই س ل م মূল থেকে: অধ্যায় ৪-এর মূল-পদ্ধতি মনে আছে?"),
    T("أَعْبُدُ اللّٰهَ وَحْدَهُ.", "আʿবুদুল্লাːহা ওয়াহ়দাহ", "aʿbudullāha waḥdah", "আমি এক আল্লাহরই ইবাদত করি।", "I worship God alone."),
    T("وَمُحَمَّدٌ خَاتَمُ الْأَنْبِيَاءِ.", "ওয়া মুহ়াম্মাদুন খ়াːতামুল-আনবিয়াːʾ", "wa muḥammadun khātamul-anbiyāʾ",
      "আর মুহাম্মদ ﷺ শেষ নবী।", "And Muhammad is the last of the prophets.",
      "নামের পরে বলুন: صَلَّى اللّٰهُ عَلَيْهِ وَسَلَّمَ (স়াল্লাল্লাːহু ʿআলাইহি ওয়া সাল্লাম) = আল্লাহ তাঁর ওপর রহমত ও শান্তি বর্ষণ করুন।"),
    T("وَأُؤْمِنُ بِإِبْرَاهِيمَ وَمُوسَى وَعِيسَى عَلَيْهِمُ السَّلَامُ.", "ওয়া উʾমিনু বিইবরাːহীːমা ওয়া মূːসাː ওয়া ʿঈːসাː ʿআলাইহিমুস-সালাːম",
      "wa uʾminu bi-ibrāhīma wa mūsā wa ʿīsā ʿalayhimus-salām", "আমি ইব্রাহিম, মুসা ও ঈসা (আ.)-এর প্রতিও বিশ্বাস রাখি।", "And I believe in Abraham, Moses and Jesus, peace be upon them."),
    T("الْإِسْلَامُ عِنْدِي طَرِيقَةُ حَيَاةٍ.", "আল-ইসলাːমু ʿইনদীː টারীːক়াতু হ়াইয়াːহ", "al-islāmu ʿindī ṭarīqatu ḥayāh",
      "আমার কাছে ইসলাম একটি জীবনধারা।", "For me, Islam is a way of life."),
]
BELIEF = [
    T("أُؤْمِنُ بِاللّٰهِ.", "উʾমিনু বিল্লাːহ", "uʾminu billāh", "আমি আল্লাহয় বিশ্বাস করি।", "I believe in God."),
    T("أُؤْمِنُ بِالْمَلَائِكَةِ.", "উʾমিনু বিল-মালাːʾইকাহ", "uʾminu bil-malāʾikah", "আমি ফেরেশতাদের প্রতি বিশ্বাস করি।", "I believe in the angels."),
    T("أُؤْمِنُ بِالْكُتُبِ: التَّوْرَاةِ وَالْإِنْجِيلِ وَالْقُرْآنِ.", "উʾমিনু বিল-কুতুবি: আত-তাওরাːতি ওয়াল-ইনজীːলি ওয়াল-ক়ুরʾআːন",
      "uʾminu bil-kutubi: at-tawrāti wal-injīli wal-qurʾān", "আমি আসমানি কিতাবে বিশ্বাস করি: তাওরাত, ইঞ্জিল ও কুরআন।", "I believe in the revealed books: the Torah, the Gospel and the Qur'an."),
    T("أُؤْمِنُ بِجَمِيعِ الرُّسُلِ.", "উʾমিনু বিজামীːʿইর-রুসুল", "uʾminu bi-jamīʿir-rusul", "আমি সকল রাসূলের প্রতি বিশ্বাস করি।", "I believe in all the messengers."),
    T("أُؤْمِنُ بِالْيَوْمِ الْآخِرِ.", "উʾমিনু বিল-ইয়াওমিল-আːখ়ির", "uʾminu bil-yawmil-ākhir", "আমি শেষ দিবসে (আখিরাতে) বিশ্বাস করি।", "I believe in the Last Day."),
    T("أُؤْمِنُ بِالْقَدَرِ خَيْرِهِ وَشَرِّهِ.", "উʾমিনু বিল-ক়াদারি খ়াইরিহি ওয়া শাররিহ", "uʾminu bil-qadari khayrihi wa sharrih",
      "আমি তাকদিরে বিশ্বাস করি, ভালো-মন্দ সবই।", "I believe in destiny, its good and its bad."),
]
PILLARS = [
    T("أَشْهَدُ أَنْ لَا إِلٰهَ إِلَّا اللّٰهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ اللّٰهِ.", "আশহাদু আন লাː ইলাːহা ইল্লাল্লাːহ, ওয়া আশহাদু আন্না মুহ়াম্মাদান রাসূːলুল্লাːহ",
      "ashhadu an lā ilāha illallāh, wa ashhadu anna muḥammadan rasūlullāh", "আমি সাক্ষ্য দিই, আল্লাহ ছাড়া কোনো উপাস্য নেই, আর মুহাম্মদ ﷺ আল্লাহর রাসূল।",
      "I bear witness that there is no god but God, and that Muhammad is the Messenger of God.", "এটি কালিমা শাহাদাহ, ইসলামের প্রথম স্তম্ভ।"),
    T("أُصَلِّي خَمْسَ مَرَّاتٍ فِي الْيَوْمِ.", "উস়াল্লীː খ়ামসা মাররাːতিন ফ়িল-ইয়াওম", "uṣallī khamsa marrātin fil-yawm", "আমি দিনে পাঁচবার নামাজ পড়ি।", "I pray five times a day."),
    T("أَصُومُ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ.", "আস়ূːমু রামাডাːনা মিনাল-ফ়াজরি ইলাল-মাগ়রিব", "aṣūmu ramaḍāna minal-fajri ilal-maghrib",
      "আমি রমজানে ফজর থেকে মাগরিব পর্যন্ত রোজা রাখি।", "I fast in Ramadan from dawn to sunset."),
    T("أُخْرِجُ الزَّكَاةَ كُلَّ عَامٍ لِلْفُقَرَاءِ.", "উখ়রিজুজ়-জ়াকাːতা কুল্লা ʿআːমিন লিল-ফ়ুক়ারাːʾ", "ukhrijuz-zakāta kulla ʿāmin lil-fuqarāʾ",
      "আমি প্রতি বছর গরিবদের জন্য জাকাত দিই।", "Every year I give zakat to the poor."),
    T("أَرْجُو أَنْ أَحُجَّ إِلَى بَيْتِ اللّٰهِ الْحَرَامِ.", "আরজূː আন আহ়ুজ্জা ইলাː বাইতিল্লাːহিল-হ়ারাːম", "arjū an aḥujja ilā baytillāhil-ḥarām",
      "আমি আল্লাহর পবিত্র ঘরে হজ করার আশা রাখি।", "I hope to make the pilgrimage to the Sacred House of God."),
]
VALUES = [
    T("دِينِي يُعَلِّمُنِي الرَّحْمَةَ وَالصِّدْقَ.", "দীːনীː ইউʿআল্লিমুনির-রাহ়মাতা ওয়াস়-স়িদক়", "dīnī yuʿallimunir-raḥmata waṣ-ṣidq",
      "আমার ধর্ম আমাকে দয়া আর সততা শেখায়।", "My religion teaches me mercy and honesty."),
    T("لِلْجَارِ حَقٌّ كَبِيرٌ عَلَيْنَا.", "লিল-জাːরি হ়াক়্ক়ুন কাবীːরুন ʿআলাইনাː", "lil-jāri ḥaqqun kabīrun ʿalaynā",
      "আমাদের ওপর প্রতিবেশীর বড় অধিকার আছে।", "The neighbour has a great right over us."),
    T("بِرُّ الْوَالِدَيْنِ مُهِمٌّ جِدًّا عِنْدِي.", "বিররুল-ওয়াːলিদাইনি মুহিম্মুন জিদ্দান ʿইনদীː", "birrul-wālidayni muhimmun jiddan ʿindī",
      "মা-বাবার প্রতি সদ্ব্যবহার আমার কাছে খুব গুরুত্বপূর্ণ।", "Kindness to parents is very important to me."),
    T("النَّظَافَةُ جُزْءٌ مِنْ دِينِي.", "আন-নাযাːফ়াতু জুজ়ʾউন মিন দীːনীː", "an-naẓāfatu juzʾun min dīnī",
      "পরিচ্ছন্নতা আমার ধর্মের অংশ।", "Cleanliness is part of my religion.",
      "সহীহ মুসলিমের হাদিসে আছে: الطُّهُورُ شَطْرُ الْإِيمَانِ (পবিত্রতা ঈমানের অর্ধেক; মুসলিম ২২৩)।"),
    T("آكُلُ الْحَلَالَ فَقَطْ.", "আːকুলুল-হ়ালাːলা ফ়াক়াট", "ākulul-ḥalāla faqaṭ", "আমি শুধু হালাল খাই।", "I eat only halal food."),
]
IKHLAS = [
    T("قُلْ", "ক়ুল", "qul", "বলো", "say"), T("هُوَ", "হুওয়া", "huwa", "তিনি", "he"), T("اللّٰهُ", "আল্লাːহু", "allāhu", "আল্লাহ", "God"),
    T("أَحَدٌ", "আহ়াদ", "aḥad", "এক, অদ্বিতীয়", "one, unique"), T("الصَّمَدُ", "আস়-স়ামাদ", "aṣ-ṣamad", "যিনি কারও মুখাপেক্ষী নন, সবাই যাঁর মুখাপেক্ষী", "the Self-Sufficient"),
    T("لَمْ يَلِدْ", "লাম ইয়ালিদ", "lam yalid", "তিনি জন্ম দেননি", "He did not beget"), T("وَلَمْ يُولَدْ", "ওয়া লাম ইউːলাদ", "wa lam yūlad", "এবং তাঁকে জন্ম দেওয়া হয়নি", "nor was He begotten"),
    T("وَلَمْ يَكُنْ لَهُ", "ওয়া লাম ইয়াকুন লাহূː", "wa lam yakun lahū", "এবং তাঁর নেই", "and there is not for Him"), T("كُفُوًا أَحَدٌ", "কুফ়ুওয়ান আহ়াদ", "kufuwan aḥad", "সমতুল্য কেউ", "any equal"),
]
FAQ = [
    (T("لِمَاذَا تَصُومُ؟", "লিমাːদ়াː তাস়ূːম?", "limādhā taṣūm?", "আপনি রোজা রাখেন কেন?", "Why do you fast?"),
     T("لِأَنَّ اللّٰهَ أَمَرَنَا بِهِ. الصَّوْمُ يُعَلِّمُنِي الصَّبْرَ، وَيُذَكِّرُنِي بِالْفُقَرَاءِ.", "লিআন্নাল্লাːহা আমারানাː বিহ। আস়-স়াওমু ইউʿআল্লিমুনিস়-স়াবরা, ওয়া ইউদ়াক্কিরুনীː বিল-ফ়ুক়ারাːʾ",
       "li-annallāha amaranā bih. aṣ-ṣawmu yuʿallimuniṣ-ṣabra, wa yudhakkirunī bil-fuqarāʾ", "কারণ আল্লাহ আমাদের এর আদেশ দিয়েছেন। রোজা আমাকে ধৈর্য শেখায়, আর গরিবদের কথা মনে করায়।",
       "Because God commanded it. Fasting teaches me patience and reminds me of the poor.")),
    (T("وَلَا تَشْرَبُ الْمَاءَ أَيْضًا؟", "ওয়া লাː তাশরাবুল-মাːʾআ আইডাː?", "wa lā tashrabul-māʾa ayḍā?", "পানিও পান করেন না?", "You don't even drink water?"),
     T("لَا، وَلَا الْمَاءَ، مِنَ الْفَجْرِ إِلَى غُرُوبِ الشَّمْسِ فَقَطْ.", "লাː, ওয়া লাল-মাːʾআ, মিনাল-ফ়াজরি ইলাː গ়ুরূːবিশ-শামসি ফ়াক়াট",
       "lā, wa lal-māʾa, minal-fajri ilā ghurūbish-shamsi faqaṭ", "না, পানিও না; তবে শুধু ভোর থেকে সূর্যাস্ত পর্যন্ত।", "No, not even water, but only from dawn to sunset.")),
    (T("لِمَاذَا تُصَلِّي خَمْسَ مَرَّاتٍ؟", "লিমাːদ়াː তুস়াল্লীː খ়ামসা মাররাːত?", "limādhā tuṣallī khamsa marrāt?", "দিনে পাঁচবার নামাজ পড়েন কেন?", "Why do you pray five times?"),
     T("الصَّلَاةُ تُذَكِّرُنِي بِاللّٰهِ طُولَ الْيَوْمِ. وَفِي الْعَمَلِ أُصَلِّي فِي وَقْتِ الِاسْتِرَاحَةِ.", "আস়-স়ালাːতু তুদ়াক্কিরুনীː বিল্লাːহি টূːলাল-ইয়াওম। ওয়া ফ়িল-ʿআমালি উস়াল্লীː ফ়ীː ওয়াক়তিল-ইস্তিরাːহ়াহ",
       "aṣ-ṣalātu tudhakkirunī billāhi ṭūlal-yawm. wa fil-ʿamali uṣallī fī waqtil-istirāḥah", "নামাজ সারাদিন আমাকে আল্লাহর কথা মনে করায়। কাজের সময় আমি বিরতিতে নামাজ পড়ি।",
       "Prayer reminds me of God all day. At work, I pray during the break.")),
    (T("مَا مَعْنَى «حَلَال»؟", "মাː মাʿনাː হ়ালাːল?", "mā maʿnā ḥalāl?", "‘হালাল’ মানে কী?", "What does 'halal' mean?"),
     T("«حَلَال» يَعْنِي «مَسْمُوح». لَا آكُلُ لَحْمَ الْخِنْزِيرِ، وَلَا أَشْرَبُ الْخَمْرَ.", "হ়ালাːল ইয়াʿনীː মাসমূːহ়। লাː আːকুলু লাহ়মাল-খ়িনজ়ীːর, ওয়া লাː আশরাবুল-খ়ামর",
       "ḥalāl yaʿnī masmūḥ. lā ākulu laḥmal-khinzīr, wa lā ashrabul-khamr", "হালাল মানে ‘অনুমোদিত’। আমি শূকরের মাংস খাই না, মদ পান করি না।",
       "Halal means 'permitted'. I don't eat pork, and I don't drink alcohol.")),
    (T("لِمَاذَا تَلْبَسُ بَعْضُ الْمُسْلِمَاتِ الْحِجَابَ؟", "লিমাːদ়াː তালবাসু বাʿডুল-মুসলিমাːতিল-হ়িজাːব?", "limādhā talbasu baʿḍul-muslimātil-ḥijāb?",
       "কিছু মুসলিম নারী হিজাব পরেন কেন?", "Why do some Muslim women wear the hijab?"),
     T("كَثِيرٌ مِنْهُنَّ يَلْبَسْنَهُ عِبَادَةً لِلّٰهِ وَحَيَاءً.", "কাথ়ীːরুন মিনহুন্না ইয়ালবাসনাহু ʿইবাːদাতান লিল্লাːহি ওয়া হ়াইয়াːʾআː",
       "kathīrun minhunna yalbasnahu ʿibādatan lillāhi wa ḥayāʾā", "তাদের অনেকে আল্লাহর ইবাদত আর লজ্জাশীলতা হিসেবে এটি পরেন।",
       "Many of them wear it as worship of God and out of modesty.")),
    (T("مَا هُوَ الْعِيدُ؟", "মাː হুওয়াল-ʿঈːদ?", "mā huwal-ʿīd?", "ঈদ কী?", "What is Eid?"),
     T("عِنْدَنَا عِيدَانِ فِي السَّنَةِ: عِيدُ الْفِطْرِ وَعِيدُ الْأَضْحَى. نُصَلِّي وَنَأْكُلُ مَعًا وَنَزُورُ الْأَهْلَ.",
       "ʿইনদানাː ʿঈːদাːনি ফ়িস-সানাহ: ʿঈːদুল-ফ়িটরি ওয়া ʿঈːদুল-আডহ়াː। নুস়াল্লীː ওয়া নাʾকুলু মাʿআন ওয়া নাজ়ূːরুল-আহল",
       "ʿindanā ʿīdāni fis-sanah: ʿīdul-fiṭri wa ʿīdul-aḍḥā. nuṣallī wa naʾkulu maʿan wa nazūrul-ahl", "আমাদের বছরে দুটি ঈদ: ঈদুল ফিতর ও ঈদুল আজহা। আমরা নামাজ পড়ি, একসাথে খাই আর আত্মীয়দের বাড়ি যাই।",
       "We have two Eids a year: Eid al-Fitr and Eid al-Adha. We pray, eat together and visit family.")),
    (T("هَلِ «اللّٰهُ» إِلٰهٌ آخَرُ؟", "হালিল্লাːহু ইলাːহুন আːখ়ার?", "halillāhu ilāhun ākhar?", "আল্লাহ কি অন্য কোনো ঈশ্বর?", "Is 'Allah' a different god?"),
     T("لَا. «اللّٰهُ» هُوَ اسْمُ الْخَالِقِ بِالْعَرَبِيَّةِ، وَالْمَسِيحِيُّونَ الْعَرَبُ يَقُولُونَ «اللّٰهُ» أَيْضًا.",
       "লাː। আল্লাːহু হুওয়াসমুল-খ়াːলিক়ি বিল-ʿআরাবিয়্যাহ, ওয়াল-মাসীːহ়িয়্যূːনাল-ʿআরাবু ইয়াক়ূːলূːনা আল্লাːহু আইডাː",
       "lā. allāhu huwasmul-khāliqi bil-ʿarabiyyah, wal-masīḥiyyūnal-ʿarabu yaqūlūna allāhu ayḍā", "না। আরবিতে স্রষ্টার নামই ‘আল্লাহ’; আরব খ্রিস্টানরাও ‘আল্লাহ’ বলেন।",
       "No. 'Allah' is the name of the Creator in Arabic, and Arab Christians also say 'Allah'.")),
    (T("وَمَنْ هُوَ عِيسَى عِنْدَ الْمُسْلِمِينَ؟", "ওয়া মান হুওয়া ʿঈːসাː ʿইনদাল-মুসলিমীːন?", "wa man huwa ʿīsā ʿindal-muslimīn?", "মুসলিমদের কাছে ঈসা (যিশু) কে?", "And who is Jesus for Muslims?"),
     T("عِيسَى نَبِيٌّ عَظِيمٌ عِنْدَنَا، وَنُحِبُّ أُمَّهُ مَرْيَمَ كَثِيرًا.", "ʿঈːসাː নাবিয়্যুন ʿআযীːমুন ʿইনদানাː, ওয়া নুহ়িব্বু উম্মাহু মারইয়ামা কাথ়ীːরাː",
       "ʿīsā nabiyyun ʿaẓīmun ʿindanā, wa nuḥibbu ummahu maryama kathīrā", "আমাদের কাছে ঈসা (আ.) একজন মহান নবী, আর তাঁর মা মারইয়াম (আ.)-কেও আমরা খুব ভালোবাসি।",
       "For us Jesus is a great prophet, and we love his mother Mary very much.")),
    (T("مَا مَعْنَى «إِنْ شَاءَ اللّٰهُ»؟", "মাː মাʿনাː ইন শাːʾআল্লাːহ?", "mā maʿnā in shāʾallāh?", "‘ইনশাআল্লাহ’ মানে কী?", "What does 'in shā' Allāh' mean?"),
     T("مَعْنَاهَا «إِذَا أَرَادَ اللّٰهُ». نَقُولُهَا عِنْدَمَا نَتَكَلَّمُ عَنِ الْمُسْتَقْبَلِ.", "মাʿনাːহাː ইদ়াː আরাːদাল্লাːহ। নাক়ূːলুহাː ʿইনদামাː নাতাকাল্লামু ʿআনিল-মুস্তাক়বাল",
       "maʿnāhā idhā arādallāh. naqūluhā ʿindamā natakallamu ʿanil-mustaqbal", "এর মানে ‘আল্লাহ যদি চান’। ভবিষ্যতের কথা বলার সময় আমরা এটি বলি।",
       "It means 'if God wills'. We say it when we speak about the future.")),
    (T("هَلْ تَتَكَلَّمُونَ الْعَرَبِيَّةَ فِي بَنْغْلَادِيش؟", "হাল তাতাকাল্লামূːনাল-ʿআরাবিয়্যাতা ফ়ীː বানগ়লাːদীːশ?", "hal tatakallamūnal-ʿarabiyyata fī banghlādīsh?",
       "বাংলাদেশে কি আপনারা আরবি বলেন?", "Do you speak Arabic in Bangladesh?"),
     T("لُغَتُنَا الْبَنْغَالِيَّةُ، لٰكِنَّنَا نَقْرَأُ الْقُرْآنَ بِالْعَرَبِيَّةِ مُنْذُ الصِّغَرِ.", "লুগ়াতুনাল-বানগ়াːলিয়্যাহ, লাːকিন্নানাː নাক়রাʾউল-ক়ুরʾআːনা বিল-ʿআরাবিয়্যাতি মুনদ়ুস়-স়িগ়ার",
       "lughatunal-banghāliyyah, lākinnanā naqraʾul-qurʾāna bil-ʿarabiyyati mundhuṣ-ṣighar", "আমাদের ভাষা বাংলা, তবে ছোটবেলা থেকেই আমরা আরবিতে কুরআন পড়ি।",
       "Our language is Bengali, but we read the Qur'an in Arabic from childhood.")),
    (T("كَيْفَ رَمَضَانُ فِي بَلَدِكَ؟", "কাইফ়া রামাডাːনু ফ়ীː বালাদিক?", "kayfa ramaḍānu fī baladik?", "আপনার দেশে রমজান কেমন?", "What is Ramadan like in your country?"),
     T("جَمِيلٌ جِدًّا! الْمَسَاجِدُ مُمْتَلِئَةٌ، وَالنَّاسُ يُفْطِرُونَ مَعًا عَلَى التَّمْرِ وَالْأَطْعِمَةِ الشَّعْبِيَّةِ.",
       "জামীːলুন জিদ্দাː! আল-মাসাːজিদু মুমতালিʾআহ, ওয়ান-নাːসু ইউফ়টিরূːনা মাʿআন ʿআলাত-তামরি ওয়াল-আটʿইমাতিশ-শাʿবিয়্যাহ",
       "jamīlun jiddā! al-masājidu mumtaliʾah, wan-nāsu yufṭirūna maʿan ʿalat-tamri wal-aṭʿimatish-shaʿbiyyah", "খুব সুন্দর! মসজিদ ভরা থাকে, আর মানুষ খেজুর আর দেশি খাবার দিয়ে একসাথে ইফতার করে।",
       "Very beautiful! The mosques are full, and people break the fast together with dates and local food.", "দেশি ইফতারের কথা বলতে চাইলে: পেঁয়াজু, ছোলা, মুড়ি… আরবিতে নাম নেই, বাংলা নামই বলুন আর বুঝিয়ে দিন!")),
    (T("هَلْ يُمْكِنُنِي أَنْ أَزُورَ الْمَسْجِدَ؟", "হাল ইউমকিনুনীː আন আজ়ূːরাল-মাসজিদ?", "hal yumkinunī an azūral-masjid?", "আমি কি মসজিদ দেখতে যেতে পারি?", "Can I visit the mosque?"),
     T("طَبْعًا، أَهْلًا وَسَهْلًا! تَعَالَ مَعِي يَوْمَ الْجُمُعَةِ.", "টাবʿআন, আহলান ওয়া সাহলাː! তাʿআːলা মাʿঈː ইয়াওমাল-জুমুʿআহ",
       "ṭabʿan, ahlan wa sahlā! taʿāla maʿī yawmal-jumuʿah", "অবশ্যই, স্বাগতম! শুক্রবার আমার সাথে চলুন।", "Of course, you are welcome! Come with me on Friday.")),
]

def build():
    EXTRA_CSS.append(CSS)
    page(chapter_title(16, "আমার বিশ্বাসের পরিচয়", "Introducing My Faith") + """
<p class="lead">আরব দেশে আপনার চারপাশে শুধু আরবরা নন। উপসাগরের কর্মক্ষেত্রে ফিলিপাইন, নেপাল, শ্রীলঙ্কা, ভারত আর ইউরোপের সহকর্মীরা একে অপরের সাথে কথা বলেন
আরবিতেই; মিসর, জর্ডান, লেবাননে আছেন আরব খ্রিস্টান প্রতিবেশী। কেউ একদিন জানতে চাইবেন: আপনি রোজা রাখেন কেন? আবার আরব মুসলিম ভাইয়েরাও জানতে চাইবেন,
বাংলাদেশে রমজান কেমন। এই অধ্যায় আপনাকে শেখাবে নিজের বিশ্বাসের কথা সহজ, সুন্দর আর ভদ্র আরবিতে বলতে।</p>
<h3>দাওয়াতের আদব</h3>""" + ayah("ادْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِالْحِكْمَةِ وَالْمَوْعِظَةِ الْحَسَنَةِ", "«তোমার রবের পথে আহ্বান করো প্রজ্ঞা ও সুন্দর উপদেশের মাধ্যমে।»",
                                    "সূরা আন-নাহল ১৬:১২৫", pr("উদʿউ ইলাː সাবীːলি রাব্বিকা বিল-হ়িকমাতি ওয়াল-মাওʿইযাতিল-হ়াসানাহ", "udʿu ilā sabīli rabbika bil-ḥikmati wal-mawʿiẓatil-ḥasanah")) + """
<div class="cards">
 <div class="card"><div class="ct">১ · চরিত্র আগে, কথা পরে</div><div class="cb">আপনার সততা, সময়ানুবর্তিতা আর হাসিমুখ মানুষ আগে দেখবে। কথা আসবে তার পরে।</div></div>
 <div class="card"><div class="ct">২ · প্রশ্নের উত্তর দিন, বক্তৃতা নয়</div><div class="cb">যতটুকু জানতে চাওয়া হয়েছে ততটুকু, ছোট আর পরিষ্কার করে বলুন।</div></div>
 <div class="card"><div class="ct">৩ · তর্ক নয়, সম্মান</div><div class="cb">অন্যের বিশ্বাস ও মতকে সম্মান করুন। বিতর্কে জেতার চেয়ে হৃদয় জয় করা বড়।</div></div>
 <div class="card"><div class="ct">৪ · না জানলে বলুন</div><div class="cb"><span class="frw">لَا أَعْرِفُ، لٰكِنْ سَأَسْأَلُ الْإِمَامَ.</span> (লাː আʿরিফ়ু, লাːকিন সাআসʾআলুল-ইমাːম: জানি না, তবে ইমামকে জিজ্ঞেস করে জানাব।)</div></div>
</div>""", head=HEAD, anchor="ch16")

    page(h2("সালাম: প্রথম দাওয়াত") + """
<p>ইসলামের অভিবাদন নিজেই একটি দোয়া: শান্তির প্রার্থনা। পূর্ণ সালাম আর তার পূর্ণ উত্তর শিখে নিন; কেউ অর্থ জানতে চাইলে তৃতীয় বাক্যটি বলুন।</p>""" +
         lines(SALAM) + '<h2 style="margin-top:0.12in;">' + '<span>অংশ ক · «আমি মুসলিম»</span></h2>' + lines(INTRO[:4]),
         head=HEAD)
    page(lines(INTRO[4:]) + box("tip", "বলার কৌশল", "<p>নিজের পরিচয় দিন আনন্দ নিয়ে, ক্ষমা চাওয়ার সুরে নয়। অমুসলিম সহকর্মীকে বলার সময় উল্লেখ করুন যে ইসলাম ইব্রাহিম, মুসা ও ঈসা (আ.)-কে সম্মান করে: "
         "এটিই সবচেয়ে চেনা সেতু। আর আরব মুসলিম ভাইদের সাথে নিজের দেশের ইসলামের গল্প বলুন: মসজিদের দেশ বাংলাদেশ।</p>"), head=HEAD)
    page(h2("অংশ খ · আমি যা বিশ্বাস করি") + '<p>ঈমানের ছয়টি বিষয়, প্রথমে হাদিসের মূল আরবিতে, তারপর আপনার নিজের মুখের সহজ বাক্যে:</p>' +
         ayah("أَنْ تُؤْمِنَ بِاللّٰهِ وَمَلَائِكَتِهِ وَكُتُبِهِ وَرُسُلِهِ وَالْيَوْمِ الْآخِرِ، وَتُؤْمِنَ بِالْقَدَرِ خَيْرِهِ وَشَرِّهِ",
              "«(ঈমান হলো) আল্লাহ, তাঁর ফেরেশতা, তাঁর কিতাব, তাঁর রাসূল ও শেষ দিবসে বিশ্বাস করা, আর তাকদিরের ভালো-মন্দে বিশ্বাস করা।»",
              "সহীহ মুসলিম ৮ (হাদিসে জিবরিল)") + lines(BELIEF), head=HEAD)
    page(h2("অংশ গ · যেভাবে আমি বিশ্বাস যাপন করি") + '<p>ইসলামের পাঁচ স্তম্ভ, দৈনন্দিন জীবনের ভাষায়:</p>' + lines(PILLARS), head=HEAD)
    page(h2("অংশ ঘ · আমার বিশ্বাসের মূল্যবোধ") + lines(VALUES) +
         ayah("إِنَّ مِنْ خِيَارِكُمْ أَحْسَنَكُمْ أَخْلَاقًا", "«তোমাদের মধ্যে সর্বোত্তম তারা, যাদের চরিত্র সবচেয়ে সুন্দর।»", "সহীহ বুখারী ৩৫৫৯",
              pr("ইন্না মিন খ়িয়াːরিকুম আহ়সানাকুম আখ়লাːক়াː", "inna min khiyārikum aḥsanakum akhlāqā")),
         head=HEAD)
    page(h2("অংশ ঙ · আমার কুরআন") + """
<p>কুরআন মুসলিমদের কাছে আল্লাহর বাণী, আর এই বইয়ের পাঠক হিসেবে আপনার সৌভাগ্য: আপনি সেই ভাষাই শিখছেন, যে ভাষায় তা অবতীর্ণ।
সূরা আল-ইখলাস মাত্র চার আয়াতে আল্লাহর একত্বের পরিচয়; চলুন শব্দে শব্দে বুঝি।</p>""" +
         ayah("قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",
              "«বলুন, তিনি আল্লাহ, এক। আল্লাহ কারও মুখাপেক্ষী নন। তিনি কাউকে জন্ম দেননি, কেউ তাঁকে জন্ম দেয়নি। আর তাঁর সমতুল্য কেউ নেই।»",
              "সূরা আল-ইখলাস ১১২:১–৪",
              pr("ক়ুল হুওয়াল্লাːহু আহ়াদ। আল্লাːহুস়-স়ামাদ। লাম ইয়ালিদ ওয়া লাম ইউːলাদ। ওয়া লাম ইয়াকুন লাহূː কুফ়ুওয়ান আহ়াদ।",
                 "qul huwallāhu aḥad. allāhuṣ-ṣamad. lam yalid wa lam yūlad. wa lam yakun lahū kufuwan aḥad.")) +
         tr_table(IKHLAS, compact=True, numbered=False) +
         lines([T("الْقُرْآنُ كَلَامُ اللّٰهِ، نَزَلَ بِالْعَرَبِيَّةِ عَلَى النَّبِيِّ مُحَمَّدٍ.", "আল-ক়ুরʾআːনু কালাːমুল্লাːহ, নাজ়ালা বিল-ʿআরাবিয়্যাতি ʿআলান-নাবিয়্যি মুহ়াম্মাদ",
                  "al-qurʾānu kalāmullāh, nazala bil-ʿarabiyyati ʿalan-nabiyyi muḥammad", "কুরআন আল্লাহর বাণী, নবী মুহাম্মদ ﷺ-এর ওপর আরবিতে অবতীর্ণ।",
                  "The Qur'an is the word of God, revealed in Arabic to the Prophet Muhammad.")]) +
         box("culture", "তিলাওয়াত আর উচ্চারণ-লিপি", "<p>এই বইয়ের উচ্চারণ-লিপি সাধারণ পাঠের জন্য। কুরআন তিলাওয়াতে তাজবিদের আরও নিয়ম আছে (যেমন ইদগাম, গুন্নাহ, মাদ্দ); "
             "তা শিখুন একজন যোগ্য কারির কাছে। আর কাউকে কুরআনের অর্থ দেখাতে চাইলে তার নিজের ভাষার একটি নির্ভরযোগ্য অনুবাদ দিন।</p>"),
         head=HEAD)
    def qa(q, a):
        note = ('<div class="small">💬 %s</div>' % E(a["note_bn"])) if a.get("note_bn") else ""
        return ('<div class="faq"><div class="q"><span class="tag">প্রশ্ন</span><span class="qb">%s</span><div class="frq">%s</div>'
                '<div class="qp">%s · <i>%s</i></div></div>'
                '<div class="a"><span class="tag">উত্তর</span><div class="afr">%s</div><div class="ap">%s · <i>%s</i></div>'
                '<div class="ab">%s <span class="ae">/ %s</span></div>%s</div></div>') % (
            E(q["bn"]), E(q["fr"]), E(q["bn_pron"]), E(q["en_pron"]),
            E(a["fr"]), E(a["bn_pron"]), E(a["en_pron"]), E(a["bn"]), E(a["en"]), note)
    for k in range(0, 12, 3):
        body = "".join(qa(q, a) for q, a in FAQ[k:k + 3])
        title = "প্রতিবেশী বা সহকর্মী জানতে চাইলে"
        page((h2(title) if k == 0 else "") + (('<p class="small" style="margin-bottom:0.05in;">ছোট উত্তর, উষ্ণ সুর, শেষে একটি আমন্ত্রণ। প্রথম নয়টি প্রশ্ন সাধারণত অমুসলিম সহকর্মীরা করেন; '
              'শেষ তিনটি করেন আরব মুসলিম বন্ধুরা। এখানে পুরুষকে সম্বোধন (<span class="frw">أَنْتَ</span>); নারীকে বলতে ক্রিয়ার রূপ বদলায় (অধ্যায় ১১)।</p>') if k == 0 else "") + body, head=HEAD)

    page.done()

CSS = """
.faq{margin:0 0 0.07in;line-height:1.3;border:0.75pt solid var(--line);border-radius:3pt;background:#fff;}
.faq .q{background:var(--gold-l);padding:0.035in 0.09in;}
.faq .a{padding:0.035in 0.09in 0.04in;}
.faq .tag{font-family:BnSans;font-weight:600;font-size:8pt;color:#fff;background:var(--gold);border-radius:6pt;padding:0 0.06in;margin-right:0.06in;}
.faq .a .tag{background:var(--brand);}
.faq .frq{font-family:Arabic,serif;font-weight:700;color:var(--accent);font-size:13.5pt;line-height:1.45;direction:rtl;text-align:right;}
.faq .qb{font-size:9.3pt;font-weight:700;}
.faq .qp,.faq .ap{font-size:8.4pt;line-height:1.3;color:var(--muted);}
.faq .qp i,.faq .ap i{font-family:Lat,LatX;}
.faq .afr{font-family:Arabic,serif;font-weight:700;color:var(--accent);font-size:13.5pt;line-height:1.5;margin-top:0.02in;direction:rtl;text-align:right;}
.faq .ab{font-size:9.2pt;line-height:1.35;}
.faq .ae{font-family:Lat;color:var(--muted);font-size:8.8pt;}
"""
