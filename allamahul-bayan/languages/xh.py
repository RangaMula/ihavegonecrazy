# -*- coding: utf-8 -*-
"""Book 69 - Xhosa / isiXhosa (Latin script, 26 letters + 8 letter pairs). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Bb"); letter pairs drawn "Hl hl". In each word the letter is underlined,
because Xhosa nouns begin with a small prefix (i-, u-, isi-, um-...)."""
from generic import build, section
from maps import region_map
from _so_om_zu_xh import FONTS, GLYPH_FONTS, CSS, maker

L = maker("Xhosa letter name · syllables")
LOAN = "used mostly in words borrowed from other languages"

LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "[a]manzi", "ah-MAHN-zee", "water", "water", vowel=True, row="ba · da · ka · la · ma"),
    L("B", "ba", "bah", "a soft ‘b’, said while breathing in a little", "u[b]isi", "oo-BEE-see", "milk", "zgh_milk",
      rule="B on its own is a soft, ‘swallowed’ b. <b>BH</b> is the ordinary ‘b’ of English."),
    L("C", "ca", "[c]ah", "a <b>click</b>! Pull the tip of your tongue back from your top teeth: “tsk!”", "i[c]ephe",
      "ee-[c]EH-peh", "spoon", "spoon", rule="The <b>tsk-tsk</b> click, like saying “what a pity!”"),
    L("D", "da", "dah", "‘d’ as in “dog”", "ii[d]iliya", "ee-dee-LEE-yah", "grapes", "grapes"),
    L("E", "e", "eh", "‘e’ as in “bed”", "ibh[e]di", "ee-BEH-dee", "bed", "th_bed", vowel=True, row="be · de · ke · le · me",
      note="Xhosa words hardly ever start with E. Find it inside <i>ibhedi</i>!"),
    L("F", "fa", "fah", "‘f’ as in “fan”", "i[f]estile", "ee-fes-TEE-leh", "window", "window"),
    L("G", "ga", "gah", "‘g’ as in “go”", "i[g]ubu", "ee-GOO-boo", "drum", "dz_drum"),
    L("H", "ha", "hah", "‘h’ as in “hat”", "i[h]empe", "ee-HEM-peh", "shirt", "zu_shirt"),
    L("I", "i", "ee", "‘ee’ as in “see”", "[i]langa", "ee-LAHN-gah", "sun", "sun", vowel=True, row="bi · di · ki · li · mi"),
    L("J", "ja", "jah", "‘j’ as in “jam”", "u[j]ongilanga", "oo-jon-gee-LAHN-gah", "sunflower", "am_sunflower",
      rule="<i>ujongilanga</i> means “the one that looks at the sun”!"),
    L("K", "ka", "kah", "a soft ‘k’ (no puff of air)", "i[k]omityi", "ee-koh-MEE-tyee", "cup", "teacup",
      rule="K is soft; <b>KH</b> is a ‘k’ with a puff of air."),
    L("L", "la", "lah", "‘l’ as in “lamp”", "i[l]itye", "ee-LEE-tyeh", "stone", "sat_stones"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "u[m]lilo", "oom-LEE-loh", "fire", "dz_fire"),
    L("N", "na", "nah", "‘n’ as in “net”", "i[n]kwenkwezi", "een-kwen-KWEH-zee", "star", "star"),
    L("O", "o", "oh", "‘o’ as in “for” (short and pure)", "i[o]renji", "ee-oh-REN-jee", "orange", "ig_orange", vowel=True,
      row="bo · do · ko · lo · mo"),
    L("P", "pa", "pah", "a soft ‘p’ (no puff of air)", "i[p]ensile", "ee-pen-SEE-leh", "pencil", "km_pencil",
      rule="P is soft; <b>PH</b> is a ‘p’ with a puff of air."),
    L("Q", "qa", "[q]ah", "a <b>click</b>! Pop your tongue off the roof of your mouth, like a cork", "i[q]anda", "ee-[q]AHN-dah", "egg", "egg",
      rule="The loud <b>pop</b> click, like a bottle opening."),
    L("R", "ra", "rah", "‘r’ — " + LOAN, "i[r]ayisi", "ee-rah-YEE-see", "rice", "rice",
      rule="In Xhosa words, R comes mostly as <b>RH</b>: a scratchy sound like ‘ch’ in Scottish “loch”."),
    L("S", "sa", "sah", "‘s’ as in “sun”", "i[s]itya", "ee-SEE-tyah", "dish · bowl", "dz_bowl"),
    L("T", "ta", "tah", "a soft ‘t’ (no puff of air)", "i[t]afile", "ee-tah-FEE-leh", "table", "km_table",
      rule="T is soft; <b>TH</b> is a ‘t’ with a puff of air — never the ‘th’ of “think”."),
    L("U", "u", "oo", "‘oo’ as in “moon”", "[u]mlambo", "oom-LAHM-boh", "river", "mni_river", vowel=True, row="bu · du · ku · lu · mu"),
    L("V", "va", "vah", "‘v’ as in “van”", "im[v]ula", "eem-VOO-lah", "rain", "raincloud"),
    L("W", "wa", "wah", "‘w’ as in “water”", "i[w]otshi", "ee-WOH-tshee", "watch · clock", "clock"),
    L("X", "xa", "[x]ah", "a <b>click</b>! Click the side of your tongue, like calling a horse", "isi[x]hobo", "ee-see-[x]OH-boh",
      "tool", "tools", rule="The side click — the first sound of the word <i>Xhosa</i>! X is <b>never</b> ‘ks’ here."),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "i[y]eza", "ee-YEH-zah", "medicine", "medicine"),
    L("Z", "za", "zah", "‘z’ as in “zoo”", "i[z]ulu", "ee-ZOO-loo", "sky", "clouds"),
]

PAIRS = [
    L("BH", "bha", "bah", "‘b’ as in “ball”", "i[bh]ola", "ee-BOH-lah", "ball", "ball"),
    L("DL", "dla", "dlah", "a buzzing ‘l’: say ‘d’ and ‘l’ together, with air at the sides of the tongue", "in[dl]u", "EEN-dloo",
      "house", "house"),
    L("HL", "hla", "hlah", "a hissing ‘l’: blow air past the sides of your tongue (like Welsh “ll”)", "i[hl]athi", "ee-HLAH-tee",
      "forest", "tree"),
    L("KH", "kha", "kah", "‘k’ with a puff of air, as in “kite”", "i[kh]iwane", "ee-kee-WAH-neh", "fig", "fig"),
    L("NY", "nya", "nyah", "‘ny’ as in “canyon”", "i[ny]anga", "ee-NYAHN-gah", "moon", "moon"),
    L("PH", "pha", "pah", "‘p’ with a puff of air, as in “pen” — not ‘f’!", "i[ph]e[ph]a", "ee-PEH-pah", "paper", "th_paper"),
    L("TH", "tha", "tah", "‘t’ with a puff of air, as in “tap” — not ‘th’!", "i[th]anga", "ee-TAHN-gah", "pumpkin", "th_pumpkin"),
    L("TY", "tya", "tyah", "a quick ‘t’ + ‘y’ said together, close to the ‘ch’ in “church”", "i[ty]uwa", "ee-TYOO-wah", "salt", "salt",
      args=dict(label="ityuwa")),
]

LANG = build(dict(
    code="xh", folder="book-69-xhosa", series_no=69, isbn="", draft=True,
    name="Xhosa", native="isiXhosa", native_tr="ee-see-[x]OH-sah", name_word="igama", write_word="bhala",
    title_native="Oonobumba besiXhosa", title_letters="XxCcQq", belongs_native="Le ncwadi yeka",
    belongs_pic="star", alphabet_native="oonobumba", numbers_native="amanani", numbers_tr="ah-mah-NAH-nee",
    phrases_native="Amagama okuqala",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit="Baloo 2",
    extra_css=CSS,
    phon_feature="each letter’s Xhosa syllables (ba: ba be bi bo bu) and an introduction to the clicks C, Q and X",
    sections=[
        section(LETTERS, native="oonobumba", native_tr="oh-noh-BOOM-bah — “the letters”",
                chart_cols=7, warmup_cols=6,
                intro_html="""<p>isiXhosa uses the same <b>26 letters</b> as English. A few of them make very different sounds!</p>
<div class="box" style="margin:0.1in 0"><h3>Three clicks: C · Q · X</h3>
<b>C</b> — the “tsk-tsk” click: pull your tongue tip back from your top teeth.<br>
<b>Q</b> — the “pop” click: pop your tongue off the roof of your mouth, like a cork.<br>
<b>X</b> — the side click: click the side of your tongue, like calling a horse. You hear it in the name <b>Xhosa</b>!<br>
In the sound guides, <b>[c] [q] [x]</b> mean: make the click!</div>
<div class="box" style="margin:0.1in 0"><h3>Look past the prefix</h3>Xhosa words begin with a small part such as <b>i-</b>, <b>u-</b>, <b>isi-</b>
or <b>um-</b>: <i>i</i>-qanda (egg), <i>i</i>-cephe (spoon). The letter you are learning is <u>underlined</u> in each word.</div>
<div class="box"><h3>Ba, be, bi, bo, bu</h3>Every Xhosa syllable ends in a vowel. Every page shows the letter’s row:
<i>ba · be · bi · bo · bu</i>. Say it like a song!</div>"""),
        section(PAIRS, label="LETTER PAIR", chip="LETTER PAIRS", title="Letter Pairs",
                native="bh · dl · hl · kh · ny · ph · th · ty", native_tr="eight pairs that make one sound each",
                chart_title="letter pairs", chart_cols=4, warmup_title="the letter pairs", warmup_cols=4,
                intro_html="""<p>Many Xhosa sounds are written with <b>two letters</b>. Each pair is <b>one sound</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>A puff of air</h3>An <b>H</b> after a letter often adds a puff of air: <b>KH PH TH</b>.
So <b>PH</b> is never ‘f’ and <b>TH</b> is never the ‘th’ of “think”.</div>
<div class="box" style="margin:0.1in 0"><h3>Two special sounds: HL and DL</h3><b>HL</b> is a hissing ‘l’ and <b>DL</b> a buzzing ‘l’: let the air
slide past the sides of your tongue, as in <i>ihlathi</i> (forest) and <i>indlu</i> (house).</div>
<div class="box"><h3>Clicks in pairs too</h3>Clicks can team up with other letters: <b>gq</b>, <b>nq</b>, <b>xh</b>, <b>ngc</b>… Listen for them in
<i>isiXhosa</i> itself!</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: in Xhosa it is nearly always the second-to-last one, <i>ee-[q]AHN-dah</i>.",
        "<b>[c] [q] [x]</b> mean: make that <b>click</b> (see “Three clicks” before the letter pages).",
        "<b>hl</b> is a hissing ‘l’ and <b>dl</b> a buzzing ‘l’; in the pronunciation, <b>t</b>, <b>k</b> and <b>p</b> are never ‘th’ or ‘f’.",
        "<b>ee</b> says ‘ee’ as in “see”, <b>oo</b> says ‘oo’ as in “moon”, <b>oh</b> says ‘o’ as in “go”, <b>eh</b> says ‘e’ as in “bed”."],
    phon_explain="The box marked <i>Xhosa letter name · syllables</i> shows how Xhosa children say the letter (B is «ba», C is «ca»…) "
                 "and its row of syllables, the way they learn to read.",
    standard="Standard written Xhosa",
    hello=[
        ("Who speaks it?", "About <b>19 million people</b> speak isiXhosa, at home or as a second language.<sup>³</sup>"),
        ("Where?", "Mostly in <b>South Africa</b>, especially in the <b>Eastern Cape</b> and the <b>Western Cape</b>, around East London, "
                   "Gqeberha and Cape Town."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>26 letters</b>, plus many letter pairs such as <b>hl</b>, <b>dl</b>, <b>ty</b> and <b>xh</b>."),
        ("Clicks!", "<b>C</b>, <b>Q</b> and <b>X</b> are <b>click sounds</b> — and the name <b>Xhosa</b> itself starts with a click!"),
        ("Did you know?", "isiXhosa and isiZulu are close cousins: <i>amanzi</i> means <b>water</b> and <i>ilanga</i> means "
                          "<b>sun</b> in both!"),
    ],
    hello_pics=[("am_sunflower", {}), ("egg", {}), ("moon", {})],
    map=region_map(frame=[[17.0, -36.5], [32.0, -21.5]],
                   points=dict(eastlondon=[27.91, -33.02], gqeberha=[25.60, -33.96], mthatha=[28.78, -31.59],
                               capetown=[18.42, -33.92], komani=[26.87, -31.90]),
                   area=(27.2, -32.4, 200, 150),
                   cities=[("eastlondon", "East London", 14, 8, "start", False), ("gqeberha", "Gqeberha", -12, 20, "end", False),
                           ("mthatha", "Mthatha", 14, 8, "start", False), ("capetown", "Cape Town", 14, 8, "start", False),
                           ("komani", "Komani", -14, 8, "end", False)],
                   label="SOUTH AFRICA", label_at=[22.5, -27.0], marker=[25.0, -31.0],
                   caption="The circle shows southern Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the oceans <b>blue</b>. <b>Find it:</b> the dashed line shows where most "
                          "Xhosa speakers live, around East London, Gqeberha, Mthatha and Komani; many families also live in Cape Town.",
                   seas=[("Atlantic Ocean", 19.5, -24.0), ("Indian Ocean", 29.0, -35.5)], world_r=13),
    digits=[("0", "iqanda", "ee-[q]AHN-dah", "zero"), ("1", "inye", "EE-nyeh", "one"), ("2", "zimbini", "zeem-BEE-nee", "two"),
            ("3", "zintathu", "zeen-TAH-too", "three"), ("4", "zine", "ZEE-neh", "four"), ("5", "zintlanu", "zeen-TLAH-noo", "five"),
            ("6", "zintandathu", "zeen-tahn-DAH-too", "six"), ("7", "zisixhenxe", "zee-see-[x]EN-[x]eh", "seven"),
            ("8", "zisibhozo", "zee-see-BOH-zoh", "eight"), ("9", "zilithoba", "zee-lee-TOH-bah", "nine")],
    phrases=[("Assalaamu alaykum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaykum assalaam", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Molo!", "MOH-loh", "Hello! (to one person)"),
             ("Igama lam ngu…", "ee-GAH-mah lahm ngoo…", "My name is …"),
             ("Enkosi", "en-KOH-see", "Thank you"),
             ("Jazaakallaahu khayran", "jah-zaa-kal-LAA-hoo KHAY-ran", "May Allah reward you with good"),
             ("umama · utata", "oo-MAH-mah · oo-TAH-tah", "Mother · Father"),
             ("ubhuti · usisi", "oo-BOO-tee · oo-SEE-see", "Brother · Sister"),
             ("ewe · hayi", "EH-weh · HAH-yee", "Yes · No"),
             ("Ndifunda isiXhosa!", "ndee-FOON-dah ee-see-[x]OH-sah", "I am learning Xhosa!")],
    cheer=("Mashallah! Wenze kakuhle!", "mah-SHAH-lah! WEN-zeh kah-KOO-hleh", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="A B C", right="Q X Z"),
    review_note="Machine-drafted: a native Xhosa speaker must check every word (especially iidiliya, iorenji, isixhobo, ibhedi, ihempe), "
                "the book title, the numbers (zero = iqanda?) and phrases, the click spellings and the stress marks.",
    tiles="XCQAMZ", cover_pics=["am_sunflower", "egg", "sun", "star"], title_size=50,
    speakers_blurb="isiXhosa is spoken by about 19 million people, mostly in South Africa.",
    sample_words=[("iqanda", "ee-[q]AHN-dah", "egg"), ("icephe", "ee-[c]EH-peh", "spoon"), ("ilanga", "ee-LAHN-gah", "sun")],
    keywords=["xhosa alphabet book for kids", "learn isixhosa for children", "xhosa coloring book clicks",
              "xhosa letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual xhosa english toddlers south africa"],
))
