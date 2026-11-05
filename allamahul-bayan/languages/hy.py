# -*- coding: utf-8 -*-
"""Book 35 - Armenian (Armenian script, 39 letters as taught in Armenia today). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Աա"). Pronunciation and letter names follow Eastern Armenian."""
from generic import build, letter, section
from maps import region_map

PH = "Armenian letter name"
F = "noto-sans-armenian-armenian"


def Lt(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, big=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:3px">{rule}</div>' if rule else ""))
    return letter(big or (cap + small), name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


PUFF = " with a little puff of air, as in English"
NOPUFF = " without a puff of air (hold a hand in front of your mouth: it should not move)"

LETTERS = [
    Lt("Ա", "ա", "այբ", "ayb", "‘a’ as in “father”", "աստղ", "astgh", "star", "star"),
    Lt("Բ", "բ", "բեն", "ben", "‘b’ as in “ball”", "բանան", "ba-NAN", "banana", "banana"),
    Lt("Գ", "գ", "գիմ", "geem", "‘g’ as in “go”", "գնդակ", "guhn-DAK", "ball", "ball"),
    Lt("Դ", "դ", "դա", "da", "‘d’ as in “door”", "դուռ", "doorr", "door", "door",
       note="Say it out loud: Armenian <span class='nt'>դուռ</span> sounds almost like English “door”!"),
    Lt("Ե", "ե", "եչ", "yech", "‘ye’ as in “yes” at the start of a word; ‘e’ as in “bed” inside a word",
       "ելակ", "ye-LAK", "strawberry", "hy_strawberry"),
    Lt("Զ", "զ", "զա", "za", "‘z’ as in “zoo”", "զամբյուղ", "zam-BYOOGH", "basket", "basket"),
    Lt("Է", "է", "է", "e", "‘e’ as in “bed” (it never says ‘ye’)", "էջ", "ej", "page (of a book)", "book",
       args=dict(left="Ա Բ Գ", right="Դ Ե Զ")),
    Lt("Ը", "ը", "ըթ", "uht", "a short, soft ‘uh’, like the ‘a’ in “about”", "ընկույզ", "uhn-KOOYZ", "walnut", "walnut"),
    Lt("Թ", "թ", "թո", "to", "‘t’" + PUFF + " “top”", "թեյ", "tey", "tea", "teacup"),
    Lt("Ժ", "ժ", "ժե", "zhe", "‘zh’, like the ‘s’ in “treasure”", "ժամացույց", "zha-ma-TSOOYTS", "clock", "clock"),
    Lt("Ի", "ի", "ինի", "ee-NEE", "‘ee’ as in “see”", "ինքնաթիռ", "een-kuh-na-TEERR", "aeroplane", "plane"),
    Lt("Լ", "լ", "լյուն", "lyoon", "‘l’ as in “lemon”", "լուսին", "loo-SEEN", "moon", "moon"),
    Lt("Խ", "խ", "խե", "khe", "a scratchy ‘kh’ from the back of the throat, like ‘ch’ in Scottish “loch”",
       "խնձոր", "khuhn-DZOR", "apple", "apple"),
    Lt("Ծ", "ծ", "ծա", "tsa", "‘ts’ as in “cats”" + NOPUFF, "ծաղիկ", "tsa-GHEEK", "flower", "flower"),
    Lt("Կ", "կ", "կեն", "ken", "‘k’" + NOPUFF, "կիտրոն", "keet-RON", "lemon", "lemon"),
    Lt("Հ", "հ", "հո", "ho", "‘h’ as in “hat”", "հովանոց", "ho-va-NOTS", "umbrella", "umbrella"),
    Lt("Ձ", "ձ", "ձա", "dza", "‘dz’ as in “kids”", "ձմերուկ", "dzuh-me-ROOK", "watermelon", "watermelon"),
    Lt("Ղ", "ղ", "ղատ", "ghat", "a soft, throaty ‘gh’, like a gargle (similar to the French ‘r’)", "աղ", "agh", "salt", "salt",
       args=dict(label="աղ"), note="Few words start with <span class='nt'>ղ</span>. Find it at the end of <span class='nt'>աղ</span>!"),
    Lt("Ճ", "ճ", "ճե", "che", "‘ch’ as in “church”" + NOPUFF, "ճրագ", "chuh-RAG", "oil lamp", "hy_lamp"),
    Lt("Մ", "մ", "մեն", "men", "‘m’ as in “moon”", "մեղր", "meghr", "honey", "honey"),
    Lt("Յ", "յ", "յի", "yee", "‘y’ as in “yes”", "յոթ", "yot", "seven", "one", args=dict(digit="7")),
    Lt("Ն", "ն", "նու", "noo", "‘n’ as in “net”", "նուռ", "noorr", "pomegranate", "pomegranate"),
    Lt("Շ", "շ", "շա", "sha", "‘sh’ as in “ship”", "շուշան", "shoo-SHAN", "lily", "lily"),
    Lt("Ո", "ո", "ո", "vo", "‘vo’ at the start of a word; ‘o’ as in “dog” inside a word", "ոլոռ", "vo-LORR", "peas", "hy_peas"),
    Lt("Չ", "չ", "չա", "cha", "‘ch’" + PUFF + " “cheese”", "չամիչ", "cha-MEECH", "raisins (dried grapes)", "grapes"),
    Lt("Պ", "պ", "պե", "pe", "‘p’" + NOPUFF, "պատուհան", "pa-too-HAN", "window", "window"),
    Lt("Ջ", "ջ", "ջե", "je", "‘j’ as in “jam”", "ջուր", "joor", "water", "water"),
    Lt("Ռ", "ռ", "ռա", "rra", "a strong, rolled ‘rr’", "ռեհան", "rre-HAN", "basil", "hy_basil"),
    Lt("Ս", "ս", "սե", "se", "‘s’ as in “sun”", "սար", "sar", "mountain", "mountain"),
    Lt("Վ", "վ", "վեվ", "vev", "‘v’ as in “van”", "վարունգ", "va-ROONG", "cucumber", "hy_cucumber"),
    Lt("Տ", "տ", "տյուն", "tyoon", "‘t’" + NOPUFF, "տուն", "toon", "house", "house"),
    Lt("Ր", "ր", "րե", "re", "a soft, quick ‘r’ (just one tap of the tongue)", "ծիրան", "tsee-RAN", "apricot", "hy_apricot",
       note="No Armenian word starts with <span class='nt'>ր</span>. Find it in the middle of <span class='nt'>ծիրան</span>, "
            "the apricot — a famous Armenian fruit!"),
    Lt("Ց", "ց", "ցո", "tso", "‘ts’" + PUFF + " “cats”", "ցորեն", "tso-REN", "wheat", "hy_wheat"),
    Lt("Ու", "ու", "ու", "oo", "‘oo’ as in “moon”", "ուլունք", "oo-LOONK", "beads", "hy_beads", big="Ուու",
       rule="Two shapes, <span class='nt'>ո + ւ</span>, make one letter and one sound: ‘oo’."),
    Lt("Փ", "փ", "փյուր", "pyoor", "‘p’" + PUFF + " “pen”", "փուչիկ", "poo-CHEEK", "balloon", "balloon"),
    Lt("Ք", "ք", "քե", "ke", "‘k’" + PUFF + " “kite”", "քար", "kar", "stones", "hy_stones"),
    Lt("Եվ", "և", "և", "yev", "‘yev’ at the start of a word; ‘ev’ inside a word", "արև", "a-REV", "sun", "sun", big="և",
       note="<span class='nt'>և</span> is also a word on its own: it means “and”. Find it at the end of <span class='nt'>արև</span>!",
       rule="It joins <span class='nt'>ե + վ</span>. At the start of a sentence it is written <span class='nt'>Եվ</span>."),
    Lt("Օ", "օ", "օ", "o", "‘o’ as in “dog”", "օդապարուկ", "o-da-pa-ROOK", "kite", "kite"),
    Lt("Ֆ", "ֆ", "ֆե", "fe", "‘f’ as in “fan”", "ֆինիկ", "fee-NEEK", "dates", "dates"),
]

LANG = build(dict(
    code="hy", folder="book-35-armenian", series_no=35, isbn="", draft=True,
    name="Armenian", native="հայերեն", native_tr="ha-ye-REN", name_word="անուն", write_word="գրիր",
    title_native="Իմ առաջին այբուբենը", title_letters="ԱաԲբԳգ", belongs_native="Այս գիրքը պատկանում է",
    belongs_pic="pomegranate", alphabet_native="այբուբեն", numbers_native="թվեր", numbers_tr="tver",
    phrases_native="Առաջին բառեր",
    fonts=[("Noto Sans Armenian", w, "normal", f"{F}-{w}-normal.woff2", "U+0530-058F,U+FB13-FB17") for w in (400, 700, 800)],
    disp_family="Noto Sans Armenian", text_family="Noto Sans Armenian",
    glyph_font=[f"{F}-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Armenian",
    extra_css=".nt,.ntd,.lp-name{font-family:'Noto Sans Armenian','Nunito',sans-serif}",
    phon_feature="each letter’s Armenian name (Ա «այբ», Բ «բեն», Գ «գիմ»…)",
    sections=[section(LETTERS, native="այբուբեն", native_tr="ay-boo-BEN — “the alphabet”",
                      chart_cols=7, warmup_cols=7,
                      intro_html="""<p>The Armenian alphabet is called <span class="nt">այբուբեն</span> (<i>ay-boo-BEN</i>), from the names of its
first two letters, <span class="nt">այբ</span> and <span class="nt">բեն</span> — just like “alphabet” comes from <i>alpha</i> and <i>beta</i>.
Children in Armenia learn <b>39 letters</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Puff or no puff?</h3>Some letters come in pairs that sound almost the same.
<span class="nt">Թ</span>, <span class="nt">Փ</span>, <span class="nt">Ք</span>, <span class="nt">Չ</span>, <span class="nt">Ց</span> are said with a little
<b>puff of air</b>; <span class="nt">Տ</span>, <span class="nt">Պ</span>, <span class="nt">Կ</span>, <span class="nt">Ճ</span>, <span class="nt">Ծ</span>
are said with <b>no puff</b>. Hold a hand in front of your mouth and feel the difference!</div>
<div class="box" style="margin:0.1in 0"><h3>Two shapes, one letter</h3><span class="nt">ու</span> (‘oo’) and <span class="nt">և</span> (‘yev’)
are written with two joined shapes, but each one counts as a single letter.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt">Աա</span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable. In Armenian it is almost always the <b>last</b> one: "
        "<i>loo-SEEN</i>.",
        "<b>uh</b> is the short, soft sound of ‘a’ in “about” (letter <span class='nt'>ը</span>). Armenian often slips this sound in "
        "between two consonants without writing it: <span class='nt'>գնդակ</span> is said <i>guhn-DAK</i>.",
        "<b>kh</b> is a scratchy sound from the back of the throat (‘ch’ in Scottish “loch”); <b>gh</b> is its soft, gargled partner.",
        "<b>rr</b> is a strong rolled ‘r’; a single <b>r</b> is one quick tap of the tongue.",
        "<b>ee</b> as in “see”, <b>oo</b> as in “moon”, <b>e</b> as in “bed”, <b>o</b> as in “dog”, <b>a</b> as in “father”."],
    phon_explain="The box marked <i>Armenian letter name</i> shows the letter’s name written in Armenian (Ա is «այբ», Բ is «բեն»…), "
                 "and for some letters a short spelling tip.",
    standard="Eastern Armenian, as spoken in Armenia",
    hello=[
        ("Who speaks it?", "More than <b>5 million people</b> speak Armenian.<sup>³</sup>"),
        ("Where?", "In <b>Armenia</b>, a country of mountains between the Black Sea and the Caspian Sea, and in Armenian families "
                   "in many countries of the world."),
        ("How is it written?", "In its very own <b>Armenian alphabet</b>, from <b>left to right</b>, with capital and small letters."),
        ("How many letters?", "<b>39 letters</b> are taught in Armenia today, from <span class='nt'>Ա ա</span> to <span class='nt'>Ֆ ֆ</span>."),
        ("Did you know?", "The Armenian alphabet was created more than <b>1,600 years ago</b>, in the year 405, by the scholar "
                          "<b>Mesrop Mashtots</b>. Long ago its letters were also used as numbers!"),
        ("Two ways to speak", "There are two main kinds of Armenian: <b>Eastern</b> (spoken in Armenia) and <b>Western</b>. "
                              "This book uses Eastern Armenian."),
    ],
    hello_pics=[("pomegranate", {}), ("hy_apricot", {}), ("mountain", {})],
    map=region_map(frame=[[37.5, 36.5], [51.5, 46.0]],
                   points=dict(yerevan=[44.51, 40.18], gyumri=[43.85, 40.79]),
                   area=None,
                   cities=[("yerevan", "Yerevan", 14, 8, "start", False), ("gyumri", "Gyumri", -14, 8, "end", False)],
                   label="ARMENIA", label_at=[44.8, 41.25], marker=[44.5, 40.5],
                   caption="The circle shows Armenia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Armenian is spoken in Yerevan "
                          "and Gyumri, high in the mountains between the <b>Black Sea</b> and the <b>Caspian Sea</b>.",
                   seas=[("Black Sea", 39.3, 42.4), ("Caspian Sea", 50.0, 42.6)], world_r=13),
    digits=[("0", "զրո", "zro", "zero"), ("1", "մեկ", "mek", "one"), ("2", "երկու", "yer-KOO", "two"),
            ("3", "երեք", "ye-REK", "three"), ("4", "չորս", "chors", "four"), ("5", "հինգ", "heeng", "five"),
            ("6", "վեց", "vets", "six"), ("7", "յոթ", "yot", "seven"), ("8", "ութ", "oot", "eight"),
            ("9", "ինը", "EE-nuh", "nine")],
    phrases=[("Ասսալամու ալեյքում", "as-sa-LA-moo a-LEY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Վա ալեյքում ասսալամ", "wa a-LEY-koom as-sa-LAM", "And upon you be peace (the reply)"),
             ("Բարև", "ba-REV", "Hello!"),
             ("Իմ անունը … է", "eem a-NOO-nuh … e", "My name is …"),
             ("Շնորհակալություն · Ջազաքալլահու խայրան", "shnor-ha-ka-loo-TYOON · ja-za-KAL-la-hoo KHAY-ran",
              "Thank you · May Allah reward you with good"),
             ("մայրիկ · հայրիկ", "mai-REEK · hai-REEK", "Mother · Father"),
             ("եղբայր · քույր", "yegh-BAIR · kooyr", "Brother · Sister"),
             ("այո · ոչ", "a-YO · voch", "Yes · No"),
             ("Ես հայերեն եմ սովորում։", "yes ha-ye-REN em so-vo-ROOM", "I am learning Armenian!")],
    cheer=("Մաշալլահ, ապրե՛ս", "ma-shal-LAH, ap-RES!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="Ա Բ Գ", right="Դ Ե Զ"),
    review_note=("Check: the 39-letter order used in Armenian schools (Ու after Ց, և after Ք) and how և / Ու are shown as big "
                 "letters; Eastern Armenian letter names (յի, ըթ, լյուն, տյուն, փյուր); the Armenian spellings of the Islamic phrases "
                 "(Ասսալամու ալեյքում, Վա ալեյքում ասսալամ, Ջազաքալլահու խայրան, Մաշալլահ); the name plate 'Այս գիրքը պատկանում է' "
                 "(a name after it needs a dative ending); word choices ֆինիկ (dates; or արմավ?), ճրագ (oil lamp), "
                 "ուլունք (beads), քար (stone/stones), յոթ (seven, shown as the number 7), աղ for Ղ; the speaker number."),
    tiles="ԱԲԳԴԵԶ", cover_pics=["pomegranate", "hy_apricot", "kite", "mountain"], title_size=46,
    speakers_blurb="Armenian is spoken by more than 5 million people in Armenia and around the world.",
    sample_words=[("ծիրան", "tsee-RAN", "apricot"), ("նուռ", "noorr", "pomegranate"), ("արև", "a-REV", "sun")],
    keywords=["armenian alphabet book for kids", "learn armenian for children", "armenian letters coloring book",
              "armenian alphabet tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual armenian english toddlers"],
))
