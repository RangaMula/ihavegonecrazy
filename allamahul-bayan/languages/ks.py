# -*- coding: utf-8 -*-
"""Book 18 - Kashmiri (Perso-Arabic script, right-to-left). Allamahul Bayan Series. REVIEW DRAFT.
Modelled on ur.py (joined forms, dir="rtl"). Pictures: objects, plants and nature only.
Kashmiri-only vowel marks (ٲ ٕ ۄ ێ ؠ ...) are explained on the section intro page."""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel, used to show joined forms
PH = "Letter shapes · how it joins"


def forms(ch, joins=True, only_final=False):
    if only_final:
        return (f'<div style="font-size:12pt">Joined to the letter before: '
                f'<span class="ntd" style="font-size:24pt">{JOIN}{ch}</span></div>')
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:24pt">{ch}</span> · '
                f'after a letter <span class="ntd" style="font-size:24pt">{JOIN}{ch}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def K(ch, name, name_tr, sound, word, tr, meaning, pic, joins=True, note=None, args=None, only_final=False, extra=None):
    phon = forms(ch, joins, only_final) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


S_SAME = "Sounds the same as {}; it is used mostly in words from Arabic and Persian."

LETTERS = [
    K("ا", "اَلِف", "alif", "‘a’ or ‘aa’ — a long ‘aa’ as in “father” inside a word", "آب", "aab", "water", "water", joins=False,
      extra="With a little wave on top, <span class='nt'>آ</span> says a long ‘aa’ at the start of a word."),
    K("ب", "بے", "be", "‘b’ as in “ball”", "بادام", "baadaam", "almonds", "almond", extra="One dot below."),
    K("پ", "پے", "pe", "‘p’ as in “pen”", "پوش", "posh", "flower", "flower", extra="Three dots below."),
    K("ت", "تے", "te", "a soft ‘t’ — tongue touches the back of the teeth", "تارُکھ", "taarukh", "star", "star", extra="Two dots above."),
    K("ٹ", "ٹے", "ṭe", "a hard ‘t’ — curl your tongue back, as in “top”", "ٹماٹر", "ṭamaaṭar", "tomato", "tomato",
      extra="A little ‘ṭ’ sign on top."),
    K("ث", "ثے", "se", "‘s’ as in “sun”", "ثَمَر", "samar", "fruit", "basket", extra=S_SAME.format("<span class='nt'>س</span>")),
    K("ج", "جیٖم", "jeem", "‘j’ as in “jam”", "جہاز", "jahaaz", "ship", "ship"),
    K("چ", "چے", "che", "‘ch’ as in “chair”", "چَشمہٕ", "chashma", "spring of water", "dew"),
    K("ح", "حے", "he", "‘h’ as in “hat”", "حج", "hajj", "Hajj, the journey to the Kaaba in Makkah", "kaaba"),
    K("خ", "خے", "khe", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "خط", "khat",
      "letter (that you post)", "envelope"),
    K("د", "دال", "daal", "a soft ‘d’ — tongue touches the back of the teeth", "دان", "daan", "pomegranate", "pomegranate", joins=False),
    K("ڈ", "ڈال", "ḍaal", "a hard ‘d’ — curl your tongue back, as in “dog”", "ڈَبہٕ", "ḍabba", "box", "box", joins=False),
    K("ذ", "ذال", "zaal", "‘z’ as in “zoo”", "ذِکر", "zikr", "dhikr — remembering Allah", "tasbih", joins=False,
      extra=S_SAME.format("<span class='nt'>ز</span>")),
    K("ر", "رے", "re", "a tapped ‘r’ — flick the tongue once", "روٗد", "rood", "rain", "raincloud", joins=False),
    K("ز", "زے", "ze", "‘z’ as in “zoo”", "زوٗن", "zoon", "moon", "moon", joins=False),
    K("ژ", "ژے", "tse", "‘ts’ as in “cats” — in Kashmiri this letter is <b>not</b> ‘zh’!", "ژوٗنٹھ", "tsoonṭh", "apple", "apple",
      joins=False, extra="Three dots on <span class='nt'>ز</span>. In Urdu and Persian it says ‘zh’, but in Kashmiri it says ‘ts’."),
    K("س", "سیٖن", "seen", "‘s’ as in “sun”", "سِرؠ", "siry", "sun", "sun",
      note="Look at the end of <span class='nt'>سِرؠ</span>: the special Kashmiri <span class='nt'>ؠ</span> adds a tiny ‘y’ breath."),
    K("ش", "شیٖن", "sheen", "‘sh’ as in “shoe”", "شیٖن", "sheen", "snow", "ks_snow",
      note="The letter’s name and the word for snow sound the same!"),
    K("ص", "صاد", "su’aad", "‘s’ as in “sun”", "صابَن", "saaban", "soap", "soap", extra=S_SAME.format("<span class='nt'>س</span>")),
    K("ض", "ضاد", "zu’aad", "‘z’ as in “zoo”", "ضیا", "ziyaa", "light", "bulb", extra=S_SAME.format("<span class='nt'>ز</span>")),
    K("ط", "طوے", "to’e", "a soft ‘t’, like <span class='nt'>ت</span>", "طَشت", "tasht", "washing basin (with its jug)", "ewer",
      extra=S_SAME.format("<span class='nt'>ت</span>")),
    K("ظ", "ظوے", "zo’e", "‘z’ as in “zoo”", "ظَرف", "zarf", "container, jar", "jar", extra=S_SAME.format("<span class='nt'>ز</span>")),
    K("ع", "عین", "ain", "in Kashmiri, just the vowel next to it — in Arabic, a sound from deep in the throat", "عینَک", "ainak",
      "glasses", "glasses"),
    K("غ", "غین", "ghain", "a soft gargled ‘gh’ from the back of the throat", "غُبارہٕ", "ghubaara", "balloon", "balloon"),
    K("ف", "فے", "fe", "‘f’ as in “fan”", "فانوس", "faanoos", "lantern", "eid"),
    K("ق", "قاف", "qaaf", "a ‘k’ said far back in the throat", "قَلَم", "qalam", "pen", "pen"),
    K("ک", "کاف", "kaaf", "‘k’ as in “kite”", "کانگٕر", "kaangir", "kangri — a little clay fire-pot in a wicker basket",
      "ks_kangri", extra="Families in Kashmir keep warm with a kangri in the snowy winter."),
    K("گ", "گاف", "gaaf", "‘g’ as in “go”", "گُلاب", "gulaab", "rose", "ks_rose"),
    K("ل", "لام", "laam", "‘l’ as in “lamp”", "لالہٕ", "laala", "tulip", "ks_tulip"),
    K("م", "میٖم", "meem", "‘m’ as in “moon”", "مَشیٖد", "masheed", "mosque", "mosque"),
    K("ن", "نوٗن", "noon", "‘n’ as in “net”", "نوٗن", "noon", "salt", "salt", args=dict(label="نوٗن"),
      note="Salt is used to make <i>noon chai</i>, Kashmir’s pink salty tea."),
    K("و", "واو", "vaav", "‘v’ as in “van”, or the vowels ‘oo’ and ‘o’", "وَن", "van", "forest", "tree", joins=False),
    K("ہ", "ہے", "he", "‘h’ as in “hat”", "ہیٚر", "her", "stairs, ladder", "ladder"),
    K("ھ", "دو چشمی ہے", "do-chashmi he", "adds a puff of breath to the letter before it: ٹ + ھ = ٹھ ‘ṭh’", "ٹھوٗل", "ṭhool",
      "egg", "egg", note='Find <span class="nt">ھ</span> in <span class="nt">ٹھوٗل</span> — it never starts a word.',
      extra="Its name means “two-eyed he”."),
    K("ء", "ہَمزہ", "hamza", "a tiny break in the voice between two vowels", "آئینہٕ", "aa’ina", "mirror", "mirror", joins=False,
      note='Find the <span class="nt">ء</span> sitting on its seat in <span class="nt">آئینہٕ</span>. Small hamza marks are also used as Kashmiri vowel signs.'),
    K("ی", "یے", "ye", "‘y’ as in “yes”, or the long vowel ‘ee’", "یٔمبرزَل", "yambarzal", "narcissus flower", "lily"),
    K("ے", "بوٚڈ یے", "boḍ ye", "‘e’ as in “they” — only at the end of a word", "چاے", "chaay", "tea", "teacup", only_final=True,
      note='Look for <span class="nt">ے</span> at the end of <span class="nt">چاے</span>!'),
]

N = len(LETTERS)

def _vrow(ex, txt):
    return (f'<tr><td class="ntd" style="font-size:20pt;width:1.0in;text-align:center;line-height:1.7">{ex}</td>'
            f'<td style="padding-left:6px">{txt}</td></tr>')


VOWELS_HTML = ("""<div class="box" style="margin:0.08in 0"><h3>Kashmiri vowel marks</h3>Kashmiri has more vowel sounds than Urdu, so it
uses some <b>extra little marks</b> above and below the letters. Books for grown-ups often leave them out; children’s books keep them.
<table style="width:100%;border-collapse:collapse;margin-top:2px;font-size:11.5pt"><tr><td style="width:50%;vertical-align:top"><table>"""
    + _vrow("بَ", "<b>zabar</b> (line above): short ‘a’ as in “cup”")
    + _vrow("بِ", "<b>zer</b> (line below): short ‘i’ as in “sit”")
    + _vrow("بُ", "<b>pesh</b> (curl above): short ‘u’ as in “put”")
    + _vrow("بٕ", "<b>hamza below</b>: a short sound between ‘i’ and ‘u’")
    + _vrow("بٔ", "<b>hamza above</b>: a short ‘uh’")
    + """</table></td><td style="width:50%;vertical-align:top"><table>"""
    + _vrow("کٲشُر", "<b>ٲ</b> alif with a wavy hamza: a long, deep ‘uh’, as in <i>koshur</i> (Kashmiri)")
    + _vrow("زوٗن", "<b>وٗ</b>: long ‘oo’, as in <i>zoon</i> (moon)")
    + _vrow("شیٖن", "<b>یٖ</b>: long ‘ee’, as in <i>sheen</i> (snow)")
    + _vrow("ۄ &nbsp; ێ", "<b>ۄ</b> (ring): ‘o’ as in “hot” · <b>ێ</b> (little v): ‘e’ as in “bed”")
    + _vrow("سِرؠ", "<b>ؠ</b> at the end of a word: a tiny ‘y’ breath, as in <i>siry</i> (sun)")
    + "</table></td></tr></table></div>")

INTRO = f"""<p>Kashmiri is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them and change shape a little.
Each letter page shows the shapes at the start, middle and end of a word.
<div class="ntd" style="font-size:22pt;text-align:center;direction:rtl;line-height:1.7">ب + ا + د + ا + م = <span class="nt">بادام</span>
<span style="font-family:Nunito;font-size:12pt;font-weight:400;direction:ltr;unicode-bidi:isolate"> &nbsp;<i>baadaam</i> (almonds)</span></div></div>
{VOWELS_HTML}
<div class="box"><h3>Ten letters never join forward</h3><span class="ntd" style="font-size:18pt;word-spacing:0.12in">ا د ڈ ذ ر ز ژ و ء</span> (and the final
<span class="nt">ے</span>) join to the letter <i>before</i> them, but never to the one after.</div>"""

FONTS = (fontset("Noto Sans Arabic", "noto-sans-arabic-arabic", "Noto Nastaliq Urdu", "noto-nastaliq-urdu-arabic"))

LANG = build(dict(
    code="ks", folder="book-18-kashmiri", series_no=18, isbn="", dir="rtl", draft=True,
    name="Kashmiri", native="کٲشُر", native_tr="koshur", name_word="ناو", write_word="لیٚکھِو",
    title_native="کٲشُر اَلِف بے", title_letters="ابپتژس", belongs_native="یہ کِتاب چھےٚ میٲنؠ", belongs_pic="ks_tulip",
    alphabet_native="اَلِف بے", numbers_native="گَنزرٕ", numbers_tr="ganzir", phrases_native="گۄڈنِکؠ لَفظ",
    fonts=FONTS, disp_family="Noto Sans Arabic", text_family="Noto Nastaliq Urdu",
    glyph_font=["baloo-bhaijaan-2-arabic-800-normal.woff2", "noto-sans-arabic-arabic-800-normal.woff2"],
    font_credit="Baloo Bhaijaan 2, Noto Sans Arabic, Noto Nastaliq Urdu",
    extra_css=(".nt{line-height:2.0} .lp-name{font-size:19pt;line-height:2.1} .lp-word .w{font-size:34pt;line-height:1.7} "),
    phon_feature="each letter’s <b>joined shapes</b> and the special <b>Kashmiri vowel marks</b>",
    sections=[section(LETTERS, label="LETTER", chip="THE LETTERS", title="The Kashmiri Letters", native="اَلِف بے",
                      native_tr="alif be — “the A-B-C”", chart_title="letters", chart_cols=7, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Kashmiri is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>A dot under t and d</b> (<i>ṭ, ḍ</i>) means a <i>hard</i> sound with the tongue curled back; without the dot the "
        "tongue touches the back of the top teeth.",
        "<b>ts</b> is one sound, as at the end of “cats”: Kashmiri writes it with <span class='nt'>ژ</span>.",
        "<b>Some letters sound the same</b> (<span class='nt'>ث س ص</span> all say <i>s</i>; <span class='nt'>ذ ز ض ظ</span> all say <i>z</i>). "
        "They keep their Arabic spelling, which helps when children later read the Qur’an.",
        "Kashmiri has a few vowels English does not have. The guides use the nearest English sound — listen to a Kashmiri speaker if you can."],
    phon_explain="Because Kashmiri letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked). The extra Kashmiri "
                 "vowel marks are explained on the page before the letters.",
    standard="Kashmiri as spoken in the Kashmir Valley",
    hello=[
        ("Who speaks it?", "About <b>7 million people</b> speak Kashmiri.<sup>³</sup> Its own name for itself is "
                           "<span class='nt'>کٲشُر</span> <i>koshur</i>."),
        ("Where?", "In the <b>Kashmir Valley</b> and nearby valleys, high in the <b>Himalaya mountains</b>, around the city of "
                   "<b>Srinagar</b>. Kashmiri families also live in many other places."),
        ("How is it written?", "From <b>right to left</b>, in a Perso-Arabic script, usually in the flowing <b>Nastaliq</b> style. "
                               "Some people also write it in Devanagari."),
        ("How many letters?", f"This book teaches <b>{N} letters</b>, plus the special <b>vowel marks</b> that make Kashmiri "
                              "different from Urdu and Persian (<span class='nt'>ٲ ۄ ێ ؠ</span>)."),
        ("A land of flowers", "Kashmir is famous for its <b>tulips</b>, its tall <b>chinar trees</b>, its almonds and apples, "
                              "and its lakes and snowy mountains."),
        ("Warm in winter", "In the cold winter, people carry a <span class='nt'>کانگٕر</span> <i>kaangir</i>, a little clay "
                           "pot of warm embers in a wicker basket, and drink salty pink <i>noon chai</i>."),
    ],
    hello_pics=[("ks_tulip", {}), ("ks_snow", {}), ("apple", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[63.0, 15.0], [87.0, 39.0]],
                   points=dict(srinagar=[74.80, 34.08]),
                   area=(74.9, 34.0, 74, 46), area_rot=-25,
                   cities=[("srinagar", "Srinagar", 84, 8, "start", False)],
                   label="HIMALAYA", label_at=[80.5, 31.0], marker=[75.0, 34.0],
                   caption="The circle shows the Kashmir Valley on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b> · the high snowy mountains <b>white</b>. "
                          "<b>Find it:</b> the dashed line goes around the Kashmir Valley, where Kashmiri is spoken. "
                          "Srinagar is its biggest city, beside Dal Lake.",
                   seas=[("Arabian Sea", 66.5, 18.0)]),
    digits=[("۰", "صِفر", "sifar", "zero"), ("۱", "اَکھ", "akh", "one"), ("۲", "زٕ", "zi", "two"), ("۳", "ترٕ", "tri", "three"),
            ("۴", "ژور", "tsor", "four"), ("۵", "پانٛژ", "paants", "five"), ("۶", "شےٚ", "sheh", "six"),
            ("۷", "سَتھ", "sath", "seven"), ("۸", "ٲٹھ", "aaṭh", "eight"), ("۹", "نَو", "nav", "nine")],
    phrases=[("السلام علیکم", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("وعلیکم السلام", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("میون ناو چھُ …", "myon naav chhu …", "My name is …"),
             ("شُکریہ", "shukriya", "Thank you"),
             ("جزاک اللہ خیراً", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("مٲج · مول", "moj · mol", "Mother · Father"),
             ("بوے · بێنہِ", "boy · beni", "Brother · Sister"),
             ("آ · نَہ", "aa · na", "Yes · No"),
             ("بہٕ چھُس کٲشُر ہیچھان!", "bi chhus koshur hechhaan!", "I am learning Kashmiri! (a girl says: bi chhes … hechhaan)")],
    cheer=("ماشاءاللہ! شاباش!", "maashaa-allaah! shaabaash!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="ا ب پ", right="ت ٹ ث"),
    review_note=("Kashmiri is drafted from limited sources and needs a careful native check: (1) the exact letter list and order "
                 "(ڑ was left out because Kashmiri does not use it natively; ں is not shown); (2) letter names; (3) the vowel-mark table on "
                 "the intro page (which mark = which sound); (4) the spellings with marks: تارُکھ, چَشمہٕ, ڈَبہٕ, روٗد, ژوٗنٹھ, سِرؠ, شیٖن, "
                 "کانگٕر, لالہٕ, مَشیٖد, ہیٚر, ٹھوٗل, آئینہٕ, یٔمبرزَل, چاے; (5) whether دان (pomegranate), ہیٚر (stairs), ثَمَر, ضیا, غُبارہٕ, "
                 "طَشت are natural Kashmiri words for children; (6) numbers, especially شےٚ (6) and ٲٹھ (8); (7) the phrases "
                 "(بوے · بێنہِ, آ · نَہ, the 'I am learning' sentence) and the titles کٲشُر اَلِف بے, گَنزرٕ, گۄڈنِکؠ لَفظ, لیٚکھِو, "
                 "یہ کِتاب چھےٚ میٲنؠ."),
    tiles="ابپتژک", cover_pics=["ks_tulip", "apple", "ks_kangri", "mosque"], title_size=48,
    speakers_blurb="Kashmiri is spoken by about 7 million people in the Kashmir Valley, high in the Himalaya mountains.",
    sample_words=[("زوٗن", "zoon", "moon"), ("پوش", "posh", "flower"), ("ژوٗنٹھ", "tsoonṭh", "apple")],
    keywords=["kashmiri alphabet book for kids", "learn kashmiri for children", "koshur letters tracing workbook",
              "kashmiri coloring book", "muslim kids activity book", "islamic coloring book for children",
              "kashmiri heritage language gift"],
))
