# -*- coding: utf-8 -*-
"""Book 60 - Fula (Pulaar / Pular / Fulfulde) in the Adlam script (28 letters, right to left, cased).
Allamahul Bayan Series. REVIEW DRAFT: every word, spelling and letter name needs a native check.

Words are typed in the Latin Fula spelling and converted to Adlam by ad() below, so the Adlam and the
transliteration always agree: long vowels get the lengthener marks, double consonants the gemination
mark, the apostrophe the Adlam hamza."""
from generic import build, letter, section, fontset
from maps import region_map

# ---- Latin Fula -> Adlam ------------------------------------------------------------------
_SMALL = dict(a="𞤢", d="𞤣", l="𞤤", m="𞤥", b="𞤦", s="𞤧", p="𞤨", ɓ="𞤩", r="𞤪", e="𞤫", f="𞤬", i="𞤭", o="𞤮",
              ɗ="𞤯", ƴ="𞤰", w="𞤱", n="𞤲", k="𞤳", y="𞤴", u="𞤵", j="𞤶", c="𞤷", h="𞤸", q="𞤹", g="𞤺", ñ="𞤻",
              t="𞤼", ŋ="𞤽", v="𞤾", x="𞤿", z="𞥁", š="𞥃")
_CAP = {k: chr(ord(v) - 0x22) for k, v in _SMALL.items()}
ALIF_LONG, VOWEL_LONG, GEMIN, HAMZA = "\U0001E944", "\U0001E945", "\U0001E946", "\U0001E947"


def ad(text):
    """'Alluwal' -> 𞤀𞤤𞥆𞤵𞤱𞤢𞤤.  kh -> 𞤿, sh -> 𞥃, a capital Latin letter -> an Adlam capital."""
    t = text.replace("kh", "x").replace("Kh", "X").replace("sh", "š")
    out, i = [], 0
    while i < len(t):
        ch = t[i]
        low = ch.lower()
        nxt = t[i + 1].lower() if i + 1 < len(t) else ""
        if low in _SMALL:
            out.append(_CAP[low] if ch != low else _SMALL[low])
            if nxt == low:                       # long vowel or double consonant
                out.append((ALIF_LONG if low == "a" else VOWEL_LONG) if low in "aeiou" else GEMIN)
                i += 1
        elif ch == "'":
            out.append(HAMZA)
        elif ch == "!":
            out.append("!")
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def excl(text):
    """Adlam exclamations open with the initial mark 𞥞 and close with !"""
    return "𞥞" + ad(text)


NT = '<span class="nt">{}</span>'


def A(cap_lat, name, sound, word, tr, meaning, pic, args=None, note=None, cap_word=False):
    small = _SMALL[cap_lat.lower()]
    cap = _CAP[cap_lat.lower()]
    w = ad(word[0].upper() + word[1:]) if cap_word else ad(word)
    phon = (f'<div style="display:flex;justify-content:space-between;align-items:center">'
            f'<div class="nt" style="font-size:26pt;line-height:1.5">{cap} &nbsp; {small}</div>'
            f'<div style="font:600 18pt Nunito">{cap_lat} {cap_lat.lower()}</div></div>'
            f'<div class="small">Adlam capital · small &nbsp;=&nbsp; Fula Latin letters</div>'
            f'<div class="small" style="margin-top:3px">Joined: <span class="nt" style="font-size:18pt">{small * 3}</span></div>')
    return letter(cap + small, ad(name), name, sound, w, tr, meaning, pic, phon, "Capital · small · joined", args, note)


LETTERS = [
    A("A", "alif", "‘a’ as in “father”, but short; with the long mark 𞥄 it is ‘aa’", "alluwal", "al-LOO-wal",
      "wooden writing board (for learning the Qur’an)", "ff_alluwal", cap_word=False),
    A("D", "daali", "‘d’ as in “day”", "deftere", "def-TEH-reh", "book", "book", args=dict(left="𞤀 𞤁 𞤂", right="𞤃 𞤄 𞤅")),
    A("L", "laam", "‘l’ as in “lamp”", "lekki", "LEK-kee", "tree", "tree"),
    A("M", "miim", "‘m’ as in “moon”", "misiide", "mee-SEE-deh", "mosque", "mosque"),
    A("B", "ba", "‘b’ as in “ball”", "baafal", "BAA-fal", "door", "door"),
    A("S", "sinnyiiyhe", "‘s’ as in “sun”", "suudu", "SOO-doo", "house", "house"),
    A("P", "pe", "‘p’ as in “pen”", "piindi", "PEEN-dee", "flowers", "flower"),
    A("Ɓ", "bhe", "a ‘b’ said while gently pulling air in — a special Fula sound", "ɓoggol", "ƁOG-gol", "rope", "ff_rope"),
    A("R", "ra", "a rolled ‘r’", "ruulde", "ROOL-deh", "cloud", "clouds"),
    A("E", "e", "‘e’ as in “bed”", "lewru", "LEW-roo", "moon", "moon",
      note=f"Very few Fula words start with E. Find {NT.format('𞤫')} inside {NT.format(ad('lewru'))}!"),
    A("F", "fa", "‘f’ as in “fan”", "fuɗnaange", "fuɗ-NAAN-geh", "the east, where the sun rises", "sunrise"),
    A("I", "i", "‘i’ as in “sit”; with the long mark 𞥅 it is ‘ee’ as in “see”", "Islaam", "is-LAAM", "Islam",
      "kaaba", cap_word=True, note="A name starts with a capital letter, so Islaam begins with the big 𞤋."),
    A("O", "o", "‘o’ as in “for”, short and round", "loonde", "LOON-deh", "big water jar", "jar",
      note=f"Very few Fula words start with O. Find {NT.format('𞤮')} inside {NT.format(ad('loonde'))}!"),
    A("Ɗ", "dha", "a ‘d’ said while gently pulling air in — a special Fula sound", "ɗerewol", "ƊEH-reh-wol",
      "sheet of paper, a letter", "envelope"),
    A("Ƴ", "yhe", "a ‘y’ with a little catch in the throat — a special Fula sound", "kaaƴe", "KAA-ƴeh",
      "rocks, hills", "mountain", note=f"Ƴ rarely starts a word. Find {NT.format('𞤰')} inside {NT.format(ad('kaaƴe'))}!"),
    A("W", "waw", "‘w’ as in “water”", "weendu", "WEEN-doo", "pond, lake", "waves"),
    A("N", "nun", "‘n’ as in “net”", "naange", "NAAN-geh", "sun", "sun"),
    A("K", "kaf", "‘k’ as in “kite”", "kammu", "KAM-moo", "sky", "rainbow"),
    A("Y", "ya", "‘y’ as in “yes”", "yiite", "YEE-teh", "fire", "ff_fire"),
    A("U", "u", "‘u’ as in “put”; with the long mark 𞥅 it is ‘oo’ as in “moon”", "tummude", "TOOM-moo-deh",
      "calabash bowl", "ff_calabash", note=f"Very few Fula words start with U. Find {NT.format('𞤵')} inside {NT.format(ad('tummude'))}!"),
    A("J", "jiim", "‘j’ as in “jam”", "juulde", "JOOL-deh", "prayer (salah)", "prayermat"),
    A("C", "chi", "‘ch’ as in “chair”", "ceede", "CHEH-deh", "money", "ff_coins"),
    A("H", "ha", "‘h’ as in “hat”", "hoɗere", "HO-ɗeh-reh", "star", "star"),
    A("Q", "qaaf", "a ‘k’ said far back in the throat — used in words from Arabic", "Qur'aana", "qur-AA-nah",
      "the Qur’an", "ff_rehal", cap_word=True, note="Q comes in words from Arabic, like the name of the Qur’an."),
    A("G", "ga", "‘g’ as in “go”", "gawri", "GAW-ree", "millet (a grain)", "paddy"),
    A("Ñ", "nya", "‘ny’ as in “canyon”", "ñiiri", "NYEE-ree", "food (a cooked grain dish)", "plate"),
    A("T", "tu", "‘t’ as in “top”", "toɓo", "TO-ɓo", "rain", "raincloud"),
    A("Ŋ", "nha", "‘ng’ as in “sing”", "kaŋŋe", "KANG-ngeh", "gold", "ring",
      note=f"Ŋ never starts a word. Find {NT.format('𞤽')} inside {NT.format(ad('kaŋŋe'))}!"),
]

HOOKS = "U+0181,U+018A,U+01B3-01B4,U+0253,U+0257,U+014A-014B"
FONTS = (fontset("Noto Sans Adlam", "noto-sans-adlam-adlam", "Noto Sans Adlam", "noto-sans-adlam-adlam")
         + [("Nunito", w, "normal", f"nunito-latin-ext-{w}-normal.woff2", HOOKS) for w in (400, 700)])

LANG = build(dict(
    code="ff", folder="book-60-fula", series_no=60, isbn="", draft=True, dir="rtl",
    name="Fula", native=ad("Pulaar"), native_tr="pu-LAAR (also Pular, Fulfulde)", name_word=ad("innde"),
    write_word=ad("winndu"), letters_word="Letters",
    title="My First Fula Alphabet", subtitle="A Coloring Book to Learn, Trace & Say the 28 Letters of Adlam, "
                                             "the Fula Alphabet, with English Phonetics",
    cover_title_html="My First Fula<br>Alphabet", title_size=46,
    title_native=ad("Alkule Adlam"), title_letters="𞤀𞤁𞤂𞤃𞤄𞤅", belongs_native=ad("Ndee deftere ko am"),
    belongs_pic="star", alphabet_native=ad("Alkule"), numbers_native=ad("limre"), numbers_tr="LIM-reh",
    phrases_native=ad("Konngi"),
    fonts=FONTS, disp_family="Noto Sans Adlam", text_family="Noto Sans Adlam",
    glyph_font=["noto-sans-adlam-adlam-700-normal.woff2"], font_credit="Noto Sans Adlam",
    extra_css=".nt{line-height:1.6} .lp-name{font-size:24pt} .lp-word .w{font-size:38pt;line-height:1.5}",
    phon_feature="each letter’s capital, small and joined shapes, with its Fula Latin twin (𞤀𞤢 = Aa)",
    sections=[section(LETTERS, native=ad("Alkule"), native_tr="al-KOO-leh — “the letters”",
                      chart_cols=7, warmup_cols=6, chart_title="letters",
                      intro_html=f"""<p>Adlam is written <b>from right to left</b>, like the Qur’an. Start reading each line on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Big and small</h3>Every Adlam letter has a <b>capital</b> and a <b>small</b> form, just like English:
<div class="nt" style="font-size:26pt;text-align:center;line-height:1.6">𞤀 𞤢 &nbsp;·&nbsp; 𞤄 𞤦 &nbsp;·&nbsp; 𞤃 𞤥</div>
Capitals start a sentence or a name: <span class="nt" style="font-size:16pt">{ad('Islaam')}</span>.</div>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Small letters <b>join</b> to each other inside a word, like Arabic:
<div class="nt" style="font-size:26pt;text-align:center;line-height:1.6">𞤧 + 𞤵 + 𞤵 + 𞤣 + 𞤵 = {ad('suudu')}</div>
<div style="text-align:center"><i>s + u + u + d + u = suudu</i> (house)</div></div>
<div class="box"><h3>Little helper marks</h3><span class="nt" style="font-size:18pt">𞤢𞥄</span> the long mark on <b>a</b> makes <i>aa</i>;
<span class="nt" style="font-size:18pt">𞤭𞥅</span> makes the other vowels long (<i>ii, ee, oo, uu</i>);
<span class="nt" style="font-size:18pt">𞤤𞥆</span> doubles a consonant (<i>ll</i>), as in <span class="nt" style="font-size:16pt">{ad('alluwal')}</span>.</div>""")],
    sound_notes=[
        "<b>Adlam is read from right to left</b>. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “they”, <i>ii</i> as in “see”, <i>oo</i> as in “door”, <i>uu</i> as in “moon”.",
        "<b>Doubled consonants are held a little longer:</b> <i>lekki</i> is “lek-kee”.",
        "<b>CAPITALS</b> in the pronunciation show the stressed part of the word.",
        "<b>ɓ, ɗ, ƴ</b> are special Fula sounds: say <i>b, d, y</i> while gently pulling air in. The transliteration keeps these Fula letters.",
        "Sounds follow the Pular of Guinea and the Pulaar of Senegal; other Fula regions say some words a little differently."],
    phon_explain="The third box shows the letter’s <b>capital</b> and <b>small</b> shapes, the matching letter of the Fula "
                 "<b>Latin</b> alphabet, and the small letter <b>joined</b> three times, as it looks inside a word.",
    standard="Pular (Guinea) and Pulaar (Senegal)",
    hello=[
        ("Who speaks it?", "About <b>35 million people</b> speak Fula, also called <b>Pulaar</b>, <b>Pular</b> or <b>Fulfulde</b>.<sup>³</sup>"),
        ("Where?", "In a wide belt across <b>West and Central Africa</b>, from <b>Senegal</b> and <b>Guinea</b> to <b>Nigeria</b> and "
                   "<b>Cameroon</b>. Most Fula families are <b>Muslim</b>."),
        ("How is it written?", "Fula is written in Latin letters, in Arabic letters (<i>Ajami</i>) and in <b>Adlam</b>, "
                               "a new alphabet written from <b>right to left</b>."),
        ("How many letters?", "Adlam has <b>28 letters</b>, each with a capital and a small form, plus 6 extra letters for words "
                              "from other languages."),
        ("Made by two boys!", "In <b>1989</b>, two young brothers in Guinea, <b>Ibrahima and Abdoulaye Barry</b>, invented Adlam so "
                              "that Fula could be written in its own letters."),
        ("What does ADLaM mean?", f"It is made from the first letters of <span class='nt'>{ad('Alkule Dandayɗe Leñol Mulugol')}</span> — "
                                  "“the alphabet that keeps the peoples from being lost”."),
    ],
    hello_pics=[("ff_alluwal", {}), ("mosque", {}), ("sunrise", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[-18.5, -2.0], [16.5, 26.0]],
                   points=dict(conakry=[-13.71, 9.51], labe=[-12.28, 11.32], dakar=[-17.44, 14.69],
                               niamey=[2.11, 13.51], maroua=[14.32, 10.59]),
                   area=(-2.0, 12.5, 430, 120),
                   cities=[("conakry", "Conakry", 14, 22, "start", False), ("labe", "Labé", 14, -8, "start", False),
                           ("dakar", "Dakar", 14, -10, "start", False), ("niamey", "Niamey", 14, 8, "start", False),
                           ("maroua", "Maroua", -14, -10, "end", False)],
                   label="WEST AFRICA", label_at=[-1.0, 22.0], marker=[-2.0, 12.0],
                   caption="The circle shows West Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Fula is spoken all along the "
                          "dashed area, from Dakar and Conakry to Niamey and Maroua. Adlam was born near <b>Labé</b>, in the hills of Fuuta Jaloo.",
                   seas=[("Atlantic Ocean", -12.0, 1.0)], world_r=16),
    digits=[("𞥐", ad("ɓolum"), "ɓo-LUM", "zero"), ("𞥑", ad("go'o"), "GO-'o", "one"), ("𞥒", ad("ɗiɗi"), "ƊI-ɗi", "two"),
            ("𞥓", ad("tati"), "TA-ti", "three"), ("𞥔", ad("nayi"), "NA-yi", "four"), ("𞥕", ad("joy"), "joy", "five"),
            ("𞥖", ad("jeegom"), "JEH-gom", "six"), ("𞥗", ad("jeeɗiɗi"), "jeh-ƊI-ɗi", "seven"),
            ("𞥘", ad("jeetati"), "jeh-TA-ti", "eight"), ("𞥙", ad("jeenayi"), "jeh-NA-yi", "nine")],
    phrases=[(ad("Assalaamu alaykum"), "as-sa-LAA-mu a-LAY-kum", "Peace be upon you (the Muslim greeting)"),
             (ad("Wa alaykum assalaam"), "wa a-LAY-kum as-sa-LAAM", "And upon you be peace (the reply)"),
             (ad("Innde am ko …"), "INN-deh am ko …", "My name is …"),
             (ad("A jaaraama"), "a jaa-RAA-ma", "Thank you"),
             (ad("Jazaakallaahu khayran"), "ja-ZAA-kal-LAA-hu KHAY-ran", "May Allah reward you with good"),
             (ad("yumma · baaba"), "YUM-ma · BAA-ba", "Mother · Father"),
             (ad("musiɗɗo gorko · musiɗɗo debbo"), "mu-SIƊ-ɗo GOR-ko · mu-SIƊ-ɗo DEB-bo", "Brother · Sister"),
             (ad("Eey · Alaa"), "eey · a-LAA", "Yes · No"),
             (excl("Miɗo jaŋnga Pulaar!"), "MI-ɗo JANG-nga pu-LAAR!", "I am learning Fula!")],
    cheer=(excl("Maasha Allah! A waɗii moƴƴa!"), "MAA-sha AL-lah! a wa-ƊII MOƳ-ƴa!", "Mashallah! You did well!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International, all Fula varieties together); the story of Adlam from "
                 "the <b>Unicode Standard</b> (Adlam block, 2016) and its inventors’ published accounts.",
    book_pic=dict(left="𞤀 𞤁 𞤂", right="𞤃 𞤄 𞤅"),
    review_note=("Fula has many regional varieties; this draft mixes Pular (Guinea) and Pulaar (Senegal) forms. A native speaker "
                 "should check: (1) every Adlam spelling, especially the long-vowel marks, the gemination mark (used for every double "
                 "consonant, e.g. alluwal, lekki, kammu) and prenasalised clusters (nd, ng: loonde, naange, weendu), which are written "
                 "here as plain n + consonant; (2) the letter names (alif, daali, laam … taken from the Unicode names; teachers may say "
                 "a, da, la … instead); (3) the words piindi (flowers), ñiiri (food), ɗerewol (paper), toɓo (rain), kaaƴe (rocks); "
                 "(4) the phrases (Innde am ko …, yumma, musiɗɗo gorko/debbo, Miɗo jaŋnga Pulaar, A waɗii moƴƴa), the numbers "
                 "(ɓolum for zero, go'o with the Adlam hamza) and the cover/title words (Alkule Adlam, Ndee deftere ko am, limre, konngi)."),
    tiles="𞤀𞤁𞤂𞤃𞤄𞤅", cover_pics=["ff_alluwal", "sunrise", "mosque", "star"],
    speakers_blurb="Fula (Pulaar, Pular, Fulfulde) is spoken by about 35 million people across West and Central Africa.",
    sample_words=[(ad("naange"), "NAAN-geh", "sun"), (ad("misiide"), "mee-SEE-deh", "mosque"), (ad("lekki"), "LEK-kee", "tree")],
    keywords=["fula alphabet book for kids", "adlam alphabet coloring book", "learn pulaar pular for children",
              "fulfulde letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "african language gift for kids"],
))
