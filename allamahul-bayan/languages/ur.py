# -*- coding: utf-8 -*-
"""Book 3 - Urdu (Perso-Arabic script, Nastaliq style). Allamahul Bayan Series.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
"""

JOIN = "ـ"  # tatweel, used to show joined forms

def forms(letter, joins=True, only_final=False):
    if only_final:
        f = f'<span class="ntd">{JOIN}{letter}</span>'
        return (f'<div style="font-size:12pt">Joined to the letter before: <span style="font-size:24pt">{f}</span></div>')
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">{letter}</span> · '
                f'after a letter <span class="ntd" style="font-size:24pt">{JOIN}{letter}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')

def U(letter, name, name_tr, sound, word, tr, meaning, pic, joins=True, note=None, args=None, only_final=False, extra=None):
    phon = forms(letter, joins, only_final) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return dict(letter=letter, name_native=name, name_en=name_tr, sound=sound,
                phon_label="Letter shapes · how it joins", phon=phon, note=note,
                word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {})

S_SAME = "Sounds the same as {}; it is used mostly in words from Arabic."

LETTERS = [
    U("ا", "الف", "alif", "‘a’ or ‘aa’ — a long ‘aa’ as in “father” inside a word", "انار", "anaar", "pomegranate", "pomegranate", joins=False),
    U("ب", "بے", "be", "‘b’ as in “ball”", "بادل", "baadal", "clouds", "clouds", extra="One dot below."),
    U("پ", "پے", "pe", "‘p’ as in “pen”", "پتنگ", "patang", "kite", "kite", extra="Three dots below."),
    U("ت", "تے", "te", "a soft ‘t’ — tongue touches the back of the teeth", "تربوز", "tarbooz", "watermelon", "watermelon", extra="Two dots above."),
    U("ٹ", "ٹے", "ṭe", "a hard ‘t’ — curl your tongue back, as in “top”", "ٹماٹر", "ṭamaaṭar", "tomato", "tomato", extra="A little ‘ṭ’ sign on top."),
    U("ث", "ثے", "se", "‘s’ as in “sun”", "ثمر", "samar", "fruit", "basket", extra=S_SAME.format("س")),
    U("ج", "جیم", "jeem", "‘j’ as in “jam”", "جہاز", "jahaaz", "ship", "ship"),
    U("چ", "چے", "che", "‘ch’ as in “chair”", "چاند", "chaand", "moon", "moon"),
    U("ح", "بڑی حے", "baṛi he", "‘h’ as in “hat”", "حج", "hajj", "Hajj, the journey to the Kaaba in Makkah", "kaaba",
      extra="Its name means “big he”."),
    U("خ", "خے", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خط", "khat", "letter (that you post)", "envelope"),
    U("د", "دال", "daal", "a soft ‘d’ — tongue touches the back of the teeth", "دروازہ", "darvaaza", "door", "door", joins=False),
    U("ڈ", "ڈال", "ḍaal", "a hard ‘d’ — curl your tongue back, as in “dog”", "ڈبہ", "ḍabba", "box", "box", joins=False),
    U("ذ", "ذال", "zaal", "‘z’ as in “zoo”", "ذکر", "zikr", "dhikr — remembering Allah", "tasbih", joins=False,
      extra=S_SAME.format("ز")),
    U("ر", "رے", "re", "a tapped ‘r’ — flick the tongue once", "روٹی", "roṭi", "flatbread (roti)", "roti", joins=False),
    U("ڑ", "ڑے", "ṛe", "a flapped ‘r’ with the tongue curled back — never at the start of a word", "پہاڑ", "pahaaṛ", "mountain", "mountain",
      joins=False, note='Look for <span class="nt">ڑ</span> at the end of <span class="nt">پہاڑ</span>!'),
    U("ز", "زے", "ze", "‘z’ as in “zoo”", "زمین", "zameen", "the Earth", "globe", joins=False),
    U("ژ", "ژے", "zhe", "‘zh’ like the ‘s’ in “measure” — a rare letter", "ژالہ", "zhaala", "hail", "raincloud", joins=False),
    U("س", "سین", "seen", "‘s’ as in “sun”", "سورج", "sooraj", "sun", "sun"),
    U("ش", "شین", "sheen", "‘sh’ as in “shoe”", "شہد", "shahad", "honey", "honey"),
    U("ص", "صاد", "su’aad", "‘s’ as in “sun”", "صابن", "saabun", "soap", "soap", extra=S_SAME.format("س")),
    U("ض", "ضاد", "zu’aad", "‘z’ as in “zoo”", "ضیا", "ziya", "light", "bulb", extra=S_SAME.format("ز")),
    U("ط", "طوئے", "to’e", "a soft ‘t’, like ت", "طشتری", "tashtari", "saucer, small plate", "plate", extra=S_SAME.format("ت")),
    U("ظ", "ظوئے", "zo’e", "‘z’ as in “zoo”", "ظرف", "zarf", "container, jar", "jar", extra=S_SAME.format("ز")),
    U("ع", "عین", "ain", "in Urdu, just the vowel next to it — in Arabic, a sound from deep in the throat", "عینک", "ainak", "glasses", "glasses"),
    U("غ", "غین", "ghain", "a soft gargled ‘gh’ from the back of the throat", "غبارہ", "ghubaara", "balloon", "balloon"),
    U("ف", "فے", "fe", "‘f’ as in “fan”", "فانوس", "faanoos", "lantern", "eid"),
    U("ق", "قاف", "qaaf", "a ‘k’ said far back in the throat", "قلم", "qalam", "pen", "pen"),
    U("ک", "کاف", "kaaf", "‘k’ as in “kite”", "کیلا", "kela", "banana", "banana"),
    U("گ", "گاف", "gaaf", "‘g’ as in “go”", "گاجر", "gaajar", "carrot", "carrot"),
    U("ل", "لام", "laam", "‘l’ as in “lamp”", "لٹو", "laṭṭoo", "spinning top", "top"),
    U("م", "میم", "meem", "‘m’ as in “moon”", "مسجد", "masjid", "mosque", "mosque"),
    U("ن", "نون", "noon", "‘n’ as in “net”", "نمک", "namak", "salt", "salt", args=dict(label="نمک")),
    U("و", "واؤ", "vaa’o", "‘v’ as in “van”, or the long vowels ‘oo’ and ‘o’", "وضو", "wuzu", "wudu — washing before prayer", "ewer", joins=False),
    U("ہ", "چھوٹی ہے", "chhoṭi he", "‘h’ as in “hat”", "ہانڈی", "haanḍi", "clay pot", "pot", extra="Its name means “little he”."),
    U("ھ", "دو چشمی ہے", "do-chashmi he", "adds a puff of breath to the letter before it: پ + ھ = پھ ‘ph’", "پھول", "phool", "flower", "flower",
      note='Find <span class="nt">ھ</span> in <span class="nt">پھول</span> — it never starts a word.', extra="Its name means “two-eyed he”."),
    U("ء", "ہمزہ", "hamza", "a tiny break in the voice between two vowels", "چائے", "chaa’e", "tea", "teacup", joins=False,
      note='Find the <span class="nt">ء</span> sitting on its seat in <span class="nt">چائے</span>.'),
    U("ی", "چھوٹی یے", "chhoṭi ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "یخ", "yakh", "ice", "ice", extra="Its name means “little ye”."),
    U("ے", "بڑی یے", "baṛi ye", "‘e’ as in “they” — only at the end of a word", "انڈے", "anḍe", "eggs", "egg", only_final=True,
      note='Look for <span class="nt">ے</span> at the end of <span class="nt">انڈے</span>!'),
]

FONTS = [("Baloo Bhaijaan 2", 400, "normal", "baloo-bhaijaan-2-arabic-400-normal.woff2", None),
         ("Baloo Bhaijaan 2", 700, "normal", "baloo-bhaijaan-2-arabic-700-normal.woff2", None),
         ("Baloo Bhaijaan 2", 800, "normal", "baloo-bhaijaan-2-arabic-800-normal.woff2", None),
         ("Noto Nastaliq Urdu", 400, "normal", "noto-nastaliq-urdu-arabic-400-normal.woff2", None),
         ("Noto Nastaliq Urdu", 700, "normal", "noto-nastaliq-urdu-arabic-700-normal.woff2", None)]

LANG = dict(
    code="ur", folder="book-03-urdu", series_no=3, isbn="", dir="rtl",
    name="Urdu", native="اردو", native_tr="urdoo", name_word="نام", write_word="لکھیں",
    title="My First Urdu Alphabet", title_native="میری پہلی اردو حروفِ تہجی",
    subtitle="A Coloring Book to Learn, Trace & Say the 38 Urdu Letters with English Phonetics",
    title_letters="ابپتجچ", belongs_native="یہ کتاب میری ہے", belongs_pic="pen",
    alphabet_native="حروفِ تہجی", numbers_native="گنتی", numbers_tr="ginti", phrases_native="پہلے الفاظ",
    fonts=FONTS, disp_family="Baloo Bhaijaan 2", text_family="Noto Nastaliq Urdu",
    glyph_font="baloo-bhaijaan-2-arabic-800-normal.woff2", font_credit="Baloo Bhaijaan 2, Noto Nastaliq Urdu",
    extra_css=".nt{line-height:2.0} .lp-name{font-size:19pt;line-height:2.1} .lp-word .w{font-size:36pt;line-height:1.6}",
    series_line="<b>Book 3 is Urdu</b> — the national language of Pakistan and a language of millions in India. "
                "More languages of the subcontinent are in the series, in shā’ Allāh.",
    sound_notes=[
        "<b>Urdu is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>A dot under t, d, r</b> (<i>ṭ, ḍ, ṛ</i>) means a <i>hard</i> sound with the tongue curled back; without the dot the "
        "tongue touches the back of the top teeth.",
        "<b>Some letters sound the same</b> in Urdu (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ض ظ</span> all say <i>z</i>). "
        "They keep their Arabic spelling, which helps when children later read the Qur’an.",
        "<b>kh</b> and <b>gh</b> are soft throat sounds; <b>q</b> is a <i>k</i> said deep in the throat."],
    phon_explain="Because Urdu letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="standard Urdu as spoken in Pakistan and India",
    hello=[
        ("Who speaks it?", "About <b>230 million people</b> speak Urdu as a first or second language.<sup>³</sup>"),
        ("Where?", "Urdu is the <b>national language of Pakistan</b>. In <b>India</b> it is an official language in several states, and "
                   "families speak it all over the world."),
        ("How is it written?", "From <b>right to left</b>, in a Perso-Arabic script — usually in the flowing, sloping style called "
                               "<b>Nastaliq</b>. Most letters <b>join</b> to the next one and change shape."),
        ("How many letters?", "This book teaches <b>38 letters</b>. Urdu shares many of them with Arabic and Persian, and adds its own "
                              "(<span class='nt'>ٹ ڈ ڑ</span> and <span class='nt'>ے</span>)."),
        ("A friend of the Qur’an", "Many Urdu words come from Arabic: <span class='nt'>قلم</span> <i>qalam</i> (pen), <span class='nt'>کتاب</span> "
                                    "<i>kitaab</i> (book), <span class='nt'>صبر</span> <i>sabr</i> (patience). Knowing the letters helps with reading the Qur’an."),
        ("Cousins: Urdu and Hindi", "In everyday talk, Urdu and Hindi are so close that speakers understand each other easily — but Urdu is "
                                    "written in this script and Hindi in Devanagari."),
    ],
    hello_pics=[("pen", {}), ("mosque", {}), ("kite", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=dict(
        frame=[[60.5, 17.0], [88.0, 36.8]], land=True,
        points=dict(islamabad=[73.05, 33.68], karachi=[67.0, 24.86], lahore=[74.36, 31.52], delhi=[77.21, 28.61],
                    lucknow=[80.95, 26.85], hyderabad=[78.47, 17.38], pak=[68.8, 29.2], india=[80.5, 21.8], arabian=[64.8, 19.5]),
        cities=[("islamabad", "Islamabad", 18, 8, "start", True), ("karachi", "Karachi", 14, 8, "start", False),
                ("lahore", "Lahore", 14, 8, "start", False), ("delhi", "Delhi", 14, 8, "start", False),
                ("lucknow", "Lucknow", 14, 8, "start", False), ("hyderabad", "Hyderabad", 14, -10, "start", False)],
        labels=[("pak", "PAKISTAN", 36, False), ("india", "INDIA", 36, False), ("arabian", "Arabian Sea", 30, True)],
        world_marker=[73.0, 27.0], world_r=16, world_caption="The circle shows Pakistan and north India on the world map.",
        legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Islamabad ★ is the capital of Pakistan. "
               "Urdu is also spoken in Karachi and Lahore, and in Indian cities such as Delhi, Lucknow and Hyderabad."),
    sections=[
        dict(key="letters", label="LETTER", chip="THE LETTERS", title="The Urdu Letters", native="حروفِ تہجی",
             native_tr="huroof-e-tahajji — “the letters for spelling”", chart_title="letters", chart_cols=7,
             warmup_title="the letters", warmup_cols=6,
             intro_html="""<p>Urdu is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Most Urdu letters <b>join</b> to the letter after them, and their shape changes
a little at the start, middle and end of a word. Each letter page shows all three shapes.
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ب + ا + د + ل = <span class="nt">بادل</span></div>
<div style="text-align:center"><i>b + aa + d + l = baadal</i> (clouds)</div></div>
<div class="box" style="margin:0.1in 0"><h3>Dots make the difference</h3>Many letters share one shape and differ only in their dots:
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ب &nbsp; پ &nbsp; ت &nbsp; ٹ &nbsp; ث</div>
<div style="text-align:center">one dot below · three below · two above · a little ‘ṭ’ · three above</div></div>
<div class="box"><h3>Nine letters never join forward</h3><span class="nt" style="font-size:16pt">ا د ڈ ذ ر ڑ ز ژ و</span> join to the letter
<i>before</i> them, but never to the one after. Look for the small note on their pages.</div>""",
             items=LETTERS),
    ],
    digits=[("۰", "صفر", "sifr", "zero"), ("۱", "ایک", "ek", "one"), ("۲", "دو", "do", "two"), ("۳", "تین", "teen", "three"),
            ("۴", "چار", "chaar", "four"), ("۵", "پانچ", "paanch", "five"), ("۶", "چھ", "chhe", "six"), ("۷", "سات", "saat", "seven"),
            ("۸", "آٹھ", "aaṭh", "eight"), ("۹", "نو", "nau", "nine")],
    phrases=[("السلام علیکم", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("وعلیکم السلام", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("میرا نام … ہے", "meraa naam … hai", "My name is …"),
             ("شکریہ", "shukriya", "Thank you"),
             ("جزاک اللہ خیراً", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("امی · ابو", "ammi · abbu", "Mother · Father"),
             ("بھائی · بہن", "bhaai · behen", "Brother · Sister"),
             ("جی ہاں · نہیں", "jee haan · naheen", "Yes · No"),
             ("میں اردو سیکھ رہا ہوں!", "main urdoo seekh rahaa hoon!", "I am learning Urdu! (a girl says: seekh rahee hoon)")],
    cheer=("ماشاءاللہ! شاباش!", "maashaa-allaah! shaabaash!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); status from the <b>Constitution of Pakistan</b> (Article 251).",
    book_pic=dict(left="ا ب پ", right="ت ٹ ث"),
    review_note="Check every letter name, the joined forms on each page and the Nastaliq spellings; confirm ژالہ (hail) and ضیا (light) are the words you want for ژ and ض.",
    cover=dict(title_html="My First Urdu<br>Alphabet", tiles="ابپتجم", pics=["pomegranate", "kite", "pen", "mosque"],
               blurb="Urdu is spoken by about 230 million people in Pakistan, India and around the world. This big, friendly coloring book "
                     "introduces young children to all <b>38 letters</b> of the Urdu alphabet <b>through English</b> — no Urdu needed at home.",
               bullets=["<b>Every letter on its own page</b> — a giant letter to color, its name in Urdu <i>and</i> English letters",
                        "<b>Easy English sound guides</b> and the letter’s <b>joined shapes</b> (start · middle · end)",
                        "<b>A word and picture for every letter</b>: <span class='nt'>قلم</span> <i>qalam</i> pen, <span class='nt'>مسجد</span> <i>masjid</i> mosque…",
                        "<b>Right-to-left tracing rows</b> and a warm-up page — great practice for reading the Qur’an",
                        "<b>Map to color</b>, Urdu numbers <span class='nt'>۰–۹</span>, first phrases and a certificate",
                        "<b>Single-sided coloring pages</b> so markers never ruin the next picture"]),
    kdp=dict(market="Amazon.com (also Amazon.co.uk and Amazon.ca)",
             desc_intro="Urdu is spoken by about 230 million people in Pakistan, India and around the world. This big, friendly coloring book introduces young children to all <b>38 letters</b> of the Urdu alphabet <b>through English</b>, so no Urdu is needed at home.",
             desc_bullets=["<b>Every letter on its own page:</b> a giant letter to color, with its name written in Urdu <i>and</i> in English letters",
                           "<b>Easy English sound guides</b>, plus the letter’s joined shapes at the start, middle and end of a word",
                           "<b>A word and a picture for every letter</b> to color and say: قلم <i>qalam</i> (pen), مسجد <i>masjid</i> (mosque), پتنگ <i>patang</i> (kite)…",
                           "<b>Right-to-left pencil tracing rows</b> on every page — a gentle first step towards reading the Qur’an",
                           "<b>Meet the language:</b> where Urdu is spoken, a map to color, the whole alphabet on one page, the numbers ۰–۹ and first friendly phrases"],
             categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                         "Children's Books › Education & Reference › Foreign Language Study",
                         "Children's Books › Religions › Islam"],
             keywords=["urdu alphabet book for kids", "learn urdu for children", "urdu letters tracing workbook",
                       "huroof e tahajji coloring", "muslim kids activity book", "islamic coloring book for children",
                       "pakistani heritage language gift"]),
)
