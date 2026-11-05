# -*- coding: utf-8 -*-
"""Book 33 - Assyrian Neo-Aramaic (Sureth), Syriac script in the East Syriac (Madnhaya) style, 22 letters,
right-to-left, joined like Arabic. Allamahul Bayan Series. REVIEW DRAFT.
House rules: objects/plants/nature only; script + transliteration + English; neutral, non-religious facts.
Words are written without vowel points; the transliteration gives the vowels.
"""
from generic import build, letter, section, fontset
from maps import region_map

JOIN = "ـ"  # tatweel (U+0640) shows joined forms; Noto Sans Syriac Eastern has it
PH = "Letter shapes · how it joins"


def forms(lt, joins=True):
    if not joins:
        return (f'<div style="font-size:12pt">Alone <span class="ntd" style="font-size:26pt">{lt}</span> · '
                f'after a letter <span class="ntd" style="font-size:26pt">{JOIN}{lt}</span></div>'
                f'<div class="small">It never joins to the letter after it.</div>')
    return (f'<div class="ntd" style="font-size:26pt;line-height:1.5;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{lt}{JOIN}&nbsp;&nbsp;{JOIN}{lt}{JOIN}&nbsp;&nbsp;{JOIN}{lt}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def S(lt, name, name_tr, sound, word, tr, meaning, pic, joins=True, extra=None, note=None, args=None):
    phon = forms(lt, joins) + (f'<div class="small" style="margin-top:3px">{extra}</div>' if extra else "")
    return letter(lt, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


WAVY = "With a small wavy mark below it, {} says {}."

LETTERS = [
    S("ܐ", "ܐܠܦ", "AA-lap", "no sound of its own — it carries a vowel at the start of a word, here ‘i’", "ܐܝܠܢܐ", "i-LAA-na", "tree", "tree",
      joins=False, extra="At the end of a word it is the ‘a’ ending: ܐܝܠܢܐ i-LAA-<b>na</b>."),
    S("ܒ", "ܒܝܬ", "bet", "‘b’ as in “ball”; after a vowel it often softens to ‘w’", "ܒܝܬܐ", "BE-ta", "house", "house",
      extra="Find the soft ‘w’ in ܟܘܟܒܐ <i>KOKH-wa</i> (star)."),
    S("ܓ", "ܓܡܠ", "GAA-mal", "‘g’ as in “go”", "ܓܘܙܐ", "GO-za", "walnut", "walnut",
      extra=WAVY.format("<span class='nt'>ܓ̰</span>", "‘j’ as in “jam”")),
    S("ܕ", "ܕܠܬ", "DAA-lat", "‘d’ as in “dog”", "ܕܪܡܢܐ", "dar-MAA-na", "medicine", "medicine", joins=False,
      extra="One dot <b>below</b>. Resh ܪ has its dot above."),
    S("ܗ", "ܗܐ", "heh", "‘h’ as in “hat”", "ܗܘܐ", "HA-wa", "air, wind (that flies a kite)", "kite", joins=False),
    S("ܘ", "ܘܘ", "waw", "‘w’ as in “water”; it also writes the vowels ‘o’ and ‘oo’", "ܘܪܕܐ", "WAR-da", "flower", "flower", joins=False),
    S("ܙ", "ܙܝܢ", "zen", "‘z’ as in “zoo”", "ܙܝܬܐ", "ZE-ta", "olive", "olive", joins=False,
      extra=WAVY.format("<span class='nt'>ܙ̰</span>", "‘zh’, like the ‘s’ in “measure”")),
    S("ܚ", "ܚܝܬ", "khet", "a scratchy ‘kh’ from the back of the throat, as in Scottish “loch”", "ܚܒܘܫܐ", "kha-BOO-sha", "apple", "apple"),
    S("ܛ", "ܛܝܬ", "tet", "a heavy ‘t’, said with the tongue pressed low (like Arabic ط)", "ܛܘܪܐ", "TOO-ra", "mountain", "mountain"),
    S("ܝ", "ܝܘܕ", "yud", "‘y’ as in “yes”; it also writes the vowels ‘ee’ and ‘e’", "ܝܡܐ", "YAM-ma", "sea", "waves"),
    S("ܟ", "ܟܦ", "kap", "‘k’ as in “kite”; after a vowel it often softens to ‘kh’", "ܟܘܟܒܐ", "KOKH-wa", "star", "star",
      extra=WAVY.format("<span class='nt'>ܟ̰</span>", "‘ch’ as in “chair”")),
    S("ܠ", "ܠܡܕ", "LAA-mad", "‘l’ as in “lamp”", "ܠܚܡܐ", "LAKH-ma", "bread", "roti"),
    S("ܡ", "ܡܝܡ", "meem", "‘m’ as in “moon”", "ܡܝܐ", "MA-ya", "water", "water"),
    S("ܢ", "ܢܘܢ", "noon", "‘n’ as in “net”", "ܢܘܗܪܐ", "NOOH-ra", "light", "bulb",
      extra="At the end of a word nun drops down below the line."),
    S("ܣ", "ܣܡܟܬ", "SIM-kat", "‘s’ as in “sun”", "ܣܦܝܢܬܐ", "SPEEN-ta", "ship", "ship"),
    S("ܥ", "ܥܐ", "eh", "in Assyrian usually just the vowel next to it — in old Aramaic a deep throat sound, like Arabic ع",
      "ܥܢܒ̈ܐ", "IN-weh", "grapes", "grapes",
      extra="The two dots above the word (<i>siyame</i>) mean “more than one”."),
    S("ܦ", "ܦܐ", "peh", "‘p’ as in “pen”; after a vowel it can soften to ‘f’", "ܦܬܘܪܐ", "pa-TO-ra", "table", "syr_table"),
    S("ܨ", "ܨܕܐ", "SAA-deh", "a heavy ‘s’, said with the tongue pressed low (like Arabic ص)", "ܨܦܪܐ", "SAP-ra", "morning", "sunrise",
      joins=False),
    S("ܩ", "ܩܘܦ", "qop", "a ‘k’ said far back in the throat (like Arabic ق)", "ܩܫܬܐ", "QESH-ta", "rainbow", "rainbow"),
    S("ܪ", "ܪܝܫ", "reesh", "a rolled ‘r’ — flick the tongue", "ܪܘܡܢܐ", "roo-MAA-na", "pomegranate", "pomegranate", joins=False,
      extra="One dot <b>above</b>. Dalat ܕ has its dot below."),
    S("ܫ", "ܫܝܢ", "sheen", "‘sh’ as in “shoe”", "ܫܡܫܐ", "SHIM-sha", "sun", "sun"),
    S("ܬ", "ܬܘ", "taw", "‘t’ as in “top”", "ܬܪܥܐ", "TAR-a", "door", "door", joins=False,
      extra="The last letter of the alphabet."),
]

INTRO = """<p>Assyrian is written <b>from right to left</b>, in the <b>Syriac alphabet</b>. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.08in 0"><h3>Letters hold hands</h3>Most letters <b>join</b> to the letter after them, and their shape changes
a little at the start, middle and end of a word. Each letter page shows the shapes.
<div class="ntd" style="font-size:28pt;text-align:center;direction:rtl;line-height:1.6">ܫ + ܡ + ܫ + ܐ = <span class="nt">ܫܡܫܐ</span></div>
<div style="text-align:center"><i>sh + m + sh + a = SHIM-sha</i> (sun)</div></div>
<div class="box" style="margin:0.08in 0"><h3>Eight letters never join forward</h3><span class="nt" style="font-size:20pt">ܐ ܕ ܗ ܘ ܙ ܨ ܪ ܬ</span>
join to the letter <i>before</i> them, but never to the one after. Look for the small note on their pages.</div>
<div class="box" style="margin:0.08in 0"><h3>Dots and marks</h3><span class="nt" style="font-size:20pt">ܕ</span> d and
<span class="nt" style="font-size:20pt">ܪ</span> r differ only in their dot: below or above. A small wavy mark under a letter makes a new sound:
<span class="nt" style="font-size:20pt">ܓ̰</span> j · <span class="nt" style="font-size:20pt">ܟ̰</span> ch · <span class="nt" style="font-size:20pt">ܙ̰</span> zh.</div>
<div class="box"><h3>Where are the vowels?</h3>Vowels can be written as small dots above and below the letters. Everyday writing often leaves them
out, so the words in this book are written without them — the English letters under each word tell you how to say it.</div>"""

LANG = build(dict(
    code="syr", folder="book-33-assyrian-neo-aramaic", series_no=33, isbn="", draft=True, dir="rtl",
    name="Assyrian", native="ܣܘܪܝܬ", native_tr="SOO-rit (Sureth)", name_word="ܫܡܐ", write_word="ܟܬܘܒ",
    title="My First Assyrian Alphabet",
    subtitle="A Coloring Book to Learn, Trace & Say the 22 Letters of Assyrian Neo-Aramaic (Sureth) with English Phonetics",
    title_native="ܐܠܦ ܒܝܬ ܩܕܡܝܐ ܕܝܠܝ", title_letters="ܐܒܓܕܗܘ", belongs_native="ܐܗܐ ܟܬܒܐ ܕܝܠܝ ܝܠܗ",
    belongs_pic="star", alphabet_native="ܐܠܦ ܒܝܬ", numbers_native="ܡܢܝܢܐ", numbers_tr="min-YAA-neh",
    phrases_native="ܡܠܐ̈ ܩܕܡܝܐ̈",
    fonts=fontset("Noto Sans Syriac Eastern", "noto-sans-syriac-eastern-syriac", "Noto Sans Syriac Eastern", "noto-sans-syriac-eastern-syriac")[:3],
    disp_family="Noto Sans Syriac Eastern", text_family="Noto Sans Syriac Eastern",
    glyph_font=["noto-sans-syriac-eastern-syriac-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Syriac Eastern, Baloo 2",
    extra_css=".nt{line-height:1.6} .lp-name{font-size:24pt;line-height:1.6} .lp-word .w{font-size:40pt;line-height:1.6}",
    phon_feature="each letter’s Assyrian name and its <b>joined shapes</b> (start · middle · end)",
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    sections=[section(LETTERS, native="ܐܬܘܬܐ", native_tr="at-WAA-teh — “the letters”",
                      chart_cols=6, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>Assyrian is read from right to left</b>, like the Qur’an. The tracing rows on each page also start on the right.",
        "<b>CAPITALS</b> show the stressed part of the word: <i>BE-ta</i> means “say BE a little louder”. Most Assyrian words are "
        "stressed on the <b>last-but-one</b> part.",
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”. "
        "<i>e</i> is as in “bed”, <i>o</i> as in “more”.",
        "<b>kh</b> is a scratchy throat sound, as in Scottish “loch” or Arabic <span class='ar'>خ</span>; <b>q</b> is a <i>k</i> said "
        "deep in the throat.",
        "Sounds follow the common modern spoken standard; families from different villages and towns may say some words a little differently."],
    phon_explain="Because Assyrian letters <b>change shape</b> when they join, the third box shows the letter at the start, "
                 "middle and end of a word (letters that never join to the next letter are marked).",
    standard="modern standard spoken Assyrian (Sureth)",
    hello=[
        ("Who speaks it?", "<b>Several hundred thousand people</b> speak Assyrian Neo-Aramaic. Its speakers call it "
                           "<span class='nt'>ܣܘܪܝܬ</span> <i>Sureth</i>.<sup>³</sup>"),
        ("Where?", "In villages and towns of northern <b>Iraq</b>, north-eastern <b>Syria</b>, north-western <b>Iran</b> and "
                   "south-eastern <b>Türkiye</b>, and by families around the world, from the USA to Sweden and Australia."),
        ("How is it written?", "From <b>right to left</b>, in the <b>Syriac alphabet</b>. Most letters <b>join</b> to the next one, "
                               "as in Arabic. This book uses the rounded <i>Eastern</i> style of the letters."),
        ("How many letters?", "<b>22 letters</b>, in the same order as the old Arabic order <i>abjad</i>: alif, baa’, jeem, daal…"),
        ("Cousins: Aramaic and Arabic", "Both belong to the same family of languages, so many words are alike: "
                                        "<span class='nt'>ܫܡܫܐ</span> <i>SHIM-sha</i> and <span class='ar'>شمس</span> <i>shams</i> (sun); "
                                        "<span class='nt'>ܡܝܐ</span> <i>MA-ya</i> and <span class='ar'>ماء</span> <i>maa’</i> (water)."),
        ("A very old language", "Aramaic has been spoken and written for about <b>3,000 years</b>. Long ago it was used for letters and "
                                "trade all across the Middle East."),
    ],
    hello_pics=[("sun", {}), ("pomegranate", {}), ("tree", {})],
    map=region_map(frame=[[31.5, 29.0], [52.0, 44.0]],
                   points=dict(duhok=[42.99, 36.87], erbil=[44.01, 36.19], urmia=[45.07, 37.55], qamishli=[41.23, 37.05],
                               baghdad=[44.37, 33.31]),
                   area=(43.2, 36.6, 190, 120),
                   cities=[("duhok", "Duhok", 0, -18, "middle", False), ("erbil", "Erbil", 14, 26, "start", False),
                           ("urmia", "Urmia", 14, 8, "start", False), ("qamishli", "Qamishli", -14, 8, "end", False),
                           ("baghdad", "Baghdad", 14, 8, "start", False)],
                   label="MESOPOTAMIA", label_at=[40.6, 32.2], marker=[43.5, 36.5],
                   caption="The circle shows the region on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> the dashed line shows the hills and "
                          "plains where many Assyrian villages are. The language is also spoken in cities such as Duhok, Erbil, Qamishli, "
                          "Urmia and Baghdad.",
                   seas=[("Mediterranean Sea", 33.4, 33.0), ("Caspian Sea", 50.6, 41.4)], world_r=12),
    digits=[("0", "ܣܝܦܪ", "SI-fir", "zero"), ("1", "ܚܕ", "kha", "one"), ("2", "ܬܪܝܢ", "treh", "two"),
            ("3", "ܬܠܬܐ", "TLAA-ha", "three"), ("4", "ܐܪܒܥܐ", "AR-ba", "four"), ("5", "ܚܡܫܐ", "KHAM-sha", "five"),
            ("6", "ܫܬܐ", "ISH-ta", "six"), ("7", "ܫܒܥܐ", "SHO-a", "seven"), ("8", "ܬܡܢܝܐ", "TMAN-ya", "eight"),
            ("9", "ܬܫܥܐ", "ICH-a", "nine")],
    phrases=[("ܐܣܠܐܡܘ ܥܠܝܟܘܡ", "as-sa-LAA-mu a-LAY-kum", "Peace be upon you (the Muslim greeting)"),
             ("ܘܥܠܝܟܘܡ ܐܣܠܐܡ", "wa a-LAY-kum as-sa-LAAM", "And upon you be peace (the reply)"),
             ("ܫܡܝ … ܝܠܗ", "SHIM-mi … i-LEH", "My name is …"),
             ("ܬܘܕܝ", "TAW-di", "Thank you"),
             ("ܓ̰ܙܐܟܐܠܠܗܘ ܚܝܪܐܢ", "ja-ZAA-kal-laa-hu KHAY-ran", "May Allah reward you with good"),
             ("ܝܡܐ · ܒܒܐ", "YIM-ma · BAA-ba", "Mother · Father"),
             ("ܐܚܘܢܐ · ܚܬܐ", "a-KHOO-na · KHAA-ta", "Brother · Sister"),
             ("ܐܝܢ · ܠܐ", "eh · la", "Yes · No"),
             ("ܐܢܐ ܝܠܦܢ ܣܘܪܝܬ!", "AA-na YAL-pin SOO-rit!", "I am learning Assyrian! (a girl says: yal-PAN)")],
    cheer=("ܡܐܫܐܠܠܗ! ܒܣܝܡܐ!", "maa-shaa-AL-lah! ba-SEE-ma!", "Well done, lovely!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), entry “Assyrian Neo-Aramaic”.",
    book_pic=dict(left="ܐ ܒ ܓ", right="ܕ ܗ ܘ"),
    review_note="Everything Assyrian needs a native check, especially: the letter names as said in Assyrian (zen, SIM-kat, eh…); "
                "the words ܗܘܐ (air, wind), ܣܦܝܢܬܐ (ship), ܥܢܒ̈ܐ (grapes), ܦܬܘܪܐ (table), ܨܦܪܐ (morning), ܩܫܬܐ (rainbow), "
                "ܕܪܡܢܐ (medicine); the number ܣܝܦܪ (zero); the phrases ܐܢܐ ܝܠܦܢ ܣܘܪܝܬ (I am learning Assyrian), "
                "ܒܣܝܡܐ (well done), the title ܐܠܦ ܒܝܬ ܩܕܡܝܐ ܕܝܠܝ and ܐܗܐ ܟܬܒܐ ܕܝܠܝ ܝܠܗ; and the spelling of the Arabic "
                "phrases in Syriac letters. Words are deliberately unvocalized.",
    tiles="ܐܒܓܕܗܘ", cover_pics=["pomegranate", "sun", "tree", "star"], title_size=48,
    speakers_blurb="Assyrian Neo-Aramaic (Sureth) is spoken by several hundred thousand people in the Middle East and around the world.",
    sample_words=[("ܫܡܫܐ", "SHIM-sha", "sun"), ("ܘܪܕܐ", "WAR-da", "flower"), ("ܚܒܘܫܐ", "kha-BOO-sha", "apple")],
    keywords=["assyrian alphabet book for kids", "learn assyrian neo-aramaic for children", "syriac letters coloring book",
              "sureth aramaic tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "aramaic alphabet for kids"],
))
