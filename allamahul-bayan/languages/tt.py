# -*- coding: utf-8 -*-
"""Book 42 - Tatar (Cyrillic script, 39 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Әә"). Fonts: Nunito (Cyrillic + Cyrillic Extended), SIL OFL."""
from generic import build, letter, section
from maps import region_map

# ---- fonts: Nunito Cyrillic + Cyrillic-ext (covers Ә Ө Ү Җ Ң Һ) ------------------------------------
FAM = "Nunito Cyrillic"
_R = {"cyrillic": "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
      "cyrillic-ext": "U+0460-052F,U+1C80-1C8A,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F",
      "latin": None}
FONTS = [(FAM, w, "normal", f"nunito-{sub}-{w}-normal.woff2", rng)
         for sub, rng in _R.items() for w in (400, 700, 800)]
GLYPH = ["nunito-cyrillic-900-normal.woff2", "nunito-cyrillic-ext-900-normal.woff2", "nunito-latin-900-normal.woff2"]

PH = "Tatar letter name"
def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)

TT = "a Tatar letter!"
LOAN = "used mostly in words borrowed from other languages"
LETTERS = [
    L("А", "а", "a", "‘a’ as in “father”", "алма", "al-MA", "apple", "apple"),
    L("Ә", "ә", "ä", "‘a’ as in “cat” — " + TT, "Әлифба", "ä-lif-BA", "ABC book", "book", dict(left="А Ә Б", right="В Г Д"),
      rule="Ә is the soft partner of А."),
    L("Б", "бэ", "be", "‘b’ as in “ball”", "бал", "bal", "honey", "honey"),
    L("В", "вэ", "ve", "‘w’ in Tatar words, ‘v’ as in “van” in borrowed words", "велосипед", "ve-li-si-PED", "bicycle", "kk_bicycle"),
    L("Г", "гэ", "ge", "‘g’ as in “garden” (deeper, almost gargled, next to а, о, у, ы)", "гөл", "göl", "flower", "flower"),
    L("Д", "дэ", "de", "‘d’ as in “dog”", "дөнья", "dön-YA", "world", "globe"),
    L("Е", "е", "ye", "‘ye’ as in “yes” at the start of a word, ‘e’ as in “bed” inside it", "елга", "yel-GA", "river", "waves"),
    L("Ё", "ё", "yo", "‘yo’ as in “yogurt” — " + LOAN, "вертолёт", "ver-to-LYOT", "helicopter", "kk_helicopter",
      note="Ё comes only in borrowed words. Find it inside <i>вертолёт</i>!"),
    L("Ж", "жэ", "zhe", "‘zh’ like the ‘s’ in “measure” — " + LOAN, "журнал", "zhur-NAL", "magazine", "kk_magazine"),
    L("Җ", "җэ", "je", "‘j’ as in “jam”, said softly — " + TT, "җиләк", "ji-LÄK", "strawberry", "kk_strawberry"),
    L("З", "зэ", "ze", "‘z’ as in “zoo”", "зәйтүн", "zäy-TÜN", "olive", "olive"),
    L("И", "и", "i", "‘ee’ as in “see”", "ипи", "i-PI", "bread", "roti"),
    L("Й", "кыска и", "kuhs-KA i", "‘y’ as in “yes” or “boy”", "йолдыз", "yol-DUHZ", "star", "star"),
    L("К", "ка", "ka", "‘k’ as in “kite” (deeper, from the throat, next to а, о, у, ы)", "кояш", "ko-YASH", "sun", "sun"),
    L("Л", "эл", "el", "‘l’ as in “lamp”", "лимон", "li-MON", "lemon", "lemon"),
    L("М", "эм", "em", "‘m’ as in “moon”", "мәчет", "mä-CHET", "mosque", "mosque"),
    L("Н", "эн", "en", "‘n’ as in “nest”", "нарат", "na-RAT", "pine tree", "kk_fir"),
    L("Ң", "эң", "eng", "‘ng’ as in “sing” — " + TT, "таң", "tang", "dawn", "sunrise",
      note="Ң never starts a word. Find it at the end of <i>таң</i>!"),
    L("О", "о", "o", "‘o’ as in “more” (short and round)", "очкыч", "och-KUHCH", "aeroplane", "plane"),
    L("Ө", "ө", "ö", "like ‘u’ in “fur”, with rounded lips — " + TT, "өй", "öy", "house", "house",
      rule="Ө is the soft partner of О."),
    L("П", "пэ", "pe", "‘p’ as in “pen”", "помидор", "po-mi-DOR", "tomato", "tomato"),
    L("Р", "эр", "er", "a rolled ‘r’ — let your tongue buzz!", "Рамазан", "ra-ma-ZAN", "Ramadan, the month of fasting", "iftar"),
    L("С", "эс", "es", "‘s’ as in “sun”", "су", "su", "water", "water"),
    L("Т", "тэ", "te", "‘t’ as in “tap”", "тау", "taw", "mountain", "mountain"),
    L("У", "у", "u", "‘oo’ as in “put”; ‘w’ after a vowel", "урындык", "u-ruhn-DUHK", "chair, stool", "stool"),
    L("Ү", "ү", "ü", "‘ee’ said with rounded lips, like German ü — " + TT, "үсемлек", "ü-sem-LEK", "plant", "kk_sprout",
      rule="Ү is the soft partner of У."),
    L("Ф", "эф", "ef", "‘f’ as in “fan” — " + LOAN, "фонарь", "fo-NAR", "lantern", "eid"),
    L("Х", "ха", "kha", "‘kh’ — a raspy ‘h’, as in Scottish “loch”", "хат", "khat", "letter (to post)", "envelope"),
    L("Һ", "һэ", "he", "‘h’ as in “hat” — " + TT, "һава шары", "ha-VA sha-RUH", "balloon (an “air ball”)", "balloon"),
    L("Ц", "цэ", "tse", "‘ts’ as in “cats” — " + LOAN, "цифр", "tsifr", "digit (a number sign)", "one", dict(digit="1")),
    L("Ч", "чэ", "che", "a soft ‘ch’ (many Tatars say it almost like a soft ‘sh’)", "чәй", "chäy", "tea", "teacup"),
    L("Ш", "ша", "sha", "‘sh’ as in “ship”", "шакмак", "shak-MAK", "blocks, cubes", "blocks", dict(letters=("Ш", "Ә", "Җ"))),
    L("Щ", "ща", "shcha", "a long, soft ‘sh-ch’ — " + LOAN, "щётка", "SHCHYOT-ka", "brush", "kk_brush",
      note="Щ comes only in a few borrowed words."),
    L("Ъ", "калынлык билгесе", "ka-luhn-LUHK bil-ge-SE", "no sound of its own! In words from Arabic it marks a tiny stop", "Коръән", "kor-ÄN", "the Qur’an", "kk_rehal",
      note="Ъ (the hard sign) never starts a word. In <i>Коръән</i> it shows a little catch in the voice, like the ‘ʾ’ in Arabic <i>Qurʾān</i>."),
    L("Ы", "ы", "uh", "a short ‘uh’ — like the ‘e’ in “the”", "кыяр", "kuh-YAR", "cucumber", "kk_cucumber",
      note="Ы hardly ever starts a Tatar word. Find it in <i>кыяр</i>!"),
    L("Ь", "нечкәлек билгесе", "nech-kä-LEK bil-ge-SE", "no sound! The soft sign makes the sound before it soft", "сәгать", "sä-GAT", "clock", "clock",
      note="Ь (the soft sign) never starts a word. Find it at the end of <i>сәгать</i>!"),
    L("Э", "э", "e", "‘e’ as in “egg”", "энә", "e-NÄ", "needle", "kk_needle"),
    L("Ю", "ю", "yu", "‘yu’ as in “you”", "юкә", "yu-KÄ", "linden tree", "tree"),
    L("Я", "я", "ya", "‘ya’ as in “yard”", "яфрак", "yaf-RAK", "leaf", "kk_leaf"),
]

LANG = build(dict(
    code="tt", folder="book-42-tatar", series_no=42, isbn="", draft=True,
    name="Tatar", native="татар теле", native_tr="ta-TAR te-LE", name_word="исеме", write_word="яз",
    title_native="Минем беренче әлифбам", title_letters="ӘӨҮҖҢҺ", belongs_native="Бу китапның хуҗасы",
    belongs_pic="star", alphabet_native="әлифба", numbers_native="саннар", numbers_tr="san-NAR",
    phrases_native="Беренче сүзләр",
    fonts=FONTS, disp_family=FAM, text_family=FAM, glyph_font=GLYPH,
    font_credit="Nunito (Cyrillic and Cyrillic Extended)",
    phon_feature="each letter’s Tatar name (А «а», Б «бэ», Җ «җэ»…)",
    sections=[section(LETTERS, native="әлифба", native_tr="ä-lif-BA — “the alphabet”",
                      chart_cols=7, warmup_cols=7,
                      intro_html="""<p>Tatar is written with <b>39 Cyrillic letters</b>: the 33 letters of the Russian alphabet
plus <b>6 letters of its own</b>: <b>Ә Ө Ү Җ Ң Һ</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Hard and soft words</h3>Tatar vowels come in pairs: <b>hard</b> ones made at the back of the
mouth (<b>а о у ы</b>) and <b>soft</b> ones made at the front (<b>ә ө ү е</b>). A Tatar word usually keeps all its vowels hard
(<i>кояш, алма</i>) or all soft (<i>гөл, җиләк</i>).</div>
<div class="box" style="margin:0.1in 0"><h3>Borrowed-word letters</h3><b>Ё Ж Ф Ц Щ</b> come mostly in words that Tatar borrowed from
Russian and other languages. They are still part of the alphabet, so we learn them too!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Әә</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable. Tatar words are usually stressed on the <b>last</b> syllable: <i>al-MA</i>.",
        "<b>ä</b> = ‘a’ in “cat” · <b>ö</b> = ‘u’ in “fur” with round lips · <b>ü</b> = ‘ee’ with round lips · <b>uh</b> = a short ‘uh’.",
        "<b>ng</b> = ‘ng’ in “sing” · <b>kh</b> = ‘ch’ in Scottish “loch” · <b>zh</b> = ‘s’ in “measure” · <b>j</b> = a soft ‘j’ (Tatar <b>Җ</b>).",
        "<b>w</b> = Tatar <b>У</b> or <b>В</b> said like English ‘w’: <i>тау</i> = <i>taw</i>."],
    phon_explain="The box marked <i>Tatar letter name</i> shows the capital and small letter and the name Tatar children use for it "
                 "(Б is «бэ», Җ is «җэ»…), plus a tip when the letter has a hard or soft partner.",
    standard="standard (Kazan) Tatar",
    hello=[
        ("Who speaks it?", "About <b>5 million people</b> speak Tatar.<sup>³</sup>"),
        ("Where?", "In <b>Tatarstan</b>, on the great <b>Volga River</b>, where the city of <b>Kazan</b> stands, and in Tatar communities "
                   "in many other places."),
        ("How is it written?", "In <b>Cyrillic letters</b>, from <b>left to right</b>. In its long history Tatar has also been written in "
                               "<b>Arabic letters</b> and in <b>Latin letters</b>."),
        ("How many letters?", "<b>39 letters</b>: 33 Russian Cyrillic letters plus 6 Tatar ones: <b>Ә Ө Ү Җ Ң Һ</b>."),
        ("A Turkic language", "Tatar is a cousin of Kazakh, Bashkir, Uzbek and Turkish: <i>алма</i> (apple) and <i>тау</i> (mountain) "
                              "sound almost the same in many of them!"),
        ("Did you know?", "Islam reached the Volga lands in the year <b>922</b> — more than 1,100 years ago! So Tatar has many words from "
                          "Arabic: <i>китап</i> (book), <i>мәчет</i> (mosque) and <i>рәхмәт</i> (thank you, from <i>raḥma</i>, mercy)."),
    ],
    hello_pics=[("kk_strawberry", {}), ("apple", {}), ("mosque", {})],
    map=region_map(frame=[[30.0, 40.0], [70.0, 62.0]],
                   points=dict(kazan=[49.12, 55.79], chelny=[52.40, 55.74], ufa=[55.97, 54.74]),
                   area=(51.0, 55.4, 150, 90), cities=[("kazan", "Kazan", -14, 8, "end", False),
                                                     ("chelny", "Naberezhnye Chelny", 0, -18, "middle", False),
                                                     ("ufa", "Ufa", 14, 8, "start", False)],
                   label="THE VOLGA LANDS", label_at=[50.0, 50.5], marker=[50.0, 55.5],
                   caption="The circle shows Tatarstan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Tatar is spoken in Kazan "
                          "and Naberezhnye Chelny inside the dashed line, in Ufa nearby, and in Tatar communities far beyond.",
                   seas=[("Caspian Sea", 50.8, 42.6), ("Black Sea", 34.5, 43.2)], world_r=14),
    digits=[("0", "нуль", "nul", "zero"), ("1", "бер", "ber", "one"), ("2", "ике", "i-KE", "two"), ("3", "өч", "öch", "three"),
            ("4", "дүрт", "dürt", "four"), ("5", "биш", "bish", "five"), ("6", "алты", "al-TUH", "six"), ("7", "җиде", "ji-DE", "seven"),
            ("8", "сигез", "si-GEZ", "eight"), ("9", "тугыз", "tu-GUHZ", "nine")],
    phrases=[("Әссәламегаләйкем", "äs-sä-la-me-gä-läy-KEM", "Peace be upon you (the Muslim greeting)"),
             ("Вәгаләйкемәссәлам", "wä-gä-läy-ke-mäs-sä-LAM", "And upon you be peace (the reply)"),
             ("Исәнмесез!", "i-sän-me-SEZ", "Hello!"),
             ("Минем исемем …", "mi-NEM i-se-MEM …", "My name is …"),
             ("Рәхмәт", "räkh-MÄT", "Thank you"),
             ("Җәзакаллаһу хәйран", "jä-za-KAL-la-hu khäy-RAN", "May Allah reward you with good"),
             ("әни · әти", "ä-NI · ä-TI", "Mother · Father"),
             ("абый · апа", "a-BUHY · a-PA", "Big brother · Big sister"),
             ("әйе · юк", "ä-YE · yuk", "Yes · No"),
             ("Мин татар телен өйрәнәм!", "min ta-TAR te-LEN öy-rä-NÄM", "I am learning Tatar!")],
    cheer=("Машаллаһ! Афәрин!", "ma-SHAL-lah! a-fä-RIN!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="А Ә Б", right="В Г Д"),
    review_note=("Check first: the Tatar letter names (бэ/вэ/гэ…, «җэ», «эң», «һэ», the names of Й, Ъ and Ь), the words for "
                 "Ё (вертолёт), Ж (журнал), У (урындык), Ү (үсемлек), Ц (цифр), Ы (кыяр), Ь (сәгать) and Ю (юкә), "
                 "the description of Ч, the stress marks, the spelling of the greeting pair and «Җәзакаллаһу хәйран», and «Мин татар телен өйрәнәм!»."),
    tiles="ӘӨҮҖҢҺ", cover_pics=["apple", "kk_strawberry", "balloon", "mosque"], title_size=48,
    speakers_blurb="Tatar is spoken by about 5 million people, in Tatarstan on the Volga River and far beyond.",
    sample_words=[("алма", "al-MA", "apple"), ("җиләк", "ji-LÄK", "strawberry"), ("йолдыз", "yol-DUHZ", "star")],
    keywords=["tatar alphabet book for kids", "learn tatar for children", "tatar cyrillic letters coloring",
              "tatar letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual tatar english toddlers"],
))
