# -*- coding: utf-8 -*-
"""Book 41 - Kazakh (Cyrillic script, 42 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Әә"). Fonts: Nunito (Cyrillic + Cyrillic Extended), SIL OFL."""
from generic import build, letter, section
from maps import region_map

# ---- fonts: Nunito Cyrillic + Cyrillic-ext (covers Ә Ғ Қ Ң Ө Ұ Ү Һ І) --------------------------------
FAM = "Nunito Cyrillic"
_R = {"cyrillic": "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
      "cyrillic-ext": "U+0460-052F,U+1C80-1C8A,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F",
      "latin": None}
FONTS = [(FAM, w, "normal", f"nunito-{sub}-{w}-normal.woff2", rng)
         for sub, rng in _R.items() for w in (400, 700, 800)]
GLYPH = ["nunito-cyrillic-900-normal.woff2", "nunito-cyrillic-ext-900-normal.woff2", "nunito-latin-900-normal.woff2"]

PH = "Kazakh letter name"
def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)

KZ = "a Kazakh letter!"
LOAN = "used mostly in words borrowed from other languages"
LETTERS = [
    L("А", "а", "a", "‘a’ as in “father”", "алма", "al-MA", "apple", "apple"),
    L("Ә", "ә", "ä", "‘a’ as in “cat” — " + KZ, "әліппе", "ä-lip-PE", "ABC book", "book", dict(left="А Ә Б", right="В Г Ғ"),
      rule="Ә is the soft partner of А."),
    L("Б", "бэ", "be", "‘b’ as in “ball”", "бал", "bal", "honey", "honey"),
    L("В", "вэ", "ve", "‘v’ as in “van” — " + LOAN, "велосипед", "ve-lo-si-PED", "bicycle", "kk_bicycle"),
    L("Г", "гэ", "ge", "‘g’ as in “garden”", "гүл", "gül", "flower", "flower"),
    L("Ғ", "ғы", "ghuh", "a soft ‘g’ from the throat, like gentle gargling — " + KZ, "ғимарат", "ghi-ma-RAT", "building", "building",
      rule="Ғ is the deep partner of Г."),
    L("Д", "дэ", "de", "‘d’ as in “dog”", "доп", "dop", "ball", "ball"),
    L("Е", "е", "ye", "‘ye’ as in “yes” at the start of a word, ‘e’ as in “bed” inside it", "емен", "ye-MEN", "oak tree", "tree"),
    L("Ё", "ё", "yo", "‘yo’ as in “yogurt” — " + LOAN, "ёлка", "YOL-ka", "fir tree", "kk_fir",
      note="Ё comes only in borrowed words like <i>ёлка</i>."),
    L("Ж", "жэ", "zhe", "‘zh’ like the ‘s’ in “measure” (many people say ‘j’)", "жұлдыз", "zhul-DUHZ", "star", "star"),
    L("З", "зэ", "ze", "‘z’ as in “zoo”", "зәйтүн", "zäy-TÜN", "olive", "olive"),
    L("И", "и", "iy", "‘iy’ — like ‘ee’ in “see”", "ине", "i-NE", "needle", "kk_needle"),
    L("Й", "қысқа и", "quhs-QA iy", "‘y’ as in “boy” (a short ‘i’)", "ай", "ay", "moon", "moon",
      note="Й hardly ever starts a Kazakh word. Find it at the end of <i>ай</i>!"),
    L("К", "ка", "ka", "‘k’ as in “kite”", "күн", "kün", "sun", "sun"),
    L("Қ", "қа", "qa", "a deep ‘k’ from the back of the throat — " + KZ, "қарбыз", "qar-BUHZ", "watermelon", "watermelon",
      rule="Қ is the deep partner of К."),
    L("Л", "эл", "el", "‘l’ as in “lamp”", "лимон", "li-MON", "lemon", "lemon"),
    L("М", "эм", "em", "‘m’ as in “moon”", "мешіт", "me-SHIT", "mosque", "mosque"),
    L("Н", "эн", "en", "‘n’ as in “nest”", "нан", "nan", "bread", "roti"),
    L("Ң", "ың", "uhng", "‘ng’ as in “sing” — " + KZ, "теңіз", "te-NGIZ", "sea", "waves",
      note="Ң never starts a word. Find it in the middle of <i>теңіз</i>!"),
    L("О", "о", "o", "‘o’ as in “more” (short and round)", "орамал", "o-ra-MAL", "headscarf", "scarf"),
    L("Ө", "ө", "ö", "like ‘u’ in “fur”, with rounded lips — " + KZ, "өрік", "ö-RIK", "apricot", "kk_apricot"),
    L("П", "пэ", "pe", "‘p’ as in “pen”", "пияз", "pi-YAZ", "onion", "onion"),
    L("Р", "эр", "er", "a rolled ‘r’ — let your tongue buzz!", "Рамазан", "ra-ma-ZAN", "Ramadan, the month of fasting", "iftar"),
    L("С", "эс", "es", "‘s’ as in “sun”", "су", "su", "water", "water"),
    L("Т", "тэ", "te", "‘t’ as in “tap”", "тау", "taw", "mountain", "mountain"),
    L("У", "у", "u", "‘w’ after a vowel, ‘uw’ (like “oo”) at the start of a word", "уақыт", "wa-QUHT", "time", "clock"),
    L("Ұ", "ұ", "u", "short ‘u’ as in “put” — " + KZ, "ұшақ", "u-SHAQ", "aeroplane", "plane"),
    L("Ү", "ү", "ü", "‘ee’ said with rounded lips, like German ü — " + KZ, "үй", "üy", "house", "house"),
    L("Ф", "эф", "ef", "‘f’ as in “fan” — " + LOAN, "фонарь", "fo-NAR", "lantern", "eid"),
    L("Х", "ха", "kha", "‘kh’ — a raspy ‘h’, as in Scottish “loch”", "хат", "khat", "letter (to post)", "envelope"),
    L("Һ", "һа", "ha", "‘h’ as in “hat” — " + KZ, "гауһар", "gaw-HAR", "diamond", "kk_gem",
      note="Һ comes in a few words from Arabic and Persian. Find it inside <i>гауһар</i>!"),
    L("Ц", "цэ", "tse", "‘ts’ as in “cats” — " + LOAN, "цифр", "tsifr", "digit (a number sign)", "one", dict(digit="1")),
    L("Ч", "че", "che", "‘ch’ as in “chair” — " + LOAN, "чемодан", "che-mo-DAN", "suitcase", "kk_suitcase"),
    L("Ш", "ша", "sha", "‘sh’ as in “ship”", "шай", "shay", "tea", "teacup"),
    L("Щ", "ща", "shcha", "a long, soft ‘sh-ch’ — " + LOAN, "щетка", "SHCHYOT-ka", "brush", "kk_brush",
      note="Щ comes only in a few borrowed words."),
    L("Ъ", "айыру белгісі", "a-yuh-RU bel-gi-SI", "no sound! The hard sign keeps two sounds apart", "подъезд", "pod-YEZD", "entrance of a building", "door",
      note="Ъ (the hard sign) never starts a word and has no sound of its own. It sits inside a few borrowed words like <i>подъезд</i>."),
    L("Ы", "ы", "uh", "‘uh’ — like the ‘e’ in “the”, said deep in the mouth", "ыдыс", "uh-DUHS", "pot, dish", "pot"),
    L("І", "і", "i", "short ‘i’ as in “sit” — " + KZ, "інжір", "in-ZHIR", "fig", "fig",
      rule="І is the soft partner of Ы."),
    L("Ь", "жіңішкелік белгісі", "zhi-ngish-ke-LIK bel-gi-SI", "no sound! The soft sign makes the letter before it soft", "пальма", "PAL-ma", "palm tree", "kk_palm",
      note="Ь (the soft sign) never starts a word. It sits inside borrowed words like <i>пальма</i>."),
    L("Э", "э", "e", "‘e’ as in “egg” — " + LOAN, "электр шамы", "e-LEKTR sha-MUH", "light bulb", "bulb"),
    L("Ю", "ю", "yu", "‘yu’ as in “you”", "ою", "o-YU", "ornament, pattern", "kk_ornament",
      note="Ю hardly ever starts a Kazakh word. Find it at the end of <i>ою</i> — the beautiful patterns on Kazakh felt rugs!"),
    L("Я", "я", "ya", "‘ya’ as in “yard”", "қияр", "qi-YAR", "cucumber", "kk_cucumber",
      note="Я hardly ever starts a Kazakh word. Find it in the middle of <i>қияр</i>!"),
]

LANG = build(dict(
    code="kk", folder="book-41-kazakh", series_no=41, isbn="", draft=True,
    name="Kazakh", native="қазақ тілі", native_tr="qa-ZAQ ti-LI", name_word="атауы", write_word="жаз",
    title_native="Менің алғашқы әліппем", title_letters="ӘҒҚҢӨҰ", belongs_native="Бұл кітаптың иесі",
    belongs_pic="star", alphabet_native="әліпби", numbers_native="сандар", numbers_tr="san-DAR",
    phrases_native="Алғашқы сөздер",
    fonts=FONTS, disp_family=FAM, text_family=FAM, glyph_font=GLYPH,
    font_credit="Nunito (Cyrillic and Cyrillic Extended)",
    phon_feature="each letter’s Kazakh name (А «а», Б «бэ», Ғ «ғы»…)",
    sections=[section(LETTERS, native="әліпби", native_tr="ä-lip-BI — “the alphabet”",
                      chart_cols=7, warmup_cols=7,
                      intro_html="""<p>Kazakh is written with <b>42 Cyrillic letters</b>: the 33 letters of the Russian alphabet
plus <b>9 letters of its own</b>: <b>Ә Ғ Қ Ң Ө Ұ Ү Һ І</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Soft and deep partners</h3>Many Kazakh letters come in pairs: a <b>soft</b> one made at the
front of the mouth and a <b>deep</b> one made further back: <b>Ә–А</b>, <b>Ө–О</b>, <b>Ү–Ұ</b>, <b>І–Ы</b>, <b>К–Қ</b>, <b>Г–Ғ</b>.
A Kazakh word usually keeps all its vowels soft (<i>күн, інжір</i>) or all deep (<i>алма, қарбыз</i>).</div>
<div class="box" style="margin:0.1in 0"><h3>Borrowed-word letters</h3><b>В Ё Ф Х Һ Ц Ч Щ Ъ Ь Э</b> come mostly in words that Kazakh borrowed
from Russian, Arabic and Persian. They are still part of the alphabet, so we learn them too!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Әә</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable. Kazakh words are usually stressed on the <b>last</b> syllable: <i>al-MA</i>.",
        "<b>ä</b> = ‘a’ in “cat” · <b>ö</b> = ‘u’ in “fur” with round lips · <b>ü</b> = ‘ee’ with round lips · <b>uh</b> = a deep ‘uh’.",
        "<b>q</b> = a deep ‘k’ from the throat · <b>gh</b> = a soft, gargled ‘g’ · <b>ng</b> = ‘ng’ in “sing” · <b>kh</b> = ‘ch’ in Scottish “loch”.",
        "<b>zh</b> = ‘s’ in “measure” · <b>w</b> = Kazakh <b>У</b> after a vowel: <i>тау</i> = <i>taw</i>."],
    phon_explain="The box marked <i>Kazakh letter name</i> shows the capital and small letter and the name Kazakh children use for it "
                 "(Б is «бэ», Ң is «ың»…), plus a tip when the letter has a soft or deep partner.",
    standard="standard Kazakh as taught in schools in Kazakhstan",
    hello=[
        ("Who speaks it?", "About <b>16 million people</b> speak Kazakh.<sup>³</sup>"),
        ("Where?", "Mostly in <b>Kazakhstan</b>, the wide land of the Great Steppe in Central Asia, and in Kazakh communities in nearby countries."),
        ("How is it written?", "In <b>Cyrillic letters</b>, from <b>left to right</b>. Kazakhstan is also moving, step by step, to a "
                               "<b>new Latin alphabet</b>: <i>Қазақ</i> is written <i>Qazaq</i>."),
        ("How many letters?", "<b>42 letters</b>: 33 Russian Cyrillic letters plus 9 Kazakh ones: <b>Ә Ғ Қ Ң Ө Ұ Ү Һ І</b>."),
        ("A Turkic language", "Kazakh is a cousin of Tatar, Kyrgyz, Uzbek and Turkish: <i>алма</i> (apple) and <i>тау</i> (mountain) "
                              "sound almost the same in many of them!"),
        ("Did you know?", "Kazakh has many words from Arabic: <i>кітап</i> (book, from <i>kitāb</i>), <i>мешіт</i> (mosque, from "
                          "<i>masjid</i>) and <i>рақмет</i> (thank you, from <i>raḥma</i>, mercy)."),
    ],
    hello_pics=[("mountain", {}), ("apple", {}), ("mosque", {})],
    map=region_map(frame=[[46.0, 38.0], [88.0, 56.0]],
                   points=dict(astana=[71.45, 51.17], almaty=[76.95, 43.25], shymkent=[69.60, 42.32], atyrau=[51.92, 47.10]),
                   area=(67.0, 48.0, 450, 240), cities=[("astana", "Astana", 14, 8, "start", False), ("almaty", "Almaty", 14, 8, "start", False),
                                                     ("shymkent", "Shymkent", -14, 8, "end", False), ("atyrau", "Atyrau", 14, -8, "start", False)],
                   label="THE GREAT STEPPE", label_at=[66.0, 48.5], marker=[67.0, 48.0],
                   caption="The circle shows Kazakhstan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> and <b>yellow</b> like the steppe · the sea <b>blue</b>. <b>Find it:</b> Kazakh is "
                          "spoken in Astana, Almaty, Shymkent, Atyrau and all across the wide steppe of Central Asia.",
                   seas=[("Caspian Sea", 51.6, 42.4)], world_r=16),
    digits=[("0", "нөл", "nöl", "zero"), ("1", "бір", "bir", "one"), ("2", "екі", "ye-KI", "two"), ("3", "үш", "üsh", "three"),
            ("4", "төрт", "tört", "four"), ("5", "бес", "bes", "five"), ("6", "алты", "al-TUH", "six"), ("7", "жеті", "zhe-TI", "seven"),
            ("8", "сегіз", "se-GIZ", "eight"), ("9", "тоғыз", "to-GHUHZ", "nine")],
    phrases=[("Ассалаумағалейкум", "as-sa-law-ma-gha-ley-KUM", "Peace be upon you (the Muslim greeting)"),
             ("Уағалейкумассалам", "wa-gha-ley-kum-as-sa-LAM", "And upon you be peace (the reply)"),
             ("Сәлеметсіз бе!", "sä-le-MET-siz be", "Hello!"),
             ("Менің атым …", "me-NING a-TUHM …", "My name is …"),
             ("Рақмет", "raq-MET", "Thank you"),
             ("Жазакаллаһу хайран", "ja-za-KAL-la-hu khay-RAN", "May Allah reward you with good"),
             ("ана · әке", "a-NA · ä-KE", "Mother · Father"),
             ("аға · әпке", "a-GHA · äp-KE", "Big brother · Big sister"),
             ("иә · жоқ", "i-YÄ · zhoq", "Yes · No"),
             ("Мен қазақ тілін үйреніп жүрмін!", "men qa-ZAQ ti-LIN üy-re-NIP zhür-MIN", "I am learning Kazakh!")],
    cheer=("Машаллаһ! Жарайсың!", "ma-SHAL-lah! zha-ray-SUHNG!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="А Ә Б", right="В Г Ғ"),
    review_note=("Check first: the Kazakh letter names (бэ/вэ/гэ…, «ғы», «қа», «ың», the names of Ъ and Ь), the words for "
                 "В (велосипед), Ё (ёлка), Ц (цифр), Ч (чемодан), Щ (щетка), Ъ (подъезд), Ь (пальма), Э (электр шамы) and Ю (ою), "
                 "the stress marks, the spelling of the greeting pair and «Жазакаллаһу хайран», and the sentence «Мен қазақ тілін үйреніп жүрмін!»."),
    tiles="АӘҒҚҢҰ", cover_pics=["apple", "kk_bicycle", "watermelon", "mosque"], title_size=48,
    speakers_blurb="Kazakh is spoken by about 16 million people, mostly in Kazakhstan, the land of the Great Steppe.",
    sample_words=[("алма", "al-MA", "apple"), ("қарбыз", "qar-BUHZ", "watermelon"), ("жұлдыз", "zhul-DUHZ", "star")],
    keywords=["kazakh alphabet book for kids", "learn kazakh for children", "kazakh cyrillic letters coloring",
              "kazakh letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual kazakh english toddlers"],
))
