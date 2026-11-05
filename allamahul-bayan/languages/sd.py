# -*- coding: utf-8 -*-
"""Book 15 - Sindhi (Perso-Arabic script, Naskh style, 52 letters). Allamahul Bayan Series.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
REVIEW DRAFT: words, letter names and transliterations need a native Sindhi speaker.
"""
from indic import fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
U_ = lambda c: f"<u>{c}</u>"  # underlined letter = Sindhi implosive ("gulping") sound


def forms(letter, joins=True, only_final=False):
    if only_final:
        f = f'<span class="ntd">{JOIN}{letter}</span>'
        return f'<div style="font-size:12pt">Joined to the letter before: <span style="font-size:24pt">{f}</span></div>'
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">{letter}</span> · '
                f'after a letter <span class="ntd" style="font-size:24pt">{JOIN}{letter}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}{JOIN}&nbsp;&nbsp;{JOIN}{letter}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def S(letter, name, name_tr, sound, word, tr, meaning, pic, joins=True, note=None, args=None, extra=None):
    phon = forms(letter, joins) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return dict(letter=letter, name_native=name, name_en=name_tr, sound=sound,
                phon_label="Letter shapes · how it joins", phon=phon, note=note,
                word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {})


def nt(t):
    return f'<span class="nt">{t}</span>'


SAME = "Sounds the same as {}; it is used mostly in words from Arabic."
GULP = "a special Sindhi ‘{}’: say it while gently swallowing the air in (a “gulping” sound)"
PUFF = "Its sound is {} with a puff of air."

LETTERS = [
    S("ا", "الف", "alif", "‘a’, or a long ‘aa’ as in “father” inside a word", "انب", "ambu", "mango", "mango", joins=False),
    S("ب", "بي", "be", "‘b’ as in “ball”", "بادام", "baadaamu", "almond", "almond", extra="One dot below."),
    S("ٻ", "ٻي", U_("b") + "e", GULP.format("b"), "ٻيڙي", U_("b") + "eṛee", "boat", "boat",
      extra="Two dots below. A sound English does not have!"),
    S("ڀ", "ڀي", "bhe", "‘bh’ — a ‘b’ with a puff of air, as in “club-house”", "ڀت", "bhiti", "wall", "brick",
      extra="Four dots below."),
    S("ت", "تي", "te", "a soft ‘t’ — tongue touches the back of the teeth", "تارو", "taaro", "star", "star", extra="Two dots above."),
    S("ٿ", "ٿي", "the", "a soft ‘t’ with a puff of air (‘th’, but not as in “the”)", "ٿوم", "thoomu", "garlic", "sd_garlic",
      extra="Four dots above."),
    S("ٽ", "ٽي", "ṭe", "a hard ‘t’ — curl your tongue back, as in “top”", "ٽماٽو", "ṭamaaṭo", "tomato", "tomato"),
    S("ٺ", "ٺي", "ṭhe", "a hard ‘ṭ’ with a puff of air", "ڪاٺ", "kaaṭhu", "wood, logs", "sd_wood",
      note=f'Look for {nt("ٺ")} at the end of {nt("ڪاٺ")}!'),
    S("ث", "ثي", "se", "‘s’ as in “sun”", "ثمر", "samaru", "fruit", "basket", extra=SAME.format(nt("س"))),
    S("پ", "پي", "pe", "‘p’ as in “pen”", "پتنگ", "patangu", "kite", "kite", extra="Three dots below."),
    S("ج", "جيم", "jeem", "‘j’ as in “jam”", "جهاز", "jahaazu", "ship", "ship"),
    S("ڄ", "ڄي", U_("j") + "e", GULP.format("j"), "ڄمون", U_("j") + "amoon", "jamun (black plum)", "sd_jamun"),
    S("جه", "جهي", "jhe", "‘jh’ — a ‘j’ with a puff of air", "جهنڊو", "jhanḍo", "flag", "flag",
      extra=f"Written with two shapes: {nt('ج')} + {nt('ه')}, but it counts as one letter."),
    S("ڃ", "ڃي", "ñe", "‘ny’ as in “canyon”, said through the nose", "اُڃ", "uñ", "thirst (time for water!)", "water",
      note=f'{nt("ڃ")} almost never starts a word. Find it at the end of {nt("اُڃ")}.'),
    S("چ", "چي", "che", "‘ch’ as in “chair”", "چنڊ", "chanḍu", "moon", "moon"),
    S("ڇ", "ڇي", "chhe", "‘chh’ — a ‘ch’ with a big puff of air", "ڇٽي", "chhaṭee", "umbrella", "umbrella",
      extra="Four dots below."),
    S("ح", "وڏي حي", "vaḍee he", "‘h’ as in “hat”", "حج", "hajj", "Hajj, the journey to the Kaaba in Makkah", "kaaba",
      extra="Its name means “big he”."),
    S("خ", "خي", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خط", "khatu",
      "letter (that you post)", "envelope"),
    S("د", "دال", "daal", "a soft ‘d’ — tongue touches the back of the teeth", "دروازو", "darwaazo", "door", "door", joins=False),
    S("ڌ", "ڌال", "dhaal", "a soft ‘d’ with a puff of air", "ڌرتي", "dhartee", "the Earth", "globe", joins=False),
    S("ڏ", "ڏال", U_("d") + "aal", GULP.format("d"), "ڏاڙهون", U_("d") + "aaṛhoon", "pomegranate", "pomegranate", joins=False),
    S("ڊ", "ڊال", "ḍaal", "a hard ‘d’ — curl your tongue back, as in “dog”", "ڊٻو", "ḍa" + U_("b") + "o", "box", "box",
      joins=False, extra="One dot below."),
    S("ڍ", "ڍال", "ḍhaal", "a hard ‘ḍ’ with a puff of air", "ڍنڍ", "ḍhanḍhu", "lake", "sd_lake", joins=False),
    S("ذ", "ذال", "zaal", "‘z’ as in “zoo”", "ذڪر", "zikru", "dhikr — remembering Allah", "tasbih", joins=False,
      extra=SAME.format(nt("ز"))),
    S("ر", "ري", "re", "a tapped ‘r’ — flick the tongue once", "رومال", "roomaalu", "handkerchief, scarf", "scarf", joins=False),
    S("ڙ", "ڙي", "ṛe", "a flapped ‘r’ with the tongue curled back — it never starts a word", "پهاڙ", "pahaaṛu", "mountain",
      "mountain", joins=False, note=f'Look for {nt("ڙ")} at the end of {nt("پهاڙ")}!'),
    S("ز", "زي", "ze", "‘z’ as in “zoo”", "زيتون", "zaitoonu", "olive", "olive", joins=False),
    S("س", "سين", "seen", "‘s’ as in “sun”", "سج", "siju", "sun", "sun"),
    S("ش", "شين", "sheen", "‘sh’ as in “shoe”", "شيشو", "sheesho", "mirror", "mirror"),
    S("ص", "صاد", "su’aad", "‘s’ as in “sun”", "صابڻ", "saabaṇu", "soap", "soap", extra=SAME.format(nt("س"))),
    S("ض", "ضاد", "zu’aad", "‘z’ as in “zoo”", "ضيا", "ziyaa", "light", "bulb", extra=SAME.format(nt("ز"))),
    S("ط", "طوئي", "to’e", "a soft ‘t’, like ت", "طشتري", "tashtaree", "saucer, small plate", "plate", extra=SAME.format(nt("ت"))),
    S("ظ", "ظوئي", "zo’e", "‘z’ as in “zoo”", "ظرف", "zarfu", "container, jar", "jar", extra=SAME.format(nt("ز"))),
    S("ع", "عين", "ain", "in Sindhi, just the vowel next to it — in Arabic, a sound from deep in the throat", "عينڪ", "ainak",
      "glasses", "glasses"),
    S("غ", "غين", "ghain", "a soft gargled ‘gh’ from the back of the throat", "غبارو", "ghubaaro", "balloon", "balloon"),
    S("ف", "في", "fe", "‘f’ as in “fan”", "فانوس", "faanoosu", "lantern", "eid"),
    S("ڦ", "ڦي", "phe", "‘ph’ — a ‘p’ with a puff of air (not an ‘f’!)", "ڦڻي", "phaṇee", "comb", "sd_comb",
      extra="Four dots above."),
    S("ق", "قاف", "qaaf", "a ‘k’ said far back in the throat", "قلم", "qalamu", "pen", "pen"),
    S("ڪ", "ڪاف", "kaaf", "‘k’ as in “kite”", "ڪيلو", "kelo", "banana", "banana",
      extra="This long, flat shape is the everyday Sindhi ‘k’."),
    S("ک", "کي", "khe", "‘kh’ — a ‘k’ with a puff of air", "کجور", "khajoor", "dates", "dates",
      extra=f"Careful: in Urdu this shape is ‘k’, but in Sindhi {nt('ک')} is always ‘kh’."),
    S("گ", "گاف", "gaaf", "‘g’ as in “go”", "گل", "gulu", "flower", "flower"),
    S("ڳ", "ڳي", U_("g") + "e", GULP.format("g"), "ڳنو", U_("g") + "ano", "sugarcane", "sugarcane", extra="Two dots below."),
    S("گه", "گهي", "ghe", "‘gh’ — a ‘g’ with a puff of air, as in “dog-house”", "گهر", "gharu", "house, home", "house",
      extra=f"Written with two shapes: {nt('گ')} + {nt('ه')}, but it counts as one letter."),
    S("ڱ", "ڱي", "ṅe", "‘ng’ as in “sing” — it never starts a word", "رڱ", "raṅu", "colour", "palette",
      note=f'Look for {nt("ڱ")} at the end of {nt("رڱ")}!'),
    S("ل", "لام", "laam", "‘l’ as in “lamp”", "لٽو", "laṭṭoo", "spinning top", "top"),
    S("م", "ميم", "meem", "‘m’ as in “moon”", "مسجد", "masjidu", "mosque", "mosque"),
    S("ن", "نون", "noon", "‘n’ as in “net”", "ناريل", "naareelu", "coconut", "coconut"),
    S("ڻ", "ڻون", "ṇoon", "a hard ‘n’ with the tongue curled back — it never starts a word", "لوڻ", "looṇu", "salt", "salt",
      args=dict(label="لوڻ"), note=f'Look for {nt("ڻ")} at the end of {nt("لوڻ")}!'),
    S("و", "واؤ", "waa’u", "‘w’ as in “water”, or the long vowels ‘oo’ and ‘o’", "وڻ", "waṇu", "tree", "tree", joins=False),
    S("ه", "هي", "he", "‘h’ as in “hat”", "هندوانو", "hindwaano", "watermelon", "watermelon",
      extra="It also makes the puff of air in جه and گه."),
    dict(S("ء", "همزو", "hamzo", "a tiny break in the voice between two vowels", "ٿانءُ", "thaa’u", "pot, vessel", "pot",
           note=f'Find the little {nt("ء")} in {nt("ٿانءُ")}.'),
         phon=('<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">ء</span> · on a seat '
               '<span class="ntd" style="font-size:24pt">ئ &nbsp;ؤ &nbsp;أ</span></div>'
               '<div class="small">It never joins to any letter. Often it sits on a little “seat”.</div>')),
    S("ي", "يي", "ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "ياسمين", "yaasmeen", "jasmine", "sd_jasmine",
      extra="Two dots below."),
]

FONTS = fontset("Noto Sans Arabic", "noto-sans-arabic-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic")

LANG = dict(
    code="sd", folder="book-15-sindhi", series_no=15, isbn="", dir="rtl", draft=True,
    name="Sindhi", native="سنڌي", native_tr="sindhee", name_word="نالو", write_word="لکو",
    title="My First Sindhi Alphabet", title_native="منهنجو پهريون سنڌي ڪتاب",
    subtitle="A Coloring Book to Learn, Trace & Say the 52 Sindhi Letters with English Phonetics",
    title_letters="ابٻڀتٿ", belongs_native="هي ڪتاب منهنجو آهي", belongs_pic="pen",
    alphabet_native="الف ب", numbers_native="انگ", numbers_tr="ang", phrases_native="پهريان لفظ",
    fonts=FONTS, disp_family="Noto Sans Arabic", text_family="Noto Naskh Arabic",
    glyph_font=["noto-sans-arabic-arabic-800-normal.woff2", "noto-naskh-arabic-arabic-700-normal.woff2"],
    font_credit="Noto Sans Arabic, Noto Naskh Arabic",
    extra_css=".nt{line-height:1.9} .lp-name{font-size:20pt;line-height:1.9} .lp-word .w{font-size:38pt;line-height:1.6}",
    series_line="<b>Book 15 is Sindhi</b> — the language of Sindh, along the great Indus River. "
                "More languages of the subcontinent are in the series, in shā’ Allāh.",
    sound_notes=[
        "<b>Sindhi is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. Many Sindhi "
        "words end in a very short <i>u</i>, <i>o</i> or <i>i</i> (<i>ambu</i>, <i>kelo</i>): say it lightly.",
        "<b>An underlined letter</b> (<i><u>b</u>, <u>j</u>, <u>d</u>, <u>g</u></i>) is one of Sindhi’s four special "
        "<b>“gulping” sounds</b> (<span class='nt'>ٻ ڄ ڏ ڳ</span>): say the sound while gently pulling the air in.",
        "<b>An ‘h’ after a letter</b> (<i>bh, th, ṭh, jh, chh, dh, ḍh, ph, kh, gh</i>) means a <b>puff of air</b>. In Sindhi "
        "most of these have their own letter, so <i>ph</i> is a puffed ‘p’, never an ‘f’.",
        "<b>A dot under t, d, r, n</b> (<i>ṭ, ḍ, ṛ, ṇ</i>) means a <i>hard</i> sound with the tongue curled back; without the dot "
        "the tongue touches the back of the top teeth.",
        "<b>Some letters sound the same</b> (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ض ظ</span> all say "
        "<i>z</i>). They keep their Arabic spelling, which helps when children later read the Qur’an."],
    phon_explain="Because Sindhi letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="standard Sindhi as written in Pakistan (Naskh style)",
    hello=[
        ("Who speaks it?", "More than <b>30 million people</b> speak Sindhi.<sup>³</sup>"),
        ("Where?", "Sindhi is the language of <b>Sindh</b>, in the south of <b>Pakistan</b>, along the Indus River and the coast of "
                   "the Arabian Sea. Many Sindhi families also live in <b>India</b> and all over the world."),
        ("How is it written?", "From <b>right to left</b>, in a Perso-Arabic script, in the clear upright style called <b>Naskh</b>. "
                               "Most letters <b>join</b> to the next one and change shape. (In India, some people also write "
                               "Sindhi in Devanagari letters.)"),
        ("How many letters?", "This book teaches <b>52 letters</b> — many more than Arabic! Sindhi adds letters with extra dots for "
                              "its own sounds, such as <span class='nt'>ٻ ڀ ٽ ٿ ڄ ڇ ڊ ڏ ڳ ڻ</span>."),
        ("Four gulping sounds", "Sindhi has four very special sounds, <span class='nt'>ٻ ڄ ڏ ڳ</span>, made while pulling the air "
                                "<i>in</i>. Very few languages in the world have them!"),
        ("A friend of the Qur’an", "Many Sindhi words come from Arabic: <span class='nt'>قلم</span> <i>qalamu</i> (pen), "
                                    "<span class='nt'>ڪتاب</span> <i>kitaabu</i> (book), <span class='nt'>صبر</span> <i>sabru</i> (patience)."),
    ],
    hello_pics=[("boat", {}), ("sd_lake", {}), ("mango", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[61.5, 19.5], [75.5, 33.5]],
                   points=dict(karachi=[67.0, 24.86], hyderabad=[68.37, 25.39], sukkur=[68.86, 27.70], larkana=[68.21, 27.56],
                               thatta=[67.92, 24.75]),
                   area=(68.6, 26.2, 175, 215), area_rot=-10,
                   cities=[("karachi", "Karachi", -14, 30, "end", True), ("hyderabad", "Hyderabad", 14, -10, "start", False),
                           ("sukkur", "Sukkur", 14, 8, "start", False), ("larkana", "Larkana", -14, 8, "end", False),
                           ("thatta", "Thatta", 4, 34, "start", False)],
                   label="SINDH", label_at=[68.6, 28.35], marker=[68.5, 26.0],
                   caption="The circle shows Sindh on the world map.",
                   legend="<b>Color it:</b> Sindh (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · the sea "
                          "<b>blue</b>. <b>Find it:</b> Karachi ★ is the biggest city of Sindh. Sindhi is also spoken in Hyderabad, "
                          "Sukkur, Larkana and Thatta. Draw the great <b>Indus River</b> flowing south through Sindh "
                          "into the sea!",
                   seas=[("Arabian Sea", 64.6, 22.2)]),
    sections=[
        dict(key="letters", label="LETTER", chip="THE LETTERS", title="The Sindhi Letters", native="الف ب",
             native_tr="alif be — “the a-b-c”", chart_title="letters", chart_cols=8,
             warmup_title="the letters", warmup_cols=7,
             intro_html="""<p>Sindhi is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Most Sindhi letters <b>join</b> to the letter after them, and their shape changes
a little at the start, middle and end of a word. Each letter page shows all three shapes.
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ب + ا + د + ا + م = <span class="nt">بادام</span></div>
<div style="text-align:center"><i>b + aa + d + aa + m = baadaamu</i> (almond)</div></div>
<div class="box" style="margin:0.1in 0"><h3>Dots make the difference</h3>One shape, many letters — only the dots change:
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ب &nbsp; ٻ &nbsp; ڀ &nbsp; ت &nbsp; ٿ &nbsp; ٽ &nbsp; ٺ &nbsp; ث &nbsp; پ</div>
<div style="text-align:center">from the right: b · <u>b</u> · bh · t · th · ṭ · ṭh · s · p — count the dots on each one!</div></div>
<div class="box"><h3>Twelve letters never join forward</h3><span class="nt" style="font-size:16pt">ا د ڌ ڏ ڊ ڍ ذ ر ڙ ز و ء</span> join to the letter
<i>before</i> them, but never to the one after. Two letters, <span class="nt">جه</span> and <span class="nt">گه</span>, are written with two shapes.</div>""",
             items=LETTERS),
    ],
    digits=[("۰", "ٻڙي", U_("b") + "uṛee", "zero"), ("۱", "هڪ", "hiku", "one"), ("۲", "ٻه", U_("b") + "a", "two"),
            ("۳", "ٽي", "ṭe", "three"), ("۴", "چار", "chaar", "four"), ("۵", "پنج", "panja", "five"), ("۶", "ڇهه", "chha", "six"),
            ("۷", "ست", "sata", "seven"), ("۸", "اٺ", "aṭha", "eight"), ("۹", "نو", "nava", "nine")],
    phrases=[("السلام عليڪم", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("وعليڪم السلام", "wa alaikum assalaam", "And upon you be peace (the reply)"),
             ("منهنجو نالو … آهي", "munhinjo naalo … aahe", "My name is …"),
             ("مهرباني", "meharbaanee", "Thank you"),
             ("جزاڪ الله خيرًا", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("امڙ · بابا", "amaṛ · baabaa", "Mother · Father"),
             ("ڀاءُ · ڀيڻ", "bhaa’u · bheeṇa", "Brother · Sister"),
             ("ها · نه", "haa · na", "Yes · No"),
             ("مان سنڌي سکي رهيو آهيان!", "maan sindhee sikhee rahyo aahyaan!", "I am learning Sindhi! (a girl says: rahee aahyaan)")],
    cheer=("ماشاءالله! شاباس!", "maashaa-allaah! shaabaas!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="ا ب ٻ", right="ڀ ت ٿ"),
    review_note=("Draft for native review. Check: the 52-letter list (this book counts ء and the two-shape letters جه, گه, and "
                 "leaves out ژ, which some charts add); every letter name; the words ڀت (wall), ٿوم (garlic), ڪاٺ (wood), ڄمون (jamun), "
                 "اُڃ (thirst, for ڃ), ڏاڙهون (pomegranate), ڍنڍ (lake), ڦڻي (comb), ڳنو (sugarcane), رڱ (colour, for ڱ), ٿانءُ "
                 "(pot, for ء), ياسمين (jasmine), ضيا, طشتري, ظرف; the number words (esp. ٻڙي for zero); and every transliteration, "
                 "including the short final vowels and the underlined implosives."),
    cover=dict(title_html="My First Sindhi<br>Alphabet", tiles="ابٻڄڏڳ", pics=["boat", "mango", "moon", "mosque"],
               blurb="Sindhi is spoken by more than 30 million people in Pakistan, India and around the world. This big, friendly "
                     "coloring book introduces young children to all <b>52 letters</b> of the Sindhi alphabet <b>through English</b> — "
                     "no Sindhi needed at home.",
               bullets=["<b>Every letter on its own page</b> — a giant letter to color, its name in Sindhi <i>and</i> English letters",
                        "<b>Easy English sound guides</b> and the letter’s <b>joined shapes</b> (start · middle · end)",
                        "<b>A word and picture for every letter</b>: <span class='nt'>ٻيڙي</span> <i><u>b</u>eṛee</i> boat, "
                        "<span class='nt'>چنڊ</span> <i>chanḍu</i> moon…",
                        "<b>Right-to-left tracing rows</b> and a warm-up page — great practice for reading the Qur’an",
                        "<b>Map to color</b>, Sindhi numbers <span class='nt'>۰–۹</span>, first phrases and a certificate",
                        "<b>Single-sided coloring pages</b> so markers never ruin the next picture"]),
    kdp=dict(market="Amazon.com (also Amazon.co.uk and Amazon.ca)",
             desc_intro="Sindhi is spoken by more than 30 million people in Pakistan, India and around the world. This big, friendly "
                        "coloring book introduces young children to all <b>52 letters</b> of the Sindhi alphabet <b>through English</b>, "
                        "so no Sindhi is needed at home.",
             desc_bullets=["<b>Every letter on its own page:</b> a giant letter to color, with its name written in Sindhi <i>and</i> in English letters",
                           "<b>Easy English sound guides</b> (including Sindhi’s special “gulping” sounds), plus the letter’s joined shapes at the start, middle and end of a word",
                           "<b>A word and a picture for every letter</b> to color and say: ٻيڙي <i>beṛee</i> (boat), چنڊ <i>chanḍu</i> (moon), مسجد <i>masjidu</i> (mosque)…",
                           "<b>Right-to-left pencil tracing rows</b> on every page — a gentle first step towards reading the Qur’an",
                           "<b>Meet the language:</b> where Sindhi is spoken, a map to color, the whole alphabet on one page, the numbers ۰–۹ and first friendly phrases"],
             categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                         "Children's Books › Education & Reference › Foreign Language Study",
                         "Children's Books › Religions › Islam"],
             keywords=["sindhi alphabet book for kids", "learn sindhi for children", "sindhi letters tracing workbook",
                       "alif be sindhi coloring", "muslim kids activity book", "islamic coloring book for children",
                       "sindhi heritage language gift"]),
)
