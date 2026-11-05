# -*- coding: utf-8 -*-
"""Book 49 - Khmer (Khmer script: 33 consonants + 9 independent vowels). Allamahul Bayan Series. REVIEW DRAFT.
Built with engine/generic.py: Khmer consonants come in two 'voices' (series), which the Indic builder's
single hidden vowel cannot show, so each consonant page shows its series and how it reads with the sign ា."""
from generic import build, letter, section, fontset
from maps import region_map

A_VOICE, O_VOICE = "a-voice", "o-voice"
SER_NATIVE = {A_VOICE: "សំឡេង អ", O_VOICE: "សំឡេង អូ"}


def K(ch, name_tr, voice, sound, word, tr, meaning, pic, aa_tr, args=None, note=None):
    """A consonant. aa_tr = how the consonant + the sign ា is read (it depends on the voice)."""
    hint = ("an <b>a-voice</b> letter: its hidden vowel is ‘a’ as in “father”" if voice == A_VOICE
            else "an <b>o-voice</b> letter: its hidden vowel is ‘o’, like the ‘aw’ in “saw”")
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">{ch} + ា = {ch}ា '
            f'<span class="tr" style="font-family:Nunito;font-size:14pt">({aa_tr})</span></div>'
            f'<div class="small">{hint} · <span class="nt">{SER_NATIVE[voice]}</span></div>')
    return letter(ch, ch, name_tr, sound, word, tr, meaning, pic, phon, "Khmer phonetics · voice", args, note)


def V(ch, name_tr, sound, like, word, tr, meaning, pic, args=None, note=None):
    """An independent vowel (ស្រៈពេញ). like = the consonant + vowel-sign spelling it sounds like."""
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">{ch} ~ {like}</div>'
            f'<div class="small">A <b>full vowel</b>: it stands alone and needs no consonant. '
            f'It sounds about the same as <span class="nt">{like}</span>.</div>')
    return letter(ch, ch, name_tr, sound, word, tr, meaning, pic, phon, "Khmer phonetics · full vowel", args, note)


RARE = ("<span class='nt'>{0}</span> is a rare letter, used in a few words that came from the old Pali and Sanskrit languages. "
        "In <span class='nt'>{1}</span> it hides as a little foot under <span class='nt'>{2}</span> — can you find it?")

CONSONANTS = [
    K("ក", "ka", A_VOICE, "‘k’ as in “skip” (no puff of air)", "កន្ត្រក", "kan-trak", "basket", "basket", "kaa"),
    K("ខ", "kha", A_VOICE, "‘k’ with a puff of air, as in “kite”", "ខ្មៅដៃ", "khmao-dai", "pencil", "km_pencil", "khaa"),
    K("គ", "ko", O_VOICE, "‘k’ as in “skip”, with the o-voice", "គ្រែ", "krae", "bed", "km_bed", "kea"),
    K("ឃ", "kho", O_VOICE, "‘k’ with a puff of air, with the o-voice", "ឃ្លោក", "khlouk", "bottle gourd", "km_gourd", "khea"),
    K("ង", "ngo", O_VOICE, "‘ng’ as in “sing” — Khmer words can start with it!", "ងងឹត", "ngo-ngut", "dark (at night)", "moon", "ngea"),
    K("ច", "cha", A_VOICE, "‘ch’ as in “chair”, but softer", "ចាន", "chaan", "plate", "plate", "chaa"),
    K("ឆ", "chha", A_VOICE, "‘ch’ with a puff of air", "ឆ័ត្រ", "chhat", "umbrella", "umbrella", "chhaa"),
    K("ជ", "cho", O_VOICE, "‘ch’ as in “chair”, with the o-voice", "ជណ្ដើរ", "chun-daeur", "ladder", "ladder", "chea"),
    K("ឈ", "chho", O_VOICE, "‘ch’ with a puff of air, with the o-voice", "ឈើ", "chheu", "wood, trees", "tree", "chhea"),
    K("ញ", "nyo", O_VOICE, "‘ny’ as in “canyon”", "ញញួរ", "nyo-nyuor", "hammer", "tools", "nyea"),
    K("ដ", "da", A_VOICE, "‘d’ as in “day”", "ដូង", "doung", "coconut", "coconut", "daa"),
    K("ឋ", "tha", A_VOICE, "‘t’ with a puff of air — a rare letter", "សណ្ឋាគារ", "son-thaa-kia", "hotel", "building", "thaa",
      note=RARE.format("ឋ", "សណ្ឋាគារ", "ណ")),
    K("ឌ", "do", O_VOICE, "‘d’ as in “day”, with the o-voice — a rare letter", "មណ្ឌល", "mon-dol", "centre (a meeting place)", "house", "dea",
      note=RARE.format("ឌ", "មណ្ឌល", "ណ")),
    K("ឍ", "tho", O_VOICE, "‘t’ with a puff of air, with the o-voice — a rare letter", "វឌ្ឍនៈ", "vot-tha-nak", "growing, getting bigger", "paddy", "thea",
      note=RARE.format("ឍ", "វឌ្ឍនៈ", "ឌ")),
    K("ណ", "na", A_VOICE, "‘n’ as in “net” — almost never at the start of a word", "អណ្ដូង", "an-doung", "well (for water)", "well", "naa",
      note="Find <span class='nt'>ណ</span> in the middle of <span class='nt'>អណ្ដូង</span>!"),
    K("ត", "ta", A_VOICE, "‘t’ as in “stop” (no puff of air)", "តុ", "tok", "table", "km_table", "taa"),
    K("ថ", "tha", A_VOICE, "‘t’ with a puff of air, as in “top”", "ថ្ម", "thmaa", "stones", "km_stones", "thaa"),
    K("ទ", "to", O_VOICE, "‘t’ as in “stop”, with the o-voice", "ទឹក", "tuk", "water", "water", "tea"),
    K("ធ", "tho", O_VOICE, "‘t’ with a puff of air, with the o-voice", "ធុរេន", "thu-reen", "durian (a spiky fruit)", "km_durian", "thea"),
    K("ន", "no", O_VOICE, "‘n’ as in “net”", "នាឡិកា", "nea-li-kaa", "clock", "clock", "nea"),
    K("ប", "ba", A_VOICE, "‘b’ as in “ball”", "បង្អួច", "bang-uoch", "window", "window", "baa"),
    K("ផ", "pha", A_VOICE, "‘p’ with a puff of air, as in “pen”", "ផ្កា", "phkaa", "flower", "flower", "phaa"),
    K("ព", "po", O_VOICE, "‘p’ as in “spin” (no puff of air)", "ពង", "pong", "egg", "egg", "pea"),
    K("ភ", "pho", O_VOICE, "‘p’ with a puff of air, with the o-voice", "ភ្នំ", "phnum", "mountain", "mountain", "phea"),
    K("ម", "mo", O_VOICE, "‘m’ as in “moon”", "ម្នាស់", "mnoas", "pineapple", "pineapple", "mea"),
    K("យ", "yo", O_VOICE, "‘y’ as in “yes”", "យន្តហោះ", "yon-hoh", "aeroplane", "plane", "yea"),
    K("រ", "ro", O_VOICE, "a light rolled ‘r’", "រទេះ", "ro-teh", "cart", "cart", "rea"),
    K("ល", "lo", O_VOICE, "‘l’ as in “lamp”", "ល្ពៅ", "l-pov", "pumpkin", "km_pumpkin", "lea"),
    K("វ", "vo", O_VOICE, "‘v’ or ‘w’ — between the two", "វ៉ែនតា", "vaen-taa", "glasses", "glasses", "vea"),
    K("ស", "sa", A_VOICE, "‘s’ as in “sun”", "សៀវភៅ", "siev-phov", "book", "book", "saa", args=dict(left="ក ខ គ", right="ឃ ង ច")),
    K("ហ", "ha", A_VOICE, "‘h’ as in “hat”", "ហិប", "hep", "chest, box", "box", "haa"),
    K("ឡ", "la", A_VOICE, "‘l’ as in “lamp”, with the a-voice", "ឡាន", "laan", "car", "km_car", "laa"),
    K("អ", "a", A_VOICE, "a little catch in the throat, then the vowel — like the start of “uh-oh”", "អំពូល", "am-pul", "light bulb", "bulb", "aa",
      note="<span class='nt'>អ</span> also carries vowel signs at the start of a word: <span class='nt'>អា អិ អី អុ</span>…"),
]

VOWELS = [
    V("ឥ", "e", "a short ‘e’, like the ‘i’ in “bit”", "អិ", "ឥដ្ឋ", "et", "brick", "brick"),
    V("ឦ", "ei", "‘ei’ as in “eight”", "អី", "ឦសាន", "ei-saan", "north-east (on a compass)", "km_compass"),
    V("ឧ", "o", "a short ‘o’ as in “book”", "អុ", "ឧបករណ៍", "u-pa-kaa", "tools", "tools"),
    V("ឪ", "euv", "‘euv’ — say ‘uh’ and round your lips into ‘oo’", "អៅ", "ឪឡឹក", "euv-luek", "watermelon", "watermelon"),
    V("ឫ", "ru", "‘ru’ with a short ‘u’ said with flat lips", "រឹ", "ឫស្សី", "rue-sey", "bamboo", "km_bamboo"),
    V("ឬ", "rue", "‘rue’ — a long ‘u’ said with flat lips", "រឺ", "ប៉ោម ឬ ចេក?", "paom rue chek?", "an apple or a banana? (ឬ means “or”)",
      "km_apple_or_banana", note="<span class='nt'>ឬ</span> is a whole word by itself: it means “or”."),
    V("ឮ", "lue", "‘lue’ — a long ‘u’ said with flat lips", "លឺ", "ឮ", "lue", "to hear (the bell)", "km_bell",
      note="<span class='nt'>ឮ</span> is a whole word by itself: it means “to hear”."),
    V("ឯ", "ae", "‘ae’ — like the ‘a’ in “cat”, said long", "អែ", "ឯក", "aek", "one, alone", "one", args=dict(digit="១")),
    V("ឱ", "ao", "‘ao’ as in “now”, said with rounded lips", "អោ", "ឱសថ", "ao-sot", "medicine", "medicine"),
]

LANG = build(dict(
    code="km", folder="book-49-khmer", series_no=49, isbn="", draft=True,
    name="Khmer", native="ខ្មែរ", native_tr="khmae", name_word="ឈ្មោះ", write_word="សរសេរ",
    title_native="អក្ខរក្រមខ្មែរដំបូងរបស់ខ្ញុំ", title_letters="កខគឃងច", belongs_native="សៀវភៅនេះជារបស់",
    belongs_pic="km_bamboo", alphabet_native="អក្ខរក្រម", numbers_native="លេខ", numbers_tr="lekh",
    phrases_native="ពាក្យដំបូង",
    fonts=fontset("Kantumruy Pro", "kantumruy-pro-khmer", "Noto Sans Khmer", "noto-sans-khmer-khmer"),
    disp_family="Kantumruy Pro", text_family="Noto Sans Khmer",
    glyph_font=["noto-sans-khmer-khmer-800-normal.woff2"],
    font_credit="Noto Sans Khmer, Kantumruy Pro",
    phon_feature="Khmer phonetics: each consonant’s <i>voice</i> (a-voice or o-voice) and how it reads with a vowel sign",
    sections=[
        section(CONSONANTS, label="CONSONANT", chip="PART 1", title="The Consonants", native="ព្យញ្ជនៈ",
                native_tr="pyun-chea-nak — the 33 consonants", chart_title="consonants", chart_cols=7, warmup_cols=6,
                warmup_title="the consonants",
                intro_html="""<p>Khmer children first learn the <b>33 consonants</b>, in the same order as this book:
<span class="nt">ក ខ គ ឃ ង</span> <i>ka, kha, ko, kho, ngo</i>…</p>
<div class="box" style="margin:0.1in 0"><h3>Two voices</h3>Every consonant carries a hidden vowel. Some carry <b>‘a’</b>
(as in “father”) — the <b>a-voice</b> letters, like <span class="nt">ក</span> <i>ka</i>. Others carry <b>‘o’</b> (like “aw” in “saw”)
— the <b>o-voice</b> letters, like <span class="nt">គ</span> <i>ko</i>. The voice changes how a vowel sign is read:
<div class="nt" style="font-size:20pt;text-align:center;margin-top:4px">ក + ា = កា <span class="tr" style="font-family:Nunito;font-size:13pt">(kaa)</span>
&nbsp;·&nbsp; គ + ា = គា <span class="tr" style="font-family:Nunito;font-size:13pt">(kea)</span></div></div>
<div class="box" style="margin:0.1in 0"><h3>Pairs</h3>Many sounds come in pairs, one of each voice:
<span class="nt">ក/គ ខ/ឃ ច/ជ ឆ/ឈ ដ/ឌ ត/ទ ថ/ធ ប/ព ផ/ភ ស ហ ឡ អ</span>. Listen for the voice!</div>
<div class="box"><h3>Letters with feet</h3>When two consonants sit together with no vowel between them, the second one shrinks and
hangs <b>under</b> the first as a little “foot” (<span class="nt">ជើង</span> <i>cheung</i>): <span class="nt">ក + ្ក = ក្ក</span>.
You will see feet in many words in this book, like <span class="nt">ផ្កា</span> <i>phkaa</i> (flower).</div>"""),
        section(VOWELS, label="VOWEL", chip="PART 2", title="The Full Vowels", native="ស្រៈពេញ",
                native_tr="srak penh — “full vowels”", chart_title="full vowels", chart_cols=9, warmup_cols=5,
                warmup_title="the full vowels",
                intro_html="""<p>Most Khmer vowels are small <b>vowel signs</b> written around a consonant: above, below, before or after it —
<span class="nt">កា កិ កី កុ កូ កេ កែ កោ</span>… There are more than twenty of them, and each one sounds a little different with an
a-voice or an o-voice consonant.</p>
<div class="box" style="margin:0.1in 0"><h3>Full vowels</h3>A few vowels also have a <b>full letter</b> of their own, called
<span class="nt">ស្រៈពេញ</span> <i>srak penh</i>. A full vowel stands alone: it never needs a consonant. This book teaches the
<b>9 full vowels</b> children meet most often: <span class="nt" style="font-size:16pt">ឥ ឦ ឧ ឪ ឫ ឬ ឮ ឯ ឱ</span></div>
<div class="box"><h3>Sounds like…</h3>Each full vowel sounds about the same as <span class="nt">អ</span> (or <span class="nt">រ, ល</span>) with
a vowel sign: <span class="nt">ឥ ~ អិ</span>, <span class="nt">ឯ ~ អែ</span>, <span class="nt">ឫ ~ រឹ</span>. A few more full vowels
(<span class="nt">ឩ ឭ ឰ ឳ</span>) are found only in a handful of old words.</div>"""),
    ],
    letters_word="Letters",
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>a-voice and o-voice:</b> <i>ka</i> has the ‘a’ of “father”; <i>ko</i> has an open ‘o’, like the ‘aw’ in “saw”.",
        "<b>h after a letter</b> (<i>kh, chh, th, ph</i>) means “add a puff of breath”. Without the h (<i>k, ch, t, p</i>) say it "
        "with <b>no</b> puff, as in “skip”, “stop”, “spin”. <i>th</i> is never the English “th” of “the”.",
        "<b>ea</b> is said like “ee-uh” run together: <span class='nt'>គា</span> <i>kea</i> sounds like “kee-uh”.",
        "<b>eu / ue</b> is an ‘oo’ said with flat, smiling lips."],
    phon_explain="The box marked <i>Khmer phonetics</i> shows whether a consonant is an <b>a-voice</b> or <b>o-voice</b> letter, and how "
                 "it reads with the vowel sign <span class='nt'>ា</span>: <span class='nt'>ក + ា = កា</span> <i>kaa</i>, but "
                 "<span class='nt'>គ + ា = គា</span> <i>kea</i>. For a full vowel it shows the spelling it sounds like.",
    standard="the standard Khmer of Phnom Penh",
    hello=[
        ("Who speaks it?", "About <b>18 million people</b> speak Khmer.<sup>³</sup> It is the language of <b>Cambodia</b>."),
        ("Where?", "In <b>Cambodia</b>, on the great <b>Mekong River</b>, and in nearby parts of Thailand and Vietnam, and by "
                   "Khmer families around the world."),
        ("How is it written?", "In the <b>Khmer script</b>, from <b>left to right</b>. Words in a sentence are usually written "
                               "<b>without spaces</b> between them!"),
        ("How many letters?", "This book teaches <b>42</b>: the <b>33 consonants</b> and <b>9 full vowels</b>. Khmer also has more "
                              "than twenty small vowel signs."),
        ("A very old script", "Khmer writing has been carved on stone for more than <b>1,300 years</b>. It is one of the oldest "
                              "scripts of Southeast Asia."),
        ("Did you know?", "Cambodia’s <b>Tonle Sap</b> lake grows to several times its size in the rainy season, when the "
                          "Mekong pushes water back up the river into it!"),
    ],
    hello_pics=[("km_bamboo", {}), ("paddy", {}), ("coconut", {})],
    map=region_map(frame=[[99.5, 7.5], [110.5, 18.5]],
                   points=dict(phnompenh=[104.92, 11.56], siemreap=[103.86, 13.36], battambang=[103.20, 13.10],
                               sihanoukville=[103.53, 10.63], kampongcham=[105.46, 11.99]),
                   area=(104.9, 12.6, 300, 230), area_rot=-8,
                   cities=[("phnompenh", "Phnom Penh", 16, 30, "start", True), ("siemreap", "Siem Reap", 14, -12, "start", False),
                           ("battambang", "Battambang", -14, 8, "end", False), ("sihanoukville", "Sihanoukville", -14, 8, "end", False),
                           ("kampongcham", "Kampong Cham", 14, -10, "start", False)],
                   label="CAMBODIA", label_at=[105.4, 14.6], marker=[104.9, 12.5],
                   caption="The circle shows Cambodia on the world map.",
                   legend="<b>Color it:</b> the land where Khmer is spoken (inside the dashed line) <b>yellow</b> · the rest of the "
                          "land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Phnom Penh ★ sits where the rivers meet. Draw the "
                          "big <b>Mekong River</b> flowing south to the sea!",
                   seas=[("Gulf of Thailand", 101.6, 9.6)]),
    digits=[("០", "សូន្យ", "soun", "zero"), ("១", "មួយ", "muoy", "one"), ("២", "ពីរ", "pii", "two"), ("៣", "បី", "bei", "three"),
            ("៤", "បួន", "buon", "four"), ("៥", "ប្រាំ", "pram", "five"), ("៦", "ប្រាំមួយ", "pram-muoy", "six"),
            ("៧", "ប្រាំពីរ", "pram-pii", "seven"), ("៨", "ប្រាំបី", "pram-bei", "eight"), ("៩", "ប្រាំបួន", "pram-buon", "nine")],
    phrases=[("អាស្សាឡាមូអាឡៃកុំ", "as-sa-laa-mu a-lai-kum", "Peace be upon you (the Muslim greeting)"),
             ("វ៉ាអាឡៃកុំអាស្សាឡាម", "wa a-lai-kum as-sa-laam", "And upon you be peace (the reply)"),
             ("ខ្ញុំឈ្មោះ …", "khnyom chhmuoh …", "My name is …"),
             ("អរគុណ", "aw-kun", "Thank you"),
             ("ជ៉ាហ្សាកាល់ឡោះហ៊ូខៃរ៉ន", "ja-zaa-kal-laa-hu khai-ran", "May Allah reward you with good"),
             ("ម្ដាយ · ឪពុក", "m-daay · euv-puk", "Mother · Father"),
             ("បងប្រុស · បងស្រី", "bong pros · bong srey", "Brother · Sister (older)"),
             ("បាទ / ចាស · ទេ", "baat / chaas · te", "Yes (a boy / a girl says) · No"),
             ("ខ្ញុំកំពុងរៀនភាសាខ្មែរ!", "khnyom kom-pung rien phea-saa khmae!", "I am learning Khmer!")],
    cheer=("ម៉ាស្ហាអល់ឡោះ! ពូកែណាស់!", "maa-shaa-al-loh! puu-kae nah!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="ក ខ គ", right="ឃ ង ច"),
    review_note="Khmer is a REVIEW DRAFT. Please check: the romanized letter names (ka/ko style) and the a-voice/o-voice "
                "readings with ា (kaa / kea); the words for the rare letters ឋ (សណ្ឋាគារ), ឌ (មណ្ឌល) and ឍ (វឌ្ឍនៈ); "
                "the choice of 9 full vowels and their words (ឦសាន, ឬ, ឮ); and the Khmer spellings of the Arabic phrases "
                "(Assalamu alaikum, Jazakallahu khairan, Mashallah) as Cambodian Muslims write them.",
    tiles="កខគងចអ", cover_pics=["coconut", "pineapple", "km_bamboo", "flower"], title_size=50,
    speakers_blurb="Khmer is the language of Cambodia, spoken by about 18 million people.",
    sample_words=[("ផ្កា", "phkaa", "flower"), ("ម្នាស់", "mnoas", "pineapple"), ("ភ្នំ", "phnum", "mountain")],
    keywords=["khmer alphabet book for kids", "learn khmer for children", "cambodian language coloring book",
              "khmer letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "khmer heritage language gift"],
))
