# -*- coding: utf-8 -*-
"""Book 87 - Haitian Creole (Kreyòl ayisyen, Latin script: 24 single letters + 4 nasal vowels + 4 letter pairs = 32).
Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
import _afrolatin as AF

L = AF.maker("Kreyòl name · syllables", ["a", "e", "i", "o", "ou"], vowel_examples="b d k l m")

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "avyon", "ah-VYON", "aeroplane", "plane", vowel=True),
    L("B", "b", "be", "beh", "‘b’ as in “ball”", "bannann", "bah-NAHN", "plantain (a big cooking banana)", "banana"),
    L("D", "d", "de", "deh", "‘d’ as in “door”", "dlo", "dloh", "water", "water"),
    L("E", "e", "e", "ay", "‘ay’ as in “day” (short and pure)", "eskalye", "es-kah-LYAY", "stairs, staircase", "ht_stairs", vowel=True),
    L("È", "è", "è", "eh", "‘e’ as in “bed” — an open E", "sèl", "sel", "salt", "salt", vowel=True,
      note="È hardly ever starts a word. Find it in the middle of <i>sèl</i>!",
      rule="e = “d<b>ay</b>” · è = “b<b>e</b>d”"),
    L("F", "f", "fe", "feh", "‘f’ as in “fan”", "flè", "fleh", "flower", "flower"),
    L("G", "g", "ge", "geh", "‘g’ as in “go” (always hard)", "gato", "gah-TOH", "cake", "ht_cake"),
    L("H", "h", "he", "heh", "‘h’ as in “hat” — a rare letter in Kreyòl", "hamak", "hah-MAHK", "hammock", "ht_hammock"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "diri", "dee-REE", "rice", "rice", vowel=True,
      note="Find I twice in <i>diri</i> — rice, the food of every Haitian table!"),
    L("J", "j", "je", "zheh", "‘zh’ like the ‘s’ in “measure” — never ‘j’ as in “jam”", "joumou", "zhoo-MOO", "pumpkin, squash", "ht_pumpkin"),
    L("K", "k", "ke", "keh", "‘k’ as in “kite”", "kokoye", "koh-koh-YAY", "coconut", "coconut"),
    L("L", "l", "le", "leh", "‘l’ as in “lamp”", "lalin", "lah-LEEN", "moon", "moon"),
    L("M", "m", "me", "meh", "‘m’ as in “moon”", "mango", "mahn-GOH", "mango", "mango"),
    L("N", "n", "ne", "neh", "‘n’ as in “net”", "nechèl", "neh-SHEL", "ladder", "ladder"),
    L("O", "o", "o", "oh", "‘o’ as in “go” (short and pure)", "bato", "bah-TOH", "boat", "boat", vowel=True,
      note="Few Kreyòl words start with O. Find it at the end of <i>bato</i>!", rule="o = “g<b>o</b>” · ò = “m<b>o</b>re”"),
    L("Ò", "ò", "ò", "aw", "‘o’ as in “more” — an open O", "pòt", "pawt", "door", "door", vowel=True,
      note="Ò hardly ever starts a word. Find it in the middle of <i>pòt</i>!"),
    L("P", "p", "pe", "peh", "‘p’ as in “pen”", "parapli", "pah-rah-PLEE", "umbrella", "umbrella"),
    L("R", "r", "re", "reh", "a soft ‘r’ from the throat, almost like ‘w’ before o and ou", "rezen", "ray-ZEN", "grapes", "grapes"),
    L("S", "s", "se", "seh", "‘s’ as in “sun” — always a hiss, never ‘z’", "solèy", "soh-LEY", "sun", "sun"),
    L("T", "t", "te", "teh", "‘t’ as in “tap”", "tomat", "toh-MAHT", "tomato", "tomato"),
    L("V", "v", "ve", "veh", "‘v’ as in “van”", "vè", "veh", "drinking glass", "ht_glass"),
    L("W", "w", "we", "weh", "‘w’ as in “water”", "wòch", "wawsh", "rock, stone", "ht_rock"),
    L("Y", "y", "ye", "yeh", "‘y’ as in “yes”", "yanm", "yahn", "yam", "ht_yam"),
    L("Z", "z", "ze", "zeh", "‘z’ as in “zoo”", "zetwal", "zay-TWAHL", "star", "star"),
]

NASAL = [
    L("An", "an", "an", "ahn", "‘ah’ said through the nose (like French “an”)", "zanmann", "zahn-MAHN", "almonds", "almond",
      vowel=True, note="Find AN twice in <i>zanmann</i>!"),
    L("En", "en", "en", "ehn", "‘eh’ said through the nose", "pen", "pehn", "bread", "ht_bread", vowel=True),
    L("On", "on", "on", "ohn", "‘oh’ said through the nose", "bonbon", "bohn-BOHN", "cookies", "ht_cookies", vowel=True),
    L("Oun", "oun", "oun", "oohn", "‘oo’ said through the nose", "youn", "yoohn", "one", "one", args=dict(digit="1"),
      vowel=True, note="<i>Youn</i> means “one”. Find OUN at the end!"),
]

PAIRS = [
    L("Ch", "ch", "che", "sheh", "‘sh’ as in “ship” — never ‘ch’ as in “church”", "chodyè", "shoh-DYEH", "cooking pot", "pot"),
    L("Ng", "ng", "ng", "ng", "‘ng’ as in “sing” — found at the end of words", "bilding", "beel-DEENG", "building", "building",
      note="NG never starts a word. Find it at the end of <i>bilding</i>!"),
    L("Ou", "ou", "ou", "oo", "‘oo’ as in “moon”", "zouti", "zoo-TEE", "tools", "tools", vowel=True,
      note="OU is <b>one</b> vowel sound. Find it in <i>zouti</i>!"),
    L("Ui", "ui", "ui", "wee", "‘wee’ as in “week”", "uit", "weet", "eight", "one", args=dict(digit="8"), vowel=True,
      note="<i>Uit</i> means “eight”: count to eight in Kreyòl!"),
]

LANG = build(dict(
    code="ht", folder="book-87-haitian-creole", series_no=87, isbn="", draft=True,
    name="Haitian Creole", native="kreyòl ayisyen", native_tr="kray-OL ah-yee-SYEN", name_word="non", write_word="ekri",
    title_native="Premye abese mwen an kreyòl", title_letters="AaÈèÒò", belongs_native="Liv sa a se pou",
    belongs_pic="star", alphabet_native="alfabè a", numbers_native="chif yo", numbers_tr="sheef yoh",
    phrases_native="Premye mo yo", letters_word="Letters and Sounds",
    fonts=AF.afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=AF.GLYPH_FONTS, font_credit=AF.FONT_CREDIT, extra_css=getattr(AF, "EXTRA_CSS", ""),
    phon_feature="each letter’s Kreyòl name and its syllables (ba, be, bi, bo, bou)",
    sections=[
        section(LETTERS, native="lèt yo", native_tr="let yoh — “the letters”", chart_cols=8, warmup_cols=6,
                intro_html="""<p>Kreyòl is written with <b>24 single letters</b>, plus <b>4 nasal vowels</b> and <b>4 letter pairs</b>: <b>32</b> in all.</p>
<div class="box" style="margin:0.1in 0"><h3>One sound, one spelling</h3>Kreyòl is written just as it sounds — no silent letters!
It has no C, Q, U or X on their own: <b>s</b> and <b>k</b> do their work.</div>
<div class="box" style="margin:0.1in 0"><h3>Watch the little marks</h3><b>è</b> and <b>ò</b> have a mark called an <i>aksan</i>. It changes the sound:
<i>e</i> is “day”, <i>è</i> is “bed”; <i>o</i> is “go”, <i>ò</i> is “more”.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(NASAL, label="NASAL", chip="NASAL VOWELS", title="Nasal Vowels", native="vwayèl nazal",
                native_tr="vwah-YEL nah-ZAHL — “nose vowels”", chart_title="nasal vowels", chart_cols=4,
                warmup_title="the nasal vowels", warmup_cols=4,
                intro_html="""<p>Some Kreyòl vowels are said <b>through the nose</b>. They are written with an <b>n</b> after the vowel:
<b>an · en · on · oun</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Hum it!</h3>Pinch your nose gently and say <i>an</i>: you will feel it buzz. The <b>n</b> is not said
on its own — it tells you to send the vowel through your nose.</div>
<div class="box"><h3>A tricky pair</h3>When <b>n</b> must be said on its own after a nasal vowel, Kreyòl writes it twice: <i>bannann</i>, <i>zanmann</i>.</div>"""),
        section(PAIRS, label="PAIR", chip="LETTER PAIRS", title="Letter Pairs", native="de lèt ansanm",
                native_tr="deh let ahn-SAHN — “two letters together”", chart_title="letter pairs", chart_cols=4,
                warmup_title="the letter pairs", warmup_cols=4,
                intro_html="""<p>Four Kreyòl sounds are written with <b>two letters together</b>: <b>ch · ng · ou · ui</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Two letters, one sound</h3><b>ch</b> says “sh”, <b>ou</b> says “oo”, <b>ui</b> says “wee” and
<b>ng</b> is the ‘ng’ at the end of “sing”.</div>
<div class="box"><h3>Count them!</h3>24 letters + 4 nasal vowels + 4 letter pairs = the <b>32 letters and sounds</b> of the Kreyòl alphabet.</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>koh-koh-YAY</i>. In Kreyòl the last syllable is usually a little stronger.",
        "<b>ahn, ehn, ohn, oohn</b> (with <b>n</b> after the vowel) mean “say the vowel through your nose”.",
        "<b>zh</b> is the sound of Kreyòl <b>j</b>, like the ‘s’ in “measure”; <b>sh</b> is Kreyòl <b>ch</b>.",
        "<b>ay</b> is a short, pure ‘e’ (Kreyòl e); <b>aw</b> is the open ‘o’ of “more” (Kreyòl ò)."],
    phon_explain="The box marked <i>Kreyòl name · syllables</i> shows the name children say for the letter "
                 "(B is «be») and its row of syllables: <i>ba, be, bi, bo, bou</i>. For vowels it shows them with consonants: <i>ba, da, ka…</i>",
    standard="Standard Haitian Creole spelling (the official alphabet in use since about 1980)",
    chart_note="Read the letters row by row — the single letters first, then the nasal vowels and the letter pairs.",
    hello=[
        ("Who speaks it?", "About <b>12 million people</b> speak Haitian Creole. Almost everyone in Haiti speaks it from childhood.<sup>³</sup>"),
        ("Where?", "In <b>Haiti</b>, on the island it shares with the Dominican Republic in the <b>Caribbean Sea</b>, and in Haitian families in "
                   "the United States, Canada, France and other countries."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with marks on <b>è</b> and <b>ò</b>."),
        ("How many letters?", "<b>32 letters and sounds</b>: 24 single letters, 4 nasal vowels (<i>an en on oun</i>) and 4 letter pairs "
                              "(<i>ch ng ou ui</i>)."),
        ("Land of mountains", "The name <b>Ayiti</b> comes from the island’s first people, the Taíno: it means “land of high mountains”. "
                              "A Kreyòl proverb says <i>Dèyè mòn, gen mòn</i> — “Behind the mountains, more mountains!”"),
        ("Did you know?", "Most Kreyòl words come from <b>French</b>, with words from West African languages, Taíno, Spanish and English. "
                          "Kreyòl and French are both official languages of Haiti."),
    ],
    hello_pics=[("mountain", {}), ("mango", {}), ("mosque", {})],
    map=region_map(frame=[[-75.6, 16.0], [-68.0, 23.6]],
                   points=dict(pap=[-72.34, 18.54], cap=[-72.20, 19.76], cayes=[-73.75, 18.19], gonaives=[-72.69, 19.45],
                               jacmel=[-72.53, 18.23]),
                   area=(-72.8, 18.9, 190, 150), area_rot=-8,
                   cities=[("pap", "Port-au-Prince", 12, 4, "start", False), ("cap", "Cap-Haïtien", 12, -6, "start", False),
                           ("cayes", "Les Cayes", -12, 16, "end", False), ("gonaives", "Gonaïves", -12, 4, "end", False),
                           ("jacmel", "Jacmel", 12, 18, "start", False)],
                   label="HAITI", label_at=[-72.6, 20.55], marker=[-72.5, 19.0],
                   caption="The circle shows Haiti in the Caribbean on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Kreyòl is spoken in Port-au-Prince, "
                          "Cap-Haïtien, Gonaïves, Jacmel and Les Cayes. The dashed line shows Haiti, on the western part of the island.",
                   seas=[("Caribbean Sea", -71.3, 16.9), ("Atlantic Ocean", -70.3, 22.2)], world_r=12),
    digits=[("0", "zewo", "zay-WOH", "zero"), ("1", "en", "ehn", "one"), ("2", "de", "day", "two"), ("3", "twa", "twah", "three"),
            ("4", "kat", "kaht", "four"), ("5", "senk", "senk", "five"), ("6", "sis", "sees", "six"), ("7", "sèt", "set", "seven"),
            ("8", "uit", "weet", "eight"), ("9", "nèf", "nef", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Bonjou!", "bohn-ZHOO", "Hello! Good morning!"),
             ("Kijan ou ye? · Mwen byen!", "kee-ZHAHN oo YAY · mwehn BYEHN", "How are you? · I am fine!"),
             ("Mwen rele …", "mwehn reh-LAY …", "My name is …"),
             ("Mèsi", "meh-SEE", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAL-lah-hoo KHAI-ran", "May Allah reward you with good"),
             ("manman · papa", "mahn-MAHN · pah-PAH", "Mother · Father"),
             ("frè · sè", "freh · seh", "Brother · Sister"),
             ("wi · non", "wee · nohn", "Yes · No"),
             ("M ap aprann kreyòl!", "m ahp ah-PRAHN kray-OL", "I am learning Kreyòl!")],
    cheer=("Mashallah! Bravo, ou fè l byen!", "MAH-shah-lah! brah-VOH, oo FEHL byehn!", "Mashallah! Bravo, you did it well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A AN B", right="CH D E"),
    review_note="Check: <i>hamak</i> for H (H is rare; a better H word is welcome); <i>eskalye</i> (stairs) for E; <i>bilding</i> for NG; "
                "<i>uit</i> for UI (or <i>kuiyè</i>, spoon); letter names «be, de, fe…»; <i>bannann</i>, <i>zanmann</i>, <i>yanm</i> spellings; "
                "the sound guide for R; the title <i>Premye abese mwen an kreyòl</i>; and the cheer <i>Bravo, ou fè l byen</i>.",
    tiles="AÈKMÒZ", cover_pics=["mango", "coconut", "boat", "sun"],
    speakers_blurb="Haitian Creole (Kreyòl) is spoken by about 12 million people in Haiti and around the world.",
    sample_words=[("solèy", "soh-LEY", "sun"), ("kokoye", "koh-koh-YAY", "coconut"), ("zetwal", "zay-TWAHL", "star")],
    keywords=["haitian creole alphabet book for kids", "learn kreyol for children", "kreyol ayisyen coloring book",
              "haitian creole letters tracing workbook", "haiti kids activity book", "muslim kids activity book",
              "islamic coloring book for children"],
))
