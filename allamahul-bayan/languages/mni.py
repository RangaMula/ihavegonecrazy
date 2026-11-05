# -*- coding: utf-8 -*-
"""Book 21 - Manipuri / Meitei (Meitei Mayek script). Allamahul Bayan Series. REVIEW DRAFT.
Four groups as taught in Manipur: Iyek Ipee (18 original letters), Lom Iyek (9 added letters),
Cheitap Iyek (8 vowel signs) and Lonsum Iyek (8 final letters) = 43. Built with engine/generic.py."""
from generic import build, letter, section, fontset
from maps import region_map

NT = "<span class='nt'>{}</span>"
MID = "Find <b>{}</b> in the middle of " + NT + "!"


def phon_box(big, small, rule=None):
    return (f'<div class="nt" style="font-size:21pt;line-height:1.35">{big}</div>'
            f'<div class="small">{small}</div>' + (f'<div class="small" style="margin-top:3px">{rule}</div>' if rule else ""))


def K(ch, name, rom, sound, word, tr, meaning, pic, args=None, note=None, rule=None, partner=None):
    """A consonant letter (Iyek Ipee or Lom Iyek)."""
    if ch in "ꯎꯏ":
        small = f"Its name is «{rom}». A vowel letter: it starts a word on its own, without ꯑ."
    else:
        small = f"Its name is «{rom}». With vowel signs: {NT.format(f'{ch}ꯥ {ch}ꯤ {ch}ꯨ {ch}ꯦ')}"
    if partner:
        p, how = partner
        small += f"<br>Partner letter: {NT.format(p)} — {how}"
    return letter(ch, name, rom, sound, word, tr, meaning, pic, phon_box(f"{ch} — {name}", small, rule),
                  "Meitei Mayek name · with vowel signs", args, note)


def V(sign, name, rom, sound, word, tr, meaning, pic, args=None, note=None):
    """A vowel sign (Cheitap Iyek), drawn big on the carrier letter ꯑ."""
    big = f"◌{sign} — {name}"
    small = (f"Its name is «{rom}». On its own, a vowel sits on {NT.format('ꯑ')}: {NT.format('ꯑ' + sign)}. "
             f"After a letter: {NT.format(f'ꯀ + ◌{sign} = ꯀ{sign}')}")
    return letter("ꯑ" + sign, name, rom, sound, word, tr, meaning, pic, phon_box(big, small),
                  "Meitei Mayek name · how the sign joins", args, note)


def F(ch, base, name, rom, sound, word, tr, meaning, pic, args=None, note=None, how=None):
    """A final letter (Lonsum Iyek)."""
    small = f"Its name is «{rom}». {NT.format(base)} becomes {NT.format(ch)} when it closes a syllable."
    return letter(ch, name, rom, sound, word, tr, meaning, pic,
                  phon_box(f"{base} → {ch}", small, how), "Meitei Mayek name · the final shape", args, note)


IPEE = [
    K("ꯀ", "ꯀꯣꯛ", "kok", "‘k’ as in “sky” (no puff of air)", "ꯀꯩꯍꯣꯝ", "KEI-hom", "pineapple", "pineapple"),
    K("ꯁ", "ꯁꯝ", "sam", "‘s’ as in “sun”", "ꯁꯅꯥ", "sa-NAA", "gold", "ring"),
    K("ꯂ", "ꯂꯥꯏ", "lai", "‘l’ as in “lamp”", "ꯂꯐꯣꯏ", "la-PHOI", "banana", "banana"),
    K("ꯃ", "ꯃꯤꯠ", "mit", "‘m’ as in “moon”", "ꯃꯩ", "mei", "fire", "mni_fire"),
    K("ꯄ", "ꯄꯥ", "pa", "‘p’ as in “spin” (no puff of air)", "ꯄꯥꯠ", "paat", "lake", "waves",
      rule="Manipur’s great lake is " + NT.format("ꯂꯣꯛꯇꯥꯛ ꯄꯥꯠ") + " «Loktak paat»."),
    K("ꯅ", "ꯅꯥ", "na", "‘n’ as in “net”", "ꯅꯣꯡ", "nong", "rain", "raincloud"),
    K("ꯆ", "ꯆꯤꯜ", "chil", "‘ch’ as in “chair”", "ꯆꯤꯡ", "ching", "hill", "mountain"),
    K("ꯇ", "ꯇꯤꯜ", "til", "‘t’ as in “stop” (no puff of air)", "ꯇꯤꯜꯍꯧ", "TIL-hou", "onion", "onion"),
    K("ꯈ", "ꯈꯧ", "khou", "‘k’ with a puff of air, as in “kite”", "ꯈꯣꯏꯖꯨ", "KHOI-ju", "honey", "honey"),
    K("ꯉ", "ꯉꯧ", "ngou", "‘ng’ as in “sing” — even at the start of a word!", "ꯉꯁꯤ", "nga-SI", "today", "sunrise"),
    K("ꯊ", "ꯊꯧ", "thou", "‘t’ with a puff of air, as in “top” (not the English ‘th’)", "ꯊꯝꯕꯜ", "THAM-bal", "lotus", "lily"),
    K("ꯋ", "ꯋꯥꯏ", "wai", "‘w’ as in “water”", "ꯋꯥ", "waa", "bamboo", "mni_bamboo"),
    K("ꯌ", "ꯌꯥꯡ", "yang", "‘y’ as in “yes”", "ꯌꯨꯝ", "yoom", "house", "house"),
    K("ꯍ", "ꯍꯨꯛ", "huk", "‘h’ as in “hat”", "ꯍꯤ", "hee", "boat", "boat"),
    K("ꯎ", "ꯎꯟ", "un", "‘oo’ as in “moon”", "ꯎꯄꯥꯜ", "oo-PAAL", "tree", "tree"),
    K("ꯏ", "ꯏ", "ee", "‘ee’ as in “see”", "ꯏꯁꯤꯡ", "ee-SING", "water", "water"),
    K("ꯐ", "ꯐꯝ", "pham", "‘p’ with a puff of air, as in “pin” (not ‘f’)", "ꯐꯧ", "phou", "paddy (rice plant)", "paddy"),
    K("ꯑ", "ꯑꯇꯤꯌꯥ", "atiya", "‘a’ as in “about”; it also carries the vowel signs", "ꯑꯂꯨ", "a-LOO", "potato", "potato"),
]

LOM = [
    K("ꯒ", "ꯒꯣꯛ", "gok", "‘g’ as in “go”", "ꯒꯥꯔꯤ", "GAA-ree", "cart, car", "cart",
      partner=("ꯀ", "ꯒ is the soft ‘g’ of ꯀ ‘k’")),
    K("ꯓ", "ꯓꯝ", "jham", "‘j’ with a puff of air", "ꯓꯔ꯭ꯅꯥ", "JHAR-naa", "waterfall", "mni_waterfall",
      partner=("ꯖ", "ꯓ is ꯖ ‘j’ with a puff of air"), note="<b>ꯓ</b> is a rare letter, used mostly in borrowed words."),
    K("ꯔ", "ꯔꯥꯏ", "rai", "a tapped ‘r’", "ꯇꯨꯔꯦꯜ", "too-REL", "river", "mni_river",
      partner=("ꯂ", "old Meitei words often say ‘l’ where other languages say ‘r’"), note=MID.format("ꯔ", "ꯇꯨꯔꯦꯜ")),
    K("ꯕ", "ꯕꯥ", "ba", "‘b’ as in “ball”", "ꯕꯣꯜ", "bol", "ball", "ball",
      partner=("ꯄ", "ꯕ is the soft ‘b’ of ꯄ ‘p’")),
    K("ꯖ", "ꯖꯤꯜ", "jil", "‘j’ as in “jam”", "ꯁꯤꯡꯖꯨ", "SING-ju", "singju (a crunchy Manipuri salad)", "plate",
      partner=("ꯆ", "ꯖ is the soft ‘j’ of ꯆ ‘ch’"), note=MID.format("ꯖ", "ꯁꯤꯡꯖꯨ")),
    K("ꯗ", "ꯗꯤꯜ", "dil", "‘d’ as in “day”", "ꯗꯥꯜ", "daal", "dal (lentil soup)", "pot",
      partner=("ꯇ", "ꯗ is the soft ‘d’ of ꯇ ‘t’")),
    K("ꯘ", "ꯘꯧ", "ghou", "‘g’ with a puff of air", "ꯘꯤ", "ghee", "ghee (clarified butter)", "jar",
      partner=("ꯒ", "ꯘ is ꯒ ‘g’ with a puff of air"), note="<b>ꯘ</b> is a rare letter, used mostly in borrowed words."),
    K("ꯙ", "ꯙꯧ", "dhou", "‘d’ with a puff of air", "ꯙꯅꯨ", "DHA-nu", "bow (and arrow)", "bowarrow",
      partner=("ꯗ", "ꯙ is ꯗ ‘d’ with a puff of air"), note="<b>ꯙ</b> is a rare letter, used mostly in borrowed words."),
    K("ꯚ", "ꯚꯝ", "bham", "‘b’ with a puff of air", "ꯚꯦꯟꯗꯤ", "BHEN-dee", "okra (lady’s finger)", "mni_okra",
      partner=("ꯕ", "ꯚ is ꯕ ‘b’ with a puff of air"), note="<b>ꯚ</b> is a rare letter, used mostly in borrowed words."),
]

CHEITAP = [
    V("ꯣ", "ꯑꯣꯠꯅꯥꯞ", "otnap", "‘o’ as in “go” (short and pure)", "ꯃꯣꯔꯣꯛ", "mo-ROK", "chilli", "mni_chilli"),
    V("ꯤ", "ꯏꯅꯥꯞ", "inap", "‘i’ as in “sit”", "ꯊꯋꯥꯟꯃꯤꯆꯥꯛ", "tha-WAAN-mi-chaak", "star", "star"),
    V("ꯥ", "ꯑꯥꯇꯥꯞ", "aatap", "‘aa’ as in “father”", "ꯊꯥ", "thaa", "moon", "moon"),
    V("ꯦ", "ꯌꯦꯠꯅꯥꯞ", "yetnap", "‘e’ as in “bed”", "ꯌꯦꯔꯨꯝ", "ye-ROOM", "egg", "egg"),
    V("ꯧ", "ꯁꯧꯅꯥꯞ", "sounap", "‘ou’ as in “go”, sliding to ‘oo’", "ꯍꯩꯅꯧ", "HEI-nou", "mango", "mango"),
    V("ꯨ", "ꯎꯅꯥꯞ", "unap", "‘u’ as in “put”", "ꯅꯨꯡ", "noong", "stone", "mni_stones"),
    V("ꯩ", "ꯆꯩꯅꯥꯞ", "cheinap", "‘ei’ as in “day”", "ꯂꯩ", "lei", "flower", "flower"),
    V("ꯪ", "ꯅꯨꯡ", "nung", "a humming ‘ng’ after a vowel, as in “song”", "ꯀꯪꯖꯩ", "KANG-jei", "hockey stick", "mni_kangjei",
      note="<b>ꯪ</b> is a dot that adds ‘ng’. Many words write the same sound with " + NT.format("ꯡ") + " instead."),
]

LONSUM = [
    F("ꯛ", "ꯀ", "ꯀꯣꯛ ꯂꯣꯟꯁꯨꯝ", "kok lonsum", "a short ‘k’ that stops the word", "ꯆꯥꯛ", "chaak", "rice (cooked)", "rice",
      how=NT.format("ꯆ + ◌ꯥ + ꯛ = ꯆꯥꯛ")),
    F("ꯜ", "ꯂ", "ꯂꯥꯏ ꯂꯣꯟꯁꯨꯝ", "lai lonsum", "‘l’ at the end, as in “ball”", "ꯂꯩꯆꯤꯜ", "LEI-chil", "cloud", "clouds",
      how=NT.format("ꯆ + ◌ꯤ + ꯜ = ꯆꯤꯜ")),
    F("ꯝ", "ꯃ", "ꯃꯤꯠ ꯂꯣꯟꯁꯨꯝ", "mit lonsum", "‘m’ at the end, as in “drum”", "ꯊꯨꯝ", "thoom", "salt", "salt", dict(label="ꯊꯨꯝ"),
      how=NT.format("ꯊ + ◌ꯨ + ꯝ = ꯊꯨꯝ")),
    F("ꯞ", "ꯄ", "ꯄꯥ ꯂꯣꯟꯁꯨꯝ", "pa lonsum", "a short ‘p’ that stops the word", "ꯈꯣꯡꯎꯞ", "KHONG-oop", "shoe", "mni_shoe",
      how=NT.format("ꯎ + ꯞ = ꯎꯞ")),
    F("ꯟ", "ꯅ", "ꯅꯥ ꯂꯣꯟꯁꯨꯝ", "na lonsum", "‘n’ at the end, as in “sun”", "ꯈꯥꯃꯦꯟ ꯑꯁꯤꯟꯕ", "KHAA-men a-SIN-ba", "tomato", "tomato",
      how=NT.format("ꯃ + ◌ꯦ + ꯟ = ꯃꯦꯟ")),
    F("ꯠ", "ꯇ", "ꯇꯤꯜ ꯂꯣꯟꯁꯨꯝ", "til lonsum", "a short ‘t’ that stops the word", "ꯅꯨꯃꯤꯠ", "NOO-mit", "sun", "sun",
      how=NT.format("ꯃ + ◌ꯤ + ꯠ = ꯃꯤꯠ")),
    F("ꯡ", "ꯉ", "ꯉꯧ ꯂꯣꯟꯁꯨꯝ", "ngou lonsum", "‘ng’ at the end, as in “sing”", "ꯆꯨꯝꯊꯥꯡ", "CHOOM-thaang", "rainbow", "rainbow",
      how=NT.format("ꯊ + ◌ꯥ + ꯡ = ꯊꯥꯡ")),
    F("ꯢ", "ꯏ", "ꯏ ꯂꯣꯟꯁꯨꯝ", "ee lonsum", "a short ‘i’ that ends a sound, as in “eye”", "ꯂꯥꯢꯔꯤꯛ", "LAI-rik", "book", "book",
      dict(left="ꯀ ꯁ ꯂ", right="ꯃ ꯄ ꯅ"),
      note="Many books write this word with " + NT.format("ꯏ") + " instead: " + NT.format("ꯂꯥꯏꯔꯤꯛ") + "."),
]

INTRO_IPEE = """<p>Meiteilon is written in <b>Meitei Mayek</b> <span class="nt">ꯃꯩꯇꯩ ꯃꯌꯦꯛ</span>, the old script of Manipur, from left to right.
It is taught in four groups. The first group is the <b>18 original letters</b>, called <b>Iyek Ipee</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letters named after the body</h3>Each of the 18 letters has a name taken from a part of the human body:
<span class="nt">ꯀ</span> <i>kok</i> means “head”, <span class="nt">ꯁ</span> <i>sam</i> “hair”, <span class="nt">ꯂ</span> <i>lai</i> “forehead”
and <span class="nt">ꯃ</span> <i>mit</i> “eye”.</div>
<div class="box" style="margin:0.1in 0"><h3>A hidden vowel</h3>Every letter already says a short <b>a</b>: <span class="nt">ꯀ</span> is «ka».
To change the vowel, add a <b>vowel sign</b>: <span class="nt">ꯀ + ◌ꯥ = ꯀꯥ</span> «kaa».</div>
<div class="box"><h3>The four groups</h3><span class="nt">ꯏꯌꯦꯛ ꯏꯄꯤ</span> Iyek Ipee, 18 letters ·
<span class="nt">ꯂꯣꯝ ꯏꯌꯦꯛ</span> Lom Iyek, 9 added letters · <span class="nt">ꯆꯩꯇꯥꯞ ꯏꯌꯦꯛ</span> Cheitap Iyek, 8 vowel signs ·
<span class="nt">ꯂꯣꯟꯁꯨꯝ ꯏꯌꯦꯛ</span> Lonsum Iyek, 8 final letters.</div>"""

INTRO_LOM = """<p><b>Lom Iyek</b> means “added letters”. These <b>9 letters</b> were added to write softer sounds
like <b>g, j, d, b</b>, the sound <b>r</b>, and sounds with a puff of air like <b>gh, dh, bh</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letter partners</h3>Most added letters have a partner among the first 18:
<div class="nt" style="font-size:17pt;line-height:1.7;margin-top:4px">ꯀ → ꯒ · ꯄ → ꯕ · ꯆ → ꯖ · ꯇ → ꯗ<br>ꯖ → ꯓ · ꯒ → ꯘ · ꯗ → ꯙ · ꯕ → ꯚ</div></div>
<div class="box"><h3>Rare letters</h3>Some of these letters are used mostly in words that Meiteilon has borrowed from other languages,
so they do not appear very often.</div>"""

INTRO_CHEITAP = """<p><b>Cheitap Iyek</b> are the <b>8 vowel signs</b>. A vowel sign never stands alone: it holds on to a letter.
To write a vowel at the start of a word, put the sign on <span class="nt">ꯑ</span>.</p>
<table style="width:100%;border-collapse:collapse;margin-top:0.08in;text-align:center" class="vt">
<tr style="font:600 10.5pt Fredoka"><th>Sign</th><th>Name</th><th>On ꯑ</th><th>With ꯀ</th></tr>""" + "".join(
    f'<tr><td class="nt" style="font-size:18pt">◌{s}</td><td class="tr">{n}</td><td class="nt" style="font-size:18pt">ꯑ{s}</td>'
    f'<td class="nt" style="font-size:18pt">ꯀ{s}</td></tr>'
    for s, n in [("ꯣ", "otnap"), ("ꯤ", "inap"), ("ꯥ", "aatap"), ("ꯦ", "yetnap"), ("ꯧ", "sounap"), ("ꯨ", "unap"),
                 ("ꯩ", "cheinap"), ("ꯪ", "nung")]) + """</table>
<style>.vt td,.vt th{border-bottom:1.5px solid #bbb;padding:1px 4px}</style>"""

INTRO_LONSUM = """<p><b>Lonsum Iyek</b> are the <b>8 final letters</b>. When a sound closes a syllable, its letter changes shape
and loses its hidden vowel.</p>
<div class="box" style="margin:0.1in 0"><h3>Before and after</h3>
<div class="nt" style="font-size:19pt;line-height:1.7;margin-top:4px">ꯀ → ꯛ · ꯂ → ꯜ · ꯃ → ꯝ · ꯄ → ꯞ<br>ꯅ → ꯟ · ꯇ → ꯠ · ꯉ → ꯡ · ꯏ → ꯢ</div></div>
<div class="box"><h3>Try it</h3><span class="nt">ꯌ + ◌ꯨ + ꯝ = ꯌꯨꯝ</span> «yoom», “house”. Without the final letter it would be
<span class="nt">ꯌꯨ</span> «yu».</div>"""

LANG = build(dict(
    code="mni", folder="book-21-manipuri", series_no=21, isbn="", draft=True,
    name="Manipuri", native="ꯃꯩꯇꯩꯂꯣꯟ", native_tr="MEI-tei-lon", name_word="ꯃꯤꯡ", write_word="ꯏꯕꯤꯌꯨ",
    title_native="ꯑꯩꯒꯤ ꯑꯍꯥꯅꯕ ꯃꯩꯇꯩ ꯃꯌꯦꯛ", title_letters="ꯀꯁꯂꯃꯄ", belongs_native="ꯂꯥꯏꯔꯤꯛ ꯑꯁꯤ … ꯒꯤꯅꯤ",
    belongs_pic="lily", alphabet_native="ꯃꯩꯇꯩ ꯃꯌꯦꯛ", numbers_native="ꯃꯁꯤꯡ", numbers_tr="ma-SING",
    phrases_native="ꯑꯍꯥꯅꯕ ꯋꯥꯍꯩ",
    fonts=fontset("Noto Sans Meetei Mayek", "noto-sans-meetei-mayek-meetei-mayek", "Noto Sans Meetei Mayek",
                  "noto-sans-meetei-mayek-meetei-mayek"),
    disp_family="Noto Sans Meetei Mayek", text_family="Noto Sans Meetei Mayek",
    glyph_font="noto-sans-meetei-mayek-meetei-mayek-800-normal.woff2",
    font_credit="Noto Sans Meetei Mayek",
    extra_css=(".nt{font-family:'Noto Sans Meetei Mayek','Nunito',sans-serif} "
               ".ntd{font-family:'Noto Sans Meetei Mayek','Nunito',sans-serif;font-weight:800}"),
    title="My First Manipuri Alphabet",
    subtitle="A Coloring Book to Learn, Trace & Say the 43 Letters and Signs of Meitei Mayek with English Phonetics",
    letters_word="Letters and Signs",
    phon_feature="each letter’s Meitei Mayek name (ꯀ «kok», ꯁ «sam», ꯂ «lai»…) and how it joins with vowel signs",
    sections=[
        section(IPEE, label="LETTER", chip="IYEK IPEE · THE 18 LETTERS", title="The 18 Letters", native="ꯏꯌꯦꯛ ꯏꯄꯤ",
                native_tr="ee-yek ee-pee — “the original letters”", chart_title="original letters", chart_cols=9,
                warmup_title="the 18 letters", warmup_cols=6, intro_html=INTRO_IPEE),
        section(LOM, label="ADDED LETTER", chip="LOM IYEK · ADDED LETTERS", title="Added Letters", native="ꯂꯣꯝ ꯏꯌꯦꯛ",
                native_tr="lom ee-yek — “the added letters”", chart_title="added letters", chart_cols=9,
                warmup_title="the added letters", warmup_cols=5, intro_html=INTRO_LOM),
        section(CHEITAP, label="VOWEL SIGN", chip="CHEITAP IYEK · VOWEL SIGNS", title="Vowel Signs", native="ꯆꯩꯇꯥꯞ ꯏꯌꯦꯛ",
                native_tr="chei-taap ee-yek — “the vowel signs”", chart_title="vowel signs (shown on ꯑ)", chart_cols=8,
                warmup_title="the vowel signs", warmup_cols=4, intro_html=INTRO_CHEITAP),
        section(LONSUM, label="FINAL LETTER", chip="LONSUM IYEK · FINAL LETTERS", title="Final Letters", native="ꯂꯣꯟꯁꯨꯝ ꯏꯌꯦꯛ",
                native_tr="lon-soom ee-yek — “the final letters”", chart_title="final letters", chart_cols=8,
                warmup_title="the final letters", warmup_cols=4, intro_html=INTRO_LONSUM),
    ],
    chart_note="Read each group row by row — the same order as in this book.",
    sound_notes=[
        "<b>a</b> is short, as in “about”; <b>aa</b> is long, as in “father”. <b>ei</b> is as in “day”; <b>ou</b> as in “go”.",
        "<b>CAPITALS</b> show the part of the word to say a little louder: <i>THAM-bal</i>.",
        "<b>kh, th, ph</b> mean k, t, p with a puff of air. <b>ph</b> is never ‘f’ and <b>th</b> is never the English “th”.",
        "<b>ng</b> is the sound in “sing” — in Meiteilon it can start a word: <i>nga-SI</i>.",
        "Meiteilon is a <b>tonal</b> language: the voice can go up or down. The guides here leave tones out; listen to a speaker."],
    phon_explain="The box with the letter’s <i>Meitei Mayek name</i> shows the name Manipuri children use "
                 "(<span class='nt'>ꯀ</span> is «kok», <span class='nt'>ꯁ</span> is «sam»…) and how the letter joins with vowel signs.",
    standard="the Meiteilon of the Imphal valley",
    hello=[
        ("Who speaks it?", "About <b>1.8 million people</b> speak Meiteilon (also called Manipuri).<sup>³</sup> "
                           "It is one of the 22 languages listed in India’s Constitution."),
        ("Where?", "Mostly in <b>Manipur</b> in north-east India, and also in <b>Assam</b> and <b>Tripura</b>, and by families in "
                   "<b>Bangladesh</b> and <b>Myanmar</b>."),
        ("How is it written?", "In its own script, <b>Meitei Mayek</b> <span class='nt'>ꯃꯩꯇꯩ ꯃꯌꯦꯛ</span>, from <b>left to right</b>. "
                               "It is also written in Bengali letters."),
        ("How many letters?", "<b>27 letters</b> (18 original + 9 added), <b>8 vowel signs</b> and <b>8 final letters</b>: "
                              "<b>43</b> in this book, plus its own numbers <span class='nt'>꯰ ꯱ ꯲ ꯳</span>…"),
        ("Hello!", "A warm Manipuri greeting is <span class='nt'>ꯈꯨꯔꯨꯝꯖꯔꯤ</span> <i>khoo-room-ja-ree</i>."),
        ("Did you know?", "Manipur is home to <b>Meitei Muslims</b>, called <b>Meitei Pangal</b>, whose families have spoken "
                          "Meiteilon for about 400 years."),
    ],
    hello_pics=[("lily", {}), ("pineapple", {}), ("mni_bamboo", {})],
    map=region_map(frame=[[86.5, 18.0], [100.5, 32.0]],
                   points=dict(imphal=[93.94, 24.81]),
                   area=(93.9, 24.75, 70, 85), cities=[("imphal", "Imphal", 16, 8, "start", True)],
                   label="MANIPUR", label_at=[93.9, 26.9], marker=[93.9, 24.8],
                   caption="The circle shows Manipur on the world map.",
                   legend="<b>Color it:</b> Manipur (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · "
                          "the sea <b>blue</b>. <b>Find it:</b> Imphal ★ is the capital of Manipur. Meiteilon is also spoken "
                          "in parts of Assam and Tripura.",
                   seas=[("Bay of Bengal", 89.6, 19.6)]),
    digits=[("꯰", "ꯐꯨꯟ", "phoon", "zero"), ("꯱", "ꯑꯃꯥ", "a-MAA", "one"), ("꯲", "ꯑꯅꯤ", "a-NEE", "two"), ("꯳", "ꯑꯍꯨꯝ", "a-HOOM", "three"),
            ("꯴", "ꯃꯔꯤ", "ma-REE", "four"), ("꯵", "ꯃꯉꯥ", "ma-NGAA", "five"), ("꯶", "ꯇꯔꯨꯛ", "ta-ROOK", "six"),
            ("꯷", "ꯇꯔꯦꯠ", "ta-RET", "seven"), ("꯸", "ꯅꯤꯄꯥꯟ", "ni-PAAN", "eight"), ("꯹", "ꯃꯥꯄꯟ", "MAA-pan", "nine")],
    phrases=[("ꯑꯁ꯭ꯁꯂꯥꯃꯨ ꯑꯂꯥꯏꯀꯨꯝ", "as-sa-LAA-moo a-LAI-koom", "Peace be upon you (the Muslim greeting)"),
             ("ꯋꯥ ꯑꯂꯥꯏꯀꯨꯝ ꯑꯁ꯭ꯁꯂꯥꯝ", "wa a-LAI-koom as-sa-LAAM", "And upon you be peace (the reply)"),
             ("ꯈꯨꯔꯨꯝꯖꯔꯤ", "khoo-room-ja-REE", "Hello! (a respectful greeting)"),
             ("ꯑꯩꯒꯤ ꯃꯤꯡ … ꯅꯤ", "EI-gee ming … nee", "My name is …"),
             ("ꯊꯥꯒꯠꯆꯔꯤ", "THAA-gat-cha-ree", "Thank you"),
             ("ꯖꯥꯖꯥꯀꯜꯂꯥꯍꯨ ꯈꯥꯏꯔꯟ", "jaa-zaa-kal-LAA-hoo KHAI-ran", "May Allah reward you with good"),
             ("ꯏꯃꯥ · ꯏꯄꯥ", "ee-MAA · ee-PAA", "Mother · Father"),
             ("ꯇꯥꯃꯣ · ꯏꯆꯦ", "TAA-mo · ee-CHE", "Big brother · Big sister"),
             ("ꯍꯣꯏ · ꯅꯠꯇꯦ", "hoi · NAT-te", "Yes · No"),
             ("ꯑꯩ ꯃꯩꯇꯩꯂꯣꯟ ꯇꯝꯂꯤ!", "ei MEI-tei-lon TAM-lee", "I am learning Manipuri!")],
    cheer=("ꯃꯥꯁꯥꯜꯂꯥ! ꯌꯥꯝꯅ ꯐꯖꯩ!", "MAA-shaal-laa! YAAM-na pha-JEI!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the Census of India.",
    book_pic=dict(left="ꯀ ꯁ ꯂ", right="ꯃ ꯄ ꯅ"),
    review_note=("Drafted without a native speaker. Check: the Lom Iyek example words (ꯒꯥꯔꯤ, ꯓꯔ꯭ꯅꯥ, ꯕꯣꯜ, ꯗꯥꯜ, ꯘꯤ, ꯙꯅꯨ, ꯚꯦꯟꯗꯤ "
                 "are borrowed words; replace with better ones if you know them); ꯀꯩꯍꯣꯝ pineapple, ꯉꯁꯤ today, ꯀꯪꯖꯩ (spelling with ꯪ), "
                 "ꯂꯥꯢꯔꯤꯛ (use of ꯢ), ꯈꯣꯡꯎꯞ shoe; the letter-name meanings (kok head, sam hair, lai forehead, mit eye); "
                 "the order of the four groups; spellings of the Arabic phrases (apun ꯭); the title, ‘belongs to’ line and cheer."),
    tiles="ꯀꯁꯂꯃꯄꯅ", cover_pics=["lily", "pineapple", "mni_bamboo", "star"], title_size=48,
    speakers_blurb="Manipuri (Meiteilon) is spoken by about 1.8 million people in Manipur and north-east India, and it has its own beautiful script, Meitei Mayek.",
    sample_words=[("ꯂꯩ", "lei", "flower"), ("ꯊꯝꯕꯜ", "THAM-bal", "lotus"), ("ꯍꯩꯅꯧ", "HEI-nou", "mango")],
    keywords=["manipuri alphabet book for kids", "meitei mayek coloring book", "learn meiteilon for children",
              "meitei mayek letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "manipuri english bilingual toddlers"],
))
