# -*- coding: utf-8 -*-
"""Book 51 - Javanese (Aksara Jawa / Hanacaraka). Allamahul Bayan Series. REVIEW DRAFT.
Built with engine/generic.py: three sections - the 20 basic letters (aksara nglegena, in hanacaraka order),
the 5 vowel signs (sandhangan swara) and 4 closing signs (sandhangan panyigeg).
Transliteration = the normal Latin spelling of Javanese (e = pepet schwa, é/è = taling, dh/th = retroflex)."""
from generic import build, letter, section, fontset
from maps import region_map

FONT = "noto-sans-javanese-javanese"
V_SIGNS = [("", "a"), ("ꦶ", "i"), ("ꦸ", "u"), ("ꦺ", "é"), ("ꦼ", "e"), ("ꦺꦴ", "o")]
SPECIAL = {("ꦫ", "ꦼ"): "ꦉ", ("ꦭ", "ꦼ"): "ꦊ"}  # rê and lê have their own letters (pa cerek, nga lelet)


def cell(s, t, fs=16):
    return (f'<div style="text-align:center"><div class="nt" style="font-size:{fs}pt;line-height:1.45;padding-bottom:7px">{s}</div>'
            f'<div class="tr small" style="line-height:1.05">{t}</div></div>')


def grid(cells, cols=4):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:10px 4px;margin-top:2px">{"".join(cells)}</div>'


def syllables(ch, root):
    cells = [cell(SPECIAL.get((ch, s), ch + s), root + v) for s, v in V_SIGNS]
    cells.append(cell(ch + "꧀", root or "–"))
    return grid(cells)


PH = "Javanese phonetics · vowel signs + pangkon"


def A(ch, name, root, sound, word, tr, meaning, pic, args=None, note=None):
    return letter(ch, ch, name, sound, word, tr, meaning, pic, syllables(ch, root), PH, args, note)


def S(big, sign, name_nat, name, sound, word, tr, meaning, pic, examples, args=None, note=None, label=PH):
    ex = "".join(f'<div>{b} + ◌{sign} = {r} <span class="tr" style="font-family:Nunito;font-size:12pt">({t})</span></div>'
                 for b, r, t in examples)
    phon = (f'<div class="nt" style="font-size:26pt;line-height:1.45;text-align:center">◌{sign}</div>'
            f'<div class="nt" style="font-size:17pt;line-height:1.6;text-align:center">{ex}</div>')
    return letter(big, name_nat, name, sound, word, tr, meaning, pic, phon, label, args, note)


INSIDE = "Rarely first: find <span class='nt'>{}</span> inside <span class='nt'>{}</span>!"

LETTERS = [
    A("ꦲ", "ha", "h", "‘h’ as in “hat” — at the start of a word often just ‘a’", "ꦲꦭꦶꦲꦭꦶ", "ali-ali", "ring", "ring",
      note="At the start of a word <span class='nt'>ꦲ</span> often carries just a vowel: “a-li a-li”."),
    A("ꦤ", "na", "n", "‘n’ as in “net”", "ꦤꦤꦱ꧀", "nanas", "pineapple", "pineapple"),
    A("ꦕ", "ca", "c", "‘ch’ as in “chair”", "ꦕꦁꦏꦶꦂ", "cangkir", "cup", "teacup"),
    A("ꦫ", "ra", "r", "a tapped ‘r’ — flick the tongue once", "ꦫꦺꦴꦠꦶ", "roti", "bread", "roti"),
    A("ꦏ", "ka", "k", "‘k’ as in “kite”, with no puff of air", "ꦏꦼꦩ꧀ꦧꦁ", "kembang", "flower", "flower"),
    A("ꦢ", "da", "d", "a soft ‘d’ — the tongue touches the back of the teeth", "ꦢꦼꦭꦶꦩ", "delima", "pomegranate", "pomegranate"),
    A("ꦠ", "ta", "t", "a soft ‘t’ — the tongue touches the back of the teeth", "ꦠꦼꦧꦸ", "tebu", "sugarcane", "sugarcane"),
    A("ꦱ", "sa", "s", "‘s’ as in “sun”", "ꦱꦥꦸ", "sapu", "broom", "broom"),
    A("ꦮ", "wa", "w", "‘w’ as in “water”", "ꦮꦸꦭꦤ꧀", "wulan", "moon", "moon"),
    A("ꦭ", "la", "l", "‘l’ as in “lamp”", "ꦭꦮꦁ", "lawang", "door", "door"),
    A("ꦥ", "pa", "p", "‘p’ as in “pen”, with no puff of air", "ꦥꦶꦫꦶꦁ", "piring", "plate", "plate"),
    A("ꦝ", "dha", "dh", "a hard ‘d’ — curl the tongue back", "ꦝꦶꦁꦏ꧀ꦭꦶꦏ꧀", "dhingklik", "little stool", "stool"),
    A("ꦗ", "ja", "j", "‘j’ as in “jam”", "ꦗꦒꦸꦁ", "jagung", "corn", "corn"),
    A("ꦪ", "ya", "y", "‘y’ as in “yes”", "ꦥꦪꦸꦁ", "payung", "umbrella", "umbrella", note=INSIDE.format("ꦪ", "ꦥꦪꦸꦁ")),
    A("ꦚ", "nya", "ny", "‘ny’ as in “canyon”", "ꦧꦚꦸ", "banyu", "water", "water", note=INSIDE.format("ꦚ", "ꦧꦚꦸ")),
    A("ꦩ", "ma", "m", "‘m’ as in “moon”", "ꦩꦱ꧀ꦗꦶꦢ꧀", "masjid", "mosque", "mosque"),
    A("ꦒ", "ga", "g", "‘g’ as in “go”", "ꦒꦸꦤꦸꦁ", "gunung", "mountain", "mountain"),
    A("ꦧ", "ba", "b", "‘b’ as in “ball”", "ꦧꦤ꧀ꦠꦭ꧀", "bantal", "pillow", "pillow"),
    A("ꦛ", "tha", "th", "a hard ‘t’ — curl the tongue back (not the ‘th’ of “the”)", "ꦥꦼꦛꦶ", "pethi", "chest, big box", "box",
      note=INSIDE.format("ꦛ", "ꦥꦼꦛꦶ")),
    A("ꦔ", "nga", "ng", "‘ng’ as in “sing”, but at the start of a syllable", "ꦗꦔꦤ꧀", "jangan", "vegetable soup", "pot",
      note=INSIDE.format("ꦔ", "ꦗꦔꦤ꧀")),
]

SV = "Javanese phonetics · vowel sign"
VOWELS = [
    S("ꦲꦶ", "ꦶ", "ꦮꦸꦭꦸ", "wulu", "‘i’ as in “sit” (a little longer)", "ꦲꦶꦱꦸꦏ꧀", "isuk", "morning", "sunrise",
      [("ꦏ", "ꦏꦶ", "ki"), ("ꦤ", "ꦤꦶ", "ni")], label=SV),
    S("ꦲꦸ", "ꦸ", "ꦱꦸꦏꦸ", "suku", "‘u’ as in “put”", "ꦲꦸꦢꦤ꧀", "udan", "rain", "raincloud",
      [("ꦏ", "ꦏꦸ", "ku"), ("ꦱ", "ꦱꦸ", "su")], label=SV),
    S("ꦲꦺ", "ꦺ", "ꦠꦭꦶꦁ", "taling", "‘é’ like the ‘ay’ in “say” (short), or ‘è’ as in “bed”", "ꦲꦺꦱ꧀", "ès", "ice", "ice",
      [("ꦏ", "ꦏꦺ", "ké"), ("ꦩ", "ꦩꦺ", "mé")], label=SV,
      note="<i>Taling</i> is written <b>before</b> the letter, but said after it!"),
    S("ꦲꦼ", "ꦼ", "ꦥꦼꦥꦼꦠ꧀", "pepet", "a quiet ‘uh’, like the ‘a’ in “about”", "ꦲꦼꦤ꧀ꦝꦺꦴꦒ꧀", "endhog", "egg", "egg",
      [("ꦏ", "ꦏꦼ", "ke"), ("ꦠ", "ꦠꦼ", "te")], label=SV,
      note="With <span class='nt'>ꦫ</span> and <span class='nt'>ꦭ</span> Javanese uses special letters instead: "
           "<span class='nt'>ꦉ</span> <i>re</i> and <span class='nt'>ꦊ</span> <i>le</i>."),
    S("ꦲꦺꦴ", "ꦺꦴ", "ꦠꦭꦶꦁ ꦠꦫꦸꦁ", "taling tarung", "‘o’ as in “go”, said short", "ꦲꦺꦴꦩꦃ", "omah", "house", "house",
      [("ꦏ", "ꦏꦺꦴ", "ko"), ("ꦥ", "ꦥꦺꦴ", "po")], label=SV,
      note="Two pieces hug the letter: <span class='nt'>ꦺ</span> in front and <span class='nt'>ꦴ</span> behind."),
]

SC = "Javanese phonetics · closing sign"
CLOSERS = [
    S("ꦮꦁ", "ꦁ", "ꦕꦼꦕꦏ꧀", "cecak", "adds ‘ng’ as in “sing” to the end of a syllable", "ꦧꦮꦁ", "bawang", "onion", "onion",
      [("ꦏ", "ꦏꦁ", "kang"), ("ꦮ", "ꦮꦁ", "wang")], label=SC),
    S("ꦪꦂ", "ꦂ", "ꦭꦪꦂ", "layar", "adds ‘r’ to the end of a syllable", "ꦭꦪꦂ", "layar", "sail", "boat",
      [("ꦏ", "ꦏꦂ", "kar"), ("ꦪ", "ꦪꦂ", "yar")], label=SC,
      note="The sign <i>layar</i> means “sail” — and so does the word <span class='nt'>ꦭꦪꦂ</span>!"),
    S("ꦮꦃ", "ꦃ", "ꦮꦶꦒ꧀ꦚꦤ꧀", "wignyan", "adds a breathy ‘h’ to the end of a syllable", "ꦱꦮꦃ", "sawah", "rice field", "paddy",
      [("ꦏ", "ꦏꦃ", "kah"), ("ꦮ", "ꦮꦃ", "wah")], label=SC),
    S("ꦧ꧀", "꧀", "ꦥꦁꦏꦺꦴꦤ꧀", "pangkon", "takes the vowel away: ꦧ ba becomes just ‘b’", "ꦏꦶꦠꦧ꧀", "kitab", "book", "book",
      [("ꦏ", "ꦏ꧀", "k"), ("ꦧ", "ꦧ꧀", "b")], args=dict(left="ꦲ ꦤ ꦕ", right="ꦫ ꦏ ꦢ"), label=SC,
      note="Inside a word the next letter tucks under instead (a <i>pasangan</i>)."),
]

INTRO1 = """<p>Javanese has its own beautiful script: <b>Aksara Jawa</b>, also called <b>Hanacaraka</b> after its first five letters.
It is written from <b>left to right</b>, and the letters hang from an invisible line.</p>
<div class="box" style="margin:0.1in 0"><h3>20 letters, four little lines</h3>Children learn the 20 basic letters
(<i>aksara nglegena</i>) as four short lines, like a rhyme:
<div class="nt" style="font-size:20pt;line-height:1.7;margin-top:4px;text-align:center">ꦲꦤꦕꦫꦏ · ꦢꦠꦱꦮꦭ<br>ꦥꦝꦗꦪꦚ · ꦩꦒꦧꦛꦔ</div>
<div style="text-align:center"><i>ha na ca ra ka · da ta sa wa la · pa dha ja ya nya · ma ga ba tha nga</i></div></div>
<div class="box" style="margin:0.1in 0"><h3>Every letter says “a”</h3>Each letter is a whole syllable: <span class="nt">ꦏ</span> is
<i>ka</i>, not just <i>k</i>. In everyday Central Javanese the “a” often sounds like ‘o’ in “on”, so many children
recite <i>ho no co ro ko</i>.</div>
<div class="box"><h3>Change the vowel</h3>Small <b>vowel signs</b> (Part 2) change the “a”: <span class="nt">ꦏ ꦏꦶ ꦏꦸ ꦏꦺꦴ</span>
<i>ka ki ku ko</i>. Every letter page shows its whole family.</div>"""

INTRO2 = """<p>A vowel sign is called a <b>sandhangan</b> — a little piece of “clothing” that a letter puts on. It can sit
above the letter, below it, in front of it, or on both sides!</p>
<div class="box" style="margin:0.1in 0"><h3>Five vowel signs</h3>
<div class="nt" style="font-size:20pt;line-height:1.8;text-align:center">ꦏꦶ · ꦏꦸ · ꦏꦺ · ꦏꦼ · ꦏꦺꦴ</div>
<div style="text-align:center"><i>ki · ku · ké · ke · ko</i></div></div>
<div class="box" style="margin:0.1in 0"><h3>Words that start with a vowel</h3>In Javanese, a word that begins with a vowel is
written with the letter <span class="nt">ꦲ</span>: <span class="nt">ꦲꦸꦢꦤ꧀</span> <i>udan</i> (rain). So on these pages the big
letter is <span class="nt">ꦲ</span> wearing each sign.</div>
<div class="box"><h3>Special vowel letters</h3>Javanese also has separate vowel letters (<span class="nt">ꦄ ꦆ ꦈ ꦌ ꦎ</span>),
but they are used mostly for names and borrowed words, so this book keeps to the signs.</div>"""

INTRO3 = """<p>Some syllables end with a consonant: <i>ba-<b>wang</b></i>, <i>la-<b>yar</b></i>. Javanese closes them with
<b>sandhangan panyigeg</b> — four little closing signs.</p>
<div class="box" style="margin:0.1in 0"><h3>Four closing signs</h3>
<div class="nt" style="font-size:20pt;line-height:1.8;text-align:center">ꦏꦁ · ꦏꦂ · ꦏꦃ · ꦏ꧀</div>
<div style="text-align:center"><i>kang · kar · kah · k</i></div></div>
<div class="box"><h3>Look closely!</h3>On these pages the big letter is the <b>last syllable</b> of the word, so you can find the
closing sign inside the word below it.</div>"""

SECTIONS = [
    section(LETTERS, label="LETTER", chip="PART 1", title="The 20 Letters", native="ꦲꦏ꧀ꦱꦫ ꦔ꧀ꦭꦼꦒꦺꦤ",
            native_tr="aksara nglegena — “the bare letters”", intro_html=INTRO1, chart_title="letters (hanacaraka)",
            chart_cols=5, warmup_title="the 20 letters", warmup_cols=5),
    section(VOWELS, label="VOWEL SIGN", chip="PART 2", title="The Vowel Signs", native="ꦱꦤ꧀ꦝꦔꦤ꧀ ꦱ꧀ꦮꦫ",
            native_tr="sandhangan swara — “vowel clothing”", intro_html=INTRO2, chart_title="vowel signs (on ꦲ)",
            chart_cols=5, warmup_title="the vowel signs", warmup_cols=4),
    section(CLOSERS, label="CLOSING SIGN", chip="PART 3", title="Closing Signs", native="ꦥꦚꦶꦒꦼꦒ꧀",
            native_tr="sandhangan panyigeg — “closing clothing”", intro_html=INTRO3, chart_title="closing signs",
            chart_cols=5, warmup_title="the closing signs", warmup_cols=4),
]

LANG = build(dict(
    code="jv", folder="book-51-javanese", series_no=51, isbn="", draft=True,
    name="Javanese", native="ꦧꦱꦗꦮ", native_tr="basa Jawa", name_word="ꦗꦼꦤꦼꦁ (jeneng)", write_word="ꦠꦸꦭꦶꦱꦼꦤ꧀ (tulisen)",
    title_native="ꦱꦶꦤꦲꦸ ꦲꦏ꧀ꦱꦫ ꦗꦮ", title_letters="ꦲꦤꦕꦫꦏ", belongs_native="ꦧꦸꦏꦸ ꦲꦶꦏꦶ ꦢꦸꦮꦺꦏ꧀ꦏꦸ",
    belongs_pic="star", alphabet_native="ꦲꦤꦕꦫꦏ", numbers_native="ꦲꦁꦏ", numbers_tr="angka",
    phrases_native="ꦲꦪꦺꦴ ꦒꦸꦤꦼꦩꦤ꧀",
    fonts=fontset("Noto Sans Javanese", FONT, "Noto Sans Javanese", FONT)[:2],
    disp_family="Noto Sans Javanese", text_family="Noto Sans Javanese",
    glyph_font=f"{FONT}-700-normal.woff2", font_credit="Noto Sans Javanese",
    extra_css="h1,h2{line-height:1.5} h3{line-height:1.7} .lp-name{line-height:1.6} .dash .ntd{line-height:2 !important;padding-bottom:10px}",
    letters_word="Letters and Signs",
    phon_feature="a syllable chart for every letter (ꦏ <i>ka</i>, ꦏꦶ <i>ki</i>, ꦏꦸ <i>ku</i>…)",
    sections=SECTIONS,
    sound_notes=[
        "The English letters under each word are the <b>normal Latin spelling of Javanese</b>, the way it is written in "
        "Indonesia today. Every letter is said; vowels are short and pure.",
        "<b>e</b> (plain) is the quiet ‘uh’ in “about” (<i>pepet</i>). <b>é</b> is like ‘ay’ in “say” but short; <b>è</b> is ‘e’ in “bed”.",
        "<b>c</b> is always ‘ch’ as in “chair”: <i>cangkir</i> sounds like “chang-kir”.",
        "<b>dh</b> and <b>th</b> are a hard d and t with the tongue curled back. The h does <i>not</i> mean a puff of air, and "
        "<i>th</i> is never the English “th”. Plain <b>d</b> and <b>t</b> touch the back of the teeth.",
        "<b>ny</b> is ‘ny’ in “canyon”; <b>ng</b> is ‘ng’ in “sing”, even at the start of a syllable.",
        "In everyday Central Javanese an ‘a’ at the end of a word often sounds like ‘o’ in “on”: <i>Jawa</i> is said “Jowo”, "
        "<i>delima</i> “delimo”. A <b>k</b> at the end of a word is a tiny catch in the throat."],
    phon_explain="For each letter, the box marked <i>Javanese phonetics</i> shows the letter wearing each vowel sign "
                 "(<span class='nt'>ꦏ ꦏꦶ ꦏꦸ</span> <i>ka ki ku</i>…) and with the <i>pangkon</i> that takes the vowel away — "
                 "the way Javanese children practise their letters. On the sign pages it shows the sign on a few letters.",
    standard="Central Javanese (Yogyakarta and Surakarta), everyday <i>ngoko</i> words",
    hello=[
        ("Who speaks it?", "About <b>68 million people</b> speak Javanese as their first language — more than any other language "
                           "of Indonesia.<sup>³</sup>"),
        ("Where?", "On the island of <b>Java</b> in Indonesia, mostly in Central and East Java, and in Javanese families in "
                   "Sumatra, Malaysia and even <b>Suriname</b> in South America."),
        ("How is it written?", "In <b>Aksara Jawa</b> (Hanacaraka), from <b>left to right</b>. Today Javanese is mostly written in Latin "
                               "letters, but you can still see the old script on street signs in Yogyakarta."),
        ("How many letters?", "This book teaches the <b>20 basic letters</b>, <b>5 vowel signs</b> and <b>4 closing signs</b>."),
        ("Polite words", "Javanese has everyday words (<i>ngoko</i>) and extra-polite words (<i>krama</i>) for speaking to "
                         "elders: “thank you” is <i>matur nuwun</i>."),
        ("Did you know?", "In the <i>pesantren</i> (Islamic boarding schools) of Java, Javanese was also written in Arabic letters, "
                          "called <b>Pegon</b>."),
    ],
    hello_pics=[("paddy", {}), ("mountain", {}), ("mosque", {})],
    map=region_map(frame=[[104.5, -13.0], [116.5, -1.0]],
                   points=dict(yogya=[110.37, -7.80], solo=[110.82, -7.57], semarang=[110.42, -6.97], surabaya=[112.75, -7.25],
                               jakarta=[106.85, -6.21]),
                   area=(111.7, -7.45, 270, 66), area_rot=6,
                   cities=[("yogya", "Yogyakarta", -12, 34, "end", False), ("solo", "Surakarta", 12, 34, "start", False),
                           ("semarang", "Semarang", 0, -18, "middle", False), ("surabaya", "Surabaya", 14, -12, "start", False),
                           ("jakarta", "Jakarta", 0, -22, "middle", True)],
                   label="JAVA", label_at=[110.5, -9.6], marker=[110.0, -7.5],
                   caption="The circle shows Java on the world map.",
                   legend="<b>Color it:</b> Central and East Java (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · "
                          "the seas <b>blue</b>. <b>Find it:</b> Javanese is spoken in Yogyakarta, Surakarta (Solo), Semarang and Surabaya. "
                          "Jakarta ★ is Indonesia’s capital.",
                   seas=[("Java Sea", 110.5, -4.6), ("Indian Ocean", 110.5, -11.6)]),
    digits=[("꧐", "ꦤꦺꦴꦭ꧀", "nol", "zero"), ("꧑", "ꦱꦶꦗꦶ", "siji", "one"), ("꧒", "ꦭꦺꦴꦫꦺꦴ", "loro", "two"), ("꧓", "ꦠꦼꦭꦸ", "telu", "three"),
            ("꧔", "ꦥꦥꦠ꧀", "papat", "four"), ("꧕", "ꦭꦶꦩ", "lima", "five"), ("꧖", "ꦤꦼꦤꦼꦩ꧀", "nenem", "six"), ("꧗", "ꦥꦶꦠꦸ", "pitu", "seven"),
            ("꧘", "ꦮꦺꦴꦭꦸ", "wolu", "eight"), ("꧙", "ꦱꦔ", "sanga", "nine")],
    phrases=[("ꦲꦱ꧀ꦱꦭꦩꦸ ꦲꦭꦻꦏꦸꦩ꧀", "assalamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ꦮꦲꦭꦻꦏꦸꦩ꧀ ꦱꦭꦩ꧀", "wa alaikum salam", "And upon you be peace (the reply)"),
             ("ꦗꦼꦤꦼꦁꦏꦸ …", "jenengku …", "My name is …"),
             ("ꦩꦠꦸꦂ ꦤꦸꦮꦸꦤ꧀", "matur nuwun", "Thank you"),
             ("ꦗꦗ꦳ꦏꦭ꧀ꦭꦲꦸ ꦏ꦳ꦻꦫꦤ꧀", "jazakallahu khairan", "May Allah reward you with good"),
             ("ꦲꦶꦧꦸ · ꦧꦥꦏ꧀", "ibu · bapak", "Mother · Father"),
             ("ꦩꦱ꧀ · ꦩ꧀ꦧꦏ꧀", "mas · mbak", "Big brother · Big sister"),
             ("ꦲꦶꦪ · ꦲꦺꦴꦫ", "iya · ora", "Yes · No"),
             ("ꦲꦏꦸ ꦭꦒꦶ ꦱꦶꦤꦲꦸ ꦧꦱ ꦗꦮ!", "aku lagi sinau basa Jawa!", "I am learning Javanese!")],
    cheer=("ꦩꦱꦾꦲꦭ꧀ꦭꦃ! ꦲꦥꦶꦏ꧀ ꦠꦼꦤꦤ꧀!", "masya Allah! apik tenan!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), first-language speakers, rounded.",
    book_pic=dict(left="ꦲ ꦤ ꦕ", right="ꦫ ꦏ ꦢ"),
    review_note=("Javanese is a REVIEW DRAFT. Please check: (1) the words for ꦛ tha (pethi), ꦔ nga (jangan), ꦝ dha (dhingklik) "
                 "and the use of ꦲ for word-initial vowels (isuk, udan, ès, endhog, omah, ali-ali); (2) the spellings of "
                 "loan and Arabic words in the phrases (assalamu alaikum with dirga mure ꦻ, jazakallahu khairan with cecak telu "
                 "ꦗ꦳ ꦏ꦳, masya Allah with pengkal); (3) whether spaces and final pangkon in the phrases are acceptable for "
                 "children’s material; (4) the title “Sinau Aksara Jawa” and “buku iki duwèkku”; (5) é/è/e marking in the "
                 "Latin spelling; (6) speaker number."),
    tiles="ꦲꦤꦕꦫꦏꦢ", cover_pics=["pineapple", "umbrella", "corn", "mosque"], title_size=48,
    speakers_blurb="Javanese is spoken by about 68 million people on the island of Java in Indonesia and around the world.",
    sample_words=[("ꦏꦼꦩ꧀ꦧꦁ", "kembang", "flower"), ("ꦗꦒꦸꦁ", "jagung", "corn"), ("ꦒꦸꦤꦸꦁ", "gunung", "mountain")],
    keywords=["javanese alphabet book for kids", "aksara jawa hanacaraka coloring", "learn javanese script for children",
              "indonesian heritage language workbook", "muslim kids activity book", "islamic coloring book for children",
              "javanese letters tracing toddlers"],
))
