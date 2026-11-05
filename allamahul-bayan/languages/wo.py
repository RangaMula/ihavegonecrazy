# -*- coding: utf-8 -*-
"""Book 73 - Wolof (Latin script, official CLAD spelling, 27 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"), as in languages/es.py."""
from generic import build, section, fontset
from maps import region_map
from _sn_rw_ln_wo import fonts, GLYPH_FONTS, maker, inside

L = maker("Wolof syllables", "a e ë i o u")

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”; À is a short, sharp ‘a’", "àlluwa", "AHL-loo-wah",
      "wooden writing board of the Qur’an school", "wo_alluwa", vowel=True,
      note="Children in the <i>daara</i> (Qur’an school) write their first Arabic letters on an <i>àlluwa</i>."),
    L("B", "b", "ba", "bah", "‘b’ as in “ball”", "biddiw", "BID-deew", "star", "star"),
    L("C", "c", "ca", "chah", "‘ch’ as in “church”", "ceeb", "CHAYB", "rice", "rice"),
    L("D", "d", "da", "dah", "‘d’ as in “day”", "dugub", "DOO-goob", "millet", "wo_millet"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”; double EE is long, like “ay” in “day”", "xeer", "KHAYR", "stone", "sn_rocks", vowel=True,
      note=inside("E", "xeer")),
    L("Ë", "ë", "ë", "uh", "‘u’ as in “but” — a Wolof letter!", "kër", "KUHR", "house, home", "house", vowel=True,
      note=inside("Ë", "kër")),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "fëlër", "FUH-luhr", "flower", "flower"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "garab", "GAH-rahb", "tree", "tree"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "kaani", "KAH-nee", "hot pepper (chilli)", "ln_chilli", vowel=True,
      note=inside("I", "kaani")),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "jàkka", "JAHK-kah", "mosque", "mosque"),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "kuddu", "KOOD-doo", "spoon", "spoon"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lem", "LEHM", "honey", "honey"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "mburu", "MBOO-roo", "bread", "wo_bread", rule="mb = ‘m’ joined to ‘b’"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "ndox", "NDOKH", "water", "water", rule="nd, ng, nj = ‘n’ joined to the next letter"),
    L("Ñ", "ñ", "ña", "nyah", "‘ny’ as in “canyon” — a Wolof letter!", "ñambi", "NYAHM-bee", "cassava", "wo_cassava"),
    L("Ŋ", "ŋ", "ŋa", "ngah", "‘ng’ as in “sing” — a Wolof letter!", "limoŋ", "lee-MONG", "lime, lemon", "lemon",
      note="Ŋ hardly ever starts a word. Find it at the end of <i>limoŋ</i>!"),
    L("O", "o", "o", "oh", "‘o’ as in “for”; Ó is a closed ‘o’ as in “go”", "soble", "SOHB-leh", "onion", "onion", vowel=True,
      note=inside("O", "soble")),
    L("P", "p", "pa", "pah", "‘p’ as in “pen”", "palanteer", "pah-lahn-TAYR", "window", "window"),
    L("Q", "q", "qa", "qah", "a deep ‘k’ from the back of the throat, like Arabic ق", "mboq", "MBOHQ", "maize (corn)", "corn",
      note="Q never starts a Wolof word. Find it at the end of <i>mboq</i>!"),
    L("R", "r", "ra", "rah", "a rolled ‘r’", "kurus", "KOO-roos", "prayer beads (tasbih)", "tasbih", note=inside("R", "kurus")),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "saabu", "SAH-boo", "soap", "soap"),
    L("T", "t", "ta", "tah", "‘t’ as in “top”", "taw", "TOW", "rain", "raincloud"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "suuf", "SOOF", "sand, ground", "sn_sand", vowel=True, note=inside("U", "suuf")),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "weer", "WAYR", "moon", "moon"),
    L("X", "x", "xa", "khah", "a rough ‘kh’ from the throat, like Arabic خ", "xorom", "KHOH-rohm", "salt", "salt", args=dict(label="xorom")),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "yoon", "YOHN", "road, path", "wo_road"),
]

LANG = build(dict(
    code="wo", folder="book-73-wolof", series_no=73, isbn="", draft=True,
    name="Wolof", native="Wolof", native_tr="WOH-lohf", name_word="tur", write_word="bindal",
    title_native="Sama araf yu njëkk ci Wolof", title_letters="AaËëŊŋ", belongs_native="Boroom téere bii:",
    belongs_pic="wo_alluwa", alphabet_native="araf yi", numbers_native="lim yi", numbers_tr="LEEM yee",
    phrases_native="Baat yu njëkk",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fonts(),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS,
    font_credit="Baloo 2",
    phon_feature="each letter’s Wolof syllable row (ba be bë bi bo bu), including the Wolof letters Ë, Ñ and Ŋ",
    sections=[section(LETTERS, native="araf yi", native_tr="AH-rahf yee — “the letters”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Wolof is written with <b>27 letters</b> in the official Latin spelling, including three that English
does not have: <b>Ë</b>, <b>Ñ</b> and <b>Ŋ</b>. <b>H, V</b> and <b>Z</b> appear only in borrowed words.</p>
<div class="box" style="margin:0.1in 0"><h3>Little marks on vowels</h3><b>à</b> is a short, sharp a; <b>é</b> and <b>ó</b> are closed
(like “day” and “go”); <b>ë</b> is the soft ‘u’ of “but”. A double vowel is long: <i>ceeb</i>, <i>suuf</i>.</div>
<div class="box" style="margin:0.1in 0"><h3>Sounds you know from the Qur’an</h3><b>X</b> sounds like Arabic <span class="ar">خ</span>
and <b>Q</b> like Arabic <span class="ar">ق</span>. Wolof has borrowed many words from Arabic too.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ëë</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the syllable said a little more strongly; in Wolof it is usually the first one.",
        "<b>kh</b> in the pronunciation is the rough Wolof <b>x</b>, like Arabic خ; <b>q</b> is a deep k, like Arabic ق.",
        "<b>uh</b> is the Wolof <b>ë</b>, the soft vowel in “but”. Double letters (<i>dd, kk, ll</i>) are held a little longer.",
        "Sounds follow the Wolof of Dakar, in the official Senegalese spelling."],
    phon_explain="The box marked <i>Wolof syllables</i> shows how the letter is named in class and its row of syllables "
                 "(ba be bë bi bo bu), the way Senegalese children practise reading.",
    standard="Senegalese (Dakar) Wolof in the official Latin spelling",
    hello=[
        ("Who speaks it?", "About <b>6 million people</b> speak Wolof at home, and millions more use it every day in Senegal.<sup>³</sup>"),
        ("Where?", "In <b>Senegal</b> and <b>the Gambia</b>, on the Atlantic coast of West Africa, and also in Mauritania."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with the extra letters <b>Ë, Ñ, Ŋ</b>."),
        ("Written in Arabic letters too", "For centuries Wolof has also been written in Arabic letters, called <b>Wolofal</b> "
                                          "(Wolof Ajami). Scholars wrote poems in Wolofal, and it is still learnt in Qur’an schools."),
        ("How many letters?", "<b>27 letters</b> in this book."),
        ("Did you know?", "Most Wolof speakers are Muslim. The two Eids are called <b>Korite</b> (Eid al-Fitr) and <b>Tabaski</b> "
                          "(Eid al-Adha), and the greeting is <i>Asalaa maalekum!</i>"),
    ],
    hello_pics=[("wo_alluwa", {}), ("mosque", {}), ("eid", {})],
    map=region_map(frame=[[-20.0, 9.0], [-8.0, 21.0]],
                   points=dict(dakar=[-17.44, 14.69], saintlouis=[-16.49, 16.03], touba=[-15.88, 14.86],
                               kaolack=[-16.07, 14.15], banjul=[-16.58, 13.45]),
                   area=(-16.0, 14.8, 150, 135),
                   cities=[("dakar", "Dakar", -12, 16, "end", False), ("saintlouis", "Saint-Louis", 12, -4, "start", False),
                           ("touba", "Touba", 12, -4, "start", False), ("kaolack", "Kaolack", 12, 12, "start", False),
                           ("banjul", "Banjul", -12, 14, "end", False)],
                   label="WEST AFRICA", label_at=[-12.5, 18.6], marker=[-15.0, 14.5],
                   caption="The circle shows West Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Wolof is spoken in Dakar, "
                          "Saint-Louis, Touba, Kaolack and Banjul. The dashed line shows where most Wolof families live.",
                   seas=[("Atlantic Ocean", -18.6, 10.8)], world_r=13),
    digits=[("0", "dara", "DAH-rah", "zero (nothing)"), ("1", "benn", "BEHN", "one"), ("2", "ñaar", "NYAHR", "two"),
            ("3", "ñett", "NYEHT", "three"), ("4", "ñeent", "NYAYNT", "four"), ("5", "juróom", "joo-ROHM", "five"),
            ("6", "juróom-benn", "joo-ROHM-behn", "six (five + one)"), ("7", "juróom-ñaar", "joo-ROHM-nyahr", "seven (five + two)"),
            ("8", "juróom-ñett", "joo-ROHM-nyeht", "eight (five + three)"), ("9", "juróom-ñeent", "joo-ROHM-nyaynt", "nine (five + four)")],
    phrases=[("Asalaa maalekum", "ah-sah-LAH mah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Maalekum salaam", "mah-LAY-koom sah-LAHM", "And upon you be peace (the reply)"),
             ("Na nga def?", "nah ngah DEF?", "How are you?"),
             ("Maa ngi tudd …", "MAH ngee TOOD …", "My name is …"),
             ("Jërëjëf", "JUH-ruh-juhf", "Thank you"),
             ("Jazaakallaahu xayran", "jah-zah-KAH-lah-hoo KHAY-rahn", "May Allah reward you with good"),
             ("yaay · baay", "YAAI · BAAI", "Mother · Father"),
             ("mag ju góor · mag ju jigéen", "MAHG joo GOHR · MAHG joo jee-GAYN", "Big brother · Big sister"),
             ("waaw · déedéet", "WAOW · DAY-dayt", "Yes · No"),
             ("Maa ngi jàng Wolof!", "MAH ngee JAHNG WOH-lohf", "I am learning Wolof!")],
    cheer=("Mashallah! Baax na lool!", "MAH-shah-lah! BAHKH nah LOHL!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="Ë Ñ Ŋ"),
    review_note="Drafted without a native speaker. Check above all: limoŋ (lime) for Ŋ and mboq (maize) for Q; fëlër (flower, "
                "a loan; tóortóor is the older word); àlluwa, kurus (prayer beads), palanteer (window), dugub, ñambi, yoon; "
                "dara for zero; the title “Sama araf yu njëkk ci Wolof” and “Boroom téere bii:”; mag ju góor · mag ju jigéen "
                "for brother · sister; and the letter names used in Senegalese classrooms (given here as a, ba, ca…).",
    tiles="AËÑŊXJ", cover_pics=["wo_alluwa", "mosque", "moon", "wo_bread"], title_size=50,
    speakers_blurb="Wolof is spoken by millions of people in Senegal and the Gambia, on the Atlantic coast of West Africa.",
    sample_words=[("weer", "WAYR", "moon"), ("garab", "GAH-rahb", "tree"), ("jàkka", "JAHK-kah", "mosque")],
    keywords=["wolof alphabet book for kids", "learn wolof for children", "senegal kids coloring book",
              "wolof english bilingual", "muslim kids activity book", "islamic coloring book for children",
              "african language alphabet workbook"],
))
