# -*- coding: utf-8 -*-
"""Book 55 - Inuktitut in Canadian Aboriginal syllabics (qaniujaaqpait), Nunavut/Baffin usage.
Allamahul Bayan Series. REVIEW DRAFT.

The book teaches the grid as Inuit children learn it: 3 vowels (i, u, a) and 13 consonant rows, each
row turning one shape to point up (i), right (u) and left (a): 3 + 13 x 3 = 42 syllables, one page each.
Finals, long-vowel dots, the ai column and the extra rows (nng, h, ł) are explained in the intros."""
import unicodedata
from generic import build, letter, section, fontset
from maps import region_map

VOW = ["i", "u", "a"]
ROWS = [  # consonant, (i, u, a, final), English sound guide for the consonant
    ("", "ᐃᐅᐊ", ""),
    ("p", "ᐱᐳᐸᑉ", "‘p’ as in “pen”"), ("t", "ᑎᑐᑕᑦ", "‘t’ as in “top”"), ("k", "ᑭᑯᑲᒃ", "‘k’ as in “kite”"),
    ("g", "ᒋᒍᒐᒡ", "a soft, breathy ‘g’"), ("m", "ᒥᒧᒪᒻ", "‘m’ as in “moon”"),
    ("n", "ᓂᓄᓇᓐ", "‘n’ as in “net”"), ("s", "ᓯᓱᓴᔅ", "‘s’ as in “sun”"), ("l", "ᓕᓗᓚᓪ", "‘l’ as in “lamp”"),
    ("j", "ᔨᔪᔭᔾ", "‘y’ as in “yes” (written j)"), ("v", "ᕕᕗᕙᕝ", "‘v’ as in “van”"),
    ("r", "ᕆᕈᕋᕐ", "a gargled ‘r’ from the throat, like French ‘r’"),
    ("q", "ᕿᖁᖃᖅ", "a ‘k’ said far back in the throat, like Arabic ق"), ("ng", "ᖏᖑᖓᖕ", "‘ng’ as in “sing”"),
]
VSND = dict(i="‘i’ as in “sit”", u="‘u’ as in “put”", a="‘a’ as in “father”, but short")


def long_form(ch):
    try:
        n = unicodedata.name(ch)
        return unicodedata.lookup(n + n[-1])
    except (KeyError, ValueError):
        return None


def phon(row, k):
    cons, chars, _ = row
    cells = []
    for j in range(3):
        on = j == k
        st = ("border:2.5px solid #111;border-radius:8px;background:#eee;padding:0 6px" if on else "padding:0 6px")
        cells.append(f'<span style="{st}">{chars[j]}</span>')
    fin = (f' &nbsp;<span style="font-size:16pt;color:#444">{chars[3]}</span>') if len(chars) > 3 else ""
    lf = long_form(chars[k])
    tr = (cons + VOW[k])
    bits = []
    if len(chars) > 3:
        bits.append(f'final <span class="nt" style="font-size:14pt">{chars[3]}</span> = <i>{cons}</i>')
    if lf:
        bits.append(f'long <span class="nt" style="font-size:14pt">{lf}</span> = <i>{tr}{VOW[k]}</i>')
    how = f"<i>{cons}</i> + <i>{VOW[k]}</i>" if cons else f"the vowel <i>{VOW[k]}</i>"
    return (f'<div class="nt" style="font-size:24pt;line-height:1.45">{" ".join(cells)}{fin}</div>'
            f'<div class="small">{how}: the shape points {["up", "right", "left"][k]}</div>'
            f'<div class="small">{" · ".join(bits)}</div>')


def S(ch, word, tr, meaning, pic, args=None, note=None):
    for row in ROWS:
        if ch in row[1][:3]:
            k = row[1].index(ch)
            cons = row[0]
            sound = (f"{row[2]}, then {VSND[VOW[k]]}" if cons else VSND[VOW[k]])
            return letter(ch, ch, cons + VOW[k], sound, word, tr, meaning, pic, phon(row, k),
                          "Syllabics row · how it turns", args, note)
    raise KeyError(ch)


def inside(ch, word=None):
    return f'Find <span class="nt">{ch}</span> inside the word!'


def never(row, ch, few=False):
    return (f'{"Few" if few else "No"} Inuktitut words start with <span class="nt">{row}</span>. ' + inside(ch))


VOWELS = [
    S("ᐃ", "ᐃᒡᓗ", "iglu", "house", "house", note="English “igloo” comes from this word!"),
    S("ᐅ", "ᐅᒃᑯᓯᒃ", "ukkusik", "cooking pot", "pot"),
    S("ᐊ", "ᐊᐳᑦ", "aput", "snow (lying on the ground)", "iu_snow"),
]
SYLL = [
    S("ᐱ", "ᐱᖃᓗᔭᖅ", "piqalujaq", "iceberg", "iu_iceberg"),
    S("ᐳ", "ᐳᐊᓗᒃ", "pualuk", "mitten", "iu_mitten"),
    S("ᐸ", "ᐸᓚᐅᒑᖅ", "palaugaaq", "bannock (pan bread)", "roti"),
    S("ᑎ", "ᑎᖕᒥᓲᖅ", "tingmisuuq", "airplane — “the one that flies”", "plane"),
    S("ᑐ", "ᑐᐱᖅ", "tupiq", "tent", "iu_tent"),
    S("ᑕ", "ᑕᖅᑭᖅ", "taqqiq", "moon", "moon"),
    S("ᑭ", "ᑭᑭᐊᖅ", "kikiaq", "nail", "iu_nail"),
    S("ᑯ", "ᑰᒃ", "kuuk", "river", "iu_river", note="The dot on <span class='nt'>ᑰ</span> makes the vowel long: <i>kuu</i>."),
    S("ᑲ", "ᑲᒥᒃ", "kamik", "boot (a warm skin boot)", "iu_kamik"),
    S("ᒋ", "ᐊᑎᒋ", "atigi", "parka (an inner coat)", "iu_parka", note=never("ᒋ ᒍ ᒐ", "ᒋ", few=True)),
    S("ᒍ", "ᓂᕆᒍᒪᔪᖓ", "nirigumajunga", "I want to eat!", "plate",
      note="Few words start with <span class='nt'>ᒍ</span>; it lives in endings like <i>-guma-</i> “want to”."),
    S("ᒐ", "ᐃᒐᓛᖅ", "igalaaq", "window", "window", note=never("ᒋ ᒍ ᒐ", "ᒐ", few=True)),
    S("ᒥ", "ᐅᒥᐊᖅ", "umiaq", "boat", "boat", note=inside("ᒥ")),
    S("ᒧ", "ᖃᒧᑎᒃ", "qamutik", "sled", "iu_sled", note=inside("ᒧ")),
    S("ᒪ", "ᒪᓐᓂᒃ", "mannik", "egg", "egg"),
    S("ᓂ", "ᓂᓚᒃ", "nilak", "fresh-water ice (melted for drinking)", "ice"),
    S("ᓄ", "ᓄᕗᔭᖅ", "nuvujaq", "cloud", "clouds"),
    S("ᓇ", "ᓇᓴᖅ", "nasaq", "hat", "iu_hat"),
    S("ᓯ", "ᓯᕿᓂᖅ", "siqiniq", "sun", "sun"),
    S("ᓱ", "ᓱᓗᒃ", "suluk", "feather", "feather"),
    S("ᓴ", "ᓴᕕᒃ", "savik", "knife (also the word for metal)", "iu_knife"),
    S("ᓕ", "ᐃᓕᓐᓂᐊᕐᕕᒃ", "ilinniarvik", "school — “the place for learning”", "book",
      args=dict(left="ᐃ ᐅ ᐊ", right="ᐱ ᐳ ᐸ"), note=never("ᓕ ᓗ ᓚ", "ᓕ")),
    S("ᓗ", "ᐅᓪᓗᕆᐊᖅ", "ulluriaq", "star", "star", note=never("ᓕ ᓗ ᓚ", "ᓗ")),
    S("ᓚ", "ᕿᓚᒃ", "qilak", "sky", "rainbow", note=never("ᓕ ᓗ ᓚ", "ᓚ")),
    S("ᔨ", "ᐊᔾᔨᙳᐊᖅ", "ajjinnguaq", "picture, photo", "iu_picture", note=never("ᔨ ᔪ ᔭ", "ᔨ", few=True)),
    S("ᔪ", "ᐅᒥᐊᕐᔪᐊᖅ", "umiarjuaq", "ship — “big boat”", "ship", note=never("ᔨ ᔪ ᔭ", "ᔪ", few=True)),
    S("ᔭ", "ᐅᔭᕋᒃ", "ujarak", "stone, rock", "iu_stone", note=never("ᔨ ᔪ ᔭ", "ᔭ", few=True)),
    S("ᕕ", "ᐃᒡᓗᕕᒐᖅ", "igluvigaq", "snow house", "iu_igloo", note=inside("ᕕ")),
    S("ᕗ", "ᓄᓇᕗᑦ", "Nunavut", "Nunavut — “our land”", "mountain", note=inside("ᕗ")),
    S("ᕙ", "ᐃᕙᓗ", "ivalu", "sewing thread (made from sinew)", "wool", note=inside("ᕙ")),
    S("ᕆ", "ᑕᕆᐅᖅ", "tariuq", "the sea, salt water", "waves", note=never("ᕆ ᕈ ᕋ", "ᕆ")),
    S("ᕈ", "ᐱᕈᖅᓯᐊᖅ", "piruqsiaq", "plant, flower — “something that grows”", "flower", note=never("ᕆ ᕈ ᕋ", "ᕈ")),
    S("ᕋ", "ᑎᑎᕋᐅᑦ", "titiraut", "pencil — “something to write with”", "pen", note=never("ᕆ ᕈ ᕋ", "ᕋ")),
    S("ᕿ", "ᕿᑭᖅᑕᖅ", "qikiqtaq", "island", "iu_island"),
    S("ᖁ", "ᖁᓪᓕᖅ", "qulliq", "stone oil lamp", "iu_qulliq"),
    S("ᖃ", "ᖃᔭᖅ", "qajaq", "kayak", "iu_kayak", note="English “kayak” comes from this word!"),
    S("ᖏ", "ᑲᖏᖅᓱᒃ", "kangiqsuk", "bay (sea reaching into the land)", "iu_bay", note=never("ᖏ ᖑ ᖓ", "ᖏ")),
    S("ᖑ", "ᑐᖑᔪᖅᑐᖅ", "tungujuqtuq", "it is blue — color the sea and sky blue!", "iu_blue",
      note=never("ᖏ ᖑ ᖓ", "ᖑ")),
    S("ᖓ", "ᐱᖓᓱᑦ", "pingasut", "three", "iu_three", note=never("ᖏ ᖑ ᖓ", "ᖓ")),
]

GRID = "".join(f'<tr><td style="font:600 12pt Nunito;padding:0 8px">{r[0] or "—"}</td>'
               + "".join(f'<td class="nt" style="font-size:19pt;padding:0 10px">{c}</td>' for c in r[1][:3])
               + f'<td class="nt" style="font-size:13pt;color:#555;padding:0 8px">{r[1][3] if len(r[1]) > 3 else ""}</td></tr>'
               for r in ROWS)

FONTS = fontset("Noto Sans Canadian Aboriginal", "noto-sans-canadian-aboriginal-canadian-aboriginal",
                "Noto Sans Canadian Aboriginal", "noto-sans-canadian-aboriginal-canadian-aboriginal")

LANG = build(dict(
    code="iu", folder="book-55-inuktitut", series_no=55, isbn="", draft=True,
    name="Inuktitut", native="ᐃᓄᒃᑎᑐᑦ", native_tr="i-NUK-ti-tut — “like the Inuit”", name_word="ᐊᑎᖓ",
    write_word="ᑎᑎᕋᕐᓂᖅ", letters_word="Syllables",
    title="My First Inuktitut Syllabics",
    subtitle="A Coloring Book to Learn, Trace & Say the 42 Inuktitut Syllables with English Phonetics",
    cover_title_html="My First Inuktitut<br>Syllabics", title_size=42,
    title_native="ᐃᓄᒃᑎᑐᑦ ᖃᓂᐅᔮᖅᐸᐃᑦ", title_letters="ᐃᐅᐊᐱᐳᐸ", belongs_native="ᐅᖃᓕᒫᒐᕋ", belongs_pic="star",
    alphabet_native="ᖃᓂᐅᔮᖅᐸᐃᑦ", numbers_native="ᓈᓴᐅᑏᑦ", numbers_tr="naasautiit", phrases_native="ᐅᖃᐅᓯᑦ",
    fonts=FONTS, disp_family="Noto Sans Canadian Aboriginal", text_family="Noto Sans Canadian Aboriginal",
    glyph_font=["noto-sans-canadian-aboriginal-canadian-aboriginal-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Canadian Aboriginal, Baloo 2",
    extra_css=".lp-name{font-size:26pt}",
    phon_feature="the whole syllabics row of every syllable (ᐱ ᐳ ᐸ: pi pu pa), its final and its long form",
    sections=[
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels", native="ᐃ ᐅ ᐊ", native_tr="i · u · a",
                chart_title="vowels", chart_cols=3, warmup_title="the vowels", warmup_cols=3,
                intro_html="""<p>Inuktitut has just <b>three vowels</b>: <i>i, u, a</i>. Each one is the same little shape, turned to
point a different way:</p>
<div class="box" style="margin:0.1in 0;text-align:center"><div class="nt" style="font-size:44pt;line-height:1.4">ᐃ &nbsp; ᐅ &nbsp; ᐊ</div>
<b>i</b> points up · <b>u</b> points right · <b>a</b> points left</div>
<div class="box" style="margin:0.1in 0"><h3>Turn it, and the vowel changes</h3>Every consonant shape works the same way. Learn the three
directions and you can read a whole row: <span class="nt" style="font-size:18pt">ᐱ ᐳ ᐸ</span> <i>pi, pu, pa</i>.</div>
<div class="box"><h3>Long vowels get a dot</h3>A dot on top makes the vowel long: <span class="nt" style="font-size:18pt">ᐃ → ᐄ</span>
<i>i → ii</i>. Some regions (Nunavik) write two vowels instead: <span class="nt" style="font-size:18pt">ᐃᐃ</span>.</div>"""),
        section(SYLL, label="SYLLABLE", chip="THE SYLLABLES", title="The Syllables", native="ᖃᓂᐅᔮᖅᐸᐃᑦ",
                native_tr="qaniujaaqpait — “syllabics”", chart_title="syllables", chart_cols=6,
                warmup_title="the syllables", warmup_cols=6,
                intro_html=f"""<p>Each consonant has <b>one shape</b>, turned three ways for <i>i, u, a</i>. Its small, raised form is the
<b>final</b>: the consonant alone, with no vowel.</p>
<div style="display:flex;gap:0.2in;align-items:flex-start">
<table style="border-collapse:collapse;border:2px solid #111;border-radius:12px">
<tr><td></td><td style="font:600 11pt Nunito;padding:0 10px">i</td><td style="font:600 11pt Nunito;padding:0 10px">u</td>
<td style="font:600 11pt Nunito;padding:0 10px">a</td><td style="font:600 10pt Nunito">final</td></tr>{GRID}</table>
<div style="flex:1">
<div class="box" style="margin-bottom:0.1in"><h3>Read a word</h3><div class="nt" style="font-size:26pt;line-height:1.5">ᐃ + ᒡ + ᓗ = ᐃᒡᓗ</div>
<i>i + g + lu = iglu</i> (house)</div>
<div class="box" style="margin-bottom:0.1in"><h3>More to discover</h3>Some regions also use an <b>ai</b> column (<span class="nt">ᐁ ᐯ ᑌ</span>), a
<b>nng</b> row (<span class="nt">ᙱ ᙳ ᙵ</span>), <b>h</b> (<span class="nt">ᕼ</span>) and <b>ł</b> (<span class="nt">ᖠ ᖢ ᖤ</span>). This book keeps to the
42 shapes every child learns first.</div>
<div class="box"><h3>Never first</h3>Inuktitut words never start with the <b>l</b>, <b>r</b> and <b>ng</b> rows, and hardly ever with <b>g</b> or <b>j</b>.
On those pages, find the syllable <i>inside</i> the word.</div></div></div>"""),
    ],
    sound_notes=[
        "<b>Three vowels:</b> <i>i</i> as in “sit”, <i>u</i> as in “put”, <i>a</i> as in “father” (short). <b>Doubled vowels are long:</b> "
        "<i>ii, uu, aa</i>.",
        "<b>q</b> is a <i>k</i> said deep in the throat, like Arabic ق. <b>r</b> is a gargled sound from the back of the throat.",
        "<b>j</b> sounds like English <i>y</i> in “yes”. <b>ng</b> is the sound in “sing”. <b>g</b> is soft and breathy.",
        "Double consonants are held a little longer: <i>taqqiq</i>, <i>ukkusik</i>. Inuktitut has no strong stress, so the "
        "transliteration has no capitals."],
    phon_explain="The third box shows the syllable’s <b>whole row</b> (the same shape pointing up, right and left), its small "
                 "<b>final</b> form, and its <b>long</b> form with a dot.",
    standard="the Inuktitut of Nunavut (Baffin Island), written in the standard syllabics of the Inuit Cultural Institute",
    hello=[
        ("Who speaks it?", "About <b>40,000 Inuit</b> speak Inuktitut.<sup>³</sup>"),
        ("Where?", "In <b>Nunavut</b> and <b>Nunavik</b> (the far north of Quebec), in the Arctic of <b>Canada</b> — a land of snow, "
                   "ice, sea and long summer days."),
        ("How is it written?", "In <b>syllabics</b>, <span class='nt'>ᖃᓂᐅᔮᖅᐸᐃᑦ</span>, from <b>left to right</b>. Each shape is a whole "
                               "syllable, like <i>pa</i> or <i>ki</i>."),
        ("How many shapes?", "This book teaches <b>42 syllables</b>: 3 vowels and 13 consonant rows of 3. Small raised “finals” and "
                             "dots for long vowels complete the system."),
        ("Turn it around!", "The same shape points <b>up</b> for <i>i</i>, <b>right</b> for <i>u</i> and <b>left</b> for <i>a</i>: "
                            "<span class='nt' style='font-size:16pt'>ᑎ ᑐ ᑕ</span> <i>ti, tu, ta</i>."),
        ("Did you know?", "English borrowed words from Inuktitut: <b>igloo</b> (<span class='nt'>ᐃᒡᓗ</span> <i>iglu</i>, house) and "
                          "<b>kayak</b> (<span class='nt'>ᖃᔭᖅ</span> <i>qajaq</i>)."),
    ],
    hello_pics=[("iu_igloo", {}), ("iu_kayak", {}), ("iu_qulliq", {})],
    chart_note="Read the syllabics row by row: each row is one consonant with <i>i, u, a</i> — the same order as in this book.",
    map=region_map(frame=[[-100.0, 54.0], [-58.0, 76.0]],
                   points=dict(iqaluit=[-68.52, 63.75], rankin=[-92.08, 62.81], igloolik=[-81.80, 69.38],
                               pond=[-77.96, 72.70], kuujjuaq=[-68.40, 58.10]),
                   area=(-77.0, 65.0, 330, 300),
                   cities=[("iqaluit", "Iqaluit", 14, 8, "start", False), ("rankin", "Rankin Inlet", 14, 22, "start", False),
                           ("igloolik", "Igloolik", -14, 8, "end", False), ("pond", "Pond Inlet", 14, -8, "start", False),
                           ("kuujjuaq", "Kuujjuaq", 14, 8, "start", False)],
                   label="ARCTIC CANADA", label_at=[-90.0, 73.5], marker=[-78.0, 66.0],
                   caption="The circle shows Arctic Canada on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> or <b>white</b> like snow · the sea <b>blue</b>. <b>Find it:</b> Inuktitut is "
                          "spoken in Iqaluit, Igloolik, Pond Inlet and Rankin Inlet in Nunavut, and in Kuujjuaq in Nunavik.",
                   seas=[("Hudson Bay", -86.0, 59.0), ("Baffin Bay", -64.0, 73.5)], world_r=18),
    digits=[("0", "", "(say “zero”)", "zero"), ("1", "ᐊᑕᐅᓯᖅ", "atausiq", "one"), ("2", "ᒪᕐᕉᒃ", "marruuk", "two"),
            ("3", "ᐱᖓᓱᑦ", "pingasut", "three"), ("4", "ᓯᑕᒪᑦ", "sitamat", "four"), ("5", "ᑕᓪᓕᒪᑦ", "tallimat", "five"),
            ("6", "ᐊᕐᕕᓂᓕᒃ", "arvinilik", "six"), ("7", "ᐊᕐᕕᓂᓪᓕᑦ ᒪᕐᕉᒃ", "arvinillit marruuk", "seven"),
            ("8", "ᐊᕐᕕᓂᓪᓕᑦ ᐱᖓᓱᑦ", "arvinillit pingasut", "eight"), ("9", "ᐊᕐᕕᓂᓪᓕᑦ ᓯᑕᒪᑦ", "arvinillit sitamat", "nine")],
    phrases=[("ᐊᔅᓴᓚᒧ ᐊᓚᐃᑯᒻ", "assalamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ᕙ ᐊᓚᐃᑯᒻ ᐊᔅᓴᓚᒻ", "va alaikum assalam", "And upon you be peace (the reply)"),
             ("ᐊᑎᕋ …", "atira …", "My name is …"),
             ("ᖁᔭᓐᓇᒦᒃ", "qujannamiik", "Thank you"),
             ("ᔭᓴᑲᓪᓚᕼᐅ ᑲᐃᕋᓐ", "jazakallahu khairan", "May Allah reward you with good"),
             ("ᐊᓈᓇ · ᐊᑖᑕ", "anaana · ataata", "Mother · Father"),
             ("ᐊᓂᒃ · ᓇᔭᒃ", "anik · najak", "Brother (a girl says) · Sister (a boy says)"),
             ("ᐄ · ᐋᒃᑲ", "ii · aakka", "Yes · No"),
             ("ᐃᓄᒃᑎᑐᑦ ᐃᓕᓐᓂᐊᖅᑐᖓ!", "inuktitut ilinniaqtunga!", "I am learning Inuktitut!")],
    cheer=("ᒫᓵᓪᓛ! ᐱᐅᔪᑦᓯᐊᖅ!", "maasaallaa! piujutsiaq!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the <b>2021 Census of Canada</b> "
                 "(Statistics Canada); syllabics chart of the <b>Inuit Cultural Institute</b> standard.",
    book_pic=dict(left="ᐃ ᐅ ᐊ", right="ᐱ ᐳ ᐸ"),
    review_note=("Check every word with a Nunavut speaker, and especially: the words for the rows that rarely or never start a word "
                 "(atigi, nirigumajunga, igalaaq, ajjinnguaq, tungujuqtuq, kangiqsuk); kikiaq (nail), palaugaaq (bannock), "
                 "piruqsiaq (plant), ivalu (thread), pualuk (mitten); the brother/sister words (anik, najak), which depend on who is "
                 "speaking; the numbers 6–9 (arvinilik system; other regions say pingasuujuqtut etc.); ᑎᑎᕋᕐᓂᖅ, ᐊᑎᖓ, ᐅᖃᓕᒫᒐᕋ and ᐅᖃᐅᓯᑦ "
                 "used as page labels; and the Arabic phrases (Assalamu alaikum, Jazakallahu khairan, Mashallah) spelled in syllabics, "
                 "which have no established Inuktitut spelling."),
    tiles="ᐃᐊᐱᑐᖃᓄ", cover_pics=["iu_igloo", "iu_kayak", "iu_qulliq", "star"],
    speakers_blurb="Inuktitut is spoken by about 40,000 Inuit in Nunavut and Nunavik, in the Arctic of Canada.",
    sample_words=[("ᐃᒡᓗ", "iglu", "house"), ("ᖃᔭᖅ", "qajaq", "kayak"), ("ᓯᕿᓂᖅ", "siqiniq", "sun")],
    keywords=["inuktitut syllabics book for kids", "learn inuktitut for children", "inuit language coloring book",
              "nunavut syllabics tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "arctic canada language gift"],
))
