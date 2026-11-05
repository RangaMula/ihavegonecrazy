# -*- coding: utf-8 -*-
"""Book 74 - Malagasy (Latin script, 21 letters). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Malagasy name · syllables"
VOWELS = ["a", "e", "i", "o"]


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
    small = cap.lower()
    if row is None:
        row = " · ".join(c + small for c in "b d k m".split()) if vowel else " · ".join(small + v for v in VOWELS)
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
            f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + small, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "akondro", "ah-KOON-droo", "banana", "banana", vowel=True),
    L("B", "ba", "bah", "‘b’ as in “ball”", "boky", "BOO-kee", "book", "book", args=dict(left="A B D", right="E F G")),
    L("D", "da", "dah", "‘d’ as in “door”", "dite", "DEE-teh", "tea", "teacup",
      rule="dr sounds like the ‘dr’ in “dream”: <i>adrisa</i>"),
    L("E", "e", "eh", "‘e’ as in “bed”", "entana", "EN-tah-nah", "luggage, things you carry", "mg_entana", vowel=True),
    L("F", "fa", "fah", "‘f’ as in “fan”", "fary", "FAH-ree", "sugarcane", "sugarcane"),
    L("G", "ga", "gah", "‘g’ as in “go” (always hard)", "gilasy", "gee-LAH-see", "ice, ice cream", "ice"),
    L("H", "ha", "hah", "a very soft ‘h’ — often you hardly hear it", "hazo", "HAH-zoo", "tree", "tree"),
    L("I", "i", "ee", "‘ee’ as in “see”", "isa", "EE-sah", "one (when you count)", "one", args=dict(digit="1"), vowel=True),
    L("J", "ji", "dzee", "‘dz’ — a ‘d’ and a ‘z’ said together", "jiro", "DZEE-roo", "lamp, light", "bulb",
      note="Careful: Malagasy J does not sound like English J. <i>jiro</i> sounds like “DZEE-roo”."),
    L("K", "ka", "kah", "‘k’ as in “kite”", "kintana", "KEEN-tah-nah", "star", "star"),
    L("L", "la", "lah", "‘l’ as in “lamp”", "lakana", "LAH-kah-nah", "canoe", "boat"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "manga", "MAHN-gah", "mango", "mango"),
    L("N", "na", "nah", "‘n’ as in “net”", "nosy", "NOO-see", "island", "mg_nosy",
      rule="N and M often hold hands with the next letter: ma<b>ng</b>a, sa<b>mb</b>o, ki<b>nt</b>ana"),
    L("O", "o", "oo", "‘oo’ as in “moon” — Malagasy O says “oo”!", "orana", "OO-rah-nah", "rain", "raincloud", vowel=True,
      note="O always says “oo”: <i>rano</i> (water) is “RAH-noo”."),
    L("P", "pa", "pah", "‘p’ as in “pen”", "pataty", "pah-TAH-tee", "sweet potato", "potato"),
    L("R", "ra", "rah", "a rolled or tapped ‘r’", "rano", "RAH-noo", "water", "water"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "sambo", "SAHM-boo", "ship", "ship"),
    L("T", "ta", "tah", "‘t’ as in “tap”", "tanimbary", "tah-neem-BAH-ree", "rice field", "paddy",
      rule="tr sounds like the ‘tr’ in “tree” · ts sounds like the ‘ts’ in “cats”"),
    L("V", "va", "vah", "‘v’ as in “van”", "vary", "VAH-ree", "rice", "rice"),
    L("Y", "y", "ee", "‘ee’ as in “see” — the same sound as I", "ony", "OO-nee", "river", "mg_ony", vowel=True,
      rule="i inside a word · y at the end of a word: bok<b>y</b>, var<b>y</b>, nos<b>y</b>",
      note="Y almost never starts a word. Find it at the end of <i>ony</i> — and of <i>boky</i>, <i>fary</i> and <i>vary</i>!"),
    L("Z", "za", "zah", "‘z’ as in “zoo”", "zavona", "ZAH-voo-nah", "mist, fog", "clouds"),
]

LANG = build(dict(
    code="mg", folder="book-74-malagasy", series_no=74, isbn="", draft=True,
    name="Malagasy", native="teny malagasy", native_tr="TEH-nee mah-lah-GAHSS", name_word="anarana", write_word="soraty",
    title_native="Ny abidiko voalohany amin’ny teny malagasy", title_letters="AaBbDd", belongs_native="An’i … ity boky ity",
    belongs_pic="mg_baobab", alphabet_native="ny abidy", numbers_native="ny isa", numbers_tr="nee EE-sah",
    phrases_native="Teny voalohany",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Malagasy name and its syllables (ba, be, bi, bo)",
    sections=[section(LETTERS, native="ny abidy malagasy", native_tr="nee ah-BEE-dee mah-lah-GAHSS — “the Malagasy A-B-C”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Malagasy is written with <b>21 letters</b>. It has no C, Q, U, W or X.</p>
<div class="box" style="margin:0.1in 0"><h3>Four vowel sounds</h3><b>A E I O</b> say <i>ah, eh, ee, oo</i>. Yes — Malagasy <b>O</b> says
<i>oo</i>, and <b>Y</b> says <i>ee</i>, just like I. Children learn to read by singing the syllables: <i>ba be bi bo, da de di do…</i></div>
<div class="box" style="margin:0.1in 0"><h3>Letter friends</h3>Some letters like to stand together: <b>tr</b> (as in “tree”), <b>dr</b>
(as in “dream”), <b>ts</b> (as in “cats”), and <b>mb, nd, ng, nj, nt</b>, where the M or N hums into the next letter.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>RAH-noo</i> means “say RAH a little louder”.",
        "The last vowel of a Malagasy word is often said very softly: <i>vary</i> can sound almost like “VAHR”.",
        "<b>oo</b> is how Malagasy O sounds; <b>dz</b> is how Malagasy J sounds.",
        "<b>tr</b> and <b>dr</b> are said together quickly, as in English “tree” and “dream”."],
    phon_explain="The box marked <i>Malagasy name · syllables</i> shows the name children use for the letter "
                 "(B is «ba», D is «da») and its row of syllables — the way Malagasy is taught in school.",
    standard="Official Malagasy (based on the speech of the central highlands)",
    hello=[
        ("Who speaks it?", "About <b>25 million people</b> speak Malagasy — nearly everyone on the island of Madagascar.<sup>³</sup>"),
        ("Where?", "On <b>Madagascar</b>, a very big island in the <b>Indian Ocean</b>, east of Africa. Its capital is "
                   "<b>Antananarivo</b>, “the city of a thousand”."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, for about 200 years. Long before that, "
                               "Malagasy was written in <b>Arabic letters</b>, a way of writing called <i>sorabe</i>, “big writing”."),
        ("How many letters?", "<b>21 letters</b>: A B D E F G H I J K L M N O P R S T V Y Z."),
        ("A cousin far away", "Malagasy’s closest cousins are spoken on the island of <b>Borneo</b>, thousands of kilometres away. "
                              "Sailors crossed the ocean long, long ago!"),
        ("Did you know?", "Some days of the week come from Arabic: <i>Talata</i> (Tuesday), <i>Alarobia</i> (Wednesday), "
                          "<i>Alakamisy</i> (Thursday) and <i>Zoma</i> (Friday, from <i>al-jumuʿa</i>). And <i>Salama!</i> (hello) "
                          "comes from <i>salām</i>, peace."),
    ],
    hello_pics=[("mg_baobab", {}), ("mg_nosy", {}), ("mosque", {})],
    map=region_map(frame=[[39.5, -27.0], [55.5, -11.0]],
                   points=dict(tana=[47.52, -18.91], toamasina=[49.40, -18.15], mahajanga=[46.32, -15.72],
                               toliara=[43.67, -23.35], antsiranana=[49.29, -12.28], fianarantsoa=[47.09, -21.45]),
                   area=None,
                   cities=[("tana", "Antananarivo", -14, 8, "end", True), ("toamasina", "Toamasina", 14, 8, "start", False),
                           ("mahajanga", "Mahajanga", -14, 8, "end", False), ("toliara", "Toliara", -14, 8, "end", False),
                           ("antsiranana", "Antsiranana", 14, 8, "start", False), ("fianarantsoa", "Fianarantsoa", 14, 8, "start", False)],
                   label="MADAGASCAR", label_at=[47.5, -26.0], marker=[47.0, -19.0],
                   caption="The circle shows Madagascar on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Malagasy is spoken all over the island, "
                          "in Antananarivo, Toamasina, Mahajanga, Fianarantsoa, Toliara and Antsiranana.",
                   seas=[("Indian Ocean", 52.5, -21.0), ("Mozambique Channel", 41.8, -18.5)], world_r=14),
    digits=[("0", "aotra", "OW-tchah", "zero"), ("1", "iray", "ee-RAI", "one"), ("2", "roa", "ROO-ah", "two"),
            ("3", "telo", "TEH-loo", "three"), ("4", "efatra", "EH-fah-tchah", "four"), ("5", "dimy", "DEE-mee", "five"),
            ("6", "enina", "EH-nee-nah", "six"), ("7", "fito", "FEE-too", "seven"), ("8", "valo", "VAH-loo", "eight"),
            ("9", "sivy", "SEE-vee", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAI-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAI-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Salama! · Manao ahoana!", "sah-LAHM · mah-NOW ah-OHN", "Hello! · How are you?"),
             ("Ny anarako dia …", "nee ah-NAH-rah-koo dee …", "My name is …"),
             ("Misaotra", "mee-SOW-tchah", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAHL-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("neny · dada", "NEH-nee · DAH-dah", "Mother · Father"),
             ("rahalahy · anabavy", "rah-hah-LAH-hee · ah-nah-BAH-vee", "Brother · Sister (when a boy speaks)"),
             ("eny · tsia", "EH-nee · TSEE", "Yes · No"),
             ("Mianatra teny malagasy aho!", "mee-AH-nah-tchah TEH-nee mah-lah-GAHSS ah-OO", "I am learning Malagasy!")],
    cheer=("Mashallah! Tsara be!", "MAH-shah-lah! TSAH-rah BEH!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B D", right="E F G"),
    review_note="Check the letter names (a, ba, da… — some schools may say «i fohy» and «y» or other names for I and Y); "
                "the syllable rows (ba be bi bo); <i>entana</i> for E, <i>gilasy</i> for G, <i>isa</i> for I and <i>ony</i> for Y; "
                "the stress capitals and the soft final vowels in the pronunciation guide; <i>aotra</i> for zero; the brother/sister "
                "pair (it changes when a girl speaks: <i>anadahy · rahavavy</i>); and the sorabe and Borneo facts.",
    tiles="ABDHMZ", cover_pics=["mg_baobab", "mg_nosy", "banana", "mosque"],
    speakers_blurb="Malagasy is spoken by about 25 million people on the island of Madagascar.",
    sample_words=[("rano", "RAH-noo", "water"), ("kintana", "KEEN-tah-nah", "star"), ("manga", "MAHN-gah", "mango")],
    keywords=["malagasy alphabet book for kids", "learn malagasy for children", "madagascar language coloring book",
              "malagasy letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual malagasy english toddlers"],
))
