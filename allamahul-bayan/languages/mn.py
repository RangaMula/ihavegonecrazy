# -*- coding: utf-8 -*-
"""Book 44 - Mongolian (Cyrillic script, 35 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Өө"). Fonts: Nunito (Cyrillic + Cyrillic Extended), SIL OFL."""
from generic import build, letter, section
from maps import region_map

# ---- fonts: Nunito Cyrillic + Cyrillic-ext (covers Ө Ү) --------------------------------------------
FAM = "Nunito Cyrillic"
_R = {"cyrillic": "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
      "cyrillic-ext": "U+0460-052F,U+1C80-1C8A,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F",
      "latin": None}
FONTS = [(FAM, w, "normal", f"nunito-{sub}-{w}-normal.woff2", rng)
         for sub, rng in _R.items() for w in (400, 700, 800)]
GLYPH = ["nunito-cyrillic-900-normal.woff2", "nunito-cyrillic-ext-900-normal.woff2", "nunito-latin-900-normal.woff2"]

PH = "Mongolian letter name"
def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)

MN = "a Mongolian letter!"
LOAN = "used only in words borrowed from other languages"
LETTERS = [
    L("А", "а", "a", "‘a’ as in “father”", "алим", "a-lim", "apple", "apple"),
    L("Б", "бэ", "be", "‘b’ as in “ball”", "бөмбөг", "böm-bög", "ball", "ball"),
    L("В", "вэ", "ve", "a soft ‘v’, almost a ‘w’", "ваар", "vaar", "vase", "kk_vase"),
    L("Г", "гэ", "ge", "‘g’ as in “garden” (deeper next to а, о, у)", "гэр", "ger", "ger — a round felt home", "kk_ger"),
    L("Д", "дэ", "de", "‘d’ as in “dog”", "дугуй", "du-gui", "bicycle (“wheel”)", "kk_bicycle"),
    L("Е", "е", "ye", "‘ye’ as in “yes” (or ‘yö’ in round-vowel words)", "ес", "yös", "nine", "one", dict(digit="9")),
    L("Ё", "ё", "yo", "‘yo’ as in “yonder”", "ёотон", "yoo-ton", "sugar cubes", "ice"),
    L("Ж", "жэ", "je", "‘j’ as in “jam”", "жимс", "jims", "fruit", "pear"),
    L("З", "зэ", "dze", "‘dz’ as in “adze” — a ‘d’ and ‘z’ together", "зүү", "dzüü", "needle", "kk_needle"),
    L("И", "и", "i", "‘ee’ as in “see”", "илгээмж", "il-geemj", "parcel", "box"),
    L("Й", "хагас и", "kha-gas i", "‘y’ as in “boy” (a “half i”)", "цай", "tsai", "tea", "teacup",
      note="Й never starts a Mongolian word. Find it at the end of <i>цай</i>!"),
    L("К", "ка", "ka", "‘k’ as in “kite” — " + LOAN, "кран", "kran", "tap, faucet", "tap"),
    L("Л", "эл", "el", "a breathy ‘l’: put your tongue for ‘l’ and blow air past it", "лууван", "luu-van", "carrot", "carrot"),
    L("М", "эм", "em", "‘m’ as in “moon”", "мод", "mod", "tree", "tree"),
    L("Н", "эн", "en", "‘n’ as in “nest” (‘ng’ at the end of a word)", "нар", "nar", "sun", "sun"),
    L("О", "о", "o", "‘o’ as in “more” — a round ‘aw’", "од", "od", "star", "star"),
    L("Ө", "ө", "ö", "like ‘u’ in “fur”, with rounded lips — " + MN, "өндөг", "ön-dög", "egg", "egg",
      rule="Ө is the front partner of О."),
    L("П", "пэ", "pe", "‘p’ as in “pen” — " + LOAN, "помидор", "po-mi-dor", "tomato", "tomato"),
    L("Р", "эр", "er", "a rolled ‘r’ — let your tongue buzz!", "ракет", "ra-ket", "rocket", "kk_rocket",
      note="Р hardly ever starts a Mongolian word — <i>ракет</i> is a borrowed word."),
    L("С", "эс", "es", "‘s’ as in “sun”", "сар", "sar", "moon", "moon"),
    L("Т", "тэ", "te", "‘t’ as in “tap”, with a little puff of air", "тогоо", "to-goo", "cooking pot", "pot"),
    L("У", "у", "u", "‘oo’ as in “book”, said deep in the mouth", "уул", "uul", "mountain", "mountain"),
    L("Ү", "ү", "ü", "‘oo’ as in “moon”, said at the front of the mouth — " + MN, "үүл", "üül", "cloud", "clouds",
      rule="Ү is the front partner of У."),
    L("Ф", "фэ", "fe", "‘f’ as in “fan” — " + LOAN, "футболк", "fut-bolk", "T-shirt", "kk_shirt"),
    L("Х", "хэ", "khe", "‘kh’ — a raspy ‘h’, as in Scottish “loch”", "хаалга", "khaal-ga", "door", "door"),
    L("Ц", "цэ", "tse", "‘ts’ as in “cats”", "цонх", "tsonkh", "window", "window"),
    L("Ч", "чэ", "che", "‘ch’ as in “chair”", "чихэр", "chi-kher", "sweets, candy", "kk_candy"),
    L("Ш", "ша", "sha", "‘sh’ as in “ship”", "шүхэр", "shü-kher", "umbrella", "umbrella"),
    L("Щ", "щэ", "shche", "a long, soft ‘sh-ch’ — " + LOAN, "щётка", "shchyot-ka", "brush", "kk_brush",
      note="Щ comes only in a few borrowed words."),
    L("Ъ", "хатуугийн тэмдэг", "kha-tuu-giin tem-deg", "no sound! The hard sign keeps two sounds apart", "явъя", "yav-ya", "let’s go!", "kk_road",
      note="Ъ (the hard sign) never starts a word. Find it in <i>явъя!</i> — “let’s go!”"),
    L("Ы", "ы", "ii", "a long ‘ee’ — it comes only after hard letters", "номын сан", "no-miin san", "library (“treasure of books”)", "book",
      dict(left="А Б В", right="Г Д Е"),
      note="Ы never starts a word. It comes in word endings like <i>номын</i> (“of books”)."),
    L("Ь", "зөөлний тэмдэг", "dzööl-nii tem-deg", "a tiny ‘i’ sound, softening the letter before it", "толь", "toli", "mirror", "mirror",
      note="Ь (the soft sign) never starts a word. Find it at the end of <i>толь</i>!"),
    L("Э", "э", "e", "‘e’ as in “egg”", "эрдэнэ", "er-de-ne", "jewel, treasure", "kk_gem"),
    L("Ю", "ю", "yu", "‘yu’ as in “you”", "юүлүүр", "yuu-lüür", "funnel", "kk_funnel"),
    L("Я", "я", "ya", "‘ya’ as in “yard”", "ягаан цэцэг", "ya-gaan tse-tseg", "pink flower", "flower"),
]

LANG = build(dict(
    code="mn", folder="book-44-mongolian", series_no=44, isbn="", draft=True,
    name="Mongolian", native="монгол хэл", native_tr="mon-gol khel", name_word="нэр", write_word="бич",
    title_native="Миний анхны цагаан толгой", title_letters="АБВӨҮЯ", belongs_native="Энэ номын эзэн",
    belongs_pic="star", alphabet_native="цагаан толгой", numbers_native="тоо", numbers_tr="too",
    phrases_native="Анхны үгс",
    fonts=FONTS, disp_family=FAM, text_family=FAM, glyph_font=GLYPH,
    font_credit="Nunito (Cyrillic and Cyrillic Extended)",
    phon_feature="each letter’s Mongolian name (А «а», Б «бэ», Ө «ө»…)",
    sections=[section(LETTERS, native="цагаан толгой", native_tr="tsa-gaan tol-goi — “the alphabet” (“white head”)",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Mongolian is written with <b>35 Cyrillic letters</b>: the 33 letters of the Russian alphabet
plus <b>two letters of its own</b>: <b>Ө</b> and <b>Ү</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Double letters, long sounds</h3>Mongolian writes a long vowel with <b>two letters</b>:
<b>аа, ээ, оо, өө, уу, үү</b>. Hold them longer: <i>уул</i> (mountain), <i>үүл</i> (cloud), <i>тогоо</i> (pot).</div>
<div class="box" style="margin:0.1in 0"><h3>Back and front words</h3>Mongolian vowels come in families: <b>а о у</b> are said at the
back of the mouth and <b>э ө ү</b> at the front. A word keeps its vowels in one family: <i>алим, тогоо</i> · <i>өндөг, үүл</i>.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Өө</b>. Color both!</div>""")],
    sound_notes=[
        "<b>Doubled vowels are long</b>, just as Mongolian writes them: <i>uul</i> = “oool”. Words are said gently, with a light push on the first part.",
        "<b>ö</b> = Mongolian <b>Ө</b>, like ‘u’ in “fur” with round lips · <b>ü</b> = Mongolian <b>Ү</b>, ‘oo’ in “moon” · <b>u</b> = Mongolian <b>У</b>, a deeper ‘oo’.",
        "<b>kh</b> = ‘ch’ in Scottish “loch” · <b>dz</b> = Mongolian <b>З</b> · <b>j</b> = Mongolian <b>Ж</b> · <b>ts</b> = Mongolian <b>Ц</b>.",
        "Mongolian <b>Л</b> is a breathy ‘l’ (blow air past your tongue); <b>i</b> at the end, as in <i>toli</i>, is very short."],
    phon_explain="The box marked <i>Mongolian letter name</i> shows the capital and small letter and the name Mongolian children use for it "
                 "(Б is «бэ», Й is «хагас и» — “half i”…), plus a tip for Ө and Ү.",
    standard="standard (Khalkha) Mongolian as spoken in Mongolia",
    hello=[
        ("Who speaks it?", "About <b>6 million people</b> speak Mongolian.<sup>³</sup>"),
        ("Where?", "In <b>Mongolia</b>, a land of wide grassy steppes, high mountains and the <b>Gobi Desert</b>, and in nearby lands."),
        ("How is it written?", "In Mongolia, in <b>Cyrillic letters</b>, from <b>left to right</b>. Mongolian also has its own beautiful "
                               "<b>traditional script</b>, written in columns from <b>top to bottom</b>!"),
        ("How many letters?", "<b>35 letters</b>: 33 Russian Cyrillic letters plus 2 Mongolian ones: <b>Ө</b> and <b>Ү</b>."),
        ("“White head”", "Mongolian children call the alphabet <i>цагаан толгой</i> (<i>tsagaan tolgoi</i>) — “white head”!"),
        ("Did you know?", "Many Mongolian families live in a <b>гэр</b> (<i>ger</i>): a round home of wood and felt that can be packed up "
                          "and moved to fresh grass."),
    ],
    hello_pics=[("kk_ger", {}), ("mountain", {}), ("star", {})],
    map=region_map(frame=[[86.0, 34.0], [128.0, 54.0]],
                   points=dict(ulaanbaatar=[106.92, 47.92], erdenet=[104.04, 49.03], choibalsan=[114.53, 48.07], khovd=[91.64, 48.01]),
                   area=(103.8, 46.9, 400, 200),
                   cities=[("ulaanbaatar", "Ulaanbaatar", 14, 8, "start", False), ("erdenet", "Erdenet", -14, -6, "end", False),
                           ("choibalsan", "Choibalsan", 14, 8, "start", False), ("khovd", "Khovd", 14, 8, "start", False)],
                   label="THE STEPPE AND THE GOBI", label_at=[103.0, 44.2], marker=[104.0, 47.0],
                   caption="The circle shows Mongolia on the world map.",
                   legend="<b>Color it:</b> the steppe <b>green</b>, the Gobi Desert <b>yellow</b> · the sea <b>blue</b>. <b>Find it:</b> "
                          "Mongolian is spoken in Ulaanbaatar, Erdenet, Choibalsan, Khovd and all across the steppe.",
                   seas=[("Yellow Sea", 123.0, 35.6)], world_r=16),
    digits=[("0", "тэг", "teg", "zero"), ("1", "нэг", "neg", "one"), ("2", "хоёр", "kho-yor", "two"), ("3", "гурав", "gu-rav", "three"),
            ("4", "дөрөв", "dö-röv", "four"), ("5", "тав", "tav", "five"), ("6", "зургаа", "dzur-gaa", "six"), ("7", "долоо", "do-loo", "seven"),
            ("8", "найм", "naim", "eight"), ("9", "ес", "yös", "nine")],
    phrases=[("Ассаламу алейкум", "as-sa-la-mu a-ley-kum", "Peace be upon you (the Muslim greeting)"),
             ("Уалейкум ассалам", "wa-ley-kum as-sa-lam", "And upon you be peace (the reply)"),
             ("Сайн байна уу?", "sain bain-uu", "Hello! (How are you?)"),
             ("Миний нэр …", "mi-nii ner …", "My name is …"),
             ("Баярлалаа", "ba-yar-la-laa", "Thank you"),
             ("Жазакаллаху хайран", "ja-za-kal-la-khu khai-ran", "May Allah reward you with good"),
             ("ээж · аав", "eej · aav", "Mother · Father"),
             ("ах · эгч", "akh · egch", "Big brother · Big sister"),
             ("тийм · үгүй", "tiim · ü-güi", "Yes · No"),
             ("Би монгол хэл сурч байна!", "bi mon-gol khel surch bai-na", "I am learning Mongolian!")],
    cheer=("Машаллах! Мундаг!", "ma-shal-lakh! mun-dag!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="А Б В", right="Г Д Е"),
    review_note=("Check first: the Mongolian letter names (бэ/вэ/гэ…, «хагас и», «фэ», «щэ», the names of Ъ and Ь), the words for "
                 "Ё (ёотон), И (илгээмж), К (кран), Ф (футболк), Щ (щётка), Ъ (явъя), Ы (номын сан) and Ю (юүлүүр), "
                 "the transliterations (especially ес = ‘yös’ and the long vowels), the Mongolian spelling of the greeting pair and "
                 "«Жазакаллаху хайран», and the cheer «Мундаг!»."),
    tiles="АӨҮГЭЯ", cover_pics=["kk_ger", "apple", "kk_rocket", "umbrella"], title_size=46,
    speakers_blurb="Mongolian is spoken by about 6 million people, in the wide land of steppes, mountains and the Gobi Desert.",
    sample_words=[("гэр", "ger", "ger, a round felt home"), ("нар", "nar", "sun"), ("үүл", "üül", "cloud")],
    keywords=["mongolian alphabet book for kids", "learn mongolian for children", "mongolian cyrillic letters coloring",
              "mongolian letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual mongolian english toddlers"],
))
