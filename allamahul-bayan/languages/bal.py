# -*- coding: utf-8 -*-
"""Book 19 - Balochi (Perso-Arabic script, right-to-left). Allamahul Bayan Series. REVIEW DRAFT.
Modelled on ur.py (joined forms, dir="rtl"). The alphabet follows the Balochi letters as commonly taught in
Pakistan; the Arabic-only letters (ث ح ذ ص ض ط ظ ع ف ق) are shown on the section intro page.
Pictures: objects, plants and nature only."""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
PH = "Letter shapes · how it joins"


def forms(ch, joins=True, only_final=False):
    if only_final:
        return (f'<div style="font-size:12pt">Joined to the letter before: '
                f'<span class="ntd" style="font-size:24pt">{JOIN}{ch}</span></div>')
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">{ch}</span> · '
                f'after a letter <span class="ntd" style="font-size:24pt">{JOIN}{ch}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def B(ch, name, name_tr, sound, word, tr, meaning, pic, joins=True, note=None, args=None, only_final=False, extra=None):
    phon = forms(ch, joins, only_final) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    B("ا", "اَلِپ", "alip", "‘a’ at the start of a word; a long ‘aa’ as in “father” inside a word", "انار", "anaar", "pomegranate",
      "pomegranate", joins=False),
    B("آ", "آ", "aa", "a long ‘aa’ as in “father”, at the start of a word", "آپ", "aap", "water", "water", joins=False,
      extra="An alif with a little wave on top. Balochi counts it as its own letter."),
    B("ب", "بے", "be", "‘b’ as in “ball”", "بوجیگ", "bojig", "boat", "boat", extra="One dot below."),
    B("پ", "پے", "pe", "‘p’ as in “pen”", "پُل", "pul", "flower", "flower", extra="Three dots below."),
    B("ت", "تے", "te", "a soft ‘t’ — tongue touches the back of the teeth", "تاس", "taas", "cup, bowl", "teacup", extra="Two dots above."),
    B("ٹ", "ٹے", "ṭe", "a hard ‘t’ — curl your tongue back, as in “top”", "ٹماٹر", "ṭamaaṭar", "tomato", "tomato",
      extra="A little ‘ṭ’ sign on top."),
    B("ج", "جیم", "jeem", "‘j’ as in “jam”", "جَو", "jaw", "barley", "paddy"),
    B("چ", "چے", "che", "‘ch’ as in “chair”", "چِراگ", "chiraag", "oil lamp", "bal_lamp"),
    B("خ", "خے", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خط", "khat", "letter (that you post)",
      "envelope"),
    B("د", "دال", "daal", "a soft ‘d’ — tongue touches the back of the teeth", "دْرَچک", "drachk", "tree", "tree", joins=False),
    B("ڈ", "ڈال", "ḍaal", "a hard ‘d’ — curl your tongue back, as in “dog”", "ڈَگار", "ḍagaar", "land, the earth", "globe", joins=False),
    B("ر", "رے", "re", "a tapped ‘r’ — flick the tongue once", "روچ", "roch", "sun, day", "sun", joins=False),
    B("ڑ", "ڑے", "ṛe", "a flapped ‘r’ with the tongue curled back — never at the start of a word", "گُڑ", "guṛ",
      "jaggery (sugar made from sugarcane)", "sugarcane", joins=False,
      note='Look for <span class="nt">ڑ</span> at the end of <span class="nt">گُڑ</span>!'),
    B("ز", "زے", "ze", "‘z’ as in “zoo”", "زِر", "zir", "sea", "waves", joins=False),
    B("ژ", "ژے", "zhe", "‘zh’ like the ‘s’ in “measure” — a rare letter", "ژالہ", "zhaala", "hail", "raincloud", joins=False,
      note="ژ is rare in Balochi: it is found in only a few words."),
    B("س", "سین", "seen", "‘s’ as in “sun”", "سیب", "seeb", "apple", "apple"),
    B("ش", "شین", "sheen", "‘sh’ as in “shoe”", "شَپ", "shap", "night", "moon"),
    B("غ", "غین", "ghain", "a soft gargled ‘gh’ from the back of the throat", "غار", "ghaar", "cave", "mountain"),
    B("ک", "کاف", "kaaf", "‘k’ as in “kite”", "کِتاب", "kitaab", "book", "book", args=dict(left="ا آ ب", right="پ ت ٹ")),
    B("گ", "گاف", "gaaf", "‘g’ as in “go”", "گوات", "gwaat", "wind", "bal_wind"),
    B("ل", "لام", "laam", "‘l’ as in “lamp”", "لوگ", "log", "house, home", "house"),
    B("م", "میم", "meem", "‘m’ as in “moon”", "مَسیت", "maseet", "mosque", "mosque"),
    B("ن", "نون", "noon", "‘n’ as in “net”", "نَگن", "nagan", "bread", "roti"),
    B("و", "واو", "waaw", "‘w’ as in “water”, or the long vowels ‘oo’ and ‘o’", "وَرگ", "warag", "food", "plate", joins=False),
    B("ھ", "ھے", "he", "‘h’ as in “hat”", "ھُرماگ", "hurmaag", "dates", "dates",
      extra="Balochi writes ‘h’ with this two-eyed <span class='nt'>ھ</span>."),
    B("ی", "یے", "ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "یَکّ", "yakk", "one", "one", args=dict(digit="۱")),
    B("ے", "مزنیں یے", "mazanen ye", "a long ‘e’ as in “they” — only at the end of a word", "چاے", "chaay", "tea", "teacup",
      only_final=True, note='Look for <span class="nt">ے</span> at the end of <span class="nt">چاے</span>!',
      extra="Its name means “big ye”."),
]

N = len(LETTERS)

INTRO = """<p>Balochi is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them and change shape a little.
Each letter page shows the shapes at the start, middle and end of a word.
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ل + و + گ = <span class="nt">لوگ</span>
<span style="font-family:Nunito;font-size:12pt;font-weight:400;direction:ltr;unicode-bidi:isolate"> &nbsp;<i>log</i> (house)</span></div></div>
<div class="box" style="margin:0.08in 0"><h3>Long and short vowels</h3>The long vowels are written with letters:
<div style="display:flex;justify-content:space-around;margin:2px 0;direction:rtl">
<div style="text-align:center"><span class="ntd" style="font-size:22pt">ا &nbsp;آ</span><br><i>aa</i></div>
<div style="text-align:center"><span class="ntd" style="font-size:22pt">ی</span><br><i>ee</i></div>
<div style="text-align:center"><span class="ntd" style="font-size:22pt">ے</span><br><i>e</i></div>
<div style="text-align:center"><span class="ntd" style="font-size:22pt">و</span><br><i>oo</i> or <i>o</i></div></div>
Short vowels are little marks that are often left out:
<div style="display:flex;justify-content:center;gap:0.5in;direction:rtl;margin-top:2px">
<div style="text-align:center"><span class="ntd" style="font-size:24pt">بَ</span><br><i>ba</i> · zabar</div>
<div style="text-align:center"><span class="ntd" style="font-size:24pt">بِ</span><br><i>bi</i> · zer</div>
<div style="text-align:center"><span class="ntd" style="font-size:24pt">بُ</span><br><i>bu</i> · pesh</div></div></div>
<div class="box" style="margin:0.08in 0"><h3>Letters for Arabic words</h3>Balochi words do not need these letters, but you will meet them in words
from Arabic, in names and when reading the Qur’an:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ث &nbsp; ح &nbsp; ذ &nbsp; ص &nbsp; ض &nbsp; ط &nbsp; ظ &nbsp; ع &nbsp; ف &nbsp; ق</div></div>
<div class="box"><h3>Ten letters never join forward</h3><span class="ntd" style="font-size:18pt;word-spacing:0.12in">ا آ د ڈ ر ڑ ز ژ و</span> (and the final
<span class="nt">ے</span>) join to the letter <i>before</i> them, but never to the one after.</div>"""

FONTS = fontset("Baloo Bhaijaan 2", "baloo-bhaijaan-2-arabic", "Noto Nastaliq Urdu", "noto-nastaliq-urdu-arabic")

LANG = build(dict(
    code="bal", folder="book-19-balochi", series_no=19, isbn="", dir="rtl", draft=True,
    name="Balochi", native="بلوچی", native_tr="balochi", name_word="نام", write_word="بنبیس",
    title_native="بلوچی الف بے", title_letters="اآبپتٹ", belongs_native="اے کتاب منی اِنت", belongs_pic="dates",
    alphabet_native="الف بے", numbers_native="شمار", numbers_tr="shumaar", phrases_native="اولی لبز",
    fonts=FONTS, disp_family="Baloo Bhaijaan 2", text_family="Noto Nastaliq Urdu",
    glyph_font="baloo-bhaijaan-2-arabic-800-normal.woff2", font_credit="Baloo Bhaijaan 2, Noto Nastaliq Urdu",
    extra_css=".nt{line-height:2.0} .lp-name{font-size:19pt;line-height:2.1} .lp-word .w{font-size:36pt;line-height:1.6}",
    phon_feature="each letter’s <b>joined shapes</b> (start · middle · end)",
    sections=[section(LETTERS, label="LETTER", chip="THE LETTERS", title="The Balochi Letters", native="الف بے",
                      native_tr="alif be — “the A-B-C”", chart_title="letters", chart_cols=7, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Balochi is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. "
        "<i>e</i> and <i>o</i> are long too, as in “they” and “go”.",
        "<b>A dot under t, d, r</b> (<i>ṭ, ḍ, ṛ</i>) means a <i>hard</i> sound with the tongue curled back; without the dot the "
        "tongue touches the back of the top teeth.",
        "<b>kh</b> and <b>gh</b> are soft throat sounds.",
        "Balochi is spoken in several ways from place to place. This book mostly follows the words used in the south, along the coast."],
    phon_explain="Because Balochi letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="Balochi as written in Pakistan, with mostly southern (coastal) words",
    hello=[
        ("Who speaks it?", "About <b>8 million people</b> speak Balochi.<sup>³</sup>"),
        ("Where?", "Mostly in the <b>south-west of Pakistan</b>, in the province of Balochistan and in Karachi. Balochi is also "
                   "spoken in nearby parts of <b>Iran</b> and <b>Afghanistan</b>, and by families in <b>Oman</b> and the Gulf."),
        ("How is it written?", "From <b>right to left</b>, in a Perso-Arabic script. Most letters <b>join</b> to the next one and "
                               "change shape."),
        ("How many letters?", f"This book teaches <b>{N} letters</b>. Balochi shares them with Urdu and Persian, and uses the "
                              "two-eyed <span class='nt'>ھ</span> for every ‘h’."),
        ("Mountains, desert and sea", "Balochi lands have high, dry mountains, wide deserts and a long coast on the "
                                      "<b>Arabian Sea</b>, where fishing boats sail from towns such as <b>Gwadar</b>."),
        ("Sweet dates", "Date palms grow in the south. A Balochi child might say <span class='nt'>ھُرماگ</span> <i>hurmaag</i> "
                        "— dates — the fruit Muslims love to open their fast with."),
    ],
    hello_pics=[("dates", {}), ("boat", {}), ("mountain", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[55.5, 20.0], [71.0, 34.5]],
                   points=dict(quetta=[67.00, 30.18], gwadar=[62.33, 25.12], turbat=[63.05, 26.00], karachi=[67.01, 24.86]),
                   area=(64.3, 28.2, 210, 150), area_rot=-15,
                   cities=[("quetta", "Quetta", 14, 8, "start", False), ("gwadar", "Gwadar", 0, 34, "middle", False),
                           ("turbat", "Turbat", 14, -10, "start", False), ("karachi", "Karachi", 14, 8, "start", False)],
                   label="BALOCHI", label_at=[63.8, 29.0], marker=[64.0, 27.5],
                   caption="The circle shows where Balochi is spoken on the world map.",
                   legend="<b>Color it:</b> the land <b>yellow</b> or <b>brown</b> · the sea <b>blue</b>. <b>Find it:</b> the dashed line goes "
                          "around the main area where Balochi is spoken. Find Quetta, Turbat, Karachi and Gwadar by the sea.",
                   seas=[("Arabian Sea", 63.5, 22.0), ("Gulf of Oman", 58.0, 24.6)]),
    digits=[("۰", "صِفر", "sifr", "zero"), ("۱", "یَکّ", "yakk", "one"), ("۲", "دو", "do", "two"), ("۳", "سئے", "sai", "three"),
            ("۴", "چار", "chaar", "four"), ("۵", "پنچ", "panch", "five"), ("۶", "شش", "shash", "six"), ("۷", "ھپت", "hapt", "seven"),
            ("۸", "ھشت", "hasht", "eight"), ("۹", "نُہ", "noh", "nine")],
    phrases=[("السلام علیکم", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("وعلیکم السلام", "wa alaikum assalaam", "And upon you be peace (the reply)"),
             ("منی نام … اِنت", "mani naam … int", "My name is …"),
             ("منت وار", "minnatwaar", "Thank you"),
             ("جزاک اللہ خیراً", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("مات · پِت", "maat · pit", "Mother · Father"),
             ("برات · گوھار", "braat · gwahaar", "Brother · Sister"),
             ("ھو · نہ", "haw · na", "Yes · No"),
             ("من بلوچی ھیل کنگءَ آں!", "man balochi hel kanaga aan!", "I am learning Balochi!")],
    cheer=("ماشاءاللہ! شاباش!", "maashaa-allaah! shaabaash!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded, for all forms of Balochi together.",
    book_pic=dict(left="ا آ ب", right="پ ت ٹ"),
    review_note=("Balochi has several spelling traditions; please check (1) the letter list and order (آ as its own letter; خ and غ kept "
                 "in the main list; ہ left out because ھ is used for every h; ء not given its own page; Arabic-only letters shown on the intro "
                 "page); (2) the letter names, especially اَلِپ and مزنیں یے; (3) the words تاس (cup), جَو (barley), خط, گُڑ, ژالہ, غار, سیب, "
                 "وَرگ (food), چاے (and whether ے is right there), ٹماٹر; (4) southern vs. other forms: پُل, دْرَچک, ڈَگار, بوجیگ, نَگن, ھُرماگ; "
                 "(5) numbers سئے (3) and نُہ (9); (6) the phrases منت وار, ھو · نہ, the 'I am learning Balochi' sentence, and the titles "
                 "بنبیس, شمار, اولی لبز, اے کتاب منی اِنت; (7) the speaker number (about 8 million)."),
    tiles="اآبپگل", cover_pics=["dates", "boat", "bal_lamp", "mosque"], title_size=48,
    speakers_blurb="Balochi is spoken by about 8 million people, mostly in the south-west of Pakistan and in nearby lands by the Arabian Sea.",
    sample_words=[("روچ", "roch", "sun"), ("پُل", "pul", "flower"), ("لوگ", "log", "house")],
    keywords=["balochi alphabet book for kids", "learn balochi for children", "balochi letters tracing workbook",
              "baluchi coloring book", "muslim kids activity book", "islamic coloring book for children",
              "balochi heritage language gift"],
))
