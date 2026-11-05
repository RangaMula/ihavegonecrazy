# -*- coding: utf-8 -*-
"""Book 22 - Konkani (Devanagari). Allamahul Bayan Series. REVIEW DRAFT: needs a native Konkani speaker.
Standard (Goan) Konkani in Devanagari, the official script of Goa. Vocabulary is Konkani, not Hindi or Marathi,
wherever the drafter knew a Konkani word: उदक water, नाल्ल coconut, तारूं boat, जनेल window, णव nine..."""
from indic import build, vowel as V, cons as C, fontset, COMMON_NOTES
from maps import south_asia_map


def _rare(t):
    return f"<b>Rare in Konkani:</b> {t}"


LANG = build(dict(
    code="kok", folder="book-22-konkani", series_no=22, isbn="", draft=True,
    name="Konkani", native="कोंकणी", native_tr="konkaṇee", name_word="नांव", write_word="बरय",
    title_native="म्हजी पयली कोंकणी वर्णमाळा", title_letters="अआइकखग", belongs_native="हें पुस्तक म्हजें", belongs_pic="kok_cashew",
    alphabet_native="वर्णमाळा", numbers_native="आंकडे", numbers_tr="aankḍe", phrases_native="पयले शब्द",
    fonts=fontset("Baloo 2", "baloo-2-devanagari", "Noto Sans Devanagari", "noto-sans-devanagari-devanagari"),
    disp_family="Baloo 2", text_family="Noto Sans Devanagari", glyph_font="baloo-2-devanagari-800-normal.woff2",
    font_credit="Baloo 2, Noto Sans Devanagari",
    base="क", base_tr="ka", virama="्", inherent="अ", inherent_tr="a",
    virama_note="<i>k + a = ka</i> — the little slanting mark <span class='nt'>्</span> (<i>halant</i>) means “no vowel”.",
    vowels_native="स्वर", vowels_tr="svar — “voice letters”", cons_native="व्यंजनां", cons_tr="vyanjanaan",
    vowel_extra="<b>Rare in Konkani:</b> <span class='nt'>ऋ</span> and <span class='nt'>अः</span> appear only in a few "
                "learned words, and words that start with <span class='nt'>ऐ</span> or <span class='nt'>औ</span> are few.",
    cons_extra=" That includes <span class='nt'>ळ</span> and the two joined letters <span class='nt'>क्ष ज्ञ</span>.",
    cons_box="<div class='box'><h3>Rare letters</h3><span class='nt'>ङ ञ ष क्ष ज्ञ</span> are found only in a few words "
             "borrowed from Sanskrit, and <span class='nt'>छ</span> is rare too. But <span class='nt'>ण</span> and "
             "<span class='nt'>ळ</span> are everywhere — Konkani even counts <span class='nt'>णव</span> <i>ṇav</i>, nine!</div>",
    families=[("क ख ग घ ङ", "back of the throat"), ("च छ ज झ ञ", "middle of the tongue"),
              ("ट ठ ड ढ ण", "tongue curled back (hard)"), ("त थ द ध न", "tongue on the teeth (soft)"), ("प फ ब भ म", "the lips")],
    vowels=[
        V("अ", "a", "a short ‘a’ as in “about” — in Konkani often close to the ‘u’ in “cup”", "", "",
          "अळमी", "aḷmee", "wild mushrooms (they pop up in the monsoon rain)", "kok_mushroom"),
        V("आ", "aa", "‘aa’ as in “father”", "ा", "आकार", "आंबो", "aambo", "mango", "mango"),
        V("इ", "i", "‘i’ as in “sit” — short", "ि", "इकार", "इमारत", "imaarat", "building", "building"),
        V("ई", "ee", "‘ee’ as in “see” — long", "ी", "ईकार", "ईद", "eed", "Eid, the festival day", "eid"),
        V("उ", "u", "‘u’ as in “put” — short", "ु", "उकार", "उदक", "udak", "water", "water"),
        V("ऊ", "oo", "‘oo’ as in “moon” — long", "ू", "ऊकार", "ऊस", "oos", "sugarcane", "sugarcane"),
        V("ऋ", "ru", "‘ru’ — Konkani says this vowel as ‘ru’. A rare letter", "ृ", "ऋकार", "ऋतू", "rutoo", "season", "seasons",
          note=_rare("<span class='nt'>ऋ</span> is used only in a few words that come from Sanskrit.")),
        V("ए", "e", "‘e’ as in “they” (say “ay”)", "े", "एकार", "एक", "ek", "one", "one", args=dict(digit="१")),
        V("ऐ", "ai", "‘ai’ as in “aisle”", "ै", "ऐकार", "ऐरण", "airaṇ", "anvil", "anvil",
          note=_rare("few Konkani words start with <span class='nt'>ऐ</span>.")),
        V("ओ", "o", "‘o’ as in “go”", "ो", "ओकार", "ओढणी", "oḍhaṇee", "scarf", "scarf"),
        V("औ", "au", "‘au’ — like the ‘ow’ in “owl”", "ौ", "औकार", "औषध", "aushadh", "medicine", "medicine",
          note=_rare("<span class='nt'>औ</span> is found mostly in learned words. At home you may hear "
                     "<span class='nt'>वखद</span> <i>vakhad</i> for medicine.")),
        V("अं", "an", "a nasal ‘n’ or ‘m’ after the vowel", "ं", "अनुस्वार", "अंधार", "andhaar", "darkness, night", "moon",
          name="अं (अनुस्वार)"),
        V("अः", "ah", "a short breath ‘h’ after the vowel — a rare sign", "ः", "विसर्ग", "प्रातःकाळ", "praatahkaaḷ",
          "early morning", "sunrise", name="अः (विसर्ग)",
          note=_rare("the sign <span class='nt'>ः</span> appears only in a few learned words like this one.")),
    ],
    consonants=[
        C("क", "ka", "‘k’ as in “kite”", "काजू", "kaajoo", "cashew (the fruit and its nut)", "kok_cashew"),
        C("ख", "kha", "‘k’ with a puff of air", "खजूर", "khajoor", "dates", "dates"),
        C("ग", "ga", "‘g’ as in “go”", "गाडी", "gaaḍee", "cart, car", "cart"),
        C("घ", "gha", "‘g’ with a breath", "घर", "ghar", "house, home", "house"),
        C("ङ", "nga", "‘ng’ as in “sing” — a rare letter", "रङ्ग", "rang", "colour", "palette",
          note="Today <span class='nt'>रङ्ग</span> is written <span class='nt'>रंग</span>, with a dot instead of <span class='nt'>ङ</span>."),
        C("च", "cha", "‘ch’ as in “chair” (sometimes ‘ts’)", "चमचो", "chamcho", "spoon", "spoon"),
        C("छ", "chha", "‘ch’ with a puff of air — a rare letter in Konkani", "छत्री", "chhatree", "umbrella", "umbrella",
          note="Many Konkani speakers say <span class='nt'>सत्री</span> <i>satree</i>."),
        C("ज", "ja", "‘j’ as in “jam” (sometimes ‘dz’)", "जनेल", "janel", "window", "window"),
        C("झ", "jha", "‘j’ with a breath", "झाड", "jhaaḍ", "tree", "tree"),
        C("ञ", "nya", "a soft ‘n’ near the roof of the mouth — a rare letter", "अञ्जीर", "anjeer", "fig", "fig",
          note="Today <span class='nt'>अञ्जीर</span> is written <span class='nt'>अंजीर</span>."),
        C("ट", "ṭa", "a hard ‘t’ — curl your tongue back, as in “top”", "टोमाट", "ṭomaaṭ", "tomato", "tomato"),
        C("ठ", "ṭha", "a hard ‘t’ with a puff of air", "ठोकळो", "ṭhokaḷo", "building block", "blocks",
          args=dict(letters=("अ", "आ", "क"))),
        C("ड", "ḍa", "a hard ‘d’ — curl your tongue back, as in “dog”", "डबो", "ḍabo", "box, tin", "box"),
        C("ढ", "ḍha", "a hard ‘d’ with a breath", "ढाल", "ḍhaal", "shield", "shield"),
        C("ण", "ṇa", "‘n’ with the tongue curled back", "णव", "ṇav", "nine", "one", args=dict(digit="९"),
          note="In Hindi <span class='nt'>ण</span> never starts a word — but Konkani counts <span class='nt'>णव</span>, nine!"),
        C("त", "ta", "a soft ‘t’ — tongue touches the back of the teeth", "तारूं", "taaroon", "boat", "boat"),
        C("थ", "tha", "a soft ‘t’ with a puff of air", "थाळी", "thaaḷee", "plate", "plate"),
        C("द", "da", "a soft ‘d’ — tongue touches the back of the teeth", "दार", "daar", "door", "door"),
        C("ध", "dha", "a soft ‘d’ with a breath", "धागो", "dhaago", "thread, yarn", "wool"),
        C("न", "na", "‘n’ as in “net”", "नाल्ल", "naall", "coconut", "coconut"),
        C("प", "pa", "‘p’ as in “pen”", "पाव", "paav", "bread rolls (Goan pao)", "kok_pao"),
        C("फ", "pha", "‘p’ with a puff of air — close to ‘f’", "फूल", "phool", "flower", "flower"),
        C("ब", "ba", "‘b’ as in “ball”", "बदाम", "badaam", "almonds", "almond"),
        C("भ", "bha", "‘b’ with a breath", "भात", "bhaat", "rice plants in the field (paddy)", "paddy"),
        C("म", "ma", "‘m’ as in “moon”", "मशीद", "masheed", "mosque", "mosque"),
        C("य", "ya", "‘y’ as in “yes”", "यंत्र", "yantra", "machine", "gears"),
        C("र", "ra", "a tapped ‘r’", "रताळें", "rataaḷen", "sweet potato", "potato"),
        C("ल", "la", "‘l’ as in “lamp”", "लिंबू", "limboo", "lemon", "lemon"),
        C("व", "va", "between ‘v’ and ‘w’", "वीज", "veej", "electricity, lightning", "bulb"),
        C("श", "sha", "‘sh’ as in “shoe”", "शीत", "sheet", "cooked rice", "rice"),
        C("ष", "sha", "‘sh’ as in “shoe” — a rare letter", "षट्कोन", "shaṭkon", "hexagon", "hexagon",
          note="<span class='nt'>ष</span> is found only in a few words that come from Sanskrit."),
        C("स", "sa", "‘s’ as in “sun”", "सूर्य", "soorya", "sun", "sun"),
        C("ह", "ha", "‘h’ as in “hat”", "हातोडो", "haatoḍo", "hammer", "tools"),
        C("ळ", "ḷa", "an ‘l’ with the tongue curled back — never at the start of a word", "कमळ", "kamaḷ", "lotus, water lily", "lily",
          note="Look for <span class='nt'>ळ</span> at the end of <span class='nt'>कमळ</span>!"),
        C("क्ष", "ksha", "‘k’ + ‘sh’ said together — a rare letter", "क्षितीज", "kshiteej", "horizon (where the sea meets the sky)", "waves",
          phon="क् + ष = क्ष"),
        C("ज्ञ", "gnya", "said ‘gnya’ in Konkani — a rare letter", "ज्ञान", "gnyaan", "knowledge", "book", phon="ज् + ञ = ज्ञ",
          args=dict(left="अ आ इ", right="क ख ग")),
    ],
    sound_notes=COMMON_NOTES + [
        "<b>a</b> is the short sound in “about”. Every consonant carries it: <span class='nt'>क</span> = <i>ka</i>; at the end of a word "
        "it is usually silent. In Konkani it often sounds close to the ‘u’ in “cup”.",
        "<b>A dot under t, d, n, l</b> (<i>ṭ, ḍ, ṇ, ḷ</i>) means a <i>hard</i> sound with the tongue curled back; without it, the tongue touches the teeth.",
        "<b>-en at the end</b> (<span class='nt'>रताळें</span> <i>rataaḷen</i>) is a nasal ‘e’, said through the nose — a very Konkani sound."],
    standard="standard Konkani as spoken in Goa",
    hello=[
        ("Who speaks it?", "About <b>2 million people</b> speak Konkani as their first language.<sup>³</sup>"),
        ("Where?", "Along India’s west coast, the <b>Konkan</b>: in <b>Goa</b>, where it is the official language, and in coastal "
                   "Karnataka (Karwar, Mangaluru), Maharashtra and Kerala."),
        ("How is it written?", "In Goa, in the <b>Devanagari</b> script, from <b>left to right</b>. Konkani has also been written in the "
                               "Kannada, Malayalam, Roman and Arabic scripts — five scripts for one language!"),
        ("How many letters?", "This book teaches <b>49</b>: <b>13 vowels</b> (<span class='nt'>स्वर</span>) and <b>36 consonants</b> "
                              "(<span class='nt'>व्यंजनां</span>), including <span class='nt'>ळ</span>."),
        ("Rare letters", "<span class='nt'>ऋ अः ङ ञ ष क्ष ज्ञ</span> live mostly in words from Sanskrit. The pages for them say so."),
        ("A day for Konkani", "On <b>20 August 1992</b> Konkani was added to the list of India’s official languages. "
                              "Goa remembers the day every year.<sup>³</sup>"),
    ],
    hello_pics=[("kok_cashew", {}), ("coconut", {}), ("boat", {})],
    map=south_asia_map(
        points=dict(panaji=[73.83, 15.49], margao=[73.96, 15.28], karwar=[74.13, 14.81], mangaluru=[74.86, 12.91],
                    area=[74.05, 14.9], label=[78.6, 15.6]),
        area=(20, 50, -18), label="KONKAN",
        cities=[("panaji", "Panaji", -12, 6, "end", True), ("karwar", "Karwar", 12, 10, "start", False),
                ("mangaluru", "Mangaluru", 12, 8, "start", False)],
        marker=[74.0, 15.0], caption="The circle shows Goa and the Konkan coast on the world map.",
        legend="<b>Color it:</b> the Konkan coast (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · the sea "
               "<b>blue</b>. Draw coconut palms along the beach! <b>Find it:</b> Panaji ★ is the capital of Goa; Karwar and Mangaluru "
               "are Konkani towns further down the coast."),
    digits=[("०", "शून्य", "shoonya", "zero"), ("१", "एक", "ek", "one"), ("२", "दोन", "don", "two"), ("३", "तीन", "teen", "three"),
            ("४", "चार", "chaar", "four"), ("५", "पांच", "paanch", "five"), ("६", "स", "sa", "six"), ("७", "सात", "saat", "seven"),
            ("८", "आठ", "aaṭh", "eight"), ("९", "णव", "ṇav", "nine")],
    phrases=[("अस्सलामु अलैकुम", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("व अलैकुम अस्सलाम", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("म्हजें नांव …", "mhajen naanv …", "My name is …"),
             ("देव बरें करूं · धन्यवाद", "dev baren karoon · dhanyavaad", "Thank you (the first means “may God do you good”)"),
             ("जज़ाकल्लाहु ख़ैरन", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("आवय · बापूय", "aavay · baapooy", "Mother · Father"),
             ("भाव · भयण", "bhaav · bhayaṇ", "Brother · Sister"),
             ("हंय · ना", "hay · naa", "Yes · No"),
             ("हांव कोंकणी शिकतां!", "haanv konkaṇee shiktaan!", "I am learning Konkani!")],
    cheer=("माशाअल्लाह! शाबास!", "maashaa-allaah! shaabaas!", "Well done, bravo!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the Census of India 2011; the 1992 date from the "
                 "<b>Constitution of India</b> (71st Amendment).",
    book_pic=dict(left="अ आ इ", right="क ख ग"),
    review_note="Drafted from general knowledge, not from a Konkani dictionary: every word, spelling and transliteration needs a Goan "
                "Konkani speaker. Check first: अळमी (mushroom; or आळमी?), ऊस (sugarcane), ऐरण, ओढणी, औषध/वखद, अंधार, टोमाट, ठोकळो, "
                "डबो, धागो, रताळें, वीज, शीत, हातोडो, क्षितीज; the phrases देव बरें करूं, आवय · बापूय, भाव · भयण, हंय, "
                "हांव कोंकणी शिकतां; the title म्हजी पयली कोंकणी वर्णमाळा and आंकडे. Is ज्ञ said ‘gnya’ in Goa? "
                "Transliteration writes अ as ‘a’ (Romi Konkani would write ‘o’: udok).",
    tiles="अआकखगम", cover_pics=["kok_cashew", "coconut", "boat", "mosque"], title_size=48,
    speakers_blurb="Konkani is the language of Goa and India’s sunny Konkan coast.",
    sample_words=[("आंबो", "aambo", "mango"), ("नाल्ल", "naall", "coconut"), ("तारूं", "taaroon", "boat")],
    keywords=["konkani alphabet book for kids", "learn konkani for children", "konkani letters tracing",
              "goa konkani workbook", "muslim kids activity book", "islamic coloring book for children",
              "konkani heritage language gift"],
))
