# -*- coding: utf-8 -*-
"""Book 68 - Zulu / isiZulu (Latin script, 26 letters + 7 letter pairs). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Bb"); letter pairs drawn "Hl hl". In each word the letter is underlined,
because Zulu nouns begin with a small prefix (i-, u-, isi-, um-...)."""
from generic import build, section
from maps import region_map
from _so_om_zu_xh import FONTS, GLYPH_FONTS, CSS, maker

L = maker("Zulu letter name · syllables")
LOAN = "used mostly in words borrowed from other languages"

LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "[a]manzi", "ah-MAHN-zee", "water", "water", vowel=True, row="ba · da · ka · la · ma"),
    L("B", "ba", "bah", "a soft ‘b’, said while breathing in a little", "u[b]isi", "oo-BEE-see", "milk", "zgh_milk",
      rule="B on its own is a soft, ‘swallowed’ b. <b>BH</b> is the ordinary ‘b’ of English."),
    L("C", "ca", "[c]ah", "a <b>click</b>! Pull the tip of your tongue back from your top teeth: “tsk!”", "isi[c]athulo",
      "ee-see-[c]ah-TOO-loh", "shoe", "mni_shoe", rule="The <b>tsk-tsk</b> click, like saying “what a pity!”"),
    L("D", "da", "dah", "‘d’ as in “dog”", "i[d]wala", "ee-DWAH-lah", "rock · big stone", "km_stones"),
    L("E", "e", "eh", "‘e’ as in “bed”", "ikh[e]kh[e]", "ee-KEH-keh", "cake", "zu_cake", vowel=True, row="be · de · ke · le · me",
      note="Zulu words hardly ever start with E. Find it inside <i>ikhekhe</i>!"),
    L("F", "fa", "fah", "‘f’ as in “fan”", "i[f]asitela", "ee-fah-see-TEH-lah", "window", "window"),
    L("G", "ga", "gah", "‘g’ as in “go”", "i[g]agasi", "ee-gah-GAH-see", "wave", "waves"),
    L("H", "ha", "hah", "‘h’ as in “hat”", "i[h]embe", "ee-HEM-beh", "shirt", "zu_shirt"),
    L("I", "i", "ee", "‘ee’ as in “see”", "[i]langa", "ee-LAHN-gah", "sun", "sun", vowel=True, row="bi · di · ki · li · mi"),
    L("J", "ja", "jah", "‘j’ as in “jam”", "u[j]eqe", "oo-JEH-[q]eh", "steamed bread", "ru_bread"),
    L("K", "ka", "kah", "a soft ‘k’ (no puff of air)", "isi[k]ebhe", "ee-see-KEH-beh", "boat", "boat",
      rule="K is soft; <b>KH</b> is a ‘k’ with a puff of air."),
    L("L", "la", "lah", "‘l’ as in “lamp”", "i[l]ayisi", "ee-lah-YEE-see", "rice", "rice"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "i[m]ali", "ee-MAH-lee", "money", "chr_coins"),
    L("N", "na", "nah", "‘n’ as in “net”", "i[n]kanyezi", "een-kah-NYEH-zee", "star", "star"),
    L("O", "o", "oh", "‘o’ as in “for” (short and pure)", "um[o]ya", "oo-MOH-yah", "wind · air", "bal_wind", vowel=True,
      row="bo · do · ko · lo · mo"),
    L("P", "pa", "pah", "a soft ‘p’ (no puff of air)", "i[p]ensela", "ee-pen-SEH-lah", "pencil", "my_pencil",
      rule="P is soft; <b>PH</b> is a ‘p’ with a puff of air."),
    L("Q", "qa", "[q]ah", "a <b>click</b>! Pop your tongue off the roof of your mouth, like a cork", "i[q]anda", "ee-[q]AHN-dah", "egg", "egg",
      rule="The loud <b>pop</b> click, like a bottle opening."),
    L("R", "ra", "rah", "‘r’ — " + LOAN, "i[r]ozi", "ee-ROH-zee", "rose", "ks_rose"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "i[s]ando", "ee-SAHN-doh", "hammer", "th_hammer"),
    L("T", "ta", "tah", "a soft ‘t’ (no puff of air)", "u[t]amatisi", "oo-tah-mah-TEE-see", "tomato", "tomato",
      rule="T is soft; <b>TH</b> is a ‘t’ with a puff of air — never the ‘th’ of “think”."),
    L("U", "u", "oo", "‘oo’ as in “moon”", "[u]mfula", "oom-FOO-lah", "river", "mni_river", vowel=True, row="bu · du · ku · lu · mu"),
    L("V", "va", "vah", "‘v’ as in “van”", "im[v]ula", "eem-VOO-lah", "rain", "raincloud"),
    L("W", "wa", "wah", "‘w’ as in “water”", "i[w]ashi", "ee-WAH-shee", "watch · clock", "clock"),
    L("X", "xa", "[x]ah", "a <b>click</b>! Click the side of your tongue, like calling a horse", "isi[x]hobo", "ee-see-[x]OH-boh",
      "tool", "tools", rule="The side click, made at the side of the mouth. In Zulu X is <b>never</b> ‘ks’!"),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "i[y]eza", "ee-YEH-zah", "medicine", "medicine"),
    L("Z", "za", "zah", "‘z’ as in “zoo”", "i[z]ambane", "ee-zahm-BAH-neh", "potato", "potato"),
]

PAIRS = [
    L("BH", "bha", "bah", "‘b’ as in “ball”", "i[bh]anana", "ee-bah-NAH-nah", "banana", "banana"),
    L("DL", "dla", "dlah", "a buzzing ‘l’: say ‘d’ and ‘l’ together, with air at the sides of the tongue", "in[dl]u", "EEN-dloo",
      "house", "house"),
    L("HL", "hla", "hlah", "a hissing ‘l’: blow air past the sides of your tongue (like Welsh “ll”)", "i[hl]athi", "ee-HLAH-tee",
      "forest", "tree"),
    L("KH", "kha", "kah", "‘k’ with a puff of air, as in “kite”", "u[kh]ezo", "oo-KEH-zoh", "spoon", "spoon"),
    L("NY", "nya", "nyah", "‘ny’ as in “canyon”", "i[ny]anga", "ee-NYAHN-gah", "moon", "moon"),
    L("PH", "pha", "pah", "‘p’ with a puff of air, as in “pen” — not ‘f’!", "i[ph]e[ph]a", "ee-PEH-pah", "paper", "th_paper"),
    L("TH", "tha", "tah", "‘t’ with a puff of air, as in “tap” — not ‘th’!", "i[th]anga", "ee-TAHN-gah", "pumpkin", "km_pumpkin"),
]

LANG = build(dict(
    code="zu", folder="book-68-zulu", series_no=68, isbn="", draft=True,
    name="Zulu", native="isiZulu", native_tr="ee-see-ZOO-loo", name_word="igama", write_word="bhala",
    title_native="Izinhlamvu zesiZulu", title_letters="AaBbCc", belongs_native="Le ncwadi ingeka",
    belongs_pic="star", alphabet_native="izinhlamvu", numbers_native="izinombolo", numbers_tr="ee-zee-nohm-BOH-loh",
    phrases_native="Amagama okuqala",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit="Baloo 2",
    extra_css=CSS,
    phon_feature="each letter’s Zulu syllables (ba: ba be bi bo bu) and an introduction to the clicks C, Q and X",
    sections=[
        section(LETTERS, native="izinhlamvu", native_tr="ee-zeen-HLAHM-voo — “the letters”",
                chart_cols=7, warmup_cols=6,
                intro_html="""<p>isiZulu uses the same <b>26 letters</b> as English. A few of them make very different sounds!</p>
<div class="box" style="margin:0.1in 0"><h3>Three clicks: C · Q · X</h3>
<b>C</b> — the “tsk-tsk” click: pull your tongue tip back from your top teeth.<br>
<b>Q</b> — the “pop” click: pop your tongue off the roof of your mouth, like a cork.<br>
<b>X</b> — the side click: click the side of your tongue, like calling a horse.<br>
In the sound guides, <b>[c] [q] [x]</b> mean: make the click!</div>
<div class="box" style="margin:0.1in 0"><h3>Look past the prefix</h3>Zulu words begin with a small part such as <b>i-</b>, <b>u-</b>, <b>isi-</b>
or <b>um-</b>: <i>i</i>-qanda (egg), <i>isi</i>-cathulo (shoe). The letter you are learning is <u>underlined</u> in each word.</div>
<div class="box"><h3>Ba, be, bi, bo, bu</h3>Every Zulu syllable ends in a vowel. Every page shows the letter’s row:
<i>ba · be · bi · bo · bu</i>. Say it like a song!</div>"""),
        section(PAIRS, label="LETTER PAIR", chip="LETTER PAIRS", title="Letter Pairs",
                native="bh · dl · hl · kh · ny · ph · th", native_tr="seven pairs that make one sound each",
                chart_title="letter pairs", chart_cols=7, warmup_title="the letter pairs", warmup_cols=4,
                intro_html="""<p>Some Zulu sounds are written with <b>two letters</b>. Each pair is <b>one sound</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>A puff of air</h3>An <b>H</b> after a letter often adds a puff of air: <b>KH PH TH</b>.
So <b>PH</b> is never ‘f’ and <b>TH</b> is never the ‘th’ of “think”.</div>
<div class="box"><h3>Two special sounds: HL and DL</h3><b>HL</b> is a hissing ‘l’ and <b>DL</b> a buzzing ‘l’: let the air
slide past the sides of your tongue. Zulu children say them in <i>ihlathi</i> (forest) and <i>indlu</i> (house).</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: in Zulu it is nearly always the second-to-last one, <i>ee-[q]AHN-dah</i>.",
        "<b>[c] [q] [x]</b> mean: make that <b>click</b> (see “Three clicks” before the letter pages).",
        "<b>hl</b> is a hissing ‘l’ and <b>dl</b> a buzzing ‘l’; in the pronunciation, <b>t</b>, <b>k</b> and <b>p</b> are never ‘th’ or ‘f’.",
        "<b>ee</b> says ‘ee’ as in “see”, <b>oo</b> says ‘oo’ as in “moon”, <b>oh</b> says ‘o’ as in “go”, <b>eh</b> says ‘e’ as in “bed”."],
    phon_explain="The box marked <i>Zulu letter name · syllables</i> shows how Zulu children say the letter (B is «ba», C is «ca»…) "
                 "and its row of syllables, the way they learn to read.",
    standard="Standard written Zulu",
    hello=[
        ("Who speaks it?", "About <b>28 million people</b> speak isiZulu, at home or as a second language.<sup>³</sup>"),
        ("Where?", "Mostly in <b>South Africa</b>, especially around <b>Durban</b> and <b>Johannesburg</b>, and in neighbouring countries."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>."),
        ("How many letters?", "<b>26 letters</b>, plus letter pairs such as <b>hl</b>, <b>dl</b> and <b>ph</b> that make one sound."),
        ("Clicks!", "<b>C</b>, <b>Q</b> and <b>X</b> are <b>click sounds</b>. Say <i>iqanda</i> (egg) with a pop!"),
        ("Did you know?", "<i>izulu</i> means <b>sky</b>. And in isiZulu the word for zero is <i>iqanda</i> — the same word as “egg”, "
                          "because a zero is shaped like an egg!"),
    ],
    hello_pics=[("egg", {}), ("sun", {}), ("waves", {})],
    map=region_map(frame=[[23.0, -35.0], [37.0, -21.0]],
                   points=dict(durban=[31.03, -29.86], joburg=[28.05, -26.20], pmb=[30.38, -29.60], richards=[32.04, -28.78],
                               newcastle=[29.93, -27.76]),
                   area=(30.3, -28.0, 230, 210),
                   cities=[("durban", "Durban", 14, 8, "start", False), ("joburg", "Johannesburg", -14, 8, "end", False),
                           ("pmb", "Pietermaritzburg", -14, 10, "end", False), ("richards", "Richards Bay", 14, 8, "start", False),
                           ("newcastle", "Newcastle", -14, 8, "end", False)],
                   label="SOUTHERN AFRICA", label_at=[26.5, -23.0], marker=[29.0, -28.0],
                   caption="The circle shows southern Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> the dashed line shows where most "
                          "Zulu speakers live, around Durban, Pietermaritzburg, Richards Bay and Newcastle, up to Johannesburg.",
                   seas=[("Indian Ocean", 33.5, -32.5)], world_r=13),
    digits=[("0", "iqanda", "ee-[q]AHN-dah", "zero"), ("1", "kunye", "KOO-nyeh", "one"), ("2", "kubili", "koo-BEE-lee", "two"),
            ("3", "kuthathu", "koo-TAH-too", "three"), ("4", "kune", "KOO-neh", "four"), ("5", "kuhlanu", "koo-HLAH-noo", "five"),
            ("6", "isithupha", "ee-see-TOO-pah", "six"), ("7", "isikhombisa", "ee-see-kohm-BEE-sah", "seven"),
            ("8", "isishiyagalombili", "ee-see-shee-yah-gah-lohm-BEE-lee", "eight"),
            ("9", "isishiyagalolunye", "ee-see-shee-yah-gah-loh-LOO-nyeh", "nine")],
    phrases=[("Assalaamu alaykum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaykum assalaam", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Sawubona!", "sah-woo-BOH-nah", "Hello! (to one person)"),
             ("Igama lami ngu…", "ee-GAH-mah LAH-mee ngoo…", "My name is …"),
             ("Ngiyabonga", "ngee-yah-BOHN-gah", "Thank you"),
             ("Jazaakallaahu khayran", "jah-zaa-kal-LAA-hoo KHAY-ran", "May Allah reward you with good"),
             ("umama · ubaba", "oo-MAH-mah · oo-BAH-bah", "Mother · Father"),
             ("umfowethu · udadewethu", "oom-foh-WEH-too · oo-dah-deh-WEH-too", "My brother · My sister"),
             ("yebo · cha", "YEH-boh · [c]ah", "Yes · No"),
             ("Ngifunda isiZulu!", "ngee-FOON-dah ee-see-ZOO-loo", "I am learning Zulu!")],
    cheer=("Mashallah! Wenze kahle!", "mah-SHAH-lah! WEN-zeh KAH-hleh", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="A B C", right="Q X Z"),
    review_note="Machine-drafted: a native Zulu speaker must check every word (especially irozi, isixhobo, ikhekhe, iwashi), "
                "the book title and phrases, the click spellings and the stress marks.",
    tiles="CQXZUL", cover_pics=["egg", "sun", "banana", "star"], title_size=50,
    speakers_blurb="isiZulu is spoken by about 28 million people, mostly in South Africa.",
    sample_words=[("iqanda", "ee-[q]AHN-dah", "egg"), ("ilanga", "ee-LAHN-gah", "sun"), ("inkanyezi", "een-kah-NYEH-zee", "star")],
    keywords=["zulu alphabet book for kids", "learn isizulu for children", "zulu coloring book clicks",
              "zulu letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual zulu english toddlers south africa"],
))
