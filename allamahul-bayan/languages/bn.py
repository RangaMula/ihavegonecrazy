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


# =============================================================================================
# Engine description of this book (used by ../build.py)
# =============================================================================================
from series import indic_consonant, indic_vowel

def _vowel_item(v):
    phon = indic_vowel(v["sign"], v.get("sign_name"), v.get("example"), v.get("example_tr"), "ক") or \
        f'<div style="font-size:11.5pt"><span class="nt">{v["sign_note"]}</span></div>'
    return dict(letter=v["letter"], name_native=v["name_bn"], name_en=v["name_en"], sound=v["sound"],
                phon_label="Bengali phonetics · vowel sign", phon=phon, word=v["word"], translit=v["translit"],
                meaning=v["meaning"], pic=v["pic"], pic_args=dict(blocks={}, one={}).get(v["pic"], {}))

def _cons_item(c):
    note = None
    if c.get("pos") == "middle":
        note = f'<span class="nt">{c["letter"]}</span> likes the middle of words — can you find it in <span class="nt">{c["word"]}</span>?'
    elif c.get("pos") == "end":
        note = f'Look for <span class="nt">{c["letter"]}</span> at the end of <span class="nt">{c["word"]}</span>!'
    return dict(letter=c["letter"], name_native=c["name_bn"], name_en=c["name_en"], sound=c["sound"],
                phon_label="Bengali phonetics · উচ্চারণ", phon=f'<div class="nt" style="font-size:19pt">{c["breakdown"]}</div>',
                note=note, word=c["word"], translit=c["translit"], meaning=c["meaning"], pic=c["pic"])

_vrows = "".join(f'<tr><td class="ntd" style="font-size:22pt">{v["letter"]}</td><td class="tr">{v["name_en"]}</td>'
                 f'<td class="nt" style="font-size:16pt">{("◌" + v["sign"]) if v["sign"] else "—"}</td>'
                 f'<td class="nt" style="font-size:16pt">{v.get("example", "ক")}</td><td class="tr">{v.get("example_tr", "ko")}</td></tr>'
                 for v in VOWELS)

LANG = dict(
    code="bn", folder="book-01-bengali", series_no=1, isbn=BOOK["isbn"],
    name="Bengali", native="বাংলা", native_tr="baanglaa", name_word="নাম", write_word="লেখো",
    title=BOOK["title"], title_native=BOOK["title_bn"], subtitle=BOOK["subtitle"],
    title_letters="অআইকখগ", belongs_native="এই বইটি যার", belongs_pic="lily",
    alphabet_native="বর্ণমালা", numbers_native="সংখ্যা", numbers_tr="shongkhaa", phrases_native="প্রথম কথা",
    fonts=[("Baloo Da 2", 400, "normal", "baloo-da-2-bengali-400-normal.woff2", None),
           ("Baloo Da 2", 700, "normal", "baloo-da-2-bengali-700-normal.woff2", None),
           ("Baloo Da 2", 800, "normal", "baloo-da-2-bengali-800-normal.woff2", None),
           ("Noto Sans Bengali", 400, "normal", "noto-sans-bengali-bengali-400-normal.woff2", None),
           ("Noto Sans Bengali", 700, "normal", "noto-sans-bengali-bengali-700-normal.woff2", None)],
    disp_family="Baloo Da 2", text_family="Noto Sans Bengali", glyph_font="baloo-da-2-bengali-800-normal.woff2",
    font_credit="Baloo Da 2, Noto Sans Bengali",
    series_line="<b>Book 1 is Bengali (Bangla)</b> — the language of Bangladesh, where this series was born. "
                "More languages will follow, in shā’ Allāh.",
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>o</b> is the short, open sound in “on”. Every Bengali consonant carries it: <span class='nt'>ক</span> = <i>ko</i>.",
        "<b>h after a letter</b> (<i>kh, gh, th, dh, bh</i>) means “add a puff of breath” — hold a tissue in front of your "
        "mouth and watch it move! It never means the English “th” of “the”.",
        "<b>Hard and soft t / d:</b> Bengali has two of each. For the <i>hard</i> ones (<span class='nt'>ট ঠ ড ঢ</span>) curl the "
        "tongue back; for the <i>soft</i> ones (<span class='nt'>ত থ দ ধ</span>) touch the back of your top teeth."],
    phon_explain="The box marked <i>Bengali phonetics</i> shows how the sound is built the way Bengali children learn it, "
                 "for example <span class='nt'>ক্ + অ = ক</span>.",
    standard="the standard spoken Bengali of Bangladesh and West Bengal",
    hello=[
        ("Who speaks it?", "About <b>270 million people</b> speak Bengali, also called <b>Bangla</b>. It is one of the ten most spoken languages in the world.<sup>³</sup>"),
        ("Where?", "It is the national language of <b>Bangladesh</b>. In <b>India</b> it is spoken in <b>West Bengal</b>, <b>Tripura</b> and the <b>Barak Valley of Assam</b>, and by families all over the world."),
        ("How is it written?", "In the <b>Bengali script</b>, from <b>left to right</b>, like English. Most letters hang from a line along the top called <span class='nt'>মাত্রা</span> <i>(maatraa)</i>."),
        ("How many letters?", "<b>50</b> letters: <b>11 vowels</b> (<span class='nt'>স্বরবর্ণ</span> <i>shorobornno</i>) and <b>39 consonants</b> (<span class='nt'>ব্যঞ্জনবর্ণ</span> <i>byanjonbornno</i>)."),
        ("A day for languages", "On <b>21 February 1952</b>, students in Dhaka stood up for the right to use Bengali. Today the whole world remembers them on <b>International Mother Language Day</b>.<sup>³</sup>"),
        ("Did you know?", "Bangladesh has <b>six seasons</b>, its national flower is the water lily <span class='nt'>শাপলা</span> <i>(shaaplaa)</i>, and it is home to one of the largest Muslim communities in the world."),
    ],
    hello_pics=[("lily", {}), ("boat", {}), ("flag", {})],
    chart_note="Read the alphabet left to right, row by row — the same order as in this book.",
    map=dict(
        frame=[[86.1, 20.7], [93.3, 26.9]], land=False, bold="Bangladesh",
        countries=["China", "Nepal", "Bhutan", "Myanmar", "India", "Bangladesh"],
        points=dict(dhaka=[90.41, 23.81], kolkata=[88.36, 22.57], agartala=[91.28, 23.83], silchar=[92.79, 24.83],
                    wb=[87.55, 23.35], bay=[89.6, 21.15], tripura=[91.75, 23.25], assam=[92.75, 25.35],
                    bd=[90.0, 24.55], india=[87.4, 25.5], myanmar=[92.75, 21.9], nepal=[87.1, 26.75], bhutan=[90.6, 26.95]),
        cities=[("dhaka", "Dhaka", 18, 8, "start", True), ("kolkata", "Kolkata", -14, 8, "end", False),
                ("agartala", "Agartala", 14, -10, "start", False), ("silchar", "Silchar", -12, -12, "end", False)],
        labels=[("bd", "BANGLADESH", 34, False), ("india", "INDIA", 34, False), ("myanmar", "MYANMAR", 24, False),
                ("nepal", "NEPAL", 22, False), ("bhutan", "BHUTAN", 22, False), ("bay", "Bay of Bengal", 34, True),
                ("wb", "WEST BENGAL", 20, False), ("tripura", "TRIPURA", 18, False), ("assam", "ASSAM", 18, False)],
        world_marker=[90.3, 23.7], world_caption="The circle shows Bangladesh on the world map.",
        legend="<b>Color it:</b> Bangladesh <b>green</b> · India <b>orange</b> · the sea <b>blue</b> · the other countries any colour you like. "
               "<b>Find it:</b> Dhaka ★ is the capital of Bangladesh. Bengali is also spoken around Kolkata (West Bengal), "
               "Agartala (Tripura) and Silchar (Assam) in India."),
    sections=[
        dict(key="vowels", label="VOWEL", chip="PART 1", title="The Vowels", native="স্বরবর্ণ", native_tr="shorobornno — “voice letters”",
             chart_title="vowels", chart_cols=6, warmup_title="the vowels", warmup_cols=4,
             intro_html=f"""<p>Vowels are the sounds you make with your mouth open: <i>o, aa, i, ee, u, oo…</i> Bengali has <b>11 vowels</b>.</p>
<p>A vowel has <b>two shapes</b>. At the start of a word it is written as a full letter (<span class="nt">আ</span>).
After a consonant it becomes a small <b>vowel sign</b> (<span class="nt">◌া</span>) that holds on to the consonant:
<span class="nt">ক + া = কা</span> <i>(kaa)</i>. Some signs even sit in front of the letter they belong to!</p>
<table style="width:100%;border-collapse:collapse;margin-top:0.1in;text-align:center" class="vt">
<tr style="font:600 10.5pt Fredoka"><th>Vowel</th><th>Name</th><th>Sign</th><th>With <span class="nt">ক</span></th><th>Say</th></tr>{_vrows}</table>
<style>.vt td,.vt th{{border-bottom:1.5px solid #bbb;padding:2px 4px}}</style>""",
             items=[_vowel_item(v) for v in VOWELS]),
        dict(key="consonants", label="CONSONANT", chip="PART 2", title="The Consonants", native="ব্যঞ্জনবর্ণ", native_tr="byanjonbornno",
             chart_title="consonants", chart_cols=7, warmup_title="the consonants", warmup_cols=6,
             intro_html="""<p>Consonants are the sounds made by stopping or squeezing the air: <i>k, g, ch, j, t, d, p, b…</i> Bengali has <b>39 consonants</b>.</p>
<div class="box" style="margin:0.12in 0"><h3>The hidden vowel</h3>Every consonant secretly carries the vowel <span class="nt">অ</span> <i>(o)</i>. That is why
<span class="nt">ক</span> is said <i>ko</i>, not just <i>k</i>. Bengali children learn it like this:
<div class="nt" style="font-size:22pt;text-align:center;margin-top:4px">ক্ + অ = ক</div>
<div style="text-align:center"><i>k + o = ko</i> — the little mark <span class="nt">্</span> (<i>hoshonto</i>) means “no vowel”.</div></div>
<div class="box" style="margin:0.12in 0"><h3>Families of five</h3>The first 25 consonants come in five families, each made in a different part of the mouth:
<div class="nt" style="font-size:17pt;line-height:1.6;margin-top:4px">ক খ গ ঘ ঙ — <span class="small" style="font-family:Nunito">back of the throat</span><br>
চ ছ জ ঝ ঞ — <span class="small" style="font-family:Nunito">middle of the tongue</span><br>ট ঠ ড ঢ ণ — <span class="small" style="font-family:Nunito">tongue curled back (hard)</span><br>
ত থ দ ধ ন — <span class="small" style="font-family:Nunito">tongue on the teeth (soft)</span><br>প ফ ব ভ ম — <span class="small" style="font-family:Nunito">the lips</span></div></div>
<div class="box"><h3>The puff test</h3>Hold a tissue in front of your mouth and say <span class="nt">ক</span> <i>(ko)</i>, then <span class="nt">খ</span>
<i>(kho)</i>. The tissue jumps for <span class="nt">খ</span>! An <i>h</i> in the sound guide means “add a puff”.</div>""",
             items=[_cons_item(c) for c in CONSONANTS]),
    ],
    digits=DIGITS, phrases=PHRASES,
    cheer=("মাশাআল্লাহ! খুব ভালো!", "maashaa-allaah! khub bhaalo!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); International Mother Language Day from <b>UNESCO</b>.",
    book_pic=dict(left="অ আ ই", right="ক খ গ"),
    cover=dict(title_html="My First Bengali<br>Alphabet", tiles="অআকখগম", pics=["mango", "lily", "boat", "mosque"],
               blurb="Bengali (Bangla) is spoken by about 270 million people in Bangladesh, India and all over the world. This big, "
                     "friendly coloring book introduces young children to all <b>50 letters</b> of the Bengali alphabet "
                     "<b>through English</b> — no Bengali needed at home.",
               bullets=["<b>Every letter on its own page</b> — a giant letter to color, its name in Bengali <i>and</i> English letters",
                        "<b>Easy English sound guides</b> plus Bengali phonetics (<span class='nt'>ক্ + অ = ক</span>)",
                        "<b>A word and picture for every letter</b> to color and say: <span class='nt'>আম</span> <i>aam</i> mango, <span class='nt'>নৌকা</span> <i>noukaa</i> boat…",
                        "<b>Pencil tracing rows</b> and warm-up pages for vowels and consonants",
                        "<b>Map to color</b>, Bengali numbers <span class='nt'>০–৯</span>, first phrases and a certificate",
                        "<b>Single-sided coloring pages</b> so markers never ruin the next picture"]),
    kdp=dict(market="Amazon.com (also Amazon.co.uk for UK Bengali families)",
             desc_intro="Bengali (Bangla) is spoken by about 270 million people in Bangladesh, India and all over the world. This big, friendly coloring book introduces young children to all <b>50 letters</b> of the Bengali alphabet <b>through English</b>, so no Bengali is needed at home.",
             desc_bullets=["<b>Every letter on its own page:</b> a giant letter to color, with its name written in Bengali <i>and</i> in English letters",
                           "<b>Easy English sound guides</b> plus simple Bengali phonetics (ক্ + অ = ক)",
                           "<b>A word and a picture for every letter</b> to color and say: আম <i>aam</i> (mango), নৌকা <i>noukaa</i> (boat), শাপলা <i>shaaplaa</i> (water lily)…",
                           "<b>Pencil tracing rows</b> on every page, plus warm-up pages for the vowels and consonants",
                           "<b>Meet the language:</b> where Bengali is spoken, a map to color, the whole alphabet on one page, the numbers ০–৯ and first friendly phrases"],
             categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                         "Children's Books › Education & Reference › Foreign Language Study",
                         "Children's Books › Religions › Islam"],
             keywords=["bangla alphabet book for kids", "learn bengali for children", "bangla letters tracing workbook",
                       "bengali language learning toddlers", "muslim kids activity book", "islamic coloring book for children",
                       "heritage language gift bangladesh"]),
)
