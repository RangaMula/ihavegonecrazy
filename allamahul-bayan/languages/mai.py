# -*- coding: utf-8 -*-
"""Book 23 - Maithili (Devanagari). Allamahul Bayan Series. REVIEW DRAFT: needs a native Maithili speaker.
Vocabulary is Maithili where the drafter knew a Maithili word (गाछ tree, चान moon, लताम guava, कुसियार sugarcane,
तरेगन stars, पोखरि pond, मखान fox nuts...), not Hindi."""
from indic import build, vowel as V, cons as C, fontset, COMMON_NOTES
from maps import south_asia_map


def _rare(t):
    return f"<b>Rare in Maithili:</b> {t}"


LANG = build(dict(
    code="mai", folder="book-23-maithili", series_no=23, isbn="", draft=True,
    name="Maithili", native="मैथिली", native_tr="maithilee", name_word="नाम", write_word="लिखू",
    title_native="हमर पहिल मैथिली वर्णमाला", title_letters="अआइकखग", belongs_native="ई पोथी हमर अछि", belongs_pic="mai_makhana",
    alphabet_native="वर्णमाला", numbers_native="अंक", numbers_tr="ank", phrases_native="पहिल शब्द",
    fonts=fontset("Baloo 2", "baloo-2-devanagari", "Noto Sans Devanagari", "noto-sans-devanagari-devanagari"),
    disp_family="Baloo 2", text_family="Noto Sans Devanagari", glyph_font="baloo-2-devanagari-800-normal.woff2",
    font_credit="Baloo 2, Noto Sans Devanagari",
    base="क", base_tr="ka", virama="्", inherent="अ", inherent_tr="a",
    virama_note="<i>k + a = ka</i> — the little slanting mark <span class='nt'>्</span> (<i>halant</i>) means “no vowel”.",
    vowels_native="स्वर", vowels_tr="svar — “voice letters”", cons_native="व्यंजन", cons_tr="vyanjan",
    vowel_extra="<b>Rare in Maithili:</b> <span class='nt'>ऋ</span> and <span class='nt'>अः</span> appear only in a few "
                "words that come from Sanskrit.",
    cons_extra=" That includes the flapped letters <span class='nt'>ड़ ढ़</span> and the joined letters <span class='nt'>क्ष त्र ज्ञ</span>.",
    cons_box="<div class='box'><h3>Rare letters</h3><span class='nt'>ङ ञ ण ष क्ष ज्ञ</span> are found mostly in words from Sanskrit. "
             "In everyday Maithili, <span class='nt'>श ष स</span> all sound like <i>s</i>, <span class='nt'>ण</span> sounds like "
             "<span class='nt'>न</span>, and <span class='nt'>व</span> often sounds like <span class='nt'>ब</span>.</div>",
    families=[("क ख ग घ ङ", "back of the throat"), ("च छ ज झ ञ", "middle of the tongue"),
              ("ट ठ ड ढ ण", "tongue curled back (hard)"), ("त थ द ध न", "tongue on the teeth (soft)"), ("प फ ब भ म", "the lips")],
    vowels=[
        V("अ", "a", "a short ‘a’ as in “about”", "", "", "अड़हुल", "aṛahul", "hibiscus flower", "flower"),
        V("आ", "aa", "‘aa’ as in “father”", "ा", "आकार", "आम", "aam", "mango", "mango"),
        V("इ", "i", "‘i’ as in “sit” — short", "ि", "इकार", "इनार", "inaar", "well (for water)", "well"),
        V("ई", "ee", "‘ee’ as in “see” — long", "ी", "ईकार", "ईंटा", "eenṭaa", "brick", "brick"),
        V("उ", "u", "‘u’ as in “put” — short", "ु", "उकार", "उपहार", "uphaar", "gift", "gift"),
        V("ऊ", "oo", "‘oo’ as in “moon” — long", "ू", "ऊकार", "ऊन", "oon", "wool", "wool"),
        V("ऋ", "ri", "‘ri’ as in “ring” — a rare letter", "ृ", "ऋकार", "ऋतु", "ritu", "season", "seasons",
          note=_rare("<span class='nt'>ऋ</span> is used only in a few words that come from Sanskrit.")),
        V("ए", "e", "‘e’ as in “they” (say “ay”)", "े", "एकार", "एक", "ek", "one", "one", args=dict(digit="१")),
        V("ऐ", "ai", "‘ai’ as in “aisle”", "ै", "ऐकार", "ऐना", "ainaa", "mirror", "mirror"),
        V("ओ", "o", "‘o’ as in “go”", "ो", "ओकार", "ओखरि", "okhari", "mortar (for grinding)", "mortar"),
        V("औ", "au", "‘au’ — like the ‘ow’ in “owl”", "ौ", "औकार", "औंठी", "aunṭhee", "ring", "ring"),
        V("अं", "an", "a nasal ‘n’ or ‘m’ after the vowel", "ं", "अनुस्वार", "अंगूर", "angoor", "grapes", "grapes",
          name="अं (अनुस्वार)"),
        V("अः", "ah", "a short breath ‘h’ after the vowel — a rare sign", "ः", "विसर्ग", "प्रातः", "praatah", "early morning",
          "sunrise", name="अः (विसर्ग)",
          note=_rare("the sign <span class='nt'>ः</span> appears only in a few learned words. Everyday Maithili says "
                     "<span class='nt'>भोर</span> <i>bhor</i> for early morning.")),
    ],
    consonants=[
        C("क", "ka", "‘k’ as in “kite”", "कुसियार", "kusiyaar", "sugarcane", "sugarcane"),
        C("ख", "kha", "‘k’ with a puff of air", "खजूर", "khajoor", "dates", "dates"),
        C("ग", "ga", "‘g’ as in “go”", "गाछ", "gaachh", "tree", "tree"),
        C("घ", "gha", "‘g’ with a breath", "घर", "ghar", "house, home", "house"),
        C("ङ", "nga", "‘ng’ as in “sing” — a rare letter", "रङ्ग", "rang", "colour", "palette",
          note="Today <span class='nt'>रङ्ग</span> is written <span class='nt'>रंग</span>, with a dot instead of <span class='nt'>ङ</span>."),
        C("च", "cha", "‘ch’ as in “chair”", "चान", "chaan", "moon", "moon"),
        C("छ", "chha", "‘ch’ with a puff of air", "छाता", "chhaataa", "umbrella", "umbrella"),
        C("ज", "ja", "‘j’ as in “jam”", "जहाज", "jahaaj", "ship", "ship"),
        C("झ", "jha", "‘j’ with a breath", "झाड़ू", "jhaaṛoo", "broom", "broom"),
        C("ञ", "nya", "a soft ‘n’ near the roof of the mouth — a rare letter", "अञ्जीर", "anjeer", "fig", "fig",
          note="Today <span class='nt'>अञ्जीर</span> is written <span class='nt'>अंजीर</span>."),
        C("ट", "ṭa", "a hard ‘t’ — curl your tongue back, as in “top”", "टमाटर", "ṭamaaṭar", "tomato", "tomato"),
        C("ठ", "ṭha", "a hard ‘t’ with a puff of air", "ठेला", "ṭhelaa", "push-cart", "cart"),
        C("ड", "ḍa", "a hard ‘d’ — curl your tongue back, as in “dog”", "डाली", "ḍaalee", "basket", "basket"),
        C("ढ", "ḍha", "a hard ‘d’ with a breath", "ढाकन", "ḍhaakan", "lid", "jar"),
        C("ण", "ṇa", "‘n’ with the tongue curled back — rare; most Maithili speakers say it like न",
          "बाण", "baaṇ", "arrow", "bowarrow",
          note="Look for <span class='nt'>ण</span> at the end of <span class='nt'>बाण</span>!"),
        C("त", "ta", "a soft ‘t’ — tongue touches the back of the teeth", "तरेगन", "taregan", "stars", "star"),
        C("थ", "tha", "a soft ‘t’ with a puff of air", "थारी", "thaaree", "plate", "plate"),
        C("द", "da", "a soft ‘d’ — tongue touches the back of the teeth", "दरबज्जा", "darbajjaa", "door, front porch", "door"),
        C("ध", "dha", "a soft ‘d’ with a breath", "धान", "dhaan", "rice plants (paddy)", "paddy"),
        C("न", "na", "‘n’ as in “net”", "नारियर", "naariyar", "coconut", "coconut"),
        C("प", "pa", "‘p’ as in “pen”", "पोखरि", "pokhari", "pond (with lotus flowers)", "lily"),
        C("फ", "pha", "‘p’ with a puff of air", "फुकना", "phuknaa", "balloon", "balloon"),
        C("ब", "ba", "‘b’ as in “ball”", "बाँस", "baans", "bamboo", "mai_bamboo"),
        C("भ", "bha", "‘b’ with a breath", "भात", "bhaat", "cooked rice", "rice"),
        C("म", "ma", "‘m’ as in “moon”", "मखान", "makhaan", "fox nuts (puffed lotus seeds)", "mai_makhana"),
        C("य", "ya", "‘y’ as in “yes” — at the start of a word Maithili often says ‘j’", "यंत्र", "yantra", "machine", "gears"),
        C("र", "ra", "a tapped ‘r’", "रोटी", "roṭee", "flatbread (roti)", "roti"),
        C("ल", "la", "‘l’ as in “lamp”", "लताम", "lataam", "guava", "mai_guava"),
        C("व", "va", "between ‘v’ and ‘w’ — Maithili often says ‘b’", "वर्षा", "varshaa", "rain", "raincloud",
          note="In everyday Maithili rain is <span class='nt'>बरखा</span> <i>barkhaa</i>."),
        C("श", "sha", "‘sh’ as in “shoe” — Maithili usually says ‘s’", "शहद", "shahad", "honey", "honey",
          note="Maithili more often says <span class='nt'>मधु</span> <i>madhu</i> for honey."),
        C("ष", "sha", "‘sh’ with the tongue curled back — a rare letter", "षट्कोण", "shaṭkoṇ", "hexagon", "hexagon",
          note="<span class='nt'>ष</span> is found only in words that come from Sanskrit."),
        C("स", "sa", "‘s’ as in “sun”", "सुरुज", "suruj", "sun", "sun"),
        C("ह", "ha", "‘h’ as in “hat”", "हाँड़ी", "haanṛee", "clay pot", "pot"),
        C("ड़", "ṛa", "a quick flapped ‘r’ — never at the start of a word", "पहाड़", "pahaaṛ", "mountain", "mountain",
          phon="ड + ़ (dot) = ड़", note="Look for <span class='nt'>ड़</span> at the end of <span class='nt'>पहाड़</span>!"),
        C("ढ़", "ṛha", "a flapped ‘r’ with a breath — never at the start of a word", "सीढ़ी", "seeṛhee", "ladder", "ladder",
          phon="ढ + ़ (dot) = ढ़", note="Find <span class='nt'>ढ़</span> in the middle of <span class='nt'>सीढ़ी</span>!"),
        C("क्ष", "ksha", "‘k’ + ‘sh’ said together — rare; often said ‘chh’", "अक्षर", "akshar", "letter (of the alphabet)", "blocks",
          phon="क् + ष = क्ष", note="Find <span class='nt'>क्ष</span> in the middle of <span class='nt'>अक्षर</span>!",
          args=dict(letters=("अ", "आ", "क"))),
        C("त्र", "tra", "‘t’ + ‘r’ said together", "त्रिकोण", "trikoṇ", "triangle", "triangle", phon="त् + र = त्र"),
        C("ज्ञ", "gya", "said ‘gya’ in Maithili — a rare letter", "ज्ञान", "gyaan", "knowledge", "book", phon="ज् + ञ = ज्ञ",
          args=dict(left="अ आ इ", right="क ख ग")),
    ],
    sound_notes=COMMON_NOTES + [
        "<b>a</b> is the short sound in “about”. Every consonant carries it: <span class='nt'>क</span> = <i>ka</i>; at the end of a word it is usually silent.",
        "<b>A dot under t, d, n</b> (<i>ṭ, ḍ, ṇ</i>) means a <i>hard</i> sound with the tongue curled back; <i>ṛ</i> is a quick flap of the tongue."],
    standard="standard Maithili as spoken around Darbhanga and Madhubani",
    hello=[
        ("Who speaks it?", "About <b>14 million people</b> in India and more than <b>3 million</b> in Nepal speak Maithili.<sup>³</sup>"),
        ("Where?", "In <b>Mithila</b>: the plains of north <b>Bihar</b> in India (Darbhanga, Madhubani) and the eastern lowlands of "
                   "<b>Nepal</b> (Janakpur). It is the second most spoken language of Nepal."),
        ("How is it written?", "Today in <b>Devanagari</b>, from <b>left to right</b>. Long ago it had its own script, "
                               "<b>Tirhuta</b> (<i>Mithilakshar</i>), a cousin of the Bengali script."),
        ("How many letters?", "This book teaches <b>51</b>: <b>13 vowels</b> (<span class='nt'>स्वर</span>) and <b>38 consonants</b> "
                              "(<span class='nt'>व्यंजन</span>), including <span class='nt'>ड़ ढ़</span> and <span class='nt'>क्ष त्र ज्ञ</span>."),
        ("Rare letters", "<span class='nt'>ऋ अः ङ ञ ण ष क्ष ज्ञ</span> live mostly in words from Sanskrit. The pages for them say so."),
        ("Did you know?", "Mithila is famous for <span class='nt'>मखान</span> <i>makhaan</i>, the puffed seeds of a water plant, "
                          "for its many ponds, and for colourful wall paintings. In <b>2003</b> Maithili became one of India’s "
                          "official languages.<sup>³</sup>"),
    ],
    hello_pics=[("mai_makhana", {}), ("mango", {}), ("lily", {})],
    map=south_asia_map(
        points=dict(darbhanga=[85.90, 26.15], madhubani=[86.07, 26.35], janakpur=[85.92, 26.73], muzaffarpur=[85.39, 26.12],
                    area=[86.1, 26.4], label=[86.0, 23.4]),
        area=(62, 30, -5), label="MITHILA",
        cities=[("darbhanga", "Darbhanga", -12, 10, "end", True), ("janakpur", "Janakpur", 12, -4, "start", False)],
        marker=[86.0, 26.4], caption="The circle shows Mithila on the world map.",
        legend="<b>Color it:</b> Mithila (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · the seas <b>blue</b>. "
               "Draw little blue ponds inside it! <b>Find it:</b> Darbhanga ★ is the biggest Maithili city in Bihar; "
               "Janakpur is the biggest Maithili city in Nepal."),
    digits=[("०", "शून्य", "shoonya", "zero"), ("१", "एक", "ek", "one"), ("२", "दू", "doo", "two"), ("३", "तीन", "teen", "three"),
            ("४", "चारि", "chaari", "four"), ("५", "पाँच", "paanch", "five"), ("६", "छह", "chhah", "six"), ("७", "सात", "saat", "seven"),
            ("८", "आठ", "aaṭh", "eight"), ("९", "नौ", "nau", "nine")],
    phrases=[("अस्सलामु अलैकुम", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("व अलैकुम अस्सलाम", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("हमर नाम … अछि", "hamar naam … achhi", "My name is …"),
             ("धन्यवाद", "dhanyavaad", "Thank you"),
             ("जज़ाकल्लाहु ख़ैरन", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("माय · बाबू", "maay · baaboo", "Mother · Father"),
             ("भाय · बहिन", "bhaay · bahin", "Brother · Sister"),
             ("हँ · नहि", "han · nahi", "Yes · No"),
             ("हम मैथिली सिखि रहल छी!", "ham maithilee sikhi rahal chhee!", "I am learning Maithili!")],
    cheer=("माशाअल्लाह! बड़ नीक!", "maashaa-allaah! baṛ neek!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), the Census of India 2011 and the National Census of "
                 "Nepal; the 2003 date from the <b>Constitution of India</b> (92nd Amendment).",
    book_pic=dict(left="अ आ इ", right="क ख ग"),
    review_note="Drafted from general knowledge, not from a Maithili dictionary: every word, spelling and transliteration needs a "
                "Maithili speaker. Check first: अड़हुल, ईंटा, उपहार (a Maithili word for ‘gift’ would be better), ओखरि, औंठी, "
                "कुसियार, ढाकन, तरेगन, थारी, दरबज्जा, फुकना, लताम, मखान, हाँड़ी, सुरुज; the phrases हमर नाम … अछि, माय · बाबू, "
                "भाय · बहिन, हँ · नहि, हम मैथिली सिखि रहल छी; the title हमर पहिल मैथिली वर्णमाला and ई पोथी हमर अछि; "
                "the number words दू, चारि, छह. Maithili writers sometimes use the sign ऽ (avagraha); this book does not.",
    tiles="अआकखगम", cover_pics=["mai_makhana", "mango", "lily", "mosque"], title_size=48,
    speakers_blurb="Maithili is spoken by more than 17 million people in Mithila, in north Bihar and the lowlands of Nepal.",
    sample_words=[("आम", "aam", "mango"), ("चान", "chaan", "moon"), ("मखान", "makhaan", "fox nuts")],
    keywords=["maithili alphabet book for kids", "learn maithili for children", "maithili letters tracing",
              "mithila heritage workbook", "muslim kids activity book", "islamic coloring book for children",
              "maithili heritage language gift"],
))
