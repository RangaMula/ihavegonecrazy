# -*- coding: utf-8 -*-
"""Book 78 - Setswana (Tswana, Latin script: 21 letters + 6 letter groups). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
import _afrolatin as AF

L = AF.maker("Setswana sound · syllables", ["a", "e", "i", "o", "u"])

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "apole", "ah-POH-leh", "apple", "apple", vowel=True),
    L("B", "b", "ba", "bah", "‘b’ as in “ball” (soft, lips barely touching)", "buka", "BOO-kah", "book", "book",
      args=dict(left="A B D", right="E F G")),
    L("D", "d", "da", "dah", "‘d’ as in “door” — in Setswana it comes before <b>i</b> and <b>u</b>", "dithunya", "dee-TOO-nyah",
      "flowers", "flower", rule="la · le · lo but di · du: L turns into D before i and u!"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”, or ‘ay’ as in “day”", "lee", "LEH-eh", "egg", "egg", vowel=True,
      note="Few Setswana naming words start with E. Find it twice in <i>lee</i> — say each e!"),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "fensetere", "fen-seh-TEH-reh", "window", "window"),
    L("G", "g", "ga", "khah", "a rasping sound in the throat, like Arabic <b>خ</b> (kh) — never ‘g’ as in “go”", "galase",
      "khah-LAH-seh", "drinking glass", "tn_glass"),
    L("H", "h", "ha", "hah", "‘h’ as in “hat” (mostly in words from other languages)", "hempe", "HEM-peh", "shirt", "tn_shirt"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "metsi", "MEH-tsee", "water", "water", vowel=True,
      note="Few Setswana words start with I. Find it at the end of <i>metsi</i>!"),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "bojang", "boh-JAHNG", "grass", "tn_grass",
      note="Find J in the middle of <i>bojang</i>."),
    L("K", "k", "ka", "kah", "‘k’ as in “skip” (no puff of air)", "kopi", "KOH-pee", "cup", "teacup"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "letsatsi", "leh-TSAH-tsee", "sun", "sun"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "maru", "MAH-roo", "clouds", "clouds"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "naledi", "nah-LEH-dee", "star", "star"),
    L("O", "o", "o", "oh", "‘o’ as in “more”, or ‘oh’ as in “go”", "molelo", "moh-LEH-loh", "fire", "tn_fire", vowel=True,
      note="Few Setswana naming words start with O. Find it twice in <i>molelo</i>!"),
    L("P", "p", "pa", "pah", "‘p’ as in “spin” (no puff of air)", "pitsa", "PEE-tsah", "cooking pot", "pot"),
    L("R", "r", "ra", "rah", "a rolled ‘r’ — let your tongue buzz!", "raese", "rah-EH-seh", "rice", "rice"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sefofane", "seh-foh-FAH-neh", "aeroplane", "plane"),
    L("T", "t", "ta", "tah", "‘t’ as in “stop” (no puff of air)", "tamati", "tah-MAH-tee", "tomato", "tomato"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "pula", "POO-lah", "rain", "raincloud", vowel=True,
      note="Find U in <i>pula</i> — the most loved word in a dry land!"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "lewatle", "leh-WAH-tleh", "sea", "waves",
      note="Find W in the middle of <i>lewatle</i>."),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "seyalemoya", "seh-yah-leh-MOH-yah", "radio (“it goes on the wind”)", "tn_radio",
      note="Find Y twice in <i>seyalemoya</i>!"),
]

GROUPS = [
    L("Kg", "kg", "kga", "kkhah", "a ‘k’ and the throaty G-sound (kh) said together", "kgwedi", "KKHWEH-dee", "moon, month", "moon"),
    L("Th", "th", "tha", "t’hah", "a ‘t’ with a strong puff of air — <b>not</b> the ‘th’ of “think”!", "thaba", "T’HAH-bah",
      "mountain", "mountain", rule="t = no puff · th = big puff of air"),
    L("Tl", "tl", "tla", "tlah", "‘t’ and ‘l’ said together, like the end of “bottle”", "ntlo", "N-tloh", "house", "house",
      note="Find TL inside <i>ntlo</i>: the N at the front is a short hum."),
    L("Tlh", "tlh", "tlha", "tlhah", "like TL, but with a puff of air out past the sides of the tongue", "setlhare", "seh-TLHAH-reh",
      "tree", "tree", note="Three letters, one sound! Find TLH inside <i>setlhare</i>."),
    L("Ts", "ts", "tsa", "tsah", "‘ts’ as in “cats”", "tsela", "TSEH-lah", "road, path", "tn_road"),
    L("Tsh", "tsh", "tsha", "ts’hah", "‘ts’ with a strong puff of air", "tshimo", "TS’HEE-moh", "field, farm", "corn"),
]

LANG = build(dict(
    code="tn", folder="book-78-setswana", series_no=78, isbn="", draft=True,
    name="Setswana", native="Setswana", native_tr="seh-TSWAH-nah", name_word="leina", write_word="kwala",
    title_native="Ditlhaka tsa me tsa ntlha tsa Setswana", title_letters="AaBbDd", belongs_native="Buka e ke ya",
    belongs_pic="star", alphabet_native="ditlhaka", numbers_native="dipalo", numbers_tr="dee-PAH-loh",
    phrases_native="Mafoko a ntlha",
    fonts=AF.afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=AF.GLYPH_FONTS, font_credit=AF.FONT_CREDIT, extra_css=getattr(AF, "EXTRA_CSS", ""),
    phon_feature="each letter’s sound and its syllables (ba, be, bi, bo, bu)",
    sections=[
        section(LETTERS, native="ditlhaka tsa Setswana", native_tr="dee-TLHAH-kah tsah seh-TSWAH-nah — “the Setswana letters”",
                chart_cols=7, warmup_cols=6,
                intro_html="""<p>Setswana is written with <b>21 letters</b>. Words of its own use no C, Q, V, X or Z.</p>
<div class="box" style="margin:0.1in 0"><h3>Easy to read aloud</h3>Setswana is written just as it sounds, and almost every word ends with a vowel.
Children learn to read by singing the syllables: <i>ba be bi bo bu, da de di do du…</i></div>
<div class="box" style="margin:0.1in 0"><h3>Five vowels</h3><b>A E I O U</b> say <i>ah, eh, ee, oh, oo</i>. E and O each have an open and a closed sound,
like “bed”/“day” and “more”/“go”.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(GROUPS, label="GROUP", chip="LETTER GROUPS", title="Letter Groups", native="ditlhaka tse di kopaneng",
                native_tr="dee-TLHAH-kah tseh dee koh-pah-NENG — “letters that join together”",
                chart_title="letter groups", chart_cols=6, warmup_title="the letter groups", warmup_cols=3,
                intro_html="""<p>Some Setswana sounds are written with <b>two or three letters together</b>. Each group makes <b>one</b> sound.</p>
<div class="box" style="margin:0.1in 0"><h3>Puff of air</h3>An <b>h</b> after a letter means “add a puff of air”: <b>t</b> is soft, <b>th</b> puffs.
Hold your hand in front of your mouth and feel the difference!</div>
<div class="box"><h3>Special Setswana sounds</h3><b>tl</b> and <b>tlh</b> are said with the sides of the tongue, and <b>kg</b> rasps in the
throat. Practise them slowly: <i>ntlo, setlhare, kgwedi</i>.</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>leh-TSAH-tsee</i> means “say TSAH a little louder”. Setswana stress is usually on the next-to-last syllable.",
        "<b>kh</b> in the English guide is the rasping throat sound of Setswana <b>g</b>, like Arabic خ.",
        "<b>t’h</b> and <b>ts’h</b> mean a strong puff of air after the t — not the ‘th’ of “think”.",
        "<b>N-</b> or <b>M-</b> at the start of a word is a short hum: <i>N-tloh</i>."],
    phon_explain="The box marked <i>Setswana sound · syllables</i> shows the letter as Setswana children say it (B is «ba») "
                 "and its row of syllables — the way Setswana is taught in school.",
    standard="Standard Setswana as written in Botswana and South Africa",
    hello=[
        ("Who speaks it?", "More than <b>10 million people</b> speak Setswana, as their first language or as a second one.<sup>³</sup>"),
        ("Where?", "In <b>Botswana</b>, where almost everyone speaks it, and in <b>South Africa</b>, mostly in the North West. "
                   "Smaller groups live in <b>Namibia</b> and <b>Zimbabwe</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with letter groups such as <i>tl</i>, <i>tlh</i> and "
                               "<i>kg</i> for its special sounds."),
        ("How many letters?", "<b>21 letters</b>, plus <b>letter groups</b> such as <i>th</i>, <i>ts</i> and <i>tsh</i>."),
        ("One word, many shapes", "A <b>Motswana</b> is one person, the <b>Batswana</b> are the people, <b>Setswana</b> is the language and "
                                  "<b>Botswana</b> is the land!"),
        ("Did you know?", "Botswana’s money is called <i>pula</i>, which means <b>rain</b>. In a dry land, rain is a precious blessing. "
                          "People even say “<i>Pula!</i>” to cheer!"),
    ],
    hello_pics=[("raincloud", {}), ("tn_fire", {}), ("star", {})],
    map=region_map(frame=[[11.0, -36.0], [35.0, -12.0]],
                   points=dict(gaborone=[25.91, -24.65], francistown=[27.51, -21.17], maun=[23.42, -19.98],
                               mahikeng=[25.64, -25.86], kimberley=[24.76, -28.73]),
                   area=(24.6, -23.6, 230, 270), area_rot=10,
                   cities=[("gaborone", "Gaborone", 14, 4, "start", False), ("francistown", "Francistown", 14, 8, "start", False),
                           ("maun", "Maun", -14, 8, "end", False), ("mahikeng", "Mahikeng", -14, 18, "end", False),
                           ("kimberley", "Kimberley", 14, 8, "start", False)],
                   label="SOUTHERN AFRICA", label_at=[23.0, -14.5], marker=[24.5, -24.0],
                   caption="The circle shows southern Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the oceans <b>blue</b>. <b>Find it:</b> Setswana is spoken in Gaborone, "
                          "Francistown, Maun, Mahikeng and Kimberley. The dashed line shows where most Setswana speakers live.",
                   seas=[("Atlantic Ocean", 13.6, -31.0), ("Indian Ocean", 33.0, -32.5)], world_r=16),
    digits=[("0", "lefela", "leh-FEH-lah", "zero"), ("1", "nngwe", "N-ngweh", "one"), ("2", "pedi", "PEH-dee", "two"),
            ("3", "tharo", "T’HAH-roh", "three"), ("4", "nne", "N-neh", "four"), ("5", "tlhano", "TLHAH-noh", "five"),
            ("6", "thataro", "t’hah-T’HAH-roh", "six"), ("7", "supa", "SOO-pah", "seven"), ("8", "robedi", "roh-BEH-dee", "eight"),
            ("9", "robongwe", "roh-BOH-ngweh", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Dumela!", "doo-MEH-lah", "Hello! (to one person)"),
             ("Leina la me ke …", "LAY-nah lah meh keh …", "My name is …"),
             ("Ke a leboga", "keh ah leh-BOH-khah", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAL-lah-hoo KHAI-ran", "May Allah reward you with good"),
             ("mme · rre", "M-meh · R-reh", "Mother · Father"),
             ("morwarre · kgaitsadi", "moh-RWAH-rreh · kkhah-ee-TSAH-dee", "Brother · Sister"),
             ("ee · nnyaa", "eh-eh · N-nyah", "Yes · No"),
             ("Ke ithuta Setswana!", "keh ee-T’HOO-tah seh-TSWAH-nah", "I am learning Setswana!")],
    cheer=("Mashallah! O dirile sentle!", "MAH-shah-lah! oh dee-REE-leh SEN-tleh!", "Mashallah! You did well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B D", right="E F G"),
    review_note="Check the borrowed words <i>fensetere</i> (window), <i>galase</i> (glass), <i>hempe</i> (shirt) and <i>raese</i> (rice); "
                "<i>seyalemoya</i> for radio (or <i>seyalemowa</i>); whether letters are named «ba, da…» in school; the words for brother/sister "
                "(<i>morwarre · kgaitsadi</i> depend on who is speaking); the title and “Buka e ke ya”; and the stress marks.",
    tiles="ABDKMT", cover_pics=["raincloud", "sun", "tn_fire", "star"],
    speakers_blurb="Setswana is spoken by more than 10 million people in Botswana and South Africa.",
    sample_words=[("letsatsi", "leh-TSAH-tsee", "sun"), ("pula", "POO-lah", "rain"), ("naledi", "nah-LEH-dee", "star")],
    keywords=["setswana alphabet book for kids", "learn setswana for children", "tswana coloring book",
              "setswana letters tracing workbook", "botswana kids activity book", "muslim kids activity book",
              "islamic coloring book for children"],
))
