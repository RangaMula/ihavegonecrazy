# -*- coding: utf-8 -*-
"""Book 84 - Aymara (Aymar aru), official alphabet: 3 vowels + 3 long vowels (Ä Ï Ü) + 26 consonants = 32 letters.
Allamahul Bayan Series. REVIEW DRAFT. Words follow Central (La Paz / Altiplano) Aymara."""
from generic import build, section
from maps import region_map
from _andes import FONTS, GLYPH_FONTS, FONT_CREDIT, maker, ASPIRATE, EJECTIVE

L = maker("Aymara name · syllables", ["a", "i", "u"])

VOWELS = [
    L("A", "a", "a", "a", "‘a’ as in “father”", "awayu", "a-WA-yu", "woven cloth for carrying things", "scarf", vowel=True),
    L("I", "i", "i", "i", "‘i’ as in “machine” — but next to Q or X it sounds like ‘e’ in “bed”", "inti", "IN-ti", "sun", "sun",
      vowel=True),
    L("U", "u", "u", "u", "‘u’ as in “rule” — but next to Q or X it sounds like ‘o’ in “more”", "uta", "U-ta", "house", "house",
      vowel=True),
]

LONG = [
    L("Ä", "ä", "ä", "aa", "a long ‘aa’ — hold the ‘a’ twice as long", "llätunka", "lyaa-TUN-ka", "nine", "ay_count",
      args=dict(n=9), vowel=True, row="a · ä",
      note="Long vowels never start a word. Find <b>ä</b> inside <i>llätunka</i> — count the nine flowers!"),
    L("Ï", "ï", "ï", "ii", "a long ‘ii’ — hold the ‘i’ twice as long", "jïsa", "HII-sa", "yes!", "ay_tick", vowel=True, row="i · ï",
      note="Find <b>ï</b> inside <i>jïsa</i>, “yes”. Some writers spell it <i>jisa</i>."),
    L("Ü", "ü", "ü", "uu", "a long ‘uu’ — hold the ‘u’ twice as long", "jichhüru", "hi-CHHUU-ru", "today", "ay_calendar",
      vowel=True, row="u · ü",
      note="<i>jichha</i> (now) + <i>uru</i> (day) = <i>jichhüru</i>, “today”. The two vowels melt into one long <b>ü</b>."),
]

CONS = [
    L("Ch", "ch", "cha", "chah", "‘ch’ as in “chair”", "chuwa", "CHU-wa", "bowl, plate", "plate"),
    L("Chh", "chh", "chha", "chhah", f"‘ch’ {ASPIRATE}", "chhullunkhiya", "chhu-lyun-KHI-ya", "ice", "ice"),
    L("Ch’", "ch’", "ch’a", "ch’ah", f"‘ch’ as {EJECTIVE}", "ch’uqi", "CH’O-qe", "potato", "potato",
      note="The potato comes from the land around Lake Titicaca! Aymara farmers grow hundreds of kinds."),
    L("J", "j", "ja", "hah", "a breathy ‘h’, like Spanish J", "jallu", "HA-lyu", "rain", "raincloud"),
    L("K", "k", "ka", "kah", "‘k’ as in “sky” (no puff of air)", "kimsa", "KIM-sa", "three", "ay_count", args=dict(n=3)),
    L("Kh", "kh", "kha", "khah", f"‘k’ {ASPIRATE}", "khunu", "KHU-nu", "snow", "ay_snow"),
    L("K’", "k’", "k’a", "k’ah", f"‘k’ as {EJECTIVE}", "k’awna", "K’AW-na", "egg", "egg"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "laphi", "LA-phi", "leaf", "ay_leaf"),
    L("Ll", "ll", "lla", "lyah", "‘lli’ as in “million”", "llant’a", "LYAN-t’a", "firewood", "ay_logs"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "misk’i", "MIS-k’i", "honey", "honey"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "nina", "NI-na", "fire", "qu_fire"),
    L("Ñ", "ñ", "ña", "nyah", "‘ny’ as in “canyon”", "ch’uxña", "CH’OKH-nya", "green", "tree",
      note="Ñ hardly ever starts a word. Find it inside <i>ch’uxña</i>, “green” — and color the tree green!"),
    L("P", "p", "pa", "pah", "‘p’ as in “spin” (no puff of air)", "panqara", "pan-QA-ra", "flower", "flower"),
    L("Ph", "ph", "pha", "phah", f"‘p’ {ASPIRATE} — not an ‘f’!", "phaxsi", "PHAKH-si", "moon", "moon"),
    L("P’", "p’", "p’a", "p’ah", f"‘p’ as {EJECTIVE}", "p’uñu", "P’U-nyu", "clay water jug", "jar"),
    L("Q", "q", "qa", "qah", "a ‘k’ made far back in the throat", "quta", "QO-ta", "lake", "qu_lake",
      note="The great lake of the Aymara is <i>Titiqaqa</i> (Lake Titicaca), high in the mountains."),
    L("Qh", "qh", "qha", "qhah", "a deep throaty ‘q’ with a rush of air", "qhantati", "qhan-TA-ti", "dawn, sunrise", "sunrise"),
    L("Q’", "q’", "q’a", "q’ah", f"a deep ‘q’ as {EJECTIVE}", "q’ipi", "Q’E-pe", "bundle carried on the back", "ay_bundle"),
    L("R", "r", "ra", "rah", "a quick tapped ‘r’", "jawira", "ha-WI-ra", "river", "ay_river",
      note="Aymara words never start with R. Find it inside <i>jawira</i>!"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "suni", "SU-ni", "high, cold mountain land", "mountain"),
    L("T", "t", "ta", "tah", "‘t’ as in “stop” (no puff of air)", "tunqu", "TUN-qo", "maize, corn", "corn"),
    L("Th", "th", "tha", "thah", f"‘t’ {ASPIRATE} — not the ‘th’ of “think”!", "thaya", "THA-ya", "cold, icy wind", "qu_wind"),
    L("T’", "t’", "t’a", "t’ah", f"‘t’ as {EJECTIVE}", "t’ant’a", "T’AN-t’a", "bread", "ay_bread"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "warawara", "wa-ra-WA-ra", "star", "star"),
    L("X", "x", "xa", "khah", "a rough ‘h’ from deep in the throat, like clearing your throat softly", "suxta", "SOKH-ta", "six",
      "ay_count", args=dict(n=6), note="X hardly ever starts a word. Find it inside <i>suxta</i> — count the six flowers!"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "yapu", "YA-pu", "farm field", "ay_field"),
]

LANG = build(dict(
    code="ay", folder="book-84-aymara", series_no=84, isbn="", draft=True,
    name="Aymara", native="Aymar aru", native_tr="AY-mar A-ru", name_word="suti", write_word="qillqaña",
    title_native="Aymar aru qillqanaka", title_letters="AaÄäXx", belongs_native="Aka pankana dueñopa",
    belongs_pic="flower", alphabet_native="qillqanaka", numbers_native="jakhunaka", numbers_tr="ha-khu-NA-ka",
    phrases_native="Nayriri arunaka",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s Aymara name and its syllables (cha, chi, chu)",
    sections=[
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels", native="vocalanaka",
                native_tr="vo-ka-la-NA-ka — “the vowels”", chart_title="vowels", chart_cols=3, warmup_title="the vowels", warmup_cols=3,
                intro_html="""<p>Aymara is written with only <b>three vowels</b>: <b>a, i, u</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Three vowels, five sounds</h3>Next to the deep letters <b>Q</b> and <b>X</b>, <b>i</b> sounds like “e”
and <b>u</b> sounds like “o”: <i>quta</i> (lake) is said “QO-ta”. You still write <b>u</b>!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(LONG, label="LONG VOWEL", chip="LONG VOWELS", title="Long Vowels", native="jach’a vocalanaka",
                native_tr="HA-ch’a vo-ka-la-NA-ka — “big vowels”", chart_title="long vowels", chart_cols=3,
                warmup_title="the long vowels", warmup_cols=3,
                intro_html="""<p>Two little dots on top make a vowel <b>long</b>: <b>ä · ï · ü</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Hold it longer!</h3>Say <b>a</b>, then say <b>ä</b> twice as long: <i>aa</i>. A long vowel can change
the meaning of a word, so listen carefully.</div>
<div class="box"><h3>Inside words</h3>Long vowels never start a word. They often appear where two vowels melt together:
<i>jichha</i> + <i>uru</i> = <i>jichhüru</i> (today).</div>"""),
        section(CONS, label="LETTER", chip="THE CONSONANTS", title="The Consonants", native="consonantenaka",
                native_tr="kon-so-nan-te-NA-ka — “the consonants”", chart_title="consonants", chart_cols=5,
                warmup_title="the consonants", warmup_cols=5,
                intro_html="""<p>Aymara has <b>26 consonants</b>. Some are written with <b>two or three letters</b>: <b>ch, ll</b> and the families below.</p>
<div class="box" style="margin:0.1in 0"><h3>Plain, puffy and popping</h3>Many sounds come in threes. <b>k</b> is plain, <b>kh</b> has a
<b>puff of air</b>, and <b>k’</b> <b>pops</b> in the throat. The same goes for <b>ch · chh · ch’</b>, <b>p · ph · p’</b>, <b>q · qh · q’</b>
and <b>t · th · t’</b>.</div>
<div class="box"><h3>J and X</h3><b>j</b> is a soft breathy ‘h’. <b>x</b> is a rougher ‘h’ made deep in the throat — it is
<b>not</b> the English ‘ks’!</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>U-ta</i> means “say U a little louder”. Aymara usually stresses the next-to-last syllable.",
        "In this book <b>i</b> sounds like “machine” and <b>u</b> like “rule”; <b>doubled vowels</b> (<i>aa, ii, uu</i>) are the long vowels ä, ï, ü.",
        "<b>h</b> after a letter (<i>kh, ph, th, chh, qh</i>) means a strong puff of air; <b>’</b> after a letter means a “popping” sound.",
        "<b>q</b> is a ‘k’ far back in the throat; <b>kh</b> after a vowel (as in <i>SOKH-ta</i>) is the rough throat sound of X; "
        "<b>ly</b> is the ‘lli’ in “million”; <b>ny</b> is the ‘ny’ in “canyon”."],
    phon_explain="The box marked <i>Aymara name · syllables</i> shows how the letter is called (<i>ka, kha, k’a</i>…) and its row of "
                 "syllables with the three vowels — the way Aymara is taught in school.",
    standard="Central Aymara (La Paz and the Altiplano), official alphabet",
    hello=[
        ("Who speaks it?", "About <b>2 million people</b> speak Aymara.<sup>³</sup>"),
        ("Where?", "On the high plains of the <b>Andes</b> around <b>Lake Titicaca</b>: in <b>Bolivia</b>, southern <b>Peru</b> and northern "
                   "<b>Chile</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with marks for puffs of air (<b>h</b>), "
                               "popping sounds (<b>’</b>) and long vowels (<b>¨</b>)."),
        ("How many letters?", "<b>32 letters</b> in this book: <b>3 vowels</b>, <b>3 long vowels</b> and <b>26 consonants</b>."),
        ("High up!", "Lake Titicaca lies about <b>3,800 metres</b> above the sea — one of the highest big lakes in the world."),
        ("Did you know?", "In Aymara, <i>nayra</i> means both “eye” and “the past”. The past is <b>in front</b> of you, because you "
                          "can already see it!"),
    ],
    hello_pics=[("qu_lake", {}), ("potato", {}), ("scarf", {})],
    map=region_map(frame=[[-76.0, -26.0], [-60.0, -10.0]],
                   points=dict(lapaz=[-68.15, -16.50], puno=[-70.02, -15.84], oruro=[-67.11, -17.97], arica=[-70.31, -18.48],
                               potosi=[-65.75, -19.58]),
                   area=(-68.6, -17.1, 170, 95), area_rot=40,
                   cities=[("lapaz", "La Paz", 14, 8, "start", False), ("puno", "Puno", -14, 8, "end", False),
                           ("oruro", "Oruro", 14, 8, "start", False), ("arica", "Arica", -14, 8, "end", False),
                           ("potosi", "Potosí", 14, 8, "start", False)],
                   label="THE ALTIPLANO", label_at=[-68.5, -12.5], marker=[-68.5, -17.0],
                   caption="The circle shows the Altiplano on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Aymara is spoken in La Paz, Puno and "
                          "Oruro, on the high plains around Lake Titicaca, and down to Arica by the sea. The dashed line shows where most "
                          "speakers live.",
                   seas=[("Pacific Ocean", -73.5, -22.0)], world_r=14),
    digits=[("0", "ch’usa", "CH’U-sa", "zero (“empty”)"), ("1", "maya", "MA-ya", "one"), ("2", "paya", "PA-ya", "two"),
            ("3", "kimsa", "KIM-sa", "three"), ("4", "pusi", "PU-si", "four"), ("5", "phisqa", "PHES-qa", "five"),
            ("6", "suxta", "SOKH-ta", "six"), ("7", "paqallqu", "pa-QALY-qo", "seven"), ("8", "kimsaqallqu", "kim-sa-QALY-qo", "eight"),
            ("9", "llätunka", "lyaa-TUN-ka", "nine")],
    phrases=[("Assalamu alaikum", "as-sa-LA-mu a-LAY-kum", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wa a-LAY-kum as-sa-LAM", "And peace be upon you (the reply)"),
             ("Kamisaki? · Waliki!", "ka-mi-SA-ki · wa-LI-ki", "How are you? · I am fine!"),
             ("Nayan sutijaxa …", "NA-yan su-ti-HA-kha …", "My name is …"),
             ("Yuspagara", "yus-pa-GA-ra", "Thank you"),
             ("Jazakallahu khairan", "ja-za-KAL-la-hu KHAI-ran", "May Allah reward you with good"),
             ("tayka · awki", "TAY-ka · AW-ki", "Mother · Father"),
             ("jilata · kullaka", "hi-LA-ta · ku-LYA-ka", "Brother · Sister"),
             ("jïsa · janiwa", "HII-sa · ha-NI-wa", "Yes · No"),
             ("Aymar aru yatiqasktwa!", "AY-mar A-ru ya-ti-QASK-twa", "I am learning Aymara!")],
    cheer=("Mashallah! Wali suma!", "MA-sha-la! WA-li SU-ma!", "Mashallah! Very good — well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A I U", right="Ä Ï Ü"),
    review_note="Words follow Central (La Paz) Aymara; spellings vary between writers. Please check: the long-vowel words "
                "<i>llätunka</i> (nine), <i>jïsa</i> (yes — often written <i>jisa</i>) and <i>jichhüru</i> (today); <i>chuwa</i> (bowl), "
                "<i>chhullunkhiya</i> (ice), <i>k’awna</i> (egg), <i>misk’i</i> (honey), <i>p’uñu</i> (clay jug), <i>q’ipi</i> (bundle), "
                "<i>suni</i> (highland), <i>ch’uxña</i> (green); the title “Aymar aru qillqanaka”, “Aka pankana dueñopa” (owner of this book), "
                "<i>Nayriri arunaka</i>, <i>vocalanaka / jach’a vocalanaka / consonantenaka</i>, “Nayan sutijaxa …”, “Aymar aru yatiqasktwa”, "
                "<i>ch’usa</i> for zero; and the stressed syllables in the sound guide.",
    tiles="AÄQXKÑ", cover_pics=["qu_lake", "potato", "star", "flower"], title_size=48,
    speakers_blurb="Aymara is spoken by about 2 million people on the high plains of the Andes around Lake Titicaca.",
    sample_words=[("uta", "U-ta", "house"), ("phaxsi", "PHAKH-si", "moon"), ("panqara", "pan-QA-ra", "flower")],
    keywords=["aymara alphabet book for kids", "learn aymara children", "aymara coloring book",
              "andes language tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bolivia peru native language for toddlers"],
))
