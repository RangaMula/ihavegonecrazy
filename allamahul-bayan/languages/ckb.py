# -*- coding: utf-8 -*-
"""Book 30 - Kurdish, Sorani (Central Kurdish, Arabic-based script, right-to-left, 33 letters). Allamahul Bayan Series.
REVIEW DRAFT. Modelled on ur.py (joined forms, dir="rtl"). Sorani writes its vowels with full letters
(ا ە و ۆ ی ێ ...); a word that starts with a vowel begins with the silent seat ئ.
Pictures: objects, plants and nature only. Facts kept neutral: no political borders or claims."""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
PH = "Letter shapes · how it joins"
BIG = 'class="ntd" style="font-size:24pt"'


def forms(ch, kind="dual"):
    if kind == "right":   # joins only to the letter before it
        return (f'<div style="font-size:12pt">Alone <span {BIG}>{ch}</span> · '
                f'after a letter <span {BIG}>{JOIN}{ch}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    if kind == "inside":  # never starts a word, joins both ways
        return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
                f'{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
                f'<div class="small">middle · end of a word (it never starts a word)</div>')
    if kind == "inside_right":  # never starts a word, joins only backwards
        return (f'<div style="font-size:12pt">Inside or at the end: <span {BIG}>{JOIN}{ch}</span> · <span {BIG}>{ch}</span></div>'
                f'<div class="small">It never starts a word and never joins to the letter after it.</div>')
    if kind == "seat":    # ئ
        return (f'<div style="font-size:12pt">Start of a word: <span {BIG}>{ch}{JOIN}</span></div>'
                f'<div class="small">It carries the vowel after it: <span class="nt">ئا ئە ئۆ ئێ ئی ئو</span>.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def K(ch, name, name_tr, sound, word, tr, meaning, pic, kind="dual", note=None, args=None, extra=None):
    phon = forms(ch, kind) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


S = "<span class='nt'>{}</span>".format
ARABIC = "Used mostly in words that come from Arabic."
SEAT = "At the start of a word it is written after the silent " + S("ئ") + ": "

LETTERS = [
    K("ئ", "هەمزە", "hemze", "silent — it lets a word begin with a vowel (like a tiny catch in the voice)", "ئەستێرە", "estêre", "star",
      "star", kind="seat"),
    K("ا", "ئەلیف", "elif", "‘a’ as in “father”", "ئاو", "aw", "water", "water", kind="right", extra=SEAT + S("ئا"),
      note="Find " + S("ا") + " after the silent " + S("ئ") + " in " + S("ئاو") + "."),
    K("ب", "بێ", "bê", "‘b’ as in “ball”", "بادەم", "badem", "almonds", "almond", extra="One dot below."),
    K("پ", "پێ", "pê", "‘p’ as in “pen”", "پیاز", "piyaz", "onion", "onion", extra="Three dots below."),
    K("ت", "تێ", "tê", "‘t’ as in “top”", "تەماتە", "temate", "tomato", "tomato", extra="Two dots above."),
    K("ج", "جیم", "jeem", "‘j’ as in “jam”", "جەژن", "jezhn", "Eid, a happy festival day", "eid"),
    K("چ", "چێ", "chê", "‘ch’ as in “chair”", "چا", "cha", "tea", "teacup"),
    K("ح", "حێ", "ḥê", "a strong breathy ‘h’ from the middle of the throat", "حەج", "hej", "Hajj, the journey to the Kaaba in Makkah",
      "kaaba", extra=ARABIC),
    K("خ", "خێ", "khê", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خورما", "khurma", "dates", "dates"),
    K("د", "دال", "dal", "‘d’ as in “dog”", "دار", "dar", "tree", "tree", kind="right"),
    K("ر", "رێ", "rê", "a light, tapped ‘r’ — never at the start of a word", "باران", "baran", "rain", "raincloud", kind="inside_right",
      note="Find " + S("ر") + " in the middle of " + S("باران") + ". A word never starts with " + S("ر") + ": it starts with " + S("ڕ") + "."),
    K("ڕ", "ڕێی قەڵەو", "ṟêy qeḷew", "a strong rolled ‘ṟ’ — let your tongue buzz! (as in Spanish “perro”)", "ڕۆژ", "ṟozh",
      "sun; day", "sun", kind="right", extra="The little ‘v’ under it makes the rolled ‘ṟ’. Its name means “heavy r”."),
    K("ز", "زێ", "zê", "‘z’ as in “zoo”", "زەیتوون", "zeytoon", "olives", "olive", kind="right"),
    K("ژ", "ژێ", "zhê", "‘zh’ like the ‘s’ in “measure”", "ژەم", "zhem", "a meal", "plate", kind="right"),
    K("س", "سین", "seen", "‘s’ as in “sun”", "سێو", "sêw", "apple", "apple"),
    K("ش", "شین", "sheen", "‘sh’ as in “shoe”", "شاخ", "shakh", "mountain", "mountain"),
    K("ع", "عەین", "‘eyn", "a squeezed sound deep in the throat, before or after a vowel", "عەرەبانە", "‘erebane", "cart", "cart",
      extra=ARABIC),
    K("غ", "غەین", "gheyn", "a soft gargled ‘gh’ from the back of the throat", "غار", "ghar", "cave", "ckb_cave"),
    K("ف", "فێ", "fê", "‘f’ as in “fan”", "فڕۆکە", "fiṟoke", "aeroplane", "plane"),
    K("ڤ", "ڤێ", "vê", "‘v’ as in “van” — a rare letter in Sorani", "ڤیتامین", "vitameen", "vitamins", "medicine",
      note=S("ڤ") + " is used mostly in borrowed words, and much more in Northern Kurdish.", extra="Three dots above."),
    K("ق", "قاف", "qaf", "a ‘k’ said far back in the throat", "قەڵەم", "qeḷem", "pen", "pen"),
    K("ک", "کاف", "kaf", "‘k’ as in “kite”", "کتێب", "kitêb", "book", "book", args=dict(left="ئ ا ب", right="پ ت ج")),
    K("گ", "گاف", "gaf", "‘g’ as in “go”", "گوڵ", "guḷ", "flower, rose", "flower"),
    K("ل", "لام", "lam", "a light ‘l’ as in “lemon”", "لیمۆ", "leemo", "lemon", "lemon"),
    K("ڵ", "ڵام", "ḷam", "a heavy, dark ‘ḷ’ as in “ball” — never at the start of a word", "ماڵ", "maḷ", "home, house", "house",
      kind="inside", note="Find " + S("ڵ") + " at the end of " + S("ماڵ") + "!", extra="The little ‘v’ on top makes the heavy ‘ḷ’."),
    K("م", "میم", "meem", "‘m’ as in “moon”", "مزگەوت", "mizgewt", "mosque", "mosque"),
    K("ن", "نوون", "noon", "‘n’ as in “net”", "نان", "nan", "bread", "roti"),
    K("ه", "هێ", "hê", "‘h’ as in “hat”", "هەنار", "henar", "pomegranate", "pomegranate"),
    K("ە", "ە", "e", "‘e’ as in “bed”", "هەور", "hewr", "cloud", "clouds", kind="right", extra=SEAT + S("ئە"),
      note="Find " + S("ە") + " after the " + S("ه") + " in " + S("هەور") + "."),
    K("و", "واو", "waw", "‘w’ as in “water”, or ‘u’ as in “put”; doubled " + S("وو") + " says a long ‘oo’", "وەرز", "werz",
      "season", "seasons", kind="right"),
    K("ۆ", "ۆ", "o", "‘o’ as in “go”", "تۆپ", "top", "ball", "ball", kind="right", extra=SEAT + S("ئۆ"),
      note="Find " + S("ۆ") + " in the middle of " + S("تۆپ") + "."),
    K("ی", "یێ", "yê", "‘y’ as in “yes”, or ‘ee’ as in “see”", "یاقووت", "yaqoot", "ruby, a red gem", "ring"),
    K("ێ", "ێ", "ê", "‘ê’ as in “they”", "مێوە", "mêwe", "fruit", "basket", extra=SEAT + S("ئێ"),
      note="Find " + S("ێ") + " in " + S("مێوە") + " — and look for the little ‘v’ under it."),
]

INTRO = """<p>Kurdish (Sorani) is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Vowels are written too</h3>Sorani writes its vowels with full letters, so you can read
every word aloud: <span class="nt">ا ە و ۆ ی ێ</span>. At the start of a word a vowel comes after the silent <span class="nt">ئ</span>:
<span class="nt">ئاو</span> <i>aw</i> (water).</div>
<div class="box" style="margin:0.1in 0"><h3>The little ‘v’ mark</h3>A small ‘v’ makes a new Kurdish sound:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ر → ڕ &nbsp;&nbsp; ل → ڵ &nbsp;&nbsp; و → ۆ &nbsp;&nbsp; ی → ێ</div>
<div style="text-align:center">r → rolled ṟ · l → heavy ḷ · w → o · y → ê</div></div>
<div class="box"><h3>Letters hold hands</h3>Most letters <b>join</b> to the next one. These never join forward:
<span class="nt" style="font-size:16pt">ا د ر ڕ ز ژ ە و ۆ</span>. Each page shows the letter’s shapes.</div>"""

LANG = build(dict(
    code="ckb", folder="book-30-kurdish-sorani", series_no=30, isbn="", draft=True, dir="rtl",
    name="Kurdish", native="کوردی", native_tr="kurdee", name_word="ناو", write_word="بنووسە",
    title="My First Kurdish (Sorani) Alphabet", cover_title_html="My First Kurdish<br>Alphabet", title_size=46,
    title_native="یەکەم ئەلفوبێی کوردیم", title_letters="ابپتجچ", belongs_native="ئەم کتێبە هی منە",
    belongs_pic="pen", alphabet_native="ئەلفوبێ", numbers_native="ژمارەکان", numbers_tr="zhimarekan",
    phrases_native="یەکەم وشەکان",
    fonts=fontset("Vazirmatn", "vazirmatn-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic"),
    disp_family="Vazirmatn", text_family="Noto Naskh Arabic",
    glyph_font=["vazirmatn-arabic-800-normal.woff2", "vazirmatn-latin-800-normal.woff2"],
    font_credit="Vazirmatn, Noto Naskh Arabic",
    extra_css=".nt{line-height:1.8;font-size:1.12em} .lp-name{font-size:24pt;line-height:1.6} .lp-word .w{font-size:38pt;line-height:1.5}",
    phon_feature="each letter’s <b>joined shapes</b> (start · middle · end)",
    sections=[section(LETTERS, native="ئەلفوبێ", native_tr="elfubê — “the A-B-C”", chart_cols=7, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Kurdish is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Vowels:</b> <i>a</i> as in “father”, <i>e</i> as in “bed”, <i>ê</i> as in “they”, <i>i</i> as in “sit”, "
        "<i>o</i> as in “go”, <i>u</i> as in “put”. <b>Doubled vowels are long:</b> <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>ṟ</b> (with a line under it) is a strong rolled ‘r’; <b>ḷ</b> (with a dot under it) is a heavy, dark ‘l’.",
        "<b>kh</b> and <b>gh</b> are soft throat sounds; <b>q</b> is a <i>k</i> said deep in the throat; <b>zh</b> is the ‘s’ in “measure”."],
    phon_explain="Because Kurdish letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="Sorani (Central Kurdish) as spoken in Erbil and Sulaymaniyah",
    hello=[
        ("Who speaks it?", "About <b>6 million people</b> speak Sorani, also called Central Kurdish.<sup>³</sup>"),
        ("Where?", "In the mountains and valleys of <b>northern Iraq</b> and <b>western Iran</b>, and by families all over the world. "
                   "Kurdish is one of the two official languages of Iraq, with Arabic."),
        ("How is it written?", "From <b>right to left</b>, in an Arabic-based script — and, unlike Arabic, every vowel is written."),
        ("How many letters?", "This book teaches <b>33 letters</b>, including Kurdish ones with a little ‘v’ mark: "
                              "<span class='nt'>ڕ ڵ ۆ ێ</span>, and <span class='nt'>ڤ</span>."),
        ("One language, many dialects", "Kurdish has several main dialects. Sorani is written in this script; Northern Kurdish "
                                        "(Kurmanji) is usually written in Latin letters."),
        ("A friend of the Qur’an", "Many Kurdish words come from Arabic: <span class='nt'>کتێب</span> <i>kitêb</i> (book), "
                                    "<span class='nt'>قەڵەم</span> <i>qeḷem</i> (pen). Knowing the letters helps with reading the Qur’an."),
    ],
    hello_pics=[("mountain", {}), ("pomegranate", {}), ("pen", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[38.5, 30.5], [51.5, 41.5]],
                   points=dict(erbil=[44.01, 36.19], sulaymaniyah=[45.43, 35.56], sanandaj=[47.00, 35.31],
                               mahabad=[45.72, 36.76], koya=[44.63, 36.08]),
                   area=(45.6, 35.9, 85, 55), area_rot=-30,
                   cities=[("erbil", "Erbil", -12, 6, "end", False), ("sulaymaniyah", "Sulaymaniyah", -10, 20, "end", False),
                           ("sanandaj", "Sanandaj", 12, 8, "start", False), ("mahabad", "Mahabad", 12, -8, "start", False)],
                   label="ZAGROS MOUNTAINS", label_at=[44.6, 33.2], marker=[45.5, 36.0],
                   caption="The circle shows the Zagros Mountains on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Sorani Kurdish is spoken "
                          "in cities such as Erbil and Sulaymaniyah in northern Iraq, and Sanandaj and Mahabad in western Iran.",
                   seas=[("Caspian Sea", 50.4, 39.6)], world_r=16),
    digits=[("٠", "سفر", "sifr", "zero"), ("١", "یەک", "yek", "one"), ("٢", "دوو", "doo", "two"), ("٣", "سێ", "sê", "three"),
            ("٤", "چوار", "chwar", "four"), ("٥", "پێنج", "pênj", "five"), ("٦", "شەش", "shesh", "six"), ("٧", "حەوت", "hewt", "seven"),
            ("٨", "هەشت", "hesht", "eight"), ("٩", "نۆ", "no", "nine")],
    phrases=[("ئەلسەلامو عەلەیکوم", "esselamu ‘eleykum", "Peace be upon you (the Muslim greeting)"),
             ("وەعەلەیکوم سەلام", "we‘eleykum selam", "And upon you be peace (the reply)"),
             ("ناوم … ە", "nawim … e", "My name is …"),
             ("سوپاس", "supas", "Thank you"),
             ("جەزاکەڵڵاهو خەیر", "jezakeḷḷahu kheyr", "May Allah reward you with good"),
             ("دایک · باوک", "dayk · bawk", "Mother · Father"),
             ("برا · خوشک", "bira · khushk", "Brother · Sister"),
             ("بەڵێ · نەخێر", "beḷê · nekhêr", "Yes · No"),
             ("من فێری کوردی دەبم!", "min fêrî kurdee debim!", "I am learning Kurdish!")],
    cheer=("ماشەڵڵا! دەستخۆش!", "masheḷḷa! destkhosh!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded; official status from the "
                 "<b>Constitution of Iraq</b> (Article 4).",
    book_pic=dict(left="ئ ا ب", right="پ ت ج"),
    review_note=("Check every word and spelling, the letter names (especially ر «ڕێ» and ڕ «ڕێی قەڵەو», which primers name in "
                 "different ways), the title یەکەم ئەلفوبێی کوردیم, and in particular: غار ghar (cave) for غ — ئەشکەوت is the commoner "
                 "word, so a better غ word may be wanted; ڤیتامین (vitamins) for the rare ڤ; ژەم zhem (meal) for ژ; یاقووت yaqoot (ruby) "
                 "for ی; جەژن (Eid) for ج; the h letter written ه (not ھ); the greetings ئەلسەلامو عەلەیکوم / وەعەلەیکوم سەلام and "
                 "جەزاکەڵڵاهو خەیر; the phrase من فێری کوردی دەبم; and the speaker number (about 6 million, Ethnologue)."),
    tiles="ڕڵۆێکژ", cover_pics=["pomegranate", "mountain", "pen", "mosque"],
    speakers_blurb="Sorani Kurdish is spoken by about 6 million people in northern Iraq, western Iran and around the world.",
    sample_words=[("سێو", "sêw", "apple"), ("گوڵ", "guḷ", "flower"), ("مزگەوت", "mizgewt", "mosque")],
    keywords=["kurdish alphabet book for kids", "learn sorani kurdish for children", "kurdish letters tracing workbook",
              "sorani alphabet coloring book", "muslim kids activity book", "islamic coloring book for children",
              "kurdish heritage language gift"],
))
