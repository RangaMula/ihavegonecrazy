# -*- coding: utf-8 -*-
"""Book 16 - Pashto (Perso-Arabic script, Naskh style, 44 letters). Allamahul Bayan Series.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
REVIEW DRAFT: words, letter names and transliterations need a native Pashto speaker.
"""
from indic import fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms


def forms(letter, joins=True, only_final=False):
    if only_final:
        f = f'<span class="ntd">{JOIN}{letter}</span>'
        return f'<div style="font-size:12pt">At the end of a word: <span style="font-size:24pt">{f}</span></div>'
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">{letter}</span> · '
                f'after a letter <span class="ntd" style="font-size:24pt">{JOIN}{letter}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def nt(t):
    return f'<span class="nt">{t}</span>'


def S(letter, name, name_tr, sound, word, tr, meaning, pic, joins=True, note=None, args=None, extra=None, only_final=False):
    phon = forms(letter, joins, only_final) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return dict(letter=letter, name_native=name, name_en=name_tr, sound=sound,
                phon_label="Letter shapes · how it joins", phon=phon, note=note,
                word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {})


SAME = "Sounds the same as {}; it is used mostly in words from Arabic."
RING = "The little ring under it means the tongue curls back."

LETTERS = [
    S("ا", "الف", "alif", "‘a’, or a long ‘aa’ as in “father” inside a word", "انار", "anaar", "pomegranate", "pomegranate", joins=False),
    S("ب", "بې", "be", "‘b’ as in “ball”", "بالښت", "baalisht", "pillow", "pillow", extra="One dot below."),
    S("پ", "پې", "pe", "‘p’ as in “pen”", "پياز", "pyaaz", "onion", "onion", extra="Three dots below."),
    S("ت", "تې", "te", "a soft ‘t’ — tongue touches the back of the teeth", "توت", "toot", "mulberry", "ps_mulberry",
      extra="Two dots above."),
    S("ټ", "ټې", "ṭe", "a hard ‘t’ — curl your tongue back, as in “top”", "ټماټر", "ṭamaaṭar", "tomato", "tomato", extra=RING),
    S("ث", "ثې", "se", "‘s’ as in “sun”", "ثمر", "samar", "fruit", "basket", extra=SAME.format(nt("س"))),
    S("ج", "جيم", "jeem", "‘j’ as in “jam”", "جومات", "jumaat", "mosque", "mosque"),
    S("چ", "چې", "che", "‘ch’ as in “chair”", "چتر", "chatr", "umbrella", "umbrella"),
    S("ح", "حې", "he", "‘h’ as in “hat”", "حج", "hajj", "Hajj, the journey to the Kaaba in Makkah", "kaaba"),
    S("خ", "خې", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خرما", "khurmaa", "dates", "dates"),
    S("څ", "څې", "tse", "‘ts’ as in “cats”", "څاه", "tsaah", "well (for water)", "well", extra="Three dots above."),
    S("ځ", "ځې", "dze", "‘dz’ as in “kids” (some people say ‘z’)", "ځمکه", "dzmaka", "the Earth", "globe", extra="A little hamza on top."),
    S("د", "دال", "daal", "a soft ‘d’ — tongue touches the back of the teeth", "دروازه", "darwaaza", "door", "door", joins=False),
    S("ډ", "ډال", "ḍaal", "a hard ‘d’ — curl your tongue back, as in “dog”", "ډوډۍ", "ḍoḍay", "bread", "roti", joins=False, extra=RING),
    S("ذ", "ذال", "zaal", "‘z’ as in “zoo”", "ذکر", "zikr", "dhikr — remembering Allah", "tasbih", joins=False,
      extra=SAME.format(nt("ز"))),
    S("ر", "رې", "re", "a tapped ‘r’ — flick the tongue once", "رنګ", "rang", "colour", "palette", joins=False),
    S("ړ", "ړې", "ṛe", "a flapped ‘r’ with the tongue curled back — it never starts a word",
      "ګړۍ", "gaṛay", "clock, watch", "clock", joins=False, note=f'Find {nt("ړ")} in the middle of {nt("ګړۍ")}!'),
    S("ز", "زې", "ze", "‘z’ as in “zoo”", "زيتون", "zaytoon", "olive", "olive", joins=False),
    S("ژ", "ژې", "zhe", "‘zh’ like the ‘s’ in “measure”", "ژاله", "zhaala", "hail", "raincloud", joins=False),
    S("ږ", "ږې", "ẓe", "in the south a curled-back ‘zh’; in the north-east a ‘g’", "ږمنځ", "zhmandz (gmanz)", "comb", "ps_comb",
      joins=False, extra="One dot above and one dot below."),
    S("س", "سين", "seen", "‘s’ as in “sun”", "ستوری", "storay", "star", "star"),
    S("ش", "شين", "sheen", "‘sh’ as in “shoe”", "شات", "shaat", "honey", "honey"),
    S("ښ", "ښين", "ṣheen", "in the south a curled-back ‘sh’; in the north-east a ‘kh’", "ښيښه", "shisha (khikha)", "mirror, glass",
      "mirror", extra="One dot above and one dot below."),
    S("ص", "صاد", "swaad", "‘s’ as in “sun”", "صابون", "saaboon", "soap", "soap", extra=SAME.format(nt("س"))),
    S("ض", "ضاد", "zwaad", "‘z’ as in “zoo”", "ضيا", "ziyaa", "light", "bulb", extra=SAME.format(nt("ز"))),
    S("ط", "طوی", "toy", "a soft ‘t’, like ت", "طياره", "tayyaara", "aeroplane", "plane", extra=SAME.format(nt("ت"))),
    S("ظ", "ظوی", "zoy", "‘z’ as in “zoo”", "ظرف", "zarf", "container, jar", "jar", extra=SAME.format(nt("ز"))),
    S("ع", "عين", "ayn", "in Pashto, just the vowel next to it — in Arabic, a sound from deep in the throat", "عينکې", "aynake",
      "glasses", "glasses"),
    S("غ", "غين", "ghayn", "a soft gargled ‘gh’ from the back of the throat", "غر", "ghar", "mountain", "mountain"),
    S("ف", "فې", "fe", "‘f’ as in “fan”", "فانوس", "faanoos", "lantern", "eid"),
    S("ق", "قاف", "qaaf", "a ‘k’ said far back in the throat", "قلم", "qalam", "pen", "pen"),
    S("ک", "کاف", "kaaf", "‘k’ as in “kite”", "کور", "kor", "house, home", "house"),
    S("ګ", "ګاف", "gaaf", "‘g’ as in “go”", "ګل", "gul", "flower", "flower", extra="A little ring under it."),
    S("ل", "لام", "laam", "‘l’ as in “lamp”", "لمر", "lmar", "sun", "sun"),
    S("م", "ميم", "meem", "‘m’ as in “moon”", "مڼه", "maṇa", "apple", "apple"),
    S("ن", "نون", "noon", "‘n’ as in “net”", "ناک", "naak", "pear", "pear"),
    S("ڼ", "ڼون", "ṇoon", "a hard ‘n’ with the tongue curled back — it never starts a word", "پاڼه", "paaṇa", "leaf", "ps_leaf",
      note=f'Find {nt("ڼ")} in the middle of {nt("پاڼه")}!', extra=RING),
    S("و", "واو", "waaw", "‘w’ as in “water”, or the long vowels ‘oo’ and ‘o’", "ونه", "wana", "tree", "tree", joins=False),
    S("ه", "هې", "he", "‘h’ as in “hat”; at the end of a word it often says ‘a’", "هندواڼه", "hindwaaṇa", "watermelon", "watermelon"),
    S("ي", "معروفه يې", "maaroofa ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "يخ", "yakh", "ice", "ice",
      extra="Two dots below, even at the end of a word."),
    S("ې", "مجهوله يې", "majhoola ye", "‘e’ as in “they”", "کېله", "kela", "banana", "banana",
      note=f'Find {nt("ې")} in the middle of {nt("کېله")}!', extra="Two dots below, one over the other."),
    S("ی", "نرمه يې", "narma ye", "‘ay’ at the end of a word, as in “day”", "منګی", "mangay", "clay water jug", "pot",
      only_final=True, note=f'Look for {nt("ی")} at the end of {nt("منګی")}!', extra="No dots at the end of a word. Inside a word it looks just like <span class='nt'>يـ</span>."),
    S("ۍ", "ښځينه يې", "shadzeena ye", "‘ay’ at the end of a word, in words for girls and things called “she”", "کړۍ", "kaṛay",
      "ring", "ring", only_final=True, note=f'Look for {nt("ۍ")} at the end of {nt("کړۍ")}!', extra="It has a little tail, and it only comes at the end of a word."),
    S("ئ", "فعلي يې", "feli ye", "‘ay’ at the end of action words; inside a word, a little break in the voice", "دائره", "daa’ira",
      "circle", "ps_circle", note=f'Find {nt("ئ")} in the middle of {nt("دائره")}!', extra="A little hamza on top."),
]

FONTS = fontset("Noto Sans Arabic", "noto-sans-arabic-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic")

MAP = region_map(frame=[[58.5, 23.0], [75.5, 40.0]],
                 points=dict(kabul=[69.17, 34.53], kandahar=[65.71, 31.61], peshawar=[71.58, 34.01], quetta=[67.0, 30.18]),
                 area=(68.6, 32.6, 300, 165), area_rot=-32,
                 cities=[("kabul", "Kabul", -14, -12, "end", True), ("kandahar", "Kandahar", -14, 8, "end", False),
                         ("peshawar", "Peshawar", 14, 8, "start", False), ("quetta", "Quetta", 14, 8, "start", False)],
                 label="AFGHANISTAN", label_at=[64.5, 35.6], marker=[68.5, 32.5],
                 caption="The circle shows Afghanistan and Pakistan on the world map.",
                 legend="<b>Color it:</b> the area inside the dashed line <b>yellow</b> · the rest of the land <b>green</b> · the sea "
                        "<b>blue</b>. <b>Find it:</b> Kabul ★ is the capital of Afghanistan. Pashto is spoken in Kabul and Kandahar, "
                        "and in Peshawar and Quetta in Pakistan. Draw the high mountains with snowy tops!",
                 seas=[("Arabian Sea", 63.5, 24.2)])
MAP["points"]["pk"] = [70.6, 27.4]
MAP["labels"].append(("pk", "PAKISTAN", 32, False))

LANG = dict(
    code="ps", folder="book-16-pashto", series_no=16, isbn="", dir="rtl", draft=True,
    name="Pashto", native="پښتو", native_tr="pashto", name_word="نوم", write_word="وليکئ",
    title="My First Pashto Alphabet", title_native="زما لومړنی پښتو کتاب",
    subtitle="A Coloring Book to Learn, Trace & Say the 44 Pashto Letters with English Phonetics",
    title_letters="ابپتټث", belongs_native="دا کتاب زما دی", belongs_pic="pen",
    alphabet_native="الفبا", numbers_native="شمېرې", numbers_tr="shmere", phrases_native="لومړني ټکي",
    fonts=FONTS, disp_family="Noto Sans Arabic", text_family="Noto Naskh Arabic",
    glyph_font=["noto-sans-arabic-arabic-800-normal.woff2", "noto-naskh-arabic-arabic-700-normal.woff2"],
    font_credit="Noto Sans Arabic, Noto Naskh Arabic",
    extra_css=".nt{line-height:1.9} .lp-name{font-size:20pt;line-height:1.9} .lp-word .w{font-size:38pt;line-height:1.6} .tr.small[style*='8.5pt']{font-size:7.2pt!important}",
    series_line="<b>Book 16 is Pashto</b> — the language of the mountains and valleys of Afghanistan and north-west Pakistan. "
                "More languages of the region are in the series, in shā’ Allāh.",
    sound_notes=[
        "<b>Pashto is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. A short "
        "<i>a</i> in Pashto is often a quick, light ‘uh’ sound (as in “about”).",
        "<b>A dot under t, d, r, n</b> (<i>ṭ, ḍ, ṛ, ṇ</i>) means a <i>hard</i> sound with the tongue curled back. In Pashto "
        "these letters wear a <b>little ring</b>: <span class='nt'>ټ ډ ړ ڼ</span>.",
        "<b>Two ways to speak:</b> in the south (around Kandahar) <span class='nt'>ښ</span> and <span class='nt'>ږ</span> sound "
        "like a curled-back <i>sh</i> and <i>zh</i>; in the north-east (around Peshawar) they sound like <i>kh</i> and <i>g</i>. "
        "Both are right! This book shows the southern sound first and the other one in brackets.",
        "<b>Pashto has five letters for ‘y’ and ‘e’ sounds</b> (<span class='nt'>ي ې ی ۍ ئ</span>). Most of them live at the "
        "end of words, so look carefully at the last letter!",
        "<b>Some letters sound the same</b> (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ض ظ</span> all say "
        "<i>z</i>). They keep their Arabic spelling, which helps when children later read the Qur’an."],
    phon_explain="Because Pashto letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="standard written Pashto as used in Afghanistan and Pakistan",
    hello=[
        ("Who speaks it?", "More than <b>40 million people</b> speak Pashto.<sup>³</sup>"),
        ("Where?", "Pashto is one of the main languages of <b>Afghanistan</b>, and it is spoken by millions of people in north-west "
                   "<b>Pakistan</b>, in cities such as Peshawar and Quetta. Pashto-speaking families live all over the world."),
        ("How is it written?", "From <b>right to left</b>, in a Perso-Arabic script, in the clear upright style called <b>Naskh</b>. "
                               "Most letters <b>join</b> to the next one and change shape."),
        ("How many letters?", "This book teaches <b>44 letters</b>. Pashto adds its own letters to the Arabic ones, such as "
                              "<span class='nt'>ټ ډ ړ ڼ څ ځ ږ ښ ګ</span>."),
        ("Rings and dots", "Look for the <b>little rings</b> under <span class='nt'>ټ ډ ړ ڼ ګ</span> and the extra dots on "
                           "<span class='nt'>څ ږ ښ</span>. They tell you the special Pashto sounds."),
        ("A friend of the Qur’an", "Many Pashto words come from Arabic: <span class='nt'>قلم</span> <i>qalam</i> (pen), "
                                    "<span class='nt'>کتاب</span> <i>kitaab</i> (book), <span class='nt'>صبر</span> <i>sabr</i> (patience)."),
    ],
    hello_pics=[("mountain", {}), ("pomegranate", {}), ("mosque", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=MAP,
    sections=[
        dict(key="letters", label="LETTER", chip="THE LETTERS", title="The Pashto Letters", native="الفبا",
             native_tr="alifbaa — “the a-b-c”", chart_title="letters", chart_cols=8,
             warmup_title="the letters", warmup_cols=7,
             intro_html="""<p>Pashto is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Most Pashto letters <b>join</b> to the letter after them, and their shape changes
a little at the start, middle and end of a word. Each letter page shows all three shapes.
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ق + ل + م = <span class="nt">قلم</span></div>
<div style="text-align:center"><i>q + l + m = qalam</i> (pen)</div></div>
<div class="box" style="margin:0.1in 0"><h3>Rings make hard sounds</h3>A little ring changes a letter:
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ت ← ټ &nbsp;&nbsp; د ← ډ &nbsp;&nbsp; ر ← ړ &nbsp;&nbsp; ن ← ڼ</div>
<div style="text-align:center">from the right: t → ṭ · d → ḍ · r → ṛ · n → ṇ</div></div>
<div class="box"><h3>Eleven letters never join forward</h3><span class="nt" style="font-size:16pt">ا د ډ ذ ر ړ ز ژ ږ و ۍ</span> join to the letter
<i>before</i> them, but never to the one after. Look for the small note on their pages.</div>""",
             items=LETTERS),
    ],
    digits=[("۰", "صفر", "sifr", "zero"), ("۱", "يو", "yaw", "one"), ("۲", "دوه", "dwa", "two"), ("۳", "درې", "dre", "three"),
            ("۴", "څلور", "tsalor", "four"), ("۵", "پنځه", "pindza", "five"), ("۶", "شپږ", "shpazh", "six"), ("۷", "اووه", "owa", "seven"),
            ("۸", "اته", "ata", "eight"), ("۹", "نهه", "naha", "nine")],
    phrases=[("السلام عليکم", "assalaamu alaykum", "Peace be upon you (the Muslim greeting)"),
             ("وعليکم السلام", "wa alaykum assalaam", "And upon you be peace (the reply)"),
             ("زما نوم … دی", "zmaa noom … day", "My name is …"),
             ("مننه", "manana", "Thank you"),
             ("جزاک الله خيراً", "jazaakallaahu khayran", "May Allah reward you with good"),
             ("مور · پلار", "mor · plaar", "Mother · Father"),
             ("ورور · خور", "wror · khor", "Brother · Sister"),
             ("هو · نه", "ho · na", "Yes · No"),
             ("زه پښتو زده کوم!", "za pashto zda kawam!", "I am learning Pashto!")],
    cheer=("ماشاءالله! شاباس!", "maashaa-allaah! shaabaas!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="ا ب پ", right="ت ټ ث"),
    review_note=("Draft for native review. Check: the 44-letter list and order (five ye letters ي ې ی ۍ ئ); the letter names, "
                 "especially the ye names (معروفه، مجهوله، نرمه، ښځينه، فعلي يې) and طوی/ظوی; the words توت (mulberry), بالښت, "
                 "ږمنځ (comb), ښيښه, ضيا (light, for ض), طياره, ژاله (hail), ناک (pear), منګی (clay jug), کړۍ (ring), دائره (circle, "
                 "for ئ); the southern/north-eastern readings of ښ and ږ; the number words; and every transliteration."),
    cover=dict(title_html="My First Pashto<br>Alphabet", tiles="ابټډښګ", pics=["pomegranate", "mountain", "flower", "mosque"],
               blurb="Pashto is spoken by more than 40 million people in Afghanistan, Pakistan and around the world. This big, friendly "
                     "coloring book introduces young children to all <b>44 letters</b> of the Pashto alphabet <b>through English</b> — "
                     "no Pashto needed at home.",
               bullets=["<b>Every letter on its own page</b> — a giant letter to color, its name in Pashto <i>and</i> English letters",
                        "<b>Easy English sound guides</b> and the letter’s <b>joined shapes</b> (start · middle · end)",
                        "<b>A word and picture for every letter</b>: <span class='nt'>انار</span> <i>anaar</i> pomegranate, "
                        "<span class='nt'>جومات</span> <i>jumaat</i> mosque…",
                        "<b>Right-to-left tracing rows</b> and a warm-up page — great practice for reading the Qur’an",
                        "<b>Map to color</b>, Pashto numbers <span class='nt'>۰–۹</span>, first phrases and a certificate",
                        "<b>Single-sided coloring pages</b> so markers never ruin the next picture"]),
    kdp=dict(market="Amazon.com (also Amazon.co.uk and Amazon.ca)",
             desc_intro="Pashto is spoken by more than 40 million people in Afghanistan, Pakistan and around the world. This big, friendly "
                        "coloring book introduces young children to all <b>44 letters</b> of the Pashto alphabet <b>through English</b>, "
                        "so no Pashto is needed at home.",
             desc_bullets=["<b>Every letter on its own page:</b> a giant letter to color, with its name written in Pashto <i>and</i> in English letters",
                           "<b>Easy English sound guides</b>, plus the letter’s joined shapes at the start, middle and end of a word",
                           "<b>A word and a picture for every letter</b> to color and say: انار <i>anaar</i> (pomegranate), جومات <i>jumaat</i> (mosque), لمر <i>lmar</i> (sun)…",
                           "<b>Right-to-left pencil tracing rows</b> on every page — a gentle first step towards reading the Qur’an",
                           "<b>Meet the language:</b> where Pashto is spoken, a map to color, the whole alphabet on one page, the numbers ۰–۹ and first friendly phrases"],
             categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                         "Children's Books › Education & Reference › Foreign Language Study",
                         "Children's Books › Religions › Islam"],
             keywords=["pashto alphabet book for kids", "learn pashto for children", "pashto letters tracing workbook",
                       "pashto alifba coloring", "muslim kids activity book", "islamic coloring book for children",
                       "afghan heritage language gift"]),
)
