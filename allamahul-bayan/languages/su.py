# -*- coding: utf-8 -*-
"""Book 52 - Sundanese (Aksara Sunda Baku). Allamahul Bayan Series. REVIEW DRAFT.
Built with engine/generic.py: three sections - the 7 vowel letters (aksara swara), the 18 consonant letters
(aksara ngalagena, in the standard ka-ga-nga order) and 4 closing signs (rarangken).
Transliteration = the normal Latin spelling of Sundanese (e = pepet schwa, é = taling, eu = Sundanese eu)."""
from generic import build, letter, section, fontset
from maps import region_map

FONT = "noto-sans-sundanese-sundanese"
V_SIGNS = [("", "a"), ("ᮤ", "i"), ("ᮥ", "u"), ("ᮦ", "é"), ("ᮧ", "o"), ("ᮨ", "e"), ("ᮩ", "eu")]


def cell(s, t, fs=16):
    return (f'<div style="text-align:center"><div class="nt" style="font-size:{fs}pt;line-height:1.45;padding-bottom:6px">{s}</div>'
            f'<div class="tr small" style="line-height:1.05">{t}</div></div>')


def grid(cells, cols=4):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:9px 4px;margin-top:2px">{"".join(cells)}</div>'


def syllables(ch, root):
    cells = [cell(ch + s, root + v) for s, v in V_SIGNS]
    cells.append(cell(ch + "᮪", root))
    return grid(cells)


PH = "Sundanese phonetics · vowel signs + pamaéh"


def K(ch, name, root, sound, word, tr, meaning, pic, args=None, note=None):
    return letter(ch, ch, name, sound, word, tr, meaning, pic, syllables(ch, root), PH, args, note)


def phon_sign(sign, examples):
    ex = "".join(f'<div>{b} + ◌{sign} = {r} <span class="tr" style="font-family:Nunito;font-size:12pt">({t})</span></div>'
                 for b, r, t in examples)
    return (f'<div class="nt" style="font-size:26pt;line-height:1.45;text-align:center">◌{sign}</div>'
            f'<div class="nt" style="font-size:17pt;line-height:1.6;text-align:center">{ex}</div>')


PV = "Sundanese phonetics · its vowel sign"


def V(ch, name, sound, sign, sign_nat, sign_name, word, tr, meaning, pic, args=None, note=None):
    if sign:
        phon = (f'<div class="small">After a consonant it becomes the sign <b>{sign_name}</b> '
                f'(<span class="nt">{sign_nat}</span>):</div>' + phon_sign(sign, [("ᮊ", "ᮊ" + sign, "k" + name), ("ᮘ", "ᮘ" + sign, "b" + name)]))
    else:
        phon = ('<div style="font-size:12pt">No sign needed! Every consonant already says <i>a</i>:</div>'
                '<div class="nt" style="font-size:22pt;line-height:1.7;text-align:center">ᮊ ᮘ ᮙ</div>'
                '<div class="tr" style="text-align:center">ka · ba · ma</div>')
    return letter(ch, ch, name, sound, word, tr, meaning, pic, phon, PV, args, note)


PC = "Sundanese phonetics · closing sign"


def S(big, sign, name_nat, name, sound, word, tr, meaning, pic, examples, args=None, note=None):
    return letter(big, name_nat, name, sound, word, tr, meaning, pic, phon_sign(sign, examples), PC, args, note)


VOWELS = [
    V("ᮃ", "a", "‘a’ as in “father”, said short", "", "", "", "ᮃᮀᮌᮥᮁ", "anggur", "grapes", "grapes"),
    V("ᮆ", "é", "‘é’ like the ‘e’ in “bed”, a little longer", "ᮦ", "ᮕᮔᮦᮜᮦᮀ", "panéléng", "ᮆᮞ᮪", "és", "ice", "ice"),
    V("ᮄ", "i", "‘i’ as in “sit”, a little longer", "ᮤ", "ᮕᮀᮠᮥᮜᮥ", "panghulu", "ᮄᮙᮂ", "imah", "house", "house"),
    V("ᮇ", "o", "‘o’ as in “go”, said short", "ᮧ", "ᮕᮔᮧᮜᮧᮀ", "panolong", "ᮇᮘᮒ᮪", "obat", "medicine", "medicine"),
    V("ᮅ", "u", "‘u’ as in “put”", "ᮥ", "ᮕᮑᮥᮊᮥ", "panyuku", "ᮅᮚᮂ", "uyah", "salt", "salt", args=dict(label="ᮅᮚᮂ")),
    V("ᮈ", "e", "a quiet ‘uh’, like the ‘a’ in “about”", "ᮨ", "ᮕᮙᮨᮕᮨᮒ᮪", "pamepet", "ᮈᮔ᮪ᮓᮧᮌ᮪", "endog", "egg", "egg"),
    V("ᮉ", "eu", "a special Sundanese vowel: say ‘oo’ but keep your lips flat, as if smiling", "ᮩ", "ᮕᮔᮩᮜᮩᮀ", "paneuleung",
      "ᮉᮔ᮪ᮒᮩᮀ", "eunteung", "mirror", "mirror"),
]

CONS = [
    K("ᮊ", "ka", "k", "‘k’ as in “kite”, with no puff of air", "ᮊᮜᮕ", "kalapa", "coconut", "coconut"),
    K("ᮌ", "ga", "g", "‘g’ as in “go”", "ᮌᮥᮔᮥᮀ", "gunung", "mountain", "mountain"),
    K("ᮍ", "nga", "ng", "‘ng’ as in “sing”, but at the start of a syllable", "ᮞᮍᮥ", "sangu", "cooked rice", "rice",
      note="Find <span class='nt'>ᮍ</span> inside <span class='nt'>ᮞᮍᮥ</span>!"),
    K("ᮎ", "ca", "c", "‘ch’ as in “chair”", "ᮎᮄ", "cai", "water", "water"),
    K("ᮏ", "ja", "j", "‘j’ as in “jam”", "ᮏᮌᮧᮀ", "jagong", "corn", "corn"),
    K("ᮑ", "nya", "ny", "‘ny’ as in “canyon”", "ᮑᮤᮛᮥ", "nyiru", "round bamboo tray (for rice)", "su_nyiru"),
    K("ᮒ", "ta", "t", "a soft ‘t’ — the tongue touches the back of the teeth", "ᮒᮀᮊᮜ᮪", "tangkal", "tree", "tree"),
    K("ᮓ", "da", "d", "a soft ‘d’ — the tongue touches the back of the teeth", "ᮓᮜᮤᮙ", "dalima", "pomegranate", "pomegranate"),
    K("ᮔ", "na", "n", "‘n’ as in “net”", "ᮔᮔᮞ᮪", "nanas", "pineapple", "pineapple"),
    K("ᮕ", "pa", "p", "‘p’ as in “pen”, with no puff of air", "ᮕᮛᮦ", "paré", "rice plant", "paddy"),
    K("ᮘ", "ba", "b", "‘b’ as in “ball”", "ᮘᮥᮜᮔ᮪", "bulan", "moon", "moon"),
    K("ᮙ", "ma", "m", "‘m’ as in “moon”", "ᮙᮞᮤᮌᮤᮒ᮪", "masigit", "mosque", "mosque"),
    K("ᮚ", "ya", "y", "‘y’ as in “yes”", "ᮕᮚᮥᮀ", "payung", "umbrella", "umbrella",
      note="Rarely first: find <span class='nt'>ᮚ</span> inside <span class='nt'>ᮕᮚᮥᮀ</span>!"),
    K("ᮛ", "ra", "r", "a tapped ‘r’ — flick the tongue once", "ᮛᮧᮒᮤ", "roti", "bread", "roti"),
    K("ᮜ", "la", "l", "‘l’ as in “lamp”", "ᮜᮝᮀ", "lawang", "door", "door"),
    K("ᮝ", "wa", "w", "‘w’ as in “water”", "ᮝᮧᮁᮒᮨᮜ᮪", "wortel", "carrot", "carrot"),
    K("ᮞ", "sa", "s", "‘s’ as in “sun”", "ᮞᮕᮥ", "sapu", "broom", "broom"),
    K("ᮠ", "ha", "h", "‘h’ as in “hat”", "ᮠᮥᮏᮔ᮪", "hujan", "rain", "raincloud"),
]

CLOSERS = [
    S("ᮝᮀ", "ᮀ", "ᮕᮑᮨᮎᮨᮊ᮪", "panyecek", "adds ‘ng’ as in “sing” to the end of a syllable", "ᮘᮝᮀ", "bawang", "onion", "onion",
      [("ᮊ", "ᮊᮀ", "kang"), ("ᮝ", "ᮝᮀ", "wang")]),
    S("ᮊᮤᮁ", "ᮁ", "ᮕᮀᮜᮚᮁ", "panglayar", "adds ‘r’ to the end of a syllable", "ᮎᮀᮊᮤᮁ", "cangkir", "cup", "teacup",
      [("ᮊ", "ᮊᮁ", "kar"), ("ᮊᮤ", "ᮊᮤᮁ", "kir")]),
    S("ᮃᮂ", "ᮂ", "ᮕᮀᮝᮤᮞᮓ᮪", "pangwisad", "adds a breathy ‘h’ to the end of a syllable", "ᮘᮥᮃᮂ", "buah", "fruit", "apple",
      [("ᮊ", "ᮊᮂ", "kah"), ("ᮃ", "ᮃᮂ", "ah")]),
    S("ᮘ᮪", "᮪", "ᮕᮙᮆᮂ", "pamaéh", "takes the vowel away: ᮘ ba becomes just ‘b’", "ᮊᮤᮒᮘ᮪", "kitab", "book", "book",
      [("ᮊ", "ᮊ᮪", "k"), ("ᮘ", "ᮘ᮪", "b")], args=dict(left="ᮃ ᮆ ᮄ", right="ᮊ ᮌ ᮍ"),
      note="<i>Pamaéh</i> means “the one that stills” the vowel."),
]

INTRO1 = """<p>Sundanese has its own neat, upright script: <b>Aksara Sunda</b>. It is written from <b>left to right</b>.
The script in this book is the modern standard form, <b>Aksara Sunda Baku</b>, that children learn at school in West Java.</p>
<div class="box" style="margin:0.1in 0"><h3>Seven vowels</h3>Sundanese has <b>7 vowels</b> — two more than English letters can show!
<div class="nt" style="font-size:22pt;line-height:1.7;text-align:center">ᮃ ᮆ ᮄ ᮇ ᮅ ᮈ ᮉ</div>
<div style="text-align:center"><i>a · é · i · o · u · e · eu</i></div></div>
<div class="box"><h3>Two shapes</h3>At the start of a word a vowel is a <b>full letter</b>: <span class="nt">ᮄᮙᮂ</span> <i>imah</i>.
After a consonant it becomes a small <b>sign</b> (<i>rarangkén</i>): <span class="nt">ᮊ + ◌ᮤ = ᮊᮤ</span> <i>ki</i>.</div>"""

INTRO2 = """<p>The consonant letters are called <b>aksara ngalagena</b>. Each one says a whole syllable with <i>a</i>:
<span class="nt">ᮊ</span> is <i>ka</i>, not just <i>k</i>.</p>
<div class="box" style="margin:0.1in 0"><h3>18 letters in threes</h3>Children learn them in little groups of three:
<div class="nt" style="font-size:20pt;line-height:1.7;margin-top:4px;text-align:center">ᮊᮌᮍ · ᮎᮏᮑ · ᮒᮓᮔ<br>ᮕᮘᮙ · ᮚᮛᮜ · ᮝᮞᮠ</div>
<div style="text-align:center"><i>ka ga nga · ca ja nya · ta da na · pa ba ma · ya ra la · wa sa ha</i></div></div>
<div class="box"><h3>Borrowed sounds</h3>Seven more letters write sounds from Arabic and other languages:
<span class="nt">ᮖ ᮗ ᮋ ᮟ ᮐ ᮮ ᮯ</span> <i>fa va qa xa za kha sya</i>. You will meet <span class="nt">ᮐ</span> and
<span class="nt">ᮮ</span> in “jazakallahu khairan” on the phrases page!</div>"""

INTRO3 = """<p>Some syllables end with a consonant: <i>ba-<b>wang</b></i>, <i>cang-<b>kir</b></i>. Sundanese closes them with
small signs, also called <b>rarangkén</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Four closing signs</h3>
<div class="nt" style="font-size:22pt;line-height:1.8;text-align:center">ᮊᮀ · ᮊᮁ · ᮊᮂ · ᮊ᮪</div>
<div style="text-align:center"><i>kang · kar · kah · k</i></div></div>
<div class="box"><h3>Look closely!</h3>On these pages the big letter is the <b>last syllable</b> of the word, so you can find the
closing sign inside the word below it.</div>"""

SECTIONS = [
    section(VOWELS, label="VOWEL", chip="PART 1", title="The Vowels", native="ᮃᮊ᮪ᮞᮛ ᮞ᮪ᮝᮛ",
            native_tr="aksara swara — “voice letters”", intro_html=INTRO1, chart_title="vowels",
            chart_cols=7, warmup_title="the vowels", warmup_cols=4),
    section(CONS, label="CONSONANT", chip="PART 2", title="The Consonants", native="ᮃᮊ᮪ᮞᮛ ᮍᮜᮌᮨᮔ",
            native_tr="aksara ngalagena", intro_html=INTRO2, chart_title="consonants",
            chart_cols=6, warmup_title="the consonants", warmup_cols=6),
    section(CLOSERS, label="CLOSING SIGN", chip="PART 3", title="Closing Signs", native="ᮛᮛᮀᮊᮦᮔ᮪",
            native_tr="rarangkén — “the little signs”", intro_html=INTRO3, chart_title="closing signs",
            chart_cols=7, warmup_title="the closing signs", warmup_cols=4),
]

LANG = build(dict(
    code="su", folder="book-52-sundanese", series_no=52, isbn="", draft=True,
    name="Sundanese", native="ᮘᮞ ᮞᮥᮔ᮪ᮓ", native_tr="basa Sunda", name_word="ᮍᮛᮔ᮪ (ngaran)", write_word="ᮒᮥᮜᮤᮞ᮪ (tulis)",
    title_native="ᮓᮤᮃᮏᮁ ᮃᮊ᮪ᮞᮛ ᮞᮥᮔ᮪ᮓ", title_letters="ᮃᮄᮊᮌᮍ", belongs_native="ᮄᮉ ᮘᮥᮊᮥ ᮃᮘ᮪ᮓᮤ",
    belongs_pic="star", alphabet_native="ᮃᮊ᮪ᮞᮛ ᮞᮥᮔ᮪ᮓ", numbers_native="ᮃᮀᮊ", numbers_tr="angka",
    phrases_native="ᮊᮨᮎᮕ᮪ ᮙᮥᮀᮌᮛᮔ᮪",
    fonts=fontset("Noto Sans Sundanese", FONT, "Noto Sans Sundanese", FONT)[:2],
    disp_family="Noto Sans Sundanese", text_family="Noto Sans Sundanese",
    glyph_font=f"{FONT}-700-normal.woff2", font_credit="Noto Sans Sundanese",
    extra_css="h1,h2{line-height:1.45} h3{line-height:1.6} .lp-name{line-height:1.5}",
    letters_word="Letters and Signs",
    phon_feature="a syllable chart for every letter (ᮊ <i>ka</i>, ᮊᮤ <i>ki</i>, ᮊᮥ <i>ku</i>…)",
    sections=SECTIONS,
    sound_notes=[
        "The English letters under each word are the <b>normal Latin spelling of Sundanese</b>, the way it is written in "
        "Indonesia today. Every letter is said; vowels are short and pure.",
        "<b>e</b> (plain) is the quiet ‘uh’ in “about”. <b>é</b> is like ‘e’ in “bed”. <b>eu</b> is one special sound: say ‘oo’ "
        "with your lips flat, as if smiling.",
        "<b>c</b> is always ‘ch’ as in “chair”: <i>cai</i> sounds like “chah-ee”.",
        "<b>ny</b> is ‘ny’ in “canyon”; <b>ng</b> is ‘ng’ in “sing”, even at the start of a syllable: <i>sangu</i> is “sa-ngu”.",
        "<b>t</b> and <b>d</b> are soft, with the tongue on the back of the teeth; <b>k</b> and <b>p</b> have no puff of air. "
        "A <b>k</b> at the end of a word is a tiny catch in the throat."],
    phon_explain="For each consonant, the box marked <i>Sundanese phonetics</i> shows the letter wearing each vowel sign "
                 "(<span class='nt'>ᮊ ᮊᮤ ᮊᮥ</span> <i>ka ki ku</i>…) and with the <i>pamaéh</i> that takes the vowel away. "
                 "On a vowel page it shows the small sign the vowel turns into after a consonant.",
    standard="standard Sundanese as taught in West Java (Priangan / Bandung)",
    hello=[
        ("Who speaks it?", "About <b>32 million people</b> speak Sundanese as their first language — the second-largest "
                           "language of Indonesia.<sup>³</sup>"),
        ("Where?", "In the western part of the island of <b>Java</b> in Indonesia: the provinces of <b>West Java</b> and "
                   "<b>Banten</b>, around the city of Bandung."),
        ("How is it written?", "Today mostly in Latin letters, and also in <b>Aksara Sunda</b>, from <b>left to right</b>. "
                               "You can see Aksara Sunda on street signs in Bandung."),
        ("How many letters?", "This book teaches <b>7 vowels</b>, <b>18 consonants</b> and <b>4 closing signs</b>."),
        ("Polite words", "Sundanese has everyday words and extra-polite words (<i>basa lemes</i>) for elders and guests: "
                         "“thank you” is <i>hatur nuhun</i>."),
        ("Did you know?", "Numbers in Aksara Sunda are written between two little lines, so they are not mistaken for "
                          "letters: <span class='nt'>|᮲᮰᮲᮶|</span> is 2026."),
    ],
    hello_pics=[("paddy", {}), ("mountain", {}), ("mosque", {})],
    map=region_map(frame=[[104.0, -10.5], [110.5, -4.0]],
                   points=dict(bandung=[107.61, -6.91], bogor=[106.80, -6.60], cirebon=[108.55, -6.71],
                               tasik=[108.22, -7.33], jakarta=[106.85, -6.21]),
                   area=(107.3, -6.95, 300, 105), area_rot=10,
                   cities=[("bandung", "Bandung", 14, 26, "start", False), ("bogor", "Bogor", -14, 22, "end", False),
                           ("cirebon", "Cirebon", 12, -12, "start", False), ("tasik", "Tasikmalaya", 12, 28, "start", False),
                           ("jakarta", "Jakarta", -10, -18, "end", True)],
                   label="WEST JAVA", label_at=[107.3, -8.7], marker=[107.5, -7.0],
                   caption="The circle shows West Java on the world map.",
                   legend="<b>Color it:</b> West Java and Banten (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · "
                          "the seas <b>blue</b>. <b>Find it:</b> Sundanese is spoken in Bandung, Bogor, Tasikmalaya and around Cirebon. "
                          "Jakarta ★ is Indonesia’s capital.",
                   seas=[("Java Sea", 107.8, -5.0), ("Indian Ocean", 107.3, -9.8)], world_r=11),
    digits=[("᮰", "ᮔᮧᮜ᮪", "nol", "zero"), ("᮱", "ᮠᮤᮏᮤ", "hiji", "one"), ("᮲", "ᮓᮥᮃ", "dua", "two"), ("᮳", "ᮒᮤᮜᮥ", "tilu", "three"),
            ("᮴", "ᮇᮕᮒ᮪", "opat", "four"), ("᮵", "ᮜᮤᮙ", "lima", "five"), ("᮶", "ᮌᮨᮔᮨᮕ᮪", "genep", "six"), ("᮷", "ᮒᮥᮏᮥᮂ", "tujuh", "seven"),
            ("᮸", "ᮓᮜᮕᮔ᮪", "dalapan", "eight"), ("᮹", "ᮞᮜᮕᮔ᮪", "salapan", "nine")],
    phrases=[("ᮃᮞ᮪ᮞᮜᮙᮥ ᮃᮜᮄᮊᮥᮙ᮪", "assalamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ᮝᮃᮜᮄᮊᮥᮙ᮪ ᮞᮜᮙ᮪", "wa alaikum salam", "And upon you be peace (the reply)"),
             ("ᮔᮙᮤ ᮃᮘ᮪ᮓᮤ …", "nami abdi …", "My name is …"),
             ("ᮠᮒᮥᮁ ᮔᮥᮠᮥᮔ᮪", "hatur nuhun", "Thank you"),
             ("ᮏᮐᮊᮜ᮪ᮜᮠᮥ ᮮᮄᮛᮔ᮪", "jazakallahu khairan", "May Allah reward you with good"),
             ("ᮄᮘᮥ · ᮘᮕ", "ibu · bapa", "Mother · Father"),
             ("ᮃᮊᮀ · ᮒᮦᮒᮨᮂ", "akang · téteh", "Big brother · Big sister"),
             ("ᮙᮥᮠᮥᮔ᮪ · ᮠᮨᮔ᮪ᮒᮩ", "muhun · henteu", "Yes · No"),
             ("ᮃᮘ᮪ᮓᮤ ᮔᮥᮏᮥ ᮓᮤᮃᮏᮁ ᮘᮞ ᮞᮥᮔ᮪ᮓ!", "abdi nuju diajar basa Sunda!", "I am learning Sundanese!")],
    cheer=("ᮙᮯ ᮃᮜ᮪ᮜᮂ! ᮞᮆ ᮕᮤᮞᮔ᮪!", "masya Allah! saé pisan!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), first-language speakers, rounded.",
    book_pic=dict(left="ᮃ ᮆ ᮄ", right="ᮊ ᮌ ᮍ"),
    review_note=("Sundanese is a REVIEW DRAFT. Please check: (1) the order of the vowels (a é i o u e eu) and of the consonants; "
                 "(2) the words nyiru, sangu, paré, masigit, eunteung, buah and their spellings in Aksara Sunda; (3) the rarangkén "
                 "names (panghulu, panyuku, panéléng, panolong, pamepet, paneuleung, panyecek, panglayar, pangwisad, pamaéh) and their "
                 "spelling in the script; (4) the phrases, especially jazakallahu khairan (ᮐ za, ᮮ kha), masya Allah (ᮯ sya), the "
                 "lemes forms (nami abdi, muhun, nuju) and ibu · bapa / akang · téteh; (5) the title “Diajar Aksara Sunda” and "
                 "“Ieu buku abdi”; (6) the speaker number."),
    tiles="ᮃᮄᮊᮌᮙᮞ", cover_pics=["pineapple", "umbrella", "corn", "mosque"], title_size=46,
    speakers_blurb="Sundanese is spoken by about 32 million people in West Java, Indonesia.",
    sample_words=[("ᮘᮥᮜᮔ᮪", "bulan", "moon"), ("ᮏᮌᮧᮀ", "jagong", "corn"), ("ᮌᮥᮔᮥᮀ", "gunung", "mountain")],
    keywords=["sundanese alphabet book for kids", "aksara sunda coloring book", "learn sundanese script for children",
              "indonesian heritage language workbook", "muslim kids activity book", "islamic coloring book for children",
              "west java sunda letters tracing"],
))
