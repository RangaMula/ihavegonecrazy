# -*- coding: utf-8 -*-
"""Book 2 - Hindi (Devanagari). Allamahul Bayan Series.
House rules: objects/plants/nature only; script + transliteration + English; cite every ayah.
Transliteration: simple English letters, doubled vowels = long (aa, ee, oo); final silent 'a' dropped.
"""
from series import indic_vowel

V = lambda letter, name_tr, sound, sign, sname, ex, ex_tr, word, tr, meaning, pic, args=None, name=None: dict(
    letter=letter, name_native=name or letter, name_en=name_tr, sound=sound,
    phon_label="Hindi phonetics · vowel sign (मात्रा)",
    phon=indic_vowel(sign, sname, ex, ex_tr, "क") or
         '<div style="font-size:11.5pt">No sign! <span class="nt">अ</span> hides inside every consonant: <span class="nt">क = क् + अ</span></div>',
    word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {})

def C(letter, name_tr, sound, word, tr, meaning, pic, phon=None, note=None, args=None, name=None):
    return dict(letter=letter, name_native=name or letter, name_en=name_tr, sound=sound,
                phon_label="Hindi phonetics · उच्चारण",
                phon=f'<div class="nt" style="font-size:19pt">{phon or (letter + "् + अ = " + letter)}</div>',
                note=note, word=word, translit=tr, meaning=meaning, pic=pic, pic_args=args or {})

VOWELS = [
    V("अ", "a", "a short ‘a’ as in “about”", "", "", "", "", "अनार", "anaar", "pomegranate", "pomegranate"),
    V("आ", "aa", "‘aa’ as in “father”", "ा", "आ की मात्रा", "का", "kaa", "आम", "aam", "mango", "mango"),
    V("इ", "i", "‘i’ as in “sit” — short", "ि", "इ की मात्रा", "कि", "ki", "इमली", "imlee", "tamarind", "tamarind"),
    V("ई", "ee", "‘ee’ as in “see” — long", "ी", "ई की मात्रा", "की", "kee", "ईद", "eed", "Eid, the festival day", "eid"),
    V("उ", "u", "‘u’ as in “put” — short", "ु", "उ की मात्रा", "कु", "ku", "उपहार", "uphaar", "gift", "gift"),
    V("ऊ", "oo", "‘oo’ as in “moon” — long", "ू", "ऊ की मात्रा", "कू", "koo", "ऊन", "oon", "wool", "wool"),
    V("ऋ", "ri", "‘ri’ as in “ring”", "ृ", "ऋ की मात्रा", "कृ", "kri", "ऋतु", "ritu", "season", "seasons"),
    V("ए", "e", "‘e’ as in “they” (say “ay”)", "े", "ए की मात्रा", "के", "ke", "एक", "ek", "one", "one", dict(digit="१")),
    V("ऐ", "ai", "‘ai’ — like the ‘a’ in “bat”, said long", "ै", "ऐ की मात्रा", "कै", "kai", "ऐनक", "ainak", "glasses", "glasses"),
    V("ओ", "o", "‘o’ as in “go”", "ो", "ओ की मात्रा", "को", "ko", "ओखली", "okhlee", "mortar (for grinding spices)", "mortar"),
    V("औ", "au", "‘au’ — like the ‘aw’ in “saw”", "ौ", "औ की मात्रा", "कौ", "kau", "औज़ार", "auzaar", "tools", "tools"),
    V("अं", "an", "a nasal ‘n’ or ‘m’ after the vowel, as in “aunt”", "ं", "अनुस्वार", "कं", "kan", "अंगूर", "angoor", "grapes", "grapes",
      name="अं (अनुस्वार)"),
    V("अः", "ah", "a short breath ‘h’ after the vowel", "ः", "विसर्ग", "कः", "kah", "प्रातः", "praatah", "early morning", "sunrise",
      name="अः (विसर्ग)"),
]

CONSONANTS = [
    C("क", "ka", "‘k’ as in “kite”", "कलम", "kalam", "pen", "pen"),
    C("ख", "kha", "‘k’ with a puff of air — say “k” strongly", "खजूर", "khajoor", "dates", "dates"),
    C("ग", "ga", "‘g’ as in “go”", "गाजर", "gaajar", "carrot", "carrot"),
    C("घ", "gha", "‘g’ with a breath, as in “doghouse”", "घड़ी", "ghadee", "clock", "clock"),
    C("ङ", "nga", "‘ng’ as in “sing” — a rare letter", "रङ्ग", "rang", "colour", "palette",
      note='Today <span class="nt">रङ्ग</span> is usually written <span class="nt">रंग</span>, with a dot instead of <span class="nt">ङ</span>.'),
    C("च", "cha", "‘ch’ as in “chair”", "चाँद", "chaand", "moon", "moon"),
    C("छ", "chha", "‘ch’ with a puff of air", "छाता", "chhaataa", "umbrella", "umbrella"),
    C("ज", "ja", "‘j’ as in “jam”", "जहाज़", "jahaaz", "ship", "ship"),
    C("झ", "jha", "‘j’ with a breath, as in “hedgehog”", "झाड़ू", "jhaadoo", "broom", "broom"),
    C("ञ", "nya", "a soft ‘n’ made near the roof of the mouth, as in “pinch” — a rare letter", "अञ्जीर", "anjeer", "fig", "fig",
      note='Today <span class="nt">अञ्जीर</span> is usually written <span class="nt">अंजीर</span>.'),
    C("ट", "ta", "a hard ‘t’ — curl your tongue back, as in “top”", "टमाटर", "tamaatar", "tomato", "tomato"),
    C("ठ", "tha", "a hard ‘t’ with a puff of air (not the ‘th’ of “the”)", "ठेला", "thelaa", "push-cart", "cart"),
    C("ड", "da", "a hard ‘d’ — curl your tongue back, as in “dog”", "डाक", "daak", "post, letters", "envelope"),
    C("ढ", "dha", "a hard ‘d’ with a breath", "ढक्कन", "dhakkan", "lid", "jar"),
    C("ण", "na", "‘n’ with the tongue curled back — never at the start of a word", "बाण", "baan", "arrow", "bowarrow",
      note='Look for <span class="nt">ण</span> at the end of <span class="nt">बाण</span>!', name="ण (मूर्धन्य)"),
    C("त", "ta", "a soft ‘t’ — tongue touches the back of the teeth", "तरबूज़", "tarbooz", "watermelon", "watermelon"),
    C("थ", "tha", "a soft ‘t’ with a puff of air (not the ‘th’ of “think”)", "थाली", "thaalee", "plate", "plate"),
    C("द", "da", "a soft ‘d’ — tongue touches the back of the teeth", "दरवाज़ा", "darvaazaa", "door", "door"),
    C("ध", "dha", "a soft ‘d’ with a breath", "धान", "dhaan", "rice plant (paddy)", "paddy"),
    C("न", "na", "‘n’ as in “net”", "नाव", "naav", "boat", "boat"),
    C("प", "pa", "‘p’ as in “pen”", "पतंग", "patang", "kite", "kite"),
    C("फ", "pha", "‘p’ with a puff of air", "फूल", "phool", "flower", "flower"),
    C("ब", "ba", "‘b’ as in “ball”", "बादल", "baadal", "clouds", "clouds"),
    C("भ", "bha", "‘b’ with a breath, as in “abhor”", "भुट्टा", "bhuttaa", "corn cob", "corn"),
    C("म", "ma", "‘m’ as in “moon”", "मस्जिद", "masjid", "mosque", "mosque"),
    C("य", "ya", "‘y’ as in “yes”", "यंत्र", "yantra", "machine", "gears"),
    C("र", "ra", "a tapped ‘r’ — flick the tongue once", "रोटी", "rotee", "flatbread (roti)", "roti"),
    C("ल", "la", "‘l’ as in “lamp”", "लट्टू", "lattoo", "spinning top", "top"),
    C("व", "va", "between ‘v’ and ‘w’, as in “van”", "वर्षा", "varshaa", "rain", "raincloud"),
    C("श", "sha", "‘sh’ as in “shoe”", "शहद", "shahad", "honey", "honey"),
    C("ष", "sha", "‘sh’ with the tongue curled back", "षट्कोण", "shatkon", "hexagon", "hexagon", name="ष (मूर्धन्य)"),
    C("स", "sa", "‘s’ as in “sun”", "सूरज", "sooraj", "sun", "sun"),
    C("ह", "ha", "‘h’ as in “hat”", "हाँडी", "haandee", "clay pot", "pot"),
    C("ड़", "ṛa", "a quick flapped ‘r’ — never at the start of a word", "पहाड़", "pahaad", "mountain", "mountain",
      phon="ड + ़ (dot) = ड़", note='Look for <span class="nt">ड़</span> at the end of <span class="nt">पहाड़</span>!'),
    C("ढ़", "ṛha", "a flapped ‘r’ with a breath — never at the start of a word", "सीढ़ी", "seedhee", "ladder", "ladder",
      phon="ढ + ़ (dot) = ढ़", note='Find <span class="nt">ढ़</span> in the middle of <span class="nt">सीढ़ी</span>!'),
    C("क्ष", "ksha", "‘k’ + ‘sh’ said together", "अक्षर", "akshar", "letter", "blocks", phon="क् + ष = क्ष",
      note='Find <span class="nt">क्ष</span> in the middle of <span class="nt">अक्षर</span>!', args=dict(letters=("अ", "आ", "क"))),
    C("त्र", "tra", "‘t’ + ‘r’ said together", "त्रिभुज", "tribhuj", "triangle", "triangle", phon="त् + र = त्र"),
    C("ज्ञ", "gya", "said ‘gya’ in Hindi", "ज्ञान", "gyaan", "knowledge", "book", phon="ज् + ञ = ज्ञ",
      args=dict(left="अ आ इ", right="क ख ग")),
]

_vrows = "".join(f'<tr><td class="ntd" style="font-size:20pt">{v["letter"]}</td><td class="tr">{v["name_en"]}</td></tr>' for v in VOWELS[:0])
_table = "".join(
    f'<tr><td class="ntd" style="font-size:20pt">{l}</td><td class="tr">{n}</td><td class="nt" style="font-size:15pt">{s}</td>'
    f'<td class="nt" style="font-size:15pt">{e}</td><td class="tr">{t}</td></tr>'
    for l, n, s, e, t in [("अ", "a", "—", "क", "ka"), ("आ", "aa", "◌ा", "का", "kaa"), ("इ", "i", "◌ि", "कि", "ki"),
                          ("ई", "ee", "◌ी", "की", "kee"), ("उ", "u", "◌ु", "कु", "ku"), ("ऊ", "oo", "◌ू", "कू", "koo"),
                          ("ऋ", "ri", "◌ृ", "कृ", "kri"), ("ए", "e", "◌े", "के", "ke"), ("ऐ", "ai", "◌ै", "कै", "kai"),
                          ("ओ", "o", "◌ो", "को", "ko"), ("औ", "au", "◌ौ", "कौ", "kau"), ("अं", "an", "◌ं", "कं", "kan"),
                          ("अः", "ah", "◌ः", "कः", "kah")])

FONTS = [("Baloo 2", 400, "normal", "baloo-2-devanagari-400-normal.woff2", None),
         ("Baloo 2", 700, "normal", "baloo-2-devanagari-700-normal.woff2", None),
         ("Baloo 2", 800, "normal", "baloo-2-devanagari-800-normal.woff2", None),
         ("Noto Sans Devanagari", 400, "normal", "noto-sans-devanagari-devanagari-400-normal.woff2", None),
         ("Noto Sans Devanagari", 700, "normal", "noto-sans-devanagari-devanagari-700-normal.woff2", None)]

LANG = dict(
    code="hi", folder="book-02-hindi", series_no=2, isbn="",
    name="Hindi", native="हिन्दी", native_tr="hindee", name_word="नाम", write_word="लिखो",
    title="My First Hindi Alphabet", title_native="मेरी पहली हिंदी वर्णमाला",
    subtitle="A Coloring Book to Learn, Trace & Say the 51 Hindi Letters with English Phonetics",
    title_letters="अआइकखग", belongs_native="यह किताब मेरी है", belongs_pic="kite",
    alphabet_native="वर्णमाला", numbers_native="अंक", numbers_tr="ank", phrases_native="पहले शब्द",
    fonts=FONTS, disp_family="Baloo 2", text_family="Noto Sans Devanagari",
    glyph_font="baloo-2-devanagari-800-normal.woff2", font_credit="Baloo 2, Noto Sans Devanagari",
    series_line="<b>Book 2 is Hindi</b> — the most widely spoken language of India. "
                "More languages of the subcontinent are in the series, in shā’ Allāh.",
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>a</b> is the short sound in “about”. Every Hindi consonant carries it: <span class='nt'>क</span> = <i>ka</i>. "
        "At the end of a word it is usually silent: <span class='nt'>कलम</span> is <i>kalam</i>, not <i>kalama</i>.",
        "<b>h after a letter</b> (<i>kh, gh, th, dh, bh</i>) means “add a puff of breath” — hold a tissue in front of your mouth "
        "and watch it move! It never means the English “th” of “the”.",
        "<b>Hard and soft t / d:</b> for the <i>hard</i> ones (<span class='nt'>ट ठ ड ढ</span>) curl the tongue back; for the "
        "<i>soft</i> ones (<span class='nt'>त थ द ध</span>) touch the back of your top teeth.",
        "<b>A dot under a letter</b> (<span class='nt'>ज़ फ़ क़ ख़</span>) gives sounds borrowed from Arabic and Persian: "
        "<i>z, f, q, kh</i>, as in <span class='nt'>जहाज़</span> <i>jahaaz</i>."],
    phon_explain="The box marked <i>Hindi phonetics</i> shows how the sound is built the way Hindi children learn it, "
                 "for example <span class='nt'>क् + अ = क</span>, or the vowel sign (<i>maatraa</i>) <span class='nt'>क + ा = का</span>.",
    standard="standard Hindi as spoken in north India",
    hello=[
        ("Who speaks it?", "More than <b>600 million people</b> speak Hindi as a first or second language — one of the three most spoken languages in the world.<sup>³</sup>"),
        ("Where?", "Hindi is an official language of <b>India</b>, spoken most in the north and centre. It is also spoken in <b>Nepal</b>, <b>Fiji</b>, <b>Mauritius</b> and by families all over the world."),
        ("How is it written?", "In the <b>Devanagari</b> script, from <b>left to right</b>. Letters hang from a line along the top called <span class='nt'>शिरोरेखा</span> <i>(shirorekhaa)</i>."),
        ("How many letters?", "This book teaches <b>51</b>: <b>13 vowels</b> (<span class='nt'>स्वर</span> <i>svar</i>) and <b>38 consonants</b> "
                              "(<span class='nt'>व्यंजन</span> <i>vyanjan</i>), including the joined letters <span class='nt'>क्ष त्र ज्ञ</span>."),
        ("Cousins: Hindi and Urdu", "In everyday talk, Hindi and Urdu are so close that speakers understand each other easily — but Hindi is written in Devanagari and Urdu in a Perso-Arabic script."),
        ("A day for Hindi", "On <b>14 September 1949</b> Hindi was chosen as an official language of India. The day is remembered every year as <b>Hindi Diwas</b>.<sup>³</sup>"),
    ],
    hello_pics=[("kite", {}), ("mango", {}), ("mosque", {})],
    chart_note="Read the alphabet left to right, row by row — the same order as in this book.",
    map=dict(
        frame=[[67.5, 7.0], [93.0, 34.0]], land=True,
        points=dict(delhi=[77.21, 28.61], lucknow=[80.95, 26.85], patna=[85.14, 25.59], jaipur=[75.79, 26.91],
                    bhopal=[77.41, 23.26], india=[78.5, 19.5], arabian=[69.5, 15.0], bay=[88.0, 15.0], ocean=[80.0, 7.8]),
        cities=[("delhi", "New Delhi", 18, 8, "start", True), ("lucknow", "Lucknow", 14, 8, "start", False),
                ("patna", "Patna", 14, 8, "start", False), ("jaipur", "Jaipur", -14, 8, "end", False),
                ("bhopal", "Bhopal", 14, 8, "start", False)],
        labels=[("india", "INDIA", 40, False), ("arabian", "Arabian Sea", 30, True), ("bay", "Bay of Bengal", 30, True)],
        world_marker=[79.0, 22.0], world_r=16, world_caption="The circle shows India on the world map.",
        legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Hindi is spoken most in the north and "
               "centre of India — around New Delhi ★ (India’s capital), Jaipur, Lucknow, Bhopal and Patna. "
               "Draw a little heart next to each city!"),
    sections=[
        dict(key="vowels", label="VOWEL", chip="PART 1", title="The Vowels", native="स्वर", native_tr="svar — “voice letters”",
             chart_title="vowels", chart_cols=7, warmup_title="the vowels", warmup_cols=4,
             intro_html=f"""<p>Vowels are the sounds you make with your mouth open: <i>a, aa, i, ee, u, oo…</i> Hindi has <b>13</b> in this book
(11 vowels and the two special signs <span class="nt">अं</span> and <span class="nt">अः</span>).</p>
<p>A vowel has <b>two shapes</b>. At the start of a word it is a full letter (<span class="nt">आ</span>). After a consonant it becomes a
small sign called a <b><i>maatraa</i></b> (<span class="nt">◌ा</span>): <span class="nt">क + ा = का</span> <i>(kaa)</i>.
The <span class="nt">ि</span> sign is written <i>before</i> its letter, even though it is said after it!</p>
<table style="width:100%;border-collapse:collapse;margin-top:0.08in;text-align:center" class="vt">
<tr style="font:600 10.5pt Fredoka"><th>Vowel</th><th>Name</th><th>Sign</th><th>With <span class="nt">क</span></th><th>Say</th></tr>{_table}</table>
<style>.vt td,.vt th{{border-bottom:1.5px solid #bbb;padding:1px 4px}}</style>""",
             items=VOWELS),
        dict(key="consonants", label="CONSONANT", chip="PART 2", title="The Consonants", native="व्यंजन", native_tr="vyanjan",
             chart_title="consonants", chart_cols=7, warmup_title="the consonants", warmup_cols=6,
             intro_html="""<p>Consonants are the sounds made by stopping or squeezing the air: <i>k, g, ch, j, t, d, p, b…</i>
This book has <b>38</b>: the 33 main consonants, two flapped letters (<span class="nt">ड़ ढ़</span>) and three joined letters.</p>
<div class="box" style="margin:0.1in 0"><h3>The hidden vowel</h3>Every consonant secretly carries the vowel <span class="nt">अ</span> <i>(a)</i>. That is why
<span class="nt">क</span> is said <i>ka</i>, not just <i>k</i>:
<div class="nt" style="font-size:22pt;text-align:center;margin-top:2px">क् + अ = क</div>
<div style="text-align:center"><i>k + a = ka</i> — the little slanting mark <span class="nt">्</span> (<i>halant</i>) means “no vowel”.</div></div>
<div class="box" style="margin:0.1in 0"><h3>Families of five</h3>The first 25 consonants come in five families, each made in a different part of the mouth:
<div class="nt" style="font-size:17pt;line-height:1.6;margin-top:4px">क ख ग घ ङ — <span class="small" style="font-family:Nunito">back of the throat</span><br>
च छ ज झ ञ — <span class="small" style="font-family:Nunito">middle of the tongue</span><br>ट ठ ड ढ ण — <span class="small" style="font-family:Nunito">tongue curled back (hard)</span><br>
त थ द ध न — <span class="small" style="font-family:Nunito">tongue on the teeth (soft)</span><br>प फ ब भ म — <span class="small" style="font-family:Nunito">the lips</span></div></div>
<div class="box"><h3>Joined letters</h3><span class="nt">क्ष त्र ज्ञ</span> are two consonants written as one: <span class="nt">क् + ष = क्ष</span>.
They are so common that children learn them with the alphabet.</div>""",
             items=CONSONANTS),
    ],
    digits=[("०", "शून्य", "shoonya", "zero"), ("१", "एक", "ek", "one"), ("२", "दो", "do", "two"), ("३", "तीन", "teen", "three"),
            ("४", "चार", "chaar", "four"), ("५", "पाँच", "paanch", "five"), ("६", "छह", "chhah", "six"), ("७", "सात", "saat", "seven"),
            ("८", "आठ", "aath", "eight"), ("९", "नौ", "nau", "nine")],
    phrases=[("अस्सलामु अलैकुम", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("व अलैकुम अस्सलाम", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("मेरा नाम … है", "meraa naam … hai", "My name is …"),
             ("शुक्रिया · धन्यवाद", "shukriyaa · dhanyavaad", "Thank you"),
             ("जज़ाकल्लाहु ख़ैरन", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("माँ · पापा", "maan · paapaa", "Mother · Father"),
             ("भाई · बहन", "bhaaee · bahan", "Brother · Sister"),
             ("हाँ · नहीं", "haan · naheen", "Yes · No"),
             ("मैं हिंदी सीख रहा हूँ!", "main hindee seekh rahaa hoon!", "I am learning Hindi! (a girl says: seekh rahee hoon)")],
    cheer=("माशाअल्लाह! बहुत अच्छे!", "maashaa-allaah! bahut achchhe!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); Hindi Diwas from the <b>Government of India</b> (Department of Official Language).",
    book_pic=dict(left="अ आ इ", right="क ख ग"),
    review_note="Pay special attention to the rare letters ङ and ञ (pages with notes) and the nukta spellings (जहाज़, तरबूज़, दरवाज़ा, औज़ार).",
    cover=dict(title_html="My First Hindi<br>Alphabet", tiles="अआकखगम", pics=["pomegranate", "kite", "boat", "mosque"],
               blurb="Hindi is spoken by more than 600 million people in India and around the world. This big, friendly coloring book "
                     "introduces young children to <b>51 letters</b> of the Hindi alphabet <b>through English</b> — no Hindi needed at home.",
               bullets=["<b>Every letter on its own page</b> — a giant letter to color, its name in Hindi <i>and</i> English letters",
                        "<b>Easy English sound guides</b> plus Hindi phonetics (<span class='nt'>क् + अ = क</span>, <span class='nt'>क + ा = का</span>)",
                        "<b>A word and picture for every letter</b>: <span class='nt'>आम</span> <i>aam</i> mango, <span class='nt'>पतंग</span> <i>patang</i> kite…",
                        "<b>Pencil tracing rows</b> and warm-up pages for vowels and consonants",
                        "<b>Map to color</b>, Hindi numbers <span class='nt'>०–९</span>, first phrases and a certificate",
                        "<b>Single-sided coloring pages</b> so markers never ruin the next picture"]),
    kdp=dict(market="Amazon.com (also Amazon.co.uk and Amazon.ca)",
             desc_intro="Hindi is spoken by more than 600 million people in India and around the world. This big, friendly coloring book introduces young children to <b>51 letters</b> of the Hindi (Devanagari) alphabet <b>through English</b>, so no Hindi is needed at home.",
             desc_bullets=["<b>Every letter on its own page:</b> a giant letter to color, with its name written in Hindi <i>and</i> in English letters",
                           "<b>Easy English sound guides</b> plus simple Hindi phonetics (क् + अ = क, and the vowel signs क + ा = का)",
                           "<b>A word and a picture for every letter</b> to color and say: आम <i>aam</i> (mango), पतंग <i>patang</i> (kite), नाव <i>naav</i> (boat)…",
                           "<b>Pencil tracing rows</b> on every page, plus warm-up pages for the vowels and consonants",
                           "<b>Meet the language:</b> where Hindi is spoken, a map to color, the whole alphabet on one page, the numbers ०–९ and first friendly phrases"],
             categories=["Children's Books › Activities, Crafts & Games › Coloring Books",
                         "Children's Books › Education & Reference › Foreign Language Study",
                         "Children's Books › Religions › Islam"],
             keywords=["hindi alphabet book for kids", "learn hindi for children", "devanagari letters tracing",
                       "hindi varnamala workbook toddlers", "muslim kids activity book", "islamic coloring book for children",
                       "indian heritage language gift"]),
)
