# -*- coding: utf-8 -*-
"""Book 17 - Dhivehi (Thaana script, right to left). Allamahul Bayan Series. REVIEW DRAFT.
The 24 basic Thaana letters in their traditional order (ހ ށ ނ ރ ބ ޅ ކ އ ވ މ ފ ދ ތ ލ ގ ޏ ސ ޑ ޒ ޓ ޔ ޕ ޖ ޗ).
The fili (vowel signs) are taught on the section intro page and on every letter page.
Transliteration follows the Maldivian Latin habit (dh, th = teeth; d, t = curled back; lh; ey, oa long e/o).
Picture plug-ins (dv_*) live in engine/pics/si_dv_pics.py."""
from generic import build, letter, section, fontset
from maps import region_map

FILI = [("ަ", "a"), ("ާ", "aa"), ("ި", "i"), ("ީ", "ee"), ("ު", "u"), ("ޫ", "oo"),
        ("ެ", "e"), ("ޭ", "ey"), ("ޮ", "o"), ("ޯ", "oa")]
SUKUN = "ް"
PH = "The letter with its fili (vowel signs)"


def nt(t):
    return f'<span class="nt">{t}</span>'


def fili_grid(c, tr):
    cells = "".join(f'<div style="text-align:center"><div class="nt" style="font-size:17pt;line-height:1.55">{c}{f}</div>'
                    f'<div class="small" style="font-size:8.5pt;line-height:1;direction:ltr">{tr}{v}</div></div>'
                    for f, v in FILI)
    return f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:1px 2px;direction:rtl">{cells}</div>'


def T(c, name, name_tr, tr_c, sound, word, tr, meaning, pic, args=None, note=None):
    return letter(c, name, name_tr, sound, word, tr, meaning, pic, fili_grid(c, tr_c), PH, args, note)


def inside(c, word):
    return f"Find {nt(c)} inside {nt(word)} — it hardly ever starts a word."


LETTERS = [
    T("ހ", "ހާ", "haa", "h", "‘h’ as in “hat”", "ހަނދު", "handhu", "the moon", "moon"),
    T("ށ", "ށަވިޔަނި", "shaviyani", "sh", "‘sh’ as in “shoe” — but at the end of a word (ށް) it says ‘h’",
      "ކާށި", "kaashi", "coconut", "coconut", note=inside("ށ", "ކާށި")),
    T("ނ", "ނޫނު", "noonu", "n", "‘n’ as in “net”", "ނަމާދު", "namaadhu", "prayer (salah)", "prayermat",
      note=f"With no fili, {nt('ނ')} glides into the next letter: {nt('ހަނދު')} <i>handhu</i>, {nt('އަނބު')} <i>anbu</i>."),
    T("ރ", "ރާ", "raa", "r", "a tapped ‘r’ — flick the tongue once", "ރޮށި", "roshi", "flatbread (roshi)", "roti"),
    T("ބ", "ބާ", "baa", "b", "‘b’ as in “ball”", "ބިސް", "bis", "egg", "egg"),
    T("ޅ", "ޅަވިޔަނި", "lhaviyani", "lh", "an ‘l’ with the tongue curled back — written ‘lh’", "ވަޅު", "valhu",
      "well (for water)", "well", note=inside("ޅ", "ވަޅު")),
    T("ކ", "ކާފު", "kaafu", "k", "‘k’ as in “kite”", "ކަރާ", "karaa", "watermelon", "watermelon"),
    T("އ", "އަލިފު", "alifu", "", "no sound of its own — it carries the vowel at the start of a word", "އަނބު", "anbu",
      "mango", "mango", note=f"{nt('އަ')} = <i>a</i>, {nt('އާ')} = <i>aa</i>. With sukun ({nt('އް')}) it doubles the next letter."),
    T("ވ", "ވާވު", "vaavu", "v", "between ‘v’ and ‘w’", "ވާރޭ", "vaarey", "rain", "raincloud"),
    T("މ", "މީމު", "meemu", "m", "‘m’ as in “moon”", "މިސްކިތް", "miskiy", "mosque", "mosque"),
    T("ފ", "ފާފު", "faafu", "f", "‘f’ as in “fan”", "ފެން", "fen", "water", "water"),
    T("ދ", "ދާލު", "dhaalu", "dh", "a soft ‘d’ — tongue touches the back of the teeth (written ‘dh’)", "ދޯނި", "dhoani",
      "dhoni, a Maldivian boat", "boat"),
    T("ތ", "ތާ", "thaa", "th", "a soft ‘t’ — tongue touches the back of the teeth (written ‘th’, not English “th”)",
      "ތަރި", "thari", "star", "star"),
    T("ލ", "ލާމު", "laamu", "l", "‘l’ as in “lamp”", "ލުނބޯ", "lunboa", "lime", "lemon"),
    T("ގ", "ގާފު", "gaafu", "g", "‘g’ as in “go”", "ގަސް", "gas", "tree", "tree"),
    T("ޏ", "ޏަވިޔަނި", "gnaviyani", "gn", "‘ny’ as in “canyon” — a rare old letter", "ޏަވިޔަނި އަތޮޅު",
      "gnaviyani atholhu", "Gnaviyani Atoll (Fuvahmulah island)", "dv_island",
      note=f"{nt('ޏ')} is hardly used in words today, but a whole atoll, the island of Fuvahmulah, carries its name!"),
    T("ސ", "ސީނު", "seenu", "s", "‘s’ as in “sun”", "ސައި", "sai", "tea", "teacup"),
    T("ޑ", "ޑަވިޔަނި", "daviyani", "d", "a hard ‘d’ — curl your tongue back (written ‘d’)", "ހަނޑޫ", "handoo",
      "rice (grains)", "rice", note=inside("ޑ", "ހަނޑޫ")),
    T("ޒ", "ޒަވިޔަނި", "zaviyani", "z", "‘z’ as in “zoo” — mostly in words from Arabic", "ޒަމްޒަމް", "zamzam",
      "Zamzam water from Makkah", "ewer"),
    T("ޓ", "ޓަވިޔަނި", "taviyani", "t", "a hard ‘t’ — curl your tongue back (written ‘t’)", "ޓޮފީ", "tofee",
      "toffee, a sweet", "dv_toffee"),
    T("ޔ", "ޔާ", "yaa", "y", "‘y’ as in “yes”", "ފިޔާ", "fiyaa", "onion", "onion", note=inside("ޔ", "ފިޔާ")),
    T("ޕ", "ޕަވިޔަނި", "paviyani", "p", "‘p’ as in “pen” — mostly in words from English", "ޕެން", "pen", "pen", "pen"),
    T("ޖ", "ޖަވިޔަނި", "javiyani", "j", "‘j’ as in “jam”", "ޖަހާޒު", "jahaazu", "ship", "ship"),
    T("ޗ", "ޗަވިޔަނި", "chaviyani", "ch", "‘ch’ as in “chair”", "ޗީޒް", "cheez", "cheese", "dv_cheese"),
]

FILI_INFO = [("ަ", "އަބަފިލި", "abafili", "a", "‘a’ in “about”"), ("ާ", "އާބާފިލި", "aabaafili", "aa", "‘a’ in “father”"),
             ("ި", "އިބިފިލި", "ibifili", "i", "‘i’ in “sit”"), ("ީ", "އީބީފިލި", "eebeefili", "ee", "‘ee’ in “see”"),
             ("ު", "އުބުފިލި", "ubufili", "u", "‘u’ in “put”"), ("ޫ", "އޫބޫފިލި", "ooboofili", "oo", "‘oo’ in “moon”"),
             ("ެ", "އެބެފިލި", "ebefili", "e", "‘e’ in “bed”"), ("ޭ", "އޭބޭފިލި", "eybeyfili", "ey", "‘ey’ in “they”"),
             ("ޮ", "އޮބޮފިލި", "obofili", "o", "‘o’ in “on”"), ("ޯ", "އޯބޯފިލި", "oaboafili", "oa", "‘o’ in “go”, long")]

_rows = "".join(
    f'<tr><td class="nt" style="font-size:18pt">◌{s}</td><td><span class="nt" style="font-size:12pt">{n}</span> '
    f'<i class="small">{ntr}</i></td><td class="small">{snd}</td>'
    f'<td class="nt" style="font-size:18pt">ބ{s}</td><td class="tr">b{v}</td><td class="nt" style="font-size:18pt">އ{s}</td>'
    f'<td class="tr">{v}</td></tr>' for s, n, ntr, v, snd in FILI_INFO)
_rows += (f'<tr><td class="nt" style="font-size:18pt">◌{SUKUN}</td><td><span class="nt" style="font-size:12pt">ސުކުން</span> '
          f'<i class="small">sukun</i></td><td class="small">no vowel</td><td class="nt" style="font-size:18pt">ބ{SUKUN}</td>'
          f'<td class="tr">b</td><td class="nt" style="font-size:18pt">އ{SUKUN}</td><td class="small">doubles the next letter</td></tr>')

INTRO = f"""<p>Dhivehi is written <b>from right to left</b>, like the Qur’an. Thaana has <b>24 basic letters</b>, and every one of
them is a consonant. The vowels are small strokes called <b>fili</b> (<span class="nt">ފިލި</span>).</p>
<div class="box" style="margin:0.08in 0"><h3>Every letter wears a fili</h3>In a word, each letter carries a fili <b>above</b> or
<b>below</b> it — or the little circle <b>sukun</b>, which means “no vowel”. In this book the big letters are shown bare so you
can color them, and each letter page shows the letter with all ten fili.
<div style="text-align:center;margin-top:3px"><span class="nt" style="font-size:22pt">ބ + ◌ި + ސ + ◌ް = ބިސް</span>
&nbsp; <i>b + i + s = bis</i> (egg)</div></div>
<table class="ft" style="width:100%;border-collapse:collapse;text-align:center;margin-top:0.06in">
<tr style="font:600 10pt Fredoka"><th>Fili</th><th>Name</th><th>Sound</th><th colspan="2">With <span class="nt">ބ</span></th>
<th colspan="2">Start of a word</th></tr>{_rows}</table>
<style>.ft td,.ft th{{border-bottom:1.5px solid #bbb;padding:0 4px;line-height:1.5}}</style>
<p class="small" style="margin-top:0.08in">A vowel at the start of a word sits on <span class="nt">އ</span> <i>alifu</i>, which has no sound of
its own: <span class="nt">އަނބު</span> <i>anbu</i> (mango).</p>"""

LANG = build(dict(
    code="dv", folder="book-17-dhivehi", series_no=17, isbn="", draft=True, dir="rtl",
    name="Dhivehi", native="ދިވެހި", native_tr="dhivehi", name_word="ނަން", write_word="ލިޔެލާ",
    title_native="އަހަރެންގެ ފުރަތަމަ ދިވެހި އަކުރު", title_letters="ހށނރބޅ", belongs_native="މި ފޮތަކީ އަހަރެންގެ ފޮތް",
    belongs_pic="dv_island", alphabet_native="ތާނަ", numbers_native="އަދަދު", numbers_tr="adhadhu",
    phrases_native="ފުރަތަމަ ބަސްތައް",
    fonts=fontset("Noto Sans Thaana", "noto-sans-thaana-thaana", "Noto Sans Thaana", "noto-sans-thaana-thaana")[:3],
    disp_family="Noto Sans Thaana", text_family="Noto Sans Thaana",
    glyph_font=["noto-sans-thaana-thaana-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Thaana",
    extra_css=(".nt{line-height:1.8} .lp-name{font-size:22pt;line-height:1.7} .lp-word .w{font-size:40pt;line-height:1.7}"
               " .ft .small,.ft .tr{direction:ltr}"),
    phon_feature="every letter written with all ten fili, the Thaana vowel signs (ހަ ހާ ހި ހީ…)",
    sections=[section(LETTERS, title="The Thaana Letters", native="ތާނަ އަކުރު",
                      native_tr="thaana akuru — “the Thaana letters”", chart_cols=6, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Dhivehi is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. "
        "Maldivians write long e and o as <b>ey</b> and <b>oa</b>: <i>vaarey</i> (rain), <i>dhoani</i> (boat).",
        "<b>dh</b> and <b>th</b> are a soft <i>d</i> and <i>t</i> with the tongue on the back of the teeth — never the English "
        "“th” of “the”. Plain <b>d</b> and <b>t</b> are hard: curl the tongue back.",
        "<b>lh</b> is an <i>l</i> said with the tongue curled back: <i>valhu</i> (well).",
        "<b>nd, nb, ndh</b> in words like <i>handhu</i> (moon) and <i>anbu</i> (mango): say the <i>n</i> very lightly, gliding into "
        "the next sound."],
    phon_explain=("In Thaana the vowels are small signs called <b>fili</b>. The box marked <i>the letter with its fili</i> shows the "
                  "letter wearing each of the ten fili, with the sound underneath: <span class='nt'>ހަ</span> <i>ha</i>, "
                  "<span class='nt'>ހާ</span> <i>haa</i>, <span class='nt'>ހި</span> <i>hi</i>…"),
    standard="the standard Dhivehi of Malé",
    hello=[
        ("Who speaks it?", "About <b>340,000 people</b> speak Dhivehi, almost all of them in the Maldives.<sup>³</sup>"),
        ("Where?", "In the <b>Maldives</b>: about <b>1,200 small coral islands</b> in the Indian Ocean, in rings called "
                   "<b>atolls</b>. The Maldives is a Muslim country, and island after island has its own mosque."),
        ("How is it written?", "In <b>Thaana</b>, from <b>right to left</b>. The vowels are little strokes called <b>fili</b>, "
                               "written above or below each letter."),
        ("How many letters?", "<b>24</b> basic letters, plus dotted letters for Arabic words: "
                              "<span class='nt'>ޘ ޙ ޚ ޛ ޜ ޝ ޞ ޟ ޠ ޡ ޢ ޣ ޤ ޥ</span>."),
        ("Letters from numbers!", "The first nine letters, <span class='nt'>ހ</span> to <span class='nt'>ވ</span>, were made from "
                                  "the Arabic numerals 1–9, and the next nine from old Dhivehi numerals."),
        ("Letters on the map", "The atolls have letter names in alphabet order, from north to south: Haa Alifu, Shaviyani, "
                               "Noonu, Raa, Baa… all the way down to Seenu."),
    ],
    hello_pics=[("dv_island", {}), ("boat", {}), ("mosque", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(
        frame=[[67.6, -2.0], [79.6, 10.0]],
        points=dict(male=[73.51, 4.18], addu=[73.15, -0.63], fuvahmulah=[73.43, -0.30], kulhudhuffushi=[73.07, 6.62],
                    minicoy=[73.05, 8.28]),
        area=(73.25, 3.0, 80, 380),
        cities=[("male", "Malé", 16, 8, "start", True), ("addu", "Addu", -14, 14, "end", False),
                ("fuvahmulah", "Fuvahmulah", 16, -2, "start", False),
                ("kulhudhuffushi", "Kulhudhuffushi", 16, 8, "start", False), ("minicoy", "Minicoy", 16, 8, "start", False)],
        label="MALDIVES", label_at=[76.4, 2.6], marker=[73.2, 3.2],
        caption="The circle shows the Maldives on the world map.",
        legend="<b>Color it:</b> the sea <b>blue</b> · the land <b>green</b>. <b>Find it:</b> the Maldives are about 1,200 tiny "
               "islands inside the dashed line — most are too small to see on a map! Malé ★ is the capital. Draw little "
               "yellow islands along the chain. Dhivehi is also spoken on Minicoy island, to the north.",
        seas=[("Indian Ocean", 70.4, -1.2), ("Arabian Sea", 70.2, 8.6)], world_r=10),
    digits=[("0", "ސުމެއް", "sumeh", "zero"), ("1", "އެކެއް", "ekeh", "one"), ("2", "ދޭއް", "dhey", "two"),
            ("3", "ތިނެއް", "thineh", "three"), ("4", "ހަތަރެއް", "hathareh", "four"), ("5", "ފަހެއް", "faheh", "five"),
            ("6", "ހައެއް", "haeh", "six"), ("7", "ހަތެއް", "hatheh", "seven"), ("8", "އަށެއް", "asheh", "eight"),
            ("9", "ނުވައެއް", "nuvaeh", "nine")],
    phrases=[("އައްސަލާމު ޢަލައިކުމް", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ވަޢަލައިކުމް އައްސަލާމް", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("އަހަރެންގެ ނަމަކީ …", "aharenge namakee …", "My name is …"),
             ("ޝުކުރިއްޔާ", "shukuriyyaa", "Thank you"),
             ("ޖަޒާކަﷲ ޚައިރަން", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("މަންމަ · ބައްޕަ", "manma · bappa", "Mother · Father"),
             ("ބޭބެ · ދައްތަ", "beybe · dhaththa", "Big brother · Big sister"),
             ("އާން · ނޫން", "aan · noon", "Yes · No"),
             ("އަހަރެން ދިވެހި ބަސް ދަސްކުރަމުން ދަނީ!", "aharen dhivehi bas dhaskuramun dhanee!", "I am learning Dhivehi!")],
    cheer=("މާޝާﷲ! ވަރަށް ރަނގަޅު!", "maashaallaah! varah rangalhu!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); the history of the Thaana letters from "
                 "standard reference works on the script.",
    book_pic=dict(left="ހ ށ ނ", right="ރ ބ ޅ"),
    review_note=("Check the letter names, the fili names (abafili … oaboafili, sukun) and the transliterations. Words to confirm: "
                 "ކާށި (for ށ), ވަޅު (well, for ޅ), ހަނޑޫ (for ޑ), ޓޮފީ (toffee, for ޓ), ޕެން (pen — or ގަލަން?), ޖަހާޒު (ship), "
                 "ޗީޒް (cheese, for ޗ). ޏ has no everyday word: the page uses the atoll name ޏަވިޔަނި އަތޮޅު (Fuvahmulah) — "
                 "please suggest a real word if there is one. Also check ބޭބެ · ދައްތަ, ދަސްކުރަމުން ދަނީ, and the Thaana spelling "
                 "of the Muslim phrases."),
    tiles="ހށނރބޅ", cover_pics=["dv_island", "boat", "watermelon", "mosque"], title_size=48,
    speakers_blurb="Dhivehi is the language of the Maldives, spoken by about 340,000 people on its coral islands.",
    sample_words=[("ދޯނި", "dhoani", "boat"), ("ކާށި", "kaashi", "coconut"), ("މިސްކިތް", "miskiy", "mosque")],
    keywords=["dhivehi alphabet book for kids", "learn dhivehi for children", "thaana letters tracing workbook",
              "maldives language coloring book", "muslim kids activity book", "islamic coloring book for children",
              "maldivian heritage language gift"],
))
