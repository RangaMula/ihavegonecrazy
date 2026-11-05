# -*- coding: utf-8 -*-
"""Book 58 - Tamazight (Standard Moroccan Amazigh, Neo-Tifinagh script as standardised by IRCAM, 33 letters).
Allamahul Bayan Series. REVIEW DRAFT - every word needs checking by a native speaker.
Each word is shown in Tifinagh, in the official Latin transcription (IRCAM), with an easy English sound guide."""
from generic import build, letter, section
from maps import region_map

PH = "Latin letter · kind of sound"
HEAVY = "a <b>heavy</b> (emphatic) sound: say it with the back of the tongue raised, so the vowels next to it sound deeper"


def Z(ch, name, name_tr, lat, kind, sound, word, wlat, easy, meaning, pic, args=None, note=None, extra=None):
    phon = (f'<div style="font-size:20pt;line-height:1.5"><span class="ntd">{ch}</span> = <b>{lat}</b></div>'
            f'<div class="small">{kind}</div>'
            + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else ""))
    if note is None and not word.startswith(ch):
        note = (f'Find <span class="nt">{ch}</span> inside <span class="nt">{word}</span>! Most Tamazight nouns begin with '
                f'a vowel (<span class="nt">ⴰ ⵉ ⵓ</span>) or with <span class="nt">ⵜ</span>.')
    return letter(ch, name, name_tr, sound, word, f"<b>{wlat}</b> · {easy}", meaning, pic, phon, PH, args, note)


V, C_, E_ = "a vowel", "a consonant", "a heavy (emphatic) consonant"
LAB = "a consonant with rounded lips: the little mark <span class='nt'>ⵯ</span> means “round your lips”"

LETTERS = [
    Z("ⴰ", "ⵢⴰ", "ya", "a", V, "‘a’ as in “father”", "ⴰⴷⵔⴰⵔ", "adrar", "ah-drahr", "mountain", "mountain"),
    Z("ⴱ", "ⵢⴰⴱ", "yab", "b", C_, "‘b’ as in “ball”", "ⴰⴱⵔⵉⴷ", "abrid", "ah-breed", "road, path", "zgh_road"),
    Z("ⴳ", "ⵢⴰⴳ", "yag", "g", C_, "‘g’ as in “go”", "ⴰⴳⵔⵉⵙ", "agris", "ah-grees", "ice", "ice"),
    Z("ⴳⵯ", "ⵢⴰⴳⵯ", "yagʷ", "gʷ", LAB, "‘gw’ as in “Gwen”: a ‘g’ said with rounded lips", "ⴰⵙⴳⴳⵯⴰⵙ", "asggʷas", "as-ggwahs",
      "year (and its seasons)", "seasons"),
    Z("ⴷ", "ⵢⴰⴷ", "yad", "d", C_, "‘d’ as in “dog”", "ⴰⴷⵍⵉⵙ", "adlis", "ad-lees", "book", "book",
      args=dict(left="ⴰ ⴱ ⴳ", right="ⴷ ⴹ ⴻ")),
    Z("ⴹ", "ⵢⴰⴹ", "yaḍ", "ḍ", E_, "a heavy ‘d’ — " + HEAVY, "ⴰⴹⵉⵍ", "aḍil", "ah-ḍeel", "grapes", "grapes"),
    Z("ⴻ", "ⵢⴻⵢ", "yey", "e", "a very short vowel", "a tiny, quick ‘uh’ like the ‘a’ in “about”", "ⴰⵣⴻⵎⵎⵓⵔ", "azemmur",
      "ah-zuh-moor", "olives", "olive",
      note='<span class="nt">ⴻ</span> never starts a word. Find it in <span class="nt">ⴰⵣⴻⵎⵎⵓⵔ</span>! In standard spelling this '
           'short vowel is usually not written: <span class="nt">ⴰⵣⵎⵎⵓⵔ</span>.'),
    Z("ⴼ", "ⵢⴰⴼ", "yaf", "f", C_, "‘f’ as in “fan”", "ⵜⴰⴼⵓⴽⵜ", "tafukt", "tah-fookt", "sun", "sun"),
    Z("ⴽ", "ⵢⴰⴽ", "yak", "k", C_, "‘k’ as in “kite”", "ⵜⵉⴽⵉⵏⵜ", "tikint", "tee-keent", "cooking pot", "pot"),
    Z("ⴽⵯ", "ⵢⴰⴽⵯ", "yakʷ", "kʷ", LAB, "‘kw’ as in “queen”: a ‘k’ said with rounded lips", "ⴰⴽⵯⴼⴰⵢ", "akʷfay", "akw-fai",
      "milk", "zgh_milk"),
    Z("ⵀ", "ⵢⴰⵀ", "yah", "h", C_, "‘h’ as in “hat”", "ⴰⵀⴰⵔⴽⵓⵙ", "aharkus", "ah-har-koos", "slipper, sandal", "zgh_babouche"),
    Z("ⵃ", "ⵢⴰⵃ", "yaḥ", "ḥ", C_, "a strong, breathy ‘h’ from the throat, like Arabic <span class='ar'>ح</span>", "ⵍⵃⵉⵊⵊ", "lḥijj",
      "l-ḥeejj", "Hajj, the journey to the Kaaba in Makkah", "kaaba", extra="Used mostly in words from Arabic."),
    Z("ⵄ", "ⵢⴰⵄ", "yaɛ", "ɛ", C_, "a squeezed sound deep in the throat, like Arabic <span class='ar'>ع</span>", "ⵍⵄⵉⴷ", "lɛid",
      "l-ɛeed", "Eid, the festival", "eid", extra="Used mostly in words from Arabic."),
    Z("ⵅ", "ⵢⴰⵅ", "yax", "x", C_, "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "ⴰⵅⵅⴰⵎ", "axxam",
      "akh-khahm", "house", "house"),
    Z("ⵇ", "ⵢⴰⵇ", "yaq", "q", C_, "a ‘k’ said far back in the throat, like Arabic <span class='ar'>ق</span>", "ⵍⵇⵓⵔⵄⴰⵏ", "lqurɛan",
      "l-qur-ɛaan", "the Qur’an", "zgh_rehal"),
    Z("ⵉ", "ⵢⵉ", "yi", "i", V, "‘ee’ as in “see”", "ⵉⵜⵔⵉ", "itri", "ee-tree", "star", "star"),
    Z("ⵊ", "ⵢⴰⵊ", "yaj", "j", C_, "‘j’ as in “jam” (in some places ‘zh’, like the ‘s’ in “measure”)", "ⴰⵊⵊⵉⴳ", "ajjig", "aj-jeeg",
      "flower", "flower"),
    Z("ⵍ", "ⵢⴰⵍ", "yal", "l", C_, "‘l’ as in “lamp”", "ⵍⵍⵓⵃ", "lluḥ", "l-looḥ", "wooden board for learning to write", "zgh_slate"),
    Z("ⵎ", "ⵢⴰⵎ", "yam", "m", C_, "‘m’ as in “moon”", "ⴰⵎⴰⵏ", "aman", "ah-mahn", "water", "water"),
    Z("ⵏ", "ⵢⴰⵏ", "yan", "n", C_, "‘n’ as in “net”", "ⴰⵏⵓ", "anu", "ah-noo", "well (for water)", "well"),
    Z("ⵓ", "ⵢⵓ", "yu", "u", V, "‘oo’ as in “moon”", "ⵓⵔⵜⵉ", "urti", "oor-tee", "garden, orchard", "tree"),
    Z("ⵔ", "ⵢⴰⵔ", "yar", "r", C_, "a tapped ‘r’ — flick the tongue once", "ⴰⵔⴳⴰⵏ", "argan", "ar-gahn",
      "argan tree (it grows only in Morocco)", "zgh_argan"),
    Z("ⵕ", "ⵢⴰⵕ", "yaṛ", "ṛ", E_, "a heavy ‘r’ — " + HEAVY, "ⵕⵎⴹⴰⵏ", "ṛmḍan", "r-ma-ḍahn", "Ramadan, the month of fasting", "iftar"),
    Z("ⵖ", "ⵢⴰⵖ", "yaɣ", "ɣ", C_, "a soft gargled ‘gh’, like the French ‘r’ in “Paris”", "ⴰⵖⵔⵓⵎ", "aɣrum", "ah-ghroom", "bread", "roti"),
    Z("ⵙ", "ⵢⴰⵙ", "yas", "s", C_, "‘s’ as in “sun”", "ⵜⵉⵙⵏⵜ", "tisnt", "tee-sunt", "salt", "salt", args=dict(label="ⵜⵉⵙⵏⵜ")),
    Z("ⵚ", "ⵢⴰⵚ", "yaṣ", "ṣ", E_, "a heavy ‘s’ — " + HEAVY, "ⵚⵚⴰⴱⵓⵏ", "ṣṣabun", "ṣ-ṣah-boon", "soap", "soap"),
    Z("ⵛ", "ⵢⴰⵛ", "yac", "c", C_, "‘sh’ as in “shoe” (the Latin letter c always says ‘sh’)", "ⵜⴰⵛⵟⵟⴰⴱⵜ", "tacṭṭabt", "tash-ṭṭahbt",
      "broom", "broom"),
    Z("ⵜ", "ⵢⴰⵜ", "yat", "t", C_, "‘t’ as in “top”", "ⵜⵉⵢⵏⵉ", "tiyni", "teey-nee", "dates", "dates"),
    Z("ⵟ", "ⵢⴰⵟ", "yaṭ", "ṭ", E_, "a heavy ‘t’ — " + HEAVY, "ⵟⵟⴰⵊⵉⵏ", "ṭṭajin", "ṭ-ṭah-jeen", "tagine, a clay cooking pot", "zgh_tagine"),
    Z("ⵡ", "ⵢⴰⵡ", "yaw", "w", "a half-vowel", "‘w’ as in “water”", "ⵜⴰⵡⵡⵓⵔⵜ", "tawwurt", "taw-woort", "door", "door"),
    Z("ⵢ", "ⵢⴰⵢ", "yay", "y", "a half-vowel", "‘y’ as in “yes”", "ⴰⵢⵢⵓⵔ", "ayyur", "ay-yoor", "moon", "moon"),
    Z("ⵣ", "ⵢⴰⵣ", "yaz", "z", C_, "‘z’ as in “zoo”", "ⵜⴰⵣⴰⵔⵜ", "tazart", "tah-zart", "figs", "fig"),
    Z("ⵥ", "ⵢⴰⵥ", "yaẓ", "ẓ", E_, "a heavy ‘z’ — " + HEAVY, "ⵜⴰⵥⴰⵍⵍⵉⵜ", "taẓallit", "tah-ẓal-leet", "prayer (salah)", "prayermat"),
]

FONTS = [("Tifinagh Bold", 800, "normal", "noto-sans-tifinagh-emboldened-tifinagh-800-normal.woff2", None),
         ("Noto Sans Tifinagh", 400, "normal", "noto-sans-tifinagh-tifinagh-400-normal.woff2", None),
         ("Noto Sans Tifinagh", 700, "normal", "noto-sans-tifinagh-tifinagh-400-normal.woff2", None)]
# Latin transcription letters ɣ ɛ ʷ are missing from Nunito: borrow them from Noto Sans (latin-ext) for that range only.
IPA = "U+0250-02BA"
FONTS += [("Nunito", w, st, f"noto-sans-latin-ext-{w}-normal.woff2", IPA) for w in (400, 700, 800) for st in ("normal", "italic")]

LANG = build(dict(
    code="zgh", folder="book-58-tamazight", series_no=58, isbn="", draft=True,
    name="Tamazight", native="ⵜⴰⵎⴰⵣⵉⵖⵜ", native_tr="tamaziɣt (tah-mah-zeeght)", name_word="ⵉⵙⵎ · ism", write_word="ⴰⵔⵓ · aru",
    title_native="ⴰⴷⵍⵉⵙ ⵉⵏⵓ ⵏ ⵜⵉⴼⵉⵏⴰⵖ", title_letters="ⴰⴱⴳⴷⵣⵥ", belongs_native="ⴰⴷⵍⵉⵙ ⴰⴷ ⵉⵏⵓ",
    belongs_pic="zgh_argan", alphabet_native="ⵜⵉⴼⵉⵏⴰⵖ", numbers_native="ⵉⵎⴹⴰⵏ", numbers_tr="imḍan",
    phrases_native="ⵜⵉⴳⵓⵔⵉⵡⵉⵏ ⵜⵉⵎⵣⵡⵓⵔⴰ",
    fonts=FONTS, disp_family="Tifinagh Bold", text_family="Noto Sans Tifinagh",
    glyph_font=["noto-sans-tifinagh-emboldened-tifinagh-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Tifinagh (and an emboldened copy of it for the big letters), Baloo 2",
    subtitle="A Coloring Book to Learn, Trace & Say the 33 Tifinagh Letters with English Phonetics",
    phon_feature="each letter’s Latin transcription (ⴱ = b, ⵖ = ɣ, ⵛ = c…)",
    sections=[section(LETTERS, title="The Tifinagh Letters", native="ⵜⵉⴼⵉⵏⴰⵖ", native_tr="tifinaɣ (tee-fee-naagh) — “the letters”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Tamazight is written in <b>Tifinagh</b>, from <b>left to right</b>, like English. Morocco’s Royal Institute of
Amazigh Culture (IRCAM) set out this alphabet of <b>33 letters</b> for schools.</p>
<div class="box" style="margin:0.1in 0"><h3>Shapes you already know</h3>Tifinagh letters are made of simple shapes: circles, lines, dots and
crosses. <span class="ntd" style="font-size:20pt">ⵔ ⵉ ⵜ ⵙ ⵍ ⴰ</span> — can you see the circle, the line, the cross?</div>
<div class="box" style="margin:0.1in 0"><h3>Letters say “ya…”</h3>The name of a consonant is <b>ya</b> + its sound:
<span class="ntd" style="font-size:18pt">ⴱ</span> is <i>yab</i>, <span class="ntd" style="font-size:18pt">ⵎ</span> is <i>yam</i>.
There are four vowels: <span class="ntd" style="font-size:18pt">ⴰ ⵉ ⵓ ⴻ</span> (<i>a, i, u, e</i>).</div>
<div class="box"><h3>Heavy letters and round lips</h3>Five letters are “heavy” (emphatic):
<span class="ntd" style="font-size:18pt">ⴹ ⵕ ⵚ ⵟ ⵥ</span> sound deeper than <span class="ntd" style="font-size:18pt">ⴷ ⵔ ⵙ ⵜ ⵣ</span>.
The little mark <span class="ntd" style="font-size:18pt">ⵯ</span> means “round your lips”: <span class="ntd" style="font-size:18pt">ⴳⵯ ⴽⵯ</span>.</div>""")],
    sound_notes=[
        "Every word is shown three ways: in <b>Tifinagh</b>, in the official <b>Latin transcription</b> (in bold), and in an "
        "<b>easy English sound guide</b>: <i><b>aman</b> · ah-mahn</i>.",
        "<b>A dot under a letter</b> (<i>ḍ ṛ ṣ ṭ ẓ</i>) marks a heavy (emphatic) sound; <i>ḥ</i> and <i>ɛ</i> are throat sounds from Arabic.",
        "<b>ɣ</b> is a soft gargled ‘gh’; <b>x</b> is a scratchy ‘kh’; <b>c</b> says ‘sh’; <b>ʷ</b> means rounded lips (<i>gʷ, kʷ</i>).",
        "<b>Doubled letters</b> (<i>tawwurt, ajjig</i>) are held a little longer. <b>e</b> is a tiny ‘uh’.",
        "Words follow <b>Standard Moroccan Amazigh</b>; many of them are also used in Tashelhit, Central Atlas Tamazight or Tarifit."],
    phon_explain="The third box shows the <b>Latin letter</b> that IRCAM uses to write the same sound (<span class='nt'>ⵛ</span> = <i>c</i>) "
                 "and what kind of sound it is: a vowel, a consonant, a heavy (emphatic) consonant or a rounded-lips letter.",
    standard="Standard Moroccan Amazigh (IRCAM)",
    hello=[
        ("Who speaks it?", "About <b>10 million people</b> in Morocco speak a Tamazight language at home: <b>Tashelhit</b>, "
                           "<b>Central Atlas Tamazight</b> or <b>Tarifit</b>.<sup>³</sup>"),
        ("Where?", "In Morocco’s <b>Atlas</b> and <b>Rif</b> mountains, the <b>Sous</b> valley and cities such as Agadir, Marrakesh and Rabat. "
                   "Cousin Amazigh languages are spoken across North Africa and the Sahara."),
        ("How is it written?", "In <b>Tifinagh</b> letters, from <b>left to right</b>. Tamazight can also be written in Latin or Arabic letters."),
        ("How many letters?", "<b>33 letters</b>: 4 vowels, 2 half-vowels and 27 consonants, set out by IRCAM in 2003."),
        ("An official language", "Since <b>2011</b>, Tamazight has been an official language of Morocco, alongside Arabic. Children learn "
                                 "Tifinagh at school, and street signs often show it."),
        ("Very old letters", "Signs much like Tifinagh were carved on rocks in North Africa and the Sahara more than 2,000 years ago."),
    ],
    hello_pics=[("zgh_argan", {}), ("zgh_tagine", {}), ("mosque", {})],
    map=region_map(frame=[[-13.5, 28.3], [-0.5, 37.6]],
                   points=dict(rabat=[-6.84, 34.02], agadir=[-9.60, 30.42], marrakesh=[-7.99, 31.63], fes=[-5.00, 34.03],
                               alhoceima=[-3.93, 35.25]),
                   area=(-7.4, 31.2, 175, 85), area_rot=-25,
                   cities=[("rabat", "Rabat", 12, 8, "start", True), ("agadir", "Agadir", 12, 8, "start", False),
                           ("marrakesh", "Marrakesh", 12, 8, "start", False), ("fes", "Fes", 12, 8, "start", False),
                           ("alhoceima", "Al Hoceima", 12, -8, "start", False)],
                   label="MOROCCO", label_at=[-3.2, 33.0], marker=[-6.5, 31.8],
                   caption="The circle shows Morocco on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Rabat ★ is the capital. The dashed line "
                          "goes round the Atlas mountains and the Sous valley, where many families speak Tamazight; Tarifit is spoken near "
                          "Al Hoceima in the Rif.",
                   seas=[("Atlantic Ocean", -11.8, 33.6), ("Mediterranean Sea", -2.6, 36.9)], world_r=14),
    digits=[("0", "ⴰⵎⵢⴰ", "amya", "zero"), ("1", "ⵢⴰⵏ", "yan", "one"), ("2", "ⵙⵉⵏ", "sin", "two"), ("3", "ⴽⵕⴰⴹ", "kraḍ", "three"),
            ("4", "ⴽⴽⵓⵥ", "kkuẓ", "four"), ("5", "ⵙⵎⵎⵓⵙ", "smmus", "five"), ("6", "ⵚⴹⵉⵚ", "sḍiṣ", "six"), ("7", "ⵙⴰ", "sa", "seven"),
            ("8", "ⵜⴰⵎ", "tam", "eight"), ("9", "ⵜⵥⴰ", "tẓa", "nine")],
    phrases=[("ⴰⵙⵙⴰⵍⴰⵎⵓ ⵄⴰⵍⴰⵢⴽⵓⵎ", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("ⵡⴰⵄⴰⵍⴰⵢⴽⵓⵎ ⵙⵙⴰⵍⴰⵎ", "wa-ah-LAY-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("ⴰⵣⵓⵍ!", "ah-ZOOL!", "Hello!"),
             ("ⵉⵙⵎ ⵉⵏⵓ …", "ism ee-NOO …", "My name is …"),
             ("ⵜⴰⵏⵎⵎⵉⵔⵜ", "tah-nuh-MEERT", "Thank you"),
             ("ⵊⴰⵣⴰⴽⴰⵍⵍⴰⵀⵓ ⵅⴰⵢⵔⴰⵏ", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("ⵢⵉⵎⵎⴰ · ⴱⴰⴱⴰ", "YEEM-mah · BAH-bah", "Mother · Father"),
             ("ⴳⵯⵎⴰ · ⵓⵍⵜⵎⴰ", "GWMAH · OOLT-mah", "My brother · My sister"),
             ("ⵢⴰⵀ · ⵓⵀⵓ", "yah · OO-hoo", "Yes · No"),
             ("ⴰⵔ ⵍⵎⵎⴷⵖ ⵜⴰⵎⴰⵣⵉⵖⵜ!", "ar LMM-dugh tah-mah-ZEEGHT!", "I am learning Tamazight!")],
    cheer=("ⵎⴰⵛⴰⵍⵍⴰⵀ! ⵉⴼⵓⵍⴽⵉ!", "mah-shah-LAH! ee-FOOL-kee!", "Mashallah! Well done — it is lovely!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and Morocco’s 2014 census; the alphabet from "
                 "<b>IRCAM</b> (Royal Institute of Amazigh Culture).",
    book_pic=dict(left="ⴰ ⴱ ⴳ", right="ⴷ ⴹ ⴻ"),
    review_note="Native check needed for: ⴰⴽⵯⴼⴰⵢ akʷfay (milk) for ⴽⵯ — the least certain word (spelling and labialisation); "
                "ⴰⵀⴰⵔⴽⵓⵙ aharkus (slipper) for ⵀ; ⵜⴰⵛⵟⵟⴰⴱⵜ tacṭṭabt (broom) for ⵛ; ⴰⴳⵔⵉⵙ agris (ice); ⵍⵍⵓⵃ lluḥ (writing board), "
                "ⵍⵃⵉⵊⵊ lḥijj, ⵍⵇⵓⵔⵄⴰⵏ lqurɛan, ⵕⵎⴹⴰⵏ ṛmḍan, ⵚⵚⴰⴱⵓⵏ ṣṣabun, ⵟⵟⴰⵊⵉⵏ ṭṭajin (Arabic loans: is the l-/doubled form right?); "
                "phrases ⵢⵉⵎⵎⴰ (mother), ⵢⴰⵀ · ⵓⵀⵓ (yes · no), ⴰⵔ ⵍⵎⵎⴷⵖ ⵜⴰⵎⴰⵣⵉⵖⵜ, ⵉⴼⵓⵍⴽⵉ, the title ⴰⴷⵍⵉⵙ ⵉⵏⵓ ⵏ ⵜⵉⴼⵉⵏⴰⵖ and "
                "ⵜⵉⴳⵓⵔⵉⵡⵉⵏ ⵜⵉⵎⵣⵡⵓⵔⴰ; zero ⴰⵎⵢⴰ. Words mix Tashelhit and Central Atlas usage — choose one standard. "
                "The ⴻ page writes the schwa (ⴰⵣⴻⵎⵎⵓⵔ) on purpose; elsewhere IRCAM spelling leaves it out (ⵜⵉⵙⵏⵜ). "
                "Speaker number (~10 million in Morocco) to be confirmed.",
    tiles="ⴰⴱⴳⴷⵣⵥ", cover_pics=["zgh_argan", "zgh_tagine", "star", "mosque"], title_size=48,
    speakers_blurb="Tamazight is spoken by about 10 million people in Morocco and written in the ancient Tifinagh letters.",
    sample_words=[("ⴰⵎⴰⵏ", "aman", "water"), ("ⵉⵜⵔⵉ", "itri", "star"), ("ⴰⵔⴳⴰⵏ", "argan", "argan tree")],
    keywords=["tamazight alphabet book for kids", "learn tifinagh for children", "amazigh berber letters coloring",
              "tifinagh tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "moroccan heritage language gift"],
))
