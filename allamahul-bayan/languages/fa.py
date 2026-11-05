# -*- coding: utf-8 -*-
"""Book 28 - Persian / Farsi (Perso-Arabic script, right-to-left, 32 letters). Allamahul Bayan Series. REVIEW DRAFT.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
Persian spelling uses ک (U+06A9) and ی (U+06CC), never Arabic ك ي. Transliteration follows standard Iranian Persian
(Tehran): aa = long a (as in "father"), ee = long i, oo = long u; short a, e, o.
New pictures: engine/pics/fa_pics.py (fa_bud, fa_rollingpin).
"""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
S_SAME = "Sounds the same as <span class='nt'>{}</span> in Persian."


def _cell(text, cap, size=24):
    return (f'<div style="flex:1;text-align:center"><div class="ntd" style="font-size:{size}pt;line-height:1.6">{text}</div>'
            f'<div class="small" style="line-height:1.1">{cap}</div></div>')


def _row(cells):  # first cell on the right, like the script
    return f'<div style="display:flex;flex-direction:row-reverse;gap:4px">{"".join(cells)}</div>'


def forms(ch, joins=True):
    if joins:
        return _row([_cell(f"{ch}{JOIN}", "start"), _cell(f"{JOIN}{ch}{JOIN}", "middle"), _cell(f"{JOIN}{ch}", "end")])
    return (_row([_cell(ch, "alone"), _cell(f"{JOIN}{ch}", "after a letter")])
            + '<div class="small" style="text-align:center">It never joins to the letter after it.</div>')


def F(ch, name, name_tr, sound, word, tr, meaning, pic, joins=True, args=None, note=None, extra=None):
    phon = forms(ch, joins) + (f'<div class="small" style="margin-top:6px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, "Letter shapes · how it joins", args, note)


LETTERS = [
    F("ا", "الف", "alef", "a long ‘aa’ as in “father”, said with round lips; at the start of a word it can also say a, e or o",
      "انار", "anaar", "pomegranate", "pomegranate", joins=False,
      extra="With a wavy hat, <span class='nt'>آ</span> (<i>alef madde</i>) always says ‘aa’: <span class='nt'>آب</span> <i>aab</i> (water)."),
    F("ب", "بِ", "be", "‘b’ as in “ball”", "بادبادک", "baadbaadak", "kite", "kite", extra="One dot below."),
    F("پ", "پِ", "pe", "‘p’ as in “pen”", "پنجره", "panjere", "window", "window",
      extra="Three dots below — a Persian letter that Arabic does not have."),
    F("ت", "تِ", "te", "‘t’ as in “tap”", "توپ", "toop", "ball", "ball", extra="Two dots above."),
    F("ث", "ثِ", "se", "‘s’ as in “sun”", "ثانیه", "saaniye", "a second (on the clock)", "clock", extra=S_SAME.format("س")),
    F("ج", "جیم", "jeem", "‘j’ as in “jam”", "جارو", "jaaroo", "broom", "broom"),
    F("چ", "چِ", "che", "‘ch’ as in “chair”", "چتر", "chatr", "umbrella", "umbrella",
      extra="Three dots below — a Persian letter."),
    F("ح", "حِ جیمی", "he-ye jeemi", "‘h’ as in “hat”", "حلقه", "halghe", "ring", "ring", extra=S_SAME.format("ه")),
    F("خ", "خِ", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خورشید", "khorsheed", "sun", "sun"),
    F("د", "دال", "daal", "‘d’ as in “dog”", "درخت", "derakht", "tree", "tree", joins=False),
    F("ذ", "ذال", "zaal", "‘z’ as in “zoo”", "ذرت", "zorrat", "corn", "corn", joins=False, extra=S_SAME.format("ز")),
    F("ر", "رِ", "re", "a tapped ‘r’ — flick the tongue once", "رنگین‌کمان", "rangeen-kamaan", "rainbow", "rainbow", joins=False),
    F("ز", "زِ", "ze", "‘z’ as in “zoo”", "زیتون", "zeytoon", "olives", "olive", joins=False),
    F("ژ", "ژِ", "zhe", "‘zh’ like the ‘s’ in “measure”", "ژاله", "zhaale", "dew", "dew", joins=False,
      extra="Three dots above — a Persian letter."),
    F("س", "سین", "seen", "‘s’ as in “sun”", "سیب", "seeb", "apple", "apple"),
    F("ش", "شین", "sheen", "‘sh’ as in “shoe”", "شال", "shaal", "shawl, scarf", "scarf"),
    F("ص", "صاد", "saad", "‘s’ as in “sun”", "صابون", "saaboon", "soap", "soap", extra=S_SAME.format("س")),
    F("ض", "ضاد", "zaad", "‘z’ as in “zoo”", "وضو", "vozoo", "wudu — washing before prayer", "ewer", extra=S_SAME.format("ز"),
      note='Few children’s words start with <span class="nt">ض</span> — find it in the middle of <span class="nt">وضو</span>!'),
    F("ط", "طا", "taa", "‘t’ as in “tap”", "طلوع", "toloo’", "sunrise", "sunrise", extra=S_SAME.format("ت")),
    F("ظ", "ظا", "zaa", "‘z’ as in “zoo”", "ظرف", "zarf", "dish", "plate", extra=S_SAME.format("ز")),
    F("ع", "عین", "eyn", "in Persian, a tiny catch in the voice (as in “uh-oh”) — or just the vowel next to it",
      "عینک", "eynak", "glasses", "glasses"),
    F("غ", "غین", "gheyn", "a soft, gargled ‘gh’ from the back of the throat", "غنچه", "ghonche", "flower bud", "fa_bud"),
    F("ف", "فِ", "fe", "‘f’ as in “fan”", "فنجان", "fenjaan", "cup", "teacup"),
    F("ق", "قاف", "ghaaf", "a gargled ‘gh’ — in Persian it sounds the same as غ", "قایق", "ghaayegh", "boat", "boat",
      extra=S_SAME.format("غ")),
    F("ک", "کاف", "kaaf", "‘k’ as in “kite”", "کتاب", "ketaab", "book", "book", args=dict(left="ت ث ج", right="ا ب پ")),
    F("گ", "گاف", "gaaf", "‘g’ as in “go”", "گل", "gol", "flower", "flower", extra="Like <span class='nt'>ک</span> with an extra line on top — a Persian letter."),
    F("ل", "لام", "laam", "‘l’ as in “lamp”", "لیمو", "leemoo", "lemon", "lemon"),
    F("م", "میم", "meem", "‘m’ as in “moon”", "ماه", "maah", "moon", "moon"),
    F("ن", "نون", "noon", "‘n’ as in “net”", "نان", "naan", "bread", "roti"),
    F("و", "واو", "vaav", "‘v’ as in “van”, or the vowels ‘oo’ and ‘o’", "وردنه", "vardane", "rolling pin", "fa_rollingpin",
      joins=False, extra="It also says ‘oo’: <span class='nt'>توپ</span> <i>toop</i> (ball)."),
    F("ه", "هِ دوچشم", "he-ye do-cheshm", "‘h’ as in “hat”; at the end of a word it often says ‘e’", "هندوانه", "hendevaane",
      "watermelon", "watermelon", extra="Its name means “two-eyed he”. At the end of <span class='nt'>پنجره</span> it says ‘e’."),
    F("ی", "یِ", "ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "یخ", "yakh", "ice", "ice",
      extra="It also says ‘ee’: <span class='nt'>سیب</span> <i>seeb</i> (apple)."),
]

_B = 'style="font-size:24pt;text-align:center;direction:rtl;line-height:1.6"'
INTRO = f"""<p>Persian is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them, and their shape
changes a little at the start, middle and end of a word. Seven letters, <span class="nt" style="font-size:15pt">ا د ذ ر ز ژ و</span>,
never join to the letter after them.
<div class="ntd" {_B}>گ + ل = گل</div>
<div style="text-align:center"><i>g + (o) + l = gol</i> (flower)</div></div>
<div class="box" style="margin:0.08in 0"><h3>Four letters of its own</h3>Persian uses the Arabic letters and adds four more:
<div class="ntd" {_B}>پ &nbsp; چ &nbsp; ژ &nbsp; گ</div>
<div style="text-align:center"><i>p · ch · zh · g</i></div></div>
<div class="box" style="margin:0.08in 0"><h3>Same sound, different letter</h3>Some letters sound the same in Persian. They keep their Arabic
spelling, which helps when children later read the Qur’an:
<div style="display:flex;flex-direction:row-reverse;justify-content:space-around;text-align:center;margin-top:2px">
<div><span class="ntd" style="font-size:18pt">ت ط</span><br><i>t</i></div><div><span class="ntd" style="font-size:18pt">ث س ص</span><br><i>s</i></div>
<div><span class="ntd" style="font-size:18pt">ذ ز ض ظ</span><br><i>z</i></div><div><span class="ntd" style="font-size:18pt">ح ه</span><br><i>h</i></div>
<div><span class="ntd" style="font-size:18pt">غ ق</span><br><i>gh</i></div></div></div>
<div class="box"><h3>Where are the vowels?</h3>The short vowels <i>a, e, o</i> are usually <b>not written</b> — you learn them with the word.
The long vowels are letters: <span class="nt">ا</span> says <i>aa</i>, <span class="nt">و</span> says <i>oo</i> and <span class="nt">ی</span>
says <i>ee</i>: <span class="nt">کتاب</span> <i>ketaab</i> (book).</div>"""

LANG = build(dict(
    code="fa", folder="book-28-persian", series_no=28, isbn="", draft=True, dir="rtl",
    name="Persian", native="فارسی", native_tr="faarsi", name_word="نام", write_word="بنویس",
    title="My First Persian Alphabet", title_native="اولین الفبای فارسی من", title_letters="ابپتثج",
    belongs_native="این کتاب مال من است", belongs_pic="flower",
    alphabet_native="الفبا", numbers_native="عددها", numbers_tr="adad-haa", phrases_native="اولین کلمه‌های من",
    fonts=fontset("Baloo Bhaijaan 2", "baloo-bhaijaan-2-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic"),
    disp_family="Baloo Bhaijaan 2", text_family="Noto Naskh Arabic",
    glyph_font="baloo-bhaijaan-2-arabic-800-normal.woff2", font_credit="Baloo Bhaijaan 2, Noto Naskh Arabic",
    extra_css=(".nt{line-height:1.9} .lp-name{font-size:24pt;line-height:1.5} "
               ".lp-word .w{font-size:40pt;line-height:1.7} .lp-info .box .small{line-height:1.25}"),
    phon_feature="the letter’s <b>joined shapes</b> at the start, middle and end of a word",
    sections=[section(LETTERS, title="The Persian Letters", native="الفبای فارسی",
                      native_tr="alefbaa-ye faarsi — “the Persian alphabet”",
                      chart_cols=8, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Persian is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father” (with rounder lips), <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>Short vowels:</b> <i>a</i> as in “cat”, <i>e</i> as in “bed”, <i>o</i> as in “for” (short and pure).",
        "<b>kh</b> and <b>gh</b> are soft throat sounds; <b>zh</b> is the ‘s’ in “measure”; <b>’</b> marks a tiny catch in the voice.",
        "<b>Some letters sound the same</b> in Persian (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ض ظ</span> all say <i>z</i>; "
        "<span class='nt'>غ ق</span> both say <i>gh</i>). The intro page before the letters shows them all."],
    phon_explain="Because Persian letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="standard Persian as spoken in Iran; Dari in Afghanistan sounds a little different in places",
    hello=[
        ("Who speaks it?", "About <b>110 million people</b> speak Persian as a first or second language.<sup>³</sup>"),
        ("Where?", "In <b>Iran</b>; in <b>Afghanistan</b>, where it is called <b>Dari</b>; and in <b>Tajikistan</b>, where it is "
                   "called <b>Tajik</b> and written in Cyrillic letters."),
        ("How is it written?", "From <b>right to left</b>, in the Arabic script. Most letters <b>join</b> to the next one and "
                               "change shape."),
        ("How many letters?", "<b>32 letters</b>: the 28 letters of Arabic plus four of its own, "
                              "<span class='nt'>پ چ ژ گ</span>."),
        ("A friend of the Qur’an", "Persian has many words from Arabic: <span class='nt'>کتاب</span> <i>ketaab</i> (book), "
                                    "<span class='nt'>قلم</span> <i>ghalam</i> (pen), <span class='nt'>صبر</span> <i>sabr</i> (patience). "
                                    "Knowing the letters helps with reading the Qur’an."),
        ("Did you know?", "English has borrowed words from Persian: <i>bazaar</i> (<span class='nt'>بازار</span> baazaar), "
                          "<i>caravan</i> (<span class='nt'>کاروان</span> kaarvaan) and <i>jasmine</i> (<span class='nt'>یاسمن</span> yaasaman)."),
    ],
    hello_pics=[("pomegranate", {}), ("mosque", {}), ("kite", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[43.0, 23.0], [75.0, 42.0]],
                   points=dict(tehran=[51.39, 35.69], isfahan=[51.67, 32.65], shiraz=[52.53, 29.59], mashhad=[59.61, 36.30],
                               tabriz=[46.29, 38.08], herat=[62.20, 34.35], kabul=[69.17, 34.53], dushanbe=[68.78, 38.56]),
                   area=None,
                   cities=[("tehran", "Tehran", 18, 8, "start", True), ("isfahan", "Isfahan", 14, 8, "start", False),
                           ("shiraz", "Shiraz", 14, 8, "start", False), ("mashhad", "Mashhad", 14, 8, "start", False),
                           ("tabriz", "Tabriz", 14, -8, "start", False), ("herat", "Herat", 14, 8, "start", False),
                           ("kabul", "Kabul", 18, 8, "start", True), ("dushanbe", "Dushanbe", 18, 8, "start", True)],
                   label="IRAN", label_at=[55.0, 31.6], marker=[58.0, 33.0],
                   caption="The circle shows Iran, Afghanistan and Tajikistan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> the capital cities ★ "
                          "Tehran (Iran), Kabul (Afghanistan) and Dushanbe (Tajikistan). Persian is also spoken in Isfahan, Shiraz, "
                          "Mashhad, Tabriz, Herat and many more cities.",
                   seas=[("Caspian Sea", 51.0, 40.2), ("Arabian Sea", 62.5, 22.3)], world_r=16),
    digits=[("۰", "صفر", "sefr", "zero"), ("۱", "یک", "yek", "one"), ("۲", "دو", "do", "two"), ("۳", "سه", "se", "three"),
            ("۴", "چهار", "chahaar", "four"), ("۵", "پنج", "panj", "five"), ("۶", "شش", "shesh", "six"), ("۷", "هفت", "haft", "seven"),
            ("۸", "هشت", "hasht", "eight"), ("۹", "نه", "noh", "nine")],
    phrases=[("السلام علیکم", "assalaamo aleykom", "Peace be upon you (the Muslim greeting)"),
             ("و علیکم السلام", "va aleykom assalaam", "And upon you be peace (the reply)"),
             ("اسم من … است", "esm-e man … ast", "My name is …"),
             ("متشکرم · ممنون", "motashakkeram · mamnoon", "Thank you"),
             ("جزاک الله خیراً", "jazaakallaahu kheyran", "May Allah reward you with good"),
             ("مادر · پدر", "maadar · pedar", "Mother · Father"),
             ("برادر · خواهر", "baraadar · khaahar", "Brother · Sister"),
             ("بله · نه", "bale · na", "Yes · No"),
             ("من دارم فارسی یاد می‌گیرم!", "man daaram faarsi yaad migiram!", "I am learning Persian!")],
    cheer=("ماشاءالله! آفرین!", "maashaa’allaah! aafareen!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded; they count Iranian Persian, Dari and Tajik together.",
    book_pic=dict(left="ت ث ج", right="ا ب پ"),
    review_note="Check the letter names (especially حِ he-ye jeemi and هِ he-ye do-cheshm), the transliterations (Tehran "
                "pronunciation: panjere, halghe, ghaayegh), ثانیه for ث, وضو for ض, ظرف (dish) for ظ and وردنه (rolling pin) for و. "
                "Speaker number (about 110 million incl. Dari and Tajik) needs a current Ethnologue check.",
    tiles="ابپچژگ", cover_pics=["pomegranate", "flower", "kite", "mosque"], title_size=48,
    speakers_blurb="Persian (Farsi) is spoken by about 110 million people in Iran, Afghanistan, Tajikistan and around the world.",
    sample_words=[("گل", "gol", "flower"), ("کتاب", "ketaab", "book"), ("انار", "anaar", "pomegranate")],
    keywords=["persian alphabet book for kids", "learn farsi for children", "farsi alphabet coloring book",
              "persian letters tracing workbook", "alefba farsi for kids", "muslim kids activity book",
              "dari farsi heritage language gift"],
))
LANG["series_line"] = ("<b>Book 28 is Persian</b> — the language of Iran and Afghanistan, with a long tradition of poetry. "
                       "More languages from around the world are in the series, in shā’ Allāh.")
LANG["cover"]["bullets"][3] = "<b>Right-to-left tracing rows</b> and a warm-up page — great practice for reading the Qur’an"
# a second big map label
LANG["map"]["points"]["afg"] = [66.0, 32.2]
LANG["map"]["labels"].append(("afg", "AFGHANISTAN", 26, False))
