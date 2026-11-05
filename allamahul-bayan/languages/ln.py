# -*- coding: utf-8 -*-
"""Book 72 - Lingala (Lingála, Latin script with Ɛ and Ɔ, 22 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"), as in languages/es.py. Tones are not marked (everyday spelling)."""
from generic import build, section, fontset
from maps import region_map
from _sn_rw_ln_wo import fonts, GLYPH_FONTS, maker, inside

L = maker("Lingala syllables", "a e ɛ i o ɔ u")

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "ananasi", "ah-nah-NAH-see", "pineapple", "pineapple", vowel=True),
    L("B", "b", "ba", "bah", "‘b’ as in “ball”", "buku", "BOO-koo", "book", "book", args=dict(left="a b d", right="e ɛ f")),
    L("D", "d", "da", "dah", "‘d’ as in “day”", "dongodongo", "DOHN-goh-DOHN-goh", "okra", "ln_okra"),
    L("E", "e", "e", "ay", "a short ‘ay’ as in “day” (a closed e)", "etabe", "ay-TAH-bay", "banana", "banana", vowel=True),
    L("Ɛ", "ɛ", "ɛ", "eh", "‘e’ as in “bed” (an open e) — a Lingala letter!", "mbɛki", "MBEH-kee", "clay pot, bowl", "pot", vowel=True,
      note=inside("Ɛ", "mbɛki") + " Ɛ is wider and more open than E."),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "fololo", "foh-LOH-loh", "flower", "flower"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "ngomba", "NGOHM-bah", "mountain", "mountain",
      note="G usually comes after N: <i>ngomba</i>. Say “ng” together.", rule="gb = ‘g’ and ‘b’ said at the same time"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "likei", "lee-KAY-ee", "egg", "egg", vowel=True, note=inside("I", "likei")),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "kopo", "KOH-poh", "cup", "teacup"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lilala", "lee-LAH-lah", "orange", "ln_orange"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "manga", "MAHN-gah", "mango", "mango", rule="mb, mp = ‘m’ joined to b, p"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "ndako", "NDAH-koh", "house", "house",
      rule="nd, ng, nk, ns, nt, nz = ‘n’ joined to the next letter · ny = ‘ny’ as in “canyon”"),
    L("O", "o", "o", "oh", "‘o’ as in “go”, short (a closed o)", "monzoto", "moh-NZOH-toh", "star", "star", vowel=True,
      note=inside("O", "monzoto")),
    L("Ɔ", "ɔ", "ɔ", "aw", "‘aw’ as in “saw” (an open o) — a Lingala letter!", "mɔtɔ", "MAW-taw", "fire", "sn_fire", vowel=True,
      note=inside("Ɔ", "mɔtɔ") + " Ɔ is wider and more open than O."),
    L("P", "p", "pa", "pah", "‘p’ as in “pen”", "pilipili", "pee-lee-PEE-lee", "hot pepper (chilli)", "ln_chilli"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sanza", "SAHN-zah", "moon", "moon"),
    L("T", "t", "ta", "tah", "‘t’ as in “top”", "tomati", "toh-MAH-tee", "tomato", "tomato"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "mbula", "MBOO-lah", "rain", "raincloud", vowel=True, note=inside("U", "mbula")),
    L("V", "v", "va", "vah", "‘v’ as in “van”", "vɛlɔ", "VEH-law", "bicycle", "ln_bicycle",
      note="V is used mostly in borrowed words, like <i>vɛlɔ</i> from French “vélo”."),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "mwinda", "MWEEN-dah", "lamp, light", "bulb", note=inside("W", "mwinda")),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "mayi", "MAH-yee", "water", "water", note=inside("Y", "mayi")),
    L("Z", "z", "za", "zah", "‘z’ as in “zoo”", "zamba", "ZAHM-bah", "forest", "ln_forest"),
]

LANG = build(dict(
    code="ln", folder="book-72-lingala", series_no=72, isbn="", draft=True,
    name="Lingala", native="Lingala", native_tr="leen-GAH-lah", name_word="nkombo", write_word="koma",
    title_native="Alfabɛti na ngai ya liboso ya Lingala", title_letters="AaƐɛƆɔ", belongs_native="Buku oyo ezali ya",
    belongs_pic="ln_forest", alphabet_native="alfabɛti", numbers_native="mitango", numbers_tr="mee-TAHN-goh",
    phrases_native="Maloba ya liboso",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fonts(),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS,
    font_credit="Baloo 2, M PLUS Rounded 1c, Noto Sans",
    phon_feature="each letter’s Lingala syllable row (ba be bɛ bi bo bɔ bu), including the open vowels Ɛ and Ɔ",
    sections=[section(LETTERS, native="alfabɛti", native_tr="ahl-fah-BEH-tee — “the alphabet”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>This book teaches <b>22 letters</b> of Lingala, including two that English does not have:
<b>Ɛ ɛ</b> and <b>Ɔ ɔ</b>. The letters <b>C, H, J, Q, R, X</b> are hardly ever used, only in a few borrowed words.</p>
<div class="box" style="margin:0.1in 0"><h3>Seven vowels</h3><b>a, e, ɛ, i, o, ɔ, u</b>. Listen carefully: <b>e</b> is closed
(like “day”) and <b>ɛ</b> is open (like “bed”); <b>o</b> is closed (like “go”) and <b>ɔ</b> is open (like “saw”).</div>
<div class="box" style="margin:0.1in 0"><h3>N and M team up</h3>Many words begin with <b>mb, nd, ng, nz</b>…: <i>ndako</i> (house),
<i>mbula</i> (rain). Say the two letters together in one breath.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ɛɛ</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the syllable said a little more strongly: <i>NDAH-koh</i>. "
        "(Lingala is really a tone language; in everyday writing the tones are not marked, and this book does the same.)",
        "<b>ay</b> is the closed vowel <b>e</b>; <b>eh</b> is the open vowel <b>ɛ</b>. <b>oh</b> is <b>o</b>; <b>aw</b> is <b>ɔ</b>.",
        "<b>mb, nd, ng, nz</b> at the start of a word are said in one breath: <i>mbula</i> = “MBOO-lah”.",
        "Sounds follow the Lingala of Kinshasa and Brazzaville."],
    phon_explain="The box marked <i>Lingala syllables</i> shows how the letter is named in class and its row of syllables "
                 "with all seven vowels (ba be bɛ bi bo bɔ bu), the way Congolese children practise reading.",
    standard="Lingala of Kinshasa and Brazzaville, in the standard spelling with ɛ and ɔ (tones not marked)",
    hello=[
        ("Who speaks it?", "About <b>40 million people</b> speak Lingala; many of them learn it as a second, shared language.<sup>³</sup>"),
        ("Where?", "Along the great <b>Congo River</b>: in <b>Kinshasa</b> and <b>Brazzaville</b>, two capitals that face each other "
                   "across the river, and in the towns upstream."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with two extra vowels: <b>ɛ</b> and <b>ɔ</b>."),
        ("How many letters?", "<b>22 letters</b> in this book, plus letter teams such as <b>mb, nd, ng, ny, nz</b>."),
        ("Music!", "Lingala is the language of Congolese rumba songs, loved and danced to all over Africa."),
        ("Did you know?", "The Congo River is the <b>deepest river in the world</b>: in places it is more than 200 metres deep!"),
    ],
    hello_pics=[("ln_forest", {}), ("waves", {}), ("mosque", {})],
    map=region_map(frame=[[8.0, -14.0], [34.0, 12.0]],
                   points=dict(kinshasa=[15.31, -4.44], brazzaville=[15.24, -4.26], mbandaka=[18.26, 0.05], kisangani=[25.19, 0.52]),
                   area=(19.5, -1.8, 230, 120),
                   cities=[("kinshasa", "Kinshasa", 12, 16, "start", False), ("brazzaville", "Brazzaville", -12, -4, "end", False),
                           ("mbandaka", "Mbandaka", 12, -6, "start", False), ("kisangani", "Kisangani", 12, -6, "start", False)],
                   label="CONGO RIVER", label_at=[22.0, 4.2], marker=[20.0, -2.0], area_rot=-18,
                   caption="The circle shows Central Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Lingala is spoken in Kinshasa "
                          "and Brazzaville and along the Congo River up to Mbandaka and Kisangani. The dashed line shows that river land.",
                   seas=[("Atlantic Ocean", 11.0, -10.0)], world_r=13),
    digits=[("0", "zero", "zay-ROH", "zero"), ("1", "mɔkɔ", "MAW-kaw", "one"), ("2", "mibale", "mee-BAH-lay", "two"),
            ("3", "misato", "mee-SAH-toh", "three"), ("4", "minei", "mee-NAY-ee", "four"), ("5", "mitano", "mee-TAH-noh", "five"),
            ("6", "motoba", "moh-TOH-bah", "six"), ("7", "sambo", "SAHM-boh", "seven"), ("8", "mwambe", "MWAHM-bay", "eight"),
            ("9", "libwa", "LEE-bwah", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Mbote!", "MBOH-tay", "Hello!"),
             ("Nkombo na ngai …", "NKOHM-boh nah NGAH-ee …", "My name is …"),
             ("Matɔkɔsi", "mah-taw-KAW-see", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("mama · papa", "MAH-mah · PAH-pah", "Mother · Father"),
             ("ndeko mobali · ndeko mwasi", "NDAY-koh moh-BAH-lee · NDAY-koh MWAH-see", "Brother · Sister"),
             ("ɛɛ · te", "EH-eh · tay", "Yes · No"),
             ("Nazali koyekola Lingala!", "nah-ZAH-lee koh-yay-KOH-lah leen-GAH-lah", "I am learning Lingala!")],
    cheer=("Mashallah! Osali malamu!", "MAH-shah-lah! oh-SAH-lee mah-LAH-moo!", "Well done, you did it well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="a b d", right="e ɛ f"),
    review_note="Drafted without a native speaker. Check above all: mbɛki (clay pot/bowl) for Ɛ; etabe (banana); dongodongo (okra); "
                "mayi as a spelling of water (also written mai); mwinda (lamp); vɛlɔ (bicycle); tomati; the letter set (22 letters, "
                "H and R left out as loan-only); the title “Alfabɛti na ngai ya liboso ya Lingala”; zero for 0; ɛɛ for “yes”; "
                "and where ɛ/ɔ (rather than e/o) belong in each word, since tones and vowel quality were written from memory.",
    tiles="AƐƆBMZ", cover_pics=["ln_forest", "pineapple", "moon", "mosque"], title_size=48,
    speakers_blurb="Lingala is spoken by about 40 million people along the great Congo River.",
    sample_words=[("sanza", "SAHN-zah", "moon"), ("fololo", "foh-LOH-loh", "flower"), ("mɔtɔ", "MAW-taw", "fire")],
    keywords=["lingala alphabet book for kids", "learn lingala for children", "congo kids coloring book",
              "lingala english bilingual", "muslim kids activity book", "islamic coloring book for children",
              "african language alphabet workbook"],
))
