# -*- coding: utf-8 -*-
"""Book 38 - Ukrainian (Cyrillic, 33 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Аа"), built with engine/generic.py."""
from generic import build, letter, section
from maps import region_map

PH = "Ukrainian letter name"
BOOK = dict(left="А Б В", right="Г Ґ Д")


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:{20 if len(name) < 6 else 15}pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:2px">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("А", "а", "ah", "‘a’ as in “father”", "ананас", "ah-nah-NAHS", "pineapple", "pineapple"),
    L("Б", "бе", "beh", "‘b’ as in “ball”", "банан", "bah-NAHN", "banana", "banana"),
    L("В", "ве", "veh", "‘v’ as in “van” (at the end of a syllable, close to ‘w’)", "виноград", "vy-no-HRAHD", "grapes", "grapes",
      rule="Careful: it looks like English B, but it says ‘v’!"),
    L("Г", "ге", "heh", "a soft, voiced ‘h’, like ‘h’ in “ahead”", "гора", "ho-RAH", "mountain", "mountain"),
    L("Ґ", "ґе", "geh", "‘g’ as in “go”", "ґудзик", "GOOD-zyk", "button", "ru_button",
      note="Ґ is a rare letter: only a few words start with it."),
    L("Д", "де", "deh", "‘d’ as in “door”", "дерево", "DEH-reh-vo", "tree", "tree"),
    L("Е", "е", "eh", "‘e’ as in “bed”", "ескімо", "es-kee-MO", "ice cream on a stick", "ru_popsicle"),
    L("Є", "є", "yeh", "‘ye’ as in “yes”", "яєчко", "yah-YECH-ko", "little egg", "egg",
      note="Few words start with Є. Find it in the middle of <i>яєчко</i>!"),
    L("Ж", "же", "zheh", "‘zh’ like the ‘s’ in “measure”", "жолудь", "ZHO-lood", "acorn", "ru_acorn"),
    L("З", "зе", "zeh", "‘z’ as in “zoo”", "зірка", "ZEER-kah", "star", "star"),
    L("И", "и", "y", "like ‘i’ in “sit”", "лимон", "ly-MON", "lemon", "lemon",
      note="И almost never starts a word. Find it inside <i>лимон</i>!"),
    L("І", "і", "ee", "‘ee’ as in “see”", "інжир", "een-ZHYR", "figs", "fig"),
    L("Ї", "ї", "yee", "‘yee’ as in “yield”", "поїзд", "PO-yeezd", "train", "engine",
      note="Only a few words start with Ї. Find it inside <i>поїзд</i>!"),
    L("Й", "йот", "yot", "‘y’ as in “boy” — a quick glide", "чай", "chai", "tea", "teacup",
      note="Й usually comes after a vowel. Find it at the end of <i>чай</i>!"),
    L("К", "ка", "kah", "‘k’ as in “kite”", "книжка", "KNYZH-kah", "book", "book", BOOK),
    L("Л", "ел", "el", "‘l’ as in “lamp”", "ложка", "LOZH-kah", "spoon", "spoon"),
    L("М", "ем", "em", "‘m’ as in “moon”", "мечеть", "meh-CHET", "mosque", "mosque"),
    L("Н", "ен", "en", "‘n’ as in “net”", "ножиці", "NO-zhy-tsee", "scissors", "ru_scissors",
      rule="Careful: it looks like English H, but it says ‘n’!"),
    L("О", "о", "o", "‘o’ as in “more” — always clear and round", "окуляри", "o-koo-LYAH-ry", "glasses", "glasses"),
    L("П", "пе", "peh", "‘p’ as in “pen”", "парасолька", "pah-rah-SOL-kah", "umbrella", "umbrella"),
    L("Р", "ер", "er", "a rolled ‘r’ — let your tongue buzz!", "ромашка", "ro-MAHSH-kah", "daisy", "flower",
      rule="Careful: it looks like English P, but it says ‘r’!"),
    L("С", "ес", "es", "‘s’ as in “sun”", "сонце", "SON-tseh", "sun", "sun"),
    L("Т", "те", "teh", "‘t’ as in “top” (tongue on the teeth)", "тарілка", "tah-REEL-kah", "plate", "plate"),
    L("У", "у", "oo", "‘oo’ as in “moon”", "урожай", "oo-ro-ZHAI", "harvest", "basket",
      rule="Careful: it looks like English Y, but it says ‘oo’!"),
    L("Ф", "еф", "ef", "‘f’ as in “fan”", "фініки", "FEE-nee-ky", "dates", "dates"),
    L("Х", "ха", "khah", "a breathy ‘kh’, like ‘ch’ in Scottish “loch”", "хліб", "khleeb", "bread", "ru_bread",
      rule="Careful: it looks like English X, but it says ‘kh’!"),
    L("Ц", "це", "tseh", "‘ts’ as in “cats”", "цибуля", "tsy-BOO-lyah", "onion", "onion"),
    L("Ч", "че", "cheh", "‘ch’ as in “church”", "човен", "CHO-ven", "boat", "boat"),
    L("Ш", "ша", "shah", "‘sh’ as in “ship”", "шарф", "sharf", "scarf", "scarf"),
    L("Щ", "ща", "shchah", "‘sh’ + ‘ch’ together, as in “fresh cheese”", "щит", "shcheet", "shield", "shield"),
    L("Ь", "м’який знак", "m-YAH-kyy znahk (“soft sign”)", "no sound of its own: it makes the letter before it soft",
      "сіль", "seel", "salt", "salt", dict(label="сіль"),
      note="Ь never starts a word. At the end of <i>сіль</i> it makes the Л soft."),
    L("Ю", "ю", "yoo", "‘yu’ as in “you”", "юла", "yoo-LAH", "spinning top", "top"),
    L("Я", "я", "yah", "‘ya’ as in “yard”", "яблуко", "YAH-bloo-ko", "apple", "apple"),
]

EXTRA_CSS = ('.grid[style="margin-top:0.08in"]{gap:0.08in!important}'
             '.box[style*="justify-content:space-between;align-items:center;gap:0.2in"]{padding:0.04in 0.13in!important}')
CYR = [("Nunito Cyrillic", w, "normal", f"nunito-cyrillic-{w}-normal.woff2", None) for w in (400, 700, 800)]

LANG = build(dict(
    code="uk", folder="book-38-ukrainian", series_no=38, isbn="", draft=True,
    name="Ukrainian", native="українська мова", native_tr="oo-krah-YEEN-skah MO-vah", name_word="назва", write_word="пиши",
    title_native="Моя перша абетка", title_letters="АаҐґЇї", belongs_native="Ця книжка належить",
    belongs_pic="star", alphabet_native="абетка", numbers_native="числа", numbers_tr="chys-LAH",
    phrases_native="Перші слова",
    extra_css=EXTRA_CSS,
    fonts=CYR, disp_family="Nunito Cyrillic", text_family="Nunito Cyrillic",
    glyph_font=["nunito-cyrillic-900-normal.woff2", "nunito-latin-900-normal.woff2"],
    font_credit="Nunito (Cyrillic and Black weights)",
    phon_feature="each letter’s Ukrainian name (А «а», Б «бе», Й «йот»…)",
    sections=[section(LETTERS, native="абетка", native_tr="ah-BET-kah — “the alphabet”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Ukrainian is written in the <b>Cyrillic</b> alphabet. It has <b>33 letters</b>:
<b>10 vowels</b>, <b>22 consonants</b> and the <b>soft sign</b> Ь, which has no sound of its own.</p>
<div class="box" style="margin:0.1in 0"><h3>Some old friends…</h3>А, К, М, О and Т look and sound almost like English letters.</div>
<div class="box" style="margin:0.1in 0"><h3>…and some tricksters!</h3><span class="nt"><b>В Н Р С У Х</b></span> look like English letters,
but they say <i>v, n, r, s, oo, kh</i>. And Ukrainian <span class="nt"><b>Г</b></span> says a soft ‘h’, while <span class="nt"><b>Ґ</b></span> says ‘g’.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt"><b>Аа</b></span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>pah-rah-SOL-kah</i> means “say SOL a little louder”.",
        "<b>y</b> inside a word is the Ukrainian sound И, like ‘i’ in “sit”; <b>ee</b> is І, as in “see”.",
        "<b>h</b> is a soft, voiced ‘h’ (the letter Г); <b>kh</b> is a breathy sound from the throat, like ‘ch’ in Scottish “loch”.",
        "<b>zh</b> is the ‘s’ in “measure”; <b>r</b> is always rolled or tapped.",
        "Ukrainian vowels stay clear even when they are not stressed: <b>О</b> always says ‘o’."],
    phon_explain="The box marked <i>Ukrainian letter name</i> shows the name Ukrainian children use for each letter "
                 "(Б is «бе», Й is «йот»…) and a warning for letters that look like English ones but sound different.",
    standard="standard Ukrainian",
    hello=[
        ("Who speaks it?", "About <b>35 million people</b> speak Ukrainian.<sup>³</sup>"),
        ("Where?", "In <b>Ukraine</b>, and by Ukrainian families in many other countries, from Poland to Canada."),
        ("How is it written?", "In the <b>Cyrillic alphabet</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>33 letters</b>, including <span class=\"nt\"><b>Ґ, Є, І</b></span> and <span class=\"nt\"><b>Ї</b></span>."),
        ("A little mark", "Ukrainian uses an <b>apostrophe</b> inside some words to keep sounds apart: "
                          "<span class=\"nt\">п’ять</span> (<i>pyat</i>, five), <span class=\"nt\">м’яч</span> (<i>myach</i>, ball)."),
        ("Did you know?", "Some Ukrainian words came from Arabic through other languages: <span class=\"nt\">кава</span> "
                          "(<i>coffee</i>) from <i>qahwa</i>, and <span class=\"nt\">халва</span> (<i>halva</i>) from <i>ḥalwā</i>."),
    ],
    hello_pics=[("flower", {}), ("sun", {}), ("mosque", {})],
    map=region_map(frame=[[20.0, 41.5], [42.0, 55.5]],
                   points=dict(kyiv=[30.52, 50.45], lviv=[24.03, 49.84], kharkiv=[36.23, 49.99],
                               odesa=[30.73, 46.48], dnipro=[35.05, 48.46]),
                   area=None,
                   cities=[("kyiv", "Kyiv", 0, -22, "middle", True), ("lviv", "Lviv", 0, 34, "middle", False),
                           ("kharkiv", "Kharkiv", 0, -18, "middle", False), ("odesa", "Odesa", -14, 8, "end", False),
                           ("dnipro", "Dnipro", 0, 34, "middle", False)],
                   label="UKRAINE", label_at=[31.0, 52.6], marker=[31.0, 49.0],
                   caption="The circle shows Ukraine on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Ukrainian is spoken in Kyiv, "
                          "Lviv, Kharkiv, Dnipro, Odesa and in towns and villages all around them.",
                   seas=[("Black Sea", 32.5, 43.4)], world_r=12),
    digits=[("0", "нуль", "nool", "zero"), ("1", "один", "o-DYN", "one"), ("2", "два", "dvah", "two"),
            ("3", "три", "try", "three"), ("4", "чотири", "cho-TY-ry", "four"), ("5", "п’ять", "pyat", "five"),
            ("6", "шість", "sheest", "six"), ("7", "сім", "seem", "seven"), ("8", "вісім", "VEE-seem", "eight"),
            ("9", "дев’ять", "DEH-vyat", "nine")],
    phrases=[("Ассаляму алейкум", "as-sah-LYAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Ва алейкум ассалям", "wah ah-LAY-koom as-sah-LYAHM", "And upon you be peace (the reply)"),
             ("Привіт!", "pry-VEET", "Hello!"),
             ("Мене звати …", "MEH-neh ZVAH-ty …", "My name is …"),
             ("Дякую", "DYAH-koo-yoo", "Thank you"),
             ("Джазакаллаху хайран", "jah-zah-kahl-LAH-hoo KHAI-rahn", "May Allah reward you with good"),
             ("мама · тато", "MAH-mah · TAH-to", "Mother · Father"),
             ("брат · сестра", "braht · ses-TRAH", "Brother · Sister"),
             ("так · ні", "tahk · nee", "Yes · No"),
             ("Я вивчаю українську!", "yah vyv-CHAH-yoo oo-krah-YEEN-skoo", "I am learning Ukrainian!")],
    cheer=("Машаллах! Молодець!", "mah-shahl-LAH! mo-lo-DETS!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=BOOK,
    review_note="Check юла (a native speaker may prefer дзиґа for ‘spinning top’), урожай + basket picture for У, "
                "яєчко for Є, поїзд for Ї, and the stress marks in the transliterations.",
    tiles="АҐЄЇЖЯ", cover_pics=["pineapple", "sun", "ru_bread", "mosque"], title_size=46,
    speakers_blurb="Ukrainian is spoken by about 35 million people in Ukraine and around the world.",
    sample_words=[("сонце", "SON-tseh", "sun"), ("зірка", "ZEER-kah", "star"), ("яблуко", "YAH-bloo-ko", "apple")],
    keywords=["ukrainian alphabet book for kids", "learn ukrainian for children", "ukrainian abetka coloring book",
              "cyrillic letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual ukrainian english toddlers"],
))
