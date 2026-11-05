# -*- coding: utf-8 -*-
"""Book 56 - Amharic (Ethiopic script, Ge'ez fidel: 33 letter families). Allamahul Bayan Series. REVIEW DRAFT.
Each letter page teaches the base (1st-order) form of one consonant family; the phonetics box shows all seven
orders of that family with their sounds (helpers in languages/_ethiopic.py)."""
from generic import build, section, fontset
from maps import region_map
from _ethiopic import make_L, grid_table, CSS

L = make_L("The {} family · 7 sounds")
AV = ["a", "u", "i", "a", "é", "(i)", "o"]       # Amharic: ሀ ሐ ኀ አ ዐ say ‘a’ in the 1st order
SAME_H = "In Amharic <span class='nt'>ሀ ሐ ኀ</span> all say ‘h’. Children tell them apart by their nicknames."
SAME_S = "<span class='nt'>ሠ</span> and <span class='nt'>ሰ</span> sound the same; each is kept in its own words."
SAME_A = "<span class='nt'>አ</span> and <span class='nt'>ዐ</span> sound the same in Amharic; each is kept in its own words."
SAME_TS = "<span class='nt'>ጸ</span> and <span class='nt'>ፀ</span> sound the same; each is kept in its own words."
POP = "(a popped sound: hold your breath, then let the sound burst out)"


def W(text, pt):
    """A long word, drawn a little smaller on the letter page."""
    return f'<span style="font-size:{pt}pt">{text}</span>'


LETTERS = [
    L("ሀ", "h", "ሀ", "ha", "‘h’ as in “hat”", "ህንፃ", "hin-ts'a", "building", "building", vowels=AV, note=SAME_H),
    L("ለ", "l", "ለ", "le", "‘l’ as in “lamp”", "ሎሚ", "lo-mi", "lemon", "lemon"),
    L("ሐ", "h", "ሐመሩ ሐ", "hameru ha", "‘h’ as in “hat” — the same sound as ሀ", "ሐብሐብ", "hab-hab", "watermelon", "watermelon",
      vowels=AV, note=SAME_H),
    L("መ", "m", "መ", "me", "‘m’ as in “moon”", "መስኮት", "mes-kot", "window", "window"),
    L("ሠ", "s", "ንጉሡ ሠ", "negusu se", "‘s’ as in “sun” — the same sound as ሰ", "ሥዕል", "si-'il", "picture, painting", "palette",
      note=SAME_S),
    L("ረ", "r", "ረ", "re", "a quick tapped ‘r’, as in Spanish “pero”", "ሩዝ", "ruz", "rice", "rice"),
    L("ሰ", "s", "እሳቱ ሰ", "isatu se", "‘s’ as in “sun”", "ሰዓት", "se-'at", "clock", "clock", note=SAME_S),
    L("ሸ", "sh", "ሸ", "she", "‘sh’ as in “ship”", "ሸንኮራ", "shen-ko-ra", "sugarcane", "sugarcane"),
    L("ቀ", "q", "ቀ", "qe", f"‘q’ — a ‘k’ said far back in the throat {POP}", W("ቀስተ ደመና", 32), "qes-te de-me-na", "rainbow", "rainbow"),
    L("በ", "b", "በ", "be", "‘b’ as in “ball”", "በር", "ber", "door", "door"),
    L("ቨ", "v", "ቨ", "ve", "‘v’ as in “van”", "ቫኒላ", "va-ni-la", "vanilla (a climbing plant with sweet pods)", "am_vanilla",
      note="<span class='nt'>ቨ</span> is a newer letter, used only in words borrowed from other languages."),
    L("ተ", "t", "ተ", "te", "‘t’ as in “top”", "ተራራ", "te-ra-ra", "mountain", "mountain"),
    L("ቸ", "ch", "ቸ", "che", "‘ch’ as in “chair”", "ችግኝ", "chi-giny", "seedling, a young plant", "am_seedling"),
    L("ኀ", "h", "ብዙኀኑ ኀ", "bizuhanu ha", "‘h’ as in “hat” — the same sound as ሀ", "ኃይል", "hayl", "power, energy", "bulb",
      vowels=AV, note="ኀ is the rarest of the three h-letters. " + SAME_H.split(". ")[1]),
    L("ነ", "n", "ነ", "ne", "‘n’ as in “net”", "ነጠላ", "ne-t'e-la", "netela, a light cotton shawl", "scarf"),
    L("ኘ", "ny", "ኘ", "nye", "‘ny’ as in “canyon”", "አማርኛ", "a-ma-ri-nya", "Amharic — the language of this book!", "book",
      args=dict(left="ሀ ለ ሐ", right="መ ሠ ረ"), inside=True,
      note="<span class='nt'>ኘ</span> hardly ever starts a word. Find <span class='nt'>ኛ</span> at the end of <span class='nt'>አማርኛ</span>!"),
    L("አ", "", "አልፋው አ", "alfaw a", "the vowel ‘a’ as in “father” — this family writes the vowels on their own",
      "አበባ", "a-be-ba", "flower", "flower", vowels=AV, note=SAME_A),
    L("ከ", "k", "ከ", "ke", "‘k’ as in “kite”", "ኮከብ", "ko-keb", "star", "star"),
    L("ወ", "w", "ወ", "we", "‘w’ as in “water”", "ወንበር", "wen-ber", "chair, stool", "stool"),
    L("ዐ", "", "ዓይኑ ዐ", "aynu a", "the vowel ‘a’ — the same sound as አ", "ዓለም", "a-lem", "the world", "globe",
      vowels=AV, note=SAME_A),
    L("ዘ", "z", "ዘ", "ze", "‘z’ as in “zoo”", "ዝናብ", "zi-nab", "rain", "raincloud"),
    L("ዠ", "zh", "ዠ", "zhe", "‘zh’ like the ‘s’ in “measure” — a rare letter", "ዣንጥላ", "zhan-t'i-la", "umbrella", "umbrella"),
    L("የ", "y", "የ", "ye", "‘y’ as in “yes”", W("የሱፍ አበባ", 32), "ye-suf a-be-ba", "sunflower", "am_sunflower"),
    L("ደ", "d", "ደ", "de", "‘d’ as in “door”", "ደመና", "de-me-na", "cloud", "clouds"),
    L("ጀ", "j", "ጀ", "je", "‘j’ as in “jam”", "ጀልባ", "jel-ba", "boat", "boat"),
    L("ገ", "g", "ገ", "ge", "‘g’ as in “go”", "ጋሪ", "ga-ri", "cart", "cart"),
    L("ጠ", "t'", "ጠ", "t'e", f"a popped ‘t’ {POP}", W("ጠረጴዛ", 36), "t'e-re-p'é-za", "table", "am_table"),
    L("ጨ", "ch'", "ጨ", "ch'e", f"a popped ‘ch’ {POP}", "ጨረቃ", "ch'e-re-qa", "moon", "moon"),
    L("ጰ", "p'", "ጰ", "p'e", f"a popped ‘p’ — a rare letter {POP}", "ጳጉሜ", "p'a-gu-mé", "Pagumé, the short 13th month",
      "sunrise", note="The Ethiopian calendar has 13 months: twelve of 30 days, then <span class='nt'>ጳጉሜ</span> with 5 or 6 days."),
    L("ጸ", "ts'", "ጸሎቱ ጸ", "ts'elotu ts'e", f"a popped ‘ts’ {POP}", W("ጽጌረዳ", 36), "ts'i-gé-re-da", "rose", "am_rose",
      note=SAME_TS),
    L("ፀ", "ts'", "ፀሐዩ ፀ", "ts'ehayu ts'e", "a popped ‘ts’ — the same sound as ጸ", "ፀሐይ", "ts'e-hay", "sun", "sun", note=SAME_TS),
    L("ፈ", "f", "ፈ", "fe", "‘f’ as in “fan”", "ፊኛ", "fi-nya", "balloon", "balloon"),
    L("ፐ", "p", "ፐ", "pe", "‘p’ as in “pen”", "ፖም", "pom", "apple", "apple"),
]

INTRO = f"""<p>Amharic is written with the <b>fidel</b> (<span class="nt">ፊደል</span>). Every letter stands for a whole
<b>syllable</b>: a consonant <i>and</i> a vowel together. This book teaches <b>{len(LETTERS)} letter families</b>.</p>
<div class="box" style="margin:0.08in 0"><h3>One family, seven sounds</h3>
Each family starts with its <b>base letter</b> (the 1st form). Small changes to its shape give six more forms, one for each vowel.
Read the grid across: <i>le, lu, li, la, lé, l(i), lo</i>.
{grid_table([("ለ", "l"), ("መ", "m"), ("በ", "b")])}
<span class="small">The forms are called <span class="nt">ግዕዝ ካዕብ ሣልስ ራብዕ ኃምስ ሳድስ ሳብዕ</span>
(<i>ge'ez, ka'ib, salis, rabi', hamis, sadis, sabi'</i>): 1st to 7th.</span></div>
<div class="box" style="margin:0.08in 0"><h3>Spot the vowel marks</h3>
2nd: a little stroke on the right (<span class="nt">ሉ</span>) · 3rd: a foot on the right leg (<span class="nt">ሊ</span>) ·
4th: a leg that grows or bends (<span class="nt">ላ</span>) · 5th: a little ring (<span class="nt">ሌ</span>) ·
6th: a bent or broken leg (<span class="nt">ል</span>) · 7th: a ring or a shorter leg (<span class="nt">ሎ</span>).</div>
<div class="box"><h3>On every letter page</h3>The big letter is the <b>base form</b>. The box <i>The … family · 7 sounds</i>
shows all seven forms; the <b>shaded</b> one is the sound that begins the word on that page. Some families have an extra
‘-wa’ form too, like <span class="nt">ሏ</span> <i>lwa</i>. The letter <span class="nt">ኸ</span> is used in a few words only, so it has no page here.</div>"""

LANG = build(dict(
    code="am", folder="book-56-amharic", series_no=56, isbn="", draft=True,
    name="Amharic", native="አማርኛ", native_tr="a-ma-ri-nya", name_word="ስም", write_word="ጻፍ",
    title_native="የአማርኛ ፊደል መጽሐፌ", title_letters="ሀለሐመሠረ", belongs_native="ይህ መጽሐፍ የእኔ ነው",
    belongs_pic="am_sunflower", alphabet_native="ፊደል", numbers_native="ቁጥሮች", numbers_tr="qu-t'i-roch",
    phrases_native="የመጀመሪያ ቃላት",
    fonts=fontset("Noto Sans Ethiopic", "noto-sans-ethiopic-ethiopic", "Noto Sans Ethiopic", "noto-sans-ethiopic-ethiopic"),
    disp_family="Noto Sans Ethiopic", text_family="Noto Sans Ethiopic",
    glyph_font=["noto-sans-ethiopic-ethiopic-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Ethiopic",
    phon_feature="each letter family’s <b>seven vowel forms</b> (ለ ሉ ሊ ላ ሌ ል ሎ) with their sounds",
    sections=[section(LETTERS, label="FAMILY", chip="THE LETTER FAMILIES", title="The Fidel", native="ፊደል",
                      native_tr="fi-del — “the letters”", chart_title="letter families", chart_cols=7, warmup_cols=6,
                      warmup_title="the base letters", intro_html=INTRO)],
    letters_word="Letters",
    sound_notes=[
        "Vowels: <b>e</b> as in “the” · <b>u</b> as in “rule” · <b>i</b> as in “ski” · <b>a</b> as in “father” · "
        "<b>é</b> as in “café” · <b>o</b> as in “go”. <b>(i)</b> is a very quick ‘i’, often silent.",
        "An <b>apostrophe after a consonant</b> (<i>q, t', ch', p', ts'</i>) marks a <b>popped</b> sound: hold your breath, then let it burst out.",
        "An apostrophe <b>between vowels</b> (<i>se-'at</i>) is a tiny catch in the throat, like the middle of “uh-oh”.",
        "<b>ny</b> as in “canyon”; <b>zh</b> like the ‘s’ in “measure”. Hyphens split the syllables; say them all evenly."],
    phon_explain="The box marked <i>The … family · 7 sounds</i> shows the letter’s <b>whole family</b>: the base letter and its "
                 "six vowel forms, each with its sound. The shaded form is the one that starts the word on that page.",
    standard="the Amharic of Addis Ababa",
    hello=[
        ("Who speaks it?", "About <b>57 million people</b> speak Amharic: more than half of them from birth, the rest as a second language.<sup>³</sup>"),
        ("Where?", "All over <b>Ethiopia</b>, in East Africa, especially in the highlands and the capital <b>Addis Ababa</b>, "
                   "and in Ethiopian families around the world."),
        ("How is it written?", "In the <b>fidel</b> (<span class='nt'>ፊደል</span>), from <b>left to right</b>. Each letter is a whole syllable, like <i>ba</i> or <i>mo</i>."),
        ("How many letters?", f"<b>{len(LETTERS)} letter families</b>, each with <b>7 forms</b>: more than 200 letters, all made from a few simple shapes!"),
        ("Did you know?", "The first Muslims to leave Makkah for safety travelled to <b>al-Ḥabasha</b> (Abyssinia), where the just king, "
                          "<b>an-Najāshī</b>, welcomed and protected them."),
        ("13 months!", "The Ethiopian calendar has <b>13 months</b>: twelve of 30 days and one short month, "
                       "<span class='nt'>ጳጉሜ</span>, of 5 or 6 days."),
    ],
    hello_pics=[("am_sunflower", {}), ("star", {}), ("mosque", {})],
    map=region_map(frame=[[33.0, 2.0], [50.0, 19.0]],
                   points=dict(addis=[38.74, 9.03], gondar=[37.47, 12.60], bahirdar=[37.39, 11.59], dessie=[39.63, 11.13]),
                   area=(38.3, 10.6, 175, 215),
                   cities=[("addis", "Addis Ababa", 14, 8, "start", False), ("gondar", "Gondar", 14, 8, "start", False),
                           ("bahirdar", "Bahir Dar", -14, 8, "end", False), ("dessie", "Dessie", 14, 8, "start", False)],
                   label="ETHIOPIA", label_at=[42.5, 6.5], marker=[39.0, 9.0],
                   caption="The circle shows the Horn of Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Amharic is spoken all over "
                          "Ethiopia. The dashed line shows the highlands around Gondar, Bahir Dar and Dessie, where most families "
                          "speak it at home, and the capital, Addis Ababa.",
                   seas=[("Red Sea", 39.6, 17.4), ("Gulf of Aden", 47.0, 12.2)], world_r=13),
    digits=[("0", "ዜሮ", "zé-ro", "zero"), ("1", "አንድ", "and", "one · ፩"), ("2", "ሁለት", "hu-let", "two · ፪"),
            ("3", "ሦስት", "sost", "three · ፫"), ("4", "አራት", "a-rat", "four · ፬"), ("5", "አምስት", "a-mist", "five · ፭"),
            ("6", "ስድስት", "sid-ist", "six · ፮"), ("7", "ሰባት", "se-bat", "seven · ፯"), ("8", "ስምንት", "si-mint", "eight · ፰"),
            ("9", "ዘጠኝ", "ze-t'eny", "nine · ፱")],
    phrases=[("አሰላሙ ዐለይኩም", "as-se-la-mu a-ley-kum", "Peace be upon you (the Muslim greeting)"),
             ("ወዐለይኩም አሰላም", "we-a-ley-kum as-se-lam", "And upon you be peace (the reply)"),
             ("ሰላም!", "se-lam!", "Hello!"),
             ("ስሜ … ነው", "si-mé … new", "My name is …"),
             ("አመሰግናለሁ", "a-me-se-gi-na-le-hu", "Thank you"),
             ("ጀዛከላሁ ኸይራን", "je-za-ke-la-hu khey-ran", "May Allah reward you with good"),
             ("እናት · አባት", "i-nat · a-bat", "Mother · Father"),
             ("ወንድም · እህት", "wen-dim · i-hit", "Brother · Sister"),
             ("አዎ · አይ", "a-wo · ay", "Yes · No"),
             ("አማርኛ እየተማርኩ ነው!", "a-ma-ri-nya i-ye-te-mar-ku new!", "I am learning Amharic!")],
    cheer=("ማሻአላህ! በጣም ጎበዝ!", "ma-sha-al-lah! be-t'am go-bez!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded; first- and second-language speakers together.",
    book_pic=dict(left="ሀ ለ ሐ", right="መ ሠ ረ"),
    review_note="Drafted with AI, not yet checked by an Amharic speaker. Please check: (1) the nicknames for the same-sounding letters "
                "(ሐመሩ ሐ, ብዙኀኑ ኀ, ንጉሡ ሠ, እሳቱ ሰ, አልፋው አ, ዓይኑ ዐ, ጸሎቱ ጸ, ፀሐዩ ፀ) and whether ሀ should carry one too; "
                "(2) spellings with the ‘historic’ letters: ህንፃ (or ሕንፃ?), ሐብሐብ, ኃይል, ሥዕል, ዓለም, ጽጌረዳ, ፀሐይ, ጳጉሜ; "
                "(3) the choice of 33 families (ቨ included, ኸ left out); (4) the simplified transliteration (e for the 1st order, "
                "(i) for the 6th, apostrophe for ejectives) and the vowel-mark descriptions on the Fidel intro page; "
                "(5) the title ‘የአማርኛ ፊደል መጽሐፌ’ and the phrases, especially ‘ጀዛከላሁ ኸይራን’ and the greeting spellings.",
    tiles="ሀለመአበፀ", cover_pics=["am_sunflower", "rainbow", "flower", "mosque"], title_size=48,
    speakers_blurb="Amharic is spoken by about 57 million people in Ethiopia and around the world.",
    sample_words=[("አበባ", "a-be-ba", "flower"), ("ፀሐይ", "ts'e-hay", "sun"), ("ጀልባ", "jel-ba", "boat")],
    keywords=["amharic alphabet book for kids", "learn amharic for children", "amharic fidel coloring book",
              "ethiopian alphabet tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual amharic english toddlers"],
    extra_css=CSS,
))
