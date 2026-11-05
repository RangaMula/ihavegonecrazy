# -*- coding: utf-8 -*-
"""Book 37 - Russian (Cyrillic, 33 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Аа"), built with engine/generic.py."""
from generic import build, letter, section
from maps import region_map

PH = "Russian letter name"
BOOK = dict(left="А Б В", right="Г Д Е")


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:{20 if len(name) < 6 else 15}pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:2px">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("А", "а", "ah", "‘a’ as in “father”", "арбуз", "ar-BOOS", "watermelon", "watermelon"),
    L("Б", "бэ", "beh", "‘b’ as in “ball”", "банан", "bah-NAHN", "banana", "banana"),
    L("В", "вэ", "veh", "‘v’ as in “van”", "виноград", "vee-nah-GRAHT", "grapes", "grapes",
      rule="Careful: it looks like English B, but it says ‘v’!"),
    L("Г", "гэ", "geh", "‘g’ as in “go” — always hard", "груша", "GROO-shah", "pear", "pear"),
    L("Д", "дэ", "deh", "‘d’ as in “door”", "дом", "dom", "house", "house"),
    L("Е", "е", "yeh", "‘ye’ as in “yes” (after a consonant: ‘e’ as in “bed”, and the consonant goes soft)",
      "ежевика", "yee-zhee-VEE-kah", "blackberries", "ru_blackberry"),
    L("Ё", "ё", "yoh", "‘yo’ as in “yolk” — this vowel is always stressed", "ёлка", "YOL-kah", "fir tree", "ru_fir",
      rule="Grown-ups’ books often leave out the two dots; children’s books keep them."),
    L("Ж", "жэ", "zheh", "‘zh’ like the ‘s’ in “measure”", "жёлудь", "ZHO-loot", "acorn", "ru_acorn"),
    L("З", "зэ", "zeh", "‘z’ as in “zoo”", "зонт", "zont", "umbrella", "umbrella"),
    L("И", "и", "ee", "‘ee’ as in “see”", "инжир", "een-ZHEER", "figs", "fig"),
    L("Й", "и краткое", "ee KRAHT-kah-yeh (“short i”)", "‘y’ as in “boy” — a quick glide after a vowel", "чай", "chai",
      "tea", "teacup", note="Й only starts a few words. Find it at the end of <i>чай</i>!"),
    L("К", "ка", "kah", "‘k’ as in “kite”", "книга", "KNEE-gah", "book", "book", BOOK),
    L("Л", "эль", "el", "‘l’ as in “lamp” (darker, with the tongue pulled back)", "луна", "loo-NAH", "moon", "moon"),
    L("М", "эм", "em", "‘m’ as in “moon”", "мечеть", "mee-CHET", "mosque", "mosque"),
    L("Н", "эн", "en", "‘n’ as in “net”", "ножницы", "NOZH-nee-tsih", "scissors", "ru_scissors",
      rule="Careful: it looks like English H, but it says ‘n’!"),
    L("О", "о", "oh", "‘o’ as in “more” when stressed; like ‘a’ in “about” when not", "облако", "OB-lah-kah", "cloud", "clouds"),
    L("П", "пэ", "peh", "‘p’ as in “pen”", "подушка", "pah-DOOSH-kah", "pillow", "pillow"),
    L("Р", "эр", "er", "a rolled ‘r’ — let your tongue buzz!", "радуга", "RAH-doo-gah", "rainbow", "rainbow",
      rule="Careful: it looks like English P, but it says ‘r’!"),
    L("С", "эс", "es", "‘s’ as in “sun”", "солнце", "SON-tseh", "sun", "sun",
      note="In <i>солнце</i> the letter Л is silent.", rule="Careful: it looks like English C, and it always says ‘s’."),
    L("Т", "тэ", "teh", "‘t’ as in “top” (tongue on the teeth)", "тарелка", "tah-RYEL-kah", "plate", "plate"),
    L("У", "у", "oo", "‘oo’ as in “moon”", "утюг", "oo-TYOOK", "iron (for clothes)", "ru_iron",
      rule="Careful: it looks like English Y, but it says ‘oo’!"),
    L("Ф", "эф", "ef", "‘f’ as in “fan”", "финики", "FEE-nee-kee", "dates", "dates"),
    L("Х", "ха", "khah", "a breathy ‘kh’, like ‘ch’ in Scottish “loch”", "хлеб", "khlyep", "bread", "ru_bread",
      rule="Careful: it looks like English X, but it says ‘kh’!"),
    L("Ц", "цэ", "tseh", "‘ts’ as in “cats”", "цветок", "tsvee-TOK", "flower", "flower"),
    L("Ч", "че", "cheh", "‘ch’ as in “cheese”", "часы", "chee-SIH", "clock", "clock"),
    L("Ш", "ша", "shah", "‘sh’ as in “ship” (hard)", "шарик", "SHAH-reek", "balloon", "balloon"),
    L("Щ", "ща", "shshah", "a long, soft ‘sh’ — say “fresh sheep” quickly", "щит", "shsheet", "shield", "shield"),
    L("Ъ", "твёрдый знак", "TVYOR-dih znahk (“hard sign”)", "no sound of its own: it makes a tiny break before я, е, ё, ю",
      "подъезд", "pahd-YEST", "entrance of a building", "building",
      note="Ъ never starts a word. In <i>подъезд</i> it keeps “pod” and “yezd” apart."),
    L("Ы", "ы", "ih", "like ‘i’ in “ill”, said with the tongue pulled back", "мыло", "MIH-lah", "soap", "soap",
      note="Ы never starts a Russian word. Find it inside <i>мыло</i>!"),
    L("Ь", "мягкий знак", "MYAKH-kee znahk (“soft sign”)", "no sound of its own: it makes the letter before it soft",
      "соль", "sol", "salt", "salt", dict(label="соль"),
      note="Ь never starts a word. At the end of <i>соль</i> it makes the Л soft."),
    L("Э", "э", "eh", "‘e’ as in “bed”", "эскимо", "es-kee-MOH", "ice cream on a stick", "ru_popsicle"),
    L("Ю", "ю", "yoo", "‘yu’ as in “you”", "юла", "yoo-LAH", "spinning top", "top"),
    L("Я", "я", "yah", "‘ya’ as in “yard”", "яблоко", "YAB-lah-kah", "apple", "apple"),
]

# the phrases page carries 10 rows (greeting pair added), so its rows are a little tighter
EXTRA_CSS = ('.grid[style="margin-top:0.08in"]{gap:0.08in!important}'
             '.box[style*="justify-content:space-between;align-items:center;gap:0.2in"]{padding:0.04in 0.13in!important}')
CYR = [("Nunito Cyrillic", w, "normal", f"nunito-cyrillic-{w}-normal.woff2", None) for w in (400, 700, 800)]

LANG = build(dict(
    code="ru", folder="book-37-russian", series_no=37, isbn="", draft=True,
    name="Russian", native="русский язык", native_tr="ROOS-kee yee-ZIHK", name_word="название", write_word="пиши",
    title_native="Моя первая азбука", title_letters="АаБбВв", belongs_native="Эта книга принадлежит",
    belongs_pic="star", alphabet_native="алфавит", numbers_native="числа", numbers_tr="CHEES-lah",
    phrases_native="Первые слова",
    extra_css=EXTRA_CSS,
    fonts=CYR, disp_family="Nunito Cyrillic", text_family="Nunito Cyrillic",
    glyph_font=["nunito-cyrillic-900-normal.woff2", "nunito-latin-900-normal.woff2"],
    font_credit="Nunito (Cyrillic and Black weights)",
    phon_feature="each letter’s Russian name (А «а», Б «бэ», Л «эль»…)",
    sections=[section(LETTERS, native="алфавит", native_tr="al-fah-VEET — “the alphabet”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Russian is written in the <b>Cyrillic</b> alphabet. It has <b>33 letters</b>:
<b>10 vowels</b>, <b>21 consonants</b> and <b>2 signs</b> (Ъ and Ь) that have no sound of their own.</p>
<div class="box" style="margin:0.1in 0"><h3>Some old friends…</h3>А, К, М, О and Т look and sound almost like English letters.</div>
<div class="box" style="margin:0.1in 0"><h3>…and some tricksters!</h3><span class="nt"><b>В Н Р С У Х</b></span> look like English letters,
but they say <i>v, n, r, s, oo, kh</i>. Watch out for them!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt"><b>Аа</b></span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>pah-DOOSH-kah</i> means “say DOOSH a little louder”.",
        "Russian vowels change when they are not stressed: an unstressed <b>О</b> sounds like ‘a’, so <i>облако</i> is <i>OB-lah-kah</i>.",
        "<b>kh</b> is a breathy sound from the back of the throat, like ‘ch’ in Scottish “loch”.",
        "<b>zh</b> is the ‘s’ in “measure”; <b>ih</b> is the Russian sound Ы, like ‘i’ in “ill” with the tongue pulled back.",
        "<b>r</b> is always rolled or tapped with the tip of the tongue."],
    phon_explain="The box marked <i>Russian letter name</i> shows the name Russian children use for each letter "
                 "(Б is «бэ», Л is «эль»…) and a warning for letters that look like English ones but sound different.",
    standard="standard Russian (Moscow pronunciation)",
    hello=[
        ("Who speaks it?", "About <b>255 million people</b> speak Russian, around 150 million of them as their first language.<sup>³</sup>"),
        ("Where?", "In <b>Russia</b>, the largest country in the world, and by many people in Eastern Europe and Central Asia."),
        ("How is it written?", "In the <b>Cyrillic alphabet</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>33 letters</b>: 10 vowels, 21 consonants and 2 signs, Ъ and Ь."),
        ("A world language", "Russian is one of the <b>six official languages</b> of the United Nations."),
        ("Did you know?", "Some Russian words came from Arabic through other languages: <span class=\"nt\">магазин</span> "
                          "(<i>shop</i>) from <i>makhāzin</i>, “storehouses”, and <span class=\"nt\">алгебра</span> (<i>algebra</i>) from <i>al-jabr</i>."),
    ],
    hello_pics=[("ru_fir", {}), ("apple", {}), ("mosque", {})],
    map=region_map(frame=[[22.0, 40.0], [92.0, 72.0]],
                   points=dict(moscow=[37.62, 55.75], spb=[30.32, 59.94], kazan=[49.12, 55.79],
                               yekat=[60.60, 56.84], novosib=[82.92, 55.03]),
                   area=None,
                   cities=[("moscow", "Moscow", -18, 8, "end", True), ("spb", "Saint Petersburg", 14, -10, "start", False),
                           ("kazan", "Kazan", 0, 34, "middle", False), ("yekat", "Yekaterinburg", 0, -18, "middle", False),
                           ("novosib", "Novosibirsk", -14, 32, "end", False)],
                   label="RUSSIA", label_at=[62.0, 63.0], marker=[60.0, 58.0],
                   caption="The circle shows Russia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Russian is spoken in Moscow, "
                          "Saint Petersburg, Kazan, Yekaterinburg and Novosibirsk, and far beyond this map, all the way to the Pacific Ocean.",
                   seas=[("Black Sea", 34.5, 43.4), ("Caspian Sea", 51.0, 41.5), ("Barents Sea", 42.0, 70.6)], world_r=24),
    digits=[("0", "ноль", "nol", "zero"), ("1", "один", "ah-DEEN", "one"), ("2", "два", "dvah", "two"),
            ("3", "три", "tree", "three"), ("4", "четыре", "chee-TIH-ree", "four"), ("5", "пять", "pyaht", "five"),
            ("6", "шесть", "shest", "six"), ("7", "семь", "syem", "seven"), ("8", "восемь", "VOH-seem", "eight"),
            ("9", "девять", "DYEH-veet", "nine")],
    phrases=[("Ассаляму алейкум", "as-sah-LYAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Ва алейкум ассалям", "wah ah-LAY-koom as-sah-LYAHM", "And upon you be peace (the reply)"),
             ("Привет!", "pree-VYET", "Hello!"),
             ("Меня зовут …", "mee-NYAH zah-VOOT …", "My name is …"),
             ("Спасибо", "spah-SEE-bah", "Thank you"),
             ("Джазакаллаху хайран", "jah-zah-kahl-LAH-hoo KHAI-rahn", "May Allah reward you with good"),
             ("мама · папа", "MAH-mah · PAH-pah", "Mother · Father"),
             ("брат · сестра", "braht · sees-TRAH", "Brother · Sister"),
             ("да · нет", "dah · nyet", "Yes · No"),
             ("Я учу русский язык!", "yah oo-CHOO ROOS-kee yee-ZIHK", "I am learning Russian!")],
    cheer=("Машаллах! Молодец!", "mah-shahl-LAH! mah-lah-DYETS!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=BOOK,
    review_note="Check stress marks and vowel reduction in the transliterations (e.g. yee-zhee-VEE-kah, chee-SIH, VOH-seem), "
                "the choice of подъезд for Ъ, and the simplified guides for Щ (shsh) and Ы (ih).",
    tiles="АБЖЁЮЯ", cover_pics=["apple", "ru_fir", "balloon", "mosque"], title_size=48,
    speakers_blurb="Russian is spoken by about 255 million people in Russia, Eastern Europe, Central Asia and around the world.",
    sample_words=[("арбуз", "ar-BOOS", "watermelon"), ("луна", "loo-NAH", "moon"), ("яблоко", "YAB-lah-kah", "apple")],
    keywords=["russian alphabet book for kids", "learn russian for children", "russian azbuka coloring book",
              "cyrillic letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual russian english toddlers"],
))
