# -*- coding: utf-8 -*-
"""Book 83 - Guaraní (Paraguayan Guaraní, the 33-letter achegety: 12 vowels incl. Ã Ẽ Ĩ Õ Ũ Ỹ, G̃, the puso ʼ and the
digraphs CH MB ND NG NT RR). Allamahul Bayan Series. REVIEW DRAFT. Modelled on languages/es.py.

Fonts: Baloo 2 has no mark anchors for the combining tilde, so G̃ (G + U+0303, there is no precomposed letter) comes out
with the tilde sunk into the G. Nunito positions it correctly (tildecomb.case), so this book uses Nunito 800 for the big
letters and Nunito for all text:
  - Nunito latin has G g + U+0303 and the puso U+02BC;
  - Ĩ ĩ Ũ ũ Ỹ ỹ are in Nunito latin-ext; Ẽ ẽ only in Nunito vietnamese.
U+0303 is deliberately left OUT of the vietnamese unicode-range so that g̃ is shaped as one cluster by the latin face."""
from generic import build, letter, section
from maps import region_map

PH = "Guaraní letter name"
VIET = "U+0300-0301,U+0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9"
LATEXT = "U+0100-024F,U+1E00-1E9F,U+1EF2-1EFF"
FONTS = []
for w in (400, 700, 800):
    FONTS += [("Nunito", w, "normal", f"nunito-latin-ext-{w}-normal.woff2", LATEXT),
              ("Nunito", w, "normal", f"nunito-vietnamese-{w}-normal.woff2", VIET)]
GLYPH_FONTS = ["nunito-latin-800-normal.woff2", "nunito-latin-ext-800-normal.woff2", "nunito-vietnamese-800-normal.woff2"]


def L(big, show, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{show} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


NASAL = "a tilde (~) means: say it through your nose"
LETTERS = [
    L("Aa", "A a", "a", "ah", "‘a’ as in “father”", "avati", "ah-vah-TEE", "corn, maize", "corn"),
    L("Ãã", "Ã ã", "ã", "ahn", "‘ah’ said through the nose", "pytã", "pih-TAHN", "red — color the apple red!", "apple",
      rule=f"a = ah · ã = ahn · {NASAL}", note="Ã hardly ever starts a word. Find it at the end of <i>pytã</i>!"),
    L("Ch ch", "Ch ch", "che", "sheh", "‘sh’ as in “ship”", "chipa", "SHEE-pah", "chipa (a ring of cheese bread)", "ru_bagel",
      note="<b>Ch</b> is two letters that make one sound — Guaraní counts it as one letter."),
    L("Ee", "E e", "e", "eh", "‘e’ as in “bed”", "eíra", "eh-EE-rah", "honey", "honey"),
    L("Ẽẽ", "Ẽ ẽ", "ẽ", "ehn", "‘eh’ said through the nose", "takuareʼẽ", "tah-kwah-reh-’EHN", "sugarcane (“sweet cane”)", "sugarcane",
      rule=f"e = eh · ẽ = ehn · {NASAL}", note="Ẽ hardly ever starts a word. Find it at the end of <i>takuareʼẽ</i>!"),
    L("Gg", "G g", "ge", "geh", "a soft ‘g’, as in “go” said gently", "guembe", "gwem-BEH", "guembe (a big split-leaf plant)",
      "gn_guembe"),
    L("G̃g̃", "G̃ g̃", "g̃e", "geh (nasal)", "a soft ‘g’ said through the nose — a special Guaraní letter!", "koʼág̃a", "koh-’AH-ngah",
      "now (look at the clock!)", "clock", rule="g = soft g · g̃ = the same g, but through the nose",
      note="G̃ never starts a word. Find it inside <i>koʼág̃a</i>!"),
    L("Hh", "H h", "he", "heh", "‘h’ as in “hat”", "hyʼa", "hih-’AH", "calabash bowl", "ff_calabash"),
    L("Ii", "I i", "i", "ee", "‘ee’ as in “see”", "ita", "ee-TAH", "stone", "mni_stones"),
    L("Ĩĩ", "Ĩ ĩ", "ĩ", "een", "‘ee’ said through the nose", "peteĩ", "peh-teh-EEN", "one", "one",
      rule=f"i = ee · ĩ = een · {NASAL}", note="Ĩ hardly ever starts a word. Find it at the end of <i>peteĩ</i>!"),
    L("Jj", "J j", "je", "jeh", "‘j’ as in “jam” (some people say ‘y’ as in “yes”)", "jasy", "jah-SIH", "moon", "moon"),
    L("Kk", "K k", "ke", "keh", "‘k’ as in “kite” (no puff of air)", "kuarahy", "kwah-rah-HIH", "sun", "sun"),
    L("Ll", "L l", "le", "leh", "‘l’ as in “lamp” — mostly in borrowed words", "limõ", "lee-MOHN", "lemon", "lemon",
      note="L is used mostly in words borrowed from Spanish, like <i>limõ</i> (from <i>limón</i>)."),
    L("Mm", "M m", "me", "meh", "‘m’ as in “moon”", "mandiʼo", "mahn-dee-’OH", "cassava (a root we cook and eat)", "gn_mandio"),
    L("Mb mb", "Mb mb", "mbe", "mbeh", "‘m’ and ‘b’ said together, as in “ti<b>mb</b>er”", "mbokaja", "mboh-kah-JAH",
      "mbokaja palm tree", "ms_palm", note="<b>Mb</b> is two letters that make one sound — Guaraní counts it as one letter."),
    L("Nn", "N n", "ne", "neh", "‘n’ as in “net”", "narãha", "nah-rahn-HAH", "orange", "ig_orange"),
    L("Nd nd", "Nd nd", "nde", "ndeh", "‘n’ and ‘d’ said together, as in “ca<b>nd</b>y”", "andai", "ahn-dah-EE", "pumpkin, squash",
      "ar_pumpkin", note="<b>Nd</b> counts as one letter. Find it inside <i>andai</i>!"),
    L("Ng ng", "Ng ng", "nge", "ngeh", "‘n’ and ‘g’ said together, as in “fi<b>ng</b>er”", "mangá", "mahn-GAH", "mango", "mango",
      note="<b>Ng</b> counts as one letter. Find it inside <i>mangá</i>!"),
    L("Nt nt", "Nt nt", "nte", "nteh", "‘n’ and ‘t’ said together, as in “ce<b>nt</b>er”", "mentaʼi", "men-tah-’EE",
      "mint (a little herb)", "hy_basil", note="<b>Nt</b> counts as one letter. Find it inside <i>mentaʼi</i>!"),
    L("Ññ", "Ñ ñ", "ñe", "nyeh", "‘ny’ as in “canyon”", "ñanduti", "nyahn-doo-TEE", "ñanduti (Paraguay’s round lace)", "gn_nanduti"),
    L("Oo", "O o", "o", "oh", "‘o’ as in “go” (short and pure)", "óga", "OH-gah", "house", "house"),
    L("Õõ", "Õ õ", "õ", "ohn", "‘oh’ said through the nose", "mokõi", "moh-kohn-EE", "two", "ka_two",
      rule=f"o = oh · õ = ohn · {NASAL}", note="Õ hardly ever starts a word. Find it inside <i>mokõi</i>!"),
    L("Pp", "P p", "pe", "peh", "‘p’ as in “pen” (no puff of air)", "pakova", "pah-koh-VAH", "banana", "banana"),
    L("Rr", "R r", "re", "reh", "a quick tapped ‘r’, as in Spanish “pero”", "arasa", "ah-rah-SAH", "guava", "mai_guava",
      note="R does not start Guaraní words (only borrowed ones). Find it inside <i>arasa</i>!"),
    L("rr", "rr", "rre", "rreh", "a rolled ‘r’ — let your tongue buzz!", "karréta", "kah-RREH-tah", "cart (an ox cart)", "cart",
      note="<b>Rr</b> counts as one letter. It never starts a word and is found in borrowed words like <i>karréta</i>."),
    L("Ss", "S s", "se", "seh", "‘s’ as in “sun”", "sã", "sahn", "rope, string", "ff_rope"),
    L("Tt", "T t", "te", "teh", "‘t’ as in “top” (no puff of air)", "tata", "tah-TAH", "fire", "lo_fire"),
    L("Uu", "U u", "u", "oo", "‘oo’ as in “moon”", "uruku", "oo-roo-KOO", "annatto (a plant with red seeds)", "gn_uruku"),
    L("Ũũ", "Ũ ũ", "ũ", "oon", "‘oo’ said through the nose", "pytũ", "pih-TOON", "night, darkness — when the stars come out", "star",
      rule=f"u = oo · ũ = oon · {NASAL}", note="Ũ hardly ever starts a word. Find it at the end of <i>pytũ</i>!"),
    L("Vv", "V v", "ve", "veh", "a soft ‘v’, almost like ‘w’", "yvoty", "ih-voh-TIH", "flower", "flower",
      note="Find V inside <i>yvoty</i>!"),
    L("Yy", "Y y", "y", "ih", "a special vowel! Say ‘ee’, but pull your tongue back as if to say ‘oo’ (the ‘i’ in “roses”)", "y", "ih",
      "water", "water", rule="In Guaraní, Y is always a <b>vowel</b>: y = water, yvy = earth, yvága = sky"),
    L("Ỹỹ", "Ỹ ỹ", "ỹ", "ihn", "the special vowel y, said through the nose", "kyʼỹi", "kih-’IHN-ee", "chili pepper", "mni_chilli",
      rule=f"y = ih · ỹ = ihn · {NASAL}", note="Ỹ hardly ever starts a word. Find it inside <i>kyʼỹi</i>!"),
    L("ʼ", "ʼ", "puso", "POO-soh", "a tiny stop in the voice, like the break in “uh-oh”", "kaʼa", "kah-’AH",
      "yerba mate (the herb for mate tea)", "gn_mate", rule="ka-a with a stop in the middle: ka<b>ʼ</b>a",
      note="The <b>puso</b> is a letter too! It never starts a word: it sits between two vowels and tells you to stop for a moment."),
]

LANG = build(dict(
    code="gn", folder="book-83-guarani", series_no=83, isbn="", draft=True,
    name="Guaraní", native="avañeʼẽ", native_tr="ah-vah-nyeh-’EHN", name_word="téra", write_word="ehai",
    title_native="Che achegety guarani", title_letters="AaÑñỸỹ", belongs_native="Ko aranduka imbaʼe",
    belongs_pic="gn_nanduti", alphabet_native="achegety", numbers_native="papapy", numbers_tr="pah-pah-PIH",
    phrases_native="Ñeʼẽ ñepyrũrã",
    fonts=FONTS, disp_family="Nunito", text_family="Nunito",
    glyph_font=GLYPH_FONTS, font_credit="Nunito",
    phon_feature="each letter’s Guaraní name (A «a», CH «che», G̃ «g̃e»…)",
    sections=[section(LETTERS, native="achegety", native_tr="ah-sheh-geh-TIH — “the alphabet”", chart_cols=6, warmup_cols=6,
                      intro_html="""<p>The Guaraní alphabet, the <b>achegety</b>, has <b>33 letters</b>. It has no B, C, D, F, Q, W, X or Z of its own,
but it has letters English does not have!</p>
<div class="box" style="margin:0.1in 0"><h3>Twelve vowels</h3><b>A E I O U Y</b> are said through the mouth, and <b>Ã Ẽ Ĩ Õ Ũ Ỹ</b> — with a
tilde (~) — are said through the nose. <b>Y</b> is always a vowel: it sounds like ‘ee’ with the tongue pulled back.</div>
<div class="box" style="margin:0.1in 0"><h3>Pairs that are one letter</h3><b>ch · mb · nd · ng · nt · rr</b> are written with two letters but
count as <b>one</b> letter each. And <b>G̃</b> is a soft g said through the nose.</div>
<div class="box" style="margin:0.1in 0"><h3>The puso ʼ</h3>This little mark is a real letter: a tiny stop in the voice, as in <i>kaʼa</i> (yerba mate).</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> show the stressed syllable: <i>kwah-rah-HIH</i> means “say HIH a little louder”. Most Guaraní words are "
        "stressed on the <b>last</b> syllable.",
        "<b>n</b> after a vowel in the pronunciation (<i>ahn, ehn, een, ohn, oon, ihn</i>) means the vowel is said through the nose.",
        "<b>ih</b> is the special Guaraní vowel Y: say ‘ee’ with your tongue pulled back.",
        "<b>’</b> in the pronunciation is the puso: a tiny stop, like the break in “uh-oh”."],
    phon_explain="The box marked <i>Guaraní letter name</i> shows the name Paraguayan children use for the letter "
                 "(CH is «che», G̃ is «g̃e», ʼ is «puso») and, for the nasal vowels, how they differ from the plain ones.",
    standard="Paraguayan Guaraní (the spelling of the Academia de la Lengua Guaraní)",
    hello=[
        ("Who speaks it?", "About <b>6 million people</b> speak Guaraní.<sup>³</sup> In Paraguay most people speak it — in the home, at "
                           "school and at the market."),
        ("Where?", "In <b>Paraguay</b>, where it is an official language together with Spanish, and in nearby parts of "
                   "<b>Argentina</b>, <b>Bolivia</b> and <b>Brazil</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with a tilde for nasal vowels (ã ẽ ĩ õ ũ ỹ g̃) and "
                               "the <b>puso</b> (ʼ)."),
        ("How many letters?", "<b>33 letters</b>: 12 vowels, the puso and 20 consonants — six of them written with two letters "
                              "(ch, mb, nd, ng, nt, rr)."),
        ("A language of nature", "Many plant names come from Guaraní: <i>mandiʼo</i> (cassava), <i>arasa</i> (guava) and "
                                 "<i>kaʼa</i>, the yerba mate leaf."),
        ("Did you know?", "English words like <i>tapioca</i> and <i>maraca</i> come from the Tupi–Guaraní family of languages, "
                          "the family Guaraní belongs to."),
    ],
    hello_pics=[("gn_nanduti", {}), ("gn_mate", {}), ("mosque", {})],
    map=region_map(frame=[[-72.0, -38.0], [-40.0, -8.0]],
                   points=dict(asuncion=[-57.58, -25.28], cde=[-54.61, -25.51], encarnacion=[-55.87, -27.33],
                               concepcion=[-57.43, -23.41]),
                   area=(-58.3, -23.4, 150, 155),
                   cities=[("asuncion", "Asunción", -18, 8, "end", True), ("cde", "Ciudad del Este", 14, -10, "start", False),
                           ("encarnacion", "Encarnación", 14, 20, "start", False), ("concepcion", "Concepción", 14, 8, "start", False)],
                   label="PARAGUAY", label_at=[-58.3, -17.0], marker=[-58.0, -23.0],
                   caption="The circle shows Paraguay on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Paraguay is in the middle of "
                          "South America, far from the sea. Guaraní is spoken in Asunción (the star), Concepción, Ciudad del Este and "
                          "Encarnación. The dashed line shows where most Guaraní speakers live.",
                   seas=[("Atlantic Ocean", -45.0, -31.0)], world_r=16),
    digits=[("0", "mbaʼeve", "mbah-’eh-VEH", "zero (nothing)"), ("1", "peteĩ", "peh-teh-EEN", "one"), ("2", "mokõi", "moh-kohn-EE", "two"),
            ("3", "mbohapy", "mboh-ah-PIH", "three"), ("4", "irundy", "ee-roon-DIH", "four"), ("5", "po", "poh", "five"),
            ("6", "poteĩ", "poh-teh-EEN", "six"), ("7", "pokõi", "poh-kohn-EE", "seven"), ("8", "poapy", "poh-ah-PIH", "eight"),
            ("9", "porundy", "poh-roon-DIH", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Mbaʼéichapa!", "mbah-’AY-shah-pah", "Hello! How are you?"),
             ("Che réra …", "sheh REH-rah …", "My name is …"),
             ("Aguyje!", "ah-goo-JEH", "Thank you!"),
             ("Jazakallahu khairan", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("che sy · che ru", "sheh SIH · sheh ROO", "My mother · My father"),
             ("che kyvy · che reindy", "sheh kih-VIH · sheh reh-een-DIH", "My brother · My sister"),
             ("heẽ · nahániri", "heh-EHN · nah-HAH-nee-ree", "Yes · No"),
             ("Ahekomboʼe hína guarani!", "ah-heh-kohm-boh-’EH HEE-nah gwah-rah-NEE", "I am learning Guaraní!")],
    cheer=("Mashallah! Iporãite!", "MAH-shah-lah! ee-poh-rahn-ee-TEH!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A Ã CH", right="Ñ Y ʼ"),
    review_note="Check: the letter order (puso placed last) and the letter names (che, g̃e, mbe, rre, puso); the words "
                "<i>koʼág̃a</i> for G̃, <i>hyʼa</i> for H, <i>narãha</i> for N, <i>mentaʼi</i> for NT, <i>kyʼỹi</i> for Ỹ, "
                "<i>guembe</i> for G, <i>karréta</i> for RR, <i>chipa</i> (stress, accent) and <i>mbaʼeve</i> for zero; the phrases "
                "<i>Ko aranduka imbaʼe</i>, <i>Ñeʼẽ ñepyrũrã</i>, <i>Ahekomboʼe hína guarani</i> and <i>che kyvy · che reindy</i> "
                "(kyvy is a girl’s word for brother, reindy a boy’s word for sister); and the stress marks in all sound guides.",
    tiles="AÃẼÑỸJ", cover_pics=["gn_nanduti", "sun", "banana", "mosque"], title_size=48,
    speakers_blurb="Guaraní is spoken by about 6 million people, most of them in Paraguay.",
    sample_words=[("kuarahy", "kwah-rah-HIH", "sun"), ("jasy", "jah-SIH", "moon"), ("pakova", "pah-koh-VAH", "banana")],
    keywords=["guarani alphabet book for kids", "learn guarani for children", "paraguay guarani coloring book",
              "guarani letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual guarani english toddlers"],
))
