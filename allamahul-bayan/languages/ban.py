# -*- coding: utf-8 -*-
"""Book 53 - Balinese (Aksara Bali). Allamahul Bayan Series. REVIEW DRAFT.
Built with engine/generic.py: three sections - the 18 basic letters (hanacaraka order), the 5 vowel signs
(pangangge suara) and 4 closing signs (pangangge tengenan). No Hindu religious words or pictures.
Transliteration = the normal Latin spelling of Balinese (e = pepet schwa, é = taleng)."""
from generic import build, letter, section, fontset
from maps import region_map

FONT = "noto-sans-balinese-balinese"
V_SIGNS = [("", "a"), ("ᬶ", "i"), ("ᬸ", "u"), ("ᬾ", "é"), ("ᭀ", "o"), ("ᭂ", "e")]
SPECIAL = {("ᬭ", "ᭂ"): "ᬋ", ("ᬮ", "ᭂ"): "ᬍ"}  # re and le have their own letters (ra repa, la lenga)


def cell(s, t, fs=16):
    return (f'<div style="text-align:center"><div class="nt" style="font-size:{fs}pt;line-height:1.45;padding-bottom:6px">{s}</div>'
            f'<div class="tr small" style="line-height:1.05">{t}</div></div>')


def grid(cells, cols=4):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:10px 4px;margin-top:2px">{"".join(cells)}</div>'


def syllables(ch, root):
    cells = [cell(SPECIAL.get((ch, s), ch + s), root + v) for s, v in V_SIGNS]
    cells.append(cell(ch + "᭄", root))
    return grid(cells)


PH = "Balinese phonetics · vowel signs + adeg-adeg"


def A(ch, name, root, sound, word, tr, meaning, pic, args=None, note=None):
    return letter(ch, ch, name, sound, word, tr, meaning, pic, syllables(ch, root), PH, args, note)


def S(big, sign, name_nat, name, sound, word, tr, meaning, pic, examples, args=None, note=None, label=""):
    ex = "".join(f'<div>{b} + ◌{sign} = {r} <span class="tr" style="font-family:Nunito;font-size:12pt">({t})</span></div>'
                 for b, r, t in examples)
    phon = (f'<div class="nt" style="font-size:26pt;line-height:1.45;text-align:center">◌{sign}</div>'
            f'<div class="nt" style="font-size:17pt;line-height:1.6;text-align:center">{ex}</div>')
    return letter(big, name_nat, name, sound, word, tr, meaning, pic, phon, label, args, note)


INSIDE = "Rarely first: find <span class='nt'>{}</span> inside <span class='nt'>{}</span>!"

LETTERS = [
    A("ᬳ", "ha", "h", "‘h’ as in “hat” — at the start of a word often just ‘a’", "ᬳᬮᬲ᭄", "alas", "forest", "tree",
      note="Here <span class='nt'>ᬳ</span> carries just a vowel: “a-las”."),
    A("ᬦ", "na", "n", "‘n’ as in “net”", "ᬦᬲᬶ", "nasi", "cooked rice", "rice"),
    A("ᬘ", "ca", "c", "‘ch’ as in “chair”", "ᬘᬂᬓᬶᬃ", "cangkir", "cup", "teacup"),
    A("ᬭ", "ra", "r", "a tapped ‘r’ — flick the tongue once", "ᬭᭀᬢᬶ", "roti", "bread", "roti"),
    A("ᬓ", "ka", "k", "‘k’ as in “kite”, with no puff of air", "ᬓᬧᬮ᭄", "kapal", "ship", "ship"),
    A("ᬤ", "da", "d", "‘d’ as in “dog”", "ᬤᭂᬮᬶᬫ", "delima", "pomegranate", "pomegranate"),
    A("ᬢ", "ta", "t", "a soft ‘t’, with no puff of air", "ᬢᭂᬩᬸ", "tebu", "sugarcane", "sugarcane"),
    A("ᬲ", "sa", "s", "‘s’ as in “sun”", "ᬲᬫ᭄ᬧᬢ᭄", "sampat", "broom", "broom"),
    A("ᬯ", "wa", "w", "‘w’ as in “water”", "ᬯᭀᬃᬢᭂᬮ᭄", "wortel", "carrot", "carrot"),
    A("ᬮ", "la", "l", "‘l’ as in “lamp”", "ᬮᬬᬗᬦ᭄", "layangan", "kite", "kite"),
    A("ᬫ", "ma", "m", "‘m’ as in “moon”", "ᬫᬂᬕ", "mangga", "mango", "mango"),
    A("ᬕ", "ga", "g", "‘g’ as in “go”", "ᬕᬸᬦᬸᬂ", "gunung", "mountain", "mountain"),
    A("ᬩ", "ba", "b", "‘b’ as in “ball”", "ᬩᬸᬮᬦ᭄", "bulan", "moon", "moon"),
    A("ᬗ", "nga", "ng", "‘ng’ as in “sing”, but at the start of a syllable", "ᬩᬸᬗ", "bunga", "flower", "flower",
      note=INSIDE.format("ᬗ", "ᬩᬸᬗ")),
    A("ᬧ", "pa", "p", "‘p’ as in “pen”, with no puff of air", "ᬧᬤᬶ", "padi", "rice plant", "paddy"),
    A("ᬚ", "ja", "j", "‘j’ as in “jam”", "ᬚᬕᬸᬂ", "jagung", "corn", "corn"),
    A("ᬬ", "ya", "y", "‘y’ as in “yes”", "ᬧᬬᬸᬂ", "payung", "umbrella", "umbrella", note=INSIDE.format("ᬬ", "ᬧᬬᬸᬂ")),
    A("ᬜ", "nya", "ny", "‘ny’ as in “canyon”", "ᬜᬸᬄ", "nyuh", "coconut", "coconut"),
]

SV = "Balinese phonetics · vowel sign"
VOWELS = [
    S("ᬧᬶ", "ᬶ", "ᬳᬸᬮᬸ", "ulu", "‘i’ as in “sit”, a little longer", "ᬧᬶᬭᬶᬂ", "piring", "plate", "plate",
      [("ᬓ", "ᬓᬶ", "ki"), ("ᬦ", "ᬦᬶ", "ni")], label=SV),
    S("ᬳᬸ", "ᬸ", "ᬲᬸᬓᬸ", "suku", "‘u’ as in “put”", "ᬳᬸᬚᬦ᭄", "ujan", "rain", "raincloud",
      [("ᬓ", "ᬓᬸ", "ku"), ("ᬲ", "ᬲᬸ", "su")], label=SV),
    S("ᬳᬾ", "ᬾ", "ᬢᬮᬾᬂ", "taleng", "‘é’ like the ‘e’ in “bed”, a little longer", "ᬳᬾᬲ᭄", "és", "ice", "ice",
      [("ᬓ", "ᬓᬾ", "ké"), ("ᬫ", "ᬫᬾ", "mé")], label=SV,
      note="<i>Taleng</i> is written <b>before</b> the letter, but said after it!"),
    S("ᬳᭀ", "ᭀ", "ᬢᬮᬾᬂ ᬢᭂᬤᭀᬂ", "taleng tedong", "‘o’ as in “go”, said short", "ᬳᭀᬫ᭄ᬩᬓ᭄", "ombak", "waves", "waves",
      [("ᬓ", "ᬓᭀ", "ko"), ("ᬧ", "ᬧᭀ", "po")], label=SV,
      note="Two pieces hug the letter: <span class='nt'>ᬾ</span> in front and <span class='nt'>ᬵ</span> behind."),
    S("ᬲᭂ", "ᭂ", "ᬧᭂᬧᭂᬢ᭄", "pepet", "a quiet ‘uh’, like the ‘a’ in “about”", "ᬲᭂᬦ᭄ᬤᭀᬓ᭄", "sendok", "spoon", "spoon",
      [("ᬓ", "ᬓᭂ", "ke"), ("ᬢ", "ᬢᭂ", "te")], label=SV,
      note="With <span class='nt'>ᬭ</span> and <span class='nt'>ᬮ</span> Balinese uses special letters instead: "
           "<span class='nt'>ᬋ</span> <i>re</i> and <span class='nt'>ᬍ</span> <i>le</i>."),
]

SC = "Balinese phonetics · closing sign"
CLOSERS = [
    S("ᬯᬂ", "ᬂ", "ᬘᭂᬘᭂᬓ᭄", "cecek", "adds ‘ng’ as in “sing” to the end of a syllable", "ᬩᬯᬂ", "bawang", "onion", "onion",
      [("ᬓ", "ᬓᬂ", "kang"), ("ᬯ", "ᬯᬂ", "wang")], label=SC),
    S("ᬬᬃ", "ᬃ", "ᬲᬸᬭᬂ", "surang", "adds ‘r’ to the end of a syllable", "ᬮᬬᬃ", "layar", "sail", "boat",
      [("ᬓ", "ᬓᬃ", "kar"), ("ᬬ", "ᬬᬃ", "yar")], label=SC),
    S("ᬫᬄ", "ᬄ", "ᬩᬶᬲᬄ", "bisah", "adds a breathy ‘h’ to the end of a syllable", "ᬳᬸᬫᬄ", "umah", "house", "house",
      [("ᬓ", "ᬓᬄ", "kah"), ("ᬫ", "ᬫᬄ", "mah")], label=SC),
    S("ᬤ᭄", "᭄", "ᬳᬤᭂᬕ᭄ᬳᬤᭂᬕ᭄", "adeg-adeg", "takes the vowel away: ᬤ da becomes just ‘d’", "ᬳᬸᬩᬤ᭄", "ubad", "medicine", "medicine",
      [("ᬓ", "ᬓ᭄", "k"), ("ᬤ", "ᬤ᭄", "d")], label=SC,
      note="Inside a word the next letter tucks under instead (a <i>gantungan</i>)."),
]

INTRO1 = """<p>Balinese has its own lovely script: <b>Aksara Bali</b>. It is a close cousin of the Javanese script, and it is
written from <b>left to right</b>. Children in Bali learn it at school, and you can see it on signs all over the island.</p>
<div class="box" style="margin:0.1in 0"><h3>18 letters, four little lines</h3>Children learn the 18 basic letters as four
short lines, like a rhyme:
<div class="nt" style="font-size:20pt;line-height:1.75;margin-top:4px;text-align:center">ᬳᬦᬘᬭᬓ · ᬤᬢᬲᬯᬮ<br>ᬫᬕᬩᬗ · ᬧᬚᬬᬜ</div>
<div style="text-align:center"><i>ha na ca ra ka · da ta sa wa la · ma ga ba nga · pa ja ya nya</i></div></div>
<div class="box" style="margin:0.1in 0"><h3>Every letter says “a”</h3>Each letter is a whole syllable: <span class="nt">ᬓ</span> is
<i>ka</i>, not just <i>k</i>.</div>
<div class="box"><h3>Change the vowel</h3>Small <b>vowel signs</b> (Part 2) change the “a”: <span class="nt">ᬓ ᬓᬶ ᬓᬸ ᬓᭀ</span>
<i>ka ki ku ko</i>. Every letter page shows its whole family.</div>"""

INTRO2 = """<p>The vowel signs are called <b>pangangge suara</b> — little “clothes” that a letter wears. They sit above the letter,
below it, in front of it, or on both sides!</p>
<div class="box" style="margin:0.1in 0"><h3>Five vowel signs</h3>
<div class="nt" style="font-size:20pt;line-height:1.8;text-align:center">ᬓᬶ · ᬓᬸ · ᬓᬾ · ᬓᭀ · ᬓᭂ</div>
<div style="text-align:center"><i>ki · ku · ké · ko · ke</i></div></div>
<div class="box" style="margin:0.1in 0"><h3>Words that start with a vowel</h3>A word that begins with a vowel is usually written
with the letter <span class="nt">ᬳ</span>: <span class="nt">ᬳᬸᬚᬦ᭄</span> <i>ujan</i> (rain).</div>
<div class="box"><h3>Look closely!</h3>On these pages the big letter is the <b>syllable of the word</b> that wears the sign.</div>"""

INTRO3 = """<p>Some syllables end with a consonant: <i>ba-<b>wang</b></i>, <i>la-<b>yar</b></i>. Balinese closes them with
<b>pangangge tengenan</b> — four little closing signs.</p>
<div class="box" style="margin:0.1in 0"><h3>Four closing signs</h3>
<div class="nt" style="font-size:20pt;line-height:1.8;text-align:center">ᬓᬂ · ᬓᬃ · ᬓᬄ · ᬓ᭄</div>
<div style="text-align:center"><i>kang · kar · kah · k</i></div></div>
<div class="box"><h3>Look closely!</h3>On these pages the big letter is the <b>last syllable</b> of the word, so you can find the
closing sign inside the word below it.</div>"""

SECTIONS = [
    section(LETTERS, label="LETTER", chip="PART 1", title="The 18 Letters", native="ᬳᬦᬘᬭᬓ",
            native_tr="hanacaraka — after the first five letters", intro_html=INTRO1, chart_title="letters (hanacaraka)",
            chart_cols=5, warmup_title="the 18 letters", warmup_cols=6),
    section(VOWELS, label="VOWEL SIGN", chip="PART 2", title="The Vowel Signs", native="ᬧᬗᬗ᭄ᬕᬾ ᬲ᭄ᬯᬭ",
            native_tr="pangangge suara — “vowel clothing”", intro_html=INTRO2, chart_title="vowel signs",
            chart_cols=5, warmup_title="the vowel signs", warmup_cols=4),
    section(CLOSERS, label="CLOSING SIGN", chip="PART 3", title="Closing Signs", native="ᬧᬗᬗ᭄ᬕᬾ ᬢᭂᬗᭂᬦᬦ᭄",
            native_tr="pangangge tengenan — “signs on the right”", intro_html=INTRO3, chart_title="closing signs",
            chart_cols=5, warmup_title="the closing signs", warmup_cols=4),
]

LANG = build(dict(
    code="ban", folder="book-53-balinese", series_no=53, isbn="", draft=True,
    name="Balinese", native="ᬩᬲᬩᬮᬶ", native_tr="basa Bali", name_word="ᬳᬤᬦ᭄ (adan)", write_word="ᬢᬸᬮᬶᬲ᭄ (tulis)",
    title_native="ᬫᬮᬚᬄ ᬅᬓ᭄ᬱᬭ ᬩᬮᬶ", title_letters="ᬳᬦᬘᬭᬓ", belongs_native="ᬦᬶᬓᬶ ᬩᬸᬓᬸ ᬢᬶᬬᬂ",
    belongs_pic="star", alphabet_native="ᬳᬦᬘᬭᬓ", numbers_native="ᬳᬂᬓ", numbers_tr="angka",
    phrases_native="ᬓ᭄ᬭᬸᬦ",
    fonts=fontset("Noto Sans Balinese", FONT, "Noto Sans Balinese", FONT)[:2],
    disp_family="Noto Sans Balinese", text_family="Noto Sans Balinese",
    glyph_font=f"{FONT}-700-normal.woff2", font_credit="Noto Sans Balinese",
    extra_css="h1{line-height:1.5} h2{line-height:1.85} h3{line-height:1.7} .lp-name{line-height:1.6} .lp-word .w{line-height:1.9} .dash .ntd{line-height:2 !important;padding-bottom:10px}",
    letters_word="Letters and Signs",
    phon_feature="a syllable chart for every letter (ᬓ <i>ka</i>, ᬓᬶ <i>ki</i>, ᬓᬸ <i>ku</i>…)",
    sections=SECTIONS,
    sound_notes=[
        "The English letters under each word are the <b>normal Latin spelling of Balinese</b>, the way it is written in "
        "Indonesia today. Every letter is said; vowels are short and pure.",
        "<b>e</b> (plain) is the quiet ‘uh’ in “about” (<i>pepet</i>). <b>é</b> is like ‘e’ in “bed”.",
        "<b>c</b> is always ‘ch’ as in “chair”: <i>cangkir</i> sounds like “chang-kir”.",
        "<b>ny</b> is ‘ny’ in “canyon”; <b>ng</b> is ‘ng’ in “sing”, even at the start of a syllable: <i>bunga</i> is “bu-nga”.",
        "In everyday speech an ‘a’ at the end of a word often sounds like a soft ‘uh’: <i>delima</i> is said “delimuh”. "
        "A <b>k</b> at the end of a word is a tiny catch in the throat."],
    phon_explain="For each letter, the box marked <i>Balinese phonetics</i> shows the letter wearing each vowel sign "
                 "(<span class='nt'>ᬓ ᬓᬶ ᬓᬸ</span> <i>ka ki ku</i>…) and with the <i>adeg-adeg</i> that takes the vowel away. "
                 "On the sign pages it shows the sign on a few letters.",
    standard="everyday Balinese as spoken in south Bali",
    hello=[
        ("Who speaks it?", "About <b>3 million people</b> speak Balinese as their first language.<sup>³</sup>"),
        ("Where?", "On the island of <b>Bali</b> in Indonesia, just east of Java, and in some villages on the islands of "
                   "<b>Lombok</b> and <b>Nusa Penida</b>."),
        ("How is it written?", "In Latin letters and in <b>Aksara Bali</b>, from <b>left to right</b>. Many shop and street signs "
                               "in Bali show both!"),
        ("How many letters?", "This book teaches the <b>18 basic letters</b>, <b>5 vowel signs</b> and <b>4 closing signs</b>."),
        ("Polite words", "Balinese has everyday words and extra-polite words for elders and guests: “thank you” is "
                         "<i>suksma</i>."),
        ("Did you know?", "Bali is famous for its green <b>rice terraces</b> that climb up the hills like giant steps. Some "
                          "Balinese villages, such as Pegayaman, are Muslim and have spoken Balinese for hundreds of years."),
    ],
    hello_pics=[("paddy", {}), ("mountain", {}), ("kite", {})],
    map=region_map(frame=[[112.9, -10.6], [117.5, -6.0]],
                   points=dict(denpasar=[115.22, -8.65], singaraja=[115.09, -8.11], negara=[114.62, -8.36],
                               amlapura=[115.61, -8.45]),
                   area=(115.12, -8.4, 175, 105), area_rot=-10,
                   cities=[("denpasar", "Denpasar", -14, 30, "end", False), ("singaraja", "Singaraja", 0, -16, "middle", False),
                           ("negara", "Negara", -14, 26, "end", False), ("amlapura", "Amlapura", 12, -14, "start", False)],
                   label="BALI", label_at=[115.15, -9.35], marker=[115.1, -8.4],
                   caption="The circle shows Bali on the world map.",
                   legend="<b>Color it:</b> Bali (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · "
                          "the seas <b>blue</b>. <b>Find it:</b> Balinese is spoken in Denpasar, Singaraja, Negara and Amlapura. "
                          "Java is the big island to the west; Lombok is to the east.",
                   seas=[("Bali Sea", 114.9, -6.55), ("Indian Ocean", 115.2, -10.1), ("Java", 113.7, -7.95),
                         ("Lombok", 116.32, -8.72)], world_r=10),
    digits=[("᭐", "ᬦᭀᬮ᭄", "nol", "zero"), ("᭑", "ᬩᭂᬲᬶᬓ᭄", "besik", "one"), ("᭒", "ᬤᬸᬯ", "dua", "two"), ("᭓", "ᬢᭂᬮᬸ", "telu", "three"),
            ("᭔", "ᬧᬧᬢ᭄", "papat", "four"), ("᭕", "ᬮᬶᬫ", "lima", "five"), ("᭖", "ᬦᭂᬫ᭄", "nem", "six"), ("᭗", "ᬧᬶᬢᬸ", "pitu", "seven"),
            ("᭘", "ᬓᬸᬢᬸᬲ᭄", "kutus", "eight"), ("᭙", "ᬲᬶᬬ", "sia", "nine")],
    phrases=[("ᬳᬲ᭄ᬲᬮᬫᬸ ᬳᬮᬿᬓᬸᬫ᭄", "assalamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ᬯᬳᬮᬿᬓᬸᬫ᭄ ᬲᬮᬫ᭄", "wa alaikum salam", "And upon you be peace (the reply)"),
             ("ᬳᬤᬦ᭄ ᬢᬶᬬᬗᬾ …", "adan tiange …", "My name is …"),
             ("ᬲᬸᬓ᭄ᬲ᭄ᬫ", "suksma", "Thank you"),
             ("ᬚᬚᬓᬮ᭄ᬮᬳᬸ ᬔᬿᬭᬦ᭄", "jazakallahu khairan", "May Allah reward you with good"),
             ("ᬫᬾᬫᬾ · ᬩᬧ", "mémé · bapa", "Mother · Father"),
             ("ᬩᬾᬮᬶ · ᬫ᭄ᬩᭀᬓ᭄", "béli · mbok", "Big brother · Big sister"),
             ("ᬗ᭄ᬕᬶᬄ · ᬢᭂᬦ᭄", "nggih · ten", "Yes · No"),
             ("ᬢᬶᬬᬂ ᬫᬮᬚᬄ ᬩᬲ ᬩᬮᬶ!", "tiang malajah basa Bali!", "I am learning Balinese!")],
    cheer=("ᬫᬲ᭄ᬬᬳᬮ᭄ᬮᬄ! ᬮᬸᬯᬸᬂ ᬧᭂᬲᬦ᭄!", "masya Allah! luung pesan!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), first-language speakers, rounded.",
    book_pic=dict(left="ᬳ ᬦ ᬘ", right="ᬭ ᬓ ᬤ"),
    review_note=("Balinese is a REVIEW DRAFT, drafted from less source material than the Javanese and Sundanese books. Please check: "
                 "(1) every word and its Aksara Bali spelling, especially alas, nasi, sampat, layangan, nyuh, ujan, ombak, sendok, "
                 "umah and ubad; (2) the sign names (ulu, suku, taleng, taleng tedong, pepet, cecek, surang, bisah, adeg-adeg) and "
                 "the section names pangangge suara / pangangge tengenan in the script; (3) the title “Malajah Aksara Bali” (ᬅᬓ᭄ᬱᬭ "
                 "spelling), “niki buku tiang” and the heading ᬓ᭄ᬭᬸᬦ; (4) the phrases: adan tiange, suksma (ᬲᬸᬓ᭄ᬲ᭄ᬫ), nggih · ten, "
                 "mémé · bapa, béli · mbok, luung pesan, and the Arabic phrases (ai written with ᬿ, kh with ᬔ, z written with ᬚ); "
                 "(5) the Pegayaman fact and the speaker number. No Hindu religious words or images are used; keep it that way."),
    tiles="ᬳᬦᬘᬭᬓᬤ", cover_pics=["mango", "kite", "corn", "umbrella"], title_size=48,
    speakers_blurb="Balinese is spoken by about 3 million people on the island of Bali in Indonesia.",
    sample_words=[("ᬮᬬᬗᬦ᭄", "layangan", "kite"), ("ᬜᬸᬄ", "nyuh", "coconut"), ("ᬩᬸᬮᬦ᭄", "bulan", "moon")],
    keywords=["balinese alphabet book for kids", "aksara bali coloring book", "learn balinese script for children",
              "indonesian heritage language workbook", "muslim kids activity book", "bali letters tracing toddlers",
              "hanacaraka coloring workbook"],
))
