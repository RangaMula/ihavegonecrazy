# -*- coding: utf-8 -*-
"""Book 86 - K'iche' (official ALMG Mayan alphabet, 26 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"); letters of more than one sign are drawn as "B' b'", "Ch' ch'", "Tz' tz'"."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "K'iche' letter name"


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    big = cap + cap.lower() if len(cap) == 1 else f"{cap} {cap.lower()}"
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


POP = "a ‘popping’ "
INSIDE = " hardly ever starts a K'iche' word. Find it in the middle of "

LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "ab'aj", "ah-B'AHKH", "stone", "hy_stones"),
    L("B'", "b'a", "b'ah", POP + "‘b’: close the lips, and let the sound pop inward", "b'e", "b'eh", "road, path", "kk_road",
      note="K'iche' has no plain ‘b’ — every B has its little mark: <b>B'</b>."),
    L("Ch", "cha", "chah", "‘ch’ as in “chair”", "che'", "cheh'", "tree", "tree"),
    L("Ch'", "ch'a", "ch'ah", POP + "‘ch’: hold your breath in the throat and let it go", "ch'umil", "ch'oo-MEEL", "star", "star",
      rule="<b>ch</b> and <b>ch'</b> are two different letters!"),
    L("E", "e", "eh", "‘e’ as in “bed”", "etz'ab'al", "eh-ts'ah-B'AHL", "toy", "ball"),
    L("I", "i", "ee", "‘ee’ as in “see”", "ixim", "ee-SHEEM", "maize, corn", "corn"),
    L("J", "ja", "khah", "a breathy ‘kh’ from the throat, like Arabic خ", "ja", "khah", "house", "house",
      note="Listen closely: <i>ja</i> is “house”, but <i>ja'</i>, with a little stop at the end, is “water”!"),
    L("K", "ka", "kah", "‘k’ as in “kite”", "kab'", "kahb'", "honey", "honey"),
    L("K'", "k'a", "k'ah", POP + "‘k’ from the throat", "k'im", "k'eem", "straw, dry grass", "chr_grass",
      rule="<b>k</b> and <b>k'</b> are two different letters!"),
    L("L", "la", "lah", "‘l’ as in “lamp”", "laq", "lahq", "plate, bowl", "plate"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "mexa", "meh-SHAH", "table", "km_table",
      note="<i>Mexa</i> comes from the Spanish word <i>mesa</i>, “table”."),
    L("N", "na", "nah", "‘n’ as in “net”", "nima'", "nee-MAH'", "river", "nah_river"),
    L("O", "o", "oh", "‘o’ as in “go” (short and pure)", "oj", "ohkh", "avocado", "nah_avocado"),
    L("P", "pa", "pah", "‘p’ as in “pen”", "pop", "pohp", "woven mat", "nah_petlatl"),
    L("Q", "qa", "qah", "a ‘k’ made far back in the throat, like Arabic ق", "saqmo'l", "sahq-MOH'L", "egg", "egg",
      note="Q" + INSIDE + "<i>saqmo'l</i>! (<i>saq</i> means “white”.)"),
    L("Q'", "q'a", "q'ah", POP + "‘q’, deep in the throat", "q'ij", "q'eekh", "sun, day", "sun",
      rule="<b>q</b> and <b>q'</b> are two different letters!"),
    L("R", "ra", "rah", "a tapped ‘r’, as in Spanish “pero”", "rax", "rahsh", "green, fresh like a new leaf", "kk_sprout"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "sutz'", "soots'", "cloud", "clouds"),
    L("T", "ta", "tah", "‘t’ as in “top”", "tinamit", "tee-nah-MEET", "town", "building"),
    L("T'", "t'a", "t'ah", POP + "‘t’", "t'uy", "t'ooy", "small clay pot", "pot",
      rule="<b>t</b> and <b>t'</b> are two different letters!"),
    L("Tz", "tza", "tsah", "‘ts’ as in “cats” — one sound", "tzij", "tseekh", "word", "book"),
    L("Tz'", "tz'a", "ts'ah", POP + "‘ts’", "tz'ib'", "ts'eeb'", "writing", "pen",
      rule="<b>tz</b> and <b>tz'</b> are two different letters!"),
    L("U", "u", "oo", "‘oo’ as in “moon”", "ulew", "oo-LEHW", "earth, soil", "am_seedling"),
    L("W", "wa", "wah", "‘w’ as in “water”", "wa", "wah", "tortillas, food", "nah_tortilla"),
    L("X", "xa", "shah", "‘sh’ as in “shop”", "xan", "shahn", "adobe brick", "brick"),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "q'ayes", "q'ah-YEHS", "plant, herbs", "si_plant",
      note="Y" + INSIDE + "<i>q'ayes</i>!"),
]

LANG = build(dict(
    code="quc", folder="book-86-kiche", series_no=86, isbn="", draft=True,
    name="K'iche'", native="K'iche'", native_tr="k'ee-CHEH'", name_word="b'i'aj", write_word="chatz'ib'aj",
    title_native="Ri nab'e nuwuj pa K'iche'", title_letters=["A", "a", "Ch'", "ch'", "Q'", "q'"],
    belongs_native="We wuj ri' rech", belongs_pic="nah_avocado",
    alphabet_native="taq tz'ib'", numbers_native="ajilab'al", numbers_tr="ah-khee-lah-B'AHL",
    phrases_native="Nab'e taq tzij",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s K'iche' name (A «a», B' «b'a», Ch' «ch'a»…)",
    sections=[section(LETTERS, native="taq tz'ib'", native_tr="tahq ts'eeb' — “the letters”",
                      chart_cols=6, warmup_cols=5,
                      intro_html="""<p>K'iche' is written with the official <b>Mayan alphabet</b> of Guatemala’s Academy of Mayan Languages.
This book teaches its <b>26 letters</b>: 5 vowels (<b>a e i o u</b>) and 21 consonants.</p>
<div class="box" style="margin:0.1in 0"><h3>The little mark ( ' )</h3>A mark after a letter makes a <b>popping</b> sound: <b>b' ch' k' q' t' tz'</b>.
Stop the air in your throat, then let it go — pop! <b>K</b> and <b>K'</b> are different letters, so listen carefully.</div>
<div class="box" style="margin:0.1in 0"><h3>A stop in the voice</h3>The same mark on its own is a quick stop in the voice: <i>ja</i> is “house”,
but <i>ja'</i> is “water”. Some writers also show <b>long vowels</b> by writing them twice (<i>aa, ee</i>).</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>, <b>Ch' ch'</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable — in K'iche' it is almost always the <b>last</b> one: <i>ch'oo-MEEL</i>.",
        "An <b>apostrophe ( ' )</b> in the pronunciation means a little <b>pop</b> or stop in the throat.",
        "<b>kh</b> is the K'iche' letter <b>j</b>: a breathy sound from the throat, like Arabic <b>kh</b> (خ).",
        "<b>q</b> is a ‘k’ made far back in the throat, like Arabic <b>qaf</b> (ق).",
        "<b>sh</b> is the K'iche' letter <b>x</b>, and <b>ts</b> is the letter <b>tz</b>."],
    phon_explain="The box marked <i>K'iche' letter name</i> shows a simple name for the letter (the sound plus “a”: «ka», «k'a»…), "
                 "the way many Guatemalan Mayan primers say the alphabet.",
    standard="K'iche' in the official alphabet of the Academia de Lenguas Mayas de Guatemala (ALMG)",
    hello=[
        ("Who speaks it?", "More than <b>1 million people</b> speak K'iche' — one of the biggest Mayan languages.<sup>³</sup>"),
        ("Where?", "In the green <b>highlands of Guatemala</b>, around Quetzaltenango, Totonicapán, Santa Cruz del Quiché and Lake Atitlán."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with a little mark ( <b>'</b> ) for its popping sounds."),
        ("How many letters?", "<b>26 letters</b> in this book: 5 vowels and 21 consonants."),
        ("A Mayan language", "K'iche' is one of more than <b>20 Mayan languages</b> spoken in Guatemala, Mexico and Belize."),
        ("Did you know?", "K'iche' counts in <b>twenties</b>: <i>juwinaq</i> means twenty. And it has the same deep <b>q</b> sound as Arabic ق!"),
    ],
    hello_pics=[("corn", {}), ("nah_avocado", {}), ("star", {})],
    map=region_map(frame=[[-92.8, 12.9], [-87.8, 17.9]],
                   points=dict(xela=[-91.52, 14.84], quiche=[-91.15, 15.03], guate=[-90.51, 14.63]),
                   area=(-91.3, 15.0, 120, 110), area_rot=-10,
                   cities=[("xela", "Quetzaltenango", -6, 28, "end", False), ("quiche", "Santa Cruz del Quiché", 12, -10, "start", False),
                           ("guate", "Guatemala City", 14, 18, "start", False)],
                   label="GUATEMALA", label_at=[-90.6, 16.8], marker=[-91.0, 15.0],
                   caption="The circle shows Guatemala, in Central America, on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> K'iche' is spoken in the western "
                          "highlands, in Quetzaltenango, Santa Cruz del Quiché and many towns around them. The dashed line shows where most "
                          "K'iche' speakers live.",
                   seas=[("Pacific Ocean", -91.4, 13.4)], world_r=14),
    digits=[("0", "majun", "mah-KHOON", "zero (“none”)"), ("1", "jun", "khoon", "one"), ("2", "keb'", "kehb'", "two"),
            ("3", "oxib'", "oh-SHEEB'", "three"), ("4", "kajib'", "kah-KHEEB'", "four"), ("5", "job'", "khohb'", "five"),
            ("6", "waqib'", "wah-QEEB'", "six"), ("7", "wuqub'", "woo-QOOB'", "seven"),
            ("8", "wajxaqib'", "wahkh-shah-QEEB'", "eight"), ("9", "b'elejeb'", "b'eh-leh-KHEHB'", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Saqarik!", "sah-qah-REEK", "Good morning! (Hello!)"),
             ("Ri nub'i' …", "ree noo-B'EE' …", "My name is …"),
             ("Maltyox", "mahl-TYOHSH", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAHL-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("nunan · nutat", "noo-NAHN · noo-TAHT", "My mother · My father"),
             ("watz · wanab'", "wahts · wah-NAHB'", "My big brother · My sister"),
             ("je' · man", "kheh' · mahn", "Yes · No"),
             ("Kinweta'maj ri K'iche'!", "keen-weh-tah'-MAHKH ree k'ee-CHEH'", "I am learning K'iche'!")],
    cheer=("Mashallah! Sib'alaj utz!", "MAH-shah-lah! see-b'ah-LAHKH OOTS!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B' CH", right="CH' E I"),
    review_note="Check against the ALMG K'iche' standard and one chosen dialect. Check especially: the letter names («b'a», «ch'a», «q'a»…); "
                "whether to add the glottal stop ( ' ) and the long vowels (aa ee ii oo uu) as their own letters; "
                "<i>etz'ab'al</i> (toy) for E; <i>k'im</i> (straw) for K'; <i>laq</i> (plate) for L; <i>mexa</i> (a Spanish loan) for M; "
                "<i>nima'</i> (river) for N; <i>saqmo'l</i> for Q and <i>q'ayes</i> for Y, since Q and Y rarely start a word; "
                "<i>rax</i> (green) for R, which is a colour word, not a thing; <i>t'uy</i> (small pot) for T'; <i>tzij</i> (word) for TZ; "
                "<i>majun</i> for zero; <i>je' · man</i> (yes · no); <i>watz · wanab'</i> (these brother/sister words depend on who is speaking); "
                "<i>Kinweta'maj ri K'iche'</i>; and the titles <i>Ri nab'e nuwuj pa K'iche'</i>, <i>We wuj ri' rech</i>, <i>chatz'ib'aj</i>, "
                "<i>taq tz'ib'</i>, <i>ajilab'al</i> and <i>Nab'e taq tzij</i>. Stress marks follow the rule of stress on the last syllable.",
    tiles=["A", "B'", "Ch'", "Q'", "Tz", "X"], cover_pics=["corn", "nah_avocado", "star", "mosque"], title_size=48,
    speakers_blurb="K'iche', a Mayan language of the Guatemalan highlands, is spoken by more than 1 million people.",
    sample_words=[("ch'umil", "ch'oo-MEEL", "star"), ("q'ij", "q'eekh", "sun"), ("ixim", "ee-SHEEM", "corn")],
    keywords=["kiche alphabet book for kids", "learn kiche maya for children", "mayan language coloring book",
              "guatemala kids workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual kiche english"],
))
