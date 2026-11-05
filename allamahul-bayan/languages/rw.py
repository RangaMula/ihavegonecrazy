# -*- coding: utf-8 -*-
"""Book 71 - Kinyarwanda (Ikinyarwanda, Latin script, 23 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Aa"), as in languages/es.py."""
from generic import build, section, fontset
from maps import region_map
from _sn_rw_ln_wo import fonts, GLYPH_FONTS, maker, inside

L = maker("Kinyarwanda syllables", "a e i o u")


def pre(cap, parts):
    """Most Kinyarwanda nouns begin with a little vowel (i-, u-, a-): show where the letter sits."""
    return f"The word begins with a little vowel. Find <b>{cap.lower()}</b> right after it: <i>{parts}</i>"


LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "agaseke", "ah-gah-SEH-keh", "woven basket with a lid", "basket", vowel=True),
    L("B", "b", "ba", "bah", "a soft ‘b’, the lips almost touching", "ibigori", "ee-bee-GOH-ree", "maize cobs (corn)", "corn",
      note=pre("B", "i · bi · go · ri")),
    L("C", "c", "ca", "chah", "‘ch’ as in “church”", "igicu", "ee-gee-CHOO", "cloud", "clouds", note=pre("C", "i · gi · cu")),
    L("D", "d", "da", "dah", "‘d’ as in “day”", "idirishya", "ee-dee-REE-shyah", "window", "window", note=pre("D", "i · di · ri · shya")),
    L("E", "e", "e", "eh", "‘e’ as in “bed”", "inyenyeri", "ee-nyeh-NYEH-ree", "star", "star", vowel=True, note=inside("E", "inyenyeri")),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "urufunguzo", "oo-roo-foon-GOO-zoh", "key", "rw_key", note=pre("F", "u · ru · fu · ngu · zo")),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "igiti", "ee-GEE-tee", "tree", "tree", note=pre("G", "i · gi · ti")),
    L("H", "h", "ha", "hah", "a soft, breathy ‘h’ as in “hat”", "ihema", "ee-HEH-mah", "tent", "rw_tent", note=pre("H", "i · he · ma")),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "inzu", "EEN-zoo", "house", "house", vowel=True),
    L("J", "j", "ja", "jah", "‘j’ as in “jam”", "ibijumba", "ee-bee-JOOM-bah", "sweet potatoes", "potato", note=pre("J", "i · bi · ju · mba")),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "ikaramu", "ee-kah-RAH-moo", "pen, pencil", "pen", note=pre("K", "i · ka · ra · mu")),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "umusozi", "oo-moo-SOH-zee", "hill, mountain", "mountain", note=pre("M", "u · mu · so · zi")),
    L("N", "n", "na", "nah", "‘n’ as in “net”", "inanasi", "ee-nah-NAH-see", "pineapple", "pineapple", note=pre("N", "i · na · na · si"),
      rule="ny = ‘ny’ as in “canyon”"),
    L("O", "o", "o", "oh", "‘o’ as in “for” — short and pure", "inkono", "een-KOH-noh", "cooking pot", "pot", vowel=True,
      note=inside("O", "inkono")),
    L("P", "p", "pa", "pah", "‘p’ as in “pen”", "umupira", "oo-moo-PEE-rah", "ball", "ball", note=pre("P", "u · mu · pi · ra")),
    L("R", "r", "ra", "rah", "a light, tapped ‘r’ — almost an ‘l’", "urugi", "oo-ROO-gee", "door", "door", note=pre("R", "u · ru · gi")),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "isaha", "ee-SAH-hah", "clock, watch", "clock", note=pre("S", "i · sa · ha"),
      rule="sh = ‘sh’ as in “shoe”"),
    L("T", "t", "ta", "tah", "‘t’ as in “top”", "umutaka", "oo-moo-TAH-kah", "umbrella", "umbrella", note=pre("T", "u · mu · ta · ka")),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "ubuki", "oo-BOO-kee", "honey", "honey", vowel=True),
    L("V", "v", "va", "vah", "‘v’ as in “van”", "imvura", "eem-VOO-rah", "rain", "raincloud", note=pre("V", "i · mvu · ra")),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "umwembe", "oo-MWEHM-beh", "mango", "mango", note=pre("W", "u · mwe · mbe")),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "icyayi", "ee-CHAH-yee", "tea", "teacup", note=pre("Y", "i · cya · yi"),
      rule="cy = ‘ch’ as in “church”"),
    L("Z", "z", "za", "zah", "‘z’ as in “zoo”", "izuba", "ee-ZOO-bah", "sun", "sun", note=pre("Z", "i · zu · ba")),
]

LANG = build(dict(
    code="rw", folder="book-71-kinyarwanda", series_no=71, isbn="", draft=True,
    name="Kinyarwanda", native="Ikinyarwanda", native_tr="ee-kee-nyah-RWAHN-dah", name_word="izina", write_word="andika",
    title_native="Inyuguti zanjye za mbere z’Ikinyarwanda", title_letters="AaBbCc", belongs_native="Iki gitabo ni icya",
    belongs_pic="basket", alphabet_native="inyuguti", numbers_native="imibare", numbers_tr="ee-mee-BAH-reh",
    phrases_native="Amagambo ya mbere",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fonts(),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=GLYPH_FONTS,
    font_credit="Baloo 2",
    phon_feature="each letter’s Kinyarwanda syllable row (ba be bi bo bu), the way Rwandan children learn to read",
    sections=[section(LETTERS, native="inyuguti", native_tr="ee-nyoo-GOO-tee — “the letters”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Kinyarwanda is written with <b>23 letters</b>: the English alphabet without <b>L</b>, <b>Q</b> and <b>X</b>
(they appear only in a few borrowed words).</p>
<div class="box" style="margin:0.1in 0"><h3>A little vowel in front</h3>Most Kinyarwanda names of things begin with a small vowel:
<b>i-</b>, <b>u-</b> or <b>a-</b>: <i>inzu</i> (house), <i>ubuki</i> (honey), <i>amazi</i> (water). So on many pages you will
find the letter <b>right after</b> that little vowel: <i>i·<b>g</b>iti</i> (tree).</div>
<div class="box" style="margin:0.1in 0"><h3>Read in syllables</h3>Rwandan children learn to read syllable by syllable:
<i>ba be bi bo bu, ca ce ci co cu…</i> Letters team up too: <b>cy, ny, sh, shy, mb, nz</b>…</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the syllable said a little more strongly: <i>ee-GEE-tee</i>. "
        "(Kinyarwanda is really a tone language: some syllables are said higher, others lower.)",
        "<b>c</b> always says ‘ch’ as in “church”, and <b>cy</b> says it too.",
        "<b>r</b> is a light tap of the tongue, close to an ‘l’.",
        "Sounds follow standard Kinyarwanda as taught in Rwandan schools."],
    phon_explain="The box marked <i>Kinyarwanda syllables</i> shows how the letter is named in class and the row of syllables "
                 "Rwandan children chant when they learn to read (ba be bi bo bu). Under it, the word is split into syllables so "
                 "you can find the letter after the little vowel at the front.",
    standard="standard Kinyarwanda (Rwanda)",
    hello=[
        ("Who speaks it?", "About <b>12 million people</b> speak Kinyarwanda — almost everyone in Rwanda.<sup>³</sup>"),
        ("Where?", "In <b>Rwanda</b>, a small green country in the middle of Africa, and by families in nearby countries."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, almost exactly as it sounds."),
        ("How many letters?", "<b>23 letters</b>, plus letter teams such as <b>cy, ny, sh, shy</b>."),
        ("A thousand hills", "Rwanda is called <i>igihugu cy’imisozi igihumbi</i>, “the land of a thousand hills”."),
        ("Did you know?", "Rwandan weavers make tall baskets with pointed lids called <b>agaseke</b>, from grass and sisal, "
                          "in beautiful zigzag patterns."),
    ],
    hello_pics=[("basket", {}), ("mountain", {}), ("mosque", {})],
    map=region_map(frame=[[25.0, -12.0], [42.0, 5.0]],
                   points=dict(kigali=[30.06, -1.95], huye=[29.74, -2.60], musanze=[29.63, -1.50]),
                   area=(29.9, -2.0, 75, 70),
                   cities=[("kigali", "Kigali", 14, 6, "start", False), ("huye", "Huye", 12, 16, "start", False),
                           ("musanze", "Musanze", -12, -6, "end", False)],
                   label="RWANDA", label_at=[29.9, 0.3], marker=[30.0, -2.0],
                   caption="The circle shows the middle of Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Kinyarwanda is spoken all over "
                          "Rwanda: in the capital Kigali, in Huye and in Musanze near the volcanoes. The dashed line shows Rwanda.",
                   seas=[("Indian Ocean", 40.6, -10.2)], world_r=13),
    digits=[("0", "zeru", "ZEH-roo", "zero"), ("1", "rimwe", "REE-mweh", "one"), ("2", "kabiri", "kah-BEE-ree", "two"),
            ("3", "gatatu", "gah-TAH-too", "three"), ("4", "kane", "KAH-neh", "four"), ("5", "gatanu", "gah-TAH-noo", "five"),
            ("6", "gatandatu", "gah-tahn-DAH-too", "six"), ("7", "karindwi", "kah-REEN-dwee", "seven"),
            ("8", "umunani", "oo-moo-NAH-nee", "eight"), ("9", "icyenda", "ee-CHEHN-dah", "nine")],
    phrases=[("Assalamu alaykum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaykum assalam", "wah ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("Muraho!", "moo-RAH-hoh", "Hello!"),
             ("Nitwa …", "NEE-twah …", "My name is …"),
             ("Murakoze", "moo-rah-KOH-zeh", "Thank you"),
             ("Jazakallahu khayran", "jah-zah-KAH-lah-hoo KHAY-rahn", "May Allah reward you with good"),
             ("mama · data", "MAH-mah · DAH-tah", "Mother · Father"),
             ("musaza · mushiki", "moo-SAH-zah · moo-SHEE-kee", "Brother · Sister"),
             ("yego · oya", "YEH-goh · OH-yah", "Yes · No"),
             ("Ndiga Ikinyarwanda!", "NDEE-gah ee-kee-nyah-RWAHN-dah", "I am learning Kinyarwanda!")],
    cheer=("Mashallah! Wakoze neza!", "MAH-shah-lah! wah-KOH-zeh NEH-zah!", "Well done, you did it well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Drafted without a native speaker. Check: the letter names used in Rwandan classrooms (given here as a, ba, ca…); "
                "the syllable splits shown under each word; the title “Inyuguti zanjye za mbere z’Ikinyarwanda” and "
                "“Iki gitabo ni icya”; musaza · mushiki for brother · sister (strictly, the brother of a girl and the sister of a boy); "
                "“Ndiga Ikinyarwanda!”; zeru for zero; and the capitals used as a stress guide in a tone language.",
    tiles="ABCIUZ", cover_pics=["basket", "mountain", "sun", "mosque"], title_size=44,
    speakers_blurb="Kinyarwanda is spoken by about 12 million people in Rwanda, the land of a thousand hills.",
    sample_words=[("izuba", "ee-ZOO-bah", "sun"), ("inzu", "EEN-zoo", "house"), ("agaseke", "ah-gah-SEH-keh", "woven basket")],
    keywords=["kinyarwanda alphabet book for kids", "learn kinyarwanda for children", "rwanda coloring book",
              "kinyarwanda english bilingual", "muslim kids activity book", "islamic coloring book for children",
              "african language alphabet workbook"],
))
