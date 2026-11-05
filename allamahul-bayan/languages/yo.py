# -*- coding: utf-8 -*-
"""Book 64 - Yoruba (Latin script: 25 letters incl. Ẹ Ọ Ṣ GB, with tone marks). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
from _afrolatin import afro_fonts, GLYPH_FONTS, FONT_CREDIT, maker

L = maker("Yoruba name · syllables", ["a", "e", "ẹ", "i", "o", "ọ", "u"])

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "àpótí", "ah-POH-TEE", "box", "box", vowel=True),
    L("B", "b", "bi", "bee", "‘b’ as in “ball”", "bọ́ọ̀lù", "BAW-aw-loo", "ball", "ball"),
    L("D", "d", "di", "dee", "‘d’ as in “door”", "dòdò", "doh-doh", "fried ripe plantain", "banana"),
    L("E", "e", "e", "ay", "‘ay’ as in “say”, short and pure", "ewé", "ay-WAY", "leaf", "dew", vowel=True),
    L("Ẹ", "ẹ", "ẹ", "eh", "‘e’ as in “bed” — the dot makes it open", "ẹyin", "eh-yin", "egg", "egg", vowel=True,
      rule="e = s<b>ay</b> · ẹ = b<b>e</b>d"),
    L("F", "f", "fi", "fee", "‘f’ as in “fan”", "fèrèsé", "feh-reh-SAY", "window", "window"),
    L("G", "g", "gi", "gee", "‘g’ as in “go” (always hard)", "gúgúrú", "GOO-GOO-ROO", "popcorn, roasted corn", "corn"),
    L("Gb", "gb", "gbi", "gbee", "‘g’ and ‘b’ said <b>together</b>, at the same time", "ìgbálẹ̀", "ee-GBAH-leh", "broom", "broom",
      note="<b>Gb</b> is two letters that make one sound — Yoruba counts it as one letter."),
    L("H", "h", "hi", "hee", "‘h’ as in “hat”", "hámà", "HAH-mah", "hammer", "tools"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "ìwé", "ee-WAY", "book", "book", vowel=True, args=dict(left="A B D", right="E Ẹ F")),
    L("J", "j", "ji", "jee", "‘j’ as in “jam”", "jígí", "JEE-GEE", "mirror", "mirror"),
    L("K", "k", "ki", "kee", "‘k’ as in “kite”", "kànga", "kahn-gah", "well (for water)", "well"),
    L("L", "l", "li", "lee", "‘l’ as in “lamp”", "lẹ́mọ́ọ̀nù", "LEH-MAW-aw-noo", "lemon", "lemon"),
    L("M", "m", "mi", "mee", "‘m’ as in “moon”", "mọ́sálásí", "MAW-SAH-LAH-SEE", "mosque", "mosque"),
    L("N", "n", "ni", "nee", "‘n’ as in “net”", "iná", "ee-NAH", "fire, light", "bulb",
      note="Few Yoruba naming words start with N. Find it inside <i>iná</i>!"),
    L("O", "o", "o", "oh", "‘o’ as in “go”, short and pure", "omi", "oh-mee", "water", "water", vowel=True),
    L("Ọ", "ọ", "ọ", "aw", "‘aw’ as in “saw” — the dot makes it open", "ọ̀gẹ̀dẹ̀", "aw-geh-deh", "banana, plantain", "banana", vowel=True,
      rule="o = g<b>o</b> · ọ = s<b>aw</b>"),
    L("P", "p", "pi", "kpee", "‘k’ and ‘p’ said <b>together</b> — Yoruba P is never a plain ‘p’!", "pápá", "KPAH-KPAH",
      "field, grass", "ig_grass"),
    L("R", "r", "ri", "ree", "a quick tapped ‘r’", "ìràwọ̀", "ee-rah-waw", "star", "star",
      note="Few Yoruba words start with R. Find it inside <i>ìràwọ̀</i>!"),
    L("S", "s", "si", "see", "‘s’ as in “sun”", "àsíá", "ah-SEE-AH", "flag", "flag"),
    L("Ṣ", "ṣ", "ṣi", "shee", "‘sh’ as in “ship”", "ṣíbí", "SHEE-BEE", "spoon", "spoon", rule="s = <b>s</b>un · ṣ = <b>sh</b>ip"),
    L("T", "t", "ti", "tee", "‘t’ as in “tap”", "tòmátì", "toh-MAH-tee", "tomato", "tomato"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "oòrùn", "oh-oh-roon", "sun", "sun", vowel=True,
      note="No Yoruba word starts with U. Find it inside <i>oòrùn</i>!"),
    L("W", "w", "wi", "wee", "‘w’ as in “water”", "wákàtí", "WAH-kah-TEE", "hour (time on the clock)", "clock"),
    L("Y", "y", "yi", "yee", "‘y’ as in “yes”", "yìnyín", "yeen-YEEN", "ice, hailstones", "ice"),
]

LANG = build(dict(
    code="yo", folder="book-64-yoruba", series_no=64, isbn="", draft=True,
    name="Yoruba", native="Yorùbá", native_tr="yoh-roo-BAH", name_word="orúkọ", write_word="kọ ọ́",
    title_native="Álífábẹ́ẹ̀tì Yorùbá àkọ́kọ́ mi", title_letters="AaẸẹỌọ", belongs_native="Ìwé yìí jẹ́ ti",
    belongs_pic="banana", alphabet_native="álífábẹ́ẹ̀tì", numbers_native="òǹkà", numbers_tr="oh-n-kah",
    phrases_native="Ọ̀rọ̀ àkọ́kọ́",
    fonts=afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s Yoruba name and its syllables (ba, be, bẹ, bi, bo, bọ, bu)",
    sections=[section(LETTERS, native="álífábẹ́ẹ̀tì Yorùbá", native_tr="ah-LEE-FAH-BEH-eh-tee yoh-roo-BAH — “the Yoruba alphabet”",
                      chart_cols=7, warmup_cols=5,
                      intro_html="""<p>Yoruba has <b>25 letters</b>. It has no C, Q, V, X or Z — but it has <b>Ẹ</b>, <b>Ọ</b>, <b>Ṣ</b> and <b>GB</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Dots under letters</h3>A dot changes the sound: <b>e</b> says “ay” but <b>ẹ</b> says “eh”;
<b>o</b> says “oh” but <b>ọ</b> says “aw”; <b>s</b> says “s” but <b>ṣ</b> says “sh”.</div>
<div class="box" style="margin:0.1in 0"><h3>Singing tones</h3>Yoruba words go up and down like a song. Marks over the vowels show the tone:
<b>á</b> high (<i>do</i>), <b>a</b> middle (<i>re</i>), <b>à</b> low (<i>mi</i>). <b>igbá</b> is a calabash, <b>ìgbà</b> is time and
<b>igba</b> is two hundred!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ẹẹ</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show a <b>high tone</b> (say it with a higher voice): <i>ah-POH-TEE</i>. Small letters are middle or low.",
        "<b>ay</b> is Yoruba e, <b>eh</b> is ẹ, <b>oh</b> is o and <b>aw</b> is ọ. Vowels stay pure — they never slide.",
        "<b>kp</b> and <b>gb</b> are said with the back of the tongue and the lips at the same time.",
        "<b>n</b> after a vowel (an, in, un, ẹn, ọn) makes the vowel sound through the nose, as in French."],
    phon_explain="The box marked <i>Yoruba name · syllables</i> shows how Yoruba children name the letter (B is «bi», P is «pi», "
                 "said <i>kpee</i>) and its syllable row with all seven vowels.",
    standard="Standard Yoruba, based on the speech of Ọ̀yọ́ and Ìbàdàn",
    hello=[
        ("Who speaks it?", "About <b>45 million people</b> speak Yoruba.<sup>³</sup>"),
        ("Where?", "In south-western <b>Nigeria</b> and in <b>Benin</b> and <b>Togo</b>. Yoruba words are also sung far away, in Brazil and Cuba."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with dots under some letters (ẹ ọ ṣ) and tone marks "
                               "over the vowels (á à)."),
        ("How many letters?", "<b>25 letters</b>, with the special letters <b>Ẹ Ọ Ṣ</b> and the pair <b>GB</b>."),
        ("A singing language", "Yoruba has three tones — high, middle and low. Drummers can even “talk” Yoruba on the <i>dùndún</i> drum by "
                               "copying the tones!"),
        ("Did you know?", "Yoruba Muslims use many words from Arabic: <i>wákàtí</i> (hour, from <i>waqt</i>), <i>àlàáfíà</i> "
                          "(peace and good health, from <i>al-ʿāfiya</i>) and <i>àlùbáríkà</i> (blessing, from <i>baraka</i>)."),
    ],
    hello_pics=[("banana", {}), ("corn", {}), ("mosque", {})],
    map=region_map(frame=[[-0.5, 2.5], [10.5, 13.5]],
                   points=dict(lagos=[3.38, 6.52], ibadan=[3.90, 7.38], ilorin=[4.55, 8.50], akure=[5.20, 7.25], portonovo=[2.63, 6.50]),
                   area=(3.9, 7.6, 230, 190), area_rot=-10,
                   cities=[("lagos", "Lagos", 8, 26, "start", False), ("ibadan", "Ibadan", -14, 8, "end", False),
                           ("ilorin", "Ilorin", 14, 8, "start", False), ("akure", "Akure", 14, 8, "start", False),
                           ("portonovo", "Porto-Novo", -10, -12, "end", False)],
                   label="WEST AFRICA", label_at=[0.5, 12.3], marker=[4.0, 8.0],
                   caption="The circle shows Yorubaland, in West Africa, on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Yoruba is spoken in Lagos, Ibadan, "
                          "Ilorin, Akure, Porto-Novo and many other towns. The dashed line shows where most Yoruba speakers live.",
                   seas=[("Gulf of Guinea", 3.5, 4.0)], world_r=14),
    digits=[("0", "òdo", "oh-doh", "zero"), ("1", "ọ̀kan", "aw-kahn", "one"), ("2", "èjì", "ay-jee", "two"),
            ("3", "ẹ̀ta", "eh-tah", "three"), ("4", "ẹ̀rin", "eh-rin", "four"), ("5", "àrún", "ah-ROON", "five"),
            ("6", "ẹ̀fà", "eh-fah", "six"), ("7", "èje", "ay-jay", "seven"), ("8", "ẹ̀jọ", "eh-jaw", "eight"),
            ("9", "ẹ̀sán", "eh-SAHN", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum salaam", "wah ah-LAY-koom sah-LAHM", "And peace be upon you (the reply)"),
             ("Ẹ kú àárọ̀!", "eh KOO ah-AH-raw", "Good morning! (to an elder)"),
             ("Orúkọ mi ni …", "oh-ROO-kaw mee nee …", "My name is …"),
             ("Ẹ ṣé o!", "eh SHAY oh", "Thank you!"),
             ("Jazakallahu khairan", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("Ìyá · Bàbá", "ee-YAH · bah-BAH", "Mother · Father"),
             ("arákùnrin · arábìnrin", "ah-RAH-koon-rin · ah-RAH-bin-rin", "Brother · Sister"),
             ("Bẹ́ẹ̀ni · Rárá", "BEH-eh-nee · RAH-RAH", "Yes · No"),
             ("Mo ń kọ́ èdè Yorùbá!", "moh N KAW ay-day yoh-roo-BAH", "I am learning Yoruba!")],
    cheer=("Mashallah! O ṣe dáadáa!", "MAH-shah-lah! oh shay DAH-ah-DAH-ah", "Mashallah! You did very well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B D", right="E Ẹ F"),
    review_note="Check every tone mark. Uncertain words: <i>hámà</i> (hammer) for H, <i>jígí</i> (or <i>dígí</i>) for J, "
                "<i>pápá</i> (field) for P, <i>àsíá</i> (flag) for S, <i>lẹ́mọ́ọ̀nù</i>, <i>tòmátì</i>, <i>yìnyín</i> (ice); the letter "
                "names (a, bi, di…); and the title <i>Álífábẹ́ẹ̀tì Yorùbá àkọ́kọ́ mi</i>.",
    tiles="AẸMỌṢY", cover_pics=["banana", "corn", "mosque", "flower"],
    speakers_blurb="Yoruba is spoken by about 45 million people in Nigeria, Benin and Togo.",
    sample_words=[("omi", "oh-mee", "water"), ("ìwé", "ee-WAY", "book"), ("ṣíbí", "SHEE-BEE", "spoon")],
    keywords=["yoruba alphabet book for kids", "learn yoruba for children", "yoruba coloring book",
              "yoruba letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual yoruba english toddlers"],
))
