# -*- coding: utf-8 -*-
"""Book 32 - Hebrew (Hebrew script, 22 letters, right-to-left). Allamahul Bayan Series. REVIEW DRAFT.
House rules: objects/plants/nature only; script + transliteration + English; neutral, non-political facts.
The 5 final (end-of-word) forms are taught in the section intro and on their letters' pages.
"""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Shapes and sounds"


def _shapes(shapes):
    cells = "".join(f'<span style="display:inline-block;text-align:center;margin:0 7px 2px;vertical-align:top">'
                    f'<span class="nt" style="font-size:25pt;line-height:1.35">{g}</span><br>'
                    f'<span class="small" style="direction:ltr;unicode-bidi:isolate">{c}</span></span>' for g, c in shapes)
    return f'<div style="direction:rtl;text-align:right">{cells}</div>'


def H(lt, name, name_tr, sound, word, tr, meaning, pic, shapes=None, extra=None, note=None, args=None):
    phon = _shapes(shapes or [(lt, "printed letter")])
    if extra:
        phon += f'<div class="small" style="margin-top:3px">{extra}</div>'
    return letter(lt, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    H("א", "אָלֶף", "A-lef", "silent! Alef carries a vowel: here the ‘a’ of “a-va-TI-akh”", "אֲבַטִּיחַ", "a-va-TI-akh", "watermelon", "watermelon",
      extra="Alef has no sound of its own: it holds the vowel that comes with it."),
    H("ב", "בֵּית", "bet", "‘b’ as in “ball” (with a dot inside); ‘v’ as in “van” (without the dot)", "בַּיִת", "BA-yit", "house", "house",
      shapes=[("בּ", "b"), ("ב", "v")], extra="The little dot inside changes the sound. Look-alike: כ (kaf) is rounder."),
    H("ג", "גִּימֶל", "GI-mel", "‘g’ as in “go”", "גֶּזֶר", "GE-zer", "carrot", "carrot",
      shapes=[("ג", "g"), ("ג׳", "j")], extra="With a little mark ׳ after it, ג says ‘j’ in borrowed words."),
    H("ד", "דָּלֶת", "DA-let", "‘d’ as in “door”", "דֶּלֶת", "DE-let", "door", "door",
      extra="Fun fact: the letter’s name and the word for “door” sound almost the same! Look-alike: ר (resh) is round, ד has a sharp corner."),
    H("ה", "הֵא", "hey", "‘h’ as in “hat” (often silent at the end of a word)", "הַר", "har", "mountain", "mountain",
      extra="Look-alikes: ח and ת. ה has a little gap at the top left."),
    H("ו", "וָו", "vav", "‘v’ as in “van”; it also writes the vowels ‘o’ and ‘u’", "וֶרֶד", "VE-red", "rose", "flower",
      shapes=[("ו", "v"), ("וֹ", "o"), ("וּ", "u")], extra="Vav means “hook” — and it looks like one!"),
    H("ז", "זַיִן", "ZA-yin", "‘z’ as in “zoo”", "זַיִת", "ZA-yit", "olive", "olive",
      shapes=[("ז", "z"), ("ז׳", "zh")], extra="With the mark ׳ it says ‘zh’, like the ‘s’ in “measure”."),
    H("ח", "חֵית", "khet", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "חַלּוֹן", "kha-LON", "window", "window",
      extra="Look-alikes: ה (gap at the top) and ת (a little foot)."),
    H("ט", "טֵית", "tet", "‘t’ as in “top”", "טַבַּעַת", "ta-BA-at", "ring", "ring",
      extra="ט and ת (tav) sound the same in modern Hebrew."),
    H("י", "יוֹד", "yod", "‘y’ as in “yes”; it also helps write the vowel ‘ee’", "יָם", "yam", "sea", "waves",
      extra="The smallest letter! It hangs in the air, like a tiny raindrop."),
    H("כ", "כַּף", "kaf", "‘k’ as in “kite” (with a dot); ‘kh’ as in “loch” (without the dot)", "כַּדּוּר", "ka-DUR", "ball", "ball",
      shapes=[("כּ", "k"), ("כ", "kh"), ("ך", "end form")], extra="At the end of a word kaf stretches down: ך."),
    H("ל", "לָמֶד", "LA-med", "‘l’ as in “lamp”", "לִימוֹן", "li-MON", "lemon", "lemon",
      extra="The tallest letter: it reaches up above the line."),
    H("מ", "מֵם", "mem", "‘m’ as in “moon”", "מִטְרִיָּה", "mit-ri-YA", "umbrella", "umbrella",
      shapes=[("מ", "m"), ("ם", "end form")], extra="At the end of a word mem closes into a box: ם."),
    H("נ", "נוּן", "nun", "‘n’ as in “net”", "נוֹצָה", "no-TSA", "feather", "feather",
      shapes=[("נ", "n"), ("ן", "end form")], extra="At the end of a word nun grows a long leg: ן."),
    H("ס", "סָמֶךְ", "SA-mekh", "‘s’ as in “sun”", "סֻלָּם", "su-LAM", "ladder", "ladder",
      extra="Look-alike: final mem ם is square; samekh ס is round."),
    H("ע", "עַיִן", "A-yin", "in everyday Hebrew usually silent, like alef — it holds a vowel", "עָנָן", "a-NAN", "cloud", "clouds",
      extra="Some speakers say it deep in the throat, like Arabic ع."),
    H("פ", "פֵּא", "pey", "‘p’ as in “pen” (with a dot); ‘f’ as in “fan” (without the dot)", "פָּנָס", "pa-NAS", "lantern", "eid",
      shapes=[("פּ", "p"), ("פ", "f"), ("ף", "end form")], extra="At the end of a word it is written ף and says ‘f’."),
    H("צ", "צָדִי", "TSA-di", "‘ts’ as in “cats”", "צַלַּחַת", "tsa-LA-khat", "plate", "plate",
      shapes=[("צ", "ts"), ("ץ", "end form"), ("צ׳", "ch")], extra="With the mark ׳ it says ‘ch’ as in “chair”."),
    H("ק", "קוֹף", "kof", "‘k’ as in “kite”", "קֶשֶׁת", "KE-shet", "rainbow", "rainbow",
      extra="Sounds like כּ (kaf with a dot). Its leg hangs below the line."),
    H("ר", "רֵישׁ", "resh", "a soft ‘r’ made at the back of the throat", "רִמּוֹן", "ri-MON", "pomegranate", "pomegranate",
      extra="Round corner — compare ד (dalet), which has a sharp one."),
    H("ש", "שִׁין", "shin", "‘sh’ as in “shoe” (dot on the right); ‘s’ (dot on the left)", "שֶׁמֶשׁ", "SHE-mesh", "sun", "sun",
      shapes=[("שׁ", "sh"), ("שׂ", "s")], extra="With the dot on the left it is called <i>sin</i>."),
    H("ת", "תָּו", "tav", "‘t’ as in “top”", "תַּפּוּחַ", "ta-PU-akh", "apple", "apple",
      extra="The last letter of the alef-bet. ת and ט (tet) sound the same."),
]

INTRO = """<p>Hebrew is written <b>from right to left</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters stand apart</h3>Hebrew letters <b>do not join</b> — each letter keeps its own shape,
like printed blocks. All 22 letters are <b>consonants</b>.</div>
<div class="box" style="margin:0.08in 0"><h3>Five letters change at the end of a word</h3>Five letters have a special <b>end form</b>
(<i>sofit</i>). It is the same sound, just a different shape:
<div style="display:flex;justify-content:space-around;direction:rtl;margin:0.05in 0"><div style="text-align:center"><span class="nt" style="font-size:26pt;line-height:1.5">כ ← ך</span><br><span class="small">kaf</span></div><div style="text-align:center"><span class="nt" style="font-size:26pt;line-height:1.5">מ ← ם</span><br><span class="small">mem</span></div><div style="text-align:center"><span class="nt" style="font-size:26pt;line-height:1.5">נ ← ן</span><br><span class="small">nun</span></div><div style="text-align:center"><span class="nt" style="font-size:26pt;line-height:1.5">פ ← ף</span><br><span class="small">pey</span></div><div style="text-align:center"><span class="nt" style="font-size:26pt;line-height:1.5">צ ← ץ</span><br><span class="small">tsadi</span></div></div>
Most of them stretch a long leg <b>below the line</b>. Look for them on their letter pages!</div>
<div class="box" style="margin:0.08in 0"><h3>A dot can change the sound</h3>
<span class="nt" style="font-size:22pt">בּ</span> b / <span class="nt" style="font-size:22pt">ב</span> v ·
<span class="nt" style="font-size:22pt">כּ</span> k / <span class="nt" style="font-size:22pt">כ</span> kh ·
<span class="nt" style="font-size:22pt">פּ</span> p / <span class="nt" style="font-size:22pt">פ</span> f ·
<span class="nt" style="font-size:22pt">שׁ</span> sh / <span class="nt" style="font-size:22pt">שׂ</span> s</div>
<div class="box"><h3>Vowels are dots and lines</h3>Small marks under and above the letters (<i>niqqud</i>) show the vowels:
<span class="nt" style="font-size:20pt">בַּ</span> ba · <span class="nt" style="font-size:20pt">בֶּ</span> be · <span class="nt" style="font-size:20pt">בִּ</span> bi ·
<span class="nt" style="font-size:20pt">בֹּ</span> bo · <span class="nt" style="font-size:20pt">בֻּ</span> bu.
Children’s books use them; grown-ups usually leave them out. The words in this book have them.</div>"""

LANG = build(dict(
    code="he", folder="book-32-hebrew", series_no=32, isbn="", draft=True, dir="rtl",
    name="Hebrew", native="עִבְרִית", native_tr="iv-RIT", name_word="שֵׁם", write_word="כִּתְבוּ",
    title_native="הָאָלֶף־בֵּית הָרִאשׁוֹן שֶׁלִּי", title_letters="אבגדהו", belongs_native="הַסֵּפֶר הַזֶּה שֶׁלִּי",
    belongs_pic="star", alphabet_native="הָאָלֶף־בֵּית", numbers_native="מִסְפָּרִים", numbers_tr="mis-pa-RIM",
    phrases_native="מִלִּים רִאשׁוֹנוֹת",
    fonts=fontset("Rubik", "rubik-hebrew", "Noto Sans Hebrew", "noto-sans-hebrew-hebrew"),
    disp_family="Rubik", text_family="Noto Sans Hebrew",
    glyph_font=["rubik-hebrew-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Rubik, Noto Sans Hebrew, Baloo 2",
    extra_css=".nt{line-height:1.5} .lp-name{font-size:24pt;line-height:1.5} .lp-word .w{font-size:40pt;line-height:1.5}",
    phon_feature="each letter’s Hebrew name, its sounds and its end-of-word shape",
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book. "
               "Five letters have an <b>end form</b> for the last letter of a word: "
               "<span class='nt' style='font-size:16pt'>ך ם ן ף ץ</span> (kaf, mem, nun, pey, tsadi).",
    sections=[section(LETTERS, native="הָאוֹתִיּוֹת", native_tr="ha-o-ti-YOT — “the letters”",
                      chart_cols=6, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Hebrew is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>CAPITALS</b> show the stressed part of the word: <i>BA-yit</i> means “say BA a little louder”. Many Hebrew words "
        "are stressed on the <b>last</b> part: <i>kha-LON</i>, <i>ri-MON</i>.",
        "<b>Vowels are short and pure:</b> <i>a</i> as in “father”, <i>e</i> as in “bed”, <i>i</i> as in “ski”, <i>o</i> as in “more”, "
        "<i>u</i> as in “put”.",
        "<b>kh</b> is a scratchy sound from the back of the throat, as in Scottish “loch” or Arabic <span class='ar'>خ</span>.",
        "<b>r</b> is soft and made at the back of the throat, a little like a gargle."],
    phon_explain="The third box shows the letter’s <b>different shapes and sounds</b>: a dot that changes the sound "
                 "(<span class='nt'>בּ</span> b / <span class='nt'>ב</span> v), its special <b>end-of-word</b> shape, or a look-alike letter to watch out for.",
    standard="everyday modern Hebrew",
    hello=[
        ("Who speaks it?", "About <b>9 million people</b> speak Hebrew, as a first or second language.<sup>³</sup>"),
        ("Where?", "Hebrew is spoken mainly in <b>Israel</b>, on the eastern coast of the Mediterranean Sea, and by "
                   "families and communities in many other countries."),
        ("How is it written?", "From <b>right to left</b>, in the Hebrew alphabet. The letters <b>do not join</b>, and five of them "
                               "have a special shape at the end of a word."),
        ("How many letters?", "<b>22 letters</b>, all of them consonants. Vowels are small dots and lines added under and above the letters."),
        ("Cousins: Hebrew and Arabic", "Both belong to the same family of languages, so many words are alike: "
                                       "<span class='nt'>שָׁלוֹם</span> <i>shalom</i> and <span class='ar'>سلام</span> <i>salaam</i> (peace); "
                                       "<span class='nt'>שֶׁמֶשׁ</span> <i>shemesh</i> and <span class='ar'>شمس</span> <i>shams</i> (sun)."),
        ("Did you know?", "The name <i>alef-bet</i> comes from the first two letters, <span class='nt'>א</span> alef and "
                          "<span class='nt'>ב</span> bet — just like Arabic <i>alif, baa’</i> and English “alphabet”."),
    ],
    hello_pics=[("sun", {}), ("pomegranate", {}), ("olive", {})],
    map=region_map(frame=[[29.8, 27.6], [40.2, 37.2]],
                   points=dict(telaviv=[34.78, 32.08], haifa=[34.99, 32.79], beersheva=[34.79, 31.25], eilat=[34.95, 29.56]),
                   area=None,
                   cities=[("haifa", "Haifa", 14, 8, "start", False), ("telaviv", "Tel Aviv", -14, 8, "end", False),
                           ("beersheva", "Be’er Sheva", 14, 8, "start", False), ("eilat", "Eilat", 14, 8, "start", False)],
                   label="THE LEVANT", label_at=[37.6, 34.6], marker=[35.0, 31.5],
                   caption="The circle shows the eastern Mediterranean on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Hebrew is spoken in cities such as "
                          "Haifa, Tel Aviv, Be’er Sheva and Eilat, on the eastern shore of the Mediterranean Sea.",
                   seas=[("Mediterranean Sea", 32.2, 33.6)], world_r=10),
    digits=[("0", "אֶפֶס", "E-fes", "zero"), ("1", "אַחַת", "a-KHAT", "one"), ("2", "שְׁתַּיִם", "SHTA-yim", "two"),
            ("3", "שָׁלוֹשׁ", "sha-LOSH", "three"), ("4", "אַרְבַּע", "AR-ba", "four"), ("5", "חָמֵשׁ", "kha-MESH", "five"),
            ("6", "שֵׁשׁ", "shesh", "six"), ("7", "שֶׁבַע", "SHE-va", "seven"), ("8", "שְׁמוֹנֶה", "shmo-NE", "eight"),
            ("9", "תֵּשַׁע", "TE-sha", "nine")],
    phrases=[("אסלאמו עליכום", "as-sa-LAA-mu a-LAY-kum", "Peace be upon you (the Muslim greeting)"),
             ("ועליכום אסלאם", "wa a-LAY-kum as-sa-LAAM", "And upon you be peace (the reply)"),
             ("קוֹרְאִים לִי …", "kor-IM li …", "My name is …"),
             ("תּוֹדָה", "to-DA", "Thank you"),
             ("ג׳זאכאללהו ח׳יראן", "ja-ZAA-kal-laa-hu KHAY-ran", "May Allah reward you with good"),
             ("אִמָּא · אַבָּא", "I-ma · A-ba", "Mother · Father"),
             ("אָח · אָחוֹת", "akh · a-KHOT", "Brother · Sister"),
             ("כֵּן · לֹא", "ken · lo", "Yes · No"),
             ("אֲנִי לוֹמֵד עִבְרִית!", "a-NI lo-MED iv-RIT!", "I am learning Hebrew! (a girl says: lo-ME-det)")],
    cheer=("מאשאללה! כָּל הַכָּבוֹד!", "maa-shaa-AL-lah! kol ha-ka-VOD!", "Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="א ב ג", right="ד ה ו"),
    review_note="Check every pointed spelling (niqqud), the stress marks in the transliterations, and the Arabic phrases written in "
                "Hebrew letters (as-salaamu alaikum, jazakallahu khairan): the spellings אסלאמו עליכום / ג׳זאכאללהו ח׳יראן are "
                "phonetic guesses. Confirm פָּנָס (lantern) is shown well by the lantern picture.",
    tiles="אבגדהו", cover_pics=["pomegranate", "sun", "olive", "umbrella"], title_size=48,
    speakers_blurb="Hebrew is spoken by about 9 million people, mainly on the eastern shore of the Mediterranean and in communities around the world.",
    sample_words=[("שֶׁמֶשׁ", "SHE-mesh", "sun"), ("רִמּוֹן", "ri-MON", "pomegranate"), ("בַּיִת", "BA-yit", "house")],
    keywords=["hebrew alphabet book for kids", "learn hebrew letters for children", "alef bet coloring book",
              "hebrew letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "semitic languages for kids"],
))
