# -*- coding: utf-8 -*-
"""Book 36 - Georgian (Mkhedruli script, 33 letters, no capital letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = the single Mkhedruli letter. Transliteration marks the 'popping' (ejective) consonants with an apostrophe."""
from generic import build, letter, section
from maps import region_map

PH = "Georgian letter name"
F = "noto-sans-georgian-georgian"

POP = " — a <b>popping</b> sound: hold your breath and let it go with a little click"


def Lt(ch, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:22pt">{ch} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:3px">{rule}</div>' if rule else ""))
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    Lt("ა", "ანი", "a-ni", "‘a’ as in “father”", "ატამი", "a-t'a-mi", "peach", "ka_peach"),
    Lt("ბ", "ბანი", "ba-ni", "‘b’ as in “ball”", "ბურთი", "bur-ti", "ball", "ball"),
    Lt("გ", "განი", "ga-ni", "‘g’ as in “go”", "გემი", "ge-mi", "ship", "ship"),
    Lt("დ", "დონი", "do-ni", "‘d’ as in “door”", "დედამიწა", "de-da-mi-ts'a", "the Earth", "globe",
       note="<span class='nt'>დედამიწა</span> means “mother earth”: <span class='nt'>დედა</span> (mother) + <span class='nt'>მიწა</span> (earth)."),
    Lt("ე", "ენი", "e-ni", "‘e’ as in “bed”", "ენძელა", "en-dze-la", "snowdrop (a spring flower)", "ka_snowdrop"),
    Lt("ვ", "ვინი", "vi-ni", "‘v’ as in “van”", "ვაშლი", "vash-li", "apple", "apple"),
    Lt("ზ", "ზენი", "ze-ni", "‘z’ as in “zoo”", "ზეთისხილი", "ze-tis-khi-li", "olive", "olive"),
    Lt("თ", "თანი", "ta-ni", "‘t’ with a little puff of air, as in “top”", "თაფლი", "tap-li", "honey", "honey"),
    Lt("ი", "ინი", "i-ni", "‘i’ as in “machine” (like ‘ee’)", "ია", "i-a", "violet (a flower)", "flower"),
    Lt("კ", "კანი", "k'a-ni", "‘k’" + POP, "კარი", "k'a-ri", "door", "door"),
    Lt("ლ", "ლასი", "la-si", "‘l’ as in “lemon”", "ლიმონი", "li-mo-ni", "lemon", "lemon"),
    Lt("მ", "მანი", "ma-ni", "‘m’ as in “moon”", "მზე", "mze", "sun", "sun"),
    Lt("ნ", "ნარი", "na-ri", "‘n’ as in “net”", "ნავი", "na-vi", "boat", "boat"),
    Lt("ო", "ონი", "o-ni", "‘o’ as in “dog”", "ორი", "o-ri", "two", "ka_two"),
    Lt("პ", "პარი", "p'a-ri", "‘p’" + POP, "პური", "p'u-ri", "bread", "ka_bread"),
    Lt("ჟ", "ჟანი", "zha-ni", "‘zh’, like the ‘s’ in “treasure”", "ჟოლო", "zho-lo", "raspberry", "ka_raspberry"),
    Lt("რ", "რაე", "ra-e", "a quick, rolled ‘r’", "რძე", "rdze", "milk", "ka_milk"),
    Lt("ს", "სანი", "sa-ni", "‘s’ as in “sun”", "სახლი", "sakh-li", "house", "house"),
    Lt("ტ", "ტარი", "t'a-ri", "‘t’" + POP, "ტალღა", "t'al-gha", "wave", "waves"),
    Lt("უ", "უნი", "u-ni", "‘u’ as in “put” (like ‘oo’)", "ურემი", "u-re-mi", "cart", "cart"),
    Lt("ფ", "ფარი", "pa-ri", "‘p’ with a little puff of air, as in “pen”", "ფანჯარა", "pan-ja-ra", "window", "window"),
    Lt("ქ", "ქანი", "ka-ni", "‘k’ with a little puff of air, as in “kite”", "ქოლგა", "kol-ga", "umbrella", "umbrella"),
    Lt("ღ", "ღანი", "gha-ni", "a soft, throaty ‘gh’, like a gargle (similar to the French ‘r’)", "ღრუბელი", "ghru-be-li",
       "cloud", "clouds"),
    Lt("ყ", "ყარი", "q'a-ri", "a deep ‘k’ from far back in the throat" + POP, "ყურძენი", "q'ur-dze-ni", "grapes", "grapes",
       note="Georgia is one of the oldest grape-growing lands in the world."),
    Lt("შ", "შინი", "shi-ni", "‘sh’ as in “ship”", "შროშანი", "shro-sha-ni", "lily", "lily"),
    Lt("ჩ", "ჩინი", "chi-ni", "‘ch’ with a little puff of air, as in “cheese”", "ჩაი", "cha-i", "tea", "teacup"),
    Lt("ც", "ცანი", "tsa-ni", "‘ts’ as in “cats”, with a little puff of air", "ცისარტყელა", "tsi-sar-t'q'e-la", "rainbow", "rainbow"),
    Lt("ძ", "ძილი", "dzi-li", "‘dz’ as in “kids”", "ძაფი", "dza-pi", "thread, yarn", "wool"),
    Lt("წ", "წილი", "ts'i-li", "‘ts’" + POP, "წიგნი", "ts'ig-ni", "book", "book",
       args=dict(left="ა ბ გ", right="დ ე ვ")),
    Lt("ჭ", "ჭარი", "ch'a-ri", "‘ch’" + POP, "ჭიქა", "ch'i-ka", "drinking glass", "water"),
    Lt("ხ", "ხანი", "kha-ni", "a scratchy ‘kh’ from the back of the throat, like ‘ch’ in Scottish “loch”", "ხე", "khe",
       "tree", "tree"),
    Lt("ჯ", "ჯანი", "ja-ni", "‘j’ as in “jam”", "ჯამი", "ja-mi", "bowl", "rice"),
    Lt("ჰ", "ჰაე", "ha-e", "‘h’ as in “hat”", "ჰაერი", "ha-e-ri", "air", "kite",
       note="<span class='nt'>ჰ</span> is the last letter. A kite flies on the <span class='nt'>ჰაერი</span> — the air!"),
]

LANG = build(dict(
    code="ka", folder="book-36-georgian", series_no=36, isbn="", draft=True,
    name="Georgian", native="ქართული", native_tr="kar-tu-li", name_word="სახელი", write_word="დაწერე",
    title_native="ჩემი პირველი ანბანი", title_letters="აბგდევ", belongs_native="ეს წიგნი ეკუთვნის",
    belongs_pic="grapes", alphabet_native="ანბანი", numbers_native="რიცხვები", numbers_tr="rits-khve-bi",
    phrases_native="პირველი სიტყვები",
    fonts=[("Noto Sans Georgian", w, "normal", f"{F}-{w}-normal.woff2", "U+10A0-10FF,U+1C90-1CBF,U+2D00-2D2F")
           for w in (400, 700, 800)],
    disp_family="Noto Sans Georgian", text_family="Noto Sans Georgian",
    glyph_font=[f"{F}-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Georgian",
    extra_css=".nt,.ntd,.lp-name{font-family:'Noto Sans Georgian','Nunito',sans-serif}",
    phon_feature="each letter’s Georgian name (ა «ანი», ბ «ბანი», გ «განი»…)",
    sections=[section(LETTERS, native="ანბანი", native_tr="an-ba-ni — “the alphabet”",
                      chart_cols=7, warmup_cols=7,
                      intro_html="""<p>The Georgian alphabet is called <span class="nt">ანბანი</span> (<i>an-ba-ni</i>), from the names of its
first two letters, <span class="nt">ანი</span> and <span class="nt">ბანი</span>. It has <b>33 letters</b>, and every letter always
says the same sound — so once you know them, you can read any Georgian word!</p>
<div class="box" style="margin:0.1in 0"><h3>No capital letters</h3>Georgian has <b>no capital letters</b>. Names, sentences and
book titles all start with the same letters. That means one shape to learn for each letter!</div>
<div class="box" style="margin:0.1in 0"><h3>Puff, no puff… and pop!</h3>Some letters come in pairs:
<span class="nt">თ ტ</span>, <span class="nt">ფ პ</span>, <span class="nt">ქ კ</span>, <span class="nt">ც წ</span>, <span class="nt">ჩ ჭ</span>.
The first of each pair is said with a little <b>puff of air</b>; the second is a <b>popping</b> sound, made by holding your breath
and letting it go with a click. In this book the popping letters have an apostrophe: <i>k', p', t', ts', ch', q'</i>.</div>
<div class="box"><h3>Round and curly</h3>Georgian letters are round and curly, and some have tall tops or long tails.
Trace them slowly and enjoy the curves!</div>""")],
    sound_notes=[
        "Georgian has only a light stress, so say every syllable clearly and evenly: <i>li-mo-ni</i>.",
        "An <b>apostrophe</b> marks a <b>popping</b> sound: <i>k'</i>, <i>p'</i>, <i>t'</i>, <i>ts'</i>, <i>ch'</i>, and <i>q'</i> "
        "(a deep ‘k’ from far back in the throat). Hold your breath and let the sound pop out.",
        "<b>kh</b> is a scratchy sound from the back of the throat (‘ch’ in Scottish “loch”); <b>gh</b> is its soft, gargled partner.",
        "Georgian likes many consonants in a row: <i>mze</i> (sun), <i>rdze</i> (milk). Say each one, quickly, without adding vowels.",
        "<b>i</b> as in “machine”, <b>u</b> as in “put”, <b>e</b> as in “bed”, <b>o</b> as in “dog”, <b>a</b> as in “father”."],
    phon_explain="The box marked <i>Georgian letter name</i> shows the letter’s name written in Georgian (ა is «ანი», ბ is «ბანი»…).",
    standard="standard Georgian as spoken in Tbilisi",
    hello=[
        ("Who speaks it?", "About <b>4 million people</b> speak Georgian.<sup>³</sup>"),
        ("Where?", "In <b>Georgia</b>, a land of high mountains, green valleys and vineyards on the shore of the <b>Black Sea</b>, "
                   "and in Georgian families around the world."),
        ("How is it written?", "In its very own <b>Georgian alphabet</b>, called <i>Mkhedruli</i>, from <b>left to right</b>, "
                               "with <b>no capital letters</b>."),
        ("How many letters?", "<b>33 letters</b>, from <span class='nt'>ა</span> (<i>ani</i>) to <span class='nt'>ჰ</span> (<i>hae</i>)."),
        ("Did you know?", "Georgian has <b>three</b> beautiful old ways of writing its alphabet. In 2016, UNESCO listed them as a "
                          "living treasure of the world’s culture."),
        ("Mum or Dad?", "In Georgian, <span class='nt'>დედა</span> (<i>de-da</i>) means <b>mother</b> and "
                        "<span class='nt'>მამა</span> (<i>ma-ma</i>) means <b>father</b>!"),
    ],
    hello_pics=[("grapes", {}), ("mountain", {}), ("ka_peach", {})],
    map=region_map(frame=[[37.0, 37.5], [51.0, 46.5]],
                   points=dict(tbilisi=[44.79, 41.72], kutaisi=[42.70, 42.27], batumi=[41.64, 41.64]),
                   area=None,
                   cities=[("tbilisi", "Tbilisi", 14, 8, "start", False), ("kutaisi", "Kutaisi", 0, -16, "middle", False),
                           ("batumi", "Batumi", -14, 8, "end", False)],
                   label="GEORGIA", label_at=[43.3, 41.45], marker=[43.5, 42.0],
                   caption="The circle shows Georgia on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Georgian is spoken in Tbilisi, "
                          "Kutaisi and Batumi, between the <b>Black Sea</b> and the <b>Caspian Sea</b>, south of the high Caucasus "
                          "mountains.",
                   seas=[("Black Sea", 38.6, 42.7), ("Caspian Sea", 50.0, 42.6)], world_r=13),
    digits=[("0", "ნული", "nu-li", "zero"), ("1", "ერთი", "er-ti", "one"), ("2", "ორი", "o-ri", "two"),
            ("3", "სამი", "sa-mi", "three"), ("4", "ოთხი", "ot-khi", "four"), ("5", "ხუთი", "khu-ti", "five"),
            ("6", "ექვსი", "ek-vsi", "six"), ("7", "შვიდი", "shvi-di", "seven"), ("8", "რვა", "rva", "eight"),
            ("9", "ცხრა", "tskhra", "nine")],
    phrases=[("ასალამუ ალეიქუმ", "a-sa-la-mu a-lei-kum", "Peace be upon you (the Muslim greeting)"),
             ("ვა ალეიქუმ ასალამ", "va a-lei-kum a-sa-lam", "And upon you be peace (the reply)"),
             ("გამარჯობა!", "ga-mar-jo-ba", "Hello!"),
             ("მე მქვია …", "me mkvi-a …", "My name is …"),
             ("მადლობა · ჯაზაკალაჰუ ხაირან", "mad-lo-ba · ja-za-ka-la-hu khai-ran",
              "Thank you · May Allah reward you with good"),
             ("დედა · მამა", "de-da · ma-ma", "Mother · Father"),
             ("ძმა · და", "dzma · da", "Brother · Sister"),
             ("კი · არა", "k'i · a-ra", "Yes · No"),
             ("ქართულს ვსწავლობ!", "kar-tuls vs-ts'av-lob", "I am learning Georgian!")],
    cheer=("მაშალაჰ! ყოჩაღ!", "ma-sha-lah! q'o-chagh!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded; the three Georgian scripts were inscribed "
                 "on UNESCO’s Representative List of the Intangible Cultural Heritage of Humanity in 2016.",
    book_pic=dict(left="ა ბ გ", right="დ ე ვ"),
    review_note=("Check: Georgian spellings of the Islamic phrases (ასალამუ ალეიქუმ, ვა ალეიქუმ ასალამ, ჯაზაკალაჰუ ხაირან, "
                 "მაშალაჰ); the name plate 'ეს წიგნი ეკუთვნის' (a name after it needs the dative -ს); 'ქართულს ვსწავლობ' "
                 "and 'მე მქვია'; word choices ენძელა (snowdrop), ურემი (cart), ძაფი (thread, shown as a ball of yarn), "
                 "ჭიქა (glass, shown with water), ჯამი (bowl, shown with rice), ჰაერი (air, shown as a kite), ორი (two, shown as "
                 "two stars); the apostrophe convention for ejectives and the speaker number."),
    tiles="აბგდეო", cover_pics=["grapes", "ka_peach", "kite", "mountain"], title_size=48,
    speakers_blurb="Georgian is spoken by about 4 million people in Georgia and around the world.",
    sample_words=[("მზე", "mze", "sun"), ("ყურძენი", "q'ur-dze-ni", "grapes"), ("ატამი", "a-t'a-mi", "peach")],
    keywords=["georgian alphabet book for kids", "learn georgian for children", "georgian letters coloring book",
              "georgian alphabet tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual georgian english toddlers"],
))
