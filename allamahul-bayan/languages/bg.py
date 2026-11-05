# -*- coding: utf-8 -*-
"""Book 39 - Bulgarian (Cyrillic, 30 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Аа"), built with engine/generic.py."""
from generic import build, letter, section
from maps import region_map

PH = "Bulgarian letter name"
BOOK = dict(left="А Б В", right="Г Д Е")


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:{20 if len(name) < 6 else 15}pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:2px">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("А", "а", "ah", "‘a’ as in “father”", "ананас", "ah-nah-NAHS", "pineapple", "pineapple"),
    L("Б", "бъ", "buh", "‘b’ as in “ball”", "банан", "bah-NAHN", "banana", "banana"),
    L("В", "въ", "vuh", "‘v’ as in “van”", "врата", "vrah-TAH", "door", "door",
      rule="Careful: it looks like English B, but it says ‘v’!"),
    L("Г", "гъ", "guh", "‘g’ as in “go”", "грозде", "GROZ-deh", "grapes", "grapes"),
    L("Д", "дъ", "duh", "‘d’ as in “door”", "диня", "DEE-nyah", "watermelon", "watermelon"),
    L("Е", "е", "eh", "‘e’ as in “bed”", "ела", "eh-LAH", "fir tree", "ru_fir"),
    L("Ж", "жъ", "zhuh", "‘zh’ like the ‘s’ in “measure”", "жълъд", "ZHUH-lut", "acorn", "ru_acorn"),
    L("З", "зъ", "zuh", "‘z’ as in “zoo”", "звезда", "zvez-DAH", "star", "star"),
    L("И", "и", "ee", "‘ee’ as in “see”", "изгрев", "EEZ-grev", "sunrise", "sunrise"),
    L("Й", "и кратко", "ee KRAHT-ko (“short i”)", "‘y’ as in “boy” — a quick glide", "чай", "chai", "tea", "teacup",
      note="Й starts only a few words. Find it at the end of <i>чай</i>!"),
    L("К", "къ", "kuh", "‘k’ as in “kite”", "кошница", "KOSH-nee-tsah", "basket", "basket"),
    L("Л", "лъ", "luh", "‘l’ as in “lamp”", "лъжица", "luh-ZHEE-tsah", "spoon", "spoon"),
    L("М", "мъ", "muh", "‘m’ as in “moon”", "морков", "MOR-kov", "carrot", "carrot"),
    L("Н", "нъ", "nuh", "‘n’ as in “net”", "ножица", "NO-zhee-tsah", "scissors", "ru_scissors",
      rule="Careful: it looks like English H, but it says ‘n’!"),
    L("О", "о", "o", "‘o’ as in “more”", "облак", "OB-lahk", "cloud", "clouds"),
    L("П", "пъ", "puh", "‘p’ as in “pen”", "планина", "plah-nee-NAH", "mountain", "mountain"),
    L("Р", "ръ", "ruh", "a rolled ‘r’ — let your tongue buzz!", "ракета", "rah-KEH-tah", "rocket", "ru_rocket",
      rule="Careful: it looks like English P, but it says ‘r’!"),
    L("С", "съ", "suh", "‘s’ as in “sun”", "слънце", "SLUN-tseh", "sun", "sun"),
    L("Т", "тъ", "tuh", "‘t’ as in “top” (tongue on the teeth)", "топка", "TOP-kah", "ball", "ball"),
    L("У", "у", "oo", "‘oo’ as in “moon”", "учебник", "oo-CHEB-neek", "school book", "book", BOOK,
      rule="Careful: it looks like English Y, but it says ‘oo’!"),
    L("Ф", "фъ", "fuh", "‘f’ as in “fan”", "фурми", "FOOR-mee", "dates", "dates"),
    L("Х", "хъ", "khuh", "a breathy ‘kh’, like ‘ch’ in Scottish “loch”", "хляб", "khlyap", "bread", "ru_bread",
      rule="Careful: it looks like English X, but it says ‘kh’!"),
    L("Ц", "цъ", "tsuh", "‘ts’ as in “cats”", "цвете", "TSVEH-teh", "flower", "flower"),
    L("Ч", "чъ", "chuh", "‘ch’ as in “church”", "чадър", "chah-DUR", "umbrella", "umbrella"),
    L("Ш", "шъ", "shuh", "‘sh’ as in “ship”", "шал", "shahl", "scarf", "scarf"),
    L("Щ", "щъ", "shtuh", "‘sht’, as at the end of “fresh tea” said fast", "щит", "shteet", "shield", "shield",
      rule="In Bulgarian, Щ always says ‘sht’."),
    L("Ъ", "ер голям", "er go-LYAM (“big er”)", "‘u’ as in “but”, or ‘a’ in “sofa”", "дъга", "duh-GAH", "rainbow", "rainbow",
      note="Ъ rarely starts a word (<i>ъгъл</i>, “corner”, is one). Find it in <i>дъга</i>!",
      rule="In Bulgarian, Ъ is a real vowel."),
    L("Ь", "ер малък", "er MAH-luk (“small er”)", "no sound of its own: it makes the letter before it soft, and is always followed by О",
      "шампиньон", "shahm-pee-NYON", "mushrooms", "ru_mushroom",
      note="Ь never starts a word. It only comes before О, as in <i>шампиньон</i>."),
    L("Ю", "ю", "yoo", "‘yu’ as in “you”", "ютия", "yoo-TEE-yah", "iron (for clothes)", "ru_iron"),
    L("Я", "я", "yah", "‘ya’ as in “yard”", "ябълка", "YAH-bul-kah", "apple", "apple"),
]

EXTRA_CSS = ('.grid[style="margin-top:0.08in"]{gap:0.08in!important}'
             '.box[style*="justify-content:space-between;align-items:center;gap:0.2in"]{padding:0.04in 0.13in!important}')
CYR = ([("Nunito Cyrillic", w, "normal", f"nunito-latin-{w}-normal.woff2", "U+0000-00FF,U+2000-206F") for w in (400, 700, 800)]
       + [("Nunito Cyrillic", w, "normal", f"nunito-cyrillic-{w}-normal.woff2", None) for w in (400, 700, 800)])

LANG = build(dict(
    code="bg", folder="book-39-bulgarian", series_no=39, isbn="", draft=True,
    name="Bulgarian", native="български език", native_tr="BUL-gahr-skee eh-ZEEK", name_word="име", write_word="пиши",
    title_native="Моята първа азбука", title_letters="АаЪъЩщ", belongs_native="Тази книга е на",
    belongs_pic="star", alphabet_native="азбуката", numbers_native="числата", numbers_tr="chees-LAH-tah",
    phrases_native="Първи думи",
    extra_css=EXTRA_CSS,
    fonts=CYR, disp_family="Nunito Cyrillic", text_family="Nunito Cyrillic",
    glyph_font=["nunito-cyrillic-900-normal.woff2", "nunito-latin-900-normal.woff2"],
    font_credit="Nunito (Cyrillic and Black weights)",
    phon_feature="each letter’s Bulgarian name (А «а», Б «бъ», В «въ»…)",
    sections=[section(LETTERS, native="азбуката", native_tr="ahz-BOO-kah-tah — “the alphabet”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Bulgarian is written in the <b>Cyrillic</b> alphabet. It has <b>30 letters</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letter names with “uh”</h3>Bulgarian children call each consonant by its sound
plus the vowel <span class="nt"><b>Ъ</b></span> (‘uh’): <span class="nt">бъ, въ, гъ…</span> — <i>buh, vuh, guh…</i></div>
<div class="box" style="margin:0.1in 0"><h3>Some tricksters!</h3><span class="nt"><b>В Н Р С У Х</b></span> look like English letters,
but they say <i>v, n, r, s, oo, kh</i>. And <span class="nt"><b>Щ</b></span> says ‘sht’!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt"><b>Аа</b></span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>luh-ZHEE-tsah</i> means “say ZHEE a little louder”.",
        "<b>uh</b> is the Bulgarian vowel Ъ, like ‘u’ in “but” or ‘a’ in “sofa”.",
        "<b>kh</b> is a breathy sound from the throat, like ‘ch’ in Scottish “loch”; <b>zh</b> is the ‘s’ in “measure”.",
        "<b>r</b> is always rolled or tapped with the tip of the tongue.",
        "At the end of a word, a voiced sound often turns voiceless: <i>хляб</i> sounds like <i>khlyap</i>."],
    phon_explain="The box marked <i>Bulgarian letter name</i> shows the name Bulgarian children use for each letter "
                 "(Б is «бъ», Ъ is «ер голям»…) and a warning for letters that look like English ones but sound different.",
    standard="standard Bulgarian",
    hello=[
        ("Who speaks it?", "About <b>8 million people</b> speak Bulgarian.<sup>³</sup>"),
        ("Where?", "In <b>Bulgaria</b>, between the <b>Danube River</b> and the mountains of the south, by the <b>Black Sea</b>, "
                   "and by Bulgarian families in other countries."),
        ("How is it written?", "In the <b>Cyrillic alphabet</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>30 letters</b>. <span class=\"nt\"><b>Ъ</b></span> is a real vowel in Bulgarian."),
        ("“The” at the end!", "Bulgarian puts the word for “the” on the <b>end</b> of a word: <span class=\"nt\">книга</span> "
                              "(a book) becomes <span class=\"nt\">книгата</span> (the book)."),
        ("Did you know?", "Some Bulgarian words came from Arabic through Turkish: <span class=\"nt\">джамия</span> "
                          "(<i>mosque</i>) from <b>jāmiʿ</b>, and <span class=\"nt\">халва</span> (<i>halva</i>) from <i>ḥalwā</i>."),
    ],
    hello_pics=[("flower", {}), ("mountain", {}), ("mosque", {})],
    map=region_map(frame=[[21.0, 39.6], [30.4, 46.4]],
                   points=dict(sofia=[23.32, 42.70], plovdiv=[24.75, 42.15], varna=[27.91, 43.21],
                               burgas=[27.47, 42.50], ruse=[25.97, 43.85]),
                   area=None,
                   cities=[("sofia", "Sofia", -14, 8, "end", True), ("plovdiv", "Plovdiv", 0, 34, "middle", False),
                           ("varna", "Varna", -14, -8, "end", False), ("burgas", "Burgas", -14, 8, "end", False),
                           ("ruse", "Ruse", 0, -18, "middle", False)],
                   label="BULGARIA", label_at=[25.4, 43.0], marker=[25.5, 42.7],
                   caption="The circle shows Bulgaria on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Bulgarian is spoken in Sofia, "
                          "Plovdiv, Varna, Burgas, Ruse and in the towns and villages all around them.",
                   seas=[("Black Sea", 29.6, 42.4), ("Aegean Sea", 24.6, 39.9)], world_r=10),
    digits=[("0", "нула", "NOO-lah", "zero"), ("1", "едно", "ed-NO", "one"), ("2", "две", "dveh", "two"),
            ("3", "три", "tree", "three"), ("4", "четири", "CHEH-tee-ree", "four"), ("5", "пет", "pet", "five"),
            ("6", "шест", "shest", "six"), ("7", "седем", "SEH-dem", "seven"), ("8", "осем", "O-sem", "eight"),
            ("9", "девет", "DEH-vet", "nine")],
    phrases=[("Ас-саламу алейкум", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Уа алейкум ас-салам", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Здравей!", "zdrah-VAY", "Hello!"),
             ("Казвам се …", "KAHZ-vahm seh …", "My name is …"),
             ("Благодаря", "blah-go-dah-RYAH", "Thank you"),
             ("Джазакаллаху хайран", "jah-zah-kahl-LAH-hoo KHAI-rahn", "May Allah reward you with good"),
             ("мама · татко", "MAH-mah · TAHT-ko", "Mother · Father"),
             ("брат · сестра", "braht · ses-TRAH", "Brother · Sister"),
             ("да · не", "dah · neh", "Yes · No"),
             ("Уча български!", "OO-chah BUL-gahr-skee", "I am learning Bulgarian!")],
    cheer=("Машаллах! Браво!", "mah-shahl-LAH! BRAH-vo!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=BOOK,
    review_note="Check stress in морков (MOR-kov), the Arabic greeting spellings (Ас-саламу алейкум / Уа алейкум ас-салам, "
                "or the local Селям алейкум), ракета + rocket picture for Р, and the sound guides for Щ and Ь.",
    tiles="АБЖЩЪЯ", cover_pics=["apple", "ru_fir", "sun", "mosque"], title_size=46,
    speakers_blurb="Bulgarian is spoken by about 8 million people in Bulgaria and around the world.",
    sample_words=[("слънце", "SLUN-tseh", "sun"), ("звезда", "zvez-DAH", "star"), ("ябълка", "YAH-bul-kah", "apple")],
    keywords=["bulgarian alphabet book for kids", "learn bulgarian for children", "bulgarian azbuka coloring book",
              "cyrillic letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual bulgarian english toddlers"],
))
