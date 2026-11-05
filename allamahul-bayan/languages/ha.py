# -*- coding: utf-8 -*-
"""Book 63 - Hausa (Boko, the Latin-script alphabet: 28 letters incl. Ɓ Ɗ Ƙ Ƴ, Sh, Ts). Allamahul Bayan Series. REVIEW DRAFT."""
from generic import build, section
from maps import region_map
from _afrolatin import afro_fonts, GLYPH_FONTS, FONT_CREDIT, maker

L = maker("Hausa name · syllables", ["a", "e", "i", "o", "u"])

LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "agogo", "a-go-go", "clock, watch", "clock", vowel=True),
    L("B", "b", "ba", "bah", "‘b’ as in “ball”", "buta", "boo-ta", "water kettle for wuduʼ", "ewer"),
    L("Ɓ", "ɓ", "ɓa", "bah (gulped)", "a ‘b’ said while gulping air <b>in</b> — a special Hausa sound", "ɓaure", "bow-reh", "fig, fig tree", "fig",
      rule="b = ball · ɓ = the same lips, but swallow the sound in"),
    L("C", "c", "ca", "chah", "‘ch’ as in “church” — never ‘k’ or ‘s’", "cokali", "cho-ka-lee", "spoon", "spoon"),
    L("D", "d", "da", "dah", "‘d’ as in “door”", "dabino", "da-bee-no", "dates, date palm", "dates"),
    L("Ɗ", "ɗ", "ɗa", "dah (gulped)", "a ‘d’ said while gulping air <b>in</b> — a special Hausa sound", "ɗaki", "da-kee", "room, little house", "house",
      rule="d = door · ɗ = the same tongue, but swallow the sound in"),
    L("E", "e", "e", "eh", "‘e’ as in “bed”, or ‘ay’ as in “say”", "zobe", "zo-beh", "ring", "ring", vowel=True,
      note="E hardly ever starts a Hausa word. Find it at the end of <i>zobe</i>!"),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "fure", "foo-reh", "flower", "flower"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "gishiri", "gee-shee-ree", "salt", "salt"),
    L("H", "h", "ha", "hah", "‘h’ as in “hat”", "hatsi", "hat-see", "grain (millet, guinea corn)", "paddy"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "itace", "ee-ta-cheh", "tree, wood", "tree", vowel=True),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "jirgin sama", "jeer-gin sa-ma", "aeroplane (“sky boat”)", "plane"),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "kwai", "kwai", "egg", "egg"),
    L("Ƙ", "ƙ", "ƙa", "kah (popped)", "a ‘k’ with a little pop in the throat — a special Hausa sound", "ƙofa", "ko-fa", "door", "door",
      rule="k = kite · ƙ = hold your breath, then pop the k"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "littafi", "lit-ta-fee", "book", "book", args=dict(left="A B Ɓ", right="C D Ɗ")),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "masallaci", "ma-sal-la-chee", "mosque", "mosque"),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "naʼura", "na-oo-ra", "machine", "gears"),
    L("O", "o", "o", "oh", "‘o’ as in “go” (short and pure)", "kogi", "ko-gee", "river", "waves", vowel=True,
      note="O hardly ever starts a Hausa word. Find it inside <i>kogi</i>!"),
    L("R", "r", "ra", "rah", "a tapped or rolled ‘r’", "rana", "ra-na", "sun", "sun"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sabulu", "sa-boo-loo", "soap", "soap"),
    L("Sh", "sh", "sha", "shah", "‘sh’ as in “ship”", "shinkafa", "sheen-ka-fa", "rice", "rice",
      note="<b>Sh</b> is two letters that make one sound — Hausa counts it as one letter."),
    L("T", "t", "ta", "tah", "‘t’ as in “tap”", "tumatir", "too-ma-teer", "tomato", "tomato"),
    L("Ts", "ts", "tsa", "tsah (popped)", "‘ts’ as in “cats”, with a sharp pop — a special Hausa sound", "tsani", "tsa-nee", "ladder", "ladder",
      note="<b>Ts</b> is two letters that make one sound — Hausa counts it as one letter."),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "ruwa", "roo-wa", "water", "water", vowel=True,
      note="Few words you can draw start with U. Find it inside <i>ruwa</i>!"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "wata", "wa-ta", "moon", "moon"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "yalo", "ya-lo", "garden eggs (small round eggplants)", "ha_yalo"),
    L("Ƴ", "ƴ", "ƴa", "yah (squeezed)", "a ‘y’ squeezed in the throat — a special Hausa sound", "ƴaƴan itace", "yah-yan ee-ta-cheh",
      "fruits (“children of the tree”)", "basket", rule="Also written <b>ʼY ʼy</b> (in Niger and in many books): <i>ʼyaʼyan itace</i>"),
    L("Z", "z", "za", "zah", "‘z’ as in “zoo”", "zuma", "zoo-ma", "honey", "honey"),
]

LANG = build(dict(
    code="ha", folder="book-63-hausa", series_no=63, isbn="", draft=True,
    name="Hausa", native="Hausa", native_tr="how-sa", name_word="suna", write_word="rubuta",
    title_native="Littafin haruffan Hausa na farko", title_letters="AaƁɓƘƙ", belongs_native="Wannan littafin na",
    belongs_pic="dates", alphabet_native="haruffa", numbers_native="lambobi", numbers_tr="lam-bo-bee",
    phrases_native="Kalmomin farko",
    fonts=afro_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS, font_credit=FONT_CREDIT,
    phon_feature="each letter’s Hausa name and its syllables (ba, be, bi, bo, bu)",
    sections=[section(LETTERS, native="haruffan Hausa", native_tr="ha-roof-fan how-sa — “the Hausa letters”",
                      chart_cols=7, warmup_cols=7,
                      intro_html="""<p>Hausa written in Latin letters is called <b>Boko</b>. It has <b>28 letters</b> in this book, with four special ones:
<b>Ɓ Ɗ Ƙ Ƴ</b> — look for the little hooks!</p>
<div class="box" style="margin:0.1in 0"><h3>Hooked letters, special sounds</h3><b>ɓ</b> and <b>ɗ</b> are said while gulping air in; <b>ƙ</b>, <b>ts</b>
and <b>ƴ</b> are “popped” in the throat. The hook tells you: this is not the plain letter!</div>
<div class="box" style="margin:0.1in 0"><h3>Two letters, one sound</h3><b>Sh</b> and <b>Ts</b> are written with two letters but count as one.
The little mark <b>ʼ</b> (as in <i>naʼura</i>, <i>aʼa</i>) is a short catch in the voice.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ɓɓ</b>. Color both!</div>""")],
    sound_notes=[
        "Hausa sound guides here have <b>no capitals</b>: Hausa does not stress syllables like English. Say every syllable evenly.",
        "Hausa is a <b>tone</b> language (the voice goes high or low), and it has long and short vowels — but neither is written in everyday "
        "spelling. Listen to a Hausa speaker to hear them!",
        "<b>(gulped)</b> means the sound is swallowed in (ɓ, ɗ); <b>(popped)</b> means a little pop in the throat (ƙ, ts); "
        "<b>(squeezed)</b> means a ‘y’ squeezed in the throat (ƴ).",
        "<b>c</b> always says ‘ch’, and <b>g</b> is always hard as in “go”."],
    phon_explain="The box marked <i>Hausa name · syllables</i> shows the letter’s name and its syllable row "
                 "(ba, be, bi, bo, bu) — the way Hausa children learn to read Boko.",
    standard="Standard Hausa as spoken in Kano and written in Nigeria",
    hello=[
        ("Who speaks it?", "About <b>80 million people</b> speak Hausa — many of them as a second language for trade and travel.<sup>³</sup>"),
        ("Where?", "In northern <b>Nigeria</b> and southern <b>Niger</b>, and in market towns all across West Africa, from Ghana to Sudan."),
        ("How is it written?", "In <b>Boko</b>, the Latin alphabet, from <b>left to right</b>. For hundreds of years it has also been written "
                               "in <b>Ajami</b> — Arabic letters adapted for Hausa — still used in many Qurʼan schools."),
        ("How many letters?", "<b>28 letters</b> in this book, with the special hooked letters <b>Ɓ Ɗ Ƙ Ƴ</b> and the pairs <b>Sh</b> and <b>Ts</b>."),
        ("Up and down", "Hausa is a <b>tone</b> language: the same letters can mean different things when your voice goes up or down. "
                        "But tones are not written — you learn them by listening!"),
        ("Did you know?", "Hausa has many words from Arabic: <i>littafi</i> (book), <i>masallaci</i> (mosque), <i>alƙalami</i> (pen) and "
                          "<i>lokaci</i> (time)."),
    ],
    hello_pics=[("ewer", {}), ("dates", {}), ("mosque", {})],
    map=region_map(frame=[[1.0, 3.5], [16.0, 18.5]],
                   points=dict(kano=[8.52, 12.00], sokoto=[5.24, 13.06], zaria=[7.72, 11.08], maradi=[7.10, 13.50], zinder=[8.99, 13.80]),
                   area=(7.6, 12.4, 330, 200), area_rot=-5,
                   cities=[("kano", "Kano", 14, 8, "start", False), ("sokoto", "Sokoto", -14, 8, "end", False),
                           ("zaria", "Zaria", -14, 12, "end", False), ("maradi", "Maradi", -14, -4, "end", False),
                           ("zinder", "Zinder", 14, -2, "start", False)],
                   label="WEST AFRICA", label_at=[3.0, 16.8], marker=[8.0, 12.0],
                   caption="The circle shows Hausaland, in West Africa, on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> (or <b>yellow</b> for the desert in the north) · the ocean <b>blue</b>. "
                          "<b>Find it:</b> Hausa is spoken in Kano, Zaria, Sokoto, Maradi, Zinder and far beyond. The dashed line shows "
                          "where most Hausa speakers live.",
                   seas=[("Gulf of Guinea", 4.0, 3.8)], world_r=14),
    digits=[("0", "sifili", "see-fee-lee", "zero"), ("1", "ɗaya", "da-ya", "one"), ("2", "biyu", "bee-yoo", "two"),
            ("3", "uku", "oo-koo", "three"), ("4", "huɗu", "hoo-doo", "four"), ("5", "biyar", "bee-yar", "five"),
            ("6", "shida", "shee-da", "six"), ("7", "bakwai", "bak-wai", "seven"), ("8", "takwas", "tak-was", "eight"),
            ("9", "tara", "ta-ra", "nine")],
    phrases=[("Assalamu alaikum", "as-sa-la-moo a-lai-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wa a-lai-koom as-sa-lam", "And peace be upon you (the reply)"),
             ("Sannu!", "san-noo", "Hello!"),
             ("Sunana …", "soo-na-na …", "My name is …"),
             ("Na gode", "na go-deh", "Thank you"),
             ("Jazakallahu khairan", "ja-za-kal-la-hoo khai-ran", "May Allah reward you with good"),
             ("uwa · uba", "oo-wa · oo-ba", "Mother · Father"),
             ("ɗanʼuwa · ƴarʼuwa", "dan-oo-wa · yar-oo-wa", "Brother · Sister"),
             ("i · aʼa", "ee · a-a", "Yes · No"),
             ("Ina koyon Hausa!", "ee-na ko-yon how-sa", "I am learning Hausa!")],
    cheer=("Mashallah! Madalla!", "ma-shal-la! ma-dal-la!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B Ɓ", right="C D Ɗ"),
    review_note="Check the letter names (a, ba, ɓa, ca…: some teachers use bi, ɓi, ci…), and the words <i>ɓaure</i> (fig), "
                "<i>naʼura</i> (machine) for N, <i>hatsi</i> (grain) for H, <i>ƴaƴan itace</i> (fruits) for Ƴ and the Nigerian "
                "spelling ƴ vs. Niger’s ʼy. The sound guides use plain English spellings and leave tone and vowel length unmarked.",
    tiles="AƁƊƘƳZ", cover_pics=["dates", "ewer", "mosque", "flower"],
    speakers_blurb="Hausa is spoken by about 80 million people in Nigeria, Niger and across West Africa.",
    sample_words=[("rana", "ra-na", "sun"), ("zuma", "zoo-ma", "honey"), ("ƙofa", "ko-fa", "door")],
    keywords=["hausa alphabet book for kids", "learn hausa for children", "hausa boko coloring book",
              "hausa letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual hausa english toddlers"],
))
