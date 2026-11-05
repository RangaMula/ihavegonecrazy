# -*- coding: utf-8 -*-
"""Book 70 - Shona (chiShona, Latin script, 23 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"), as in languages/es.py."""
from generic import build, section, fontset
from maps import region_map
from _sn_rw_ln_wo import fonts, GLYPH_FONTS, maker, inside

L = maker("Shona syllables · ba be bi bo bu", "a e i o u")

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "mvura", "MVOO-rah", "water", "water", vowel=True,
      note="Few Shona words begin with A, but almost every word ends with a vowel. Hear it at the end of <i>mvura</i>!"),
    L("B", "b", "ba", "bah", "a soft ‘b’, said while swallowing a little; BH is the ‘b’ of “ball”", "bhora", "BOH-rah", "ball", "ball",
      rule="b = a soft, swallowed b · bh = b as in “ball”"),
    L("C", "c", "cha", "chah", "‘ch’ as in “church” — C is always written CH", "chibage", "chee-BAH-geh", "maize cob (corn)", "corn",
      row="cha · che · chi · cho · chu", note="In Shona, C never stands alone: it is always CH."),
    L("D", "d", "da", "dah", "a soft ‘d’, said while swallowing a little; DH is the ‘d’ of “dog”", "dombo", "DOHM-boh", "rock", "sn_rocks",
      rule="d = a soft, swallowed d · dh = d as in “dog” · dz = ‘dz’ as in “adze”"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "nyeredzi", "nyeh-REH-dzee", "star", "star", vowel=True, note=inside("E", "nyeredzi")),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "fasitera", "fah-see-TEH-rah", "window", "window"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "gomo", "GOH-moh", "mountain", "mountain"),
    L("H", "h", "ha", "hah", "a soft, breathy ‘h’ as in “hat”", "hari", "HAH-ree", "clay pot", "pot"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "imba", "EEM-bah", "house", "house", vowel=True),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "jecha", "JEH-chah", "sand", "sn_sand"),
    L("K", "k", "ka", "kah", "‘k’ as in “sky” (no puff of air)", "kapu", "KAH-poo", "cup", "teacup"),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "mwedzi", "MWEH-dzee", "moon", "moon",
      rule="mh = a breathy ‘m’ · mw = ‘mw’ said together"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "nhanga", "NHAHN-gah", "pumpkin", "sn_pumpkin",
      rule="nh = a breathy ‘n’ · ny = ‘ny’ as in “canyon” · n' = ‘ng’ as in “sing”"),
    L("O", "o", "o", "oh", "‘o’ as in “for” — short and pure", "moto", "MOH-toh", "fire", "sn_fire", vowel=True, note=inside("O", "moto")),
    L("P", "p", "pa", "pah", "‘p’ as in “spin” (no puff of air)", "popo", "POH-poh", "pawpaw (papaya)", "sn_pawpaw",
      rule="pf = ‘pf’ said together, as in “cupful”"),
    L("R", "r", "ra", "rah", "a light, tapped ‘r’ — almost an ‘l’", "ruva", "ROO-vah", "flower", "flower"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sadza", "SAH-dzah", "sadza — thick maize porridge", "sn_sadza",
      rule="sh = ‘sh’ as in “shoe” · sv = a whistled ‘s’ — a Shona sound!"),
    L("T", "t", "ta", "tah", "‘t’ as in “stop” (no puff of air)", "tsamba", "TSAHM-bah", "letter (to post)", "envelope",
      rule="ts = ‘ts’ as in “cats”"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "uchi", "OO-chee", "honey", "honey", vowel=True),
    L("V", "v", "va", "vah", "a soft ‘v’ made with both lips; VH is the ‘v’ of “van”", "vhiri", "VEE-ree", "wheel", "sn_wheel",
      rule="v = a soft v with both lips · vh = v as in “van”"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "wachi", "WAH-chee", "watch, clock", "clock"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "muuyu", "moo-OO-yoo", "baobab tree", "sn_baobab", note=inside("Y", "muuyu")),
    L("Z", "z", "za", "zah", "‘z’ as in “zoo”", "zuva", "ZOO-vah", "sun", "sun",
      rule="zh = ‘s’ as in “measure” · zv = a whistled ‘z’ — a Shona sound!"),
]

LANG = build(dict(
    code="sn", folder="book-70-shona", series_no=70, isbn="", draft=True,
    name="Shona", native="chiShona", native_tr="chee-SHOH-nah", name_word="zita", write_word="nyora",
    title_native="Mavara angu ekutanga echiShona", title_letters="AaBbCc", belongs_native="Muridzi webhuku iri:",
    belongs_pic="sn_baobab", alphabet_native="mavara", numbers_native="nhamba", numbers_tr="NHAHM-bah",
    phrases_native="Mazwi ekutanga",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fonts(),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS,
    font_credit="Baloo 2",
    phon_feature="each letter’s Shona syllable row (ba be bi bo bu), the way Zimbabwean children learn to read",
    sections=[section(LETTERS, native="mavara", native_tr="mah-VAH-rah — “the letters”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Shona is written with <b>23 letters</b>: the English alphabet without <b>L</b>, <b>Q</b> and <b>X</b>
(they appear only in a few borrowed words). <b>C</b> is used only in <b>CH</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Read it as you say it</h3>Every Shona letter keeps its sound, so once you know the letters
you can read almost any word. Shona children learn to read in <b>syllables</b>: <i>ba be bi bo bu, cha che chi cho chu…</i></div>
<div class="box" style="margin:0.1in 0"><h3>Letters that team up</h3>Some sounds are written with two or three letters together:
<b>bh, ch, dh, mh, nh, ny, sh, sv, ts, vh, zh, zv</b>… You will meet them on the letter pages.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the syllable said a little more strongly: <i>MVOO-rah</i>. (Shona is really a "
        "tone language: some syllables are said higher, others lower.)",
        "<b>Plain b, d</b> are softer than in English: the air is pulled in a little. <b>bh, dh</b> are the ordinary English b and d.",
        "<b>sv</b> and <b>zv</b> are “whistled” s and z, said with rounded lips — try <i>svika</i> and <i>zvino</i>!",
        "Sounds follow standard Shona as taught in Zimbabwean schools."],
    phon_explain="The box marked <i>Shona syllables</i> shows how the letter is named in class and the row of syllables "
                 "Shona children chant when they learn to read (ba be bi bo bu), plus any letter team that changes its sound.",
    standard="standard Shona (the school language of Zimbabwe)",
    hello=[
        ("Who speaks it?", "More than <b>10 million people</b> speak Shona at home, and many more use it every day.<sup>³</sup>"),
        ("Where?", "Mostly in <b>Zimbabwe</b>, the land between the Zambezi and Limpopo rivers, and also in parts of <b>Mozambique</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, almost exactly as it sounds."),
        ("How many letters?", "<b>23 letters</b>, plus letter teams such as <b>ch, sh, sv, zv</b>."),
        ("Whistling words!", "Shona has “whistled” sounds, written <b>sv</b> and <b>zv</b>. Few languages in the world have them."),
        ("Did you know?", "The name <b>Zimbabwe</b> comes from Shona <i>dzimba dzemabwe</i>, “houses of stone”, after the great "
                          "stone walls built there long ago."),
    ],
    hello_pics=[("sn_baobab", {}), ("sn_pumpkin", {}), ("mosque", {})],
    map=region_map(frame=[[20.0, -30.0], [44.0, -6.0]],
                   points=dict(harare=[31.05, -17.83], mutare=[32.67, -18.97], masvingo=[30.83, -20.07], gweru=[29.82, -19.45]),
                   area=(30.8, -18.9, 150, 125),
                   cities=[("harare", "Harare", 14, 6, "start", False), ("mutare", "Mutare", 14, 8, "start", False),
                           ("masvingo", "Masvingo", 12, 18, "start", False), ("gweru", "Gweru", -14, 8, "end", False)],
                   label="ZIMBABWE", label_at=[30.8, -14.0], marker=[30.0, -19.0],
                   caption="The circle shows southern Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Shona is spoken in Harare, "
                          "Mutare, Masvingo and Gweru. The dashed line shows where most Shona families live.",
                   seas=[("Indian Ocean", 40.0, -25.0)], world_r=13),
    digits=[("0", "ziro", "ZEE-roh", "zero"), ("1", "poshi", "POH-shee", "one"), ("2", "piri", "PEE-ree", "two"),
            ("3", "tatu", "TAH-too", "three"), ("4", "ina", "EE-nah", "four"), ("5", "shanu", "SHAH-noo", "five"),
            ("6", "tanhatu", "tah-NHAH-too", "six"), ("7", "nomwe", "NOH-mweh", "seven"), ("8", "sere", "SEH-reh", "eight"),
            ("9", "pfumbamwe", "pfoom-BAH-mweh", "nine")],
    phrases=[("Assalaamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalaam", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Mhoroi!", "mhoh-ROH-ee", "Hello! (polite)"),
             ("Zita rangu ndi …", "ZEE-tah RAHN-goo ndee …", "My name is …"),
             ("Ndatenda", "ndah-TEHN-dah", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("amai · baba", "ah-MAH-ee · BAH-bah", "Mother · Father"),
             ("mukoma · munin'ina", "moo-KOH-mah · moo-NEE-ngee-nah", "Big brother or sister · Little brother or sister"),
             ("hongu · kwete", "HOHN-goo · KWEH-teh", "Yes · No"),
             ("Ndiri kudzidza chiShona!", "ndee-ree koo-DZEE-dzah chee-SHOH-nah", "I am learning Shona!")],
    cheer=("Mashallah! Waita zvakanaka!", "MAH-shah-lah! wah-EE-tah zvah-kah-NAH-kah!", "Well done, you did it well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Drafted without a native speaker. Check: the letter names used in Zimbabwean classrooms (given here as a, ba, cha…); "
                "the loanwords fasitera (window), kapu (cup), wachi (watch), popo (pawpaw), ziro (zero); the title "
                "“Mavara angu ekutanga echiShona” and “Muridzi webhuku iri:”; mukoma · munin'ina used for brother/sister; "
                "the cheer “Waita zvakanaka!”; and the capitals used as a stress guide in a tone language.",
    tiles="ABDMSZ", cover_pics=["sn_baobab", "sn_pumpkin", "sun", "mosque"], title_size=48,
    speakers_blurb="Shona is spoken by more than 10 million people, mostly in Zimbabwe.",
    sample_words=[("zuva", "ZOO-vah", "sun"), ("ruva", "ROO-vah", "flower"), ("muuyu", "moo-OO-yoo", "baobab tree")],
    keywords=["shona alphabet book for kids", "learn shona for children", "chishona coloring book",
              "zimbabwe kids activity book", "muslim kids activity book", "islamic coloring book for children",
              "shona english bilingual toddlers"],
))
