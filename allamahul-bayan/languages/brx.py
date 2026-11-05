# -*- coding: utf-8 -*-
"""Book 25 - Bodo / Boro (Devanagari). Allamahul Bayan Series. REVIEW DRAFT: needs a native Bodo speaker.
Bodo is a Tibeto-Burman language (not related to Hindi). Native words are used wherever the drafter knew one
(दै water, सान sun, अखा rain, बिबार flower, थालिर banana, थाइजौ mango, हाथोरखि star, जोमै cloud...).
Many Devanagari letters are used only in borrowed words; their pages say so.
Transliteration: 'w' stands for the Bodo vowel /ɯ/ (written ो, and inside ै ौ), as in Roman Bodo (Bwisagu)."""
from indic import build, vowel as V, cons as C, fontset, COMMON_NOTES
from maps import south_asia_map

APOS = "’"  # Bodo marks a spoken final 'o' (and tone) with an apostrophe: बर’ = Boro


def _rare(t):
    return f"<b>Rare in Bodo:</b> {t}"


def _loan(t=""):
    return _rare("this letter is used mostly in words borrowed from other languages." + (" " + t if t else ""))


LANG = build(dict(
    code="brx", folder="book-25-bodo", series_no=25, isbn="", draft=True,
    name="Bodo", native="बर" + APOS, native_tr="boro", name_word="मुं", write_word="लिर",
    title_native="आंनि गिबि बर" + APOS + " आखर", title_letters="अआइकखग", belongs_native="बे बिजाबआ आंनि", belongs_pic="mai_bamboo",
    alphabet_native="आखर", numbers_native="अनजिमा", numbers_tr="onjimaa", phrases_native="गिबि सोदोब",
    fonts=fontset("Baloo 2", "baloo-2-devanagari", "Noto Sans Devanagari", "noto-sans-devanagari-devanagari"),
    disp_family="Baloo 2", text_family="Noto Sans Devanagari", glyph_font="baloo-2-devanagari-800-normal.woff2",
    font_credit="Baloo 2, Noto Sans Devanagari",
    base="क", base_tr="ko", virama="्", inherent="अ", inherent_tr="o",
    virama_note="<i>k + o = ko</i> — the little slanting mark <span class='nt'>्</span> (<i>halant</i>) means “no vowel”.",
    vowels_native="स्वर", vowels_tr="svor — “voice letters”", cons_native="व्यंजन", cons_tr="byanjon",
    vowel_extra="In Bodo the hidden vowel <span class='nt'>अ</span> sounds like the ‘o’ in “on”. A little mark "
                "<span class='nt'>" + APOS + "</span> after the last letter says “say the hidden o here”: "
                "<span class='nt'>बर" + APOS + "</span> <i>boro</i>. <b>Rare in Bodo:</b> long <span class='nt'>ई ऊ</span> "
                "(mostly in borrowed words); the full chart’s <span class='nt'>ऋ</span> and <span class='nt'>अः</span> "
                "are hardly ever used, so this book leaves them out.",
    cons_extra=" Many of them — <span class='nt'>घ ङ च छ झ ञ ट ठ ड ढ ण ध भ य श ष</span> — are rare in Bodo.",
    cons_box="<div class='box'><h3>Rare letters</h3>Bodo has fewer sounds than Hindi. Its own words use mostly "
             "<span class='nt'>ख ग ज थ द न फ ब म र ल व स ह</span>. The other letters, and the joined letters "
             "<span class='nt'>क्ष त्र ज्ञ</span>, are used mostly in words borrowed from Assamese, Hindi or English — "
             "the pages for them say so.</div>",
    families=[("क ख ग घ ङ", "back of the throat"), ("च छ ज झ ञ", "middle of the tongue"),
              ("ट ठ ड ढ ण", "tongue curled back (hard)"), ("त थ द ध न", "tongue on the teeth"), ("प फ ब भ म", "the lips")],
    vowels=[
        V("अ", "o", "‘o’ as in “on” — Bodo’s hidden vowel", "", "", "अखा", "okhaa", "rain", "raincloud"),
        V("आ", "aa", "‘aa’ as in “father”", "ा", "आकार", "आलु", "aalu", "potato", "potato"),
        V("इ", "i", "‘i’ as in “sit”", "ि", "इकार", "इटा", "iṭaa", "brick", "brick"),
        V("ई", "ee", "‘ee’ as in “see”", "ी", "ईकार", "ईद", "eed", "Eid, the festival day", "eid",
          note=_rare("long <span class='nt'>ई</span> is found mostly in borrowed words; Bodo words use <span class='nt'>इ</span>.")),
        V("उ", "u", "‘u’ as in “put”", "ु", "उकार", "उवा", "uwaa", "bamboo", "mai_bamboo"),
        V("ऊ", "oo", "‘oo’ as in “moon”", "ू", "ऊकार", "ऊन", "oon", "wool", "wool",
          note=_rare("long <span class='nt'>ऊ</span> is found mostly in borrowed words; Bodo words use <span class='nt'>उ</span>.")),
        V("ए", "e", "‘e’ as in “they” (say “ay”)", "े", "एकार", "एन्दि", "endi", "eri silk shawl", "scarf"),
        V("ऐ", "ai", "in Bodo words this sign is usually said ‘wi’", "ै", "ऐकार", "दै", "dwi", "water", "water",
          note="Few Bodo words start with <span class='nt'>ऐ</span>. Find its sign <span class='nt'>ै</span> in "
               "<span class='nt'>दै</span> <i>dwi</i>, water!"),
        V("ओ", "w", "the special Bodo vowel ‘w’: say ‘oo’ with flat, smiling lips", "ो", "ओकार", "ओंखाम", "wngkhaam",
          "cooked rice", "rice"),
        V("औ", "wu", "in Bodo words this sign is usually said ‘wu’", "ौ", "औकार", "थाइजौ", "thaaijwu", "mango", "mango",
          note="Few Bodo words start with <span class='nt'>औ</span>. Find its sign <span class='nt'>ौ</span> at the end of "
               "<span class='nt'>थाइजौ</span>!"),
        V("अं", "ong", "‘ng’ as in “sing” after the vowel", "ं", "अनुस्वार", "बिफां", "biphaang", "tree", "tree",
          name="अं (अनुस्वार)",
          note="Find the dot <span class='nt'>ं</span> at the end of <span class='nt'>बिफां</span>, tree!"),
    ],
    consonants=[
        C("क", "ko", "‘k’ as in “kite”", "कमला", "komolaa", "orange", "brx_orange",
          note=_rare("Bodo words prefer <span class='nt'>ख</span>; <span class='nt'>कमला</span> is borrowed from Assamese.")),
        C("ख", "kho", "‘k’ with a puff of air", "खिरकि", "khirki", "window", "window"),
        C("ग", "go", "‘g’ as in “go”", "गामि", "gaami", "village, home", "house"),
        C("घ", "gho", "‘g’ with a breath — a rare letter", "घरि", "ghori", "clock", "clock", note=_loan()),
        C("ङ", "ngo", "‘ng’ as in “sing” — a rare letter", "रङ", "rong", "colour", "palette",
          note="Bodo usually writes this sound with the dot <span class='nt'>ं</span>, as in <span class='nt'>बिफां</span>."),
        C("च", "cho", "‘ch’ as in “chair” — a rare letter", "चामुच", "chaamuch", "spoon", "spoon",
          note=_loan("Bodo’s own words use <span class='nt'>स</span> and <span class='nt'>ज</span> instead.")),
        C("छ", "chho", "‘ch’ with a puff of air — a rare letter", "छाता", "chhaataa", "umbrella", "umbrella", note=_loan()),
        C("ज", "jo", "‘j’ or ‘z’ — Bodo often says ‘z’", "जोमै", "jwmwi", "cloud", "clouds"),
        C("झ", "jho", "‘j’ with a breath — a rare letter", "झाडु", "jhaaḍu", "broom", "broom", note=_loan()),
        C("ञ", "nyo", "a soft ‘n’ near the roof of the mouth — a rare letter", "अञ्जीर", "onjeer", "fig", "fig",
          note=_loan("Today it is usually written <span class='nt'>अंजीर</span>.")),
        C("ट", "ṭo", "a hard ‘t’ — curl your tongue back — a rare letter", "टिफिन", "ṭiphin", "lunch box", "box", note=_loan()),
        C("ठ", "ṭho", "a hard ‘t’ with a puff of air — a rare letter", "ठेला", "ṭhelaa", "push-cart", "cart", note=_loan()),
        C("ड", "ḍo", "a hard ‘d’ — curl your tongue back — a rare letter", "डाब", "ḍaab", "green coconut", "coconut", note=_loan()),
        C("ढ", "ḍho", "a hard ‘d’ with a breath — a rare letter", "ढाल", "ḍhaal", "shield", "shield", note=_loan()),
        C("ण", "ṇo", "‘n’ with the tongue curled back — a rare letter", "बाण", "baaṇ", "arrow", "bowarrow",
          note=_loan("Look for <span class='nt'>ण</span> at the end of <span class='nt'>बाण</span>!")),
        C("त", "to", "a soft ‘t’", "तरमुज", "tormuj", "watermelon", "watermelon",
          note=_rare("Bodo words prefer <span class='nt'>थ</span>; <span class='nt'>तरमुज</span> is borrowed.")),
        C("थ", "tho", "‘t’ with a puff of air", "थालिर", "thaalir", "banana", "banana"),
        C("द", "do", "a soft ‘d’", "दैमा", "dwimaa", "river (“big water”)", "waves"),
        C("ध", "dho", "‘d’ with a breath — a rare letter", "धान", "dhaan", "rice plants (paddy)", "paddy",
          note=_loan("In Bodo, paddy is <span class='nt'>माइ</span> <i>maai</i>.")),
        C("न", "no", "‘n’ as in “net”", "नाउ", "naau", "boat", "boat"),
        C("प", "po", "‘p’ as in “pen”", "पेन", "pen", "pen", "pen",
          note=_rare("Bodo words prefer <span class='nt'>फ</span>; <span class='nt'>पेन</span> comes from English.")),
        C("फ", "pho", "‘p’ with a puff of air", "फान्थौ", "phaanthwu", "eggplant (brinjal)", "brx_eggplant"),
        C("ब", "bo", "‘b’ as in “ball”", "बिबार", "bibaar", "flower", "flower"),
        C("भ", "bho", "‘b’ with a breath — a rare letter", "भात", "bhaat", "rice on a plate", "plate",
          note=_loan("In Bodo, cooked rice is <span class='nt'>ओंखाम</span> <i>wngkhaam</i>.")),
        C("म", "mo", "‘m’ as in “moon”", "मुलि", "muli", "medicine", "medicine"),
        C("य", "yo", "‘y’ as in “yes” — a rare letter", "यन्त्र", "yontro", "machine", "gears", note=_loan()),
        C("र", "ro", "a tapped ‘r’", "रेल", "rel", "train", "engine"),
        C("ल", "lo", "‘l’ as in “lamp”", "लामा", "laamaa", "road, path", "brx_road"),
        C("व", "wo", "‘w’ as in “water”", "वाट", "waaṭ", "fire", "brx_fire"),
        C("श", "sho", "‘sh’ as in “shoe” — a rare letter; Bodo says ‘s’", "शरबत", "shorbot", "sweet drink (sherbet)", "teacup",
          note=_loan()),
        C("ष", "sho", "‘sh’ — a rare letter", "षट्कोण", "shoṭkon", "hexagon", "hexagon", note=_loan()),
        C("स", "so", "‘s’ as in “sun”", "सान", "saan", "sun", "sun"),
        C("ह", "ho", "‘h’ as in “hat”", "हाथोरखि", "haathwrkhi", "star", "star"),
    ],
    sound_notes=COMMON_NOTES + [
        "<b>o</b> is Bodo’s hidden vowel, as in “on”: <span class='nt'>क</span> = <i>ko</i>. At the end of a word it is silent, "
        "unless the little mark <span class='nt'>" + APOS + "</span> follows: <span class='nt'>बर" + APOS + "</span> <i>boro</i>.",
        "<b>w</b> in our English letters is a special Bodo vowel: say ‘oo’ but keep your lips flat, as if smiling. "
        "Bodo writes it with <span class='nt'>ो</span>: <span class='nt'>जोमै</span> <i>jwmwi</i>, cloud.",
        "<b>A dot under t, d, n</b> (<i>ṭ, ḍ, ṇ</i>) means a <i>hard</i> sound with the tongue curled back — only in borrowed words."],
    standard="standard Bodo as spoken around Kokrajhar",
    hello=[
        ("Who speaks it?", "About <b>1.5 million people</b> speak Bodo (also spelled <i>Boro</i>).<sup>³</sup>"),
        ("Where?", "In <b>Assam</b>, in north-east India, mostly in <b>Bodoland</b> on the north bank of the great "
                   "<b>Brahmaputra</b> river (Kokrajhar, Baksa, Udalguri), and nearby."),
        ("How is it written?", "In the <b>Devanagari</b> script, from <b>left to right</b>. Bodo writers chose Devanagari in the 1970s."),
        ("A different family", "Bodo is <b>not</b> a cousin of Hindi. It belongs to the <b>Tibeto-Burman</b> family, with Dimasa, "
                               "Garo and Tiwa — so it uses Devanagari letters for quite different sounds."),
        ("How many letters?", "This book teaches <b>44</b>: <b>11 vowels</b> and <b>33 consonants</b>. Many are "
                              "<b>rare in Bodo</b> and used only in borrowed words — those pages say so."),
        ("Did you know?", "Bodo weavers are famous for the bright <span class='nt'>दखना</span> <i>dokhnaa</i> cloth. "
                          "In <b>2003</b> Bodo became one of India’s official languages.<sup>³</sup>"),
    ],
    hello_pics=[("mai_bamboo", {}), ("banana", {}), ("brx_orange", {})],
    map=south_asia_map(
        points=dict(kokrajhar=[90.27, 26.40], udalguri=[92.10, 26.75], guwahati=[91.74, 26.14], area=[91.1, 26.6], label=[90.4, 29.4]),
        area=(42, 16, -8), label="BODOLAND",
        cities=[("kokrajhar", "Kokrajhar", -8, 26, "end", True), ("udalguri", "Udalguri", 10, -6, "start", False)],
        marker=[91.2, 26.6], caption="The circle shows Bodoland in Assam on the world map.", frame=[[66.5, 6.0], [98.0, 33.5]],
        legend="<b>Color it:</b> Bodoland (inside the dashed line) <b>yellow</b> · the rest of the land <b>green</b> · the seas <b>blue</b>. "
               "Draw the wide Brahmaputra river just below it! <b>Find it:</b> Kokrajhar ★ is the main town of Bodoland."),
    digits=[("०", "शून्य", "shunyo", "zero"), ("१", "से", "se", "one"), ("२", "नै", "nwi", "two"), ("३", "थाम", "thaam", "three"),
            ("४", "ब्रै", "brwi", "four"), ("५", "बा", "baa", "five"), ("६", "द" + APOS, "do", "six"), ("७", "स्नि", "sni", "seven"),
            ("८", "दाइन", "daain", "eight"), ("९", "गु", "gu", "nine")],
    phrases=[("अस्सलामु अलैकुम", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("व अलैकुम अस्सलाम", "va alaikum assalaam", "And upon you be peace (the reply)"),
             ("आंनि मुंआ …", "aangni mung-aa …", "My name is …"),
             ("सबैकोर", "sabwikor", "Thank you"),
             ("जज़ाकल्लाहु ख़ैरन", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("आइ · आफा", "aai · aaphaa", "Mother · Father"),
             ("आदा · आबो", "aadaa · aabw", "Big brother · Big sister"),
             ("नंगौ · नङा", "nwngwu · nongaa", "Yes (it is) · No (it is not)"),
             ("आं बर" + APOS + " राव सोलोंदों!", "aang boro raao swlwngdwng!", "I am learning Bodo!")],
    cheer=("माशाअल्लाह! जोबोद मोजां!", "maashaa-allaah! jwbwd mwjaang!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the Census of India 2011; the 2003 date from the "
                 "<b>Constitution of India</b> (92nd Amendment).",
    book_pic=dict(left="अ आ इ", right="क ख ग"),
    review_note="Drafted from general knowledge, not from a Bodo dictionary (bihung.org, the Bodo Sahitya Sabha dictionary, would be "
                "the place to check): every word, spelling and transliteration needs a Bodo speaker. Decisions to confirm: "
                "(1) the letter set — 11 vowels without ऋ and अः, 33 consonants without क्ष त्र ज्ञ; (2) that ो/ै/ौ stand for "
                "/ɯ/, /ɯi/, /ɯu/ and are transliterated w, wi, wu; (3) the apostrophe (’) in बर’ and द’. Words to check first: "
                "इटा, उवा (bamboo), एन्दि, ओंखाम, बिफां, खिरकि, गामि, घरि, रङ, चामुच, जोमै, टिफिन, डाब, तरमुज, दैमा, नाउ, "
                "फान्थौ, मुलि, लामा, वाट (fire), शरबत, हाथोरखि; the numbers (especially द’ six, दाइन eight, गु nine, and whether "
                "children count with मोन-: मोनसे, मोननै…); the phrases आंनि मुंआ, सबैकोर, आइ · आफा, आदा · आबो, नंगौ · नङा, "
                "आं बर’ राव सोलोंदों; the title आंनि गिबि बर’ आखर, बे बिजाबआ आंनि, अनजिमा, गिबि सोदोब and मोजां.",
    tiles="अआकखगम", cover_pics=["mai_bamboo", "banana", "flower", "mosque"], title_size=52,
    speakers_blurb="Bodo is spoken by about 1.5 million people in Assam, along the great Brahmaputra river.",
    sample_words=[("दै", "dwi", "water"), ("सान", "saan", "sun"), ("बिबार", "bibaar", "flower")],
    keywords=["bodo alphabet book for kids", "learn bodo for children", "boro language letters tracing",
              "bodo devanagari workbook", "muslim kids activity book", "islamic coloring book for children",
              "assam heritage language gift"],
))
