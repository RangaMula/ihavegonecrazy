# -*- coding: utf-8 -*-
"""Book 43 - Tajik (Cyrillic script, 35 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Ҷҷ"). Fonts: Nunito (Cyrillic + Cyrillic Extended), SIL OFL."""
from generic import build, letter, section
from maps import region_map

# ---- fonts: Nunito Cyrillic + Cyrillic-ext (covers Ғ Ӣ Қ Ӯ Ҳ Ҷ) ------------------------------------
FAM = "Nunito Cyrillic"
_R = {"cyrillic": "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
      "cyrillic-ext": "U+0460-052F,U+1C80-1C8A,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F",
      "latin": None}
FONTS = [(FAM, w, "normal", f"nunito-{sub}-{w}-normal.woff2", rng)
         for sub, rng in _R.items() for w in (400, 700, 800)]
GLYPH = ["nunito-cyrillic-900-normal.woff2", "nunito-cyrillic-ext-900-normal.woff2", "nunito-latin-900-normal.woff2"]

PH = "Tajik letter name"
def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)

TG = "a Tajik letter!"
LETTERS = [
    L("А", "а", "a", "‘a’ as in “father” (short)", "анор", "a-NOR", "pomegranate", "pomegranate"),
    L("Б", "бе", "be", "‘b’ as in “ball”", "бодом", "bo-DOM", "almonds", "almond"),
    L("В", "ве", "ve", "‘v’ as in “van”", "велосипед", "ve-lo-si-PED", "bicycle", "kk_bicycle"),
    L("Г", "ге", "ge", "‘g’ as in “garden”", "гул", "gul", "flower", "flower"),
    L("Ғ", "ғе", "ghe", "a soft ‘g’ from the throat, like gentle gargling — " + TG, "ғалла", "ghal-LA", "grain, wheat", "paddy",
      rule="Г with a little line: Ғ."),
    L("Д", "де", "de", "‘d’ as in “dog”", "дарахт", "da-RAKHT", "tree", "tree"),
    L("Е", "е", "ye", "‘e’ as in “bed” (‘ye’ at the start of a word)", "себ", "seb", "apple", "apple",
      note="Е seldom starts a Tajik word. Find it in the middle of <i>себ</i>!"),
    L("Ё", "ё", "yo", "‘yo’ as in “yogurt”", "ёқут", "yo-QUT", "ruby", "kk_gem"),
    L("Ж", "же", "zhe", "‘zh’ like the ‘s’ in “measure”", "жола", "zho-LA", "hail (icy rain)", "raincloud"),
    L("З", "зе", "ze", "‘z’ as in “zoo”", "зайтун", "zay-TUN", "olive", "olive"),
    L("И", "и", "i", "‘i’ as in “sit” (‘ee’ when stressed)", "иморат", "i-mo-RAT", "building", "building"),
    L("Ӣ", "ӣ", "ee", "a long, stressed ‘ee’ at the end of a word — " + TG, "сабзӣ", "sab-ZEE", "carrot", "carrot",
      note="Ӣ never starts a word. It sits at the <b>end</b> of words: <i>сабзӣ, тоҷикӣ</i>."),
    L("Й", "й", "y", "‘y’ as in “boy”", "чой", "choy", "tea", "teacup",
      note="Й seldom starts a Tajik word. Find it at the end of <i>чой</i>!"),
    L("К", "ка", "ka", "‘k’ as in “kite”", "китоб", "ki-TOB", "book", "book", dict(left="А Б В", right="Г Ғ Д")),
    L("Қ", "қоф", "qof", "a deep ‘k’ from the back of the throat — " + TG, "қалам", "qa-LAM", "pen", "pen",
      rule="К with a little tail: Қ."),
    L("Л", "эл", "el", "‘l’ as in “lamp”", "лимӯ", "li-MÖ", "lemon", "lemon"),
    L("М", "эм", "em", "‘m’ as in “moon”", "масҷид", "mas-JID", "mosque", "mosque"),
    L("Н", "эн", "en", "‘n’ as in “nest”", "нон", "non", "bread", "roti"),
    L("О", "о", "o", "‘o’ as in “more” — a round ‘aw’", "об", "ob", "water", "water"),
    L("П", "пе", "pe", "‘p’ as in “pen”", "пиёз", "pi-YOZ", "onion", "onion"),
    L("Р", "эр", "er", "a rolled ‘r’ — let your tongue buzz!", "рангинкамон", "ran-gin-ka-MON", "rainbow", "rainbow"),
    L("С", "эс", "es", "‘s’ as in “sun”", "соат", "so-AT", "clock", "clock"),
    L("Т", "те", "te", "‘t’ as in “tap”", "тарбуз", "tar-BUZ", "watermelon", "watermelon"),
    L("У", "у", "u", "‘oo’ as in “moon”", "уфуқ", "u-FUQ", "horizon", "sunrise"),
    L("Ӯ", "ӯ", "ö", "like ‘u’ in “fur”, with rounded lips — " + TG, "тӯб", "töb", "ball", "ball",
      note="Ӯ usually sits inside a word. Find it in the middle of <i>тӯб</i>!"),
    L("Ф", "эф", "ef", "‘f’ as in “fan”", "фонус", "fo-NUS", "lantern", "eid"),
    L("Х", "хе", "khe", "‘kh’ — a raspy ‘h’, as in Scottish “loch”", "хурмо", "khur-MO", "dates", "dates"),
    L("Ҳ", "ҳе", "he", "‘h’ as in “hat” — " + TG, "ҳилол", "hi-LOL", "new crescent moon", "moon",
      rule="Х with a little tail: Ҳ."),
    L("Ч", "че", "che", "‘ch’ as in “chair”", "чатр", "chatr", "umbrella", "umbrella"),
    L("Ҷ", "ҷе", "je", "‘j’ as in “jam” — " + TG, "ҷойнамоз", "joy-na-MOZ", "prayer mat", "prayermat",
      rule="Ч with a little tail: Ҷ."),
    L("Ш", "ше", "she", "‘sh’ as in “ship”", "шафтолу", "shaf-to-LU", "peach", "kk_apricot"),
    L("Ъ", "аломати ҷудоӣ", "a-lo-ma-TI ju-do-EE", "no sound of its own! It marks a tiny stop or a longer vowel", "Қуръон", "qur-ON", "the Qur’an", "kk_rehal",
      note="Ъ (the separating sign) never starts a word. In <i>Қуръон</i> it shows a little catch in the voice, like the ‘ʾ’ in Arabic <i>Qurʾān</i>."),
    L("Э", "э", "e", "‘e’ as in “egg”", "элак", "e-LAK", "sieve", "kk_sieve"),
    L("Ю", "ю", "yu", "‘yu’ as in “you”", "юнучқа", "yu-nuch-QA", "alfalfa (clover)", "kk_clover"),
    L("Я", "я", "ya", "‘ya’ as in “yard”", "ях", "yakh", "ice", "ice"),
]

LANG = build(dict(
    code="tg", folder="book-43-tajik", series_no=43, isbn="", draft=True,
    name="Tajik", native="забони тоҷикӣ", native_tr="za-bo-NI to-ji-KEE", name_word="ном", write_word="навис",
    title_native="Алифбои аввалини ман", title_letters="ҒӢҚӮҲҶ", belongs_native="Соҳиби ин китоб",
    belongs_pic="star", alphabet_native="алифбо", numbers_native="рақамҳо", numbers_tr="ra-qam-HO",
    phrases_native="Аввалин калимаҳо",
    fonts=FONTS, disp_family=FAM, text_family=FAM, glyph_font=GLYPH,
    font_credit="Nunito (Cyrillic and Cyrillic Extended)",
    phon_feature="each letter’s Tajik name (А «а», Б «бе», Қ «қоф»…)",
    sections=[section(LETTERS, native="алифбо", native_tr="a-lif-BO — “the alphabet”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Tajik is written with <b>35 Cyrillic letters</b>. Six of them are special Tajik letters:
<b>Ғ Ӣ Қ Ӯ Ҳ Ҷ</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letters with a little mark</h3>Look closely! Each special letter is a familiar letter with
a small line, tail or bar: <b>Г–Ғ</b>, <b>И–Ӣ</b>, <b>К–Қ</b>, <b>У–Ӯ</b>, <b>Х–Ҳ</b>, <b>Ч–Ҷ</b>. The little mark changes the sound.</div>
<div class="box" style="margin:0.1in 0"><h3>A Persian language</h3>Tajik is a form of <b>Persian</b>. Many words are shared with Persian
and Dari, and many come from Arabic: <i>китоб</i> (book), <i>масҷид</i> (mosque), <i>Қуръон</i>.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ҷҷ</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable. Tajik words are usually stressed on the <b>last</b> syllable: <i>a-NOR</i>.",
        "<b>o</b> = a round ‘aw’ as in “more” · <b>ö</b> = Tajik <b>Ӯ</b>, like ‘u’ in “fur” with round lips · <b>ee</b> = Tajik <b>Ӣ</b>, a long ‘ee’.",
        "<b>q</b> = a deep ‘k’ from the throat · <b>gh</b> = a soft, gargled ‘g’ · <b>kh</b> = ‘ch’ in Scottish “loch” · <b>h</b> = Tajik <b>Ҳ</b>.",
        "<b>j</b> = ‘j’ in “jam” (Tajik <b>Ҷ</b>) · <b>zh</b> = ‘s’ in “measure”."],
    phon_explain="The box marked <i>Tajik letter name</i> shows the capital and small letter and the name Tajik children use for it "
                 "(Б is «бе», Қ is «қоф»…), plus a tip for the letters that carry a little mark.",
    standard="standard Tajik as taught in schools in Tajikistan",
    hello=[
        ("Who speaks it?", "About <b>9 million people</b> speak Tajik.<sup>³</sup>"),
        ("Where?", "Mostly in <b>Tajikistan</b>, a land of high mountains in Central Asia, and in Tajik communities in nearby lands."),
        ("How is it written?", "In <b>Cyrillic letters</b>, from <b>left to right</b>. Tajik is a form of <b>Persian</b>, which in other "
                               "lands is written in Arabic letters, from right to left."),
        ("How many letters?", "<b>35 letters</b>, with six special ones: <b>Ғ Ӣ Қ Ӯ Ҳ Ҷ</b>."),
        ("The Roof of the World", "Almost all of Tajikistan is <b>mountains</b>! Its high <b>Pamir</b> mountains are called "
                                  "“the Roof of the World”."),
        ("Did you know?", "Tajik children learn poems by <b>Rudaki</b>, called the father of Persian poetry, who lived more than 1,000 years ago."),
    ],
    hello_pics=[("mountain", {}), ("pomegranate", {}), ("mosque", {})],
    map=region_map(frame=[[48.0, 30.0], [80.0, 48.0]],
                   points=dict(dushanbe=[68.78, 38.56], khujand=[69.62, 40.28], kulob=[69.78, 37.91], khorog=[71.55, 37.49]),
                   area=(70.6, 38.9, 165, 115), cities=[("dushanbe", "Dushanbe", -14, 8, "end", False), ("khujand", "Khujand", 14, 8, "start", False),
                                                      ("kulob", "Kulob", -12, 28, "end", False), ("khorog", "Khorog", 14, 8, "start", False)],
                   label="CENTRAL ASIA", label_at=[62.0, 44.0], marker=[70.0, 38.8],
                   caption="The circle shows Tajikistan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b>, the mountains <b>brown</b> · the sea <b>blue</b>. <b>Find it:</b> Tajik is "
                          "spoken in Dushanbe, Khujand, Kulob and Khorog, high in the mountains of Central Asia.",
                   seas=[("Caspian Sea", 51.3, 40.8)], world_r=14),
    digits=[("0", "сифр", "sifr", "zero"), ("1", "як", "yak", "one"), ("2", "ду", "du", "two"), ("3", "се", "se", "three"),
            ("4", "чор", "chor", "four"), ("5", "панҷ", "panj", "five"), ("6", "шаш", "shash", "six"), ("7", "ҳафт", "haft", "seven"),
            ("8", "ҳашт", "hasht", "eight"), ("9", "нӯҳ", "nöh", "nine")],
    phrases=[("Ассалому алайкум", "as-sa-LO-mu a-LAY-kum", "Peace be upon you (the Muslim greeting)"),
             ("Ваалайкум ассалом", "va-a-LAY-kum as-sa-LOM", "And upon you be peace (the reply)"),
             ("Салом!", "sa-LOM", "Hello!"),
             ("Номи ман … аст", "no-MI man … ast", "My name is …"),
             ("Раҳмат", "rah-MAT", "Thank you"),
             ("Ҷазокаллоҳу хайрон", "ja-zo-KAL-lo-hu khay-RON", "May Allah reward you with good"),
             ("модар · падар", "mo-DAR · pa-DAR", "Mother · Father"),
             ("бародар · хоҳар", "ba-ro-DAR · kho-HAR", "Brother · Sister"),
             ("ҳа · не", "ha · ne", "Yes · No"),
             ("Ман забони тоҷикиро меомӯзам!", "man za-bo-NI to-ji-ki-RO me-o-mö-ZAM", "I am learning Tajik!")],
    cheer=("Машоллоҳ! Офарин!", "ma-shol-LOH! o-fa-RIN!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="А Б В", right="Г Ғ Д"),
    review_note=("Check first: the Tajik letter names (бе/ве/ге…, «қоф», the names of Й, Ӣ, Ӯ and Ъ), the words for "
                 "Ж (жола), Э (элак), Ю (юнучқа), У (уфуқ), Ш (шафтолу) and В (велосипед), the transliteration of Ӯ as ‘ö’, "
                 "the stress marks, the spelling of the greeting pair and «Ҷазокаллоҳу хайрон», and «Ман забони тоҷикиро меомӯзам!»."),
    tiles="ҒӢҚӮҲҶ", cover_pics=["pomegranate", "kk_gem", "watermelon", "mosque"], title_size=48,
    speakers_blurb="Tajik, a form of Persian, is spoken by about 9 million people, mostly in the high mountain land of Tajikistan.",
    sample_words=[("анор", "a-NOR", "pomegranate"), ("ҷойнамоз", "joy-na-MOZ", "prayer mat"), ("тарбуз", "tar-BUZ", "watermelon")],
    keywords=["tajik alphabet book for kids", "learn tajik for children", "tajik cyrillic letters coloring",
              "tajik persian letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual tajik english toddlers"],
))
