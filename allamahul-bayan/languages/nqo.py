# -*- coding: utf-8 -*-
"""Book 59 - Manding (Bambara / Bamanankan) in the N'Ko script (right to left, joined letters, 27 letters).
Allamahul Bayan Series. REVIEW DRAFT - every word needs checking by a native N'Ko writer.
Words are written with every vowel and WITHOUT tone marks (see review_note); each word also has its Bambara
Latin spelling and an easy English sound guide."""
from generic import build, letter, section
from maps import region_map

JOIN = "ߺ"  # NKO LAJANYALAN, the joining line (like the Arabic tatweel)
PH = "Letter shapes · how it joins"


def forms(ch):
    return (f'<div class="ntd" style="font-size:24pt;line-height:1.6;direction:rtl;text-align:left;unicode-bidi:isolate">'
            f'{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}{JOIN}&nbsp;&nbsp;{JOIN}{ch}</div>'
            f'<div class="small">start · middle · end of a word (read right to left)</div>')


def N(ch, name, name_tr, lat, sound, word, wlat, easy, meaning, pic, args=None, note=None, extra=None):
    phon = (forms(ch) + f'<div class="small" style="margin-top:3px">Latin letter: <b>{lat}</b>'
            + (f' · {extra}' if extra else "") + '</div>')
    if note is None and not word.startswith(ch):
        note = f'Find <span class="nt">{ch}</span> inside <span class="nt">{word}</span>!'
    return letter(ch, name, name_tr, sound, word, f"<b>{wlat}</b> · {easy}", meaning, pic, phon, PH, args, note)


VOWELS = [
    N("ߊ", "ߊ", "a", "a", "‘a’ as in “father”", "ߊߟߌߞߎߙߊߣߊ", "Alikurana", "ah-lee-koo-rah-nah", "the Qur’an", "zgh_rehal"),
    N("ߋ", "ߋ", "e", "e", "‘ay’ as in “say”, short and pure", "ߛߋߟߌ", "seli", "say-lee", "prayer (salah)", "prayermat",
      note='<span class="nt">ߋ</span> hardly ever starts a word. Find it in <span class="nt">ߛߋߟߌ</span>!'),
    N("ߌ", "ߌ", "i", "i", "‘ee’ as in “see”", "ߡߌߛߌߙߌ", "misiri", "mee-see-ree", "mosque", "mosque"),
    N("ߍ", "ߍ", "ɛ", "ɛ", "‘e’ as in “bed”", "ߣߍߜߍ", "nɛgɛ", "neh-geh", "iron, metal", "anvil"),
    N("ߎ", "ߎ", "u", "u", "‘oo’ as in “moon”", "ߞߎߟߎ", "kulu", "koo-loo", "mountain, hill", "mountain"),
    N("ߏ", "ߏ", "o", "o", "‘o’ as in “go”, short and pure", "ߘߏߟߏ", "dolo", "doh-loh", "star", "star"),
    N("ߐ", "ߐ", "ɔ", "ɔ", "‘aw’ as in “saw”", "ߞߐߟߐ߲", "kɔlɔn", "kaw-lawn", "well (for water)", "well"),
    N("ߒ", "ߒ", "n", "n", "a humming ‘n’ (or ‘ng’) that is a whole syllable by itself", "ߒߕߏߡߌ", "ntomi", "n-toh-mee",
      "tamarind", "tamarind", extra="also the word for “I”"),
]

CONSONANTS = [
    N("ߓ", "ߓߊ", "ba", "b", "‘b’ as in “ball”", "ߓߊߖߌ", "baji", "bah-jee", "river", "waves"),
    N("ߔ", "ߔߊ", "pa", "p", "‘p’ as in “pen” — used mostly in borrowed words", "ߔߐߡߎ", "pɔmu", "paw-moo", "apple", "apple"),
    N("ߕ", "ߕߊ", "ta", "t", "‘t’ as in “top”", "ߕߌߟߋ", "tile", "tee-lay", "sun", "sun"),
    N("ߖ", "ߖߊ", "ja", "j", "‘j’ as in “jam”", "ߖߌ", "ji", "jee", "water", "water"),
    N("ߗ", "ߗߊ", "ca", "c", "‘ch’ as in “church”", "ߗߌߞߍ", "cikɛ", "chee-keh", "farming, work in the fields", "paddy"),
    N("ߘ", "ߘߊ", "da", "d", "‘d’ as in “dog”", "ߘߊߜߊ", "daga", "dah-gah", "cooking pot", "pot"),
    N("ߙ", "ߙߊ", "ra", "r", "a tapped ‘r’ — flick the tongue once; never at the start of a Bambara word", "ߖߌߙߌ", "jiri", "jee-ree",
      "tree", "tree"),
    N("ߚ", "ߚߊ", "rra", "rr", "a rolled ‘r’ — let the tongue buzz; used in borrowed words", "ߚߊߡߊߘߊ߲", "Ramadan", "rrah-mah-dahn",
      "Ramadan, the month of fasting", "iftar"),
    N("ߛ", "ߛߊ", "sa", "s", "‘s’ as in “sun”", "ߛߊ߲ߖߌ", "sanji", "sahn-jee", "rain", "raincloud"),
    N("ߜ", "ߜߊ", "gba", "g", "‘g’ as in “go” in Bambara (‘gb’, said with both lips, in Maninka)", "ߞߐߜߐ", "kɔgɔ", "kaw-gaw",
      "salt", "salt", args=dict(label="ߞߐߜߐ")),
    N("ߝ", "ߝߊ", "fa", "f", "‘f’ as in “fan”", "ߝߎߙߊ", "fura", "foo-rah", "leaf (also: medicine)", "nqo_leaf"),
    N("ߞ", "ߞߊ", "ka", "k", "‘k’ as in “kite”", "ߞߊߟߏ", "kalo", "kah-loh", "moon (and month)", "moon"),
    N("ߟ", "ߟߊ", "la", "l", "‘l’ as in “lamp”", "ߟߋߡߎߙߎ", "lemuru", "lay-moo-roo", "lime, citrus fruit", "lemon"),
    N("ߡ", "ߡߊ", "ma", "m", "‘m’ as in “moon”", "ߡߊ߲ߜߏߙߏ", "mangoro", "mahn-goh-roh", "mango", "mango"),
    N("ߢ", "ߢߊ", "nya", "ɲ", "‘ny’ as in “canyon”", "ߢߐ", "ɲɔ", "nyaw", "millet", "nqo_millet"),
    N("ߣ", "ߣߊ", "na", "n", "‘n’ as in “net”", "ߣߐߣߐ", "nɔnɔ", "naw-naw", "milk", "zgh_milk"),
    N("ߤ", "ߤߊ", "ha", "h", "‘h’ as in “hat” — used mostly in words from Arabic", "ߤߌߖߌ", "hiji", "hee-jee",
      "Hajj, the journey to the Kaaba in Makkah", "kaaba"),
    N("ߥ", "ߥߊ", "wa", "w", "‘w’ as in “water”", "ߥߏߙߏ", "woro", "woh-roh", "kola nuts", "nqo_kola"),
    N("ߦ", "ߦߊ", "ya", "y", "‘y’ as in “yes”", "ߦߋߟߋ߲", "yeelen", "yay-layn", "light", "bulb"),
]

IPA = "U+0250-02BA"  # ɛ ɔ ɲ are missing from Nunito: borrow them from Noto Sans (latin-ext) for that range only
FONTS = ([("Noto Sans NKo", w, "normal", "noto-sans-nko-nko-400-normal.woff2", None) for w in (400, 700, 800)]
         + [("Nunito", w, st, f"noto-sans-latin-ext-{w}-normal.woff2", IPA) for w in (400, 700, 800) for st in ("normal", "italic")])

LANG = build(dict(
    code="nqo", folder="book-59-manding-bambara", series_no=59, isbn="", draft=True, dir="rtl",
    name="Bambara", native="ߓߊߡߊߣߊ߲ߞߊ߲", native_tr="bamanankan (bah-mah-nahn-kahn)", name_word="ߕߐߜߐ · tɔgɔ",
    write_word="ߛߍߓߍ߲ · sɛbɛn",
    title="My First N’Ko Alphabet", cover_title_html="My First N’Ko<br>Alphabet",
    subtitle="A Coloring Book to Learn, Trace & Say the 27 N’Ko Letters of Bambara (Manding) with English Phonetics",
    title_native="ߒ ߓߍ ߒߞߏ ߞߊߟߊ߲", title_letters="ߊߓߕߞߡߣ", belongs_native="ߣߌ߲ ߜߊߝߋ ߦߋ ߒ ߕߊ ߦߋ",
    belongs_pic="star", alphabet_native="ߒߞߏ ߛߓߍߛߎ߲", numbers_native="ߖߊߕߋ", numbers_tr="jate",
    phrases_native="ߞߎߡߊ ߝߐߟߐ",
    fonts=FONTS, disp_family="Noto Sans NKo", text_family="Noto Sans NKo",
    glyph_font=["noto-sans-nko-unjoined-nko-700-normal.woff2"],
    font_credit="Noto Sans NKo, Noto Sans NKo Unjoined",
    letters_word="Letters",
    extra_css=".nt{line-height:1.8} .lp-name{line-height:1.6} .lp-word .w{font-size:38pt;line-height:1.7}",
    phon_feature="each letter’s joined shapes (start · middle · end) and its Latin letter",
    sections=[
        section(VOWELS, label="VOWEL", chip="THE VOWELS", title="The Vowels", native="ߊ ߋ ߌ ߍ ߎ ߏ ߐ ߒ",
                native_tr="a · e · i · ɛ · u · o · ɔ · n — the 7 vowels and the humming n", chart_title="vowels", chart_cols=4, warmup_title="the vowels", warmup_cols=4,
                intro_html="""<p>N’Ko is written <b>from right to left</b>, like the Qur’an. Open your book at any letter page and start reading on the right!</p>
<div class="box" style="margin:0.1in 0"><h3>Seven vowels</h3>Bambara has <b>seven vowels</b>, and N’Ko has a letter for each one:
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ߊ &nbsp; ߋ &nbsp; ߌ &nbsp; ߍ &nbsp; ߎ &nbsp; ߏ &nbsp; ߐ</div>
<div style="text-align:center"><i>a · e · i · ɛ · u · o · ɔ</i> (read from the right)</div></div>
<div class="box" style="margin:0.1in 0"><h3>The humming n</h3>The letter <span class="ntd" style="font-size:18pt">ߒ</span> is a humming ‘n’ that makes a
syllable all by itself, as in <i>n-tomi</i> (tamarind). It also means “I”: <span class="nt">ߒ ߓߍ ߒߞߏ ߞߊߟߊ߲</span> “I am learning N’Ko”.</div>
<div class="box"><h3>The tune of a word</h3>Bambara words have a <b>tune</b> (high and low tones). In books, small marks above the letters show
the tune and long vowels. This coloring book shows the letters without those marks, so they are big and clear.</div>"""),
        section(CONSONANTS, label="CONSONANT", chip="THE CONSONANTS", title="The Consonants", native="ߓ ߔ ߕ ߖ",
                native_tr="ba · pa · ta · ja … — the 19 consonants", chart_title="consonants", chart_cols=7, warmup_title="the consonants", warmup_cols=5,
                intro_html="""<p>Each consonant is named with the vowel <b>a</b>: <span class="ntd" style="font-size:18pt">ߓ</span> is <i>ba</i>,
<span class="ntd" style="font-size:18pt">ߞ</span> is <i>ka</i>, <span class="ntd" style="font-size:18pt">ߡ</span> is <i>ma</i>.</p>
<div class="box" style="margin:0.1in 0"><h3>Letters hold hands</h3>N’Ko letters <b>join</b> along a line, like Arabic letters. Each letter page
shows its shape at the start, middle and end of a word.
<div class="ntd" style="font-size:26pt;text-align:center;direction:rtl;line-height:1.7">ߞ + ߊ + ߟ + ߏ = <span class="nt">ߞߊߟߏ</span></div>
<div style="text-align:center"><i>k + a + l + o = kalo</i> (moon)</div></div>
<div class="box" style="margin:0.1in 0"><h3>One letter, two sounds</h3><span class="ntd" style="font-size:18pt">ߜ</span> is called <i>gba</i>.
In Bambara it says ‘g’ as in “go”; in Maninka it says ‘gb’, with both lips closed.</div>
<div class="box"><h3>A grown-up shortcut</h3>When two syllables in a row have the same vowel, N’Ko writers often write it only once:
<span class="nt">ߓߊߡߊߣߊ߲ߞߊ߲</span> can be written <span class="nt">ߓߡߊߣߊ߲ߞߊ߲</span>. This book writes every vowel, to help you learn.</div>"""),
    ],
    sound_notes=[
        "<b>N’Ko is read from right to left</b>. The tracing rows on each page also start on the right.",
        "Every word is shown in <b>N’Ko</b>, in the usual <b>Bambara Latin spelling</b> (in bold) and in an <b>easy English sound guide</b>: "
        "<i><b>kɔgɔ</b> · kaw-gaw</i>.",
        "In the Latin spelling, <b>ɛ</b> says ‘e’ as in “bed”, <b>ɔ</b> says ‘aw’ as in “saw”, <b>ɲ</b> says ‘ny’ and <b>c</b> says ‘ch’.",
        "<b>Doubled vowels are long</b> (<i>yeelen</i>); an <b>n</b> after a vowel makes it nasal, said a little through the nose (<i>kɔlɔn</i>).",
        "Words follow <b>Bambara</b> as spoken in Mali; Maninka and Dyula speakers say many of them a little differently."],
    phon_explain="Because N’Ko letters <b>join</b>, the third box shows the letter at the start, middle and end of a word, "
                 "plus the Latin letter used for the same sound in Bambara books.",
    standard="Bambara (Bamanankan) as spoken in Mali",
    hello=[
        ("Who speaks it?", "About <b>14 million people</b> speak Bambara as a first or second language, and many millions more speak its close "
                           "cousins Maninka, Dyula and Mandinka.<sup>³</sup>"),
        ("Where?", "Bambara is the most widely spoken language of <b>Mali</b>. Its Manding cousins are spoken in Guinea, Côte d’Ivoire, Burkina Faso, "
                   "Senegal, The Gambia and beyond."),
        ("How is it written?", "In the <b>N’Ko</b> script, from <b>right to left</b>, with joined letters. Bambara is also written in Latin letters."),
        ("How many letters?", "This book teaches <b>27 letters</b>: <b>7 vowels</b>, the humming <b>n</b> and <b>19 consonants</b>."),
        ("“I say”", "<b>N’Ko</b> means “I say” in all the Manding languages. The script was made in <b>1949</b> by the teacher Solomana Kanté in "
                    "Kankan, Guinea, so that Manding could be written in letters of its own."),
        ("Numbers too!", "N’Ko has its own digits, written from right to left: <span class='nt'>߁ ߂ ߃</span> are 1, 2, 3."),
    ],
    hello_pics=[("mosque", {}), ("nqo_kola", {}), ("mango", {})],
    chart_note="Read the alphabet from <b>right to left</b>, row by row — the same order as in this book.",
    map=region_map(frame=[[-18.0, 4.5], [0.5, 22.0]],
                   points=dict(bamako=[-8.00, 12.64], segou=[-6.27, 13.43], kankan=[-9.31, 10.38], sikasso=[-5.67, 11.32],
                               kayes=[-11.44, 14.45]),
                   area=(-8.0, 12.4, 120, 90), area_rot=0,
                   cities=[("bamako", "Bamako", 12, 8, "start", True), ("segou", "Ségou", 12, 8, "start", False),
                           ("kankan", "Kankan", 12, 8, "start", False), ("sikasso", "Sikasso", 12, 8, "start", False),
                           ("kayes", "Kayes", 12, -8, "start", False)],
                   label="WEST AFRICA", label_at=[-6.0, 18.5], marker=[-7.0, 13.0],
                   caption="The circle shows West Africa on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Bamako ★ is the capital of Mali. "
                          "The dashed line goes round the land where Bambara and its Manding cousins are spoken. N’Ko was first written "
                          "in Kankan.",
                   seas=[("Atlantic Ocean", -14.5, 7.0)], world_r=16),
    digits=[("߀", "ߛߌߝߌߙߌ", "sifiri", "zero"), ("߁", "ߞߋߟߋ߲", "kelen", "one"), ("߂", "ߝߌߟߊ", "fila", "two"),
            ("߃", "ߛߊߓߊ", "saba", "three"), ("߄", "ߣߊߣߌ", "naani", "four"), ("߅", "ߘߎߙߎ", "duuru", "five"),
            ("߆", "ߥߐߙߐ", "wɔɔrɔ", "six"), ("߇", "ߥߏߟߏ߲ߥߎߟߊ", "wolonwula", "seven"), ("߈", "ߛߋߜߌ߲", "seegin", "eight"),
            ("߉", "ߞߐߣߐ߲ߕߐ߲", "kɔnɔntɔn", "nine")],
    phrases=[("ߊߛߊߟߊߡߎ ߊߟߊߦߞߎߡ", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("ߥߊ ߊߟߊߦߞߎߡ ߛߊߟߊߡ", "wa ah-LAY-koom sah-LAHM", "And upon you be peace (the reply)"),
             ("ߒ ߕߐߜߐ ߦߋ …", "n taw-gaw yay …", "My name is …"),
             ("ߌ ߣߌ ߗߋ", "ee nee chay", "Thank you (and also: hello!)"),
             ("ߖߊߖߊߞߊߟߊߤߎ ߞߊߦߙߊ߲", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good (Bambara: Ala ka i sara)"),
             ("ߓߊ · ߝߊ", "bah · fah", "Mother · Father"),
             ("ߓߊߘߋ߲ߞߍ · ߓߊߘߋ߲ߡߎߛߏ", "bah-dayn-keh · bah-dayn-moo-soh", "Brother · Sister"),
             ("ߊߥߐ · ߊߦߌ", "ah-waw · ah-yee", "Yes · No"),
             ("ߒ ߓߍ ߓߊߡߊߣߊ߲ߞߊ߲ ߞߊߟߊ߲߹", "n beh bah-mah-nahn-kahn kah-lahn!", "I am learning Bambara!")],
    cheer=("ߡߊߛߊߟߊ߹ ߊ ߞߊ ߢߌ ߞߏߛߍߓߍ߹", "mah-shah-lah! ah kah nyee koh-seh-beh!", "Mashallah! Well done — very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International).",
    book_pic=dict(left="ߊ ߋ ߌ", right="ߓ ߔ ߕ"),
    review_note="N’Ko spelling: all words are written with every vowel (no repeated-vowel shortcut) and WITHOUT tone/length "
                "diacritics — a native N’Ko writer must add the correct tone marks (or confirm leaving them out) everywhere. "
                "Least certain words: ߔߐߡߎ pɔmu (apple) for ߔ; ߚߊߡߊߘߊ߲ Ramadan for ߚ (is ߚ the right letter?); ߗߌߞߍ cikɛ (farming) for ߗ; "
                "ߤߌߖߌ hiji (Hajj; or haji?); ߊߟߌߞߎߙߊߣߊ Alikurana (or Kurana); ߣߍߜߍ nɛgɛ (iron) with an anvil picture; ߒߕߏߡߌ ntomi "
                "(tamarind; o or ɔ?); ߛߌߝߌߙߌ sifiri (zero). Native labels to check: title ߒ ߓߍ ߒߞߏ ߞߊߟߊ߲, ߒߞߏ ߛߓߍߛߎ߲ (alphabet; the one "
                "word written with the repeated-vowel shortcut), ߖߊߕߋ jate (numbers), ߞߎߡߊ ߝߐߟߐ kuma fɔlɔ (first words), "
                "ߣߌ߲ ߜߊߝߋ ߦߋ ߒ ߕߊ ߦߋ (this book is mine), the cheer, and the Arabic phrases spelt in N’Ko (ߖߊߖߊߞߊߟߊߤߎ ߞߊߦߙߊ߲ has no ‘kh’ letter "
                "here — should it use a diacritic?). Speaker number (~14 million) to be confirmed.",
    tiles="ߊߓߕߞߡߣ", cover_pics=["mosque", "mango", "nqo_kola", "star"], title_size=50,
    speakers_blurb="Bambara is spoken by about 14 million people in Mali and West Africa, and N’Ko is its own right-to-left script.",
    sample_words=[("ߞߊߟߏ", "kalo", "moon"), ("ߘߏߟߏ", "dolo", "star"), ("ߡߊ߲ߜߏߙߏ", "mangoro", "mango")],
    keywords=["nko alphabet book for kids", "learn bambara for children", "n'ko letters coloring book",
              "manding bambara tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "mali west african heritage gift"],
))
