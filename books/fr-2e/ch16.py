# -*- coding: utf-8 -*-
"""Ch. 16 — আমার বিশ্বাসের পরিচয় · Introducing My Faith (70% introduce your faith, 30% FAQ).
Qur'an and hadith quotations: verify against Quran.com (French: Muhammad Hamidullah) and Sunnah.com before print;
scholar review gate applies (BOOK-STRUCTURE §7)."""
from part23 import FlowPages
page = FlowPages()
from engine import E, bn, box, h2, tr_line, chapter_title, EXTRA_CSS

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

def ayah(ar, bn_txt, ref, fr=None):
    frl = ('<div style="font-family:Lat;font-style:italic;color:var(--accent);text-align:center;font-size:11pt;margin-top:0.05in;">%s</div>' % E(fr)) if fr else ""
    return ('<div style="border:1.2pt solid var(--gold);background:#fff;border-radius:3pt;padding:0.14in 0.2in 0.1in;margin:0.06in 0 0.14in;">'
            '<div class="ar" style="font-size:19pt;line-height:1.85;text-align:center;color:var(--brand);">%s</div>%s'
            '<div style="text-align:center;font-size:11pt;margin-top:0.05in;">%s</div>'
            '<div style="text-align:center;font-family:BnSans;font-weight:600;font-size:9pt;color:var(--gold);margin-top:0.04in;">%s</div></div>') % (ar, frl, bn_txt, ref)

INTRO = [
    T("Je suis musulman.", "ঝ়ে° সুই মি°জ়ি°লমাঁ", "zhuh swee mü-zül-MAHN", "আমি মুসলিম (পুরুষ)।", "I am a Muslim (man)."),
    T("Je suis musulmane.", "ঝ়ে° সুই মি°জ়ি°লমান", "zhuh swee mü-zül-MAN", "আমি মুসলিম (নারী)।", "I am a Muslim (woman)."),
    T("L'islam veut dire la paix et la soumission à Dieu.", "লিসলাম ভে° দির় লা পে এ লা সুমিসিয়োঁ আ দিয়ে°",
      "lees-lahm vuh deer lah peh ay lah soo-mee-SYOHN ah DYUH", "ইসলাম মানে শান্তি এবং আল্লাহর কাছে আত্মসমর্পণ।", "Islam means peace and submission to God."),
    T("Je crois en un seul Dieu : Allah.", "ঝ়ে° ক্র়োয়া আঁ ন্যাঁ সে°ল দিয়ে° : আল্লা", "zhuh krwah ahn-nuhn suhl DYUH: ah-LAH",
      "আমি এক আল্লাহয় বিশ্বাস করি।", "I believe in one God: Allah."),
    T("Muhammad est Son dernier messager.", "মুআমাদ এ সোঁ দের়নিয়ে মেসাঝ়ে", "moo-ah-mahd ay sohn dehr-nyay meh-sah-ZHAY",
      "মুহাম্মদ ﷺ তাঁর শেষ রাসূল।", "Muhammad is His last messenger.", "নামের পরে বলতে পারেন: que la paix soit sur lui (কে° লা পে সোয়া সি°র় লুই) = তাঁর ওপর শান্তি বর্ষিত হোক।"),
    T("Je crois aussi en Abraham, Moïse et Jésus.", "ঝ়ে° ক্র়োয়া ওসি আঁ নাব্র়াআম, মোইজ় এ ঝ়েজ়ি°", "zhuh krwah oh-SEE ahn-nah-brah-AHM, moh-EEZ ay zhay-ZÜ",
      "আমি ইব্রাহিম, মুসা ও ঈসা (আ.)-এর প্রতিও বিশ্বাস রাখি।", "I also believe in Abraham, Moses and Jesus.", "ফরাসিভাষী মুসলিমরা Ibrahim, Moussa, Issa নামও ব্যবহার করেন।"),
    T("Pour moi, l'islam est une manière de vivre.", "পুর় মোয়া, লিসলাম এ তি°ন মানিয়ের় দে° ভ়িভ়র়", "poor MWAH, lees-lahm ay tün mah-NYEHR duh VEEVR",
      "আমার কাছে ইসলাম একটি জীবনধারা।", "For me, Islam is a way of life."),
]
BELIEF = [
    T("Je crois en Allah, le Dieu unique.", "ঝ়ে° ক্র়োয়া আঁ নালা, লে° দিয়ে° ই°নিক", "zhuh krwah ahn-nah-LAH, luh dyuh ü-NEEK", "আমি এক ও অদ্বিতীয় আল্লাহয় বিশ্বাস করি।", "I believe in Allah, the One God."),
    T("Je crois aux anges.", "ঝ়ে° ক্র়োয়া ও জ়াঁঝ়", "zhuh krwah oh-ZAHNZH", "আমি ফেরেশতাদের প্রতি বিশ্বাস করি।", "I believe in the angels."),
    T("Je crois aux livres révélés : la Torah, l'Évangile et le Coran.", "ঝ়ে° ক্র়োয়া ও লিভ়র় র়েভ়েলে : লা তোর়া, লেভ়াঁঝ়িল এ লে° কোর়াঁ",
      "zhuh krwah oh leevr ray-vay-LAY: lah toh-RAH, lay-vahn-ZHEEL ay luh koh-RAHN", "আমি আসমানি কিতাবে বিশ্বাস করি: তাওরাত, ইঞ্জিল ও কুরআন।", "I believe in the revealed books: the Torah, the Gospel and the Qur'an."),
    T("Je crois à tous les prophètes.", "ঝ়ে° ক্র়োয়া আ তু লে প্র়োফ়েত", "zhuh krwah ah too lay proh-FET", "আমি সকল নবীর প্রতি বিশ্বাস করি।", "I believe in all the prophets."),
    T("Je crois au Jour dernier.", "ঝ়ে° ক্র়োয়া ও ঝ়ুর় দের়নিয়ে", "zhuh krwah oh zhoor dehr-NYAY", "আমি আখিরাত (শেষ দিবস)-এ বিশ্বাস করি।", "I believe in the Last Day."),
    T("Je crois au destin, le bon comme le mauvais.", "ঝ়ে° ক্র়োয়া ও দেস্ত্যাঁ, লে° বোঁ কোম লে° মোভ়ে", "zhuh krwah oh dehs-TEHN, luh bohn kom luh moh-VEH",
      "আমি তাকদিরে বিশ্বাস করি, ভালো-মন্দ সবই।", "I believe in destiny, the good and the bad."),
]
PILLARS = [
    T("Je témoigne qu'il n'y a de dieu qu'Allah, et que Muhammad est Son messager.", "ঝ়ে° তেমোয়ান্য কিল নি ইয়া দে° দিয়ে° কালা, এ কে° মুআমাদ এ সোঁ মেসাঝ়ে",
      "zhuh tay-MWAHN-yuh keel nee-yah duh dyuh kah-LAH, ay kuh moo-ah-mahd ay sohn meh-sah-ZHAY", "আমি সাক্ষ্য দিই, আল্লাহ ছাড়া কোনো উপাস্য নেই, আর মুহাম্মদ ﷺ তাঁর রাসূল।",
      "I bear witness that there is no god but Allah, and that Muhammad is His messenger.", "এটি কালিমা শাহাদাহ, ইসলামের প্রথম স্তম্ভ।"),
    T("Je prie cinq fois par jour.", "ঝ়ে° প্র়ি স্যাঁক ফ়োয়া পার় ঝ়ুর়", "zhuh pree sehnk fwah par ZHOOR", "আমি দিনে পাঁচবার নামাজ পড়ি।", "I pray five times a day."),
    T("Pendant le Ramadan, je jeûne de l'aube au coucher du soleil.", "পাঁদাঁ লে° র়ামাদান, ঝ়ে° ঝ়ে°ন দে° লোব ও কুশে দি° সোলেই",
      "pahn-dahn luh rah-mah-DAHN, zhuh zhuhn duh lohb oh koo-shay dü soh-LAY", "রমজানে আমি ভোর থেকে সূর্যাস্ত পর্যন্ত রোজা রাখি।", "During Ramadan, I fast from dawn to sunset."),
    T("Chaque année, je donne une partie de mon argent aux pauvres.", "শাক আনে, ঝ়ে° দোন ই°ন পার়তি দে° মোঁ নার়ঝ়াঁ ও পোভ়র়",
      "shahk ah-NAY, zhuh dun ün par-TEE duh mohn-nar-ZHAHN oh POHVR", "প্রতি বছর আমি আমার সম্পদের একটি অংশ গরিবদের দিই।", "Every year, I give part of my money to the poor.", "এটি জাকাত। ফরাসিতে বলে la zakat বা l'aumône obligatoire।"),
    T("Un jour, j'espère faire le pèlerinage à La Mecque.", "অ্যাঁ ঝ়ুর়, ঝ়েসপের় ফ়ের় লে° পেলর়িনাঝ় আ লা মেক",
      "uhn ZHOOR, zhes-PEHR fehr luh pel-ree-NAHZH ah lah MEK", "একদিন আমি মক্কায় হজ করার আশা রাখি।", "One day, I hope to make the pilgrimage to Mecca."),
]
VALUES = [
    T("Ma foi m'apprend la miséricorde et l'honnêteté.", "মা ফ়োয়া মাপ্র়াঁ লা মিজ়ের়িকোর়দ এ লোনেত্তে", "mah FWAH mah-PRAHN lah mee-zay-ree-KORD ay loh-net-TAY",
      "আমার বিশ্বাস আমাকে দয়া আর সততা শেখায়।", "My faith teaches me mercy and honesty."),
    T("Le voisin a un grand droit sur nous.", "লে° ভ়োয়াজ়্যাঁ আ অ্যাঁ গ্র়াঁ দ্র়োয়া সি°র় নু", "luh vwah-ZEHN ah uhn grahn drwah sür NOO",
      "আমাদের ওপর প্রতিবেশীর বড় অধিকার আছে।", "Our neighbour has a great right over us."),
    T("Le respect des parents est très important pour moi.", "লে° র়েসপে দে পার়াঁ এ ত্র়ে জ়্যাঁপোর়তাঁ পুর় মোয়া", "luh res-PEH day pah-RAHN ay treh-zehn-por-TAHN poor MWAH",
      "মা-বাবাকে সম্মান করা আমার কাছে খুব গুরুত্বপূর্ণ।", "Respect for parents is very important to me."),
    T("La propreté fait partie de ma foi.", "লা প্র়োপ্র়ে°তে ফ়ে পার়তি দে° মা ফ়োয়া", "lah proh-pruh-TAY feh par-TEE duh mah FWAH",
      "পরিচ্ছন্নতা আমার বিশ্বাসের অংশ।", "Cleanliness is part of my faith."),
    T("Je mange halal : pas de porc, pas d'alcool.", "ঝ়ে° মাঁঝ় আলাল : পা দে° পোর়, পা দালকোল", "zhuh mahnzh ah-LAHL: pah duh POR, pah dahl-KOHL",
      "আমি হালাল খাই: শূকরের মাংস নয়, মদ নয়।", "I eat halal: no pork, no alcohol."),
]
FAQ = [
    (T("Pourquoi vous jeûnez ?", "পুর়কোয়া ভ়ু ঝ়ে°নে", "poor-kwah voo zhuh-NAY", "আপনি রোজা রাখেন কেন?", "Why do you fast?"),
     T("C'est un ordre de Dieu. Le jeûne m'apprend la patience, et je pense aux pauvres qui ont faim.", "সে ত্যাঁ নর়দ্র় দে° দিয়ে°। লে° ঝ়ে°ন মাপ্র়াঁ লা পাসিয়াঁস, এ ঝ়ে° পাঁস ও পোভ়র় কি ওঁ ফ়্যাঁ",
       "say-tuhn-NORDR duh DYUH. luh zhuhn mah-PRAHN lah pah-SYAHNS, ay zhuh pahns oh pohvr kee ohn FEHN", "এটি আল্লাহর আদেশ। রোজা আমাকে ধৈর্য শেখায়, আর ক্ষুধার্ত গরিবদের কথা মনে করায়।", "It is God's command. Fasting teaches me patience, and I think of the hungry poor.")),
    (T("Vous ne buvez même pas d'eau ?", "ভ়ু নে° বি°ভ়ে মেম পা দো", "voo nuh bü-vay mem pah DOH", "আপনি পানিও খান না?", "You don't even drink water?"),
     T("Non, même pas d'eau. Mais seulement de l'aube au coucher du soleil.", "নোঁ, মেম পা দো। মে সে°লমাঁ দে° লোব ও কুশে দি° সোলেই",
       "nohn, mem pah DOH. meh suhl-MAHN duh lohb oh koo-shay dü soh-LAY", "না, পানিও না। তবে শুধু ভোর থেকে সূর্যাস্ত পর্যন্ত।", "No, not even water. But only from dawn to sunset.")),
    (T("Pourquoi vous priez cinq fois par jour ?", "পুর়কোয়া ভ়ু প্র়িয়ে স্যাঁক ফ়োয়া পার় ঝ়ুর়", "poor-kwah voo pree-YAY sehnk fwah par ZHOOR", "আপনি দিনে পাঁচবার নামাজ পড়েন কেন?", "Why do you pray five times a day?"),
     T("La prière me rappelle Dieu toute la journée. Au travail, je prie pendant ma pause, dans un coin calme.", "লা প্র়িয়ের় মে° র়াপেল দিয়ে° তুত লা ঝ়ুর়নে। ও ত্র়াভ়াই, ঝ়ে° প্র়ি পাঁদাঁ মা পোজ়, দাঁ জ়্যাঁ কোয়্যাঁ কালম",
       "lah pree-YEHR muh rah-PEL dyuh toot lah zhoor-NAY. oh trah-VAI, zhuh pree pahn-dahn mah POHZ, dahn-zuhn kwehn KALM", "নামাজ সারাদিন আমাকে আল্লাহর কথা মনে করায়। কাজের জায়গায় আমি বিরতির সময় একটি নিরিবিলি কোণে নামাজ পড়ি।", "Prayer reminds me of God all day. At work, I pray during my break, in a quiet corner.")),
    (T("Ça veut dire quoi, « halal » ?", "সা ভে° দির় কোয়া, আলাল", "sah vuh deer KWAH, ah-LAHL", "‘হালাল’ মানে কী?", "What does 'halal' mean?"),
     T("Halal veut dire « permis ». Je ne mange pas de porc et je ne bois pas d'alcool.", "আলাল ভে° দির় পের়মি। ঝ়ে° নে° মাঁঝ় পা দে° পোর় এ ঝ়ে° নে° বোয়া পা দালকোল",
       "ah-LAHL vuh deer pehr-MEE. zhuh nuh mahnzh pah duh POR ay zhuh nuh bwah pah dahl-KOHL", "হালাল মানে ‘অনুমোদিত’। আমি শূকরের মাংস খাই না, মদ পান করি না।", "Halal means 'permitted'. I don't eat pork and I don't drink alcohol.")),
    (T("Pourquoi certaines femmes musulmanes portent un foulard ?", "পুর়কোয়া সের়তেন ফ়াম মি°জ়ি°লমান পোর়ত অ্যাঁ ফ়ুলার়", "poor-kwah sehr-ten fahm mü-zül-man port uhn foo-LAR",
       "কিছু মুসলিম নারী স্কার্ফ পরেন কেন?", "Why do some Muslim women wear a headscarf?"),
     T("Pour beaucoup de femmes, c'est un acte de foi et de pudeur. C'est leur choix.", "পুর় বোকু দে° ফ়াম, সে ত্যাঁ নাক্ত দে° ফ়োয়া এ দে° পি°দে°র়। সে লে°র় শোয়া",
       "poor boh-koo duh FAHM, say-tuhn-NAKT duh fwah ay duh pü-DUHR. say luhr SHWAH", "অনেক নারীর কাছে এটি বিশ্বাস আর শালীনতার প্রকাশ। এটি তাদের নিজের সিদ্ধান্ত।", "For many women, it is an act of faith and modesty. It is their choice.")),
    (T("C'est quoi, l'Aïd ?", "সে কোয়া, লাইদ", "say KWAH, lah-EED", "ঈদ কী?", "What is Eid?"),
     T("C'est notre fête. Il y en a deux par an. On prie, on partage un repas et on rend visite à la famille.", "সে নোত্র় ফ়েত। ইল ইয়াঁ না দে° পার় আঁ। ওঁ প্র়ি, ওঁ পার়তাঝ় অ্যাঁ র়ে°পা এ ওঁ র়াঁ ভ়িজ়িত আ লা ফ়ামিই",
       "say nohtr FET. eel yahn-nah duh par AHN. ohn PREE, ohn par-tahzh uhn ruh-PAH ay ohn rahn vee-zeet ah lah fah-MEE", "এটি আমাদের উৎসব। বছরে দুটি। আমরা নামাজ পড়ি, একসাথে খাই আর আত্মীয়দের বাড়ি যাই।", "It is our festival. There are two a year. We pray, share a meal and visit family.", "ঈদুল ফিতর (রমজানের শেষে) ও ঈদুল আজহা। পশ্চিম আফ্রিকায় ঈদুল আজহাকে বলে la Tabaski।")),
    (T("Allah, c'est un autre Dieu ?", "আল্লা, সে ত্যাঁ নোত্র় দিয়ে°", "ah-LAH, say-tuhn-NOHTR DYUH", "আল্লাহ কি অন্য কোনো ঈশ্বর?", "Is Allah a different God?"),
     T("Non. « Allah » veut dire « Dieu » en arabe. Les chrétiens arabes disent aussi « Allah ».", "নোঁ। আল্লা ভে° দির় দিয়ে° আঁ নার়াব। লে ক্র়েতিয়্যাঁ জ়ার়াব দিজ় ওসি আল্লা",
       "NOHN. ah-LAH vuh deer DYUH ahn-nah-RAHB. lay kray-tyehn-zah-RAHB deez oh-SEE ah-LAH", "না। আরবিতে ‘আল্লাহ’ মানেই ‘ঈশ্বর’। আরব খ্রিস্টানরাও ‘আল্লাহ’ বলেন।", "No. 'Allah' means 'God' in Arabic. Arab Christians also say 'Allah'.")),
    (T("Et Jésus, pour les musulmans ?", "এ ঝ়েজ়ি°, পুর় লে মি°জ়ি°লমাঁ", "ay zhay-ZÜ, poor lay mü-zül-MAHN", "আর মুসলিমদের কাছে যিশু (ঈসা)?", "And Jesus, for Muslims?"),
     T("Pour nous, Jésus est un grand prophète, et nous aimons beaucoup sa mère, Marie.", "পুর় নু, ঝ়েজ়ি° এ ত্যাঁ গ্র়াঁ প্র়োফ়েত, এ নু জ়েমোঁ বোকু সা মের়, মার়ি",
       "poor NOO, zhay-ZÜ ay-tuhn grahn proh-FET, ay noo-zay-MOHN boh-KOO sah MEHR, mah-REE", "আমাদের কাছে ঈসা (আ.) একজন মহান নবী, আর তাঁর মা মারইয়াম (আ.)-কেও আমরা খুব ভালোবাসি।", "For us, Jesus is a great prophet, and we love his mother Mary very much.")),
    (T("« Inch'Allah », ça veut dire quoi ?", "ইনশাল্লা, সা ভে° দির় কোয়া", "een-shah-LAH, sah vuh deer KWAH", "‘ইনশাআল্লাহ’ মানে কী?", "What does 'Inshallah' mean?"),
     T("Ça veut dire « si Dieu le veut ». On le dit quand on parle du futur.", "সা ভে° দির় সি দিয়ে° লে° ভে°। ওঁ লে° দি কাঁ তোঁ পার়ল দি° ফ়ি°তি°র়",
       "sah vuh deer see dyuh luh VUH. ohn luh dee kahn-tohn parl dü fü-TÜR", "এর মানে ‘আল্লাহ যদি চান’। ভবিষ্যতের কথা বলার সময় আমরা এটি বলি।", "It means 'if God wills'. We say it when we talk about the future.")),
    (T("Je peux visiter une mosquée ?", "ঝ়ে° পে° ভ়িজ়িতে ই°ন মোসকে", "zhuh puh vee-zee-tay ün mos-KAY", "আমি কি মসজিদ দেখতে যেতে পারি?", "Can I visit a mosque?"),
     T("Bien sûr, vous êtes le bienvenu ! C'est notre lieu de prière. Venez avec moi vendredi.", "বিয়্যাঁ সি°র়, ভ়ু জ়েত লে° বিয়্যাঁভ়নি°! সে নোত্র় লিয়ে° দে° প্র়িয়ের়। ভ়ে°নে আভ়েক মোয়া ভ়াঁদ্র়ে°দি",
       "byehn SÜR, voo-zet luh byehn-vuh-NÜ! say nohtr lyuh duh pree-YEHR. vuh-nay ah-vek mwah vahn-druh-DEE", "অবশ্যই, আপনাকে স্বাগতম! এটি আমাদের নামাজের জায়গা। শুক্রবার আমার সাথে চলুন।", "Of course, you are welcome! It is our place of prayer. Come with me on Friday.")),
    (T("C'est quoi, le Coran ?", "সে কোয়া, লে° কোর়াঁ", "say KWAH, luh koh-RAHN", "কুরআন কী?", "What is the Qur'an?"),
     T("C'est la parole de Dieu, révélée au prophète Muhammad. Je peux vous montrer une traduction en français.", "সে লা পার়োল দে° দিয়ে°, র়েভ়েলে ও প্র়োফ়েত মুআমাদ। ঝ়ে° পে° ভ়ু মোঁত্র়ে ই°ন ত্র়াদি°ক্সিয়োঁ আঁ ফ়্র়াঁসে",
       "say lah pah-ROL duh DYUH, ray-vay-LAY oh proh-fet moo-ah-MAHD. zhuh puh voo mohn-tray ün trah-dük-SYOHN ahn frahn-SEH", "এটি আল্লাহর বাণী, নবী মুহাম্মদ ﷺ-এর ওপর অবতীর্ণ। আমি আপনাকে ফরাসি অনুবাদ দেখাতে পারি।", "It is the word of God, revealed to the Prophet Muhammad. I can show you a French translation.")),
    (T("Je peux venir à votre iftar ?", "ঝ়ে° পে° ভ়ে°নির় আ ভ়োত্র় ইফ়তার়", "zhuh puh vuh-NEER ah vohtr eef-TAR", "আমি কি আপনার ইফতারে আসতে পারি?", "Can I come to your iftar?"),
     T("Avec plaisir ! L'iftar, c'est le repas qui rompt le jeûne. Venez ce soir !", "আভ়েক প্লেজ়ির়! লিফ়তার়, সে লে° র়ে°পা কি র়োঁ লে° ঝ়ে°ন। ভ়ে°নে সে° সোয়ার়!",
       "ah-vek pleh-ZEER! leef-TAR, say luh ruh-PAH kee rohn luh ZHUHN. vuh-nay suh SWAR", "সানন্দে! ইফতার হলো রোজা ভাঙার খাবার। আজ সন্ধ্যায় আসুন!", "With pleasure! Iftar is the meal that breaks the fast. Come this evening!")),
]

def build():
    EXTRA_CSS.append(CSS)
    page(chapter_title(16, "আমার বিশ্বাসের পরিচয়", "Introducing My Faith") + """
<p class="lead">ফরাসিভাষী দেশে আপনার সহকর্মী, প্রতিবেশী বা সহপাঠী একদিন জানতে চাইবেন: আপনি রোজা রাখেন কেন? দিনে কয়েকবার কোথায় যান?
সেই মুহূর্তটি একটি সুযোগ। এই অধ্যায় আপনাকে শেখাবে নিজের বিশ্বাসের কথা সহজ, সুন্দর আর ভদ্র ফরাসিতে বলতে।</p>
<h3>দাওয়াতের আদব</h3>""" + ayah("ادْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِالْحِكْمَةِ وَالْمَوْعِظَةِ الْحَسَنَةِ", "«তোমার রবের পথে আহ্বান করো প্রজ্ঞা ও সুন্দর উপদেশের মাধ্যমে।»", "সূরা আন-নাহল ১৬:১২৫") + """
<div class="cards">
 <div class="card"><div class="ct">১ · চরিত্র আগে, কথা পরে</div><div class="cb">আপনার সততা, সময়ানুবর্তিতা আর হাসিমুখ মানুষ আগে দেখবে। কথা আসবে তার পরে।</div></div>
 <div class="card"><div class="ct">২ · প্রশ্নের উত্তর দিন, বক্তৃতা নয়</div><div class="cb">যতটুকু জানতে চাওয়া হয়েছে ততটুকু, ছোট আর পরিষ্কার করে বলুন।</div></div>
 <div class="card"><div class="ct">৩ · তর্ক নয়, সম্মান</div><div class="cb">অন্যের বিশ্বাস ও মতকে সম্মান করুন। বিতর্কে জেতার চেয়ে হৃদয় জয় করা বড়।</div></div>
 <div class="card"><div class="ct">৪ · না জানলে বলুন</div><div class="cb">«Je ne sais pas, mais je peux demander à l'imam.» (জানি না, তবে ইমামকে জিজ্ঞেস করে জানাতে পারি।)</div></div>
</div>""", head=HEAD, anchor="ch16")

    page(h2("সালাম: প্রথম দাওয়াত") + """
<p>ইসলামের অভিবাদন নিজেই একটি দোয়া: শান্তির প্রার্থনা। মুসলিমদের সাথে আরবিতেই সালাম দিন; অমুসলিম বন্ধু জানতে চাইলে ফরাসিতে অর্থ বুঝিয়ে বলুন।</p>""" +
         lines([T("As-salâmou ʿalaykoum.", "আসসালামু আলাইকুম", "ah-sah-lah-moo ah-lay-KOOM", "আসসালামু আলাইকুম।", "Peace be upon you."),
                T("Ça veut dire : « Que la paix soit sur vous. »", "সা ভে° দির় : কে° লা পে সোয়া সি°র় ভ়ু", "sah vuh DEER: kuh lah peh swah sür VOO", "এর মানে: আপনার ওপর শান্তি বর্ষিত হোক।", "It means: 'May peace be upon you.'"),
                T("Et la réponse : « Et sur vous la paix. »", "এ লা র়েপোঁস : এ সি°র় ভ়ু লা পে", "ay lah ray-POHNS: ay sür voo lah PEH", "আর উত্তর: আপনার ওপরও শান্তি।", "And the reply: 'And upon you be peace.'")]) +
         '<h2 style="margin-top:0.12in;">' + '<span>অংশ ক · «আমি মুসলিম»</span></h2>' + lines(INTRO[:4]),
         head=HEAD)
    page(lines(INTRO[4:]) + box("tip", "বলার কৌশল", "<p>নিজের পরিচয় দিন আনন্দ নিয়ে, ক্ষমা চাওয়ার সুরে নয়। আর সবার আগে উল্লেখ করুন যে ইসলাম ইব্রাহিম, মুসা ও ঈসা (আ.)-কে সম্মান করে: "
         "ফরাসিভাষী শ্রোতার কাছে এটিই সবচেয়ে চেনা সেতু।</p>"), head=HEAD)
    page(h2("অংশ খ · আমি যা বিশ্বাস করি") + '<p>ঈমানের ছয়টি বিষয়, সহজ ফরাসি বাক্যে:</p>' + lines(BELIEF), head=HEAD)
    page(h2("অংশ গ · যেভাবে আমি বিশ্বাস যাপন করি") + '<p>ইসলামের পাঁচ স্তম্ভ, দৈনন্দিন জীবনের ভাষায়:</p>' + lines(PILLARS), head=HEAD)
    page(h2("অংশ ঘ · আমার বিশ্বাসের মূল্যবোধ") + lines(VALUES) +
         ayah("إِنَّ مِنْ خِيَارِكُمْ أَحْسَنَكُمْ أَخْلَاقًا", "«তোমাদের মধ্যে সর্বোত্তম তারা, যাদের চরিত্র সবচেয়ে সুন্দর।»", "সহীহ বুখারী ৩৫৫৯",
              "« Les meilleurs d'entre vous sont ceux qui ont le meilleur caractère. »"),
         head=HEAD)
    page(h2("অংশ ঙ · আমার কুরআন") + """
<p>কুরআন মুসলিমদের কাছে আল্লাহর বাণী, আরবিতে অবতীর্ণ। ফরাসিভাষী বন্ধুকে দেখানোর জন্য সূরা আল-ইখলাস সবচেয়ে উপযুক্ত:
মাত্র চার আয়াতে আল্লাহর একত্বের পরিচয়।</p>""" +
         ayah("قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",
              "«বলুন, তিনি আল্লাহ, এক। আল্লাহ কারও মুখাপেক্ষী নন। তিনি কাউকে জন্ম দেননি, কেউ তাঁকে জন্ম দেয়নি। আর তাঁর সমতুল্য কেউ নেই।»",
              "সূরা আল-ইখলাস ১১২:১–৪ · ফরাসি অনুবাদ: মুহাম্মদ হামিদুল্লাহ",
              "Dis : « Il est Allah, Unique. Allah, Le Seul à être imploré pour ce que nous désirons. Il n'a jamais engendré, n'a pas été engendré non plus. Et nul n'est égal à Lui. »") +
         lines([T("Voici une traduction du Coran en français.", "ভ়োয়াসি ই°ন ত্র়াদি°ক্সিয়োঁ দি° কোর়াঁ আঁ ফ়্র়াঁসে", "vwah-SEE ün trah-dük-SYOHN dü koh-RAHN ahn frahn-SEH",
                  "এই যে কুরআনের একটি ফরাসি অনুবাদ।", "Here is a French translation of the Qur'an.")]) +
         box("culture", "অনুবাদ সম্পর্কে", "<p>ফরাসিভাষী মুসলিমদের মধ্যে বহুল প্রচলিত অনুবাদ মুহাম্মদ হামিদুল্লাহর (Muhammad Hamidullah)। মনে রাখবেন, অনুবাদ কুরআনের অর্থের ব্যাখ্যা; মূল কুরআন আরবিতে।</p>"),
         head=HEAD)
    # Part B FAQ, 30%: 3 pages
    def qa(q, a):
        note = ('<div class="small">💬 %s</div>' % E(a["note_bn"])) if a.get("note_bn") else ""
        return ('<div class="faq"><div class="q"><span class="tag">প্রশ্ন</span><span class="frq">%s</span> <span class="qb">%s</span>'
                '<div class="qp">%s · <i>%s</i></div></div>'
                '<div class="a"><span class="tag">উত্তর</span><div class="afr">%s</div><div class="ap">%s · <i>%s</i></div>'
                '<div class="ab">%s <span class="ae">/ %s</span></div>%s</div></div>') % (
            E(q["fr"]), E(q["bn"]), E(q["bn_pron"]), E(q["en_pron"]),
            E(a["fr"]), E(a["bn_pron"]), E(a["en_pron"]), E(a["bn"]), E(a["en"]), note)
    for k in range(0, 12, 4):
        body = "".join(qa(q, a) for q, a in FAQ[k:k + 4])
        title = "প্রতিবেশী বা সহকর্মী জানতে চাইলে"
        page((h2(title) if k == 0 else "") + (('<p class="small" style="margin-bottom:0.05in;">ছোট উত্তর, উষ্ণ সুর, শেষে একটি আমন্ত্রণ। এখানে <span class="frw">vous</span>; ঘনিষ্ঠ বন্ধুর সাথে <span class="frw">tu</span>।</p>') if k == 0 else "") + body, head=HEAD)

    page.done()

CSS = """
.faq{margin:0 0 0.07in;line-height:1.3;border:0.75pt solid var(--line);border-radius:3pt;background:#fff;}
.faq .q{background:var(--gold-l);padding:0.035in 0.09in;}
.faq .a{padding:0.035in 0.09in 0.04in;}
.faq .tag{font-family:BnSans;font-weight:600;font-size:8pt;color:#fff;background:var(--gold);border-radius:6pt;padding:0 0.06in;margin-right:0.06in;}
.faq .a .tag{background:var(--brand);}
.faq .frq{font-family:Lat,LatX;font-weight:700;color:var(--accent);font-size:10pt;}
.faq .qb{font-size:9.3pt;}
.faq .qp,.faq .ap{font-size:8.4pt;line-height:1.3;color:var(--muted);}
.faq .afr{font-family:Lat,LatX;font-weight:700;color:var(--accent);font-size:9.8pt;line-height:1.3;margin-top:0.02in;}
.faq .ab{font-size:9.2pt;line-height:1.35;}
.faq .ae{font-family:Lat;color:var(--muted);font-size:8.8pt;}
"""
