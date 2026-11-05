# -*- coding: utf-8 -*-
"""Book 65 - Igbo (Latin script, Ọnwụ alphabet: 36 letters incl. 9 two-letter letters and Ị Ọ Ụ Ṅ). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
from _afrolatin import afro_fonts, GLYPH_FONTS, FONT_CREDIT, EXTRA_CSS, maker

L = maker("Igbo name · syllables", ["a", "e", "i", "ị", "o", "ọ", "u", "ụ"])
TWO = "<b>{}</b> is written with two letters but counts as <b>one</b> Igbo letter."

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "akwụkwọ", "ah-kwu-kwaw", "book", "book", vowel=True,
      args=dict(left="A B CH", right="D E F")),
    L("B", "b", "bị", "bih", "‘b’ as in “ball”", "bọọlụ", "baw-aw-lu", "ball", "ball"),
    L("Ch", "ch", "chị", "chih", "‘ch’ as in “church”", "nche anwụ", "n-cheh ahn-wu", "umbrella (“sun shield”)", "umbrella",
      note=TWO.format("Ch")),
    L("D", "d", "dị", "dih", "‘d’ as in “door”", "ụdara", "u-dah-rah", "African star apple (a sweet fruit)", "apple"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "enyo", "eh-nyoh", "mirror", "mirror", vowel=True),
    L("F", "f", "fụ", "fu", "‘f’ as in “fan”", "ifuru", "ee-foo-roo", "flower", "flower",
      note="Few Igbo words start with F. Find it inside <i>ifuru</i>!"),
    L("G", "g", "gị", "gih", "‘g’ as in “go” (always hard)", "ugegbe anya", "oo-geh-gbeh ah-nyah", "glasses (“eye mirror”)", "glasses"),
    L("Gb", "gb", "gbị", "gbih", "‘g’ and ‘b’ said <b>together</b>, at the same time", "ụgbọ mmiri", "u-gbaw m-mee-ree",
      "ship (“water vehicle”)", "ship", note=TWO.format("Gb")),
    L("Gh", "gh", "ghị", "ghih", "a soft gargled ‘g’ from the back of the throat, like Arabic غ", "ịgha mkpụrụ", "ih-ghah m-kpu-ru",
      "sowing seeds", "paddy", note=TWO.format("Gh")),
    L("Gw", "gw", "gwụ", "gwu", "‘gw’ as in “Gwen”, with round lips", "ọgwụ", "aw-gwu", "medicine", "medicine", note=TWO.format("Gw")),
    L("H", "h", "hị", "hih", "‘h’ as in “hat”", "ahịhịa", "ah-hih-hih-ah", "grass", "ig_grass"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "ite", "ee-teh", "cooking pot", "pot", vowel=True),
    L("Ị", "ị", "ị", "ih", "‘i’ as in “sit” — the dot makes it open", "ịchafụ", "ih-chah-fu", "headscarf", "scarf", vowel=True,
      rule="i = s<b>ee</b> · ị = s<b>i</b>t"),
    L("J", "j", "jị", "jih", "‘j’ as in “jam”", "ji", "jee", "yam", "ig_ji"),
    L("K", "k", "kị", "kih", "‘k’ as in “kite”", "akị oyibo", "ah-kih oh-yee-boh", "coconut", "coconut"),
    L("Kp", "kp", "kpị", "kpih", "‘k’ and ‘p’ said <b>together</b>, at the same time", "kpakpando", "kpah-kpahn-doh", "star", "star",
      note=TWO.format("Kp")),
    L("Kw", "kw", "kwụ", "kwu", "‘kw’ as in “quick”", "akwa", "ah-kwah", "egg", "egg", note=TWO.format("Kw")),
    L("L", "l", "lị", "lih", "‘l’ as in “lamp”", "ọla", "aw-lah", "ring, jewelry", "ring"),
    L("M", "m", "mụ", "mu", "‘m’ as in “moon”", "mmiri", "m-mee-ree", "water", "water",
      note="M can be a whole syllable on its own: <i>m-mi-ri</i>."),
    L("N", "n", "nụ", "nu", "‘n’ as in “net”", "nkata", "n-kah-tah", "basket", "basket"),
    L("Ṅ", "ṅ", "ṅụ", "ngu", "‘ng’ as in “sing”", "mmanụ aṅụ", "m-mah-nu ah-ngu", "honey (“bee oil”)", "honey",
      rule="n = <b>n</b>et · ṅ = si<b>ng</b>"),
    L("Nw", "nw", "nwụ", "nwu", "‘n’ and ‘w’ together, with round lips", "ọnwa", "aw-nwah", "moon, month", "moon", note=TWO.format("Nw")),
    L("Ny", "ny", "nyị", "nyih", "‘ny’ as in “canyon”", "anyanwụ", "ah-nyahn-wu", "sun", "sun", note=TWO.format("Ny")),
    L("O", "o", "o", "oh", "‘o’ as in “go”, short and pure", "oche", "oh-cheh", "chair, seat", "stool", vowel=True),
    L("Ọ", "ọ", "ọ", "aw", "‘aw’ as in “saw” — the dot makes it open", "ọkụ", "aw-ku", "fire, light", "bulb", vowel=True,
      rule="o = g<b>o</b> · ọ = s<b>aw</b>"),
    L("P", "p", "pị", "pih", "‘p’ as in “pen”", "pensụl", "pen-sul", "pencil", "pen",
      note="P mostly starts words that came from other languages, like <i>pensụl</i>."),
    L("R", "r", "rị", "rih", "a quick tapped ‘r’", "oroma", "oh-roh-mah", "orange", "ig_orange"),
    L("S", "s", "sị", "sih", "‘s’ as in “sun”", "osisi", "oh-see-see", "tree", "tree"),
    L("Sh", "sh", "shị", "shih", "‘sh’ as in “ship”", "ọshịmịrị", "aw-shih-mih-rih", "sea, ocean", "waves", note=TWO.format("Sh")),
    L("T", "t", "tị", "tih", "‘t’ as in “tap”", "tomato", "toh-mah-toh", "tomato", "tomato"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "ube", "oo-beh", "African pear (a soft purple fruit)", "pear", vowel=True),
    L("Ụ", "ụ", "ụ", "u", "‘u’ as in “put” — the dot makes it open", "ụlọ", "u-law", "house", "house", vowel=True,
      rule="u = m<b>oo</b>n · ụ = p<b>u</b>t"),
    L("V", "v", "vị", "vih", "‘v’ as in “van”", "ivu", "ee-voo", "a load to carry", "box",
      note="V is a rare letter in Igbo. Find it inside <i>ivu</i>!"),
    L("W", "w", "wụ", "wu", "‘w’ as in “water”", "ọwụwa anyanwụ", "aw-wu-wah ah-nyahn-wu", "sunrise", "sunrise"),
    L("Y", "y", "yị", "yih", "‘y’ as in “yes”", "yabasị", "yah-bah-sih", "onion", "onion"),
    L("Z", "z", "zị", "zih", "‘z’ as in “zoo”", "mmiri ozuzo", "m-mee-ree oh-zoo-zoh", "rain (“falling water”)", "raincloud"),
]

LANG = build(dict(
    code="ig", folder="book-65-igbo", series_no=65, isbn="", draft=True,
    name="Igbo", native="Igbo", native_tr="ee-gboh", name_word="aha", write_word="dee ya",
    title_native="Abịdịị Igbo mbụ m", title_letters="AaỊịỤụ", belongs_native="Akwụkwọ a bụ nke",
    belongs_pic="ig_orange", alphabet_native="Abịdịị", numbers_native="ọnụọgụgụ", numbers_tr="aw-nu-aw-gu-gu",
    phrases_native="Okwu mbụ",
    fonts=afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT, extra_css=EXTRA_CSS,
    phon_feature="each letter’s Igbo name and its syllables (ba, be, bi, bị, bo, bọ, bu, bụ)",
    sections=[section(LETTERS, native="Abịdịị Igbo", native_tr="ah-bih-dih-ih ee-gboh — “the Igbo A-B-D”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>The Igbo alphabet, the <b>Abịdịị</b>, has <b>36 letters</b>. Nine of them are written with two letters:
<b>ch gb gh gw kp kw nw ny sh</b>. There is no C, Q or X.</p>
<div class="box" style="margin:0.1in 0"><h3>Eight vowels in two teams</h3><b>a ị ọ ụ</b> and <b>e i o u</b>. A dot under a vowel makes it
more open: <b>i</b> “see”, <b>ị</b> “sit”; <b>o</b> “go”, <b>ọ</b> “saw”; <b>u</b> “moon”, <b>ụ</b> “put”. Most words use vowels from one team:
<i>ụlọ</i>, <i>ite</i>.</div>
<div class="box" style="margin:0.1in 0"><h3>Ṅ with a dot on top</h3><b>ṅ</b> says “ng” as in “sing”. Look for it in <i>aṅụ</i> (bee).</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ụụ</b>. Color both!</div>""")],
    sound_notes=[
        "Igbo is a <b>tone</b> language, but everyday Igbo spelling does not mark tones, so the sound guides here have no capitals. "
        "Say every syllable evenly and listen to an Igbo speaker for the tune.",
        "<b>ee</b> = i (“see”), <b>ih</b> = ị (“sit”), <b>oh</b> = o (“go”), <b>aw</b> = ọ (“saw”), <b>oo</b> = u (“moon”) and "
        "<b>u</b> = ụ (“put”).",
        "<b>kp</b> and <b>gb</b> are said with the back of the tongue and the lips at the same time.",
        "<b>m-</b> and <b>n-</b> before a consonant are a short hum on their own: <i>m-mee-ree</i>, <i>n-kah-tah</i>."],
    phon_explain="The box marked <i>Igbo name · syllables</i> shows the name Igbo children chant for the letter in the Abịdịị song "
                 "(B is «bị», M is «mụ») and its syllable row with all eight vowels.",
    standard="Standard Igbo (Igbo Izugbe)",
    hello=[
        ("Who speaks it?", "About <b>30 million people</b> speak Igbo.<sup>³</sup>"),
        ("Where?", "In south-eastern <b>Nigeria</b> — around Enugu, Onitsha, Owerri and Aba — and in Igbo families all over the world."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with dots under <b>ị ọ ụ</b> and a dot over <b>ṅ</b>. "
                               "Today’s spelling was agreed in 1961 and is called the <b>Ọnwụ</b> alphabet."),
        ("How many letters?", "<b>36 letters</b>! Nine of them are pairs that count as one letter: ch, gb, gh, gw, kp, kw, nw, ny and sh."),
        ("Listen to the tune", "Igbo is a <b>tone</b> language: <i>akwa</i> can mean egg, cloth, bed or crying — your voice tells which! "
                               "Learner books mark the tones: <i>àkwá</i> (egg), <i>ákwà</i> (cloth)."),
        ("Did you know?", "Igbo has <b>8 vowels</b> in two teams — <b>a ị ọ ụ</b> and <b>e i o u</b> — and most words keep to one team, "
                          "like friends who play together."),
    ],
    hello_pics=[("ig_ji", {}), ("ig_orange", {}), ("sun", {})],
    map=region_map(frame=[[3.0, 1.5], [12.0, 10.5]],
                   points=dict(enugu=[7.50, 6.45], onitsha=[6.79, 6.15], owerri=[7.03, 5.48], aba=[7.37, 5.11], nsukka=[7.40, 6.86]),
                   area=(7.3, 5.9, 200, 200), area_rot=0,
                   cities=[("enugu", "Enugu", 14, 8, "start", False), ("onitsha", "Onitsha", -14, 8, "end", False),
                           ("owerri", "Owerri", -14, 8, "end", False), ("aba", "Aba", 14, 10, "start", False),
                           ("nsukka", "Nsukka", 14, 4, "start", False)],
                   label="WEST AFRICA", label_at=[3.5, 9.8], marker=[7.3, 6.0],
                   caption="The circle shows Igboland, in West Africa, on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Igbo is spoken in Enugu, Nsukka, "
                          "Onitsha, Owerri, Aba and many other towns. The dashed line shows where most Igbo speakers live.",
                   seas=[("Gulf of Guinea", 5.5, 2.8)], world_r=14),
    digits=[("0", "efu", "eh-foo", "zero"), ("1", "otu", "oh-too", "one"), ("2", "abụọ", "ah-bu-aw", "two"),
            ("3", "atọ", "ah-taw", "three"), ("4", "anọ", "ah-naw", "four"), ("5", "ise", "ee-seh", "five"),
            ("6", "isii", "ee-see-ee", "six"), ("7", "asaa", "ah-sah-ah", "seven"), ("8", "asatọ", "ah-sah-taw", "eight"),
            ("9", "itoolu", "ee-toh-oh-loo", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-lah-moo ah-lay-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum salaam", "wah ah-lay-koom sah-lahm", "And peace be upon you (the reply)"),
             ("Ndewo!", "n-deh-woh", "Hello!"),
             ("Aha m bụ …", "ah-hah m bu …", "My name is …"),
             ("Daalụ", "dah-ah-lu", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-kah-lah-hoo khai-rahn", "May Allah reward you with good"),
             ("nne · nna", "n-neh · n-nah", "Mother · Father"),
             ("nwanne nwoke · nwanne nwaanyị", "nwahn-neh nwoh-keh · nwahn-neh nwah-ah-nyih", "Brother · Sister"),
             ("Ee · Mba", "eh-eh · m-bah", "Yes · No"),
             ("Ana m amụ asụsụ Igbo!", "ah-nah m ah-mu ah-su-su ee-gboh", "I am learning Igbo!")],
    cheer=("Mashallah! I mere nke ọma!", "mah-shah-lah! ee meh-reh n-keh aw-mah", "Mashallah! You did well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B CH", right="D E F"),
    review_note="Check the letter names (a, bị, chị, dị… with fụ, gwụ, kwụ, mụ, nụ, ṅụ, nwụ, wụ) against the Abịdịị song taught today. "
                "Uncertain words: <i>ịgha mkpụrụ</i> (sowing seeds) for GH, <i>ọshịmịrị</i> (sea; standard <i>osimiri</i>) for SH, "
                "<i>ivu</i> (load) for V, <i>akị oyibo</i> (coconut), <i>pensụl</i>, <i>tomato</i>, <i>ụdara</i>, <i>ugegbe anya</i>; "
                "and the title <i>Abịdịị Igbo mbụ m</i>.",
    tiles="AỊKỌỤZ", cover_pics=["ig_ji", "ig_orange", "star", "flower"],
    speakers_blurb="Igbo is spoken by about 30 million people, most of them in south-eastern Nigeria.",
    sample_words=[("ụlọ", "u-law", "house"), ("mmiri", "m-mee-ree", "water"), ("kpakpando", "kpah-kpahn-doh", "star")],
    keywords=["igbo alphabet book for kids", "learn igbo for children", "igbo abidii coloring book",
              "igbo letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual igbo english toddlers"],
))
