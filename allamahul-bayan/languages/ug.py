# -*- coding: utf-8 -*-
"""Book 29 - Uyghur (Uyghur Arabic script, UEY, right-to-left, 32 letters). Allamahul Bayan Series. REVIEW DRAFT.
Modelled on ur.py (joined forms, dir="rtl"). Uyghur writes every vowel with a full letter (8 vowel letters);
at the start of a word a vowel sits after the silent seat ئ (hamza), so the vowel pages show ئا ئە ئو ...
Transliteration follows the Uyghur Latin spelling (ULY) made easier for English readers (x -> kh).
Pictures: objects, plants and nature only."""
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
    if kind == "inside":  # ڭ: never starts a word
        return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
                f'{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
                f'<div class="small">middle · end of a word (it never starts a word)</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def vforms(v, dual=False):
    """A Uyghur vowel: ئ + vowel at the start of a word, the bare vowel inside or at the end."""
    inner = (f'<span {BIG}>{JOIN}{v}{JOIN}</span> · <span {BIG}>{JOIN}{v}</span>' if dual
             else f'<span {BIG}>{v}</span> · <span {BIG}>{JOIN}{v}</span>')
    return (f'<div style="font-size:12pt">Start of a word: <span {BIG}>ئ{v}</span></div>'
            f'<div style="font-size:12pt">Inside or at the end: {inner}</div>'
            f'<div class="small">At the start, the vowel sits after the silent seat <span class="nt">ئ</span>.'
            + ("" if dual else " It never joins to the letter after it.") + '</div>')


def U(ch, name, name_tr, sound, word, tr, meaning, pic, kind="dual", note=None, args=None, extra=None):
    phon = forms(ch, kind) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


def V(v, name_tr, sound, word, tr, meaning, pic, dual=False, note=None, args=None):
    return letter("ئ" + v, "ئ" + v, name_tr, sound, word, tr, meaning, pic, vforms(v, dual), PH, args, note)


S = "<span class='nt'>{}</span>".format

LETTERS = [
    V("ا", "a", "‘a’ as in “father”", "ئالما", "alma", "apple", "apple"),
    V("ە", "e", "‘a’ as in “cat” — an open, bright ‘e’", "ئەينەك", "eynek", "mirror", "mirror"),
    U("ب", "بە", "be", "‘b’ as in “ball”", "بادام", "badam", "almonds", "almond", extra="One dot below."),
    U("پ", "پە", "pe", "‘p’ as in “pen”", "پىياز", "piyaz", "onion", "onion", extra="Three dots below."),
    U("ت", "تە", "te", "‘t’ as in “top”", "تاغ", "tagh", "mountain", "mountain", extra="Two dots above."),
    U("ج", "جە", "je", "‘j’ as in “jam”", "جوزا", "joza", "table", "ug_table"),
    U("چ", "چە", "che", "‘ch’ as in “chair”", "چاي", "chay", "tea", "teacup"),
    U("خ", "خە", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خورما", "khorma", "dates", "dates"),
    U("د", "دە", "de", "‘d’ as in “dog”", "دەرەخ", "derekh", "tree", "tree", kind="right"),
    U("ر", "رە", "re", "a tapped ‘r’ — flick the tongue once", "رەڭ", "reng", "colour, paint", "palette", kind="right",
      extra="Few Uyghur words start with " + S("ر") + "; most are borrowed words."),
    U("ز", "زە", "ze", "‘z’ as in “zoo”", "زەيتۇن", "zeytun", "olives", "olive", kind="right"),
    U("ژ", "ژە", "zhe", "‘zh’ like the ‘s’ in “measure” — a rare letter", "ژۇرنال", "zhurnal", "magazine", "book", kind="right",
      args=dict(left="ژ ۇ ر", right="ن ا ل"), note="A rare letter, found mostly in words borrowed from other languages."),
    U("س", "سە", "se", "‘s’ as in “sun”", "سۇ", "su", "water", "water"),
    U("ش", "شە", "she", "‘sh’ as in “shoe”", "شام", "sham", "candle", "ug_candle"),
    U("غ", "غە", "ghe", "a soft gargled ‘gh’ from the back of the throat", "غازاڭ", "ghazang", "fallen autumn leaves", "ug_leaves"),
    U("ف", "فە", "fe", "‘f’ as in “fan”", "فانۇس", "fanus", "lantern", "eid",
      extra=S("ف") + " is found mostly in words borrowed from Arabic and Persian."),
    U("ق", "قە", "qe", "a ‘k’ said far back in the throat", "قەلەم", "qelem", "pen", "pen"),
    U("ك", "كە", "ke", "‘k’ as in “kite”", "كىتاب", "kitab", "book", "book", args=dict(left="ئا ئە ب", right="پ ت ج")),
    U("گ", "گە", "ge", "‘g’ as in “go”", "گۈل", "gül", "flower", "flower"),
    U("ڭ", "ڭە", "nge", "‘ng’ as in “sing” — never at the start of a word", "ياڭاق", "yangaq", "walnut", "walnut", kind="inside",
      note="Find " + S("ڭ") + " in the middle of " + S("ياڭاق") + "!"),
    U("ل", "لە", "le", "‘l’ as in “lamp”", "لىمون", "limon", "lemon", "lemon"),
    U("م", "مە", "me", "‘m’ as in “moon”", "مەسچىت", "meschit", "mosque", "mosque"),
    U("ن", "نە", "ne", "‘n’ as in “net”", "نان", "nan", "flatbread (naan)", "roti"),
    U("ھ", "ھە", "he", "‘h’ as in “hat”", "ھەسەل", "hesel", "honey", "honey"),
    V("و", "o", "‘o’ as in “go”, short and round", "ئورۇندۇق", "orunduq", "chair, seat", "stool"),
    V("ۇ", "u", "‘u’ as in “put”", "ئۇن", "un", "flour", "ug_sack"),
    V("ۆ", "ö", "‘ö’ — say ‘e’ with round lips, like German “schön”", "ئۆي", "öy", "house, home", "house"),
    V("ۈ", "ü", "‘ü’ — say ‘ee’ with round lips, like French “tu”", "ئۈزۈم", "üzüm", "grapes", "grapes"),
    U("ۋ", "ۋە", "we", "‘w’ as in “water” (some speakers say ‘v’)", "ۋاقىت", "waqit", "time (look at the clock!)", "clock",
      kind="right"),
    V("ې", "é", "‘é’ as in “they”", "ئېتىز", "étiz", "field (farmland)", "paddy", dual=True),
    V("ى", "i", "‘i’ as in “sit” or ‘ee’ as in “see”", "ئىشىك", "ishik", "door", "door", dual=True),
    U("ي", "يە", "ye", "‘y’ as in “yes”", "يۇلتۇز", "yultuz", "star", "star"),
]

INTRO = """<p>Uyghur is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Every vowel has its own letter</h3>Arabic and Urdu often leave short vowels out. Uyghur
writes <b>all eight vowels</b> as full letters:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ا &nbsp; ە &nbsp; و &nbsp; ۇ &nbsp; ۆ &nbsp; ۈ &nbsp; ې &nbsp; ى</div>
At the start of a word a vowel sits after the silent seat <span class="nt">ئ</span>: <span class="nt">ئالما</span> <i>alma</i> (apple).</div>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them and change shape a little:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ن + ا + ن = <span class="nt">نان</span></div>
<div style="text-align:center"><i>n + a + n = nan</i> (flatbread)</div></div>
<div class="box"><h3>Eleven letters never join forward</h3><span class="nt" style="font-size:16pt">ا ە د ر ز ژ و ۇ ۆ ۈ ۋ</span> join to the letter
<i>before</i> them, but never to the one after. Their pages say so.</div>"""

LANG = build(dict(
    code="ug", folder="book-29-uyghur", series_no=29, isbn="", draft=True, dir="rtl",
    name="Uyghur", native="ئۇيغۇرچە", native_tr="uyghurche", name_word="ئىسمى", write_word="يېزىڭ",
    title_native="مېنىڭ تۇنجى ئۇيغۇرچە ئېلىپبەم", title_letters="ابپتجچ", belongs_native="بۇ كىتاب مېنىڭ",
    belongs_pic="pen", alphabet_native="ئېلىپبە", numbers_native="سانلار", numbers_tr="sanlar",
    phrases_native="تۇنجى سۆزلەر",
    fonts=fontset("Vazirmatn", "vazirmatn-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic"),
    disp_family="Vazirmatn", text_family="Noto Naskh Arabic",
    glyph_font=["vazirmatn-arabic-800-normal.woff2", "vazirmatn-latin-800-normal.woff2"],
    font_credit="Vazirmatn, Noto Naskh Arabic",
    extra_css=".nt{line-height:1.8;font-size:1.12em} .lp-name{font-size:24pt;line-height:1.6} .lp-word .w{font-size:38pt;line-height:1.5}",
    phon_feature="each letter’s <b>joined shapes</b> (start · middle · end)",
    sections=[section(LETTERS, native="ئېلىپبە", native_tr="élipbe — “the alphabet”", chart_cols=7, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Uyghur is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Vowels:</b> <i>a</i> as in “father”, <i>e</i> as in “cat”, <i>é</i> as in “they”, <i>i</i> as in “sit”, <i>o</i> as in “go”, "
        "<i>u</i> as in “put”. <i>ö</i> and <i>ü</i> are said with round lips, like German ö and ü.",
        "<b>kh</b> and <b>gh</b> are soft throat sounds; <b>q</b> is a <i>k</i> said deep in the throat; <b>ng</b> is the sound at the end of “sing”.",
        "Transliterations follow the Uyghur Latin spelling, with <i>kh</i> written for the letter <span class='nt'>خ</span>."],
    phon_explain="Because Uyghur letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word. Vowel pages show how the vowel is written at the start of a word (after "
                 "<span class='nt'>ئ</span>) and inside a word.",
    standard="standard Uyghur",
    hello=[
        ("Who speaks it?", "About <b>10 million people</b> speak Uyghur.<sup>³</sup>"),
        ("Where?", "In <b>Central Asia</b>: mostly in the Xinjiang region of north-west China, with communities in Kazakhstan, "
                   "Kyrgyzstan, Uzbekistan and around the world."),
        ("How is it written?", "From <b>right to left</b>, in an Arabic-based script. Unlike Arabic, it writes <b>every vowel</b> "
                               "with its own letter."),
        ("How many letters?", "This book teaches <b>32 letters</b>: 24 consonants and 8 vowels, including "
                              "<span class='nt'>ڭ ۆ ۈ ې</span>, which Arabic does not have."),
        ("Turkic cousins", "Uyghur is a Turkic language, a cousin of Uzbek, Kazakh and Turkish: <span class='nt'>سۇ</span> <i>su</i> "
                           "means water in Uyghur and <i>su</i> in Turkish too!"),
        ("A friend of the Qur’an", "Many Uyghur words come from Arabic: <span class='nt'>كىتاب</span> <i>kitab</i> (book), "
                                    "<span class='nt'>قەلەم</span> <i>qelem</i> (pen). Knowing the letters helps with reading the Qur’an."),
    ],
    hello_pics=[("pen", {}), ("grapes", {}), ("mountain", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[66.0, 28.0], [98.0, 52.0]],
                   points=dict(urumqi=[87.62, 43.83], kashgar=[75.99, 39.47], hotan=[79.92, 37.11], ghulja=[81.32, 43.91],
                               turpan=[89.19, 42.95], almaty=[76.95, 43.24]),
                   area=(82.5, 40.5, 120, 70),
                   cities=[("urumqi", "Ürümqi", 12, -8, "start", False), ("kashgar", "Kashgar", -12, 8, "end", False),
                           ("hotan", "Hotan", 12, 8, "start", False), ("ghulja", "Ghulja", 12, -8, "start", False),
                           ("turpan", "Turpan", 12, 12, "start", False), ("almaty", "Almaty", -12, -8, "end", False)],
                   label="CENTRAL ASIA", label_at=[82.0, 49.5], marker=[82.0, 41.0],
                   caption="The circle shows Central Asia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> and the big <b>Taklamakan Desert</b> <b>yellow</b>. "
                          "<b>Find it:</b> Uyghur is spoken in oasis cities such as Kashgar, Hotan, Turpan, Ghulja and Ürümqi, "
                          "and also in Almaty.",
                   seas=[("Taklamakan Desert", 83.0, 38.6)], world_r=18),
    digits=[("0", "نۆل", "nöl", "zero"), ("1", "بىر", "bir", "one"), ("2", "ئىككى", "ikki", "two"), ("3", "ئۈچ", "üch", "three"),
            ("4", "تۆت", "töt", "four"), ("5", "بەش", "besh", "five"), ("6", "ئالتە", "alte", "six"), ("7", "يەتتە", "yette", "seven"),
            ("8", "سەككىز", "sekkiz", "eight"), ("9", "توققۇز", "toqquz", "nine")],
    phrases=[("ئەسسالامۇ ئەلەيكۇم", "essalamu eleykum", "Peace be upon you (the Muslim greeting)"),
             ("ۋەئەلەيكۇم ئەسسالام", "we’eleykum essalam", "And upon you be peace (the reply)"),
             ("مېنىڭ ئىسمىم …", "méning ismim …", "My name is …"),
             ("رەھمەت", "rehmet", "Thank you"),
             ("جەزاكاللاھۇ خەيرەن", "jezakallahu kheyren", "May Allah reward you with good"),
             ("ئانا · دادا", "ana · dada", "Mother · Father"),
             ("ئاكا · ھەدە", "aka · hede", "(Older) brother · (older) sister"),
             ("ھەئە · ياق", "he’e · yaq", "Yes · No"),
             ("مەن ئۇيغۇرچە ئۆگىنىۋاتىمەن!", "men uyghurche öginiwatimen!", "I am learning Uyghur!")],
    cheer=("ماشائاللاھ! بەك ياخشى!", "mashallah! bek yakhshi!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="ئا ئە ب", right="پ ت ج"),
    review_note=("Check every word and spelling in the Uyghur Arabic script (UEY), the letter names (be, pe, te …), the title "
                 "مېنىڭ تۇنجى ئۇيغۇرچە ئېلىپبەم, and in particular: غازاڭ ghazang (fallen leaves) for غ, فانۇس fanus (lantern) for ف, "
                 "ژۇرنال zhurnal (magazine) for ژ, ۋاقىت waqit (time) for ۋ, ئېتىز étiz (field) for ئې, ئورۇندۇق orunduq (chair) for ئو, "
                 "ئاكا · ھەدە for brother · sister (some regions say ئاچا acha), the phrase مەن ئۇيغۇرچە ئۆگىنىۋاتىمەن and the cheer. "
                 "Confirm that drawing the vowels with their seat (ئا ئە …) is how Uyghur children learn them."),
    tiles="ابپتشۈ", cover_pics=["apple", "grapes", "pen", "mosque"], title_size=50,
    speakers_blurb="Uyghur is spoken by about 10 million people in Central Asia and around the world.",
    sample_words=[("ئالما", "alma", "apple"), ("ئۈزۈم", "üzüm", "grapes"), ("مەسچىت", "meschit", "mosque")],
    keywords=["uyghur alphabet book for kids", "learn uyghur for children", "uyghur letters tracing workbook",
              "uyghur arabic script coloring", "muslim kids activity book", "islamic coloring book for children",
              "uyghur heritage language gift"],
))
