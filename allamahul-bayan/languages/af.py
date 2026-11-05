# -*- coding: utf-8 -*-
"""Book 76 - Afrikaans (Latin script, 26 letters). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Afrikaans letter name"


def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("A", "aa", "ah", "‘a’ as in “father”; short A is like ‘u’ in “cup”", "appel", "AH-pul", "apple", "apple"),
    L("B", "bee", "BEE-uh", "‘b’ as in “ball”", "boek", "BOOK", "book", "book", args=dict(left="A B C", right="D E F"),
      rule="oe = ‘oo’ as in “moon”: b<b>oe</b>k"),
    L("C", "see", "SEE-uh", "‘s’ or ‘k’ — only in borrowed words and names", "croissant", "krwah-SAHNG", "croissant", "af_croissant",
      note="C is rare in Afrikaans: it is used only in names and in words from other languages."),
    L("D", "dee", "DEE-uh", "‘d’ as in “door” (at the end of a word it says ‘t’)", "deur", "DEE-ur", "door", "door"),
    L("E", "ee", "EE-uh", "‘e’ as in “bed”; often a soft ‘uh’", "eier", "AY-ur", "egg", "egg",
      rule="ee = “ee-uh” · ei = “ay” · ê = ‘e’ as in “there”"),
    L("F", "ef", "ef", "‘f’ as in “fan”", "fynbos", "FAYN-bos", "fynbos, the wild flowers of the Cape", "af_protea"),
    L("G", "gee", "KHEE-uh", "a soft throaty ‘kh’ — like Arabic خ", "geskenk", "khuh-SKENK", "gift, present", "gift",
      note="Afrikaans G is not like English G: it is said in the throat, like the Arabic letter <i>khā’</i> (خ)."),
    L("H", "haa", "hah", "‘h’ as in “hat” (breathy)", "huis", "HAYS", "house", "house",
      rule="ui = a sound like “ay”, said with round lips"),
    L("I", "ie", "ee", "short ‘uh’ as in “the”; ie = ‘ee’ as in “see”", "ink", "UNK", "ink", "pen",
      rule="i = “uh” · ie = “ee” · î = a long “uh”"),
    L("J", "jee", "YEE-uh", "‘y’ as in “yes”", "jas", "YUS", "coat", "af_jas"),
    L("K", "kaa", "kah", "‘k’ as in “kite”", "koppie", "KAW-pee", "cup", "teacup"),
    L("L", "el", "el", "‘l’ as in “lamp”", "leer", "LEE-ur", "ladder", "ladder"),
    L("M", "em", "em", "‘m’ as in “moon”", "moskee", "maw-SKEE-uh", "mosque", "mosque"),
    L("N", "en", "en", "‘n’ as in “net”", "neut", "NEE-ut", "nut", "walnut", rule="eu = “ee-uh” said with round lips"),
    L("O", "oo", "OO-uh", "‘aw’ as in “saw” (short); oo = “oo-uh”", "olyf", "oo-LAYF", "olive", "olive"),
    L("P", "pee", "PEE-uh", "‘p’ as in “pen”", "peer", "PEE-ur", "pear", "pear"),
    L("Q", "kuu", "kew", "‘k’ — only in borrowed words", "quiche", "KEESH", "quiche (an egg tart)", "af_quiche",
      note="Q is very rare in Afrikaans: it appears only in words from other languages."),
    L("R", "er", "err", "a rolled ‘r’ — let your tongue buzz!", "reënboog", "REE-un-boo-ukh", "rainbow", "rainbow",
      rule="ë: the two dots say “start a new sound here”: re-ën"),
    L("S", "es", "es", "‘s’ as in “sun”", "son", "SAWN", "sun", "sun"),
    L("T", "tee", "TEE-uh", "‘t’ as in “tap”", "tamatie", "tuh-MAH-tee", "tomato", "tomato"),
    L("U", "uu", "ew", "say ‘ee’ with round lips; short U is like ‘u’ in “fur”", "ui", "AY", "onion", "onion",
      note="<i>ui</i> sounds like “ay” said with round lips — a very Afrikaans sound!"),
    L("V", "vee", "FEE-uh", "‘f’ as in “fan”! Afrikaans V says F", "vlag", "FLAKH", "flag", "flag"),
    L("W", "wee", "VEE-uh", "‘v’ as in “van”! Afrikaans W says V", "wolk", "VAWLK", "cloud", "clouds"),
    L("X", "eks", "eks", "‘ks’ as in “box”; ‘s’ at the start of a word — only in borrowed words", "xilofoon", "see-loo-FOO-un",
      "xylophone", "af_xilofoon", note="X is rare in Afrikaans: it is used only in words from other languages."),
    L("Y", "y", "ay", "‘ay’ — the same sound as EI", "ys", "AYS", "ice", "ice"),
    L("Z", "zet", "zet", "‘z’ as in “zoo” — only in borrowed words", "pizza", "PEET-sah", "pizza", "af_pizza",
      note="Z hardly ever starts an Afrikaans word. Find it inside <i>pizza</i>!"),
]

LANG = build(dict(
    code="af", folder="book-76-afrikaans", series_no=76, isbn="", draft=True,
    name="Afrikaans", native="Afrikaans", native_tr="ah-free-KAHNS", name_word="naam", write_word="skryf",
    title_native="My eerste Afrikaanse alfabet", title_letters="AaBbCc", belongs_native="Hierdie boek behoort aan",
    belongs_pic="af_protea", alphabet_native="die alfabet", numbers_native="die getalle", numbers_tr="dee khuh-TAH-luh",
    phrases_native="Eerste woorde",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Afrikaans name (A «aa», B «bee», G «gee»…)",
    sections=[section(LETTERS, native="die alfabet", native_tr="dee AHL-fah-bet — “the alphabet”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Afrikaans uses the same <b>26 letters</b> as English — but some of them make surprising sounds!</p>
<div class="box" style="margin:0.1in 0"><h3>Watch out!</h3><b>V</b> says “f”, <b>W</b> says “v”, <b>J</b> says “y”, and <b>G</b> is a soft
sound in the throat, like the Arabic letter خ.</div>
<div class="box" style="margin:0.1in 0"><h3>Hats and dots</h3>Some vowels wear a little hat — <b>ê ô û î</b> — to make a longer sound.
Two dots — <b>ë ï</b> — say “start a new sound here”: <i>re-ën</i> (rain).</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>tuh-MAH-tee</i> means “say MAH a little louder”.",
        "<b>kh</b> is the soft throaty sound of Afrikaans G (like Arabic خ or Scottish “loch”).",
        "<b>uh</b> is a short, relaxed sound, like the “a” in “about”.",
        "<b>ee-uh</b>, <b>oo-uh</b> are long vowels that slide a little: <i>leer</i> (ladder) is “LEE-ur”."],
    phon_explain="The box marked <i>Afrikaans letter name</i> shows the name Afrikaans children use for the letter "
                 "(B is «bee», G is «gee») and any letter friends that change its sound.",
    standard="Standard Afrikaans as taught in South African schools",
    hello=[
        ("Who speaks it?", "About <b>7 million people</b> speak Afrikaans as their first language, and millions more speak it as "
                           "a second language.<sup>³</sup>"),
        ("Where?", "In <b>South Africa</b> and <b>Namibia</b> — in <b>Cape Town</b>, Pretoria, Windhoek and across the dry, wide "
                   "lands of the west."),
        ("How is it written?", "Today in the <b>Latin alphabet</b>, from <b>left to right</b>, with little hats and dots: ê ë ô û."),
        ("How many letters?", "<b>26 letters</b> — the same as English. Afrikaans grew from Dutch, mixed with words from Malay, "
                              "Portuguese and African languages."),
        ("The Cape Malay community", "Muslims have lived at the Cape for more than <b>300 years</b>. The <b>Cape Malay</b> community "
                                     "of Cape Town built the Auwal Mosque in <b>1794</b> and gave Afrikaans words like <i>piesang</i> "
                                     "(banana, from Malay <i>pisang</i>) and <i>blatjang</i> (chutney)."),
        ("Did you know?", "Some of the <b>very first books in Afrikaans</b> were written in <b>Arabic letters</b>! Muslim teachers "
                          "at the Cape wrote Afrikaans in Arabic script to teach children in the madrasa."),
    ],
    hello_pics=[("af_bokaap", {}), ("af_protea", {}), ("mosque", {})],
    map=region_map(frame=[[14.5, -35.5], [33.0, -17.0]],
                   points=dict(capetown=[18.42, -33.92], pretoria=[28.19, -25.75], bloemfontein=[26.21, -29.09],
                               windhoek=[17.08, -22.56], upington=[21.26, -28.45], gqeberha=[25.60, -33.96]),
                   area=(21.8, -30.0, 240, 200), area_rot=0,
                   cities=[("capetown", "Cape Town", 0, 28, "middle", False), ("pretoria", "Pretoria", 14, 8, "start", False),
                           ("bloemfontein", "Bloemfontein", 14, 8, "start", False), ("windhoek", "Windhoek", 14, 8, "start", False),
                           ("upington", "Upington", 14, 8, "start", False), ("gqeberha", "Gqeberha", 0, 26, "middle", False)],
                   label="SOUTHERN AFRICA", label_at=[25.5, -19.0], marker=[22.0, -29.0],
                   caption="The circle shows southern Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the oceans <b>blue</b>. <b>Find it:</b> Afrikaans is spoken in Cape Town, "
                          "Upington, Bloemfontein, Pretoria, Gqeberha and Windhoek. The dashed line shows where many Afrikaans speakers live.",
                   seas=[("Atlantic Ocean", 16.2, -31.0), ("Indian Ocean", 30.0, -34.7)], world_r=14),
    digits=[("0", "nul", "NUL", "zero"), ("1", "een", "EE-un", "one"), ("2", "twee", "TWEE-uh", "two"),
            ("3", "drie", "DREE", "three"), ("4", "vier", "FEER", "four"), ("5", "vyf", "FAYF", "five"),
            ("6", "ses", "SES", "six"), ("7", "sewe", "SEE-vuh", "seven"), ("8", "agt", "AKHT", "eight"),
            ("9", "nege", "NEE-khuh", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAI-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAI-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Hallo! · Goeiemôre!", "HAH-loh · KHOO-yuh-MAW-ruh", "Hello! · Good morning!"),
             ("My naam is …", "may NAHM is …", "My name is …"),
             ("Dankie", "DUNG-kee", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAHL-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("ma · pa", "MAH · PAH", "Mother · Father"),
             ("broer · suster", "BROO-ur · SUR-stur", "Brother · Sister"),
             ("ja · nee", "YAH · NEE-uh", "Yes · No"),
             ("Ek leer Afrikaans!", "ek LEE-ur ah-free-KAHNS", "I am learning Afrikaans!")],
    cheer=("Mashallah! Mooi so!", "MAH-shah-lah! MOY saw!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Check the letter names (aa, bee, see… especially «kuu» for Q, «y» for Y and «zet» for Z); the sound guides for "
                "ui, eu, oo, ee and G; the borrowed-word choices for C (<i>croissant</i>), Q (<i>quiche</i>), X (<i>xilofoon</i>, "
                "and how its X is said) and Z (<i>pizza</i>); <i>ink</i> for I; the stress capitals; and the Cape Malay and "
                "Arabic-Afrikaans facts (Auwal Mosque 1794, <i>piesang</i>, <i>blatjang</i>).",
    tiles="AGJVWY", cover_pics=["af_protea", "af_bokaap", "grapes", "mosque"],
    speakers_blurb="Afrikaans is spoken by millions of people in South Africa and Namibia, among them the Muslims of the Cape.",
    sample_words=[("son", "SAWN", "sun"), ("huis", "HAYS", "house"), ("reënboog", "REE-un-boo-ukh", "rainbow")],
    keywords=["afrikaans alphabet book for kids", "learn afrikaans for children", "afrikaans coloring book",
              "afrikaans letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual afrikaans english toddlers"],
))
