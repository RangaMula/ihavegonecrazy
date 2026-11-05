# -*- coding: utf-8 -*-
"""Book 61 - Vai (Liberia, Sierra Leone) in the Vai syllabary. Allamahul Bayan Series. REVIEW DRAFT.

The Vai syllabary has about 200 signs: 7 vowel columns x about 30 consonant rows, plus nasal syllables
and a few word signs. This book teaches a core of 56: the 7 vowels and 7 common consonant rows (b t k l m s n),
one section per row, in the column order of the standard chart (the same order computers use):
    ɛ  i  a  ɔ  u  o  e

HONESTY NOTE: we could not confirm a reliable, child-friendly Vai example word for most syllables, so those
pages show the syllable on a writing slate and say so in a note, instead of inventing a word. A Vai speaker
should add one word (with a picture of an object, plant or nature) per syllable."""
import unicodedata
from generic import build, letter, section, fontset
from maps import region_map

VOWELS = [("EE", "ɛ", "eh", "‘e’ as in “bed”"), ("I", "i", "ee", "‘ee’ as in “see”"), ("A", "a", "ah", "‘a’ as in “father”"),
          ("OO", "ɔ", "aw", "‘aw’ as in “saw”"), ("U", "u", "oo", "‘oo’ as in “moon”"),
          ("O", "o", "oh", "‘o’ as in “go”, short and pure"), ("E", "e", "ay", "‘ay’ as in “day”, short and pure")]
ROWS = [("", ""), ("B", "‘b’ as in “ball”"), ("T", "‘t’ as in “top”"), ("K", "‘k’ as in “kite”"),
        ("L", "‘l’ as in “lamp”"), ("M", "‘m’ as in “moon”"), ("S", "‘s’ as in “sun”"), ("N", "‘n’ as in “net”")]


def syl(c, v):
    return unicodedata.lookup(f"VAI SYLLABLE {c}{v}")


def row_chars(c):
    return [syl(c, v[0]) for v in VOWELS]


NOWORD = "We have not yet found a sure Vai word for this syllable, so we did not guess: a Vai speaker will add one."
WORDS = {  # the few example words we are confident about: syllable -> (word, transliteration, meaning, pic, args, note)
    "ꔤ": ("ꕙꔤ", "VAH-ee", "Vai — the name of the language and its people", "book",
          dict(left="ꕉ ꔤ ꖕ", right="ꕒ ꔬ ꖝ"), 'Find <span class="nt">ꔤ</span> at the end of <span class="nt">ꕙꔤ</span>!'),
}


def item(c, k, rowdesc):
    v, vl, simple, vdesc = VOWELS[k]
    ch = syl(c, v)
    lat = c.lower() + vl
    tr = c.lower() + simple
    cells = "".join(f'<span style="padding:0 3px;{"border:2.5px solid #111;border-radius:7px;background:#eee" if j == k else ""}">'
                    f'{x}</span>' for j, x in enumerate(row_chars(c)))
    phon = (f'<div class="nt" style="font-size:17pt;line-height:1.6;white-space:nowrap">{cells}</div>'
            f'<div class="small">{"the vowel" if not c else "row <b>" + c.lower() + "</b> ·"} column <b>{vl}</b> · '
            f'Vai spelling in Latin letters: <b>{lat}</b></div>')
    sound = f"{rowdesc}, then {vdesc}" if c else vdesc
    if ch in WORDS:
        w, wtr, m, pic, args, note = WORDS[ch]
    else:
        w, wtr, m, pic, args, note = ch, tr, f"say it: “{tr}”", "vai_slate", dict(label=ch), NOWORD
    return letter(ch, ch, tr, sound, w, wtr, m, pic, phon, "Its row in the syllable chart", args, note)


def row_table(c):
    cells = "".join(f'<td style="text-align:center;padding:2px 10px"><div class="nt" style="font-size:30pt;line-height:1.4">{syl(c, v[0])}</div>'
                    f'<div class="tr small">{c.lower()}{v[2]}</div></td>' for v in VOWELS)
    return f'<table style="margin:0.1in auto;border:2px solid #111;border-radius:12px;border-collapse:separate"><tr>{cells}</tr></table>'


FIRST_INTRO = f"""<p>Vai is written in its <b>own script</b>, from <b>left to right</b>. Each sign is a whole <b>syllable</b>: one sign says
<i>ba</i>, another says <i>ki</i>.</p>
<div class="box" style="margin:0.1in 0"><h3>Seven vowels</h3>Vai has seven vowels. Here they are on their own, in the order of the
Vai chart:{row_table("")}<div class="small" style="text-align:center">ɛ (eh) · i (ee) · a (ah) · ɔ (aw) · u (oo) · o (oh) · e (ay)</div></div>
<div class="box" style="margin:0.1in 0"><h3>A big chart of syllables</h3>The full Vai chart has about <b>200 signs</b>: a row for each
consonant (b, t, k, l, m, s, n, f, g, j …) and a column for each vowel, plus signs for nasal sounds like <i>an</i>. This book teaches the
<b>7 vowels and 7 common rows</b> — 56 syllables — one row at a time.</div>
<div class="box"><h3>Tunes in the voice</h3>Vai is a <b>tone language</b>: a high or low voice can change a word’s meaning. The script does
not mark tones, so readers use the sense of the sentence.</div>"""


def intro(c):
    return (f"<p>Every syllable in this row starts with <b>{c.lower()}</b>. Each sign has its own shape, so look closely and say "
            f"the row like a little song:</p>{row_table(c)}"
            f'<div class="box" style="margin-top:0.12in"><h3>Try it</h3>Point to each sign and say it out loud, left to right. Then cover '
            f"the sounds with your hand and see how many you remember!</div>")


SECTIONS = []
for c, desc in ROWS:
    items = [item(c, k, desc) for k in range(len(VOWELS))]
    if c:
        SECTIONS.append(section(items, label="SYLLABLE", chip=f"ROW {c}", title=f"The {c} Row", native=syl(c, "A"),
                                native_tr=f"{c.lower()}ɛ, {c.lower()}i, {c.lower()}a, {c.lower()}ɔ, {c.lower()}u, {c.lower()}o, {c.lower()}e",
                                intro_html=intro(c), chart_title=f"{c.lower()} row", chart_cols=7,
                                warmup_title=f"the {c.lower()} row", warmup_cols=4))
    else:
        SECTIONS.append(section(items, label="VOWEL", chip="THE VOWELS", title="The Vowels", native=syl("", "A"),
                                native_tr="ɛ, i, a, ɔ, u, o, e", intro_html=FIRST_INTRO, chart_title="vowels", chart_cols=7,
                                warmup_title="the vowels", warmup_cols=4))

LINE = '<span style="display:inline-block;width:1.5in;border-bottom:2px solid #111">&nbsp;</span>'
BLANK = '<span style="display:inline-block;width:2.4in;border-bottom:2px solid #111">&nbsp;</span>'

LANG = build(dict(
    code="vai", folder="book-61-vai", series_no=61, isbn="", draft=True,
    name="Vai", native="ꕙꔤ", native_tr="VAH-ee", name_word="its sound", write_word="ꕙꔤ", letters_word="Syllables",
    title="My First Vai Syllables",
    cover_title_html="My First Vai<br>Syllables", title_size=50,
    title_native="ꕙꔤ", title_letters="ꕉꕒꕚꕪꕞꕮ", belongs_native="", belongs_pic="star",
    alphabet_native="ꕙꔤ", numbers_native="꘡ ꘢ ꘣", numbers_tr="Vai digits", phrases_native="ꕙꔤ",
    fonts=fontset("Noto Sans Vai", "noto-sans-vai-vai", "Noto Sans Vai", "noto-sans-vai-vai"),
    disp_family="Noto Sans Vai", text_family="Noto Sans Vai",
    glyph_font=["noto-sans-vai-vai-400-normal.woff2", "baloo-2-latin-800-normal.woff2"], font_credit="Noto Sans Vai, Baloo 2",
    extra_css=(".lp-name{font-size:28pt} .lp-word .w{font-size:44pt} "
               # digits page: no Vai number words yet, so replace the "count out loud" line with a write-in task
               'p:has(+ .grid[style*="1fr 1fr"]){font-size:0} '
               'p:has(+ .grid[style*="1fr 1fr"])::before{font-size:13pt;content:"Color the Vai digits! Ask a Vai speaker '
               'how to say each number, and write the word on the line."}'),
    phon_feature="the whole row of the Vai chart for every syllable (ꕒ ba sits between ꔬ bi and ꕸ bɔ)",
    sections=SECTIONS,
    sound_notes=[
        "Each syllable has an <b>easy English sound</b>: <i>eh, ee, ah, aw, oo, oh, ay</i> for the seven vowels.",
        "The box on each page also gives the <b>standard Latin spelling</b> of Vai, where <b>ɛ</b> says <i>eh</i> and <b>ɔ</b> says <i>aw</i>.",
        "Vai is a <b>tone language</b>: a high or low voice changes meaning. The script does not show tones, so neither does this book.",
        "Vai also has sounds that English lacks (<i>kp, gb, ɓ</i>) and nasal syllables; they are in the full chart but not in this first book."],
    phon_explain="The third box shows the syllable’s <b>row</b> in the Vai chart (the same consonant with all seven vowels), "
                 "with the syllable itself in a box.",
    standard="the Vai of Liberia; the sound guides are approximate and do not show tones",
    hello=[
        ("Who speaks it?", "More than <b>100,000 Vai people</b> speak Vai.<sup>³</sup>"),
        ("Where?", "In the west of <b>Liberia</b>, around Robertsport and Grand Cape Mount, and in the south-east of <b>Sierra Leone</b>, near "
                   "the Atlantic coast. Most Vai families are <b>Muslim</b>."),
        ("How is it written?", "In its own <b>syllabary</b>, from <b>left to right</b>. Each sign stands for a whole syllable, like "
                               "<span class='nt'>ꕒ</span> <i>ba</i>."),
        ("How many signs?", "About <b>200</b>. This book teaches the <b>56</b> most useful first: 7 vowels and 7 rows."),
        ("A script from West Africa", "The Vai script was made around <b>1833</b> by <b>Momolu Duwalu Bukele</b>. It is one of the oldest "
                                      "scripts invented in West Africa, and Vai people taught it to each other at home."),
        ("Did you know?", "The name <span class='nt'>ꕙꔤ</span> <i>Vai</i> is written with just two signs: <span class='nt'>ꕙ</span> <i>va</i> "
                          "and <span class='nt'>ꔤ</span> <i>i</i>."),
    ],
    hello_pics=[("vai_slate", dict(label="ꕙ")), ("waves", {}), ("vai_slate", dict(label="ꔤ"))],
    chart_note="Read each row from left to right: ɛ, i, a, ɔ, u, o, e — the same order as in this book.",
    map=region_map(frame=[[-14.6, 3.8], [-7.2, 11.2]],
                   points=dict(robertsport=[-11.37, 6.75], monrovia=[-10.80, 6.30], freetown=[-13.23, 8.48], pujehun=[-11.72, 7.35]),
                   area=(-11.4, 7.0, 150, 110),
                   cities=[("robertsport", "Robertsport", -14, 8, "end", False), ("monrovia", "Monrovia", 14, 22, "start", False),
                           ("freetown", "Freetown", 14, -8, "start", False), ("pujehun", "Pujehun", 14, -8, "start", False)],
                   label="WEST AFRICA", label_at=[-9.0, 10.3], marker=[-11.0, 7.5],
                   caption="The circle shows Liberia and Sierra Leone on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Vai is spoken inside the dashed "
                          "area, around Robertsport in Liberia and Pujehun in Sierra Leone, close to the Atlantic coast.",
                   seas=[("Atlantic Ocean", -12.6, 5.0)], world_r=12),
    digits=[(chr(0xA620 + i), LINE, "", en) for i, en in enumerate(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])],
    phrases=[("ꕉꕢꕞꖷ ꕉꔒꖴꖷ", "as-sa-LAA-mu a-LAY-ku-mu", "Peace be upon you (the Muslim greeting)"),
             ("ꕎ ꕉꔒꖴꖷ ꕉꕢꕞꕮ", "wa a-LAY-ku-mu as-sa-LAA-ma", "And upon you be peace (the reply)"),
             ("ꕧꕤꕪꕞꖗ ꕪꔤꕟꘋ", "ja-ZAA-kal-laa-hu KHAY-ran", "May Allah reward you with good"),
             (BLANK, "ask a Vai speaker, then write it here", "My name is …"),
             (BLANK, "ask a Vai speaker, then write it here", "Thank you"),
             (BLANK, "ask a Vai speaker, then write it here", "Mother · Father"),
             (BLANK, "ask a Vai speaker, then write it here", "Brother · Sister"),
             (BLANK, "ask a Vai speaker, then write it here", "Yes · No"),
             (BLANK, "ask a Vai speaker, then write it here", "I am learning Vai!")],
    cheer=("ꕮꕣꕞ!", "maa-shaa-LAAH!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); the history of the script from the <b>Unicode Standard</b> "
                 "(Vai block) and published histories of the Vai syllabary.",
    book_pic=dict(left="ꕉ ꔤ ꖕ", right="ꕒ ꔬ ꖝ"),
    review_note=("This is the thinnest draft in the series. (1) We found no reliable Vai example word for 55 of the 56 syllables, so "
                 "those pages show the syllable on a slate with a note; a Vai speaker should supply one picturable word per syllable "
                 "(object, plant or nature) and replace the slate. (2) The everyday phrases (my name is, thank you, mother/father, "
                 "brother/sister, yes/no, I am learning Vai) are left as write-in lines, and the number words are left out; please "
                 "supply them. (3) Check the Vai spellings of the Arabic phrases (Assalamu alaikum, Wa alaikum assalam, Jazakallahu "
                 "khairan, Mashallah), the choice of core rows (b t k l m s n) and the column order ɛ i a ɔ u o e. (4) Noto Sans Vai has "
                 "only one (regular) weight, so the big coloring signs are thinner than in other books."),
    tiles="ꕉꕒꕮꕪꕢꕞ", cover_pics=["vai_slate", "waves", "book", "star"],
    speakers_blurb="Vai is spoken by more than 100,000 people in Liberia and Sierra Leone, and has its own West African script.",
    sample_words=[("ꕙꔤ", "VAH-ee", "Vai"), ("ꕒ", "bah", "the syllable ba"), ("ꕮ", "mah", "the syllable ma")],
    keywords=["vai script book for kids", "learn vai syllabary for children", "liberia language coloring book",
              "west african script tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "african heritage language gift"],
))
