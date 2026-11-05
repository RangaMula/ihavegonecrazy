# -*- coding: utf-8 -*-
"""Book 77 - Sesotho (Southern Sotho, Latin script, 22 letters). Allamahul Bayan Series. REVIEW DRAFT.
Spelling follows the South African orthography (di-, -we, tjh); Lesotho spells some words differently (li-, -oe, ch)."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Sesotho name · syllables"
VOWELS = ["a", "e", "i", "o", "u"]


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
    small = cap.lower()
    if row is None:
        row = " · ".join(c + small for c in "b d k m".split()) if vowel else " · ".join(small + v for v in VOWELS)
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
            f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + small, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "apole", "ah-POH-leh", "apple", "apple", vowel=True),
    L("B", "ba", "bah", "‘b’ as in “ball” (softer between vowels)", "buka", "BOO-kah", "book", "book",
      args=dict(left="A B D", right="E F G")),
    L("D", "da", "dah", "‘d’ as in “door” — only before i and u", "dipalesa", "dee-pah-LEH-sah", "flowers", "flower",
      rule="di and du: the sound of L changes to D before i and u"),
    L("E", "e", "eh", "‘e’ as in “bed” (or a little closer, as in “day”)", "lehe", "LEH-heh", "egg", "egg", vowel=True,
      note="Very few Sesotho words start with E. Find it twice in <i>lehe</i>!"),
    L("F", "fa", "fah", "‘f’ as in “fan”", "folaga", "foh-LAH-gah", "flag", "flag"),
    L("G", "ga", "gah", "‘g’ as in “go” — mostly in NG, as in “singer”", "lengolo", "leh-NGOH-loh", "letter (to post)", "envelope",
      note="G hardly ever stands alone in Sesotho. Look for <b>ng</b> in <i>le<b>ng</b>olo</i>."),
    L("H", "ha", "hah", "‘h’ as in “hat”", "heke", "HEH-keh", "gate", "st_heke",
      rule="hl = blow air past the sides of your tongue · ph, th, kh = with a puff of air"),
    L("I", "i", "ee", "‘ee’ as in “see”", "pitsa", "PEE-tsah", "cooking pot", "pot", vowel=True,
      note="Very few Sesotho naming words start with I. Find it inside <i>pitsa</i>!"),
    L("J", "ja", "jah", "‘j’ as in “jam”", "jwang", "JWAHNG", "grass", "st_jwang"),
    L("K", "ka", "kah", "‘k’ as in “kite” (no puff of air)", "kopi", "KOH-pee", "cup", "teacup",
      rule="kg = a ‘k’ with a throaty ‘h’: <b>kg</b>wedi (moon)"),
    L("L", "la", "lah", "‘l’ as in “lamp”", "letsatsi", "leh-TSAH-tsee", "sun", "sun",
      rule="ts = ‘ts’ as in “cats” · tl = a ‘t’ and ‘l’ together"),
    L("M", "ma", "mah", "‘m’ as in “moon”; it can be a syllable on its own", "metsi", "MEH-tsee", "water", "water"),
    L("N", "na", "nah", "‘n’ as in “net”", "naledi", "nah-LEH-dee", "star", "star",
      rule="ny = ‘ny’ as in “canyon” · ng = ‘ng’ as in “singer”"),
    L("O", "o", "oh", "‘o’ as in “for” (or closer, as in “go”)", "mokorotlo", "moh-koh-ROH-tloh", "the Basotho grass hat", "st_mokorotlo",
      vowel=True, note="Very few Sesotho words start with O, but you can find it four times in <i>mokorotlo</i>!"),
    L("P", "pa", "pah", "‘p’ as in “spin” (no puff of air)", "pula", "POO-lah", "rain", "raincloud"),
    L("Q", "qa", "(click) ah", "a click! Pop your tongue off the roof of your mouth", "maqhubu", "mah-(click)HOO-boo", "waves", "waves",
      note="Q is a <b>click</b> sound, borrowed from neighbouring languages such as Zulu and Xhosa. Find it inside <i>maqhubu</i>!"),
    L("R", "ra", "rah", "a rolled ‘r’, sometimes from the throat", "raese", "RAH-eh-seh", "rice", "rice"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "sefate", "seh-FAH-teh", "tree", "tree",
      rule="sh = ‘sh’ as in “ship”"),
    L("T", "ta", "tah", "‘t’ as in “stop” (no puff of air)", "tamati", "tah-MAH-tee", "tomato", "tomato",
      rule="th = a ‘t’ with a puff of air · tjh = ‘ch’ with a puff of air"),
    L("U", "u", "oo", "‘oo’ as in “moon”", "mokopu", "moh-KOH-poo", "pumpkin", "st_mokopu", vowel=True,
      note="Very few Sesotho words start with U. Find it at the end of <i>mokopu</i>!"),
    L("W", "wa", "wah", "‘w’ as in “water”", "kgwedi", "KHWEH-dee", "moon", "moon",
      note="W often sits after another letter: <i>kg<b>w</b>edi</i>, <i>j<b>w</b>ang</i>."),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "monyako", "moh-NYAH-koh", "door, doorway", "door",
      note="Y hardly ever starts a Sesotho naming word. Find it in the pair <b>ny</b> of <i>mo<b>ny</b>ako</i>!"),
]

LANG = build(dict(
    code="st", folder="book-77-sesotho", series_no=77, isbn="", draft=True,
    name="Sesotho", native="Sesotho", native_tr="seh-SOO-too", name_word="lebitso", write_word="ngola",
    title_native="Alfabete ya ka ya pele ya Sesotho", title_letters="AaBbDd", belongs_native="Buka ena ke ya",
    belongs_pic="st_mokorotlo", alphabet_native="alfabete", numbers_native="dinomoro", numbers_tr="dee-noh-MOH-roh",
    phrases_native="Mantswe a pele",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Sesotho name and its syllables (ba, be, bi, bo, bu)",
    sections=[section(LETTERS, native="alfabete ya Sesotho", native_tr="ahl-fah-BEH-teh yah seh-SOO-too — “the Sesotho alphabet”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Sesotho is written with <b>22 letters</b>. It has no C, V, X or Z.</p>
<div class="box" style="margin:0.1in 0"><h3>Five written vowels</h3><b>A E I O U</b> say <i>ah, eh, ee, oh, oo</i>. Children learn to read by
singing the syllables: <i>ba be bi bo bu, da de di do du…</i></div>
<div class="box" style="margin:0.1in 0"><h3>Letter friends</h3>Many sounds are written with two or three letters: <b>hl, kg, ng, ny, ph, th, kh,
tl, ts, sh, tj, tjh</b>. And <b>Q</b> is a <b>click</b>!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>POO-lah</i> means “say POO a little louder”. Sesotho is also a tone "
        "language, so listen to a Sesotho speaker for the tune of each word.",
        "<b>(click)</b> marks the Q click: pop your tongue off the roof of your mouth.",
        "<b>kh</b> is a throaty sound, like the Arabic letter خ; <b>hl</b> is air blown past the sides of the tongue.",
        "<b>m-</b> or <b>n-</b> before another consonant is a short hum: <i>nngwe</i> (one) is “N-ngweh”."],
    phon_explain="The box marked <i>Sesotho name · syllables</i> shows a simple name for the letter (B is «ba») and its row of "
                 "syllables — the way Sesotho children practise reading.",
    standard="Sesotho as written in South Africa (Lesotho spells some words a little differently)",
    hello=[
        ("Who speaks it?", "About <b>6 million people</b> speak Sesotho as their first language, and millions more use it as "
                           "a second language.<sup>³</sup>"),
        ("Where?", "In <b>Lesotho</b>, a mountain country in southern Africa, and in <b>South Africa</b> — around Bloemfontein, "
                   "Johannesburg and the Free State."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. Lesotho and South Africa spell a few "
                               "sounds differently: <i>lipalesa</i> and <i>dipalesa</i> are the same word, “flowers”."),
        ("How many letters?", "<b>22 letters</b>: A B D E F G H I J K L M N O P Q R S T U W Y."),
        ("The Kingdom in the Sky", "All of Lesotho is high up in the mountains. Its <b>lowest</b> point is higher than the lowest "
                                   "point of any other country in the world — and snow falls there in winter!"),
        ("Did you know?", "The <b>mokorotlo</b>, a hat woven from grass, is shaped like the mountain Qiloane. Basotho families "
                          "also wrap up in warm, colourful woollen <b>blankets</b>."),
    ],
    hello_pics=[("st_mokorotlo", {}), ("mountain", {}), ("st_kobo", {})],
    map=region_map(frame=[[21.5, -35.0], [33.5, -23.0]],
                   points=dict(maseru=[27.48, -29.31], bloemfontein=[26.21, -29.09], johannesburg=[28.05, -26.20],
                               qwaqwa=[28.82, -28.53]),
                   area=(27.8, -28.6, 200, 230), area_rot=0,
                   cities=[("maseru", "Maseru", 14, 16, "start", False), ("bloemfontein", "Bloemfontein", -14, 8, "end", False),
                           ("johannesburg", "Johannesburg", 14, 8, "start", False), ("qwaqwa", "Phuthaditjhaba", 14, 4, "start", False)],
                   label="SOUTHERN AFRICA", label_at=[25.5, -24.0], marker=[28.0, -29.0],
                   caption="The circle shows Lesotho and South Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Sesotho is spoken in Maseru, "
                          "Bloemfontein, Phuthaditjhaba and Johannesburg. The dashed line shows where most Sesotho speakers live.",
                   seas=[("Indian Ocean", 30.5, -33.6)], world_r=13),
    digits=[("0", "lefela", "leh-FEH-lah", "zero, nothing"), ("1", "nngwe", "N-ngweh", "one"), ("2", "pedi", "PEH-dee", "two"),
            ("3", "tharo", "TAH-roh", "three"), ("4", "nne", "N-neh", "four"), ("5", "hlano", "HLAH-noh", "five"),
            ("6", "tshelela", "tsheh-LEH-lah", "six"), ("7", "supa", "SOO-pah", "seven"), ("8", "robedi", "roh-BEH-dee", "eight"),
            ("9", "robong", "roh-BOHNG", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAI-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAI-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Dumela!", "doo-MEH-lah", "Hello!"),
             ("Lebitso la ka ke …", "leh-BEE-tsoh lah kah keh …", "My name is …"),
             ("Ke a leboha", "keh ah leh-BOH-hah", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAHL-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("mme · ntate", "M-meh · n-TAH-teh", "Mother · Father"),
             ("abuti · ausi", "ah-BOO-tee · ah-OO-see", "Brother · Sister"),
             ("e · tjhe", "eh · CHEH", "Yes · No"),
             ("Ke ithuta Sesotho!", "keh ee-TOO-tah seh-SOO-too", "I am learning Sesotho!")],
    cheer=("Mashallah! O entse hantle!", "MAH-shah-lah! oh EHN-tseh HAHN-tleh!", "Mashallah! You did well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B D", right="E F G"),
    review_note="Check the simple letter names (a, ba, da…); the choice of South African spelling over Lesotho spelling "
                "(dipalesa/lipalesa, nngwe/’ngoe, tjhe/che, mantswe/mantsoe); <i>maqhubu</i> (waves) for the Q click; "
                "<i>lengolo</i> for G, <i>heke</i> for H, <i>raese</i> for R, <i>mokopu</i> for U and <i>monyako</i> for Y; "
                "<i>abuti · ausi</i> for brother · sister; the stress capitals (Sesotho is tonal); and the mokorotlo/Qiloane fact.",
    tiles="ABKMPQ", cover_pics=["st_mokorotlo", "st_kobo", "mountain", "mosque"],
    speakers_blurb="Sesotho is spoken by about 6 million people in Lesotho and South Africa.",
    sample_words=[("pula", "POO-lah", "rain"), ("naledi", "nah-LEH-dee", "star"), ("sefate", "seh-FAH-teh", "tree")],
    keywords=["sesotho alphabet book for kids", "learn sesotho for children", "southern sotho coloring book",
              "lesotho sesotho letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual sesotho english toddlers"],
))
