# -*- coding: utf-8 -*-
"""Book 66 - Somali (Latin script, 26 letters in the Somali order). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Bb"); digraphs drawn "Kh kh", "Sh sh", "Dh dh"."""
from generic import build, section
from maps import region_map
from _so_om_zu_xh import FONTS, GLYPH_FONTS, CSS, maker

L = maker("Somali letter name · higgaad")
THROAT = "Say it from deep in the throat."

CONSONANTS = [
    L("B", "Ba", "bah", "‘b’ as in “ball”", "biyo", "bi-yoh", "water", "water"),
    L("T", "Ta", "tah", "‘t’ as in “tap”", "timir", "ti-mir", "dates", "dates"),
    L("J", "Ja", "jah", "‘j’ as in “jam”", "jaranjaro", "ja-ran-ja-roh", "ladder · stairs", "ladder"),
    L("X", "Xa", "hhah", "a strong, breathy ‘h’ from deep in the throat (like Arabic <i>Ḥā’</i>)", "xiddig", "hhid-dig", "star", "star",
      rule="X is <b>not</b> ‘ks’ in Somali! " + THROAT),
    L("KH", "Kha", "khah", "a scratchy ‘kh’ as in Scottish “loch” (like Arabic <i>Khā’</i>)", "khudaar", "khoo-daar", "vegetables", "so_khudaar",
      rule="KH is found mostly in words from Arabic."),
    L("D", "Da", "dah", "‘d’ as in “dog”", "daaqad", "daa-qad", "window", "window"),
    L("R", "Ra", "rah", "a rolled ‘r’ — let your tongue buzz", "roob", "rohb", "rain", "raincloud"),
    L("S", "Sa", "sah", "‘s’ as in “sun”", "saacad", "saa-'ad", "clock · watch", "clock"),
    L("SH", "Sha", "shah", "‘sh’ as in “ship”", "shaah", "shaah", "tea", "teacup"),
    L("DH", "Dha", "dhah", "a ‘d’ made with the tongue curled back — it can sound a little like ‘r’", "dhagax", "dha-gahh", "stone", "mni_stones",
      rule="DH is one Somali sound, not ‘d’ + ‘h’."),
    L("C", "Ca", "'ah", "a squeezed sound from deep in the throat (like Arabic <i>‘Ayn</i>)", "caano", "'aa-noh", "milk", "zgh_milk",
      rule="C is <b>not</b> ‘k’ or ‘s’ in Somali! " + THROAT),
    L("G", "Ga", "gah", "‘g’ as in “go”", "guri", "goo-ri", "house · home", "house"),
    L("F", "Fa", "fah", "‘f’ as in “fan”", "fure", "foo-reh", "key", "si_key"),
    L("Q", "Qa", "qah", "a deep ‘k’ from the back of the throat (like Arabic <i>Qāf</i>)", "qalin", "qa-lin", "pen", "pen"),
    L("K", "Ka", "kah", "‘k’ as in “kite”", "kubbad", "koob-bad", "ball", "ball"),
    L("L", "La", "lah", "‘l’ as in “lamp”", "liin", "leen", "lemon", "lemon"),
    L("M", "Ma", "mah", "‘m’ as in “moon”", "masjid", "mas-jid", "mosque", "mosque"),
    L("N", "Na", "nah", "‘n’ as in “net”", "nal", "nahl", "lamp · light", "bulb"),
    L("W", "Wa", "wah", "‘w’ as in “water”", "webi", "weh-bi", "river", "mni_river"),
    L("H", "Ha", "hah", "a soft ‘h’ as in “hat”", "hadiyad", "ha-di-yad", "gift · present", "gift"),
    L("Y", "Ya", "yah", "‘y’ as in “yes”", "yaanyo", "yaan-yoh", "tomato", "tomato"),
]

LONG = "Write it twice for a long sound: "
VOWELS = [
    L("A", "A", "ah", "‘a’ as in “father”", "albaab", "al-baab", "door", "door", vowel=True,
      row="a · aa — ba · baa", rule=LONG + "<b>aa</b>."),
    L("E", "E", "eh", "‘e’ as in “bed”", "g[ee]d", "gehd", "tree", "tree", vowel=True,
      row="e · ee — be · bee", rule=LONG + "<b>ee</b>.",
      note="Few words start with E. Find the long <b>ee</b> inside <i>geed</i>!"),
    L("I", "I", "ee", "‘i’ as in “sit”; long <b>ii</b> as in “see”", "ibriiq", "ib-reeq", "water jug for wudu", "ewer", vowel=True,
      row="i · ii — bi · bii", rule=LONG + "<b>ii</b>."),
    L("O", "O", "oh", "‘o’ as in “for” (short and pure)", "olol", "o-lol", "flame", "chr_fire", vowel=True,
      row="o · oo — bo · boo", rule=LONG + "<b>oo</b>."),
    L("U", "U", "oo", "‘u’ as in “put”; long <b>uu</b> as in “moon”", "ukun", "oo-koon", "egg", "egg", vowel=True,
      row="u · uu — bu · buu", rule=LONG + "<b>uu</b>."),
]

LANG = build(dict(
    code="so", folder="book-66-somali", series_no=66, isbn="", draft=True,
    name="Somali", native="af-Soomaali", native_tr="af soo-maa-li", name_word="magac", write_word="qor",
    title_native="Alifbeetada af-Soomaaliga", title_letters="BbTtJj", belongs_native="Buuggan waxaa leh",
    belongs_pic="star", alphabet_native="higgaadda Soomaaliga", numbers_native="tirooyinka", numbers_tr="ti-roh-yin-ka",
    phrases_native="Erayada ugu horreeya",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit="Baloo 2",
    extra_css=CSS,
    phon_feature="each letter’s Somali name and its syllables (Ba: ba be bi bo bu)",
    sections=[
        section(CONSONANTS, label="CONSONANT", chip="THE CONSONANTS", title="The Consonants",
                native="shibbanayaasha", native_tr="shib-ba-na-yaa-sha — “the consonants”",
                chart_title="consonants", chart_cols=7, warmup_title="the consonants", warmup_cols=6,
                intro_html="""<p>Somali children learn their letters in a special order that begins
<b>B T J X KH D R S SH DH C G F Q K L M N W H Y</b>. This book keeps that order: <b>21 consonants</b>, then the <b>5 vowels</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Sounds from the throat</h3><b>X</b>, <b>C</b>, <b>KH</b> and <b>Q</b> are deep throat sounds — the same
sounds as the Arabic letters <i>Ḥā’</i>, <i>‘Ayn</i>, <i>Khā’</i> and <i>Qāf</i> that you hear in the Qur’an. In Somali, <b>X</b> is never ‘ks’ and <b>C</b> is never ‘k’!</div>
<div class="box" style="margin:0.1in 0"><h3>Two letters, one sound</h3><b>KH</b>, <b>SH</b> and <b>DH</b> are written with two letters but are
each <b>one</b> sound, with a page of their own.</div>
<div class="box"><h3>Ba, be, bi, bo, bu</h3>Somali children read by joining each letter with the vowels. Every page shows the
letter’s row: <i>ba · be · bi · bo · bu</i>. Say it like a song!</div>"""),
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels",
                native="shaqallada", native_tr="sha-qal-la-da — “the vowels”",
                chart_title="vowels", chart_cols=5, warmup_title="the vowels", warmup_cols=5,
                intro_html="""<p>Somali has <b>5 vowels</b>: <b>A E I O U</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Short and long</h3>Each vowel can be <b>short</b> (a) or <b>long</b> (aa). Write it twice and hold
the sound a little longer: <i>bar</i> and <i>baar</i> are different words!</div>
<div class="box"><h3>The little stop</h3>Somali also uses a small mark, <b>’</b>, for a tiny catch in the voice, as in
<i>lo’</i> (cattle). It is called <i>hamsa</i>.</div>"""),
    ],
    sound_notes=[
        "<b>hh</b> in the pronunciation is the deep, breathy ‘h’ of Somali <b>X</b>.",
        "<b>'</b> (an apostrophe) in the pronunciation is the squeezed throat sound of Somali <b>C</b>.",
        "<b>q</b> is a deep ‘k’ from the back of the throat; <b>kh</b> is the scratchy sound in “loch”.",
        "<b>dh</b> is a ‘d’ with the tongue curled back; <b>r</b> is rolled.",
        "In Somali spelling a doubled vowel is long (<b>aa ee ii oo uu</b>). In the pronunciation, <b>aa</b> is a long ‘a’ as in “father”, "
        "<b>ee</b> says ‘ee’ as in “see”, <b>oo</b> says ‘oo’ as in “moon”, <b>oh</b> says ‘o’ as in “go” and <b>eh</b> says ‘e’ as in “bed”.",
        "Somali uses rises in pitch rather than strong stress, so no syllable is written in capitals here."],
    phon_explain="The box marked <i>Somali letter name · higgaad</i> shows the name Somali children use for the letter "
                 "(B is «Ba», X is «Xa»…) and its row of syllables, the way Somali children learn to read (<i>higgaad</i>).",
    standard="Standard Somali (af-Maxaa)",
    hello=[
        ("Who speaks it?", "About <b>22 million people</b> speak Somali.<sup>³</sup>"),
        ("Where?", "In the <b>Horn of Africa</b> — Somalia, Djibouti, eastern Ethiopia and northeastern Kenya — and by Somali families all over the world."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. For centuries, Somali scholars also wrote it in Arabic letters."),
        ("How many letters?", "<b>21 consonants</b> and <b>5 vowels</b> — <b>26 letters</b> — plus the little stop mark <b>’</b>."),
        ("Sounds of the Qur’an", "Somali <b>X</b>, <b>C</b> and <b>Q</b> are the throat sounds of the Arabic letters <i>Ḥā’</i>, <i>‘Ayn</i> and <i>Qāf</i>, so Somali children find "
                                 "Qur’an letters easy to say!"),
        ("Did you know?", "Somalia is often called a <b>“nation of poets”</b>. Many Somali words come from Arabic: "
                          "<i>kitaab</i> (book), <i>salaad</i> (prayer), <i>masjid</i> (mosque)."),
    ],
    hello_pics=[("star", {}), ("dates", {}), ("mosque", {})],
    map=region_map(frame=[[37.0, -3.0], [55.0, 15.0]],
                   points=dict(mogadishu=[45.34, 2.04], djibouti=[43.15, 11.59], hargeisa=[44.06, 9.56], kismayo=[42.54, -0.36],
                               bosaso=[49.18, 11.28]),
                   area=(46.0, 6.5, 240, 290),
                   cities=[("mogadishu", "Mogadishu", 14, 8, "start", False), ("djibouti", "Djibouti", -14, 8, "end", False),
                           ("hargeisa", "Hargeisa", -14, 18, "end", False), ("kismayo", "Kismayo", -14, 8, "end", False),
                           ("bosaso", "Bosaso", 14, -8, "start", False)],
                   label="HORN OF AFRICA", label_at=[42.5, 4.5], marker=[45.0, 6.0],
                   caption="The circle shows the Horn of Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> the dashed line shows where most "
                          "Somali speakers live, around Mogadishu, Hargeisa, Bosaso, Kismayo and Djibouti.",
                   seas=[("Indian Ocean", 51.0, 1.0), ("Gulf of Aden", 47.5, 13.2)], world_r=13),
    digits=[("0", "eber", "e-ber", "zero"), ("1", "kow", "kow", "one"), ("2", "laba", "la-ba", "two"), ("3", "saddex", "sad-dehh", "three"),
            ("4", "afar", "a-far", "four"), ("5", "shan", "shan", "five"), ("6", "lix", "lihh", "six"), ("7", "toddoba", "tod-do-ba", "seven"),
            ("8", "siddeed", "sid-dehd", "eight"), ("9", "sagaal", "sa-gaal", "nine")],
    phrases=[("Assalaamu calaykum", "as-sa-laa-moo 'a-lay-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wacalaykum assalaam", "wa-'a-lay-koom as-sa-laam", "And upon you be peace (the reply)"),
             ("Iska warran?", "is-ka war-ran", "Hello, how are you?"),
             ("Magacaygu waa …", "ma-ga-'ay-goo waa …", "My name is …"),
             ("Mahadsanid", "ma-had-sa-nid", "Thank you"),
             ("Jazaakallaahu khayran", "ja-zaa-kal-laa-hoo khay-ran", "May Allah reward you with good"),
             ("hooyo · aabbe", "hoh-yoh · aab-beh", "Mother · Father"),
             ("walaalkay · walaashay", "wa-laal-kay · wa-laa-shay", "My brother · My sister"),
             ("haa · maya", "haa · ma-ya", "Yes · No"),
             ("Waxaan baranayaa af-Soomaali!", "wa-hhaan ba-ra-na-yaa af soo-maa-li", "I am learning Somali!")],
    cheer=("Maashaa Allah! Aad u fiican!", "maa-shaa al-lah! aad oo fee-'an", "Mashallah! Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="B T J", right="X C Q"),
    review_note="Machine-drafted: a native Somali speaker must check every word, the Somali book title, section names, "
                "the cheer and phrases, and the simple transliterations (stress/tone not marked).",
    tiles="BTJXCQ", cover_pics=["star", "mosque", "dates", "teacup"], title_size=48,
    speakers_blurb="Somali is spoken by about 22 million people in the Horn of Africa and around the world.",
    sample_words=[("xiddig", "hhid-dig", "star"), ("caano", "'aa-noh", "milk"), ("masjid", "mas-jid", "mosque")],
    keywords=["somali alphabet book for kids", "learn somali for children", "af soomaali coloring book",
              "somali letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual somali english toddlers"],
))
