# -*- coding: utf-8 -*-
"""Book 54 - Cherokee (Cherokee syllabary, 85 signs). Allamahul Bayan Series. REVIEW DRAFT.
One page per syllabary sign, in the standard chart order (the same order as Unicode U+13A0-U+13F4).
Words are only given where the author was confident; other signs get a clearly marked sound-practice
page (or a word in which the sign sits inside) instead of an invented word."""
from generic import build, letter, section, fontset
from maps import region_map

# ---- the syllabary, in chart order; romanization = the Unicode character names ----
ROMAN = ("a e i o u v ga ka ge gi go gu gv ha he hi ho hu hv la le li lo lu lv ma me mi mo mu "
         "na hna nah ne ni no nu nv qua que qui quo quu quv sa s se si so su sv "
         "da ta de te di ti do du dv dla tla tle tli tlo tlu tlv tsa tse tsi tso tsu tsv "
         "wa we wi wo wu wv ya ye yi yo yu yv").split()
SYL = {r: chr(0x13A0 + i) for i, r in enumerate(ROMAN)}
assert len(SYL) == 85

def cw(roman):
    """'a-da' -> ᎠᏓ  (spell a word from its syllables, so no sign can be mistyped)."""
    return " ".join("".join(SYL[s] for s in w.split("-")) for w in roman.split())

ROWS = [("the vowel row", "a e i o u v"), ("the G / K row", "ga ka ge gi go gu gv"), ("the H row", "ha he hi ho hu hv"),
        ("the L row", "la le li lo lu lv"), ("the M row", "ma me mi mo mu"), ("the N row", "na hna nah ne ni no nu nv"),
        ("the GW (QU) row", "qua que qui quo quu quv"), ("the S row", "sa s se si so su sv"),
        ("the D / T row", "da ta de te di ti do du dv"), ("the DL / TL row", "dla tla tle tli tlo tlu tlv"),
        ("the J (TS) row", "tsa tse tsi tso tsu tsv"), ("the W row", "wa we wi wo wu wv"), ("the Y row", "ya ye yi yo yu yv")]
ROW_OF = {s: (name, row.split()) for name, row in ROWS for s in row.split()}

VOW = {"a": ("ah", "‘ah’ as in “father”"), "e": ("eh", "‘eh’ as in “bed”"), "i": ("ee", "‘ee’ as in “see”"),
       "o": ("oh", "‘oh’ as in “go”"), "u": ("oo", "‘oo’ as in “moon”"),
       "v": ("uhn", "‘uh’ said through the nose, like a humming “uh”")}
CONS = {"": ("", ""), "g": ("g", "‘g’ as in “go”"), "k": ("k", "‘k’ as in “kite”"), "h": ("h", "‘h’ as in “hat”"),
        "l": ("l", "‘l’ as in “lamp”"), "m": ("m", "‘m’ as in “moon”"), "n": ("n", "‘n’ as in “net”"),
        "hn": ("hn", "a breathy ‘n’ (blow a little air before the n)"), "qu": ("gw", "‘gw’ as in “Gwen” (some say ‘kw’ as in “queen”)"),
        "s": ("s", "‘s’ as in “sun”"), "d": ("d", "‘d’ as in “dog”"), "t": ("t", "‘t’ as in “top”"),
        "dl": ("dl", "‘dl’ — a soft ‘d’ that slides into ‘l’"), "tl": ("tl", "‘tl’ — a ‘t’ that slides into ‘l’, with air at the sides of the tongue"),
        "ts": ("j", "‘j’ as in “jam” (some families say ‘ts’ as in “cats”)"), "w": ("w", "‘w’ as in “water”"), "y": ("y", "‘y’ as in “yes”")}

def split(r):
    for c in ("hn", "qu", "dl", "tl", "ts", "g", "k", "h", "l", "m", "n", "s", "d", "t", "w", "y"):
        if r.startswith(c) and r[len(c):] in VOW:
            return c, r[len(c):]
    return "", r

def say(r):
    if r == "s": return "s"
    if r == "nah": return "nah"
    c, v = split(r)
    return CONS[c][0] + VOW[v][0]

def sound(r):
    if r == "s":
        return "just ‘s’, as in “sun” — a hiss with no vowel. It joins onto the next syllable: Ꮝ + Ꭺ = ‘sgo’."
    if r == "nah":
        return "‘nah’ — an old sign for a ‘na’ sound; today people usually write Ꮎ instead."
    c, v = split(r)
    if not c:
        return f"{VOW[v][1]}."
    return f"{CONS[c][1]} + {VOW[v][1]} → <b>{say(r)}</b>"

def phon(r):
    name, row = ROW_OF[r]
    fs = 19 if len(row) <= 7 else 16
    cells = "".join(
        f'<div style="text-align:center;padding:1px 3px;{"border:2.5px solid #111;border-radius:8px;" if s == r else ""}">'
        f'<div class="nt" style="font-size:{fs}pt;line-height:1.3">{SYL[s]}</div><div class="small" style="line-height:1">{s}</div></div>'
        for s in row)
    return (f'<div style="display:flex;gap:2px;justify-content:center;margin-top:3px">{cells}</div>'
            f'<div class="small" style="margin-top:5px">The box shows this sign in <b>{name}</b> of the syllabary chart.</div>')

PH = "Its row in the syllabary"
PRACTICE = ("<b>Sound-practice page.</b> We did not want to guess a Cherokee word for this sign, so there is none yet. "
            "Ask a Cherokee speaker for a word with this sound!")

def S(r, kind, word=None, tr=None, meaning=None, pic=None, args=None, note=None):
    """kind: 'W' word starts with the sign · 'I' sign sits inside the word · 'P' sound practice."""
    ch = SYL[r]
    if kind == "P":
        word, tr, meaning, pic, args = ch, say(r), "sound practice — say it three times", "chr_slate", dict(text=ch)
        note = note or PRACTICE
    else:
        w = cw(word)
        tr = tr or "-".join(say(s) for s in word.split("-"))
        if kind == "I":
            hl = "-".join(f"<b>{s}</b>" if s == r else s for s in word.split("-"))
            note = note or f"Words starting with {ch} are rare, so find {ch} <b>inside</b> {w} ({hl})."
        if pic is None:
            pic, args = "chr_slate", dict(text=w)
        word = w
    return letter(ch, ch, r, sound(r), word, tr, meaning, pic, phon(r), PH, args, note)

V = [S("a", "W", "a-da", meaning="wood, a stick", pic="chr_wood"),
     S("e", "W", "e-lo-hi", meaning="earth, the world", pic="globe"),
     S("i", "W", "i-ga", meaning="day, daytime", pic="sun"),
     S("o", "W", "o-da-li", meaning="mountain", pic="mountain"),
     S("u", "W", "u-nv-tsi", meaning="snow", pic="chr_snow"),
     S("v", "W", "v-v", meaning="yes!", note="Very few words start with Ꭵ. The best known is ᎥᎥ “yes”; ᎥᏝ means “no”.")]

GHL = [S("ga", "W", "ga-du", meaning="bread", pic="roti"),
       S("ka", "W", "ka-ne-s-ga", "kah-nehs-gah", "grass, hay", "chr_grass"),
       S("ge", "I", "da-lo-ni-ge", meaning="yellow — color the lemon yellow!", pic="lemon",
         note="Ꭸ (ge) is the last sound of many colour words: ᏓᎶᏂᎨ yellow, ᎩᎦᎨ red, ᎬᎾᎨ black."),
       S("gi", "W", "gi-ga-ge", meaning="red — color the tomato red!", pic="tomato"),
       S("go", "W", "go-we-li", meaning="paper, a book, a letter", pic="book", args=dict(left="Ꭰ Ꭱ Ꭲ", right="Ꭶ Ꭷ Ꭸ")),
       S("gu", "W", "gu-le", meaning="acorn", pic="chr_acorn"),
       S("gv", "W", "gv-na-ge", meaning="black — color the pot black!", pic="pot"),
       S("ha", "W", "ha-ni", meaning="here"),
       S("he", "P"),
       S("hi", "W", "hi-s-gi", "hees-gee", "five — count 5 pebbles", "chr_count", dict(n=5)),
       S("ho", "P"), S("hu", "P"), S("hv", "P"),
       S("la", "I", "u-ne-s-da-la", "oo-nehs-dah-lah", "ice", "ice"),
       S("le", "I", "gu-le", meaning="acorn", pic="chr_acorn"),
       S("li", "I", "o-da-li", meaning="mountain", pic="mountain"),
       S("lo", "I", "ga-s-gi-lo", "gahs-gee-loh", "table, chair", "stool"),
       S("lu", "I", "se-lu", meaning="corn", pic="corn"),
       S("lv", "I", "a-tsi-lv", meaning="fire", pic="chr_fire")]

MNQ = [S("ma", "I", "a-ma", meaning="water", pic="water"),
       S("me", "P"), S("mi", "P"), S("mo", "P"), S("mu", "P"),
       S("na", "I", "nu-na", meaning="potato", pic="potato"),
       S("hna", "P"),
       S("nah", "P", note="Ꮐ is an old sign that is almost never used today. " + PRACTICE),
       S("ne", "I", "u-ne-ga", meaning="white — like the clouds", pic="clouds"),
       S("ni", "I", "e-quo-ni", meaning="river", pic="waves"),
       S("no", "W", "no-qui-si", meaning="star", pic="star"),
       S("nu", "W", "nu-na", meaning="potato", pic="potato"),
       S("nv", "W", "nv-ya", meaning="rock, stone", pic="chr_rock"),
       S("qua", "I", "da-qua-le-lu", meaning="wagon", pic="cart"),
       S("que", "P"),
       S("qui", "I", "no-qui-si", meaning="star", pic="star"),
       S("quo", "I", "e-quo-ni", meaning="river", pic="waves"),
       S("quu", "I", "sa-quu", meaning="one", pic="chr_count", args=dict(n=1)),
       S("quv", "P")]

SDT = [S("sa", "W", "sa-quu", meaning="one — count 1 pebble", pic="chr_count", args=dict(n=1)),
       S("s", "W", "s-go-hi", "sgoh-hee", "ten — count 10 pebbles", "chr_count", dict(n=10)),
       S("se", "W", "se-lu", meaning="corn", pic="corn"),
       S("si", "W", "si-nv-da", meaning="moon, month", pic="moon"),
       S("so", "W", "so-ne-la", meaning="nine — count 9 pebbles", pic="chr_count", args=dict(n=9)),
       S("su", "W", "su-da-li", meaning="six — count 6 pebbles", pic="chr_count", args=dict(n=6)),
       S("sv", "W", "sv-ga-ta", meaning="apple", pic="apple"),
       S("da", "W", "da-qua-le-lu", meaning="wagon", pic="cart"),
       S("ta", "W", "ta-li", meaning="two — count 2 pebbles", pic="chr_count", args=dict(n=2)),
       S("de", "I", "a-de-la", meaning="money, coins", pic="chr_coins"),
       S("te", "P"),
       S("di", "I", "ga-lv-la-di", meaning="sky, up above", pic="rainbow"),
       S("ti", "I", "nv-wo-ti", meaning="medicine", pic="medicine"),
       S("do", "W", "do-hi", meaning="peace, calm"),
       S("du", "W", "du-ya", meaning="beans", pic="chr_beans"),
       S("dv", "P")]

TJWY = [S("dla", "P"),
        S("tla", "W", "tla", meaning="no!", note="Ꮭ on its own is a whole word: “no”. Ꮭ also starts many “not” words."),
        S("tle", "P"), S("tli", "P"), S("tlo", "P"), S("tlu", "P"),
        S("tlv", "W", "tlv-gv", "tluhn-guhn", "tree", "tree"),
        S("tsa", "W", "tsa-la-gi", meaning="Cherokee — the people and their language"),
        S("tse", "P"),
        S("tsi", "W", "tsi-yu", meaning="boat, canoe", pic="boat"),
        S("tso", "W", "tso-i", meaning="three — count 3 pebbles", pic="chr_count", args=dict(n=3)),
        S("tsu", "W", "tsu-ne-la", meaning="eight — count 8 pebbles", pic="chr_count", args=dict(n=8)),
        S("tsv", "P"),
        S("wa", "W", "wa-do", meaning="thank you!", pic="gift"),
        S("we", "I", "go-we-li", meaning="paper, a book, a letter", pic="book", args=dict(left="Ꮹ Ꮺ Ꮻ", right="Ꮼ Ꮽ Ꮾ")),
        S("wi", "P"),
        S("wo", "I", "nv-wo-ti", meaning="medicine", pic="medicine"),
        S("wu", "P"), S("wv", "P"),
        S("ya", "I", "du-ya", meaning="beans", pic="chr_beans"),
        S("ye", "P"), S("yi", "P"),
        S("yo", "I", "o-si-yo", meaning="hello!", pic="sunrise"),
        S("yu", "I", "tsi-yu", meaning="boat, canoe", pic="boat"),
        S("yv", "I", "a-yv", meaning="I, me")]

assert [d["name_en"] for d in V + GHL + MNQ + SDT + TJWY] == ROMAN

def sec(items, title, rows, cols, warm, intro):
    nat = " ".join(SYL[r.split()[0]] for r in rows)
    return section(items, label="SIGN", chip="THE SYLLABARY", title=title, native=nat,
                   native_tr=" · ".join(r.split()[0] for r in rows), intro_html=intro,
                   chart_title=title.lower(), chart_cols=cols, warmup_title=title.lower(), warmup_cols=warm)

def rowtable(rows):
    out = ""
    for r in rows:
        out += ('<div style="display:flex;gap:0.08in;margin:0.04in 0">'
                + "".join(f'<div class="box" style="text-align:center;padding:2px 6px;min-width:0.62in"><div class="ntd" style="font-size:22pt;line-height:1.3">{SYL[s]}</div>'
                          f'<div class="small tr">{s}</div></div>' for s in r.split()) + "</div>")
    return out

SECTIONS = [
    sec(V, "The Vowels", ["a"], 6, 6, f"""<p>The Cherokee syllabary begins with <b>six vowels</b>. Five are like English vowels; the sixth, <b>Ꭵ (v)</b>,
is a humming “uh” sound said through the nose.</p>{rowtable(["a e i o u v"])}
<div class="box" style="margin:0.15in 0"><h3>One sign, one syllable</h3>Most signs in the syllabary are a whole syllable: a consonant <i>and</i>
a vowel together, like <b>Ꭶ ga</b> or <b>Ꮜ sa</b>. Only six signs are vowels on their own — these six!</div>
<div class="box"><h3>They look a bit like English letters…</h3>…but they are not! <b>Ꭰ</b> looks like D but says <i>a</i>;
<b>Ꭱ</b> looks like R but says <i>e</i>; <b>Ꭲ</b> looks like T but says <i>i</i>. Say the Cherokee sound, not the English letter.</div>"""),
    sec(GHL, "G, K, H and L", ["ga", "ha", "la"], 10, 5, f"""<p>Now the syllables begin! Each row of the chart keeps one consonant and runs through the vowels
<b>a e i o u v</b>.</p>{rowtable(["ga ka ge gi go gu gv", "ha he hi ho hu hv", "la le li lo lu lv"])}
<div class="box" style="margin-top:0.15in"><h3>Two signs for ‘ga’ and ‘ka’</h3>The G row has one extra sign: <b>Ꭶ ga</b> and <b>Ꭷ ka</b>.
For the other vowels, G and K share one sign (Ꭸ can sound like <i>ge</i> or <i>ke</i>).</div>"""),
    sec(MNQ, "M, N and GW", ["ma", "na", "qua"], 10, 5, f"""<p>Three more rows: <b>M</b>, <b>N</b> and <b>GW</b> (written <i>qu</i> in
English letters).</p>{rowtable(["ma me mi mo mu", "na hna nah ne ni no nu nv", "qua que qui quo quu quv"])}
<div class="box" style="margin-top:0.15in"><h3>Special signs</h3>The N row has <b>Ꮏ hna</b> (a breathy n) and <b>Ꮐ nah</b>,
an old sign that is hardly ever used now. The M row has only five signs in Sequoyah’s chart.</div>"""),
    sec(SDT, "S, D and T", ["sa", "da"], 10, 4, f"""<p>The <b>S</b> row and the <b>D / T</b> row.</p>{rowtable(["sa s se si so su sv", "da ta de te di ti do du dv"])}
<div class="box" style="margin-top:0.15in"><h3>The hissing sign</h3><b>Ꮝ</b> is just the sound <b>s</b>, with no vowel. It joins the next
syllable: <b>Ꮝ + Ꭺ</b> = <i>sgo</i>, as in ᏍᎪᎯ (ten).</div>
<div class="box" style="margin-top:0.1in"><h3>D and T</h3>Some syllables have two signs: <b>Ꮣ da</b> and <b>Ꮤ ta</b>, <b>Ꮥ de</b> and <b>Ꮦ te</b>, <b>Ꮧ di</b> and <b>Ꮨ ti</b>.</div>"""),
    sec(TJWY, "TL, J, W and Y", ["dla", "tsa", "wa", "ya"], 10, 5, f"""<p>The last four rows. <b>Well done — you are nearly at the end of the chart!</b></p>
{rowtable(["dla tla tle tli tlo tlu tlv", "tsa tse tsi tso tsu tsv", "wa we wi wo wu wv", "ya ye yi yo yu yv"])}
<div class="box" style="margin-top:0.12in"><h3>TL and J</h3><b>tl</b> is a ‘t’ that slides into ‘l’. The <b>ts</b> row is said like
‘j’ in many homes: <b>ᏣᎳᎩ</b> (Cherokee) sounds like <i>jah-lah-gee</i>.</div>"""),
]

SECTIONS[0].update(native=" ".join(SYL[v] for v in "aeiouv"), native_tr="a · e · i · o · u · v")

LANG = build(dict(
    code="chr", folder="book-54-cherokee", series_no=54, isbn="", draft=True,
    name="Cherokee", native="ᏣᎳᎩ", native_tr="jah-lah-gee (tsalagi)", name_word="ᏚᏙᎥ", write_word="ᎪᏪᎳ",
    title_native="ᏣᎳᎩ ᏗᎪᏪᎵ", title_letters="ᏣᎳᎩ", belongs_native="ᎯᎠ ᎪᏪᎵ …",
    belongs_pic="star", alphabet_native="ᏣᎳᎩ ᏗᎪᏪᎵ", numbers_native=cw("di-se-s-di"), numbers_tr="dee-sehs-dee",
    phrases_native="ᎣᏏᏲ!",
    letters_word="Syllables",
    subtitle="A Coloring Book to Learn, Trace & Say all 85 Signs of the Cherokee Syllabary with English Phonetics",
    fonts=fontset("Noto Sans Cherokee", "noto-sans-cherokee-cherokee", "Noto Sans Cherokee", "noto-sans-cherokee-cherokee"),
    disp_family="Noto Sans Cherokee", text_family="Noto Sans Cherokee",
    glyph_font=["noto-sans-cherokee-cherokee-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Cherokee and Baloo 2",
    phon_feature="each sign shown in its row of Sequoyah’s syllabary chart",
    sections=SECTIONS,
    chart_note="Read the chart row by row: each row keeps one consonant and runs through a, e, i, o, u, v — the same order as in this book.",
    sound_notes=[
        "Cherokee vowels: <b>a</b> = ‘ah’, <b>e</b> = ‘eh’, <b>i</b> = ‘ee’, <b>o</b> = ‘oh’, <b>u</b> = ‘oo’, and <b>v</b> = ‘uh’ through the nose (we write it <b>uhn</b>).",
        "Syllables are joined with hyphens: <i>ah-dah</i> means say “ah” then “dah”.",
        "<b>j</b> in the guide is the Cherokee <i>ts</i> sound (many speakers say it like ‘j’ in “jam”); <b>gw</b> is the <i>qu</i> sound.",
        "Cherokee also uses <b>pitch</b> (high and low tones) and long and short vowels, which this simple guide does not show — listen to a speaker!"],
    phon_explain="The box marked <i>Its row in the syllabary</i> shows the whole row of Sequoyah’s chart that the sign belongs to, "
                 "with the sign itself in a frame, so children learn the chart a row at a time.",
    standard="the Oklahoma (Cherokee Nation) way of speaking",
    hello=[
        ("Who speaks it?", "About <b>2,000 people</b> speak Cherokee as their first language, and thousands of children and adults "
                           "are learning it in schools and classes.<sup>³</sup>"),
        ("Where?", "In the <b>United States</b>: mostly in <b>Oklahoma</b> and in the mountains of <b>North Carolina</b>."),
        ("How is it written?", "In the <b>Cherokee syllabary</b>, from <b>left to right</b>. Each sign stands for a whole syllable, like "
                               "<span class=\"nt\">Ꭶ</span> <i>ga</i> or <span class=\"nt\">Ꮜ</span> <i>sa</i>."),
        ("How many signs?", "<b>85 signs</b>: 6 vowels and 79 syllables, set out in a chart of rows."),
        ("Who made it?", "A Cherokee man named <b>Sequoyah</b> created the syllabary around <b>1821</b>. Within a few years, many "
                         "Cherokee people could read and write it!"),
        ("Did you know?", "Some signs look like English letters but say other sounds: <span class=\"nt\">Ꮃ</span> looks like W but says "
                          "<i>la</i>, and <span class=\"nt\">Ꮪ</span> looks like S but says <i>du</i>."),
    ],
    hello_pics=[("corn", {}), ("mountain", {}), ("tree", {})],
    map=region_map(frame=[[-100.0, 24.0], [-70.0, 44.0]],
                   points=dict(tahlequah=[-94.97, 35.92], cherokeenc=[-83.31, 35.48]),
                   area=None,
                   cities=[("tahlequah", "Tahlequah", 0, -18, "middle", False), ("cherokeenc", "Cherokee", 0, -18, "middle", False)],
                   label="NORTH AMERICA", label_at=[-88.0, 41.0], marker=[-88.0, 36.0],
                   caption="The circle shows the south-east of North America.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Cherokee is spoken around "
                          "<b>Tahlequah</b> in Oklahoma and around the town of <b>Cherokee</b> in the mountains of North Carolina.",
                   seas=[("Gulf of Mexico", -90.0, 26.5), ("Atlantic Ocean", -75.0, 30.5)]),
    digits=[("0", cw("tla") + " " + cw("go-s-di"), "tlah gohs-dee", "zero (“nothing”)"), ("1", cw("sa-quu"), "sah-gwoo", "one"),
            ("2", cw("ta-li"), "tah-lee", "two"), ("3", cw("tso-i"), "joh-ee", "three"), ("4", cw("nv-gi"), "nuhn-gee", "four"),
            ("5", cw("hi-s-gi"), "hees-gee", "five"), ("6", cw("su-da-li"), "soo-dah-lee", "six"),
            ("7", cw("ga-li-quo-gi"), "gah-lee-gwoh-gee", "seven"), ("8", cw("tsu-ne-la"), "joo-neh-lah", "eight"),
            ("9", cw("so-ne-la"), "soh-neh-lah", "nine")],
    phrases=[(cw("a-s-sa-la-mu a-le-gu-mu"), "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting, written in Cherokee signs)"),
             (cw("wa a-le-gu-mu a-s-sa-la-mu"), "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             (cw("o-si-yo") + "!", "oh-see-yoh", "Hello!"),
             (cw("da-qua-do-v") + " …", "dah-gwah-doh-uhn …", "My name is …"),
             (cw("wa-do"), "wah-doh", "Thank you"),
             (cw("tsa-sa-ga-la-hu ga-i-la-na"), "jah-zah-KAH-lah-hoo KHAI-rahn", "Jazakallahu khairan — May Allah reward you with good"),
             (cw("e-tsi") + " · " + cw("e-do-da"), "eh-jee · eh-doh-dah", "Mother · Father"),
             (cw("a-gi-nv-tli") + " · " + cw("a-gi-do"), "ah-gee-nuhn-tlee · ah-gee-doh", "My brother · My sister (said by a boy)"),
             (cw("v-v") + " · " + cw("v-tla"), "uhn-uhn · uhn-tlah", "Yes · No"),
             (cw("tsa-la-gi a-de-lo-qua-s-gv") + "!", "jah-lah-gee ah-deh-loh-gwahs-guhn", "I am learning Cherokee!")],
    cheer=(cw("ma-sa-la") + "! " + cw("o-s-da") + "!", "MAH-shah-lah! ohs-dah!", "Mashallah! Good — well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the <b>Cherokee Nation</b> Language Department; "
                 "history of the syllabary from the <b>Cherokee Nation</b>.",
    book_pic=dict(left="Ꭰ Ꭱ Ꭲ", right="Ꭳ Ꭴ Ꭵ"),
    review_note=("Drafted without a Cherokee speaker; please check every word. 26 signs have <b>sound-practice pages</b> with no word "
                 "(he ho hu hv me mi mo mu hna nah que quv te dv dla tle tli tlo tlu tse tsv wi wu wv ye yi): a speaker could add "
                 "simple object/plant/nature words for these. Many other signs use a word in which the sign sits inside "
                 "(e.g. ᎠᏥᎸ for lv) — check these, and the less certain words ᏓᏆᎴᎷ (wagon), ᎤᏁᏍᏓᎳ (ice), ᏏᏅᏓ (month/moon), "
                 "ᎦᏍᎩᎶ (table/chair), ᎫᎴ (acorn), ᏚᏯ (beans; also seen as ᏙᏯ), ᎧᏁᏍᎦ (grass). Check the phrases: ᏓᏆᏙᎥ (my name is), "
                 "ᎠᎩᏅᏟ / ᎠᎩᏙ (kinship words depend on who is speaking), ᏣᎳᎩ ᎠᏕᎶᏆᏍᎬ, the zero word Ꮭ ᎪᏍᏗ, the native labels "
                 "ᏚᏙᎥ (name), ᎪᏪᎳ (write), ᏗᏎᏍᏗ (numbers), ᏣᎳᎩ ᏗᎪᏪᎵ (Cherokee writing) and ᎯᎠ ᎪᏪᎵ (this book). The Arabic phrases "
                 "(Assalamu alaikum, Jazakallahu khairan, Mashallah) are sound-spellings in Cherokee signs, which have no r, kh "
                 "or final consonants — a Cherokee-speaking Muslim should approve them. Sound guides follow Oklahoma speech "
                 "and ignore tone."),
    tiles="ᏣᎳᎩᎠᏎᏩ", cover_pics=["corn", "apple", "tree", "mountain"], title_size=48,
    speakers_blurb="Cherokee is the language of the Cherokee people of Oklahoma and North Carolina, written in the famous syllabary created by Sequoyah.",
    sample_words=[(cw("se-lu"), "seh-loo", "corn"), (cw("o-da-li"), "oh-dah-lee", "mountain"), (cw("sv-ga-ta"), "suhn-gah-tah", "apple")],
    keywords=["cherokee syllabary book for kids", "learn cherokee language children", "cherokee coloring book",
              "sequoyah syllabary tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "native american language for kids"],
))
