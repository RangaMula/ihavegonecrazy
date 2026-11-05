# -*- coding: utf-8 -*-
"""Book 31 - Malay in Jawi script (Arabic-based, right-to-left, 37 letters). Allamahul Bayan Series. REVIEW DRAFT.
Modelled on ur.py (joined forms, dir="rtl"). The transliteration line under every word is its Rumi (Latin)
spelling, the way Malay is written in Latin letters. Letter order follows the Dewan Bahasa dan Pustaka list
(ا ب ت ة ث ج ح چ خ د ذ ر ز س ش ص ض ط ظ ع غ ڠ ف ڤ ق ک ݢ ل م ن و ۏ ه ء ي ى ڽ).
Pictures: objects, plants and nature only."""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
PH = "Letter shapes · how it joins"
BIG = 'class="ntd" style="font-size:24pt"'


def forms(ch, kind="dual"):
    if kind == "right":   # joins only to the letter before it
        return (f'<div style="font-size:12pt">Alone <span {BIG}>{ch}</span> · '
                f'after a letter <span {BIG}>{JOIN}{ch}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    if kind == "final":   # only at the end of a word
        return (f'<div style="font-size:12pt">End of a word: <span {BIG}>{ch}</span> · '
                f'after a joining letter <span {BIG}>{JOIN}{ch}</span></div>'
                f'<div class="small">It is only found at the end of a word.</div>')
    if kind == "none":    # hamzah
        return (f'<div style="font-size:12pt">Always alone: <span {BIG}>{ch}</span></div>'
                f'<div class="small">It never joins to any letter. It sits on the line between two vowels.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def J(ch, name, name_tr, sound, word, tr, meaning, pic, kind="dual", note=None, args=None, extra=None):
    phon = forms(ch, kind) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


S = "<span class='nt'>{}</span>".format
ARABIC = "Used mostly in words that come from Arabic."
JAWI = "A Jawi letter: Arabic has no letter for this sound."

LETTERS = [
    J("ا", "اليف", "alif", "‘a’ as in “father”; at the start of a word it can also carry ‘e’, ‘i’ or ‘u’", "اون", "awan", "cloud",
      "clouds", kind="right"),
    J("ب", "با", "ba", "‘b’ as in “ball”", "بولن", "bulan", "moon", "moon", extra="One dot below."),
    J("ت", "تا", "ta", "‘t’ as in “top”", "تلور", "telur", "egg", "egg", extra="Two dots above."),
    J("ة", "تا مربوطة", "ta marbutah", "‘t’ (or ‘h’) — only at the end of words from Arabic", "صلاة", "solat", "prayer (salah)",
      "prayermat", kind="final", note="Find " + S("ة") + " at the end of " + S("صلاة") + "!"),
    J("ث", "سا", "sa", "‘s’ as in “sun”", "ثلاث", "Selasa", "Tuesday — the third day of the week", "ms_calendar",
      args=dict(label="٣"), extra=ARABIC),
    J("ج", "جيم", "jim", "‘j’ as in “jam”", "جاݢوڠ", "jagung", "corn (maize)", "corn"),
    J("ح", "حا", "ḥa", "a strong breathy ‘h’ from the middle of the throat", "حاجي", "haji", "Hajj, the journey to the Kaaba in Makkah",
      "kaaba", extra=ARABIC),
    J("چ", "چا", "ca", "‘ch’ as in “chair” — written <b>c</b> in Rumi", "چاون", "cawan", "cup", "teacup", extra=JAWI),
    J("خ", "خا", "kha", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خيمه", "khemah", "tent", "ms_tent",
      extra=ARABIC),
    J("د", "دال", "dal", "‘d’ as in “dog”", "داون", "daun", "leaf", "ms_leaf", kind="right"),
    J("ذ", "ذال", "zal", "‘z’ as in “zoo”", "ذکير", "zikir", "dhikr — remembering Allah", "tasbih", kind="right", extra=ARABIC),
    J("ر", "را", "ra", "a rolled or tapped ‘r’", "رومه", "rumah", "house", "house", kind="right"),
    J("ز", "زاي", "zai", "‘z’ as in “zoo”", "زيتون", "zaitun", "olives", "olive", kind="right"),
    J("س", "سين", "sin", "‘s’ as in “sun”", "سوڠاي", "sungai", "river", "waves"),
    J("ش", "شين", "syin", "‘sh’ as in “shoe” — written <b>sy</b> in Rumi", "شوال", "Syawal", "Syawal, the month of Eid (Hari Raya)",
      "eid"),
    J("ص", "صاد", "sad", "‘s’ as in “sun”", "صابون", "sabun", "soap", "soap", extra=ARABIC),
    J("ض", "ضاد", "dad", "‘d’ as in “dog” (in Arabic, a heavy ‘ḍ’)", "رمضان", "Ramadan", "Ramadan, the month of fasting", "iftar",
      note="Find " + S("ض") + " near the end of " + S("رمضان") + ".", extra=ARABIC),
    J("ط", "طا", "ṭa", "‘t’ as in “top” (in Arabic, a heavy ‘ṭ’)", "طهارة", "taharah", "taharah — washing to be clean for prayer",
      "ewer", extra=ARABIC),
    J("ظ", "ظا", "ẓa", "‘z’ as in “zoo” (in Arabic, a heavy ‘ẓ’)", "ظهر", "Zohor", "Zuhr — the time of the midday prayer", "clock",
      extra=ARABIC),
    J("ع", "عين", "ain", "in Malay, just the vowel next to it — in Arabic, a sound from deep in the throat", "علمو", "ilmu",
      "knowledge, learning", "book", args=dict(left="ا ب ت", right="ج ح چ"), extra=ARABIC),
    J("غ", "غين", "ghain", "a soft gargled ‘gh’ from the back of the throat", "مغرب", "Maghrib", "sunset — the time of the evening prayer",
      "ms_sunset", note="Find " + S("غ") + " in the middle of " + S("مغرب") + ".", extra=ARABIC),
    J("ڠ", "ڠا", "nga", "‘ng’ as in “sing” — written <b>ng</b> in Rumi", "بوڠا", "bunga", "flower", "flower",
      note="Find " + S("ڠ") + " in the middle of " + S("بوڠا") + "!", extra=JAWI + " Three dots above " + S("ع") + "."),
    J("ف", "فا", "fa", "‘f’ as in “fan”", "فجر", "fajar", "dawn", "sunrise"),
    J("ڤ", "ڤا", "pa", "‘p’ as in “pen”", "ڤيسڠ", "pisang", "banana", "banana", extra=JAWI + " Three dots above " + S("ف") + "."),
    J("ق", "قاف", "qaf", "‘k’ said far back in the throat (in Malay, often just ‘k’)", "قلم", "kalam", "pen", "pen"),
    J("ک", "کاف", "kaf", "‘k’ as in “kite”", "کتوڤت", "ketupat", "ketupat — rice cooked in a woven palm-leaf case for Hari Raya",
      "ms_ketupat"),
    J("ݢ", "ݢا", "ga", "‘g’ as in “go”", "ݢونوڠ", "gunung", "mountain", "mountain", extra=JAWI + " One dot above " + S("ک") + "."),
    J("ل", "لام", "lam", "‘l’ as in “lamp”", "ليماو", "limau", "lime, citrus fruit", "lemon"),
    J("م", "ميم", "mim", "‘m’ as in “moon”", "مسجد", "masjid", "mosque", "mosque"),
    J("ن", "نون", "nun", "‘n’ as in “net”", "ناسي", "nasi", "cooked rice", "rice"),
    J("و", "واو", "wau", "‘w’ as in “water”, or the vowels ‘u’ and ‘o’", "واو", "wau", "wau — a big Malay kite", "kite", kind="right",
      note="The letter’s name and the word sound the same!"),
    J("ۏ", "ۏا", "va", "‘v’ as in “van” — only in borrowed words", "ۏيتامين", "vitamin", "vitamins", "medicine", kind="right",
      extra=JAWI + " One dot above " + S("و") + "."),
    J("ه", "ها", "ha", "‘h’ as in “hat”", "هوجن", "hujan", "rain", "raincloud"),
    J("ء", "همزه", "hamzah", "a tiny break in the voice between two vowels", "کاءين", "kain", "cloth", "scarf", kind="none",
      note="Find the " + S("ء") + " between the two vowels of " + S("کاءين") + " <i>ka-in</i>."),
    J("ي", "يا", "ya", "‘y’ as in “yes”, or the vowels ‘i’ and ‘e’", "ڤايوڠ", "payung", "umbrella", "umbrella",
      note="Find " + S("ي") + " in the middle of " + S("ڤايوڠ") + "."),
    J("ى", "اليف مقصورة", "alif maksurah", "‘a’ — only at the end of some words from Arabic", "ضحى", "Duha",
      "Duha — the bright late-morning time", "sun", kind="final", note="Find " + S("ى") + " at the end of " + S("ضحى") + "!",
      extra="It looks like " + S("ي") + " without its dots."),
    J("ڽ", "ڽا", "nya", "‘ny’ as in “canyon” — written <b>ny</b> in Rumi", "ڽيور", "nyiur", "coconut palm", "ms_palm",
      extra=JAWI + " Three dots below."),
]

INTRO = """<p>Jawi is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Arabic letters, plus six more</h3>Jawi uses the Arabic letters and adds six of its own for
Malay sounds:
<div style="text-align:center;direction:rtl"><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">چ</div><div><i>c</i></div></div><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">ڠ</div><div><i>ng</i></div></div><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">ڤ</div><div><i>p</i></div></div><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">ݢ</div><div><i>g</i></div></div><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">ۏ</div><div><i>v</i></div></div><div style="display:inline-block;width:0.75in;text-align:center"><div class="ntd" style="font-size:24pt;line-height:1.5">ڽ</div><div><i>ny</i></div></div></div></div>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them and change shape a little:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.7">ب + و + ل + ن = <span class="nt">بولن</span></div>
<div style="text-align:center"><i>b + u + l + n = bulan</i> (moon)</div></div>
<div class="box"><h3>Two ways to write Malay</h3>Malay is also written in Latin letters, called <b>Rumi</b>. Under every Jawi word in this
book you will find its Rumi spelling: <span class="nt">بولن</span> = <i>bulan</i>.</div>"""

LANG = build(dict(
    code="ms", folder="book-31-malay", series_no=31, isbn="", draft=True, dir="rtl",
    name="Malay", native="بهاس ملايو", native_tr="bahasa Melayu", name_word="نام", write_word="توليس",
    title="My First Malay Jawi Alphabet", cover_title_html="My First<br>Jawi Alphabet", title_size=48,
    subtitle="A Coloring Book to Learn, Trace & Say the 37 Jawi Letters of Malay with English Phonetics",
    title_native="حروف جاوي ڤرتام ساي", title_letters="ابتچڠڤ", belongs_native="بوکو اين ميليق",
    belongs_pic="pen", alphabet_native="حروف جاوي", numbers_native="نومبور", numbers_tr="nombor",
    phrases_native="ڤرکاتاءن ڤرتام",
    fonts=fontset("Vazirmatn", "vazirmatn-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic"),
    disp_family="Vazirmatn", text_family="Noto Naskh Arabic",
    glyph_font=["vazirmatn-arabic-800-normal.woff2", "vazirmatn-latin-800-normal.woff2"],
    font_credit="Vazirmatn, Noto Naskh Arabic",
    extra_css=".nt{line-height:1.8;font-size:1.12em} .lp-name{font-size:24pt;line-height:1.6} .lp-word .w{font-size:38pt;line-height:1.5}",
    phon_feature="each letter’s <b>joined shapes</b> (start · middle · end) and the <b>Rumi</b> spelling of every word",
    sections=[section(LETTERS, native="حروف جاوي", native_tr="huruf Jawi — “the Jawi letters”", chart_cols=7, warmup_cols=6,
                      intro_html=INTRO)],
    sound_notes=[
        "<b>Jawi is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>The line under each word is its Rumi spelling</b> — Malay in Latin letters. Rumi is easy to read aloud: "
        "<i>a</i> as in “father”, <i>i</i> as in “see”, <i>u</i> as in “put”, and <i>e</i> is usually a short ‘uh’ (as in “about”).",
        "In Rumi, <b>c</b> says ‘ch’ (<i>cawan</i> = “chah-wan”), <b>sy</b> says ‘sh’, <b>ng</b> is the sound in “sing” and "
        "<b>ny</b> is the sound in “canyon”.",
        "<b>Some letters sound the same</b> in Malay (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ظ</span> all say <i>z</i>). "
        "They keep their Arabic spelling, which helps when children later read the Qur’an."],
    phon_explain="Because Jawi letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="standard Malay as written in Malaysia and Brunei",
    hello=[
        ("Who speaks it?", "About <b>80 million people</b> speak Malay as a first or second language, and Indonesian, "
                           "a form of Malay, is spoken by many millions more.<sup>³</sup>"),
        ("Where?", "In <b>Malaysia</b>, <b>Brunei</b>, <b>Singapore</b> and <b>southern Thailand</b>, and by families around the world."),
        ("How is it written?", "Malay has two scripts: <b>Rumi</b> (Latin letters) and <b>Jawi</b>, an Arabic-based script written "
                               "from <b>right to left</b>. Jawi has been used for Malay for hundreds of years."),
        ("How many letters?", "This book teaches <b>37 Jawi letters</b>: the Arabic letters plus six made for Malay sounds — "
                              "<span class='nt'>چ ڠ ڤ ݢ ۏ ڽ</span>."),
        ("Where can you see Jawi?", "On mosques, school books and religious lessons, on street signs in some states, and in Brunei, "
                                    "where Jawi is written alongside Rumi."),
        ("A friend of the Qur’an", "Many Malay words come from Arabic: <span class='nt'>مسجد</span> <i>masjid</i> (mosque), "
                                    "<span class='nt'>علمو</span> <i>ilmu</i> (knowledge). Knowing Jawi helps with reading the Qur’an."),
    ],
    hello_pics=[("kite", {}), ("banana", {}), ("mosque", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[96.0, -6.0], [121.0, 14.0]],
                   points=dict(kl=[101.69, 3.14], bsb=[114.94, 4.89], sg=[103.82, 1.35], pattani=[101.25, 6.87],
                               kotabharu=[102.24, 6.13], kuching=[110.34, 1.55]),
                   area=None,
                   cities=[("kl", "Kuala Lumpur", -12, 8, "end", False), ("bsb", "Bandar Seri Begawan", 0, -14, "middle", False),
                           ("sg", "Singapore", 12, 14, "start", False), ("pattani", "Pattani", -12, -6, "end", False),
                           ("kotabharu", "Kota Bharu", 12, 4, "start", False), ("kuching", "Kuching", 12, 14, "start", False)],
                   label="BORNEO", label_at=[115.2, -0.8], marker=[108.0, 3.0],
                   caption="The circle shows Malaysia, Brunei and Singapore on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Malay is spoken in Kuala Lumpur "
                          "and Kota Bharu (Malaysia), Kuching on the island of Borneo, Bandar Seri Begawan (Brunei), Singapore and Pattani "
                          "(southern Thailand).",
                   seas=[("Andaman Sea", 97.8, 9.5), ("Java Sea", 111.0, -4.6)], world_r=18),
    digits=[("٠", "سيفر", "sifar", "zero"), ("١", "ساتو", "satu", "one"), ("٢", "دوا", "dua", "two"), ("٣", "تيݢ", "tiga", "three"),
            ("٤", "امڤت", "empat", "four"), ("٥", "ليم", "lima", "five"), ("٦", "انم", "enam", "six"), ("٧", "توجوه", "tujuh", "seven"),
            ("٨", "لاڤن", "lapan", "eight"), ("٩", "سمبيلن", "sembilan", "nine")],
    phrases=[("السلام عليکم", "assalamualaikum", "Peace be upon you (the Muslim greeting)"),
             ("وعليکم السلام", "waalaikumussalam", "And upon you be peace (the reply)"),
             ("نام ساي …", "nama saya …", "My name is …"),
             ("تريما کاسيه", "terima kasih", "Thank you"),
             ("جزاک الله خيرا", "jazakallahu khairan", "May Allah reward you with good"),
             ("ايبو · باڤ", "ibu · bapa", "Mother · Father"),
             ("ابڠ · کاکق", "abang · kakak", "(Older) brother · (older) sister"),
             ("ي · تيدق", "ya · tidak", "Yes · No"),
             ("ساي سدڠ بلاجر بهاس ملايو!", "saya sedang belajar bahasa Melayu!", "I am learning Malay!")],
    cheer=("ماشاءالله! باݢوس!", "masya-Allah! bagus!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="ا ب ت", right="چ ڠ ڤ"),
    review_note=("Check every Jawi spelling against the Dewan Bahasa dan Pustaka rules, the letter order and count (37, with ة ى ۏ), the "
                 "letter names, and in particular: کاءين kain (cloth) for ء, ثلاث Selasa for ث, ضحى Duha for ى, صلاة solat for ة, "
                 "طهارة taharah for ط, ظهر Zohor for ظ, علمو ilmu for ع, خيمه khemah for خ, قلم kalam (pen) for ق, ڽيور nyiur for ڽ, "
                 "ۏيتامين vitamin for ۏ; whether kaf should be ک (as here) or ك; the Arabic-Indic digits ٠–٩ (Western 0–9 are also common); "
                 "the title حروف جاوي ڤرتام ساي, ي for “ya”, and the speaker figure (about 80 million)."),
    tiles="ڠڤݢڽچب", cover_pics=["kite", "banana", "pen", "mosque"],
    speakers_blurb="Malay is spoken by about 80 million people in Malaysia, Brunei, Singapore and southern Thailand, and Jawi is its "
                   "traditional Arabic-based script.",
    sample_words=[("بولن", "bulan", "moon"), ("بوڠا", "bunga", "flower"), ("مسجد", "masjid", "mosque")],
    keywords=["jawi alphabet book for kids", "learn jawi for children", "malay jawi letters tracing workbook",
              "huruf jawi coloring book", "muslim kids activity book", "islamic coloring book for children",
              "malay heritage language gift"],
))
