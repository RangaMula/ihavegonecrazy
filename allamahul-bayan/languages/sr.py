# -*- coding: utf-8 -*-
"""Book 40 - Serbian (Vuk's Cyrillic, 30 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Аа"), built with engine/generic.py."""
from generic import build, letter, section
from maps import region_map

PH = "Serbian letter name"


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:{20 if len(name) < 6 else 15}pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:2px">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("А", "а", "ah", "‘a’ as in “father”", "авион", "AH-vee-on", "aeroplane", "plane"),
    L("Б", "бе", "beh", "‘b’ as in “ball”", "балон", "BAH-lon", "balloon", "balloon"),
    L("В", "ве", "veh", "‘v’ as in “van”", "вода", "VO-dah", "water", "water",
      rule="Careful: it looks like English B, but it says ‘v’!"),
    L("Г", "ге", "geh", "‘g’ as in “go”", "грожђе", "GROZH-jeh", "grapes", "grapes"),
    L("Д", "де", "deh", "‘d’ as in “door”", "дуга", "DOO-gah", "rainbow", "rainbow"),
    L("Ђ", "ђе", "jeh (soft)", "a soft ‘j’, as in “jeep” said with the tongue flat", "ђеврек", "JEV-rek", "ring-shaped bread roll", "ru_bagel",
      rule="Ђ is the soft partner of Џ."),
    L("Е", "е", "eh", "‘e’ as in “bed”", "ексер", "EK-ser", "nail", "ru_nail"),
    L("Ж", "же", "zheh", "‘zh’ like the ‘s’ in “measure”", "жир", "zheer", "acorn", "ru_acorn"),
    L("З", "зе", "zeh", "‘z’ as in “zoo”", "звезда", "ZVEZ-dah", "star", "star"),
    L("И", "и", "ee", "‘ee’ as in “see”", "играчке", "EE-grahch-keh", "toys", "blocks", dict(letters=("А", "Б", "В"))),
    L("Ј", "је", "yeh", "‘y’ as in “yes”", "јабука", "YAH-boo-kah", "apple", "apple",
      rule="Careful: it looks like English J, but it says ‘y’!"),
    L("К", "ка", "kah", "‘k’ as in “kite”", "кућа", "KOO-chah", "house", "house"),
    L("Л", "ел", "el", "‘l’ as in “lamp”", "лопта", "LOP-tah", "ball", "ball"),
    L("Љ", "ље", "lyeh", "a soft ‘ly’, as in “million”", "љуљашка", "LYOO-lyahsh-kah", "swing", "swing",
      rule="Љ is one letter made from Л and Ь joined together."),
    L("М", "ем", "em", "‘m’ as in “moon”", "месец", "MEH-sets", "moon", "moon"),
    L("Н", "ен", "en", "‘n’ as in “net”", "наочаре", "nah-O-chah-reh", "glasses", "glasses",
      rule="Careful: it looks like English H, but it says ‘n’!"),
    L("Њ", "ње", "nyeh", "a soft ‘ny’, as in “canyon”", "њива", "NYEE-vah", "field (of crops)", "paddy",
      rule="Њ is one letter made from Н and Ь joined together."),
    L("О", "о", "o", "‘o’ as in “more”", "облак", "OB-lahk", "cloud", "clouds"),
    L("П", "пе", "peh", "‘p’ as in “pen”", "прозор", "PRO-zor", "window", "window"),
    L("Р", "ер", "er", "a rolled ‘r’ — let your tongue buzz!", "ракета", "rah-KEH-tah", "rocket", "ru_rocket",
      rule="Careful: it looks like English P, but it says ‘r’!"),
    L("С", "ес", "es", "‘s’ as in “sun”", "сунце", "SOON-tseh", "sun", "sun"),
    L("Т", "те", "teh", "‘t’ as in “top” (tongue on the teeth)", "тањир", "TAH-nyeer", "plate", "plate"),
    L("Ћ", "ће", "cheh (soft)", "a soft ‘ch’, as in “cheese” said with the tongue flat", "ћуп", "choop", "clay pot", "pot",
      rule="Ћ is the soft partner of Ч."),
    L("У", "у", "oo", "‘oo’ as in “moon”", "урме", "OOR-meh", "dates", "dates",
      rule="Careful: it looks like English Y, but it says ‘oo’!"),
    L("Ф", "еф", "ef", "‘f’ as in “fan”", "фењер", "FEH-nyer", "lantern", "ru_lantern"),
    L("Х", "ха", "khah", "a breathy ‘kh’, like ‘ch’ in Scottish “loch”", "хлеб", "khleb", "bread", "ru_bread",
      rule="Careful: it looks like English X, but it says ‘kh’!"),
    L("Ц", "це", "tseh", "‘ts’ as in “cats”", "цвет", "tsvet", "flower", "flower"),
    L("Ч", "че", "cheh (hard)", "a hard ‘ch’, as in “church”", "чамац", "CHAH-mats", "boat", "boat"),
    L("Џ", "џе", "jeh (hard)", "a hard ‘j’, as in “jungle”", "џамија", "JAH-mee-yah", "mosque", "mosque"),
    L("Ш", "ше", "sheh", "‘sh’ as in “ship”", "шал", "shahl", "scarf", "scarf"),
]

EXTRA_CSS = ('.grid[style="margin-top:0.08in"]{gap:0.08in!important}'
             '.box[style*="justify-content:space-between;align-items:center;gap:0.2in"]{padding:0.04in 0.13in!important}')
CYR = ([("Nunito Cyrillic", w, "normal", f"nunito-latin-{w}-normal.woff2", "U+0000-00FF,U+2000-206F") for w in (400, 700, 800)]
       + [("Nunito Cyrillic", w, "normal", f"nunito-cyrillic-{w}-normal.woff2", None) for w in (400, 700, 800)])

LANG = build(dict(
    code="sr", folder="book-40-serbian", series_no=40, isbn="", draft=True,
    name="Serbian", native="српски језик", native_tr="SRP-skee YEH-zeek", name_word="име", write_word="пиши",
    title_native="Моја прва азбука", title_letters="АаЂђЉљ", belongs_native="Ова књига припада",
    belongs_pic="star", alphabet_native="азбука", numbers_native="бројеви", numbers_tr="BRO-yeh-vee",
    phrases_native="Прве речи",
    extra_css=EXTRA_CSS,
    fonts=CYR, disp_family="Nunito Cyrillic", text_family="Nunito Cyrillic",
    glyph_font=["nunito-cyrillic-900-normal.woff2", "nunito-latin-900-normal.woff2"],
    font_credit="Nunito (Cyrillic and Black weights)",
    phon_feature="each letter’s Serbian name (А «а», Б «бе», Љ «ље»…)",
    sections=[section(LETTERS, native="азбука", native_tr="AHZ-boo-kah — “the alphabet”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Serbian is written in <b>Vuk’s Cyrillic</b> alphabet. It has <b>30 letters</b>, and
<b>every letter has exactly one sound</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Write as you speak!</h3>The famous rule of Serbian spelling is
<span class="nt"><i>«Пиши као што говориш»</i></span> — “write as you speak, read as it is written”.
Once you know the 30 sounds, you can read any Serbian word.</div>
<div class="box" style="margin:0.1in 0"><h3>Some tricksters!</h3><span class="nt"><b>В Н Р С У Х Ј</b></span> look like English letters,
but they say <i>v, n, r, s, oo, kh, y</i>. Watch out for them!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt"><b>Аа</b></span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>LYOO-lyahsh-kah</i> means “say LYOO a little louder”. "
        "Serbian also has rising and falling tones, which a native speaker can show you.",
        "<b>kh</b> is a breathy sound from the throat, like ‘ch’ in Scottish “loch”; <b>zh</b> is the ‘s’ in “measure”.",
        "Serbian has two ‘ch’ sounds and two ‘j’ sounds: <b>Ч</b> and <b>Џ</b> are hard, <b>Ћ</b> and <b>Ђ</b> are soft. "
        "The guides write both as <i>ch</i> and <i>j</i>.",
        "<b>r</b> is always rolled; it can even act as a vowel, as in <span class=\"nt\">српски</span> (<i>SRP-skee</i>)."],
    phon_explain="The box marked <i>Serbian letter name</i> shows the name Serbian children use for each letter "
                 "(Б is «бе», Љ is «ље»…) and a note for letters that look like English ones but sound different.",
    standard="standard Serbian (Ekavian)",
    hello=[
        ("Who speaks it?", "About <b>9 million people</b> speak Serbian.<sup>³</sup>"),
        ("Where?", "In <b>Serbia</b>, in Bosnia and Herzegovina and in Montenegro, and by Serbian families around the world."),
        ("How is it written?", "In <b>Cyrillic</b> (this book) and also in the <b>Latin</b> alphabet, from <b>left to right</b>."),
        ("How many letters?", "<b>30 letters</b>, one for each sound, including <span class=\"nt\"><b>Ђ Ј Љ Њ Ћ Џ</b></span>."),
        ("One letter, one sound", "In the 1800s the scholar <b>Vuk Karadžić</b> set out the alphabet so that every sound has its own letter."),
        ("Did you know?", "Some Serbian words came from Arabic through Turkish: <span class=\"nt\">џамија</span> "
                          "(<i>mosque</i>) from <b>jāmiʿ</b>, and <span class=\"nt\">џеп</span> (<i>pocket</i>) from <i>jayb</i>."),
    ],
    hello_pics=[("apple", {}), ("swing", {}), ("mosque", {})],
    map=region_map(frame=[[16.0, 40.6], [25.6, 47.6]],
                   points=dict(belgrade=[20.46, 44.82], novisad=[19.84, 45.27], nis=[21.90, 43.32],
                               kragujevac=[20.91, 44.01], subotica=[19.67, 46.10]),
                   area=None,
                   cities=[("belgrade", "Belgrade", 16, 8, "start", True), ("novisad", "Novi Sad", -14, 8, "end", False),
                           ("nis", "Nish", 14, 8, "start", False), ("kragujevac", "Kragujevac", -14, 8, "end", False),
                           ("subotica", "Subotica", 14, 8, "start", False)],
                   label="SERBIA", label_at=[21.2, 45.6], marker=[20.8, 44.0],
                   caption="The circle shows Serbia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Serbian is spoken in Belgrade, "
                          "Novi Sad, Subotica, Kragujevac, Niš (say “neesh”) and in the towns and villages all around them.",
                   seas=[("Adriatic Sea", 16.9, 42.4)], world_r=10),
    digits=[("0", "нула", "NOO-lah", "zero"), ("1", "један", "YEH-dahn", "one"), ("2", "два", "dvah", "two"),
            ("3", "три", "tree", "three"), ("4", "четири", "CHEH-tee-ree", "four"), ("5", "пет", "pet", "five"),
            ("6", "шест", "shest", "six"), ("7", "седам", "SEH-dahm", "seven"), ("8", "осам", "O-sahm", "eight"),
            ("9", "девет", "DEH-vet", "nine")],
    phrases=[("Есселаму алејкум", "es-seh-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Ве алејкум селам", "veh ah-LAY-koom seh-LAHM", "And upon you be peace (the reply)"),
             ("Здраво!", "ZDRAH-vo", "Hello!"),
             ("Зовем се …", "ZO-vem seh …", "My name is …"),
             ("Хвала", "KHVAH-lah", "Thank you"),
             ("Џезакаллаху хајран", "jeh-zah-kahl-LAH-hoo KHAI-rahn", "May Allah reward you with good"),
             ("мама · тата", "MAH-mah · TAH-tah", "Mother · Father"),
             ("брат · сестра", "braht · SES-trah", "Brother · Sister"),
             ("да · не", "dah · neh", "Yes · No"),
             ("Учим српски!", "OO-cheem SRP-skee", "I am learning Serbian!")],
    cheer=("Машаллах! Браво!", "mah-shahl-LAH! BRAH-vo!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="А Б В", right="Г Д Ђ"),
    review_note="Check the letter names (ел, ем, ен, ер, ес, еф, ха are a draft), the greeting spellings Есселаму алејкум / "
                "Ве алејкум селам / Џезакаллаху хајран (Bosniak usage, here in Cyrillic), the stress marks (Serbian pitch "
                "accent is simplified), ексер for Е, њива + field picture for Њ, and the speaker number.",
    tiles="АЂЖЉЋЏ", cover_pics=["apple", "balloon", "sun", "mosque"], title_size=48,
    speakers_blurb="Serbian is spoken by about 9 million people in Serbia, its neighbours and around the world.",
    sample_words=[("сунце", "SOON-tseh", "sun"), ("кућа", "KOO-chah", "house"), ("јабука", "YAH-boo-kah", "apple")],
    keywords=["serbian alphabet book for kids", "learn serbian for children", "serbian cyrillic azbuka coloring book",
              "cyrillic letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual serbian english toddlers"],
))
