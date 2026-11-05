# -*- coding: utf-8 -*-
"""Book 20 - Santali (Ol Chiki script, 30 letters). Allamahul Bayan Series. REVIEW DRAFT.
Ol Chiki is taught in six rows of five; each row starts with a vowel. Built with engine/generic.py."""
from generic import build, letter, section, fontset
from maps import south_asia_map

ROWS = ["ᱚᱛᱜᱝᱞ", "ᱟᱠᱡᱢᱣ", "ᱤᱥᱦᱧᱨ", "ᱩᱪᱫᱬᱭ", "ᱮᱯᱰᱱᱲ", "ᱳᱴᱵᱶᱷ"]
PH = "Ol Chiki name · its row"
END = "<b>{}</b> rarely starts a word. Find it at the end of <span class='nt'>{}</span>!"
MID = "<b>{}</b> never starts a word. Find it in the middle of <span class='nt'>{}</span>!"
CAUGHT = ("At the end of a word <span class='nt'>{0}</span> is a “caught” sound: the mouth closes but no air comes out "
          "(<span class='nt'>{1}</span> {2}).")


def S(ch, name, rom, name_en, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    r = next(i for i, row in enumerate(ROWS) if ch in row)
    row = " ".join(ROWS[r])
    phon = (f'<div class="nt" style="font-size:22pt;line-height:1.3">{ch} — {name}</div>'
            f'<div class="small">Its name is «{rom}». Row {r + 1}: <span class="nt" style="font-size:13pt">{row}</span></div>'
            + (f'<div class="small" style="margin-top:3px">{rule}</div>' if rule else ""))
    return letter(ch, name, name_en, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    # row 1
    S("ᱚ", "ᱞᱚ", "la", "law", "‘aw’ as in “law” (short)", "ᱚᱞ", "awl", "writing", "pen",
      rule="The word <span class='nt'>ᱚᱞ</span> gives the script its name: <span class='nt'>ᱚᱞ ᱪᱤᱠᱤ</span> «Ol Chiki»."),
    S("ᱛ", "ᱚᱛ", "at", "awt", "‘t’ as in “top”, with the tongue on the teeth", "ᱛᱩᱠᱩᱡ", "TOO-kooch", "clay pot", "pot",
      rule=CAUGHT.format("ᱛ", "ᱢᱤᱫ", "mit’ “one”")),
    S("ᱜ", "ᱚᱜ", "ag", "awg", "‘g’ as in “go”", "ᱜᱟᱰᱟ", "GAH-dah", "river", "waves",
      rule=CAUGHT.format("ᱜ", "ᱫᱟᱜ", "dahk’ “water”")),
    S("ᱝ", "ᱚᱝ", "ang", "awng", "‘ng’ as in “sing”", "ᱵᱩᱞᱩᱝ", "BOO-loong", "salt", "salt", dict(label="ᱵᱩᱞᱩᱝ"),
      note=END.format("ᱝ", "ᱵᱩᱞᱩᱝ")),
    S("ᱞ", "ᱚᱞ", "al", "awl", "‘l’ as in “lamp”", "ᱞᱤᱢᱵᱩ", "LEEM-boo", "lemon", "lemon"),
    # row 2
    S("ᱟ", "ᱞᱟ", "laa", "lah", "‘ah’ as in “father”", "ᱟᱜ", "ahk", "bow (and arrow)", "bowarrow"),
    S("ᱠ", "ᱟᱠ", "aak", "ahk", "‘k’ as in “kite”", "ᱠᱟᱭᱨᱟ", "KAI-rah", "banana", "banana"),
    S("ᱡ", "ᱟᱡ", "aaj", "ahj", "‘j’ as in “jam”", "ᱡᱚᱡᱚ", "JAW-jaw", "tamarind", "tamarind",
      rule=CAUGHT.format("ᱡ", "ᱛᱩᱠᱩᱡ", "tookooch’ “pot”")),
    S("ᱢ", "ᱟᱢ", "aam", "ahm", "‘m’ as in “moon”", "ᱢᱟᱫ", "maht", "bamboo", "sat_bamboo"),
    S("ᱣ", "ᱟᱣ", "aaw", "ahw", "‘w’ as in “water”", "ᱪᱟᱣᱞᱮ", "CHAHW-leh", "rice (the grain)", "rice",
      note="Find <b>ᱣ</b> in the middle of <span class='nt'>ᱪᱟᱣᱞᱮ</span>!"),
    # row 3
    S("ᱤ", "ᱞᱤ", "li", "lee", "‘ee’ as in “see”", "ᱤᱯᱤᱞ", "EE-peel", "star", "star"),
    S("ᱥ", "ᱤᱥ", "is", "ees", "‘s’ as in “sun”", "ᱥᱟᱠᱟᱢ", "SAH-kahm", "leaf", "sat_leaf"),
    S("ᱦ", "ᱤᱦ", "ih", "eeh", "‘h’ as in “hat”", "ᱦᱚᱲᱚ", "HAW-raw", "paddy (rice plant)", "paddy"),
    S("ᱧ", "ᱤᱧ", "iny", "eeny", "‘ny’ as in “canyon”", "ᱧᱤᱫᱟ ᱪᱟᱸᱫᱚ", "NYEE-dah CHAHN-daw", "moon (“night sun”)", "moon"),
    S("ᱨ", "ᱤᱨ", "ir", "eer", "a tapped ‘r’", "ᱨᱤᱢᱤᱞ", "REE-meel", "cloud", "clouds"),
    # row 4
    S("ᱩ", "ᱞᱩ", "lu", "loo", "‘oo’ as in “moon”", "ᱩᱞ", "ool", "mango", "mango"),
    S("ᱪ", "ᱩᱪ", "uch", "ooch", "‘ch’ as in “chair”", "ᱪᱟᱸᱫᱚ", "CHAHN-daw", "sun", "sun",
      rule="The little mark <span class='nt'>ᱸ</span> makes the vowel before it hum through the nose: <span class='nt'>ᱪᱟᱸ</span> «chahn»."),
    S("ᱫ", "ᱩᱫ", "ud", "ood", "‘d’ as in “day”, with the tongue on the teeth", "ᱫᱟᱜ", "dahk", "water", "water",
      rule=CAUGHT.format("ᱫ", "ᱢᱟᱫ", "maht’ “bamboo”")),
    S("ᱬ", "ᱩᱬ", "unn", "oon", "an ‘n’ with the tongue curled back", "ᱠᱟᱬᱴᱷᱟᱲ", "KAHN-thahr", "jackfruit", "sat_jackfruit",
      note=MID.format("ᱬ", "ᱠᱟᱬᱴᱷᱟᱲ") + " You also hear it in <span class='nt'>ᱢᱚᱬᱮ</span> «mawneh», “five”."),
    S("ᱭ", "ᱩᱭ", "uy", "ooy", "‘y’ as in “yes”", "ᱦᱚᱭ", "HAW-eh", "wind (good for flying a kite!)", "kite",
      note=END.format("ᱭ", "ᱦᱚᱭ")),
    # row 5
    S("ᱮ", "ᱞᱮ", "le", "leh", "‘e’ as in “bed”", "ᱫᱟᱨᱮ", "DAH-reh", "tree", "tree",
      note="Find <b>ᱮ</b> at the end of <span class='nt'>ᱫᱟᱨᱮ</span>!"),
    S("ᱯ", "ᱮᱯ", "ep", "ehp", "‘p’ as in “pen”", "ᱯᱩᱠᱷᱨᱤ", "POOKH-ree", "pond", "lily"),
    S("ᱰ", "ᱮᱰ", "edd", "ehd", "a ‘d’ with the tongue curled back", "ᱰᱟᱦᱟᱨ", "DAH-hahr", "path, road", "sat_path"),
    S("ᱱ", "ᱮᱱ", "en", "ehn", "‘n’ as in “net”", "ᱥᱩᱱᱩᱢ", "SOO-noom", "oil", "jar",
      note="Find <b>ᱱ</b> in the middle of <span class='nt'>ᱥᱩᱱᱩᱢ</span>!"),
    S("ᱲ", "ᱮᱲ", "err", "ehr", "a flapped ‘r’ with the tongue curled back", "ᱚᱲᱟᱜ", "AW-rahk", "house", "house",
      note=MID.format("ᱲ", "ᱚᱲᱟᱜ")),
    # row 6
    S("ᱳ", "ᱞᱳ", "lo", "loh", "‘o’ as in “go” (short and pure)", "ᱳᱛᱮ", "OH-teh", "land, the earth", "globe"),
    S("ᱴ", "ᱳᱴ", "ott", "oht", "a ‘t’ with the tongue curled back", "ᱞᱚᱴᱟ", "LAW-tah", "water jug (lota)", "ewer",
      note="Find <b>ᱴ</b> in the middle of <span class='nt'>ᱞᱚᱴᱟ</span>!"),
    S("ᱵ", "ᱳᱵ", "ob", "ohb", "‘b’ as in “ball”", "ᱵᱟᱦᱟ", "BAH-hah", "flower", "flower",
      rule=CAUGHT.format("ᱵ", "ᱥᱟᱵ", "sahp’ “catch”")),
    S("ᱶ", "ᱳᱶ", "ov", "ohw", "a ‘w’ hummed through the nose", "ᱥᱟᱶᱦᱮᱫ", "SAHW-hehd", "stories and books (literature)", "book",
      dict(left="ᱚ ᱛ ᱜ", right="ᱟ ᱠ ᱡ"),
      note=MID.format("ᱶ", "ᱥᱟᱶᱦᱮᱫ") + " It is also in <span class='nt'>ᱱᱚᱶᱟ</span> «nawah», “this”."),
    S("ᱷ", "ᱳᱷ", "oh", "ohh", "a puff of breath after the letter before it", "ᱫᱷᱤᱨᱤ", "DHEE-ree", "stone", "sat_stones",
      note="<b>ᱷ</b> never starts a word. It adds a puff of air: <span class='nt'>ᱫ + ᱷ = ᱫᱷ</span> «dh», as in <span class='nt'>ᱫᱷᱤᱨᱤ</span>."),
]

INTRO = """<p>Santali is written in <b>Ol Chiki</b> <span class="nt">ᱚᱞ ᱪᱤᱠᱤ</span>, an alphabet made just for Santali by
<b>Pandit Raghunath Murmu</b> in 1925. It has <b>30 letters</b>, and it is written from left to right.</p>
<div class="box" style="margin:0.1in 0"><h3>Six rows of five</h3>Children learn Ol Chiki in <b>six rows</b>. Each row begins with a vowel:
<div class="nt" style="font-size:17pt;line-height:1.6;margin-top:4px">""" + "<br>".join(" ".join(r) for r in ROWS) + """</div></div>
<div class="box" style="margin:0.1in 0"><h3>Letters that say their names</h3>Every letter has a short name, and the name holds the letter’s
sound: <span class="nt">ᱠ</span> is «aak», <span class="nt">ᱢ</span> is «aam». The six vowels <span class="nt">ᱚ ᱟ ᱤ ᱩ ᱮ ᱳ</span> are called
«la, laa, li, lu, le, lo».</div>
<div class="box"><h3>Full letters, no vowel signs</h3>In Ol Chiki every vowel is written as a full letter, one after another:
<span class="nt">ᱫ + ᱟ + ᱜ = ᱫᱟᱜ</span> «dahk», “water”.</div>"""

LANG = build(dict(
    code="sat", folder="book-20-santali", series_no=20, isbn="", draft=True,
    name="Santali", native="ᱥᱟᱱᱛᱟᱲᱤ", native_tr="SAHN-tah-ree", name_word="ᱧᱩᱛᱩᱢ", write_word="ᱚᱞ ᱢᱮ",
    title_native="ᱤᱧᱟᱜ ᱯᱩᱭᱞᱩ ᱚᱞ ᱪᱤᱠᱤ ᱯᱩᱛᱷᱤ", title_letters="ᱚᱛᱜᱝᱞ", belongs_native="ᱱᱚᱶᱟ ᱯᱩᱛᱷᱤ ᱫᱚ … ᱨᱮᱭᱟᱜ",
    belongs_pic="flower", alphabet_native="ᱚᱞ ᱪᱤᱠᱤ", numbers_native="ᱮᱞ ᱠᱚ", numbers_tr="EHL kaw",
    phrases_native="ᱯᱩᱭᱞᱩ ᱨᱚᱲ",
    fonts=fontset("Noto Sans Ol Chiki", "noto-sans-ol-chiki-ol-chiki", "Noto Sans Ol Chiki", "noto-sans-ol-chiki-ol-chiki"),
    disp_family="Noto Sans Ol Chiki", text_family="Noto Sans Ol Chiki",
    glyph_font="noto-sans-ol-chiki-ol-chiki-700-normal.woff2",
    font_credit="Noto Sans Ol Chiki",
    extra_css=".nt{font-family:'Noto Sans Ol Chiki','Nunito',sans-serif} .ntd{font-family:'Noto Sans Ol Chiki','Nunito',sans-serif;font-weight:700}",
    phon_feature="each letter’s Ol Chiki name («la», «at», «ag»…) and its row in the alphabet",
    sections=[section(LETTERS, native="ᱚᱞ ᱪᱤᱠᱤ", native_tr="awl CHEE-kee — “the writing letters”",
                      chart_title="letters in six rows", chart_cols=5, warmup_cols=6, intro_html=INTRO)],
    sound_notes=[
        "<b>aw</b> is the Ol Chiki vowel <span class='nt'>ᱚ</span>, like “aw” in “law” but short. <b>ah</b> is <span class='nt'>ᱟ</span>, as in “father”.",
        "<b>CAPITALS</b> show the part of the word to say a little louder: <i>BAH-hah</i>.",
        "Some sounds are made with the <b>tongue curled back</b> (<span class='nt'>ᱴ ᱰ ᱬ ᱲ</span>). The guide writes them as plain t, d, n, r; the letter page tells you to curl your tongue.",
        "At the end of a word <span class='nt'>ᱜ ᱡ ᱫ ᱵ</span> are <b>“caught” sounds</b> (k’, ch’, t’, p’): close your mouth for the sound, but let no air out.",
        "<b>kh, th, dh</b> mean the letter plus a puff of air (the letter <span class='nt'>ᱷ</span>), not the English “th”."],
    phon_explain="The box marked <i>Ol Chiki name · its row</i> shows the name Santali children use for the letter "
                 "(<span class='nt'>ᱠ</span> is «aak», <span class='nt'>ᱢ</span> is «aam»…) and the row of five it belongs to.",
    standard="Santali as written in Ol Chiki in Jharkhand and West Bengal",
    hello=[
        ("Who speaks it?", "About <b>7½ million people</b> speak Santali.<sup>³</sup> It is one of the 22 languages listed in India’s Constitution."),
        ("Where?", "In eastern <b>India</b> (Jharkhand, West Bengal, Odisha, Bihar and Assam), and also in <b>Bangladesh</b> and <b>Nepal</b>."),
        ("How is it written?", "In its own alphabet, <b>Ol Chiki</b> <span class='nt'>ᱚᱞ ᱪᱤᱠᱤ</span>, from <b>left to right</b>. Some people also write Santali in Bengali, Odia or Latin letters."),
        ("How many letters?", "<b>30 letters</b> in six rows of five, plus its own <b>numbers</b> <span class='nt'>᱐ ᱑ ᱒ ᱓</span>…"),
        ("Hello!", "Santali speakers greet each other with <span class='nt'>ᱡᱚᱦᱟᱨ</span> <i>JAW-hahr</i>."),
        ("Did you know?", "Santali belongs to the <b>Munda</b> family of languages, a different family from Hindi or Bengali. "
                          "Many Santali words are short and sweet: <span class='nt'>ᱩᱞ</span> <i>ool</i> is a mango and <span class='nt'>ᱫᱟᱜ</span> <i>dahk</i> is water."),
    ],
    hello_pics=[("flower", {}), ("sat_leaf", {}), ("mango", {})],
    map=south_asia_map(
        points=dict(jamshedpur=[86.20, 22.80], dumka=[87.25, 24.27], ranchi=[85.33, 23.35], baripada=[86.72, 21.94],
                    area=[86.5, 23.2], label=[86.0, 27.4]),
        area=(100, 85, 0), label="SANTALI",
        cities=[("ranchi", "Ranchi", -14, 8, "end", False), ("jamshedpur", "Jamshedpur", 14, 22, "start", False),
                ("dumka", "Dumka", 14, -6, "start", False), ("baripada", "Baripada", -14, 20, "end", False)],
        marker=[86.5, 23.2], caption="The circle shows the Santali-speaking area on the world map.",
        legend="<b>Color it:</b> the area inside the dashed line <b>yellow</b> · the rest of the land <b>green</b> · the seas <b>blue</b>. "
               "<b>Find it:</b> Santali is spoken around Ranchi, Jamshedpur and Dumka in Jharkhand, in West Bengal, and around Baripada in Odisha."),
    digits=[("᱐", "ᱥᱩᱱ", "soon", "zero"), ("᱑", "ᱢᱤᱫ", "mit’", "one"), ("᱒", "ᱵᱟᱨ", "bahr", "two"), ("᱓", "ᱯᱮ", "peh", "three"),
            ("᱔", "ᱯᱩᱱ", "poon", "four"), ("᱕", "ᱢᱚᱬᱮ", "MAWN-eh", "five"), ("᱖", "ᱛᱩᱨᱩᱭ", "TOO-rooy", "six"),
            ("᱗", "ᱮᱭᱟᱭ", "EH-yahy", "seven"), ("᱘", "ᱤᱨᱟᱹᱞ", "EE-rul", "eight"), ("᱙", "ᱟᱨᱮ", "AH-reh", "nine")],
    phrases=[("ᱟᱥᱥᱟᱞᱟᱢᱩ ᱟᱞᱟᱭᱠᱩᱢ", "as-sah-LAH-moo ah-LAI-koom", "Peace be upon you (the Muslim greeting)"),
             ("ᱣᱟ ᱟᱞᱟᱭᱠᱩᱢ ᱟᱥᱥᱟᱞᱟᱢ", "wa ah-LAI-koom as-sah-LAHM", "And upon you be peace (the reply)"),
             ("ᱡᱚᱦᱟᱨ!", "JAW-hahr", "Hello! (the Santali greeting)"),
             ("ᱤᱧᱟᱜ ᱧᱩᱛᱩᱢ …", "EE-nyahk NYOO-toom …", "My name is …"),
             ("ᱥᱟᱨᱦᱟᱣ", "SAHR-hahw", "Thank you"),
             ("ᱡᱟᱡᱟᱠᱟᱞᱞᱟᱦᱩ ᱠᱷᱟᱭᱨᱟᱱ", "jah-zah-kahl-LAH-hoo KHAI-rahn", "May Allah reward you with good"),
             ("ᱟᱭᱳ · ᱵᱟᱵᱟ", "AH-yoh · BAH-bah", "Mother · Father"),
             ("ᱫᱟᱫᱟ · ᱫᱟᱭ", "DAH-dah · dai", "Big brother · Big sister"),
             ("ᱦᱮᱸ · ᱵᱟᱝ", "hen · bahng", "Yes · No"),
             ("ᱤᱧ ᱥᱟᱱᱛᱟᱲᱤ ᱯᱟᱹᱨᱥᱤ ᱪᱮᱫ ᱮᱫᱟᱧ!", "eeny SAHN-tah-ree PAR-see chehd EH-dahny", "I am learning Santali!")],
    cheer=("ᱢᱟᱥᱟᱞᱞᱟᱦ! ᱵᱮᱥ ᱜᱮ!", "MAH-shah-lah! behs geh!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International) and the Census of India.",
    book_pic=dict(left="ᱚ ᱛ ᱜ", right="ᱟ ᱠ ᱡ"),
    review_note=("Drafted without a native speaker. Check: every Ol Chiki spelling (especially final ᱜ/ᱡ/ᱫ/ᱵ for k’/c’/t’/p’, "
                 "ᱚ vs ᱳ, and ᱟ vs ᱟᱹ); the words ᱛᱩᱠᱩᱡ, ᱠᱟᱭᱨᱟ, ᱞᱤᱢᱵᱩ, ᱧᱤᱫᱟ ᱪᱟᱸᱫᱚ, ᱠᱟᱬᱴᱷᱟᱲ, ᱦᱚᱭ, ᱳᱛᱮ, ᱞᱚᱴᱟ, "
                 "ᱥᱟᱶᱦᱮᱫ, ᱰᱟᱦᱟᱨ; the numbers (esp. zero ᱥᱩᱱ); all phrases, the title and ‘belongs to’ lines; "
                 "and the English transliteration of the letter names (la, at, ag…)."),
    tiles="ᱚᱛᱜᱟᱠᱡ", cover_pics=["flower", "mango", "sat_leaf", "star"], title_size=48,
    speakers_blurb="Santali is spoken by about 7½ million people in eastern India, Bangladesh and Nepal, and it has its own alphabet, Ol Chiki.",
    sample_words=[("ᱵᱟᱦᱟ", "BAH-hah", "flower"), ("ᱩᱞ", "ool", "mango"), ("ᱤᱯᱤᱞ", "EE-peel", "star")],
    keywords=["santali alphabet book for kids", "ol chiki letters coloring book", "learn santali for children",
              "santali ol chiki tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "santali english bilingual toddlers"],
))
