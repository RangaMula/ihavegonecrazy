# -*- coding: utf-8 -*-
"""Book 80 - Spanish (Latin script, 27 letters). Allamahul Bayan Series. REVIEW DRAFT.
Reference example for Latin-script languages: big letter = capital + small ("Aa")."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Spanish letter name"
def L(cap, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {cap.lower()} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(cap + cap.lower(), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)

LETTERS = [
    L("A", "a", "ah", "‘a’ as in “father”", "agua", "AH-gwah", "water", "water"),
    L("B", "be", "beh", "‘b’ as in “ball” (softer between vowels)", "barco", "BAR-koh", "ship", "ship"),
    L("C", "ce", "seh", "‘k’ before a, o, u; ‘s’ (Latin America) before e, i", "casa", "KAH-sah", "house", "house",
      rule="ca, co, cu = ka, ko, ku · ce, ci = se, si"),
    L("D", "de", "deh", "a soft ‘d’ with the tongue on the teeth", "dátiles", "DAH-tee-les", "dates", "dates"),
    L("E", "e", "eh", "‘e’ as in “bed”", "estrella", "es-TREH-yah", "star", "star"),
    L("F", "efe", "EH-feh", "‘f’ as in “fan”", "flor", "flor", "flower", "flower"),
    L("G", "ge", "heh", "‘g’ as in “go” before a, o, u; a breathy ‘h’ before e, i", "globo", "GLOH-boh", "balloon", "balloon",
      rule="ga, go, gu = ga, go, gu · ge, gi = he, hi"),
    L("H", "hache", "AH-cheh", "silent! H makes no sound in Spanish", "helado", "eh-LAH-doh", "ice cream", "ice",
      note="H is always silent: <i>helado</i> sounds like “eh-LAH-doh”."),
    L("I", "i", "ee", "‘ee’ as in “see”", "isla", "EES-lah", "island", "waves"),
    L("J", "jota", "HOH-tah", "a breathy ‘h’ from the throat", "jarra", "HAH-rrah", "jug", "ewer"),
    L("K", "ka", "kah", "‘k’ as in “kite” — used only in borrowed words", "kiwi", "KEE-wee", "kiwi fruit", "lemon"),
    L("L", "ele", "EH-leh", "‘l’ as in “lamp”", "luna", "LOO-nah", "moon", "moon"),
    L("M", "eme", "EH-meh", "‘m’ as in “moon”", "mezquita", "mes-KEE-tah", "mosque", "mosque"),
    L("N", "ene", "EH-neh", "‘n’ as in “net”", "nube", "NOO-beh", "cloud", "clouds"),
    L("Ñ", "eñe", "EH-nyeh", "‘ny’ as in “canyon” — a Spanish letter!", "piña", "PEE-nyah", "pineapple", "pineapple",
      note="Ñ hardly ever starts a word. Find it in the middle of <i>piña</i>!"),
    L("O", "o", "oh", "‘o’ as in “go” (short and pure)", "ojo de agua", "OH-hoh deh AH-gwah", "spring of water", "dew"),
    L("P", "pe", "peh", "‘p’ as in “pen” (no puff of air)", "pelota", "peh-LOH-tah", "ball", "ball"),
    L("Q", "cu", "koo", "‘k’ — always written “qu” before e or i", "queso", "KEH-soh", "cheese", "box",
      rule="que, qui = ke, ki (the u is silent)"),
    L("R", "erre", "EH-rreh", "a tapped ‘r’; rolled at the start of a word or as rr", "reloj", "rreh-LOH", "clock", "clock"),
    L("S", "ese", "EH-seh", "‘s’ as in “sun”", "sol", "sohl", "sun", "sun"),
    L("T", "te", "teh", "a soft ‘t’ with the tongue on the teeth", "tomate", "toh-MAH-teh", "tomato", "tomato"),
    L("U", "u", "oo", "‘oo’ as in “moon”", "uvas", "OO-vahs", "grapes", "grapes"),
    L("V", "uve", "OO-veh", "sounds like a soft ‘b’", "ventana", "ben-TAH-nah", "window", "window"),
    L("W", "uve doble", "OO-veh DOH-bleh", "‘w’ as in “water” — only in borrowed words", "wafle", "WAH-fleh", "waffle", "roti"),
    L("X", "equis", "EH-kees", "‘ks’ as in “taxi” (and ‘h’ in México)", "xilófono", "see-LOH-foh-noh", "xylophone — a row of bars", "brick",
      note="X is rare at the start of a word: there it sounds like ‘s’."),
    L("Y", "ye", "yeh", "‘y’ as in “yes”; alone it means “and” and says ‘ee’", "yate", "YAH-teh", "yacht", "boat"),
    L("Z", "zeta", "SEH-tah", "‘s’ in Latin America; ‘th’ as in “think” in Spain", "zanahoria", "sah-nah-OH-ryah", "carrot", "carrot"),
]

LANG = build(dict(
    code="es", folder="book-80-spanish", series_no=80, isbn="", draft=True,
    name="Spanish", native="español", native_tr="es-pah-NYOL", name_word="nombre", write_word="escribe",
    title_native="Mi primer abecedario en español", title_letters="AaBbCc", belongs_native="Este libro es de",
    belongs_pic="star", alphabet_native="el abecedario", numbers_native="los números", numbers_tr="lohs NOO-meh-rohs",
    phrases_native="Primeras palabras",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Spanish name (A «a», B «be», C «ce»…)",
    sections=[section(LETTERS, native="el abecedario", native_tr="el ah-beh-seh-DAH-ryoh — “the A-B-C”",
                      chart_cols=7, warmup_cols=6,
                      intro_html="""<p>Spanish uses the same letters as English, plus one of its own: <b>Ñ</b>. That makes <b>27 letters</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Easy to read aloud</h3>Spanish is written almost exactly as it sounds. Once you know each letter’s sound,
you can read nearly any Spanish word!</div>
<div class="box" style="margin:0.1in 0"><h3>Five pure vowels</h3><b>A E I O U</b> always say <i>ah, eh, ee, oh, oo</i> — short and clear, never sliding
like English “o” in “go”.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>KAH-sah</i> means “say KAH a little louder”.",
        "<b>rr</b> means a rolled ‘r’ — let your tongue buzz!",
        "<b>h</b> in the pronunciation is a breathy ‘h’ (the sound of Spanish J); Spanish letter H itself is silent.",
        "Sounds follow Latin American Spanish; in Spain, Z and soft C sound like ‘th’ in “think”."],
    phon_explain="The box marked <i>Spanish letter name</i> shows the name Spanish children use for the letter "
                 "(B is «be», H is «hache»…) and any spelling rule that changes its sound.",
    standard="Latin American Spanish",
    hello=[
        ("Who speaks it?", "About <b>560 million people</b> speak Spanish — one of the most spoken languages in the world.<sup>³</sup>"),
        ("Where?", "In <b>Spain</b> and in most of <b>Latin America</b>, from Mexico to Argentina, and by many families in the United States."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with one extra letter, <b>Ñ</b>, and accents on some vowels (á é í ó ú)."),
        ("How many letters?", "<b>27 letters</b>: the 26 of English plus <b>Ñ</b>."),
        ("Upside-down marks!", "Spanish questions start with <b>¿</b> and exclamations with <b>¡</b>: ¿Cómo estás? ¡Hola!"),
        ("Did you know?", "Spanish has thousands of words from Arabic, from the time of al-Andalus: <i>aceite</i> (oil), <i>azúcar</i> (sugar), "
                          "<i>almohada</i> (pillow) and <i>ojalá</i> (“if Allah wills”)."),
    ],
    hello_pics=[("star", {}), ("pineapple", {}), ("mosque", {})],
    map=region_map(frame=[[-120.0, -56.0], [-34.0, 32.0]],
                   points=dict(mexico=[-99.13, 19.43], bogota=[-74.07, 4.71], lima=[-77.04, -12.05], buenosaires=[-58.38, -34.60]),
                   area=None, cities=[("mexico", "Mexico City", 14, 8, "start", False), ("bogota", "Bogotá", 14, 8, "start", False),
                                      ("lima", "Lima", -14, 8, "end", False), ("buenosaires", "Buenos Aires", 14, 8, "start", False)],
                   label="LATIN AMERICA", label_at=[-85.0, 24.0], marker=[-70.0, -10.0],
                   caption="The circle shows Latin America on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the oceans <b>blue</b>. <b>Find it:</b> Spanish is spoken in Mexico City, Bogotá, Lima, "
                          "Buenos Aires and in most countries of Central and South America (and in Spain, across the ocean).",
                   seas=[("Pacific Ocean", -100.0, -15.0), ("Atlantic Ocean", -40.0, 5.0)], world_r=30),
    digits=[("0", "cero", "SEH-roh", "zero"), ("1", "uno", "OO-noh", "one"), ("2", "dos", "dohs", "two"), ("3", "tres", "trehs", "three"),
            ("4", "cuatro", "KWAH-troh", "four"), ("5", "cinco", "SEEN-koh", "five"), ("6", "seis", "says", "six"), ("7", "siete", "SYEH-teh", "seven"),
            ("8", "ocho", "OH-choh", "eight"), ("9", "nueve", "NWEH-veh", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("¡Hola!", "OH-lah", "Hello!"),
             ("Me llamo …", "meh YAH-moh …", "My name is …"),
             ("Gracias", "GRAH-syahs", "Thank you"),
             ("Jazakallahu jairan", "jah-zah-KAH-lah-hoo HAI-rahn", "May Allah reward you with good"),
             ("mamá · papá", "mah-MAH · pah-PAH", "Mother · Father"),
             ("hermano · hermana", "er-MAH-noh · er-MAH-nah", "Brother · Sister"),
             ("sí · no", "see · noh", "Yes · No"),
             ("¡Estoy aprendiendo español!", "es-TOY ah-pren-DYEN-doh es-pah-NYOL", "I am learning Spanish!")],
    cheer=("¡Mashallah! ¡Muy bien!", "MAH-shah-lah! mwee byen!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the <b>Instituto Cervantes</b>.",
    book_pic=dict(left="A B C", right="D E F"),
    review_note="Check stress marks in the pronunciation guide and choose Latin American or Spain spellings/sounds consistently.",
    tiles="AÑBCDE", cover_pics=["pineapple", "star", "balloon", "mosque"], title_size=48,
    speakers_blurb="Spanish is spoken by about 560 million people in Latin America, Spain and around the world.",
    sample_words=[("luna", "LOO-nah", "moon"), ("flor", "flor", "flower"), ("piña", "PEE-nyah", "pineapple")],
    keywords=["spanish alphabet book for kids", "learn spanish for children", "spanish abecedario coloring",
              "spanish letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual spanish english toddlers"],
))
