# -*- coding: utf-8 -*-
"""Book 24 - Dogri (Devanagari). Allamahul Bayan Series. REVIEW DRAFT: needs a native Dogri speaker.
Vocabulary is Dogri where the drafter knew a Dogri word (अंब mango, चन्न moon, फुल्ल flower, लूण salt, सेऊ apple,
मसीत mosque, त्रै three...), not Hindi."""
from indic import build, vowel as V, cons as C, fontset, COMMON_NOTES
from maps import south_asia_map


def _rare(t):
    return f"<b>Rare in Dogri:</b> {t}"


LANG = build(dict(
    code="doi", folder="book-24-dogri", series_no=24, isbn="", draft=True,
    name="Dogri", native="डोगरी", native_tr="ḍogree", name_word="नां", write_word="लिखो",
    title_native="मेरी पैह्ली डोगरी वर्णमाला", title_letters="अआइकखग", belongs_native="एह् कताब मेरी ऐ", belongs_pic="apple",
    alphabet_native="वर्णमाला", numbers_native="अंक", numbers_tr="ank", phrases_native="पैह्ले शब्द",
    fonts=fontset("Baloo 2", "baloo-2-devanagari", "Noto Sans Devanagari", "noto-sans-devanagari-devanagari"),
    disp_family="Baloo 2", text_family="Noto Sans Devanagari", glyph_font="baloo-2-devanagari-800-normal.woff2",
    font_credit="Baloo 2, Noto Sans Devanagari",
    base="क", base_tr="ka", virama="्", inherent="अ", inherent_tr="a",
    virama_note="<i>k + a = ka</i> — the little slanting mark <span class='nt'>्</span> (<i>halant</i>) means “no vowel”.",
    vowels_native="स्वर", vowels_tr="svar — “voice letters”", cons_native="व्यंजन", cons_tr="vyanjan",
    vowel_extra="<b>Rare in Dogri:</b> <span class='nt'>ऋ</span> and <span class='nt'>अः</span> appear only in a few words "
                "from Sanskrit, and few Dogri words start with <span class='nt'>ए</span> — Dogri even says "
                "<span class='nt'>इक</span> <i>ik</i> for one!",
    cons_extra=" That includes the flapped letters <span class='nt'>ड़ ढ़</span> and the joined letters <span class='nt'>क्ष त्र ज्ञ</span>.",
    cons_box="<div class='box'><h3>Dogri has tones!</h3>Like Punjabi, Dogri changes the <b>pitch</b> of the voice. The breathy "
             "letters <span class='nt'>घ झ ढ ध भ</span> are often said without the breath, with a change of pitch instead. "
             "<b>Rare letters:</b> <span class='nt'>ङ ञ ष क्ष ज्ञ</span> are found only in a few words from Sanskrit.</div>",
    families=[("क ख ग घ ङ", "back of the throat"), ("च छ ज झ ञ", "middle of the tongue"),
              ("ट ठ ड ढ ण", "tongue curled back (hard)"), ("त थ द ध न", "tongue on the teeth (soft)"), ("प फ ब भ म", "the lips")],
    vowels=[
        V("अ", "a", "a short ‘a’ as in “about”", "", "", "अखरोट", "akhroṭ", "walnut", "walnut"),
        V("आ", "aa", "‘aa’ as in “father”", "ा", "आकार", "आड़ू", "aaṛoo", "peach", "doi_peach"),
        V("इ", "i", "‘i’ as in “sit” — short", "ि", "इकार", "इट्ट", "iṭṭ", "brick", "brick"),
        V("ई", "ee", "‘ee’ as in “see” — long", "ी", "ईकार", "ईद", "eed", "Eid, the festival day", "eid"),
        V("उ", "u", "‘u’ as in “put” — short", "ु", "उकार", "उन्न", "unn", "wool", "wool"),
        V("ऊ", "oo", "‘oo’ as in “moon” — long", "ू", "ऊकार", "ऊखल", "ookhal", "mortar (for grinding)", "mortar"),
        V("ऋ", "ri", "‘ri’ as in “ring” — a rare letter", "ृ", "ऋकार", "ऋतु", "ritu", "season", "seasons",
          note=_rare("<span class='nt'>ऋ</span> is used only in a few words that come from Sanskrit.")),
        V("ए", "e", "‘e’ as in “they” (say “ay”)", "े", "एकार", "एलची", "elchee", "cardamom", "cardamom",
          note=_rare("few Dogri words start with <span class='nt'>ए</span>.")),
        V("ऐ", "ai", "‘ai’ — like the ‘a’ in “bat”, said long", "ै", "ऐकार", "ऐनक", "ainak", "glasses", "glasses"),
        V("ओ", "o", "‘o’ as in “go”", "ो", "ओकार", "ओले", "ole", "hailstones", "ice"),
        V("औ", "au", "‘au’ — like the ‘aw’ in “saw”", "ौ", "औकार", "औजार", "aujaar", "tools", "tools"),
        V("अं", "an", "a nasal ‘n’ or ‘m’ after the vowel", "ं", "अनुस्वार", "अंब", "amb", "mango", "mango", name="अं (अनुस्वार)"),
        V("अः", "ah", "a short breath ‘h’ after the vowel — a rare sign", "ः", "विसर्ग", "प्रातः", "praatah", "early morning",
          "sunrise", name="अः (विसर्ग)",
          note=_rare("the sign <span class='nt'>ः</span> appears only in a few learned words like this one.")),
    ],
    consonants=[
        C("क", "ka", "‘k’ as in “kite”", "कलम", "kalam", "pen", "pen"),
        C("ख", "kha", "‘k’ with a puff of air", "खिड़की", "khiṛkee", "window", "window"),
        C("ग", "ga", "‘g’ as in “go”", "गाजर", "gaajar", "carrot", "carrot"),
        C("घ", "gha", "‘g’ — often said with a low pitch instead of a breath", "घर", "ghar", "house, home", "house"),
        C("ङ", "nga", "‘ng’ as in “sing” — a rare letter", "रङ्ग", "rang", "colour", "palette",
          note="Today <span class='nt'>रङ्ग</span> is written <span class='nt'>रंग</span>, with a dot instead of <span class='nt'>ङ</span>."),
        C("च", "cha", "‘ch’ as in “chair”", "चन्न", "chann", "moon", "moon"),
        C("छ", "chha", "‘ch’ with a puff of air", "छत्तरी", "chhattaree", "umbrella", "umbrella"),
        C("ज", "ja", "‘j’ as in “jam”", "जहाज", "jahaaj", "ship", "ship"),
        C("झ", "jha", "‘j’ — often said with a low pitch instead of a breath", "झंडा", "jhanḍaa", "flag", "flag"),
        C("ञ", "nya", "a soft ‘n’ near the roof of the mouth — a rare letter", "अञ्जीर", "anjeer", "fig", "fig",
          note="Today <span class='nt'>अञ्जीर</span> is written <span class='nt'>अंजीर</span>."),
        C("ट", "ṭa", "a hard ‘t’ — curl your tongue back, as in “top”", "टोकरी", "ṭokree", "basket", "basket"),
        C("ठ", "ṭha", "a hard ‘t’ with a puff of air", "ठेला", "ṭhelaa", "push-cart", "cart"),
        C("ड", "ḍa", "a hard ‘d’ — curl your tongue back, as in “dog”", "डब्बा", "ḍabbaa", "box", "box"),
        C("ढ", "ḍha", "a hard ‘d’ — often said with a low pitch", "ढक्कन", "ḍhakkan", "lid", "jar"),
        C("ण", "ṇa", "‘n’ with the tongue curled back — never at the start of a word", "लूण", "looṇ", "salt", "salt",
          args=dict(label="लूण"), note="Look for <span class='nt'>ण</span> at the end of <span class='nt'>लूण</span>!"),
        C("त", "ta", "a soft ‘t’ — tongue touches the back of the teeth", "तारा", "taaraa", "star", "star"),
        C("थ", "tha", "a soft ‘t’ with a puff of air", "थाली", "thaalee", "plate", "plate"),
        C("द", "da", "a soft ‘d’ — tongue touches the back of the teeth", "दाड़ू", "daaṛoo", "wild pomegranate", "pomegranate"),
        C("ध", "dha", "a soft ‘d’ — often said with a low pitch", "धान", "dhaan", "rice plants (paddy)", "paddy"),
        C("न", "na", "‘n’ as in “net”", "नाशपाती", "naashpaatee", "pear", "pear"),
        C("प", "pa", "‘p’ as in “pen”", "पतंग", "patang", "kite", "kite"),
        C("फ", "pha", "‘p’ with a puff of air", "फुल्ल", "phull", "flower", "flower"),
        C("ब", "ba", "‘b’ as in “ball”", "बूहा", "boohaa", "door", "door"),
        C("भ", "bha", "‘b’ — often said with a low pitch instead of a breath", "भांडा", "bhaanḍaa", "pot, vessel", "pot"),
        C("म", "ma", "‘m’ as in “moon”", "मसीत", "maseet", "mosque", "mosque"),
        C("य", "ya", "‘y’ as in “yes”", "यंत्र", "yantra", "machine", "gears"),
        C("र", "ra", "a tapped ‘r’", "राजमाह", "raajmaah", "kidney beans", "doi_rajma"),
        C("ल", "la", "‘l’ as in “lamp”", "लट्टू", "laṭṭoo", "spinning top", "top"),
        C("व", "va", "between ‘v’ and ‘w’", "वरखा", "varkhaa", "rain", "raincloud"),
        C("श", "sha", "‘sh’ as in “shoe”", "शीशा", "sheeshaa", "mirror", "mirror"),
        C("ष", "sha", "‘sh’ with the tongue curled back — a rare letter", "षट्कोण", "shaṭkoṇ", "hexagon", "hexagon",
          note="<span class='nt'>ष</span> is found only in words that come from Sanskrit."),
        C("स", "sa", "‘s’ as in “sun”", "सेऊ", "seoo", "apple", "apple"),
        C("ह", "ha", "‘h’ as in “hat”", "हदवाना", "hadvaanaa", "watermelon", "watermelon"),
        C("ड़", "ṛa", "a quick flapped ‘r’ — never at the start of a word", "पहाड़", "pahaaṛ", "mountain", "mountain",
          phon="ड + ़ (dot) = ड़", note="Look for <span class='nt'>ड़</span> at the end of <span class='nt'>पहाड़</span>!"),
        C("ढ़", "ṛha", "a flapped ‘r’ — never at the start of a word", "सीढ़ी", "seeṛhee", "ladder", "ladder",
          phon="ढ + ़ (dot) = ढ़", note="Find <span class='nt'>ढ़</span> in the middle of <span class='nt'>सीढ़ी</span>!"),
        C("क्ष", "ksha", "‘k’ + ‘sh’ said together — a rare letter", "अक्षर", "akshar", "letter (of the alphabet)", "blocks",
          phon="क् + ष = क्ष", note="Find <span class='nt'>क्ष</span> in the middle of <span class='nt'>अक्षर</span>!",
          args=dict(letters=("अ", "आ", "क"))),
        C("त्र", "tra", "‘t’ + ‘r’ said together", "त्रै", "trai", "three", "one", phon="त् + र = त्र", args=dict(digit="३"),
          note="Dogri counts <span class='nt'>इक, दो, त्रै</span> — <i>ik, do, trai</i>!"),
        C("ज्ञ", "gya", "said ‘gya’ — a rare letter", "ज्ञान", "gyaan", "knowledge", "book", phon="ज् + ञ = ज्ञ",
          args=dict(left="अ आ इ", right="क ख ग")),
    ],
    sound_notes=COMMON_NOTES + [
        "<b>a</b> is the short sound in “about”. Every consonant carries it: <span class='nt'>क</span> = <i>ka</i>; at the end of a word it is usually silent.",
        "<b>Doubled consonants</b> (<span class='nt'>फुल्ल</span> <i>phull</i>, <span class='nt'>चन्न</span> <i>chann</i>) are held a little longer — "
        "a very Dogri sound.",
        "<b>A dot under t, d, n</b> (<i>ṭ, ḍ, ṇ</i>) means a <i>hard</i> sound with the tongue curled back; <i>ṛ</i> is a quick flap of the tongue."],
    standard="standard Dogri as spoken around Jammu",
    hello=[
        ("Who speaks it?", "About <b>2.6 million people</b> speak Dogri.<sup>³</sup>"),
        ("Where?", "In the hills and plains around the city of <b>Jammu</b> in the far north of India, and in nearby parts of "
                   "Himachal Pradesh and Punjab."),
        ("How is it written?", "Today in <b>Devanagari</b>, from <b>left to right</b>. Long ago it also had its own script, "
                               "<b>Dogra Akkhar</b>."),
        ("How many letters?", "This book teaches <b>51</b>: <b>13 vowels</b> (<span class='nt'>स्वर</span>) and <b>38 consonants</b> "
                              "(<span class='nt'>व्यंजन</span>), including <span class='nt'>ड़ ढ़</span> and <span class='nt'>क्ष त्र ज्ञ</span>."),
        ("Rare letters", "<span class='nt'>ऋ अः ङ ञ ष क्ष ज्ञ</span> live mostly in words from Sanskrit. The pages for them say so."),
        ("Did you know?", "Dogri has <b>tones</b>, like its cousin Punjabi. The Jammu hills grow walnuts, apples and kidney beans "
                          "(<span class='nt'>राजमाह</span>). In <b>2003</b> Dogri became one of India’s official languages.<sup>³</sup>"),
    ],
    hello_pics=[("walnut", {}), ("apple", {}), ("mountain", {})],
    map=south_asia_map(
        points=dict(jammu=[74.86, 32.73], kathua=[75.52, 32.37], udhampur=[75.14, 32.93], area=[75.1, 32.75], label=[79.5, 34.6]),
        area=(30, 20, -20), label="JAMMU",
        cities=[("jammu", "Jammu", -12, 10, "end", True)],
        marker=[75.0, 32.7], caption="The circle shows the Jammu region on the world map.",
        frame=[[63.5, 8.5], [92.5, 37.5]],
        legend="<b>Color it:</b> the Jammu region (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · the seas "
               "<b>blue</b>. Draw snowy mountains above it! <b>Find it:</b> Jammu ★ is the biggest Dogri-speaking city."),
    digits=[("०", "शून्य", "shoonya", "zero"), ("१", "इक", "ik", "one"), ("२", "दो", "do", "two"), ("३", "त्रै", "trai", "three"),
            ("४", "चार", "chaar", "four"), ("५", "पंज", "panj", "five"), ("६", "छे", "chhe", "six"), ("७", "सत्त", "satt", "seven"),
            ("८", "अट्ठ", "aṭṭh", "eight"), ("९", "नौ", "nau", "nine")],
    phrases=[("अस्सलामु अलैकुम", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("व अलैकुम अस्सलाम", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("मेरा नां … ऐ", "meraa naan … ai", "My name is …"),
             ("शुक्रिया · धन्नवाद", "shukriyaa · dhannvaad", "Thank you"),
             ("जज़ाकल्लाहु ख़ैरन", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("अम्मां · बापू", "ammaan · baapoo", "Mother · Father"),
             ("भ्रा · भैन", "bhraa · bhain", "Brother · Sister"),
             ("हां · नेईं", "haan · neeen", "Yes · No"),
             ("मैं डोगरी सिक्खा करदा आं!", "main ḍogree sikkhaa kardaa aan!", "I am learning Dogri! (a girl says: kardee aan)")],
    cheer=("माशाअल्लाह! बड़ा खरा!", "maashaa-allaah! baṛaa kharaa!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the Census of India 2011; the 2003 date from the "
                 "<b>Constitution of India</b> (92nd Amendment).",
    book_pic=dict(left="अ आ इ", right="क ख ग"),
    review_note="Drafted from general knowledge, not from a Dogri dictionary: every word, spelling and transliteration needs a "
                "Dogri speaker. Check first: आड़ू, इट्ट, उन्न, ऊखल, एलची (few Dogri words start with ए — is there a better one?), "
                "ओले, औजार, छत्तरी, दाड़ू, बूहा, भांडा, राजमाह, वरखा, हदवाना, लूण; whether Dogri writes पहाड़ or प्हाड़ and "
                "पैह्ली; the phrases मेरा नां … ऐ, धन्नवाद, अम्मां · बापू, भ्रा · भैन, नेईं, मैं डोगरी सिक्खा करदा आं; "
                "the title and एह् कताब मेरी ऐ; the numbers इक, त्रै, पंज, छे, सत्त, अट्ठ. Dogri tone marks are not shown.",
    tiles="अआकखगम", cover_pics=["walnut", "apple", "kite", "mosque"], title_size=50,
    speakers_blurb="Dogri is the language of Jammu and its green hills, spoken by about 2.6 million people.",
    sample_words=[("अंब", "amb", "mango"), ("चन्न", "chann", "moon"), ("सेऊ", "seoo", "apple")],
    keywords=["dogri alphabet book for kids", "learn dogri for children", "dogri letters tracing",
              "jammu heritage workbook", "muslim kids activity book", "islamic coloring book for children",
              "dogri heritage language gift"],
))
