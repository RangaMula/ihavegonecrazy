# -*- coding: utf-8 -*-
"""Book 62 - Swahili (Kiswahili, Latin script: 24 letters + 6 letter pairs). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
from _afrolatin import afro_fonts, GLYPH_FONTS, FONT_CREDIT, maker

L = maker("Swahili name · syllables", ["a", "e", "i", "o", "u"])

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "asali", "a-SA-lee", "honey", "honey", vowel=True),
    L("B", "b", "be", "beh", "‘b’ as in “ball”", "barua", "ba-ROO-a", "a letter to post", "envelope"),
    L("Ch", "ch", "che", "cheh", "‘ch’ as in “church”", "chai", "CHA-ee", "tea", "teacup",
      note="Swahili uses C only together with H: <b>ch</b>."),
    L("D", "d", "de", "deh", "‘d’ as in “door”", "dirisha", "dee-REE-sha", "window", "window"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "embe", "EM-beh", "mango", "mango", vowel=True),
    L("F", "f", "fe", "feh", "‘f’ as in “fan”", "fagio", "fa-GEE-o", "broom", "broom"),
    L("G", "g", "ge", "geh", "‘g’ as in “go” (always hard)", "gari", "GA-ree", "cart, car (anything with wheels)", "cart"),
    L("H", "h", "he", "heh", "‘h’ as in “hat”", "hilali", "hee-LA-lee", "new crescent moon", "moon"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "injini", "een-JEE-nee", "engine", "engine", vowel=True),
    L("J", "j", "je", "jeh", "‘j’ as in “jam”", "jua", "JOO-a", "sun", "sun"),
    L("K", "k", "ke", "keh", "‘k’ as in “kite”", "kitabu", "kee-TA-boo", "book", "book", args=dict(left="A B CH", right="D E F")),
    L("L", "l", "le", "leh", "‘l’ as in “lamp”", "limau", "lee-MA-oo", "lemon", "lemon"),
    L("M", "m", "me", "meh", "‘m’ as in “moon”", "msikiti", "m-see-KEE-tee", "mosque", "mosque",
      note="M can be a whole syllable on its own: <i>m-si-ki-ti</i>."),
    L("N", "n", "ne", "neh", "‘n’ as in “net”", "nanasi", "na-NA-see", "pineapple", "pineapple"),
    L("O", "o", "o", "oh", "‘o’ as in “more” (short and pure)", "orofa", "o-RO-fa", "a tall building with floors", "building",
      vowel=True, note="Not many Swahili words start with O, but O is in almost every sentence!"),
    L("P", "p", "pe", "peh", "‘p’ as in “pen”", "pete", "PEH-teh", "ring", "ring"),
    L("R", "r", "re", "reh", "a quick tapped ‘r’", "rangi", "RA-ngee", "colors, paint", "palette"),
    L("S", "s", "se", "seh", "‘s’ as in “sun”", "sabuni", "sa-BOO-nee", "soap", "soap"),
    L("T", "t", "te", "teh", "‘t’ as in “tap”", "tende", "TEH-ndeh", "dates", "dates"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "ua", "OO-a", "flower", "flower", vowel=True),
    L("V", "v", "ve", "veh", "‘v’ as in “van”", "viazi", "vee-A-zee", "potatoes", "potato"),
    L("W", "w", "we", "weh", "‘w’ as in “water”", "wali", "WA-lee", "cooked rice", "rice"),
    L("Y", "y", "ye", "yeh", "‘y’ as in “yes”", "yai", "YA-ee", "egg", "egg"),
    L("Z", "z", "ze", "zeh", "‘z’ as in “zoo”", "zabibu", "za-BEE-boo", "grapes", "grapes"),
]

PAIRS = [
    L("Dh", "dh", "dha", "thah", "‘th’ as in “this” (buzzy)", "dhoruba", "tho-ROO-ba", "storm", "raincloud"),
    L("Gh", "gh", "gha", "ghah", "a soft gargled ‘g’ from the back of the throat, like Arabic غ", "ghuba", "GHOO-ba",
      "bay (where the sea curves into the land)", "waves"),
    L("Ng’", "ng’", "ng’a", "ngah", "‘ng’ as in “sing” — but Swahili can start a word with it!", "kung’aa", "koo-NGA-a",
      "to shine, to sparkle", "star", note="Ng’ hardly ever starts a word you can draw. Find it inside <i>kung’aa</i>!",
      rule="ng’ (with the mark) = “si<b>ng</b>” · ng (no mark) = “fi<b>ng</b>er”"),
    L("Ny", "ny", "nya", "nyah", "‘ny’ as in “canyon”", "nyumba", "NYOO-mba", "house", "house"),
    L("Sh", "sh", "sha", "shah", "‘sh’ as in “ship”", "shamba", "SHA-mba", "farm, field", "paddy"),
    L("Th", "th", "tha", "thah", "‘th’ as in “think” (soft)", "theluji", "theh-LOO-jee", "snow (on a mountain top)", "mountain"),
]

LANG = build(dict(
    code="sw", folder="book-62-swahili", series_no=62, isbn="", draft=True,
    name="Swahili", native="Kiswahili", native_tr="kee-swa-HEE-lee", name_word="jina", write_word="andika",
    title_native="Alfabeti yangu ya kwanza ya Kiswahili", title_letters="AaBbDd", belongs_native="Kitabu hiki ni cha",
    belongs_pic="mango", alphabet_native="alfabeti", numbers_native="nambari", numbers_tr="nam-BA-ree",
    phrases_native="Maneno ya kwanza",
    fonts=afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s Swahili name and its syllables (ba, be, bi, bo, bu)",
    sections=[
        section(LETTERS, native="herufi za Kiswahili", native_tr="heh-ROO-fee za kee-swa-HEE-lee — “the Swahili letters”",
                chart_cols=6, warmup_cols=6,
                intro_html="""<p>Swahili is written with <b>24 letters</b>. It has no Q and no X, and C is only used in the pair <b>ch</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Easy to read aloud</h3>Swahili is written just as it sounds. Every letter is said — there are
no silent letters — and almost every word ends with a vowel.</div>
<div class="box" style="margin:0.1in 0"><h3>Five pure vowels</h3><b>A E I O U</b> always say <i>ah, eh, ee, oh, oo</i>. Swahili children learn to read
by singing the syllables: <i>ba be bi bo bu, cha che chi cho chu…</i></div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(PAIRS, label="PAIR", chip="LETTER PAIRS", title="Letter Pairs", native="herufi mbili",
                native_tr="heh-ROO-fee m-BEE-lee — “two letters”", chart_title="letter pairs", chart_cols=6,
                warmup_title="the letter pairs", warmup_cols=3,
                intro_html="""<p>Some Swahili sounds are written with <b>two letters together</b>. You already know one of them: <b>ch</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Six more pairs</h3><b>dh · gh · ng’ · ny · sh · th</b> — each pair makes <b>one</b> sound.
Many of these sounds came into Swahili with words from Arabic.</div>
<div class="box"><h3>Watch the little mark!</h3><b>ng’</b> (with the mark) sounds like the end of “sing”; <b>ng</b> (no mark) sounds like the
middle of “finger”.</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>a-SA-lee</i> means “say SA a little louder”. In Swahili the stress is almost always on the next-to-last syllable.",
        "<b>m-</b> and <b>n-</b> at the start of a word are said as a short hum: <i>m-see-KEE-tee</i>.",
        "<b>gh</b> is a soft gargle in the throat; <b>th</b> is “think”, <b>dh</b> is “this”.",
        "Every vowel is said on its own: <i>ua</i> is two beats, <i>OO-a</i>."],
    phon_explain="The box marked <i>Swahili name · syllables</i> shows the name Swahili children use for the letter "
                 "(B is «be», CH is «che») and its row of syllables — the way Swahili is taught in school.",
    standard="Standard Swahili (Kiswahili sanifu) as taught in Tanzania and Kenya",
    hello=[
        ("Who speaks it?", "More than <b>70 million people</b> speak Swahili — most of them learn it as a second language, so people from many "
                           "different families can talk together.<sup>³</sup>"),
        ("Where?", "Along the <b>East African coast</b> and far inland: in <b>Tanzania</b>, <b>Kenya</b>, <b>Uganda</b>, the eastern "
                   "<b>Congo</b> and nearby lands, and on islands such as <b>Zanzibar</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. For hundreds of years before that, Swahili poems "
                               "and letters were written in <b>Arabic letters</b>."),
        ("How many letters?", "<b>24 letters</b>, plus <b>letter pairs</b> such as <i>sh</i>, <i>ny</i> and <i>ng’</i> for special sounds."),
        ("A name from the coast", "The name <i>Swahili</i> comes from the Arabic word <i>sawāḥil</i>, “coasts”. It began as the language of "
                                  "the seaside towns!"),
        ("Did you know?", "Many Swahili words come from Arabic: <i>kitabu</i> (book, from <i>kitāb</i>), <i>msikiti</i> (mosque, from "
                          "<i>masjid</i>), <i>dunia</i> (world) and <i>saa</i> (hour, clock)."),
    ],
    hello_pics=[("boat", {}), ("coconut", {}), ("mosque", {})],
    map=region_map(frame=[[26.0, -16.0], [49.0, 7.0]],
                   points=dict(nairobi=[36.82, -1.29], mombasa=[39.67, -4.04], lamu=[40.90, -2.27],
                               zanzibar=[39.19, -6.16], dar=[39.28, -6.79]),
                   area=(37.8, -5.2, 190, 330), area_rot=-15,
                   cities=[("nairobi", "Nairobi", -14, 8, "end", False), ("mombasa", "Mombasa", 14, 8, "start", False),
                           ("lamu", "Lamu", 14, 8, "start", False), ("zanzibar", "Zanzibar", 14, 6, "start", False),
                           ("dar", "Dar es Salaam", -14, 16, "end", False)],
                   label="EAST AFRICA", label_at=[30.0, 4.0], marker=[38.0, -5.0],
                   caption="The circle shows East Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Swahili is spoken in Lamu, Mombasa, "
                          "Zanzibar, Dar es Salaam, Nairobi and all across East Africa. The dashed line shows where most Swahili speakers live.",
                   seas=[("Indian Ocean", 45.5, -9.0)], world_r=16),
    digits=[("0", "sifuri", "see-FOO-ree", "zero"), ("1", "moja", "MO-ja", "one"), ("2", "mbili", "m-BEE-lee", "two"),
            ("3", "tatu", "TA-too", "three"), ("4", "nne", "N-neh", "four"), ("5", "tano", "TA-no", "five"),
            ("6", "sita", "SEE-ta", "six"), ("7", "saba", "SA-ba", "seven"), ("8", "nane", "NA-neh", "eight"),
            ("9", "tisa", "TEE-sa", "nine")],
    phrases=[("Assalamu alaikum", "as-sa-LA-moo a-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Waalaikum salaam", "wa-a-LAY-koom sa-LAAM", "And peace be upon you (the reply)"),
             ("Hujambo? · Sijambo!", "hoo-JA-mbo · see-JA-mbo", "How are you? · I am fine!"),
             ("Jina langu ni …", "JEE-na LA-ngoo nee …", "My name is …"),
             ("Asante", "a-SA-nteh", "Thank you"),
             ("Jazakallahu khairan", "ja-za-KAL-la-hoo KHAI-ran", "May Allah reward you with good"),
             ("mama · baba", "MA-ma · BA-ba", "Mother · Father"),
             ("kaka · dada", "KA-ka · DA-da", "Brother · Sister"),
             ("ndiyo · hapana", "n-DEE-yo · ha-PA-na", "Yes · No"),
             ("Ninajifunza Kiswahili!", "nee-na-jee-FOO-nza kee-swa-HEE-lee", "I am learning Swahili!")],
    cheer=("Mashallah! Hongera!", "MA-sha-la! ho-NGEH-ra!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B CH", right="D E F"),
    review_note="Check the letter names (be, che, de…) against what schools use today; the letter-pair section (dh gh ng’ ny sh th) "
                "and its words — especially <i>kung’aa</i> for NG’ (a verb), <i>ghuba</i> for GH and <i>dhoruba</i> for DH; "
                "<i>orofa</i> (or <i>ghorofa</i>) for O; and the stress marks in the pronunciation guide.",
    tiles="ABDJKZ", cover_pics=["mango", "boat", "mosque", "pineapple"],
    speakers_blurb="Swahili is spoken by more than 70 million people across East Africa.",
    sample_words=[("jua", "JOO-a", "sun"), ("embe", "EM-beh", "mango"), ("kitabu", "kee-TA-boo", "book")],
    keywords=["swahili alphabet book for kids", "learn swahili for children", "kiswahili coloring book",
              "swahili letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual swahili english toddlers"],
))
