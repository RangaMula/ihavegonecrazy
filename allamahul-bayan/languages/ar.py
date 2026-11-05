# -*- coding: utf-8 -*-
"""Book 27 - Arabic (Arabic script, right-to-left, 28 letters + harakat). Allamahul Bayan Series. REVIEW DRAFT.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
Every Arabic word is fully voweled (harakat). Each letter page shows the joined forms and the letter
with fatha, kasra and damma. New pictures: engine/pics/ar_pics.py (ar_bag, ar_bucket, ar_pumpkin).
"""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
FA, KA, DA = "َ", "ِ", "ُ"  # fatha, kasra, damma


def _cell(text, cap, size=22):
    return (f'<div style="flex:1;text-align:center"><div class="ntd" style="font-size:{size}pt;line-height:1.55">{text}</div>'
            f'<div class="small" style="line-height:1.1">{cap}</div></div>')


def _row(cells):  # first cell on the right, like the script
    return f'<div style="display:flex;flex-direction:row-reverse;gap:4px">{"".join(cells)}</div>'


def forms(ch, joins=True):
    if joins:
        return _row([_cell(f"{ch}{JOIN}", "start"), _cell(f"{JOIN}{ch}{JOIN}", "middle"), _cell(f"{JOIN}{ch}", "end")])
    return (_row([_cell(ch, "alone"), _cell(f"{JOIN}{ch}", "after a letter")])
            + '<div class="small" style="text-align:center">It never joins to the letter after it.</div>')


def harakat(base, c):
    b = base if isinstance(base, tuple) else (base,) * 3  # alif carries hamza: أَ إِ أُ
    return ('<div style="border-top:1.5px dashed #999;margin-top:5px;padding-top:2px">'
            + _row([_cell(b[0] + FA, f"{c}a"), _cell(b[1] + KA, f"{c}i"), _cell(b[2] + DA, f"{c}u")]) + "</div>")


def A(ch, name, name_tr, sound, word, tr, meaning, pic, c, joins=True, args=None, note=None, extra=None, base=None, quran=None):
    phon = forms(ch, joins) + harakat(base or ch, c)
    if extra:
        phon += f'<div class="small" style="margin-top:3px">{extra}</div>'
    if quran:
        note = (note + " " if note else "") + f"<i>In the Qur’an:</i> {quran}"
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, "Shapes · and with ḥarakāt", args, note)


LETTERS = [
    A("ا", "أَلِف", "alif", "a long ‘aa’ as in “father”; at the start of a word it wears a little hamza (أ إ) and says a, i or u",
      "إِبْرِيق", "ibreeq", "jug, water ewer", "ewer", "", joins=False, base=("أ", "إ", "أ")),
    A("ب", "بَاء", "baa", "‘b’ as in “ball”", "بَيْت", "bayt", "house", "house", "b", quran="Al-Baqarah 2:127"),
    A("ت", "تَاء", "taa", "‘t’ as in “tap”", "تَمْر", "tamr", "dates", "dates", "t"),
    A("ث", "ثَاء", "thaa", "‘th’ as in “three”", "ثَلْج", "thalj", "ice, snow", "ice", "th"),
    A("ج", "جِيم", "jeem", "‘j’ as in “jam”", "جَبَل", "jabal", "mountain", "mountain", "j", quran="Al-Aʿrāf 7:143"),
    A("ح", "حَاء", "ḥaa", "a strong, breathy ‘ḥ’ from the middle of the throat — like breathing on a mirror to clean it",
      "حَقِيبَة", "ḥaqeeba", "school bag", "ar_bag", "ḥ"),
    A("خ", "خَاء", "khaa", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خُبْز", "khubz", "bread",
      "roti", "kh", quran="Yūsuf 12:36"),
    A("د", "دَال", "daal", "‘d’ as in “dog”", "دَلْو", "dalw", "bucket (for a well)", "ar_bucket", "d", joins=False,
      quran="Yūsuf 12:19"),
    A("ذ", "ذَال", "dhaal", "‘dh’ — the ‘th’ in “this”", "ذُرَة", "dhura", "corn", "corn", "dh", joins=False),
    A("ر", "رَاء", "raa", "a rolled ‘r’ — let the tongue tap", "رُمَّان", "rummaan", "pomegranate", "pomegranate", "r",
      joins=False, quran="Ar-Raḥmān 55:68"),
    A("ز", "زَاي", "zaay", "‘z’ as in “zoo”", "زَيْتُون", "zaytoon", "olives", "olive", "z", joins=False,
      quran="At-Tīn 95:1"),
    A("س", "سِين", "seen", "‘s’ as in “sun”", "سَفِينَة", "safeena", "ship", "ship", "s", quran="Al-Kahf 18:71"),
    A("ش", "شِين", "sheen", "‘sh’ as in “shoe”", "شَمْس", "shams", "sun", "sun", "sh", quran="Ash-Shams 91:1"),
    A("ص", "صَاد", "ṣaad", "a heavy ‘ṣ’ — say ‘s’ with a full, round mouth", "صَابُون", "ṣaaboon", "soap", "soap", "ṣ"),
    A("ض", "ضَاد", "ḍaad", "a heavy ‘ḍ’ — say ‘d’ with a full, round mouth", "ضَوْء", "ḍaw’", "light", "bulb", "ḍ",
      extra="Arabic is called <i>the language of ḍaad</i>, because this sound is so special to it."),
    A("ط", "طَاء", "ṭaa", "a heavy ‘ṭ’ — say ‘t’ with a full, round mouth", "طَائِرَة", "ṭaa’ira", "aeroplane", "plane", "ṭ"),
    A("ظ", "ظَاء", "ẓaa", "a heavy ‘ẓ’ — the ‘th’ of “this”, said with a full, round mouth", "ظَرْف", "ẓarf", "envelope",
      "envelope", "ẓ"),
    A("ع", "عَيْن", "ʿayn", "a squeezed sound from deep in the throat — listen to a reciter and copy", "عِنَب", "ʿinab",
      "grapes", "grapes", "ʿ", quran="ʿAbasa 80:28"),
    A("غ", "غَيْن", "ghayn", "a soft, gargled ‘gh’ from the back of the throat", "غَيْمَة", "ghayma", "cloud", "clouds", "gh"),
    A("ف", "فَاء", "faa", "‘f’ as in “fan”", "فَانُوس", "faanoos", "lantern", "eid", "f"),
    A("ق", "قَاف", "qaaf", "a ‘q’ — a ‘k’ said far back in the throat", "قَلَم", "qalam", "pen", "pen", "q",
      quran="Al-Qalam 68:1"),
    A("ك", "كَاف", "kaaf", "‘k’ as in “kite”", "كِتَاب", "kitaab", "book", "book", "k",
      args=dict(left="ث ج ح", right="ا ب ت"), quran="Al-Baqarah 2:2"),
    A("ل", "لَام", "laam", "‘l’ as in “lamp”", "لَيْمُون", "laymoon", "lemon", "lemon", "l",
      extra='<span class="nt">ل</span> + <span class="nt">ا</span> make a special shape: <span class="nt" style="font-size:15pt">لَا</span> <i>laa</i>.'),
    A("م", "مِيم", "meem", "‘m’ as in “moon”", "مَسْجِد", "masjid", "mosque", "mosque", "m", quran="Al-Isrāʾ 17:1"),
    A("ن", "نُون", "noon", "‘n’ as in “net”", "نَجْمَة", "najma", "star", "star", "n"),
    A("ه", "هَاء", "haa", "a soft ‘h’ as in “hat”", "هِلَال", "hilaal", "new crescent moon", "moon", "h",
      extra='With two dots, <span class="nt">ـة</span> is <i>taa marbooṭa</i>, a word ending: <span class="nt">نَجْمَة</span>.'),
    A("و", "وَاو", "waaw", "‘w’ as in “water”, or the long vowel ‘oo’", "وَرْدَة", "warda", "rose, flower", "flower", "w",
      joins=False),
    A("ي", "يَاء", "yaa", "‘y’ as in “yes”, or the long vowel ‘ee’", "يَقْطِين", "yaqṭeen", "gourd, pumpkin", "ar_pumpkin", "y",
      quran="Aṣ-Ṣāffāt 37:146"),
]

_H = 'style="font-size:24pt;line-height:1.5"'
INTRO = f"""<p>Arabic is written <b>from right to left</b>, just like the Qur’an. Open your book at any letter page and start
reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them, and their shape
changes a little at the start, middle and end of a word. Six letters, <span class="nt" style="font-size:15pt">ا د ذ ر ز و</span>,
never join to the letter after them.
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.6">ب + ي + ت = بَيْت</div>
<div style="text-align:center"><i>b + ay + t = bayt</i> (house)</div></div>
<div class="box" style="margin:0.08in 0"><h3>Dots make the difference</h3>Many letters share one shape and differ only in their dots:
<div class="ntd" style="font-size:24pt;text-align:center;direction:rtl;line-height:1.6">ب &nbsp;ت &nbsp;ث &nbsp;&nbsp;·&nbsp;&nbsp; ج &nbsp;ح &nbsp;خ &nbsp;&nbsp;·&nbsp;&nbsp; س &nbsp;ش</div></div>
<div class="box" style="margin:0.08in 0"><h3>Ḥarakāt — the little vowel marks</h3>Arabic letters are consonants. The short vowels
are tiny marks above or below a letter, called <b>ḥarakāt</b>. The muṣḥaf always shows them, and so does every word in this book.
<div style="display:flex;flex-direction:row-reverse;justify-content:space-around;text-align:center;margin-top:4px">
<div><div class="ntd" {_H}>بَ</div><b>fatḥa</b> — a line above<br>says <b>a</b>: <i>ba</i></div>
<div><div class="ntd" {_H}>بِ</div><b>kasra</b> — a line below<br>says <b>i</b>: <i>bi</i></div>
<div><div class="ntd" {_H}>بُ</div><b>ḍamma</b> — a little waw<br>says <b>u</b>: <i>bu</i></div></div>
<div style="display:flex;flex-direction:row-reverse;justify-content:space-around;text-align:center;margin-top:6px;border-top:1.5px dashed #999;padding-top:4px">
<div><div class="ntd" {_H}>بْ</div><b>sukoon</b> — no vowel<br><span class="nt">قَلْب</span> <i>qalb</i> (heart)</div>
<div><div class="ntd" {_H}>بّ</div><b>shadda</b> — say it twice<br><span class="nt">رَبّ</span> <i>rabb</i> (Lord)</div>
<div><div class="ntd" {_H}>بً بٍ بٌ</div><b>tanween</b> — adds an ‘n’<br><i>ban · bin · bun</i></div></div></div>"""

LANG = build(dict(
    code="ar", folder="book-27-arabic", series_no=27, isbn="", draft=True, dir="rtl",
    name="Arabic", native="العَرَبِيَّة", native_tr="al-ʿarabiyya", name_word="اِسْم", write_word="اُكْتُبْ",
    title_native="كِتَابِي الْأَوَّلُ لِلْحُرُوفِ الْعَرَبِيَّةِ", title_letters="ابتثجح",
    belongs_native="هٰذَا كِتَابِي", belongs_pic="pen",
    alphabet_native="الْحُرُوفُ الْهِجَائِيَّةُ", numbers_native="الْأَعْدَادُ", numbers_tr="al-aʿdaad",
    phrases_native="كَلِمَاتِي الْأُولَى",
    fonts=fontset("Baloo Bhaijaan 2", "baloo-bhaijaan-2-arabic", "Noto Naskh Arabic", "noto-naskh-arabic-arabic"),
    disp_family="Baloo Bhaijaan 2", text_family="Noto Naskh Arabic",
    glyph_font="baloo-bhaijaan-2-arabic-800-normal.woff2", font_credit="Baloo Bhaijaan 2, Noto Naskh Arabic",
    extra_css=(".nt{line-height:1.9} .lp-name{font-size:24pt;line-height:1.5} "
               ".lp-word .w{font-size:40pt;line-height:1.7} .lp-info .box .small{line-height:1.25}"),
    phon_feature="the letter’s <b>joined shapes</b> and its sounds with the vowel marks <b>fatḥa, kasra and ḍamma</b>",
    sections=[section(LETTERS, title="The Arabic Letters", native="الْحُرُوفُ الْهِجَائِيَّةُ",
                      native_tr="al-ḥuroof al-hijaa’iyya — “the letters for spelling”",
                      chart_cols=7, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Arabic is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. Hold them for two "
        "beats, just as in Qur’an recitation.",
        "<b>A dot under a letter</b> (<i>ṣ, ḍ, ṭ, ẓ</i>) means a <i>heavy</i> sound said with a full, round mouth. "
        "<b>ḥ</b> is a strong, breathy h from the middle of the throat.",
        "<b>ʿ</b> stands for ʿayn, a squeezed sound deep in the throat; <b>’</b> stands for hamza, a tiny catch in the voice, as in “uh-oh”.",
        "<b>th</b> as in “three”, <b>dh</b> as in “this”; <b>kh</b> and <b>gh</b> are soft throat sounds; <b>q</b> is a k said deep in the throat."],
    phon_explain="Arabic letters <b>change shape</b> when they join, so the third box shows each letter at the start, middle and "
                 "end of a word, and then with the three short-vowel marks (<i>ḥarakāt</i>): fatḥa <i>a</i>, kasra <i>i</i> and "
                 "ḍamma <i>u</i>. A small note shows where a word on the page also appears in the Qur’an.",
    standard="Modern Standard Arabic (<i>fuṣḥā</i>), the Arabic of books and close to the Arabic of the Qur’an",
    hello=[
        ("Who speaks it?", "About <b>380 million people</b> speak Arabic as a first or second language,<sup>³</sup> and Muslims all "
                           "over the world read the Qur’an in Arabic."),
        ("Where?", "Arabic is an official language in <b>more than 20 countries</b>, from <b>Morocco</b> on the Atlantic Ocean to "
                   "<b>Oman</b> on the Arabian Sea, across North Africa and West Asia."),
        ("How is it written?", "From <b>right to left</b>. Most letters <b>join</b> to the next one and change shape. The short vowels "
                               "are little marks called <b>ḥarakāt</b>."),
        ("How many letters?", "<b>28 letters</b>. Many of them share a shape and differ only in their <b>dots</b>: "
                              "<span class='nt'>ب ت ث</span>."),
        ("The language of the Qur’an", "Allah sent down the Qur’an in Arabic: <span class='nt'>قُرْآنًا عَرَبِيًّا</span> "
                                        "<i>qur’aanan ʿarabiyyan</i>, “an Arabic Qur’an” (Surah Yūsuf 12:2).<sup>³</sup>"),
        ("Did you know?", "English has borrowed words from Arabic: <i>sugar</i> (<span class='nt'>سُكَّر</span> sukkar), "
                          "<i>lemon</i> (<span class='nt'>لَيْمُون</span> laymoon) and <i>zero</i> (<span class='nt'>صِفْر</span> ṣifr)."),
    ],
    hello_pics=[("pen", {}), ("mosque", {}), ("dates", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[-17.0, 6.0], [66.0, 42.0]],
                   points=dict(makkah=[39.83, 21.42], madinah=[39.61, 24.47], cairo=[31.24, 30.04], baghdad=[44.36, 33.31],
                               damascus=[36.29, 33.51], muscat=[58.41, 23.59], tunis=[10.18, 36.81], casablanca=[-7.59, 33.57]),
                   area=None,
                   cities=[("makkah", "Makkah", 18, 14, "start", True), ("madinah", "Madinah", 14, 4, "start", False),
                           ("cairo", "Cairo", -14, 22, "end", False), ("baghdad", "Baghdad", 14, 8, "start", False),
                           ("damascus", "Damascus", 0, -16, "middle", False), ("muscat", "Muscat", -14, 26, "end", False),
                           ("tunis", "Tunis", 14, -6, "start", False), ("casablanca", "Casablanca", 14, 24, "start", False)],
                   label="THE ARAB WORLD", label_at=[18.0, 22.0], marker=[25.0, 25.0],
                   caption="The circle shows North Africa and West Asia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Makkah ★, the city of the Kaaba, "
                          "where the Qur’an was first revealed. Arabic is also spoken in Madinah, Cairo, Baghdad, Damascus, Muscat, "
                          "Tunis, Casablanca and many more cities.",
                   seas=[("Mediterranean Sea", 17.5, 33.9), ("Red Sea", 37.6, 17.4), ("Arabian Sea", 62.0, 15.0)], world_r=28),
    digits=[("٠", "صِفْر", "ṣifr", "zero"), ("١", "وَاحِد", "waaḥid", "one"), ("٢", "اِثْنَان", "ithnaan", "two"),
            ("٣", "ثَلَاثَة", "thalaatha", "three"), ("٤", "أَرْبَعَة", "arbaʿa", "four"), ("٥", "خَمْسَة", "khamsa", "five"),
            ("٦", "سِتَّة", "sitta", "six"), ("٧", "سَبْعَة", "sabʿa", "seven"), ("٨", "ثَمَانِيَة", "thamaaniya", "eight"),
            ("٩", "تِسْعَة", "tisʿa", "nine")],
    phrases=[("اَلسَّلَامُ عَلَيْكُمْ", "as-salaamu ʿalaykum", "Peace be upon you (the Muslim greeting)"),
             ("وَعَلَيْكُمُ السَّلَامُ", "wa ʿalaykumus-salaam", "And upon you be peace (the reply)"),
             ("اِسْمِي …", "ismee …", "My name is …"),
             ("شُكْرًا", "shukran", "Thank you"),
             ("جَزَاكَ اللّٰهُ خَيْرًا", "jazaakallaahu khayran", "May Allah reward you with good"),
             ("أُمِّي · أَبِي", "ummee · abee", "My mother · My father"),
             ("أَخِي · أُخْتِي", "akhee · ukhtee", "My brother · My sister"),
             ("نَعَمْ · لَا", "naʿam · laa", "Yes · No"),
             ("أَنَا أَتَعَلَّمُ الْعَرَبِيَّةَ!", "anaa ataʿallamul-ʿarabiyya!", "I am learning Arabic!")],
    cheer=("مَا شَاءَ اللّٰهُ! أَحْسَنْتَ!", "maa shaa’allaah! aḥsanta! (to a girl: aḥsanti)", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded. Surah Yūsuf 12:2 and the Qur’an references on the "
                 "letter pages were checked against <b>Quran.com</b>.",
    book_pic=dict(left="ث ج ح", right="ا ب ت"),
    review_note="Check every voweled word and letter name (especially the endings: words are shown in pause form, without a final "
                "case vowel), the transliterations, ضَوْء for ض and غَيْمَة for غ, and the Qur’an references on the letter pages "
                "(each names one verse where the word appears). Speaker number (about 380 million) needs a current Ethnologue check.",
    tiles="ابتثجح", cover_pics=["pen", "mosque", "dates", "moon"], title_size=48,
    speakers_blurb="Arabic is the language of the Qur’an and is spoken by about 380 million people across North Africa and West Asia.",
    sample_words=[("قَلَم", "qalam", "pen"), ("مَسْجِد", "masjid", "mosque"), ("كِتَاب", "kitaab", "book")],
    keywords=["arabic alphabet book for kids", "learn arabic letters for children", "arabic alphabet coloring book",
              "huroof hijaiyah tracing workbook", "harakat fatha kasra damma for kids", "islamic coloring book for children",
              "quran arabic letters preschool"],
))
LANG["series_line"] = ("<b>Book 27 is Arabic</b> — the language of the Qur’an. More languages from around the world are in the "
                       "series, in shā’ Allāh.")
LANG["cover"]["bullets"][3] = "<b>Right-to-left tracing rows</b>, a warm-up page and the vowel marks — a first step towards reading the Qur’an"
