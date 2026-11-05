# -*- coding: utf-8 -*-
"""Book 79 - Luganda (Oluganda, Latin script: 24 letters incl. NY and Ŋ). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
import _afrolatin as AF

L = AF.maker("Luganda name · syllables", ["a", "e", "i", "o", "u"])

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "amazzi", "ah-mah-zzee", "water", "water", vowel=True),
    L("B", "b", "ba", "bah", "‘b’ as in “ball”", "bbaluwa", "bbah-loo-wah", "a letter to post", "envelope"),
    L("C", "c", "ca", "chah", "‘ch’ as in “church” — never ‘k’ or ‘s’", "ccupa", "cchoo-pah", "bottle", "lg_bottle"),
    L("D", "d", "da", "dah", "‘d’ as in “door”", "ddirisa", "ddee-ree-sah", "window", "window"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "essaawa", "eh-ssaa-wah", "clock, watch", "clock", vowel=True),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "ffene", "ffeh-neh", "jackfruit", "lg_jackfruit"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "gonja", "goh-njah", "sweet plantain (a big banana for roasting)", "banana"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "omuti", "oh-moo-tee", "tree", "tree", vowel=True,
      note="Luganda naming words never start with I. Find it at the end of <i>omuti</i>!"),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "jjinja", "jjee-njah", "stone", "lg_stones"),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "kkalaamu", "kkah-laa-moo", "pen", "pen"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lumonde", "loo-moh-ndeh", "sweet potato", "potato"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "mwezi", "mweh-zee", "moon, month", "moon"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "nnanaasi", "nnah-naa-see", "pineapple", "pineapple"),
    L("Ny", "ny", "nya", "nyah", "‘ny’ as in “canyon” — one letter in Luganda!", "nnyaanya", "nnyaa-nyah", "tomato", "tomato",
      note="NY counts as <b>one letter</b> of the Luganda alphabet."),
    L("Ŋ", "ŋ", "ŋa", "ngah", "‘ng’ as in “sing” — but Luganda can start a word with it!", "ŋŋoma", "ngngoh-mah", "drum", "lg_drum",
      rule="ŋ = “si<b>ng</b>” · ng = “fi<b>ng</b>er”"),
    L("O", "o", "o", "oh", "‘o’ as in “more” (short and pure)", "omunnyo", "oh-moo-nnyoh", "salt", "salt", vowel=True),
    L("P", "p", "pa", "pah", "‘p’ as in “pen”", "ppaapaali", "ppaa-paa-lee", "papaya", "lg_papaya"),
    L("R", "r", "ra", "rah", "a quick tapped ‘r’ — used only after <b>e</b> or <b>i</b>", "omuceere", "oh-moo-cheh-reh", "rice", "rice",
      note="R never starts a Luganda word: it comes after E or I, where L would be. Find it in <i>omuceere</i>!",
      rule="L after a, o, u · R after e, i"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "ssabbuuni", "ssah-bboo-nee", "soap", "soap"),
    L("T", "t", "ta", "tah", "‘t’ as in “tap”", "ttaala", "ttaa-lah", "lamp, light", "bulb"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "katungulu", "kah-too-ngoo-loo", "onion", "onion", vowel=True,
      note="Few Luganda words start with U. Find it three times in <i>katungulu</i>!"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "muwogo", "moo-woh-goh", "cassava", "lg_cassava",
      note="Find W in the middle of <i>muwogo</i>."),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "caayi", "chaa-yee", "tea", "teacup",
      note="Find Y near the end of <i>caayi</i>."),
    L("Z", "z", "za", "zah", "‘z’ as in “zoo”", "lusozi", "loo-soh-zee", "hill, mountain", "mountain",
      note="Find Z at the end of <i>lusozi</i>."),
]

LANG = build(dict(
    code="lg", folder="book-79-luganda", series_no=79, isbn="", draft=True,
    name="Luganda", native="Oluganda", native_tr="oh-loo-gah-ndah", name_word="erinnya", write_word="wandiika",
    title_native="Ennukuta z’Oluganda", title_letters="AaŊŋZz", belongs_native="Ekitabo kino kya",
    belongs_pic="star", alphabet_native="ennukuta", numbers_native="ennamba", numbers_tr="en-nah-mbah",
    phrases_native="Ebigambo ebisooka",
    fonts=AF.afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=AF.GLYPH_FONTS, font_credit=AF.FONT_CREDIT, extra_css=getattr(AF, "EXTRA_CSS", ""),
    phon_feature="each letter’s Luganda name and its syllables (ba, be, bi, bo, bu)",
    sections=[
        section(LETTERS, native="ennukuta z’Oluganda", native_tr="en-noo-koo-tah zoh-loo-gah-ndah — “the letters of Luganda”",
                chart_cols=6, warmup_cols=6,
                intro_html="""<p>Luganda is written with <b>24 letters</b>. It has no H, Q, V or X, and two letters of its own: <b>NY</b> and <b>Ŋ</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Say it twice!</h3>A <b>double vowel</b> is said long: <i>caayi</i> (tea). A <b>double consonant</b> is said
strong: <i>ssabbuuni</i> (soap). Luganda spelling shows you exactly how long each sound is.</div>
<div class="box" style="margin:0.1in 0"><h3>“Kino kitabo!”</h3>Most Luganda naming words start with a little vowel: <i>e</i>kitabo, <i>o</i>muti,
<i>a</i>mazzi. When you say “this is a …”, it drops off: <i>Kino kitabo!</i> — “This is a book!” So some words in this book start without it.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
    ],
    sound_notes=[
        "Luganda has no strong stress: say every syllable evenly, and let long (double) vowels last twice as long: <i>caa-yee</i>.",
        "A <b>double consonant</b> (<i>bb, ss, kk, ŋŋ</i>) is held a little longer and said strongly: <i>ssah-bboo-nee</i>.",
        "<b>c</b> is always ‘ch’ as in “church”; <b>ŋ</b> is the ‘ng’ at the end of “sing”.",
        "Luganda is a <b>tonal</b> language: high and low voice pitch can change a word. Listen to a Luganda speaker to hear the music!"],
    phon_explain="The box marked <i>Luganda name · syllables</i> shows the name Luganda children use for the letter "
                 "(B is «ba», C is «ca») and its row of syllables.",
    standard="Standard Luganda as spoken in Kampala and Buganda",
    hello=[
        ("Who speaks it?", "More than <b>10 million people</b> speak Luganda as their first language, and millions more use it as a second "
                           "language.<sup>³</sup>"),
        ("Where?", "In <b>Uganda</b>: in the central region around <b>Kampala</b> and along the northern shores of <b>Lake Victoria</b>, "
                   "and in markets and towns all over the country."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. Double letters show long and strong sounds."),
        ("How many letters?", "<b>24 letters</b>, including <b>NY</b> and the special letter <b>Ŋ</b>."),
        ("One root, many words", "A <b>Muganda</b> is one person, the <b>Baganda</b> are the people, <b>Buganda</b> is the land and "
                                 "<b>Luganda</b> is the language!"),
        ("Did you know?", "Some Luganda words came from Arabic through Swahili: <i>kitabo</i> (book, from <i>kitāb</i>), <i>kkalaamu</i> "
                          "(pen, from <i>qalam</i>), <i>essaawa</i> (clock, from <i>sāʿa</i>) and <i>ssabbuuni</i> (soap, from <i>ṣābūn</i>)."),
    ],
    hello_pics=[("banana", {}), ("lg_drum", {}), ("mosque", {})],
    map=region_map(frame=[[27.0, -8.0], [42.0, 7.0]],
                   points=dict(kampala=[32.58, 0.35], entebbe=[32.46, 0.05], jinja=[33.20, 0.44], masaka=[31.73, -0.33]),
                   area=(32.3, 0.1, 110, 90), area_rot=0,
                   cities=[("kampala", "Kampala", -12, -6, "end", False), ("entebbe", "Entebbe", -12, 18, "end", False),
                           ("jinja", "Jinja", 12, 4, "start", False), ("masaka", "Masaka", -12, 10, "end", False)],
                   label="EAST AFRICA", label_at=[34.5, 5.0], marker=[32.5, 0.5],
                   caption="The circle shows East Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Luganda is spoken in Kampala, "
                          "Entebbe, Jinja and Masaka, in the middle of Uganda. The dashed line shows where most Luganda speakers live.",
                   seas=[("Indian Ocean", 40.5, -6.5)], world_r=16),
    digits=[("0", "zeero", "zeh-roh", "zero"), ("1", "emu", "eh-moo", "one"), ("2", "bbiri", "bbee-ree", "two"),
            ("3", "ssatu", "ssah-too", "three"), ("4", "nnya", "nnyah", "four"), ("5", "ttaano", "ttaa-noh", "five"),
            ("6", "mukaaga", "moo-kaa-gah", "six"), ("7", "musanvu", "moo-sah-nvoo", "seven"), ("8", "munaana", "moo-naa-nah", "eight"),
            ("9", "mwenda", "mweh-ndah", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-laa-moo ah-lay-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-lay-koom as-sah-laam", "And peace be upon you (the reply)"),
             ("Oli otya? · Bulungi!", "oh-lee oh-tyah · boo-loo-ngee", "How are you? · Fine!"),
             ("Erinnya lyange nze …", "eh-ree-nnyah lyah-ngeh nzeh …", "My name is …"),
             ("Webale", "weh-bah-leh", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-kal-lah-hoo khai-ran", "May Allah reward you with good"),
             ("maama · taata", "maa-mah · taa-tah", "Mother · Father"),
             ("muganda wange · mwannyinaze", "moo-gah-ndah wah-ngeh · mwah-nnyee-nah-zeh", "Brother · Sister"),
             ("yee · nedda", "yeh · neh-ddah", "Yes · No"),
             ("Njiga Oluganda!", "njee-gah oh-loo-gah-ndah", "I am learning Luganda!")],
    cheer=("Mashallah! Okoze bulungi!", "maa-shaa-lah! oh-koh-zeh boo-loo-ngee!", "Mashallah! You did well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Check: the bare word forms (<i>bbaluwa, ccupa, ddirisa, ffene, jjinja, kkalaamu, nnanaasi, ppaapaali, ssabbuuni, ttaala</i>) "
                "versus forms with the initial vowel; letter names «ba, ca…»; <i>nnyaanya</i> for NY (starts with nny); "
                "<i>zeero</i> for 0; <i>muganda wange · mwannyinaze</i> (depends on who is speaking); <i>Njiga Oluganda</i>, <i>Okoze bulungi</i>, "
                "the title <i>Ennukuta z’Oluganda</i> and <i>Ekitabo kino kya</i>; whether <i>k/g</i> before <i>i</i> should be shown as ‘ch/j’ "
                "in the sound guides.",
    tiles="ABŊKMZ", cover_pics=["banana", "lg_drum", "pineapple", "mosque"],
    speakers_blurb="Luganda is spoken by more than 10 million people in Uganda, around Kampala and Lake Victoria.",
    sample_words=[("mwezi", "mweh-zee", "moon"), ("ŋŋoma", "ngngoh-mah", "drum"), ("caayi", "chaa-yee", "tea")],
    keywords=["luganda alphabet book for kids", "learn luganda for children", "luganda coloring book",
              "luganda letters tracing workbook", "uganda kids activity book", "muslim kids activity book",
              "islamic coloring book for children"],
))
