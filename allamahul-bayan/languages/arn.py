# -*- coding: utf-8 -*-
"""Book 88 - Mapudungun (Mapuche), Alfabeto Mapuche Unificado: 6 vowels + 18 consonants = 24 letters.
Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
from _andes import FONTS, GLYPH_FONTS, FONT_CREDIT, maker

L = maker("Mapudungun name · syllables", ["a", "e", "i", "o", "u", "ü"])

VOWELS = [
    L("A", "a", "a", "a", "‘a’ as in “father”", "antü", "AN-tuh", "sun", "sun", vowel=True),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "epew", "e-PEW", "a story, a tale", "book", args=dict(left="A E I", right="O U Ü"),
      vowel=True),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "ilwen", "il-WEN", "dew", "dew", vowel=True),
    L("O", "o", "o", "oh", "‘o’ as in “more” (short and pure)", "ko", "koh", "water", "water", vowel=True,
      note="Not many words start with O. Find it at the end of <i>ko</i>, “water” — a very important word!"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "kura", "KOO-ra", "stone", "qu_stones", vowel=True,
      note="Find U inside <i>kura</i>, “stone”."),
    L("Ü", "ü", "ü", "uh", "a sound between ‘ee’ and ‘oo’: smile and say ‘oo’ — a Mapudungun vowel!", "lewfü", "LEW-fuh", "river",
      "ay_river", vowel=True, note="Ü is a special Mapudungun vowel. Find it at the end of <i>lewfü</i>, “river”."),
]

CONS = [
    L("Ch", "ch", "cha", "chah", "‘ch’ as in “chair”", "challa", "CHA-lya", "clay cooking pot", "pot"),
    L("D", "d", "da", "thah", "‘th’ as in “this” — tongue between the teeth", "kudi", "KOO-thee", "grinding stone", "mortar",
      note="Find D inside <i>kudi</i>, the stone for grinding grain."),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "füw", "fuhw", "thread, yarn", "wool"),
    L("G", "g", "ga", "ghah", "a soft gargled ‘g’, like the g in Spanish “agua”", "lüg", "luhgh", "white", "clouds",
      note="G rarely starts a word you can draw. Find it at the end of <i>lüg</i>, “white” — like the clouds!"),
    L("K", "k", "ka", "kah", "‘k’ as in “sky”", "kütral", "kuh-TRAL", "fire", "qu_fire"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lafken", "laf-KEN", "the sea; a big lake", "waves"),
    L("Ll", "ll", "lla", "lyah", "‘lli’ as in “million”", "llüfke", "LYUHF-keh", "lightning", "arn_lightning"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "mawün", "ma-WUHN", "rain", "raincloud"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "nalka", "NAL-ka", "nalca, a plant with giant leaves", "arn_nalka"),
    L("Ñ", "ñ", "ña", "nyah", "‘ny’ as in “canyon”", "ñire", "NYEE-reh", "ñire, a southern beech tree", "tree"),
    L("Ng", "ng", "nga", "ngah", "‘ng’ as in “sing” — but it can start a word!", "ngülliw", "nguh-LYEEW", "pine nuts of the pewen tree",
      "arn_pinenuts"),
    L("P", "p", "pa", "pah", "‘p’ as in “spin”", "pewen", "peh-WEN", "monkey-puzzle tree (araucaria)", "arn_pewen",
      note="The <i>pewen</i> grows on the mountains of the south. Its nuts, <i>ngülliw</i>, are good to eat."),
    L("R", "r", "ra", "rah", "‘r’ as in English “red” (not rolled)", "ruka", "ROO-ka", "house", "house"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "mansana", "man-SA-na", "apple", "apple",
      note="S is not common in Mapudungun. <i>Mansana</i> is a word borrowed from Spanish <i>manzana</i>."),
    L("T", "t", "ta", "tah", "‘t’ as in “stop”", "tapül", "ta-PUHL", "leaf", "ay_leaf"),
    L("Tr", "tr", "tra", "trah", "‘tr’ as in “tree”, said as one sound", "trayenko", "tra-YEN-koh", "waterfall", "arn_waterfall"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "wangülen", "wa-NGUH-len", "star", "star"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "küyen", "kuh-YEN", "moon", "moon",
      note="Find Y inside <i>küyen</i>, “moon”."),
]

LANG = build(dict(
    code="arn", folder="book-88-mapudungun", series_no=88, isbn="", draft=True,
    name="Mapudungun", native="Mapudungun", native_tr="ma-poo-THOO-ngoon", name_word="üy", write_word="wirin",
    title_native="Mapudungun wirintukun", title_letters="AaEeÜü", belongs_native="Tüfachi chillka ñi ngen",
    belongs_pic="arn_pewen", alphabet_native="wirintukun", numbers_native="rakin", numbers_tr="ra-KEEN",
    phrases_native="Wünelu dungu",
    fonts=FONTS, disp_family="Baloo 2", text_family="Nunito", glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s syllables with the six vowels (cha, che, chi, cho, chu, chü)",
    sections=[
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels", native="a e i o u ü",
                native_tr="the six vowels", chart_title="vowels", chart_cols=6, warmup_title="the vowels", warmup_cols=3,
                intro_html="""<p>Mapudungun has <b>six vowels</b>: <b>a, e, i, o, u</b> and a special one, <b>ü</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>The sixth vowel</h3><b>ü</b> sits between “ee” and “oo”. Smile as if to say “ee”, then try
to say “oo”. You hear it in <i>antü</i> (sun) and <i>küyen</i> (moon).</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(CONS, label="LETTER", chip="THE CONSONANTS", title="The Consonants", native="ch d f g k l ll …",
                native_tr="the consonants", chart_title="consonants", chart_cols=6,
                warmup_title="the consonants", warmup_cols=6,
                intro_html="""<p>This book uses the <b>Alfabeto Mapuche Unificado</b> (the Unified Mapuche Alphabet) with <b>18 consonants</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letter pairs</h3><b>ch</b>, <b>ll</b>, <b>ng</b> and <b>tr</b> are each <b>one sound</b> written
with two letters. <b>ng</b> can even start a word: <i>ngülliw</i> (pine nuts)!</div>
<div class="box"><h3>Tongue between the teeth</h3><b>d</b> sounds like “th” in “this”. Some writers also mark <b>l, n, t</b> said with the
tongue between the teeth by a line underneath: <b>ḻ ṉ ṯ</b>.</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>ROO-ka</i> means “say ROO a little louder”.",
        "<b>uh</b> in the sound guide is the special vowel <b>ü</b>: smile and say “oo”.",
        "<b>th</b> is the soft “th” of “this” (the letter <b>d</b>); <b>gh</b> is a soft gargled ‘g’ (the letter <b>g</b>).",
        "<b>tr</b> is one sound, like the start of “tree”; <b>ly</b> is the ‘lli’ in “million”; <b>ny</b> is the ‘ny’ in “canyon”."],
    phon_explain="The box marked <i>Mapudungun name · syllables</i> shows how the letter is called and its row of syllables with the "
                 "six vowels (<i>ka, ke, ki, ko, ku, kü</i>).",
    standard="Mapudungun of the Araucanía (southern Chile), Alfabeto Mapuche Unificado",
    hello=[
        ("Who speaks it?", "About <b>250,000 people</b> speak Mapudungun, the language of the <b>Mapuche</b> people.<sup>³</sup>"),
        ("Where?", "In <b>southern Chile</b>, around the city of <b>Temuco</b>, and across the Andes in <b>Argentina</b> — and also in big "
                   "cities such as Santiago."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>. People use a few different spelling systems; "
                               "this book uses the <b>Unified Mapuche Alphabet</b>."),
        ("How many letters?", "<b>24 letters</b>: <b>6 vowels</b> (with the special <b>ü</b>) and <b>18 consonants</b>."),
        ("Its own name", "<i>Mapudungun</i> means “the speech of the land”: <i>mapu</i> (land) + <i>dungun</i> (speech). "
                         "<i>Mapuche</i> means “people of the land”."),
        ("Did you know?", "Many places in Chile have Mapudungun names. <i>Temuco</i> comes from <i>temu</i> (a tree) + <i>ko</i> (water)."),
    ],
    hello_pics=[("arn_pewen", {}), ("ay_river", {}), ("arn_pinenuts", {})],
    map=region_map(frame=[[-81.0, -47.0], [-61.0, -27.0]],
                   points=dict(santiago=[-70.67, -33.45], concepcion=[-73.05, -36.82], temuco=[-72.59, -38.74],
                               valdivia=[-73.24, -39.81], neuquen=[-68.06, -38.95], pmontt=[-72.94, -41.47]),
                   area=(-71.4, -38.9, 150, 120), area_rot=0,
                   cities=[("santiago", "Santiago", 14, 8, "start", False), ("concepcion", "Concepción", -14, 8, "end", False),
                           ("temuco", "Temuco", 14, 8, "start", False), ("valdivia", "Valdivia", -14, 8, "end", False),
                           ("neuquen", "Neuquén", 14, 8, "start", False), ("pmontt", "Puerto Montt", 14, 8, "start", False)],
                   label="SOUTHERN ANDES", label_at=[-66.5, -31.0], marker=[-71.0, -38.0],
                   caption="The circle shows southern Chile and Argentina on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the oceans <b>blue</b>. <b>Find it:</b> Mapudungun is spoken around Temuco "
                          "and Valdivia in Chile and Neuquén in Argentina, between the Pacific Ocean and the Andes. The dashed line shows "
                          "where most speakers live.",
                   seas=[("Pacific Ocean", -77.5, -33.0), ("Atlantic Ocean", -63.5, -44.5)], world_r=14),
    digits=[("0", "ngelay", "ngeh-LAY", "zero (“there is none”)"), ("1", "kiñe", "KEE-nyeh", "one"), ("2", "epu", "EH-poo", "two"),
            ("3", "küla", "KUH-la", "three"), ("4", "meli", "MEH-lee", "four"), ("5", "kechu", "KEH-choo", "five"),
            ("6", "kayu", "KA-yoo", "six"), ("7", "regle", "REH-gleh", "seven"), ("8", "pura", "POO-ra", "eight"),
            ("9", "aylla", "AY-lya", "nine")],
    phrases=[("Assalamu alaikum", "as-sa-LA-moo a-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wa a-LAY-koom as-sa-LAM", "And peace be upon you (the reply)"),
             ("Mari mari!", "MA-ree MA-ree", "Hello!"),
             ("Iñche ñi üy …", "ee-NYCHEH nyee uhy …", "My name is …"),
             ("Chaltu may", "CHAL-too may", "Thank you"),
             ("Jazakallahu khairan", "ja-za-KAL-la-hoo KHAI-ran", "May Allah reward you with good"),
             ("ñuke · chaw", "NYOO-keh · chaw", "Mother · Father"),
             ("peñi · lamngen", "PEH-nyee · LAM-ngen", "Brother · Sister"),
             ("may · no", "may · noh", "Yes · No"),
             ("Mapudungun kimkimken!", "ma-poo-THOO-ngoon keem-keem-KEN", "I am learning Mapudungun!")],
    cheer=("Mashallah! Fentren küme!", "MA-sha-la! fen-TREN KUH-meh!", "Mashallah! Very good — well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A E I", right="O U Ü"),
    review_note="Spelling follows the Alfabeto Mapuche Unificado (AMU); Raguileo and Azümchefe spellings differ (e.g. Azümchefe writes "
                "<i>mapuzugun</i>). The interdental letters ḻ ṉ ṯ and the rare SH have no pages. Please check: <i>ilwen</i> (dew), "
                "<i>kudi</i> (grinding stone), <i>lüg</i> (white) for G, <i>llüfke</i> (lightning), <i>nalka</i> (nalca plant), "
                "<i>ñire</i> (tree), <i>ngülliw</i> (pine nuts), <i>tapül</i> (leaf), <i>challa</i> (pot), <i>mansana</i> (apple, a Spanish "
                "loan used for S); the letter names (cha, da…); the title “Mapudungun wirintukun”, “Tüfachi chillka ñi ngen” "
                "(owner of this book), <i>Wünelu dungu</i>, <i>rakin</i>; <i>ngelay</i> used for zero; “may · no” for yes/no; "
                "“Mapudungun kimkimken” (I am learning Mapudungun); and the stressed syllables in the sound guide.",
    tiles="AÜNGTR", cover_pics=["arn_pewen", "sun", "arn_waterfall", "moon"], title_size=44,
    speakers_blurb="Mapudungun, the language of the Mapuche people, is spoken by about 250,000 people in Chile and Argentina.",
    sample_words=[("antü", "AN-tuh", "sun"), ("küyen", "kuh-YEN", "moon"), ("ruka", "ROO-ka", "house")],
    keywords=["mapudungun alphabet book for kids", "learn mapuche language children", "mapudungun coloring book",
              "chile native language tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "mapuche words for toddlers"],
))
