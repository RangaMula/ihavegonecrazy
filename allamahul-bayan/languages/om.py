# -*- coding: utf-8 -*-
"""Book 67 - Oromo / Afaan Oromoo (Latin script "Qubee", 26 single letters + 5 double letters).
Allamahul Bayan Series. REVIEW DRAFT. Big letter = capital + small ("Bb"); double letters drawn "Dh dh"."""
from generic import build, section
from maps import region_map
from _so_om_zu_xh import FONTS, GLYPH_FONTS, CSS, maker

L = maker("Oromo letter name · Qubee")
POP = "A <b>popped</b> sound: close your throat, then let the sound burst out."
LOAN = "found only in words borrowed from other languages"

SINGLE = [
    L("A", "a", "ah", "‘a’ as in “father”", "aannan", "aan-nan", "milk", "zgh_milk", vowel=True,
      row="a · aa — ba · baa", rule="Write it twice for a long sound: <b>aa</b>."),
    L("B", "ba", "bah", "‘b’ as in “ball”", "bishaan", "bi-shaan", "water", "water"),
    L("C", "ca", "ch'ah", "a popped ‘ch’ (ch’)", "callee", "ch'al-leh", "beads", "hy_beads", rule=POP),
    L("D", "da", "dah", "‘d’ as in “dog”", "daabboo", "daab-boh", "bread", "am_bread"),
    L("E", "e", "eh", "‘e’ as in “bed”", "ejersa", "eh-jer-sa", "wild olive tree", "olive", vowel=True,
      row="e · ee — be · bee", rule="Write it twice for a long sound: <b>ee</b>."),
    L("F", "fa", "fah", "‘f’ as in “fan”", "firii", "fi-ree", "fruit", "om_firii"),
    L("G", "ga", "gah", "‘g’ as in “go”", "gaara", "gaa-ra", "mountain", "mountain"),
    L("H", "ha", "hah", "‘h’ as in “hat”", "haxaa'oo", "ha-t'aa-'oh", "broom", "broom",
      rule="The mark ’ (<i>hudhaa</i>) is a tiny catch in the voice."),
    L("I", "i", "ee", "‘i’ as in “sit”; long <b>ii</b> as in “see”", "ibsaa", "ib-saa", "lamp · light", "hy_lamp", vowel=True,
      row="i · ii — bi · bii", rule="Write it twice for a long sound: <b>ii</b>."),
    L("J", "ja", "jah", "‘j’ as in “jam”", "ji'a", "ji-'a", "moon · month", "moon"),
    L("K", "ka", "kah", "‘k’ as in “kite”", "kitaaba", "ki-taa-ba", "book", "book", args=dict(left="A B C", right="D E F")),
    L("L", "la", "lah", "‘l’ as in “lamp”", "loomii", "loh-mee", "lemon", "lemon"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "mana", "ma-na", "house · home", "house"),
    L("N", "na", "nah", "‘n’ as in “net”", "nuugii", "noo-gee", "niger-seed plant (noug)", "om_nuugii"),
    L("O", "o", "oh", "‘o’ as in “for” (short and pure)", "okkotee", "ok-ko-teh", "cooking pot", "pot", vowel=True,
      row="o · oo — bo · boo", rule="Write it twice for a long sound: <b>oo</b>."),
    L("P", "pa", "pah", "‘p’ as in “pen” — " + LOAN, "paappayyaa", "paap-pay-yaa", "papaya", "am_papaya"),
    L("Q", "qa", "k'ah", "a popped ‘k’ (k’)", "qamadii", "k'a-ma-dee", "wheat", "hy_wheat", rule=POP),
    L("R", "ra", "rah", "a rolled ‘r’", "rooba", "roh-ba", "rain", "raincloud"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "soogidda", "soh-gid-da", "salt", "salt", args=dict(label="soogidda")),
    L("T", "ta", "tah", "‘t’ as in “tap”", "teessoo", "tehs-soh", "seat · stool", "stool"),
    L("U", "u", "oo", "‘u’ as in “put”; long <b>uu</b> as in “moon”", "urjii", "ur-jee", "star", "star", vowel=True,
      row="u · uu — bu · buu", rule="Write it twice for a long sound: <b>uu</b>."),
    L("V", "va", "vah", "‘v’ as in “van” — " + LOAN, "tele[v]iziyoona", "te-le-vi-zi-yoh-na", "television", "am_tv",
      note="V is rare. Find it inside <i>televiziyoona</i>!"),
    L("W", "wa", "wah", "‘w’ as in “water”", "waraqaa", "wa-ra-k'aa", "paper", "th_paper"),
    L("X", "xa", "t'ah", "a popped ‘t’ (t’)", "xaafii", "t'aa-fee", "teff (a tiny grain)", "om_xaafii",
      rule="X is <b>not</b> ‘ks’ in Afaan Oromoo! " + POP),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "yeroo", "ye-roh", "time", "clock"),
    L("Z", "za", "zah", "‘z’ as in “zoo” — " + LOAN, "zayitii", "za-yi-tee", "cooking oil", "th_bottle"),
]

DOUBLE = [
    L("CH", "cha", "chah", "‘ch’ as in “chair” (not popped) — mostly in borrowed words", "chokolaatii", "cho-ko-laa-tee", "chocolate", "am_chocolate"),
    L("DH", "dha", "dhah", "a ‘d’ swallowed inwards — the tongue touches the roof of the mouth", "dhagaa", "dha-gaa", "stone", "hy_stones",
      rule="DH is one Oromo sound, not ‘d’ + ‘h’."),
    L("NY", "nya", "nyah", "‘ny’ as in “canyon”", "nyaata", "nyaa-ta", "food", "rice"),
    L("PH", "pha", "p'ah", "a popped ‘p’ (p’)", "bu[ph]aa", "boo-p'aa", "egg", "egg", rule=POP,
      note="PH hardly ever starts a word. Find it in the middle of <i>buphaa</i>!"),
    L("SH", "sha", "shah", "‘sh’ as in “ship”", "shaayii", "shaa-yee", "tea", "teacup"),
]

LANG = build(dict(
    code="om", folder="book-67-oromo", series_no=67, isbn="", draft=True,
    name="Oromo", native="Afaan Oromoo", native_tr="a-faan o-roh-moh", name_word="maqaa", write_word="barreessi",
    title_native="Qubee Afaan Oromoo", title_letters="AaBbCc", belongs_native="Kitaabni kun kan",
    belongs_pic="star", alphabet_native="Qubee", numbers_native="lakkoofsota", numbers_tr="lak-kohf-so-ta",
    phrases_native="Jechoota jalqabaa",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit="Baloo 2",
    extra_css=CSS,
    phon_feature="each letter’s Oromo name and its syllables (ba: ba be bi bo bu)",
    sections=[
        section(SINGLE, label="LETTER", chip="QUBEE", title="The Letters",
                native="Qubee", native_tr="koo-beh — the Oromo alphabet",
                chart_title="single letters", chart_cols=7, warmup_title="the single letters", warmup_cols=6,
                intro_html="""<p>Afaan Oromoo is written in <b>Qubee</b> (say <i>koo-beh</i>): the <b>26 letters</b> you know from English, plus
<b>5 double letters</b> that come at the end of this book.</p>
<div class="box" style="margin:0.1in 0"><h3>Popping sounds</h3><b>C</b>, <b>Q</b>, <b>X</b> and <b>PH</b> are <b>ejectives</b>: close your throat,
then let the sound pop out. In Oromo, <b>C</b> is a popped ‘ch’, <b>Q</b> a popped ‘k’ and <b>X</b> a popped ‘t’ — never ‘ks’!</div>
<div class="box" style="margin:0.1in 0"><h3>Write it twice</h3>A doubled vowel is long (<i>a, aa</i>) and a doubled consonant is held longer
(<i>t, tt</i>). Doubling can change the meaning, so listen carefully!</div>
<div class="box"><h3>The little catch: hudhaa</h3>The mark <b>’</b> is called <i>hudhaa</i>. It is a tiny stop in the voice, as in
<i>ji’a</i> (moon).</div>"""),
        section(DOUBLE, label="DOUBLE LETTER", chip="QUBEE DACHAA", title="The Double Letters",
                native="Qubee dachaa", native_tr="koo-beh da-chaa — “double letters”",
                chart_title="double letters", chart_cols=5, warmup_title="the double letters", warmup_cols=5,
                intro_html="""<p>Five sounds are written with <b>two letters</b>: <b>CH DH NY PH SH</b>. Each pair is <b>one sound</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Soft and popped</h3><b>CH</b> is a soft ‘ch’ as in “chair”, but <b>C</b> alone is popped.
<b>PH</b> is a popped ‘p’ — not ‘f’!</div>
<div class="box"><h3>A few rare ones</h3>Some books also teach <b>TS</b> (a popped ‘ts’) and <b>ZY</b> (the ‘s’ in “measure”).
They are rare, so they are not on their own pages here.</div>"""),
    ],
    sound_notes=[
        "<b>ch’ k’ t’ p’</b> with an apostrophe are <b>popped</b> sounds (ejectives): close your throat, then let the sound burst out.",
        "<b>'</b> between vowels is the <i>hudhaa</i>: a tiny catch in the voice, like the middle of “uh-oh”.",
        "<b>dh</b> is a ‘d’ swallowed inwards; <b>r</b> is rolled.",
        "In Oromo spelling a doubled vowel is long (<b>aa ee ii oo uu</b>). In the pronunciation, <b>aa</b> is a long ‘a’ as in “father”, "
        "<b>ee</b> says ‘ee’ as in “see”, <b>oo</b> says ‘oo’ as in “moon”, <b>oh</b> says ‘o’ as in “go” and <b>eh</b> says ‘e’ as in “bed”.",
        "Oromo uses pitch rather than strong stress, so no syllable is written in capitals here."],
    phon_explain="The box marked <i>Oromo letter name · Qubee</i> shows the name Oromo children use for the letter "
                 "(B is «ba», C is «ca»…) and its row of syllables, the way Oromo children learn to read.",
    standard="Standard written Oromo (Qubee)",
    hello=[
        ("Who speaks it?", "About <b>37 million people</b> speak Afaan Oromoo — one of the most spoken languages of Africa.<sup>³</sup>"),
        ("Where?", "Mostly in <b>Ethiopia</b>, in the highlands and lowlands around Addis Ababa, Adama, Jimma and Harar, and also in northern <b>Kenya</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, called <b>Qubee</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>26 single letters</b> and <b>5 double letters</b> (CH DH NY PH SH): <b>31</b> in this book."),
        ("Popping sounds!", "<b>C, Q, X</b> and <b>PH</b> are popped sounds. Try <i>qamadii</i> (wheat) and <i>xaafii</i> (teff)!"),
        ("Did you know?", "Ethiopia is the home of <b>coffee</b>. In Afaan Oromoo coffee is <i>buna</i>, and families share it with friends "
                          "and neighbours."),
    ],
    hello_pics=[("om_xaafii", {}), ("teacup", {}), ("mountain", {})],
    map=region_map(frame=[[31.0, -1.0], [49.0, 17.0]],
                   points=dict(addis=[38.74, 9.03], adama=[39.27, 8.54], jimma=[36.83, 7.67], harar=[42.12, 9.31],
                               nekemte=[36.55, 9.08], moyale=[39.06, 3.52]),
                   area=(39.3, 7.6, 270, 220),
                   cities=[("addis", "Addis Ababa", 10, -10, "start", False), ("adama", "Adama", 14, 10, "start", False),
                           ("jimma", "Jimma", -14, 8, "end", False), ("harar", "Harar", 14, 8, "start", False),
                           ("nekemte", "Nekemte", -12, 20, "end", False), ("moyale", "Moyale", 14, 8, "start", False)],
                   label="ETHIOPIA", label_at=[41.0, 12.8], marker=[39.0, 8.0],
                   caption="The circle shows the Horn of Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> the dashed line shows where most "
                          "Oromo speakers live, around Addis Ababa, Adama, Jimma, Nekemte and Harar, down to Moyale in the south.",
                   seas=[("Red Sea", 39.6, 16.2), ("Gulf of Aden", 46.5, 12.4), ("Indian Ocean", 46.5, 1.0)], world_r=13),
    digits=[("0", "duwwaa", "duw-waa", "zero"), ("1", "tokko", "tok-ko", "one"), ("2", "lama", "la-ma", "two"), ("3", "sadii", "sa-dee", "three"),
            ("4", "afur", "a-foor", "four"), ("5", "shan", "shan", "five"), ("6", "jaha", "ja-ha", "six"), ("7", "torba", "tor-ba", "seven"),
            ("8", "saddeet", "sad-deht", "eight"), ("9", "sagal", "sa-gal", "nine")],
    phrases=[("Assalaamu alaykum", "as-sa-laa-moo a-lay-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaykum assalaam", "wa a-lay-koom as-sa-laam", "And upon you be peace (the reply)"),
             ("Akkam?", "ak-kam", "Hello, how are you?"),
             ("Maqaan koo … dha", "ma-k'aan koh … dha", "My name is …"),
             ("Galatoomi", "ga-la-toh-mee", "Thank you"),
             ("Jazaakallaahu khayran", "ja-zaa-kal-laa-hoo khay-ran", "May Allah reward you with good"),
             ("haadha · abbaa", "haa-dha · ab-baa", "Mother · Father"),
             ("obboleessa · obboleettii", "ob-bo-lehs-sa · ob-bo-leht-tee", "Brother · Sister"),
             ("eeyyee · lakki", "ehy-yeh · lak-ki", "Yes · No"),
             ("Ani Afaan Oromoo barachaa jira!", "a-ni a-faan o-roh-moh ba-ra-chaa ji-ra", "I am learning Oromo!")],
    cheer=("Maashaa Allaah! Baay'ee gaarii!", "maa-shaa al-laah! baay-'eh gaa-ree", "Mashallah! Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Machine-drafted: a native Oromo speaker must check every word and spelling (long vowels, double consonants, hudhaa), "
                "the loan words for P V Z CH, the phrases and the cheer.",
    tiles="QUBEXC", cover_pics=["om_xaafii", "teacup", "mountain", "star"], title_size=48,
    speakers_blurb="Afaan Oromoo is spoken by about 37 million people in Ethiopia and Kenya.",
    sample_words=[("urjii", "ur-jee", "star"), ("bishaan", "bi-shaan", "water"), ("qamadii", "k'a-ma-dee", "wheat")],
    keywords=["oromo alphabet book for kids", "learn afaan oromoo for children", "qubee coloring book",
              "oromo letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual oromo english toddlers"],
))
