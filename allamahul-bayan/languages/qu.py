# -*- coding: utf-8 -*-
"""Book 82 - Quechua (Runasimi), Southern Quechua official alphabet: 3 vowels + 25 consonants = 28 letters.
Allamahul Bayan Series. REVIEW DRAFT. Words follow Cusco-Collao (Southern) Quechua."""
from generic import build, section
from maps import region_map
from _andes import FONTS, GLYPH_FONTS, FONT_CREDIT, maker, ASPIRATE, EJECTIVE

L = maker("Quechua name · syllables", ["a", "i", "u"])

VOWELS = [
    L("A", "a", "a", "a", "‘a’ as in “father”", "achupalla", "a-choo-PA-lya", "pineapple", "pineapple", vowel=True),
    L("I", "i", "i", "ee", "‘ee’ as in “see” — but next to Q it sounds like ‘e’ in “bed”", "inti", "EEN-tee", "sun", "sun",
      vowel=True, rule="qi sounds like “qe” · iq sounds like “eq”"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon” — but next to Q it sounds like ‘o’ in “more”", "unu", "OO-noo", "water", "water",
      vowel=True, rule="qu sounds like “qo” · uq sounds like “oq”"),
]

CONS = [
    L("Ch", "ch", "cha", "chah", "‘ch’ as in “chair”", "chaka", "CHA-ka", "bridge", "qu_bridge",
      note="The Andes are famous for bridges woven from grass rope!"),
    L("Chh", "chh", "chha", "chhah", f"‘ch’ {ASPIRATE}", "chhullunku", "chhoo-LYOON-koo", "ice", "ice"),
    L("Ch’", "ch’", "ch’a", "ch’ah", f"‘ch’ as {EJECTIVE}", "ch’aska", "CH’AS-ka", "star (the bright morning star)", "star"),
    L("H", "h", "ha", "hah", "‘h’ as in “hat”", "hampi", "HAM-pee", "medicine", "medicine"),
    L("K", "k", "ka", "kah", "‘k’ as in “sky” (no puff of air)", "kachi", "KA-chee", "salt", "salt", args=dict(label="kachi")),
    L("Kh", "kh", "kha", "khah", f"‘k’ {ASPIRATE}", "khipu", "KHEE-poo", "khipu — knotted cords for keeping numbers", "qu_khipu",
      note="Long ago the Inca kept their counts on knotted cords called <i>khipu</i>."),
    L("K’", "k’", "k’a", "k’ah", f"‘k’ as {EJECTIVE}", "k’aspi", "K’AS-pee", "stick", "qu_stick"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lirpu", "LEER-poo", "mirror", "mirror"),
    L("Ll", "ll", "lla", "lyah", "‘lli’ as in “million”", "llimp’i", "LYEEM-p’ee", "colors, paint", "palette"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "manka", "MAN-ka", "cooking pot", "pot"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "nina", "NEE-na", "fire", "qu_fire"),
    L("Ñ", "ñ", "ña", "nyah", "‘ny’ as in “canyon”", "ñan", "nyan", "path, road", "qu_path"),
    L("P", "p", "pa", "pah", "‘p’ as in “spin” (no puff of air)", "papa", "PA-pa", "potato", "potato",
      note="The potato comes from the Andes! Quechua farmers grow hundreds of kinds."),
    L("Ph", "ph", "pha", "phah", f"‘p’ {ASPIRATE} — not an ‘f’!", "phuyu", "PHOO-yoo", "cloud", "clouds"),
    L("P’", "p’", "p’a", "p’ah", f"‘p’ as {EJECTIVE}", "p’uyñu", "P’OOY-nyoo", "clay water jug", "jar"),
    L("Q", "q", "qa", "qah", "a ‘k’ made far back in the throat", "qucha", "QO-cha", "lake", "qu_lake",
      rule="say ‘k’, then move your tongue further back"),
    L("Qh", "qh", "qha", "qhah", "a deep throaty ‘q’ with a rush of air, almost like clearing your throat", "qhichwa", "QHECH-wa",
      "warm valley", "mountain", note="The name <i>Quechua</i> comes from <i>qhichwa</i>, the warm valleys between the mountains."),
    L("Q’", "q’", "q’a", "q’ah", f"a deep ‘q’ as {EJECTIVE}", "q’aytu", "Q’AY-too", "thread, yarn", "wool"),
    L("R", "r", "ra", "rah", "a quick tapped ‘r’", "rumi", "ROO-mee", "stone", "qu_stones"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sara", "SA-ra", "maize, corn", "corn"),
    L("T", "t", "ta", "tah", "‘t’ as in “stop” (no puff of air)", "tiyana", "tee-YA-na", "seat, stool", "stool"),
    L("Th", "th", "tha", "thah", f"‘t’ {ASPIRATE} — not the ‘th’ of “think”!", "thaya", "THA-ya", "icy wind", "qu_wind"),
    L("T’", "t’", "t’a", "t’ah", f"‘t’ as {EJECTIVE}", "t’ika", "T’EE-ka", "flower", "flower"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "wasi", "WA-see", "house", "house"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "yura", "YOO-ra", "plant", "tree"),
]

LANG = build(dict(
    code="qu", folder="book-82-quechua", series_no=82, isbn="", draft=True,
    name="Quechua", native="Runasimi", native_tr="roo-na-SEE-mee", name_word="suti", write_word="qillqay",
    title_native="Runasimi qillqakuna", title_letters="AaIiUu", belongs_native="Kay p’anqaq dueñun",
    belongs_pic="flower", alphabet_native="qillqakuna", numbers_native="yupaykuna", numbers_tr="yoo-pay-KOO-na",
    phrases_native="Ñawpaq rimaykuna",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s Quechua name and its syllables (cha, chi, chu)",
    sections=[
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels", native="vocalkuna",
                native_tr="vo-kal-KOO-na — “the vowels”", chart_title="vowels", chart_cols=3, warmup_title="the vowels", warmup_cols=3,
                intro_html="""<p>Quechua is written with only <b>three vowels</b>: <b>a, i, u</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Three vowels, five sounds</h3>Next to the deep letter <b>Q</b>, <b>i</b> sounds like “e” and
<b>u</b> sounds like “o”: <i>qucha</i> (lake) is said “QO-cha”. You still write <b>u</b>!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(CONS, label="LETTER", chip="THE CONSONANTS", title="The Consonants", native="consonantekuna",
                native_tr="kon-so-nan-teh-KOO-na — “the consonants”", chart_title="consonants", chart_cols=5,
                warmup_title="the consonants", warmup_cols=5,
                intro_html="""<p>Quechua has <b>25 consonants</b>. Some are written with <b>two or three letters</b>: <b>ch, ll</b> and the families below.</p>
<div class="box" style="margin:0.1in 0"><h3>Plain, puffy and popping</h3>Many sounds come in threes. <b>k</b> is plain, <b>kh</b> has a
<b>puff of air</b>, and <b>k’</b> <b>pops</b> in the throat. The same goes for <b>ch · chh · ch’</b>, <b>p · ph · p’</b>, <b>q · qh · q’</b>
and <b>t · th · t’</b>.</div>
<div class="box"><h3>Watch the little mark!</h3>The mark <b>’</b> is part of the letter. <i>t’ika</i> (flower) and <i>tika</i> are
different words — so never leave it out!</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>WA-see</i> means “say WA a little louder”. Quechua almost always stresses the next-to-last syllable.",
        "<b>h</b> after a letter (<i>kh, ph, th, chh, qh</i>) means a strong puff of air. <b>ph</b> is not “f” and <b>th</b> is not the “th” of “think”.",
        "<b>’</b> after a letter (<i>k’, p’, t’, ch’, q’</i>) means a “popping” sound made with the throat closed.",
        "<b>q</b> in the sound guide is a ‘k’ made far back in the throat; <b>ly</b> is the ‘lli’ in “million”; <b>ny</b> is the ‘ny’ in “canyon”."],
    phon_explain="The box marked <i>Quechua name · syllables</i> shows how the letter is called (<i>ka, kha, k’a</i>…) and its row of "
                 "syllables with the three vowels — the way Quechua is taught in school.",
    standard="Southern Quechua (Cusco–Collao), official alphabet of Peru",
    hello=[
        ("Who speaks it?", "About <b>8 million people</b> speak Quechua languages — more than any other native language of the Americas.<sup>³</sup>"),
        ("Where?", "High in the <b>Andes mountains</b>: in <b>Peru</b>, <b>Bolivia</b> and <b>Ecuador</b>, and also in parts of Argentina, "
                   "Chile and Colombia."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. The Inca kept numbers on knotted cords called "
                               "<i>khipu</i>."),
        ("How many letters?", "<b>28 letters</b> in the official Southern Quechua alphabet: <b>3 vowels</b> and <b>25 consonants</b>."),
        ("Its own name", "Speakers call their language <i>Runasimi</i>, “the people’s speech”: <i>runa</i> (people) + <i>simi</i> (mouth, words)."),
        ("Did you know?", "English has borrowed Quechua words: <i>quinoa</i> (from <i>kinwa</i>), <i>jerky</i> (from <i>ch’arki</i>, dried meat), "
                          "<i>llama</i>, <i>condor</i> and <i>puma</i>."),
    ],
    hello_pics=[("potato", {}), ("corn", {}), ("qu_khipu", {})],
    map=region_map(frame=[[-82.0, -25.0], [-58.0, -1.0]],
                   points=dict(cusco=[-71.97, -13.53], ayacucho=[-74.22, -13.16], puno=[-70.02, -15.84],
                               cochabamba=[-66.16, -17.39], potosi=[-65.75, -19.58]),
                   area=(-69.6, -16.0, 240, 120), area_rot=35,
                   cities=[("cusco", "Cusco", 14, -6, "start", False), ("ayacucho", "Ayacucho", -14, 8, "end", False),
                           ("puno", "Puno", -14, 16, "end", False), ("cochabamba", "Cochabamba", 14, 8, "start", False),
                           ("potosi", "Potosí", 14, 8, "start", False)],
                   label="THE ANDES", label_at=[-66.0, -6.0], marker=[-72.0, -14.0],
                   caption="The circle shows the Andes on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Southern Quechua is spoken in Cusco, "
                          "Ayacucho, Puno, Cochabamba and Potosí, high in the Andes. The dashed line shows where most speakers live.",
                   seas=[("Pacific Ocean", -78.0, -20.0)], world_r=16),
    digits=[("0", "ch’usaq", "CH’OO-sak", "zero (“empty”)"), ("1", "huk", "hook", "one"), ("2", "iskay", "EES-kay", "two"),
            ("3", "kimsa", "KEEM-sa", "three"), ("4", "tawa", "TA-wa", "four"), ("5", "pichqa", "PEECH-qa", "five"),
            ("6", "suqta", "SOQ-ta", "six"), ("7", "qanchis", "QAN-chees", "seven"), ("8", "pusaq", "POO-saq", "eight"),
            ("9", "isqun", "EES-qon", "nine")],
    phrases=[("Assalamu alaikum", "as-sa-LA-moo a-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wa a-LAY-koom as-sa-LAM", "And peace be upon you (the reply)"),
             ("Allillanchu? · Allillanmi!", "a-lyee-LYAN-choo · a-lyee-LYAN-mee", "Are you well? · I am well!"),
             ("Sutiymi …", "soo-TEEY-mee …", "My name is …"),
             ("Sulpayki", "sool-PAY-kee", "Thank you"),
             ("Jazakallahu khairan", "ja-za-KAL-la-hoo KHAI-ran", "May Allah reward you with good"),
             ("mama · tayta", "MA-ma · TAY-ta", "Mother · Father"),
             ("wawqi · pana", "WAW-kee · PA-na", "Brother · Sister (said by a boy)"),
             ("arí · manan", "a-REE · MA-nan", "Yes · No"),
             ("Runasimita yachakuchkani!", "roo-na-see-MEE-ta ya-cha-koo-CHKA-nee", "I am learning Quechua!")],
    cheer=("Mashallah! Ancha allin!", "MA-sha-la! AN-cha A-lyeen!", "Mashallah! Very good — well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded, for all Quechua languages together.",
    book_pic=dict(left="A I U", right="CH K P"),
    review_note="Words follow Cusco–Collao Southern Quechua; Ayacucho speakers have no aspirated/popping letters and say e.g. "
                "<i>tika</i>, <i>kaspi</i>. Please check: <i>lirpu</i> (mirror), <i>llimp’i</i> (colors), <i>p’uyñu</i> (clay jug), "
                "<i>thaya</i> (icy wind) and <i>chhullunku</i> (ice, also written <i>chullunku</i>); the Quechua title, "
                "“Kay p’anqaq dueñun” (owner of this book), “Runasimita yachakuchkani” and the letter-group names "
                "(<i>vocalkuna</i>, <i>consonantekuna</i>); zero as <i>ch’usaq</i>; and the stressed syllables in the sound guide.",
    tiles="AIUÑQK", cover_pics=["potato", "qu_bridge", "corn", "flower"], title_size=48,
    speakers_blurb="Quechua, the language of the Andes, is spoken by about 8 million people in Peru, Bolivia, Ecuador and beyond.",
    sample_words=[("inti", "EEN-tee", "sun"), ("t’ika", "T’EE-ka", "flower"), ("papa", "PA-pa", "potato")],
    keywords=["quechua alphabet book for kids", "learn quechua runasimi children", "quechua coloring book",
              "andes language tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "peru bolivia native language for toddlers"],
))
