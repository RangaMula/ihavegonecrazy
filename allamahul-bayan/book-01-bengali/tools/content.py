# -*- coding: utf-8 -*-
"""All words, phonetics and texts for Book 1 (Bengali) of the Allamahul Bayan Series.

Rules followed (Maktabatu Kunujul Akhirah house rules, from the Arabic-for-Kids master brief):
  * every Bengali item = Bengali script + simple English transliteration (italic) + English meaning
  * pictures are objects, plants and nature only - no people or animals with faces
  * every Qur'an quote carries surah:verse and a superscript that resolves on the References page
"""

BOOK = {
    "series": "Allamahul Bayan Series",
    "series_ar": "عَلَّمَهُ الْبَيَانَ",
    "series_no": 1,
    "title": "My First Bengali Alphabet",
    "title_bn": "আমার প্রথম বাংলা বর্ণমালা",
    "subtitle": "A Coloring Book to Learn, Trace & Say the 50 Bangla Letters with English Phonetics",
    "author": "Hafez Abdullah Muhammad Minhaz Reza",
    "author_short": "Minhaz Reza",
    "illustrator": "AI-assisted illustrations",
    "publisher": "Maktabatu Kunujul Akhirah",
    "publisher_ar": "مكتبة كنوز الآخرة",
    "publisher_note": "An imprint of the Kunujul Akhirah Charitable Trust",
    "contact": "minhaz.reza87@gmail.com",
    "year": "2026",
    "ages": "Ages 3–7",
    # Leave empty until KDP assigns one; the copyright page then omits the line.
    "isbn": "",
}

# ---------------------------------------------------------------------------
# VOWELS - স্বরবর্ণ (11)
# keys: letter, name_bn, name_en, sound, sign (vowel sign as used after a consonant),
#       example (ক + sign), word, translit, meaning, pic
# ---------------------------------------------------------------------------
VOWELS = [
    dict(letter="অ", name_bn="স্বরে অ", name_en="shore o", sound="‘o’ as in “on” — a short, open o",
         sign="", sign_note="No sign! অ hides inside every consonant: ক = ক্ + অ",
         word="অক্ষর", translit="okkhor", meaning="letter", pic="blocks"),
    dict(letter="আ", name_bn="স্বরে আ", name_en="shore aa", sound="‘aa’ as in “father”",
         sign="া", sign_name="আ-কার", example="কা", example_tr="kaa",
         word="আম", translit="aam", meaning="mango", pic="mango"),
    dict(letter="ই", name_bn="হ্রস্ব ই", name_en="rosho i", sound="‘i’ as in “sit” — short",
         sign="ি", sign_name="ই-কার", example="কি", example_tr="ki",
         word="ইফতার", translit="iftaar", meaning="the meal that breaks the fast", pic="iftar"),
    dict(letter="ঈ", name_bn="দীর্ঘ ঈ", name_en="dirgho ee", sound="‘ee’ as in “see” — long",
         sign="ী", sign_name="ঈ-কার", example="কী", example_tr="kee",
         word="ঈদ", translit="eed", meaning="Eid, the festival day", pic="eid"),
    dict(letter="উ", name_bn="হ্রস্ব উ", name_en="rosho u", sound="‘u’ as in “put” — short",
         sign="ু", sign_name="উ-কার", example="কু", example_tr="ku",
         word="উপহার", translit="upohaar", meaning="gift", pic="gift"),
    dict(letter="ঊ", name_bn="দীর্ঘ ঊ", name_en="dirgho oo", sound="‘oo’ as in “moon” — long",
         sign="ূ", sign_name="ঊ-কার", example="কূ", example_tr="koo",
         word="ঊর্মি", translit="oormi", meaning="wave", pic="waves"),
    dict(letter="ঋ", name_bn="ঋ", name_en="ri", sound="‘ri’ as in “ring”",
         sign="ৃ", sign_name="ঋ-কার", example="কৃ", example_tr="kri",
         word="ঋতু", translit="ritu", meaning="season (Bangladesh has six!)", pic="seasons"),
    dict(letter="এ", name_bn="এ", name_en="e", sound="‘e’ as in “egg”",
         sign="ে", sign_name="এ-কার", example="কে", example_tr="ke",
         word="এক", translit="ek", meaning="one", pic="one"),
    dict(letter="ঐ", name_bn="ঐ", name_en="oi", sound="‘oi’ as in “oil”",
         sign="ৈ", sign_name="ঐ-কার", example="কৈ", example_tr="koi",
         word="ঐ যে তারা", translit="oi je taaraa", meaning="look, there is a star!", pic="star"),
    dict(letter="ও", name_bn="ও", name_en="o", sound="‘o’ as in “go”",
         sign="ো", sign_name="ও-কার", example="কো", example_tr="ko",
         word="ওড়না", translit="orna", meaning="scarf", pic="scarf"),
    dict(letter="ঔ", name_bn="ঔ", name_en="ou", sound="‘ou’ — glide from o to u, as in “soul”",
         sign="ৌ", sign_name="ঔ-কার", example="কৌ", example_tr="kou",
         word="ঔষধ", translit="oushodh", meaning="medicine", pic="medicine"),
]

# ---------------------------------------------------------------------------
# CONSONANTS - ব্যঞ্জনবর্ণ (39)
# name_bn/name_en = the letter's name; say = how the letter is said; breakdown = native phonetic
# ---------------------------------------------------------------------------
def _c(letter, name_bn, name_en, sound, word, translit, meaning, pic, breakdown=None, pos=None):
    return dict(letter=letter, name_bn=name_bn, name_en=name_en, sound=sound, word=word,
                translit=translit, meaning=meaning, pic=pic,
                breakdown=breakdown or f"{letter}্ + অ = {letter}", pos=pos)

CONSONANTS = [
    _c("ক", "ক", "ko", "‘k’ as in “kite”", "কলা", "kolaa", "banana", "banana"),
    _c("খ", "খ", "kho", "‘k’ with a puff of air — say “k” strongly", "খেজুর", "khejur", "dates", "dates"),
    _c("গ", "গ", "go", "‘g’ as in “go”", "গাছ", "gaachh", "tree", "tree"),
    _c("ঘ", "ঘ", "gho", "‘g’ with a breath, as in “doghouse”", "ঘড়ি", "ghori", "clock", "clock"),
    _c("ঙ", "উঙ", "ungo", "‘ng’ as in “sing” — never at the start of a word", "আঙুর", "aangur", "grapes", "grapes", pos="middle"),
    _c("চ", "চ", "cho", "‘ch’ as in “chair”", "চশমা", "choshmaa", "glasses", "glasses"),
    _c("ছ", "ছ", "chho", "‘ch’ with a puff of air", "ছাতা", "chhaataa", "umbrella", "umbrella"),
    _c("জ", "বর্গীয় জ", "borgiyo jo", "‘j’ as in “jam”", "জাহাজ", "jaahaaj", "ship", "ship"),
    _c("ঝ", "ঝ", "jho", "‘j’ with a breath, as in “hedgehog”", "ঝুড়ি", "jhuri", "basket", "basket"),
    _c("ঞ", "ইঞ", "iyo", "a soft ‘n’ made near the roof of the mouth, as in “pinch”", "ইঞ্জিন", "injin", "engine", "engine", pos="middle"),
    _c("ট", "ট", "to", "a hard ‘t’ — curl your tongue back, as in “top”", "টমেটো", "tometo", "tomato", "tomato"),
    _c("ঠ", "ঠ", "tho", "a hard ‘t’ with a puff of air (not the ‘th’ of “the”)", "ঠেলাগাড়ি", "thelaagaari", "push-cart", "cart"),
    _c("ড", "ড", "do", "a hard ‘d’ — curl your tongue back, as in “dog”", "ডিম", "dim", "egg", "egg"),
    _c("ঢ", "ঢ", "dho", "a hard ‘d’ with a breath", "ঢাল", "dhaal", "shield", "shield"),
    _c("ণ", "মূর্ধন্য ণ", "murdhonno no", "‘n’ with the tongue curled back — today it sounds like ন", "লবণ", "lobon", "salt", "salt", pos="end"),
    _c("ত", "ত", "to", "a soft ‘t’ — tongue touches the back of the teeth", "তরমুজ", "tormuj", "watermelon", "watermelon"),
    _c("থ", "থ", "tho", "a soft ‘t’ with a puff of air (not the ‘th’ of “think”)", "থালা", "thaalaa", "plate", "plate"),
    _c("দ", "দ", "do", "a soft ‘d’ — tongue touches the back of the teeth", "দরজা", "dorjaa", "door", "door"),
    _c("ধ", "ধ", "dho", "a soft ‘d’ with a breath", "ধান", "dhaan", "rice plant (paddy)", "paddy"),
    _c("ন", "দন্ত্য ন", "donto no", "‘n’ as in “net”", "নৌকা", "noukaa", "boat", "boat"),
    _c("প", "প", "po", "‘p’ as in “pen”", "পতাকা", "potaakaa", "flag", "flag"),
    _c("ফ", "ফ", "pho", "‘p’ with a puff of air — close to ‘f’ in “fan”", "ফুল", "phul", "flower", "flower"),
    _c("ব", "ব", "bo", "‘b’ as in “ball”", "বই", "boi", "book", "book"),
    _c("ভ", "ভ", "bho", "‘b’ with a breath, as in “abhor”", "ভাত", "bhaat", "cooked rice", "rice"),
    _c("ম", "ম", "mo", "‘m’ as in “moon”", "মসজিদ", "moshjid", "mosque", "mosque"),
    _c("য", "অন্তঃস্থ য", "ontostho jo", "‘j’ as in “jam” — sounds just like জ", "যন্ত্র", "jontro", "tools", "tools"),
    _c("র", "র", "ro", "a tapped ‘r’ — flick the tongue once", "রংধনু", "rongdhonu", "rainbow", "rainbow"),
    _c("ল", "ল", "lo", "‘l’ as in “lamp”", "লাটিম", "laatim", "spinning top", "top"),
    _c("শ", "তালব্য শ", "taalobbo sho", "‘sh’ as in “shoe”", "শাপলা", "shaaplaa", "water lily", "lily"),
    _c("ষ", "মূর্ধন্য ষ", "murdhonno sho", "‘sh’ as in “shoe”, tongue curled back", "ষড়ভুজ", "shorobhuj", "hexagon", "hexagon"),
    _c("স", "দন্ত্য স", "donto sho", "usually ‘sh’; sometimes ‘s’ as in “sun”", "সূর্য", "shurjo", "sun", "sun"),
    _c("হ", "হ", "ho", "‘h’ as in “hat”", "হাঁড়ি", "haari", "clay pot", "pot"),
    _c("ড়", "ড-এ শূন্য ড়", "do-e shunno ro", "a quick flapped ‘r’ — never at the start of a word", "পাহাড়", "paahaar", "mountain", "mountain",
       breakdown="ড + dot = ড়", pos="end"),
    _c("ঢ়", "ঢ-এ শূন্য ঢ়", "dho-e shunno rho", "a flapped ‘r’ with a breath", "আষাঢ়", "aashaarh", "Asharh, the first month of the rainy season", "raincloud",
       breakdown="ঢ + dot = ঢ়", pos="end"),
    _c("য়", "অন্তঃস্থ অ", "ontostho o", "a gliding ‘y’ as in “yes”", "জায়নামাজ", "jaaynaamaaz", "prayer mat", "prayermat",
       breakdown="য + dot = য়", pos="middle"),
    _c("ৎ", "খণ্ড ত", "khondo to", "a short ‘t’ with no vowel after it", "বিদ্যুৎ", "biddut", "electricity", "bulb",
       breakdown="ত্ (no vowel) = ৎ", pos="end"),
    _c("ং", "অনুস্বার", "onushshaar", "‘ng’ at the end, as in “song”", "রং", "rong", "colour", "palette",
       breakdown="র + ং = রং", pos="end"),
    _c("ঃ", "বিসর্গ", "bishorgo", "a little breath; it often doubles the next sound", "প্রাতঃকাল", "praatokkaal", "early morning", "sunrise",
       breakdown="প্রাত + ঃ = প্রাতঃ", pos="middle"),
    _c("ঁ", "চন্দ্রবিন্দু", "chondrobindu", "makes the vowel nasal — hum it through your nose", "চাঁদ", "chaand", "moon", "moon",
       breakdown="চা + ঁ = চাঁ", pos="middle"),
]

DIGITS = [
    ("০", "শূন্য", "shunno", "zero"), ("১", "এক", "ek", "one"), ("২", "দুই", "dui", "two"),
    ("৩", "তিন", "tin", "three"), ("৪", "চার", "chaar", "four"), ("৫", "পাঁচ", "paanch", "five"),
    ("৬", "ছয়", "chhoy", "six"), ("৭", "সাত", "shaat", "seven"), ("৮", "আট", "aat", "eight"),
    ("৯", "নয়", "noy", "nine"),
]

PHRASES = [
    ("আসসালামু আলাইকুম", "aassaalaamu aalaaikum", "Peace be upon you (the Muslim greeting)"),
    ("ওয়ালাইকুমুস সালাম", "walaaikumus salaam", "And upon you be peace (the reply)"),
    ("আমার নাম …", "aamaar naam …", "My name is …"),
    ("ধন্যবাদ", "dhonnobaad", "Thank you"),
    ("জাযাকাল্লাহু খাইরান", "jaazaakallaahu khairan", "May Allah reward you with good"),
    ("মা · বাবা", "maa · baabaa", "Mother · Father"),
    ("ভাই · বোন", "bhaai · bon", "Brother · Sister"),
    ("হ্যাঁ · না", "hyaan · naa", "Yes · No"),
    ("আমি বাংলা শিখছি!", "aami baanglaa shikhchhi!", "I am learning Bengali!"),
]

# ---------------------------------------------------------------------------
# Qur'an quotations (simple Arabic script with full harakat).  ¹ = Quran.com on References page.
# MUST be checked by a qualified scholar / hafiz before publication.
# ---------------------------------------------------------------------------
AYAH_RAHMAN = dict(
    ref="Surah Ar-Raḥmān 55:1–4",
    ar="الرَّحْمَٰنُ ﴿١﴾ عَلَّمَ الْقُرْآنَ ﴿٢﴾ خَلَقَ الْإِنسَانَ ﴿٣﴾ عَلَّمَهُ الْبَيَانَ ﴿٤﴾",
    tr="Ar-Raḥmān. ʿAllamal-Qurʾān. Khalaqal-insān. ʿAllamahul-bayān.",
    en="The Most Merciful. He taught the Qur’an. He created the human being. He taught him clear expression (al-bayān).",
)
AYAH_RUM = dict(
    ref="Surah Ar-Rūm 30:22",
    ar="وَمِنْ آيَاتِهِ خَلْقُ السَّمَاوَاتِ وَالْأَرْضِ وَاخْتِلَافُ أَلْسِنَتِكُمْ وَأَلْوَانِكُمْ ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّلْعَالِمِينَ ﴿٢٢﴾",
    tr="Wa min āyātihī khalqus-samāwāti wal-arḍi wakh-tilāfu alsinatikum wa alwānikum. Inna fī dhālika la-āyātil-lil-ʿālimīn.",
    en="And among His signs is the creation of the heavens and the earth, and the variety of your languages and your colours. Surely in that are signs for those who know.",
)
AYAH_HUJURAT = dict(
    ref="Surah Al-Ḥujurāt 49:13 (part)",
    ar="وَجَعَلْنَاكُمْ شُعُوبًا وَقَبَائِلَ لِتَعَارَفُوا",
    tr="Wa jaʿalnākum shuʿūban wa qabāʾila li-taʿārafū.",
    en="…and We made you into peoples and tribes so that you may get to know one another.",
)
