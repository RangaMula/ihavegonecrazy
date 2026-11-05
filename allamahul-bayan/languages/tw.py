# -*- coding: utf-8 -*-
"""Book 75 - Twi / Akan (Latin script, 22 letters incl. Ɛ ɛ and Ɔ ɔ). Allamahul Bayan Series. REVIEW DRAFT.

Fonts: Baloo 2 and Nunito have no Ɛ ɛ Ɔ ɔ. Those four letters come from M PLUS Rounded 1c (800, round like
Baloo) in the display family and the big coloring letters, and from Noto Sans in the text family."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Twi name · syllables"
VOWELS = ["a", "e", "ɛ", "i", "o", "ɔ", "u"]
OPEN = "U+0186,U+0190,U+0254,U+025B"   # Ɔ Ɛ ɔ ɛ


def tw_fonts():
    out = fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext")
    for w in (400, 700, 800):
        out.append(("Baloo 2", w, "normal", "m-plus-rounded-1c-latin-ext-800-normal.woff2" if w >= 700
                    else "noto-sans-latin-ext-400-normal.woff2", OPEN))
        out.append(("Nunito", w, "normal", f"noto-sans-latin-ext-{w}-normal.woff2", OPEN))
    return out


def L(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, vowel=False, row=None):
    if row is None:
        row = " · ".join(c + small for c in "b d k m".split()) if vowel else " · ".join(small + v for v in ["a", "e", "ɛ", "o", "ɔ"])
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
            f'<div class="nt" style="font-size:15pt;margin-top:2px">{row}</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + small, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("A", "a", "a", "ah", "‘a’ as in “father”", "aborɔbɛ", "ah-baw-raw-beh", "pineapple", "pineapple", vowel=True),
    L("B", "b", "ba", "bah", "‘b’ as in “ball”", "borɔdeɛ", "baw-raw-deh-eh", "plantain (a cooking banana)", "banana"),
    L("D", "d", "da", "dah", "‘d’ as in “door”", "dua", "doo-ah", "tree", "tree",
      rule="dw sounds like “jw”: <i>dwa</i> (market) = “jwah”"),
    L("E", "e", "e", "ay", "‘ay’ as in “day”, but short", "efie", "ay-fee-ay", "home, house", "house", vowel=True),
    L("Ɛ", "ɛ", "ɛ", "eh", "‘e’ as in “bed” — the open E", "ɛpo", "eh-poh", "sea", "waves", vowel=True,
      note="Ɛ is a Twi letter! Its mouth is open wider than E: <i>e</i> as in “day”, <i>ɛ</i> as in “bed”."),
    L("F", "f", "fa", "fah", "‘f’ as in “fan”", "frankaa", "frahn-kah", "flag", "flag"),
    L("G", "g", "ga", "gah", "‘g’ as in “go”", "gyeene", "jay-nay", "onion", "onion",
      rule="gy sounds like ‘j’ in “jam”: <b>gy</b>eene = “jay-nay”"),
    L("H", "h", "ha", "hah", "‘h’ as in “hat”", "hyɛn", "shen", "ship, boat", "ship",
      rule="hy sounds like “sh” · hw sounds like “hw” (a breathy w)"),
    L("I", "i", "i", "ee", "‘ee’ as in “see”", "sika", "see-kah", "gold, money", "tw_sika", vowel=True,
      note="Very few Twi words start with I. Find it inside <i>sika</i>!"),
    L("K", "k", "ka", "kah", "‘k’ as in “kite”", "kosua", "koh-soo-ah", "egg", "egg",
      rule="ky sounds like ‘ch’ in “church” · kw sounds like ‘qu’ in “queen”"),
    L("L", "l", "la", "lah", "‘l’ as in “lamp”", "lɔre", "law-reh", "lorry, truck", "tw_lore",
      note="L is rare in Twi. It is found mostly in words from other languages, like <i>lɔre</i> (from English “lorry”)."),
    L("M", "m", "ma", "mah", "‘m’ as in “moon”", "mako", "mah-koh", "hot pepper", "tw_mako"),
    L("N", "n", "na", "nah", "‘n’ as in “net”; it can be a syllable on its own", "nsuo", "n-soo-oh", "water", "water",
      rule="ny sounds like ‘ny’ in “canyon” · nw sounds like “nw”"),
    L("O", "o", "o", "oh", "‘o’ as in “go”, but short", "owia", "oh-wee-ah", "sun", "sun", vowel=True),
    L("Ɔ", "ɔ", "ɔ", "aw", "‘aw’ as in “saw” — the open O", "ɔsram", "aw-srahm", "moon", "moon", vowel=True,
      note="Ɔ is a Twi letter! <i>o</i> sounds like “go”, <i>ɔ</i> sounds like “saw”."),
    L("P", "p", "pa", "pah", "‘p’ as in “pen”", "paanoo", "pah-noh", "bread", "tw_paanoo"),
    L("R", "r", "ra", "rah", "a light, quick ‘r’", "borɔfere", "baw-raw-feh-reh", "papaya", "tw_borofere",
      note="R never starts a Twi word. Find it twice inside <i>borɔfere</i>!"),
    L("S", "s", "sa", "sah", "‘s’ as in “sun”", "sumiɛ", "soo-mee-eh", "pillow", "pillow"),
    L("T", "t", "ta", "tah", "‘t’ as in “tap”", "toa", "toh-ah", "bottle", "tw_toa",
      rule="tw sounds like “chw”: <b>Tw</b>i = “chwee”"),
    L("U", "u", "u", "oo", "‘oo’ as in “moon”", "kube", "koo-beh", "coconut", "coconut", vowel=True,
      note="Very few Twi words start with U. Find it inside <i>kube</i>!"),
    L("W", "w", "wa", "wah", "‘w’ as in “water”", "wiemhyɛn", "wee-em-shen", "aeroplane", "plane",
      note="<i>wiem</i> (sky) + <i>hyɛn</i> (ship) = a sky-ship!"),
    L("Y", "y", "ya", "yah", "‘y’ as in “yes”", "bayerɛ", "bah-yeh-reh", "yam", "tw_bayere",
      note="Not many Twi naming words start with Y. Find it inside <i>bayerɛ</i>!"),
]

LANG = build(dict(
    code="tw", folder="book-75-twi-akan", series_no=75, isbn="", draft=True,
    name="Twi", native="Twi (Akan)", native_tr="chwee (ah-kahn)", name_word="din", write_word="kyerɛw",
    title="My First Twi Alphabet", cover_title_html="My First Twi<br>Alphabet",
    title_native="Me Twi nkyerɛwde a edi kan", title_letters="AaƐɛƆɔ", belongs_native="Saa nwoma yi yɛ …",
    belongs_pic="tw_kookoo", alphabet_native="nkyerɛwde", numbers_native="akontaa", numbers_tr="ah-kawn-tah",
    phrases_native="Nsɛm a edi kan",
    fonts=tw_fonts(), disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2",
                "m-plus-rounded-1c-latin-ext-800-normal.woff2", "noto-sans-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2, M PLUS Rounded 1c, Noto Sans",
    phon_feature="each letter’s Twi name and its syllables (ba, be, bɛ, bo, bɔ)",
    sections=[section(LETTERS, native="Twi nkyerɛwde", native_tr="chwee n-cheh-reh-deh — “the Twi letters”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Twi is written with <b>22 letters</b>. It has no C, J, Q, V, X or Z — but it has two letters of its own: <b>Ɛ ɛ</b> and <b>Ɔ ɔ</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Seven vowels</h3><b>a e ɛ i o ɔ u</b> say <i>ah, ay, eh, ee, oh, aw, oo</i>.
<b>Ɛ</b> is an “open E” (as in “bed”) and <b>Ɔ</b> is an “open O” (as in “saw”).</div>
<div class="box" style="margin:0.1in 0"><h3>Letter friends</h3>Some letters stand together to make one sound: <b>ky</b> (ch), <b>gy</b> (j),
<b>hy</b> (sh), <b>tw</b> (chw), <b>dw</b> (jw), <b>kw</b>, <b>hw</b>, <b>nw</b> and <b>ny</b>. You can hear one in the name <b>Tw</b>i itself!</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Ɛɛ</b>. Color both!</div>""")],
    sound_notes=[
        "Twi is a <b>tone language</b>: a high or low voice can change a word’s meaning. These guides use no capital letters for "
        "stress — listen to a Twi speaker for the tune of each word.",
        "<b>ay</b> is Twi <b>e</b> and <b>eh</b> is Twi <b>ɛ</b>; <b>oh</b> is Twi <b>o</b> and <b>aw</b> is Twi <b>ɔ</b>.",
        "<b>n-</b> or <b>m-</b> at the start of a word is a short hum: <i>n-soo-oh</i>.",
        "<b>ch</b>, <b>j</b> and <b>sh</b> in the guides come from the letter pairs <b>ky</b>, <b>gy</b> and <b>hy</b>."],
    phon_explain="The box marked <i>Twi name · syllables</i> shows a simple name for the letter (B is «ba») and its row of "
                 "syllables with the Twi vowels — the way children practise reading.",
    standard="Asante Twi (with Akuapem spellings where they are the usual school spellings)",
    hello=[
        ("Who speaks it?", "More than <b>10 million people</b> speak Akan as their first language, and millions more use Twi every day "
                           "as a second language.<sup>³</sup>"),
        ("Where?", "In <b>Ghana</b>, West Africa — in <b>Kumasi</b>, <b>Accra</b> and across the south of the country. "
                   "<b>Asante Twi</b>, <b>Akuapem Twi</b> and <b>Fante</b> are all kinds of Akan."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with two extra letters: <b>ɛ</b> and <b>ɔ</b>."),
        ("How many letters?", "<b>22 letters</b>: A B D E Ɛ F G H I K L M N O Ɔ P R S T U W Y."),
        ("A singing language", "Twi is a <b>tone language</b>. The same letters can mean different things when your voice goes "
                               "high or low — talking in Twi is a little like singing!"),
        ("Did you know?", "Akan children have a <b>day name</b> for the day they were born. A boy born on a Friday is "
                          "<i>Kofi</i> and a girl is <i>Afua</i>; on a Saturday, <i>Kwame</i> and <i>Ama</i>."),
    ],
    hello_pics=[("tw_kookoo", {}), ("pineapple", {}), ("mosque", {})],
    map=region_map(frame=[[-4.2, 3.6], [2.8, 11.4]],
                   points=dict(kumasi=[-1.62, 6.69], accra=[-0.19, 5.60], capecoast=[-1.25, 5.11], sunyani=[-2.33, 7.34],
                               koforidua=[-0.26, 6.09]),
                   area=(-1.4, 6.4, 260, 190), area_rot=-10,
                   cities=[("kumasi", "Kumasi", 14, 8, "start", False), ("accra", "Accra", 6, 30, "start", True),
                           ("capecoast", "Cape Coast", -14, 14, "end", False), ("sunyani", "Sunyani", -14, 8, "end", False),
                           ("koforidua", "Koforidua", 14, 4, "start", False)],
                   label="GHANA", label_at=[-0.9, 10.3], marker=[-1.2, 7.5],
                   caption="The circle shows Ghana on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Twi is spoken in Kumasi, Sunyani, "
                          "Koforidua, Accra and Cape Coast. The dashed line shows where most Akan speakers live.",
                   seas=[("Gulf of Guinea", -0.6, 4.3)], world_r=12),
    digits=[("0", "hwee", "shweh", "zero, nothing"), ("1", "baako", "bah-koh", "one"), ("2", "mmienu", "mmee-ay-noo", "two"),
            ("3", "mmiɛnsa", "mmee-en-sah", "three"), ("4", "ɛnan", "eh-nahn", "four"), ("5", "enum", "ay-noom", "five"),
            ("6", "nsia", "n-see-ah", "six"), ("7", "nson", "n-sohn", "seven"), ("8", "nwɔtwe", "n-waw-chweh", "eight"),
            ("9", "nkron", "n-krohn", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-lah-moo ah-lai-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-lai-koom as-sah-lahm", "And peace be upon you (the reply)"),
             ("Akwaaba!", "ah-kwah-bah", "Welcome!"),
             ("Me din de …", "may deen day …", "My name is …"),
             ("Medaase", "may-dah-say", "Thank you"),
             ("Jazakallahu khairan", "jah-zah-kahl-lah-hoo khai-rahn", "May Allah reward you with good"),
             ("ɛna · agya", "eh-nah · ah-jah", "Mother · Father"),
             ("nuabarima · nuabaa", "noo-ah-bah-ree-mah · noo-ah-bah", "Brother · Sister"),
             ("aane · daabi", "ah-nay · dah-bee", "Yes · No"),
             ("Meresua Twi!", "may-ray-soo-ah chwee", "I am learning Twi!")],
    cheer=("Mashallah! Ayekoo!", "mah-shah-lah! ah-yay-koh!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B D", right="E Ɛ F"),
    review_note="Check the simple letter names (a, ba, da…) — schools may use other names; the spelling of every word, "
                "especially <i>borɔdeɛ</i> (plantain), <i>gyeene</i> (onion), <i>ɛpo</i> (sea), <i>borɔfere</i> (papaya), "
                "<i>sumiɛ</i> (pillow), <i>wiemhyɛn</i> (aeroplane) and <i>bayerɛ</i> (yam); the numbers (<i>ɛnan/anan</i>, "
                "<i>enum/anum</i>, <i>hwee</i> for zero); the title and belongs-to lines in Twi; and the e/ɛ, o/ɔ sound guides. "
                "Tone is not shown at all.",
    tiles="AƐƆKSW", cover_pics=["tw_kookoo", "pineapple", "coconut", "mosque"],
    speakers_blurb="Twi (Akan) is spoken by more than 10 million people in Ghana, West Africa.",
    sample_words=[("ɔsram", "aw-srahm", "moon"), ("kosua", "koh-soo-ah", "egg"), ("aborɔbɛ", "ah-baw-raw-beh", "pineapple")],
    keywords=["twi alphabet book for kids", "learn twi for children", "akan language coloring book",
              "ghana twi letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual twi english toddlers"],
))
