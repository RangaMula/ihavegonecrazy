# -*- coding: utf-8 -*-
"""Book 85 - Nahuatl (modern Central Nahuatl, practical alphabet, 19 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"); the digraphs are drawn as "Ch ch", "Kw kw", "Tl tl", "Tz tz"."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Nahuatl letter name"


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    big = cap + cap.lower() if len(cap) == 1 else f"{cap} {cap.lower()}"
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


OLD = "Older books, written in the Spanish style, spell this sound "

LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "awakatl", "ah-WAH-kahtl", "avocado", "nah_avocado",
      note="The English word <i>avocado</i> comes from Nahuatl <i>awakatl</i>!"),
    L("Ch", "cha", "chah", "‘ch’ as in “chair”", "chili", "CHEE-lee", "chili pepper", "dz_chilli",
      note="English <i>chili</i> comes from Nahuatl <i>chili</i>."),
    L("E", "e", "eh", "‘e’ as in “bed”", "etl", "etl", "bean", "chr_beans"),
    L("I", "i", "ee", "‘ee’ as in “see”", "istatl", "ees-TAHTL", "salt", "salt"),
    L("J", "ja", "hah", "a soft breath ‘h’, as in “ahead” (in some towns a little catch in the voice)", "ojtli", "OH-h-tlee",
      "road, path", "sat_path",
      note="J hardly ever starts a Nahuatl word. Find it in the middle of <i>ojtli</i>! Older books write this sound <i>h</i>, or leave it out."),
    L("K", "ka", "kah", "‘k’ as in “kite”", "kalli", "KAHL-lee", "house", "house",
      note=OLD + "<i>c</i> or <i>qu</i>: <i>kalli</i> was written <i>calli</i>."),
    L("Kw", "kwa", "kwah", "‘kw’ as in “queen” — one sound", "kwawitl", "KWAH-weetl", "tree", "tree",
      note=OLD + "<i>cu</i> or <i>uc</i>: <i>kwawitl</i> was written <i>cuahuitl</i>."),
    L("L", "la", "lah", "‘l’ as in “lamp”; <i>ll</i> is a longer ‘l’", "molkaxitl", "mohl-KAH-sheetl", "stone mortar bowl", "mortar",
      note="L hardly ever starts a Nahuatl word. Find it in the middle of <i>molkaxitl</i>, the bowl for grinding chili and tomato!"),
    L("M", "ma", "mah", "‘m’ as in “moon”", "metztli", "METS-tlee", "moon", "moon"),
    L("N", "na", "nah", "‘n’ as in “net”", "nopalli", "noh-PAHL-lee", "prickly-pear cactus", "nah_nopal"),
    L("O", "o", "oh", "‘o’ as in “go” — some speakers say it more like ‘oo’", "okotl", "OH-kohtl", "pine tree", "ru_fir"),
    L("P", "pa", "pah", "‘p’ as in “pen”", "petlatl", "PEH-tlahtl", "woven palm mat", "nah_petlatl"),
    L("S", "sa", "sah", "‘s’ as in “sun”", "sitlalin", "see-TLAH-leen", "star", "star",
      note=OLD + "<i>c</i> or <i>z</i>: <i>sitlalin</i> was written <i>citlalin</i>."),
    L("T", "ta", "tah", "‘t’ as in “top”", "tomatl", "TOH-mahtl", "tomato", "tomato",
      note="English <i>tomato</i> comes from Nahuatl <i>tomatl</i>!"),
    L("Tl", "tla", "tlah", "one quick sound: ‘t’ and ‘l’ together, as at the end of “little”", "tlaxkalli", "tlahsh-KAHL-lee",
      "tortillas", "nah_tortilla", rule="Many Nahuatl words end in <b>-tl</b>: <i>etl, tomatl, xochitl</i>."),
    L("Tz", "tza", "tsah", "‘ts’ as in “cats” — one sound", "tzapotl", "TSAH-pohtl", "sapote fruit", "nah_sapote",
      note="Some writers spell this sound <i>ts</i>: <i>tsapotl</i>."),
    L("W", "wa", "wah", "‘w’ as in “water”", "wawtli", "WOW-tlee", "amaranth plant", "nah_amaranth",
      note=OLD + "<i>hu</i> or <i>uh</i>: <i>wawtli</i> was written <i>huauhtli</i>."),
    L("X", "xa", "shah", "‘sh’ as in “shop”", "xochitl", "SHOH-cheetl", "flower", "flower"),
    L("Y", "ya", "yah", "‘y’ as in “yes”", "yowalli", "yoh-WAHL-lee", "night", "nah_night"),
]

LANG = build(dict(
    code="nah", folder="book-85-nahuatl", series_no=85, isbn="", draft=True,
    name="Nahuatl", native="nawatl", native_tr="NAH-wahtl", name_word="tokaitl", write_word="xikijkuilo",
    title_native="Ma timomachtikan nawatl!", title_letters=["A", "a", "Tl", "tl", "X", "x"],
    belongs_native="Inin amoxtli itech pohui", belongs_pic="flower",
    alphabet_native="tlajkuilolli", numbers_native="tlapowalli", numbers_tr="tlah-poh-WAHL-lee",
    phrases_native="Achtopa tlajtolli",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Nahuatl name (A «a», Ch «cha», Tl «tla»…)",
    sections=[section(LETTERS, native="tlajkuilolli", native_tr="tlah-kwee-LOHL-lee — “the letters, the writing”",
                      chart_cols=5, warmup_cols=5,
                      intro_html="""<p>This book uses the modern <b>practical alphabet</b> that many Nahuatl schools and writers use today:
<b>19 letters</b>, four of them vowels (<b>a e i o</b>).</p>
<div class="box" style="margin:0.1in 0"><h3>Letters that work as a team</h3><b>Ch</b>, <b>Kw</b>, <b>Tl</b> and <b>Tz</b> are written with two
letters but say <b>one sound</b>. <b>Tl</b> is Nahuatl’s very own sound — and many words end with it: <i>tomatl, xochitl</i>!</div>
<div class="box" style="margin:0.1in 0"><h3>Old and new spellings</h3>Older books use Spanish-style spellings: <i>c, qu, cu, z, hu</i>.
So <i>calli</i>, <i>cuahuitl</i> and <i>huauhtli</i> are the same words as <i>kalli</i>, <i>kwawitl</i> and <i>wawtli</i>.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>, <b>Tl tl</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable — in Nahuatl it is nearly always the <b>second-to-last</b>: <i>noh-PAHL-lee</i>.",
        "<b>tl</b> in the pronunciation is one quick sound: say ‘t’ and ‘l’ together, like the end of “little”.",
        "<b>sh</b> is the Nahuatl letter <b>x</b>, and <b>ts</b> is the letter <b>tz</b>.",
        "<b>h</b> is the Nahuatl letter <b>j</b>: a soft breath, never a hard sound.",
        "Nahuatl is spoken a little differently from town to town; this book follows the central varieties."],
    phon_explain="The box marked <i>Nahuatl letter name</i> shows a simple name for the letter (the sound plus “a”: «ka», «tla»…), "
                 "the way many Nahuatl primers say the alphabet.",
    standard="modern Central Nahuatl, written in the practical alphabet (k, kw, s, w, j)",
    hello=[
        ("Who speaks it?", "About <b>1.7 million people</b> speak Nahuatl — more than any other indigenous language of Mexico.<sup>³</sup>"),
        ("Where?", "In <b>central Mexico</b>: in Puebla, Veracruz, Hidalgo, San Luis Potosí, Guerrero and around Mexico City."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. Many words end in <b>-tl</b> or <b>-tli</b>."),
        ("How many letters?", "<b>19 letters</b> in the practical alphabet: 4 vowels and 15 consonants."),
        ("Words you already know!", "<b>Tomato</b>, <b>avocado</b>, <b>chili</b> and <b>chocolate</b> all come from Nahuatl: "
                                    "<i>tomatl, awakatl, chili, chokolatl</i>."),
        ("Did you know?", "The volcano <b>Popocatépetl</b>, near Mexico City, has a Nahuatl name: “Smoking Mountain”. "
                          "Nahuatl also counts in <b>twenties</b>!"),
    ],
    hello_pics=[("nah_avocado", {}), ("tomato", {}), ("nah_nopal", {})],
    map=region_map(frame=[[-104.5, 14.0], [-92.5, 26.0]],
                   points=dict(mexico=[-99.13, 19.43], puebla=[-98.20, 19.04], veracruz=[-96.13, 19.17], slp=[-100.98, 22.15]),
                   area=(-98.5, 19.8, 190, 230), area_rot=-15,
                   cities=[("mexico", "Mexico City", -14, 18, "end", False), ("puebla", "Puebla", 12, 22, "start", False),
                           ("veracruz", "Veracruz", 14, 8, "start", False), ("slp", "San Luis Potosí", -14, 8, "end", False)],
                   label="MEXICO", label_at=[-103.0, 24.8], marker=[-98.5, 19.5],
                   caption="The circle shows central Mexico on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Nahuatl is spoken in many towns and "
                          "villages around Mexico City, Puebla and Veracruz and in the hills of the Huasteca. The dashed line shows where most "
                          "Nahuatl speakers live.",
                   seas=[("Gulf of Mexico", -94.6, 23.2), ("Pacific Ocean", -100.5, 15.2)], world_r=14),
    digits=[("0", "amitla", "ah-MEE-tlah", "zero (“nothing”)"), ("1", "se", "seh", "one"), ("2", "ome", "OH-meh", "two"),
            ("3", "eyi", "EH-yee", "three"), ("4", "nawi", "NAH-wee", "four"), ("5", "makwilli", "mah-KWEEL-lee", "five"),
            ("6", "chikwasen", "chee-KWAH-sen", "six"), ("7", "chikome", "chee-KOH-meh", "seven"),
            ("8", "chikweyi", "chee-KWEH-yee", "eight"), ("9", "chiknawi", "cheek-NAH-wee", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Niltze!", "NEEL-tseh", "Hello!"),
             ("Notokah …", "noh-TOH-kah …", "My name is …"),
             ("Tlaskamati", "tlahs-kah-MAH-tee", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAHL-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("nonan · notah", "NOH-nahn · NOH-tah", "My mother · My father"),
             ("nokniw · noweltiw", "NOHK-neew · noh-WEHL-teew", "My brother · My sister"),
             ("kema · amo", "KEH-mah · AH-moh", "Yes · No"),
             ("Ninomachtia nawatl!", "nee-noh-mahch-TEE-ah NAH-wahtl", "I am learning Nahuatl!")],
    cheer=("Mashallah! Kwali otikchiw!", "MAH-shah-lah! KWAH-lee oh-TEEK-cheew!", "Mashallah! You did it well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and Mexico’s 2020 census (<b>INEGI</b>), rounded.",
    book_pic=dict(left="A CH E", right="I J K"),
    review_note="Nahuatl varies a lot from region to region: please check every word against one chosen variety and spelling "
                "(SEP/INALI-style practical alphabet with k, kw, s, w, j, tz). Check especially: the letter names («ka», «tla»…); "
                "<i>ojtli</i> (road) for J and <i>molkaxitl</i> (mortar) for L, since neither letter normally starts a word; "
                "<i>wawtli</i> (amaranth), <i>yowalli</i> (night), <i>okotl</i> (pine) and <i>istatl</i> (salt) in modern spelling; "
                "<i>amitla</i> for zero; the greeting <i>Niltze</i> (Huasteca speakers say <i>Piyali</i>); <i>nokniw · noweltiw</i> "
                "for brother · sister; the title <i>Ma timomachtikan nawatl!</i>, <i>Inin amoxtli itech pohui</i>, <i>xikijkuilo</i>, "
                "<i>tlajkuilolli</i>, <i>Achtopa tlajtolli</i> and the cheer <i>Kwali otikchiw!</i>",
    tiles=["A", "Tl", "Ch", "Tz", "Kw", "X"], cover_pics=["nah_avocado", "tomato", "flower", "mosque"], title_size=48,
    speakers_blurb="Nahuatl, the language that gave English the words tomato, avocado and chocolate, is spoken by about 1.7 million people in Mexico.",
    sample_words=[("tomatl", "TOH-mahtl", "tomato"), ("xochitl", "SHOH-cheetl", "flower"), ("kalli", "KAHL-lee", "house")],
    keywords=["nahuatl alphabet book for kids", "learn nahuatl for children", "nahuatl coloring book",
              "mexican indigenous language workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual nahuatl english"],
))
