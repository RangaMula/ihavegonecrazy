# -*- coding: utf-8 -*-
"""Book 57 - Tigrinya (Ethiopic script, Ge'ez fidel: 32 letter families incl. ቐ and ኸ). Allamahul Bayan Series. REVIEW DRAFT.
Each letter page teaches the base (1st-order) form of one consonant family; the phonetics box shows all seven
orders of that family with their sounds (helpers in languages/_ethiopic.py)."""
from generic import build, section, fontset
from maps import region_map
from _ethiopic import make_L, grid_table, CSS

L = make_L("The {} family · 7 sounds")
POP = "(a popped sound: hold your breath, then let the sound burst out)"


def W(text, pt):
    """A long word, drawn a little smaller on the letter page."""
    return f'<span style="font-size:{pt}pt">{text}</span>'


LETTERS = [
    L("ሀ", "h", "ሀ", "he", "‘h’ as in “hat”", "ህንጻ", "hin-ts'a", "building", "building"),
    L("ለ", "l", "ለ", "le", "‘l’ as in “lamp”", "ሎሚ", "lo-mi", "lemon", "lemon"),
    L("ሐ", "ḥ", "ሐ", "ḥe", "a strong, breathy ‘h’ from deep in the throat, like the Arabic letter <span class='ar' style='font-size:16pt;line-height:1'>ح</span>", "ሕብሪ", "ḥib-ri",
      "colour", "palette", note="Muslim children know this sound from the Qur’an: it is the Arabic <span class='ar' style='font-size:15pt;line-height:1'>ح</span>."),
    L("መ", "m", "መ", "me", "‘m’ as in “moon”", "መንበር", "men-ber", "chair, stool", "stool"),
    L("ረ", "r", "ረ", "re", "a quick tapped ‘r’, as in Spanish “pero”", "ሩዝ", "ruz", "rice", "rice"),
    L("ሰ", "s", "ሰ", "se", "‘s’ as in “sun”", "ሰዓት", "se-ʿat", "clock", "clock"),
    L("ሸ", "sh", "ሸ", "she", "‘sh’ as in “ship”", "ሽጉርቲ", "shi-gur-ti", "onion", "onion"),
    L("ቀ", "q", "ቀ", "qe", f"‘q’ — a ‘k’ said far back in the throat {POP}", W("ቀስቲ ደበና", 32), "qes-ti de-be-na", "rainbow", "rainbow"),
    L("ቐ", "qh", "ቐ", "qhe", "a soft, scratchy ‘kh’ from the back of the throat: ቀ said softly after a vowel", "ሳንዱቕ", "san-duqh",
      "box", "box", inside=True,
      note="<span class='nt'>ቐ</span> never starts a word. Find <span class='nt'>ቕ</span> at the end of <span class='nt'>ሳንዱቕ</span>!"),
    L("በ", "b", "በ", "be", "‘b’ as in “ball”", "ባኒ", "ba-ni", "bread", "am_bread"),
    L("ቨ", "v", "ቨ", "ve", "‘v’ as in “van”", "ቫኒላ", "va-ni-la", "vanilla (a climbing plant with sweet pods)", "am_vanilla",
      note="<span class='nt'>ቨ</span> is a newer letter, used only in words borrowed from other languages."),
    L("ተ", "t", "ተ", "te", "‘t’ as in “top”", "ቲማቲም", "ti-ma-tim", "tomato", "tomato"),
    L("ቸ", "ch", "ቸ", "che", "‘ch’ as in “chair”", "ቸኮላታ", "che-ko-la-ta", "chocolate", "am_chocolate"),
    L("ነ", "n", "ነ", "ne", "‘n’ as in “net”", "ነጸላ", "ne-ts'e-la", "netsela, a light cotton shawl", "scarf"),
    L("ኘ", "ny", "ኘ", "nye", "‘ny’ as in “canyon”", "ትግርኛ", "tig-ri-nya", "Tigrinya — the language of this book!", "book",
      args=dict(left="ሀ ለ ሐ", right="መ ረ ሰ"), inside=True,
      note="<span class='nt'>ኘ</span> hardly ever starts a word. Find <span class='nt'>ኛ</span> at the end of <span class='nt'>ትግርኛ</span>!"),
    L("አ", "", "አ", "e", "the vowels on their own: <b>አ</b> says ‘e’ as in “the”, and its 4th form <b>ኣ</b> says ‘a’",
      W("እንቋቕሖ", 34), "in-qwaqh-ḥo", "egg", "egg"),
    L("ከ", "k", "ከ", "ke", "‘k’ as in “kite”", "ኩባያ", "ku-ba-ya", "cup", "teacup"),
    L("ኸ", "kh", "ኸ", "khe", "a soft, scratchy ‘kh’: ከ said softly after a vowel", "ኮኾብ", "ko-khob", "star", "star", inside=True,
      note="<span class='nt'>ኸ</span> hardly ever starts a word. Find <span class='nt'>ኾ</span> in the middle of <span class='nt'>ኮኾብ</span>!"),
    L("ወ", "w", "ወ", "we", "‘w’ as in “water”", "ወርሒ", "wer-ḥi", "moon; month", "moon"),
    L("ዐ", "ʿ", "ዐ", "ʿe", "a squeezed sound from deep in the throat, like the Arabic letter <span class='ar' style='font-size:16pt;line-height:1'>ع</span>", "ዕምባባ", "ʿim-ba-ba", "flower", "flower",
      note="Muslim children know this sound from the Qur’an: it is the Arabic <span class='ar' style='font-size:15pt;line-height:1'>ع</span>."),
    L("ዘ", "z", "ዘ", "ze", "‘z’ as in “zoo”", "ዝናብ", "zi-nab", "rain", "raincloud"),
    L("ዠ", "zh", "ዠ", "zhe", "‘zh’ like the ‘s’ in “measure” — a rare letter", W("ቴሌቪዥን", 36), "té-lé-vi-zhin", "television", "am_tv",
      inside=True, note="<span class='nt'>ዠ</span> is found only in borrowed words. Find <span class='nt'>ዥ</span> in <span class='nt'>ቴሌቪዥን</span>!"),
    L("የ", "y", "የ", "ye", "‘y’ as in “yes”", "ማይ", "may", "water", "water", inside=True,
      note="Few Tigrinya words start with <span class='nt'>የ</span>. Find <span class='nt'>ይ</span> at the end of <span class='nt'>ማይ</span>!"),
    L("ደ", "d", "ደ", "de", "‘d’ as in “door”", "ደበና", "de-be-na", "cloud", "clouds"),
    L("ጀ", "j", "ጀ", "je", "‘j’ as in “jam”", "ጀልባ", "jel-ba", "boat", "boat"),
    L("ገ", "g", "ገ", "ge", "‘g’ as in “go”", "ገዛ", "ge-za", "house", "house"),
    L("ጠ", "t'", "ጠ", "t'e", f"a popped ‘t’ {POP}", "ጣውላ", "t'aw-la", "table", "am_table"),
    L("ጨ", "ch'", "ጨ", "ch'e", f"a popped ‘ch’ {POP}", "ጨው", "ch'ew", "salt", "salt", args=dict(label="ጨው")),
    L("ጰ", "p'", "ጰ", "p'e", f"a popped ‘p’ — a rare letter {POP}", "ጳጉሜን", "p'a-gu-mén", "Pagumén, the short 13th month",
      "sunrise", note="The Ge’ez calendar has 13 months: twelve of 30 days, then <span class='nt'>ጳጉሜን</span> with 5 or 6 days."),
    L("ጸ", "ts'", "ጸ", "ts'e", f"a popped ‘ts’ {POP}", "ጸሓይ", "ts'e-ḥay", "sun", "sun"),
    L("ፈ", "f", "ፈ", "fe", "‘f’ as in “fan”", "ፍሩታ", "fi-ru-ta", "fruit", "basket"),
    L("ፐ", "p", "ፐ", "pe", "‘p’ as in “pen”", "ፓፓያ", "pa-pa-ya", "papaya", "am_papaya"),
]

INTRO = f"""<p>Tigrinya is written with the <b>fidel</b> (<span class="nt">ፊደል</span>). Every letter stands for a whole
<b>syllable</b>: a consonant <i>and</i> a vowel together. This book teaches <b>{len(LETTERS)} letter families</b>.</p>
<div class="box" style="margin:0.08in 0"><h3>One family, seven sounds</h3>
Each family starts with its <b>base letter</b> (the 1st form). Small changes to its shape give six more forms, one for each vowel.
Read the grid across: <i>le, lu, li, la, lé, l(i), lo</i>.
{grid_table([("ለ", "l"), ("መ", "m"), ("በ", "b"), ("ሐ", "ḥ")])}
<span class="small">The forms are called <span class="nt">ግዕዝ ካዕብ ሣልስ ራብዕ ኃምስ ሳድስ ሳብዕ</span>
(<i>ge'ez, ka'ib, salis, rabi', hamis, sadis, sabi'</i>): 1st to 7th.</span></div>
<div class="box" style="margin:0.08in 0"><h3>Spot the vowel marks</h3>
2nd: a little stroke on the right (<span class="nt">ሉ</span>) · 3rd: a foot on the right leg (<span class="nt">ሊ</span>) ·
4th: a leg that grows or bends (<span class="nt">ላ</span>) · 5th: a little ring (<span class="nt">ሌ</span>) ·
6th: a bent or broken leg (<span class="nt">ል</span>) · 7th: a ring or a shorter leg (<span class="nt">ሎ</span>).</div>
<div class="box"><h3>Tigrinya’s own letters</h3><span class="nt">ቐ</span> and <span class="nt">ኸ</span> are soft, scratchy forms of
<span class="nt">ቀ</span> and <span class="nt">ከ</span> that come after a vowel. Tigrinya also keeps <span class="nt">ሀ</span> and
<span class="nt">ሐ</span>, and <span class="nt">አ</span> and <span class="nt">ዐ</span>, as different sounds. On every letter page the
<b>shaded</b> form in the family box is the one used in the word.</div>"""

LANG = build(dict(
    code="ti", folder="book-57-tigrinya", series_no=57, isbn="", draft=True,
    name="Tigrinya", native="ትግርኛ", native_tr="tig-ri-nya", name_word="ስም", write_word="ጽሓፍ",
    title_native="ፊደል ትግርኛ", title_letters="ሀለሐመረሰ", belongs_native="እዚ መጽሓፍ ናተይ እዩ",
    belongs_pic="flower", alphabet_native="ፊደል", numbers_native="ቁጽርታት", numbers_tr="qu-ts'ir-tat",
    phrases_native="ቀዳሞት ቃላት",
    fonts=fontset("Noto Sans Ethiopic", "noto-sans-ethiopic-ethiopic", "Noto Sans Ethiopic", "noto-sans-ethiopic-ethiopic"),
    disp_family="Noto Sans Ethiopic", text_family="Noto Sans Ethiopic",
    glyph_font=["noto-sans-ethiopic-ethiopic-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Ethiopic",
    phon_feature="each letter family’s <b>seven vowel forms</b> (ለ ሉ ሊ ላ ሌ ል ሎ) with their sounds",
    sections=[section(LETTERS, label="FAMILY", chip="THE LETTER FAMILIES", title="The Fidel", native="ፊደል",
                      native_tr="fi-del — “the letters”", chart_title="letter families", chart_cols=7, warmup_cols=6,
                      warmup_title="the base letters", intro_html=INTRO)],
    sound_notes=[
        "Vowels: <b>e</b> as in “the” · <b>u</b> as in “rule” · <b>i</b> as in “ski” · <b>a</b> as in “father” · "
        "<b>é</b> as in “café” · <b>o</b> as in “go”. <b>(i)</b> is a very quick ‘i’, often silent.",
        "An <b>apostrophe after a consonant</b> (<i>q, t', ch', p', ts'</i>) marks a <b>popped</b> sound: hold your breath, then let it burst out.",
        "<b>ḥ</b> is the Arabic <span class='ar' style='font-size:15pt;line-height:1'>ح</span>; <b>ʿ</b> is the Arabic <span class='ar' style='font-size:15pt;line-height:1'>ع</span>; <b>kh</b> and <b>qh</b> are soft, "
        "scratchy sounds like the Arabic <span class='ar' style='font-size:15pt;line-height:1'>خ</span>.",
        "<b>ny</b> as in “canyon”; <b>zh</b> like the ‘s’ in “measure”. Hyphens split the syllables; say them all evenly."],
    phon_explain="The box marked <i>The … family · 7 sounds</i> shows the letter’s <b>whole family</b>: the base letter and its "
                 "six vowel forms, each with its sound. The shaded form is the one used in the word on that page.",
    standard="the Tigrinya of Asmara",
    hello=[
        ("Who speaks it?", "About <b>10 million people</b> speak Tigrinya.<sup>³</sup>"),
        ("Where?", "In <b>Eritrea</b> and in the <b>Tigray</b> region of northern <b>Ethiopia</b>, in East Africa, "
                   "and in Tigrinya-speaking families around the world."),
        ("How is it written?", "In the <b>fidel</b> (<span class='nt'>ፊደል</span>), from <b>left to right</b>, like Amharic. Each letter is a whole syllable, like <i>ba</i> or <i>mo</i>."),
        ("How many letters?", f"<b>{len(LETTERS)} letter families</b>, each with <b>7 forms</b>: more than 200 letters, all made from a few simple shapes!"),
        ("Sounds you know!", "Tigrinya has the throat sounds <span class='nt'>ሐ</span> and <span class='nt'>ዐ</span>: they are the Arabic "
                             "<span class='ar' style='font-size:15pt;line-height:1'>ح</span> and <span class='ar' style='font-size:15pt;line-height:1'>ع</span> that Muslim children read in the Qur’an."),
        ("Did you know?", "The first Muslims to leave Makkah for safety travelled to <b>al-Ḥabasha</b> (Abyssinia), where the just king, "
                          "<b>an-Najāshī</b>, welcomed and protected them."),
    ],
    hello_pics=[("flower", {}), ("star", {}), ("mosque", {})],
    map=region_map(frame=[[34.0, 9.0], [46.0, 21.0]],
                   points=dict(asmara=[38.93, 15.32], keren=[38.46, 15.78], massawa=[39.45, 15.61], mekelle=[39.47, 13.50]),
                   area=(38.9, 14.6, 170, 190),
                   cities=[("asmara", "Asmara", 0, 34, "middle", False), ("keren", "Keren", -14, 0, "end", False),
                           ("massawa", "Massawa", 14, -4, "start", False), ("mekelle", "Mekelle", 14, 8, "start", False)],
                   label="HORN OF AFRICA", label_at=[41.5, 10.3], marker=[39.0, 15.0],
                   caption="The circle shows the Horn of Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> the dashed line shows where "
                          "Tigrinya is spoken: the highlands of Eritrea, around Asmara and Keren, and the Tigray region of northern "
                          "Ethiopia, around Mekelle.",
                   seas=[("Red Sea", 40.4, 17.8), ("Gulf of Aden", 44.6, 12.0)], world_r=13),
    digits=[("0", "ዜሮ", "zé-ro", "zero"), ("1", "ሓደ", "ḥa-de", "one · ፩"), ("2", "ክልተ", "kil-te", "two · ፪"),
            ("3", "ሰለስተ", "se-les-te", "three · ፫"), ("4", "ኣርባዕተ", "ar-ba-ʿi-te", "four · ፬"), ("5", "ሓሙሽተ", "ḥa-mush-te", "five · ፭"),
            ("6", "ሽዱሽተ", "shi-dush-te", "six · ፮"), ("7", "ሸውዓተ", "shew-ʿa-te", "seven · ፯"), ("8", "ሸሞንተ", "she-mon-te", "eight · ፰"),
            ("9", "ትሽዓተ", "tish-ʿa-te", "nine · ፱")],
    phrases=[("ኣሰላሙ ዓለይኩም", "as-se-la-mu ʿa-ley-kum", "Peace be upon you (the Muslim greeting)"),
             ("ወዓለይኩም ኣሰላም", "we-ʿa-ley-kum as-se-lam", "And upon you be peace (the reply)"),
             ("ሰላም!", "se-lam!", "Hello!"),
             ("ስመይ … እዩ", "sim-ey … i-yu", "My name is …"),
             ("የቐንየለይ", "ye-qhen-ye-ley", "Thank you"),
             ("ጀዛከላሁ ኸይራን", "je-za-ke-la-hu khey-ran", "May Allah reward you with good"),
             ("ኣደ · ኣቦ", "a-de · a-bo", "Mother · Father"),
             ("ሓው · ሓብቲ", "ḥaw · ḥab-ti", "Brother · Sister"),
             ("እወ · ኣይፋል", "i-we · ay-fal", "Yes · No"),
             ("ትግርኛ ይመሃር ኣለኹ!", "tig-ri-nya yi-me-har a-le-khu!", "I am learning Tigrinya!")],
    cheer=("ማሻኣላህ! ኣዝዩ ጽቡቕ!", "ma-sha-al-lah! az-yu ts'i-buqh!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="ሀ ለ ሐ", right="መ ረ ሰ"),
    review_note="Drafted with AI, not yet checked by a Tigrinya speaker; vocabulary is the least certain part. Please check: "
                "(1) every word and spelling, especially ህንጻ, ሕብሪ, መንበር, ሽጉርቲ, ቀስቲ ደበና, ሳንዱቕ, ባኒ, ቸኮላታ, ነጸላ, እንቋቕሖ, ኩባያ, "
                "ኮኾብ, ዕምባባ, ቴሌቪዥን, ጣውላ, ፍሩታ, ፓፓያ, ሎሚ; (2) weak example words for rare letters (የ via ማይ, ዠ via ቴሌቪዥን, "
                "ቨ via ቫኒላ); (3) the choice of 32 families (ቨ included; ሠ ኀ ፀ left out as Tigrinya does not use them); "
                "(4) the simplified transliteration (e for the 1st order, (i) for the 6th, ḥ, ʿ, kh/qh, apostrophe for ejectives); "
                "(5) the title ‘ፊደል ትግርኛ’, ‘ዜሮ’ for zero, and the phrases, especially ‘ጀዛከላሁ ኸይራን’, ‘ስመይ … እዩ’ and ‘ትግርኛ ይመሃር ኣለኹ’.",
    tiles="ሀለመአበጸ", cover_pics=["flower", "rainbow", "am_bread", "mosque"], title_size=48,
    speakers_blurb="Tigrinya is spoken by about 10 million people in Eritrea, northern Ethiopia and around the world.",
    sample_words=[("ዕምባባ", "ʿim-ba-ba", "flower"), ("ጸሓይ", "ts'e-ḥay", "sun"), ("ጀልባ", "jel-ba", "boat")],
    keywords=["tigrinya alphabet book for kids", "learn tigrinya for children", "tigrinya fidel coloring book",
              "eritrean alphabet tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual tigrinya english toddlers"],
    extra_css=CSS,
))
