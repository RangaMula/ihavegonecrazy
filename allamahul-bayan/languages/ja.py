# -*- coding: utf-8 -*-
"""Book 46 - Japanese (the 46 basic hiragana, gojuuon order). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = one hiragana. The native-phonetics box shows the letter in its row of the fifty-sound
chart, its katakana twin and (where there is one) its form with the two dots ゛ or the circle ゜.
Transliteration: Hepburn romaji, long vowels doubled (oo, uu, ii), as in the house style."""
from generic import build, letter, section
from maps import region_map

ROWS = ["あいうえお", "かきくけこ", "さしすせそ", "たちつてと", "なにぬねの", "はひふへほ", "まみむめも",
        "やゆよ", "らりるれろ", "わを", "ん"]
KATA = dict(zip("".join(ROWS), "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"))
DAKU = {}
for plain, voiced, roms in (("かきくけこ", "がぎぐげご", "ga gi gu ge go"), ("さしすせそ", "ざじずぜぞ", "za ji zu ze zo"),
                            ("たちつてと", "だぢづでど", "da ji zu de do"), ("はひふへほ", "ばびぶべぼ", "ba bi bu be bo")):
    for p, v, r in zip(plain, voiced, roms.split()):
        DAKU[p] = (v, r)
HANDAKU = dict(zip("はひふへほ", zip("ぱぴぷぺぽ", "pa pi pu pe po".split())))


def nt(t):
    return f'<span class="nt">{t}</span>'


def K(kana, rom, sound, word, tr, meaning, pic, args=None, note=None):
    row = next(r for r in ROWS if kana in r)
    cells = " ".join(f'<span class="hl">{k}</span>' if k == kana else k for k in row)
    extra = f'Katakana twin: <span class="nt" style="font-size:17pt">{KATA[kana]}</span>'
    if kana in DAKU:
        v, r = DAKU[kana]
        extra += f' · with ゛: {nt(v)} <i>{r}</i>'
    if kana in HANDAKU:
        v, r = HANDAKU[kana]
        extra += f' · with ゜: {nt(v)} <i>{r}</i>'
    phon = (f'<div class="nt" style="font-size:20pt;line-height:1.5">{cells}</div>'
            f'<div style="font-size:11pt">{extra}</div>')
    return letter(kana, kana, rom, sound, word, tr, meaning, pic, phon, "Fifty-sound chart · katakana", args, note)


VOWELS = [
    K("あ", "a", "‘a’ as in “father”", "あめ", "ame", "rain", "raincloud"),
    K("い", "i", "‘ee’ as in “see”, short", "いえ", "ie", "house", "house"),
    K("う", "u", "‘oo’ as in “moon”, short, with relaxed lips", "うみ", "umi", "sea", "waves"),
    K("え", "e", "‘e’ as in “bed”", "えんぴつ", "enpitsu", "pencil", "ja_pencil"),
    K("お", "o", "‘o’ as in “go”, short and round", "おにぎり", "onigiri", "rice ball", "ja_onigiri"),
]

ROWS_KST = [
    K("か", "ka", "‘kah’", "かさ", "kasa", "umbrella", "umbrella"),
    K("き", "ki", "‘kee’ as in “key”", "き", "ki", "tree", "tree"),
    K("く", "ku", "‘koo’ as in “cool”", "くも", "kumo", "cloud", "clouds"),
    K("け", "ke", "‘ke’ as in “kettle”", "けいと", "keito", "knitting wool", "wool"),
    K("こ", "ko", "‘ko’ as in “coat”, short", "こま", "koma", "spinning top", "top"),
    K("さ", "sa", "‘sah’", "さくら", "sakura", "cherry blossom", "ja_sakura"),
    K("し", "shi", "‘shee’ as in “sheep”, not “see”!", "しお", "shio", "salt", "salt", args=dict(label="しお")),
    K("す", "su", "‘soo’, often said very softly", "すいか", "suika", "watermelon", "watermelon"),
    K("せ", "se", "‘se’ as in “set”", "せっけん", "sekken", "soap", "soap"),
    K("そ", "so", "‘so’ as in “soap”, short", "そろばん", "soroban", "abacus (a counting frame)", "ja_soroban"),
    K("た", "ta", "‘tah’", "たまご", "tamago", "egg", "egg"),
    K("ち", "chi", "‘chee’ as in “cheese”", "ちきゅう", "chikyuu", "the Earth", "globe"),
    K("つ", "tsu", "‘ts’ as at the end of “cats”, then ‘oo’", "つみき", "tsumiki", "building blocks", "blocks",
      args=dict(letters=("つ", "み", "き"))),
    K("て", "te", "‘te’ as in “ten”", "てがみ", "tegami", "letter (to post)", "envelope"),
    K("と", "to", "‘to’ as in “toe”, short", "とけい", "tokei", "clock", "clock"),
]

ROWS_NHM = [
    K("な", "na", "‘nah’", "なし", "nashi", "pear", "pear"),
    K("に", "ni", "‘nee’ as in “knee”", "にんじん", "ninjin", "carrot", "carrot"),
    K("ぬ", "nu", "‘noo’ as in “noodle”", "ぬりえ", "nurie", "coloring picture", "palette"),
    K("ね", "ne", "‘ne’ as in “net”", "ねぎ", "negi", "green onion", "ja_negi"),
    K("の", "no", "‘no’ as in “note”, short", "のこぎり", "nokogiri", "saw", "ja_saw"),
    K("は", "ha", "‘hah’; as the little word “wa” it says ‘wa’", "はな", "hana", "flower", "flower",
      note=f"In {nt('こんにちは')} (hello) the last {nt('は')} is read ‘wa’."),
    K("ひ", "hi", "‘hee’ as in “heel”", "ひこうき", "hikooki", "airplane", "plane"),
    K("ふ", "fu", "a soft ‘f’ blown between the lips, half-way to ‘hoo’", "ふうせん", "fuusen", "balloon", "balloon"),
    K("へ", "he", "‘he’ as in “hen”; as the little word “e” (to) it says ‘e’", "へちま", "hechima", "loofah gourd", "ja_hechima"),
    K("ほ", "ho", "‘ho’ as in “hope”, short", "ほし", "hoshi", "star", "star"),
    K("ま", "ma", "‘mah’", "まど", "mado", "window", "window"),
    K("み", "mi", "‘mee’ as in “meet”", "みず", "mizu", "water", "water"),
    K("む", "mu", "‘moo’", "むぎ", "mugi", "wheat", "ja_mugi"),
    K("め", "me", "‘me’ as in “met”", "めがね", "megane", "glasses", "glasses"),
    K("も", "mo", "‘mo’ as in “more”, short", "もも", "momo", "peach", "ja_momo"),
]

ROWS_LAST = [
    K("や", "ya", "‘ya’ as in “yard”", "やま", "yama", "mountain", "mountain"),
    K("ゆ", "yu", "‘you’", "ゆき", "yuki", "snow", "ja_yuki"),
    K("よ", "yo", "‘yo’ as in “yoga”", "よる", "yoru", "night", "moon"),
    K("ら", "ra", "‘ra’ with a light tap of the tongue, half-way between r, l and d", "らっかせい", "rakkasei", "peanuts", "ja_peanut"),
    K("り", "ri", "‘ree’, with a light tap", "りんご", "ringo", "apple", "apple"),
    K("る", "ru", "‘roo’, with a light tap", "くるみ", "kurumi", "walnut", "walnut",
      note=f"Few words start with {nt('る')}. Find it in the middle of {nt('くるみ')}!"),
    K("れ", "re", "‘re’ as in “red”, with a light tap", "れんこん", "renkon", "lotus root", "ja_renkon"),
    K("ろ", "ro", "‘ro’ as in “road”, short, with a light tap", "ろうそく", "roosoku", "candle", "ja_candle"),
    K("わ", "wa", "‘wa’ as in “wasp”", "わたあめ", "wataame", "cotton candy", "ja_wataame"),
    K("を", "o", "‘o’, just like お", "ほんを よむ", "hon o yomu", "read a book", "book",
      args=dict(left="あ い う", right="か き く"),
      note=f"{nt('を')} is only used as a little word after the thing you act on: {nt('ほんを よむ')}, “read a book”."),
    K("ん", "n", "a humming ‘n’ that takes a whole beat", "みかん", "mikan", "mandarin orange", "ja_mikan",
      note=f"{nt('ん')} never starts a word. Find it at the end of {nt('みかん')}!"),
]

INTRO_VOWELS = f"""<p>Japanese is written with <b>three kinds of letters</b> that work together in the same sentence.</p>
<div class="box" style="margin:0.08in 0"><h3>Hiragana {nt('ひらがな')}</h3>Round, flowing letters. Each one is a whole sound,
one beat: {nt('か')} is <i>ka</i>, {nt('き')} is <i>ki</i>. There are <b>46 basic hiragana</b>, and children learn them first.
This book teaches all 46.</div>
<div class="box" style="margin:0.08in 0"><h3>Katakana {nt('カタカナ')}</h3>A twin set of sharper letters with the same sounds,
used for words from other languages: {nt('パン')} <i>pan</i>, bread. Every page shows the katakana twin: {nt('あ ア')}.</div>
<div class="box" style="margin:0.08in 0"><h3>Kanji {nt('漢字')}</h3>Characters that came from Chinese. Each one stands for a word
or idea: {nt('山')} <i>yama</i>, mountain · {nt('木')} <i>ki</i>, tree · {nt('日')} <i>hi</i>, sun. Children learn them little by little at school.</div>
<div class="box"><h3>The fifty-sound chart {nt('ごじゅうおん')}</h3>The five vowels {nt('あ い う え お')} make the first row.
Every other row adds one consonant to them: {nt('か き く け こ')} is <i>ka ki ku ke ko</i>. This book follows the chart, row by row.</div>"""

INTRO_KST = f"""<p>Each row joins one consonant to the five vowels: <b>K</b> + a, i, u, e, o = {nt('か き く け こ')}.</p>
<div class="box" style="margin:0.1in 0"><h3>Watch out for three letters</h3>Three letters do not follow the pattern:
{nt('し')} is <i>shi</i>, {nt('ち')} is <i>chi</i> and {nt('つ')} is <i>tsu</i>.</div>
<div class="box" style="margin:0.1in 0"><h3>Two little dots ゛</h3>Two dots at the top right make the sound buzzy:
{nt('か → が')} (<i>ga</i>), {nt('さ → ざ')} (<i>za</i>), {nt('た → だ')} (<i>da</i>).</div>
<div class="box"><h3>A small つ</h3>A small {nt('っ')} means “hold for a beat”: {nt('せっけん')} is <i>sek-ken</i>, soap.</div>"""

INTRO_NHM = f"""<p>Three more rows: <b>N</b>, <b>H</b> and <b>M</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>A soft f</h3>{nt('ふ')} is <i>fu</i>: blow gently through your lips, as if
cooling a hot drink.</div>
<div class="box" style="margin:0.1in 0"><h3>Dots and a circle</h3>The H row can wear two dots or a little circle:
{nt('は → ば')} (<i>ba</i>), {nt('は → ぱ')} (<i>pa</i>).</div>
<div class="box"><h3>Look closely</h3>Some letters are cousins: {nt('ぬ')} and {nt('め')} differ only by a little loop,
and so do {nt('ね')} and {nt('れ')}. Trace them slowly!</div>"""

INTRO_LAST = f"""<p>The last rows: <b>Y</b>, <b>R</b> and <b>W</b>, and the letter {nt('ん')}.</p>
<div class="box" style="margin:0.1in 0"><h3>Only three in the Y row</h3>{nt('や ゆ よ')} — and their small forms join other letters:
{nt('き + ゃ = きゃ')} (<i>kya</i>).</div>
<div class="box" style="margin:0.1in 0"><h3>A tapped R</h3>Japanese <i>r</i> is a quick tap of the tongue behind the top teeth,
somewhere between English r, l and d.</div>
<div class="box"><h3>Two special letters</h3>{nt('を')} sounds like {nt('お')} but is only used as a little word in a sentence, and
{nt('ん')} is the only letter that is a sound all by itself, without a vowel.</div>"""

LANG = build(dict(
    code="ja", folder="book-46-japanese", series_no=46, isbn="", draft=True,
    name="Japanese", native="にほんご", native_tr="nihongo (in kanji: 日本語)", name_word="なまえ", write_word="かいてみよう",
    title_native="はじめての ひらがな", title_letters="あいうえお", belongs_native="この ほんの もちぬし",
    belongs_pic="ja_sakura", alphabet_native="ごじゅうおん", numbers_native="かず", numbers_tr="kazu",
    phrases_native="はじめての ことば",
    fonts=None,  # filled in below (CJK fonts come in many numbered subset files)
    disp_family="M PLUS Rounded 1c", text_family="M PLUS Rounded 1c",
    glyph_font=None,
    font_credit="M PLUS Rounded 1c",
    phon_feature="each letter’s row in the fifty-sound chart and its katakana twin (か · カ)",
    letters_word="Hiragana Letters",
    extra_css=".hl{border:2.5px solid #111;border-radius:8px;padding:0 4px}",
    sections=[
        section(VOWELS, label="HIRAGANA", chip="THE VOWELS", title="The Vowels", native="あいうえお",
                native_tr="a i u e o — the five vowels", intro_html=INTRO_VOWELS, chart_title="vowels", chart_cols=5,
                warmup_title="the vowels", warmup_cols=5),
        section(ROWS_KST, label="HIRAGANA", chip="ROWS K · S · T", title="The K, S and T Rows", native="か・さ・た",
                native_tr="ka, sa, ta", intro_html=INTRO_KST, chart_title="letters of the K, S and T rows",
                chart_cols=5, warmup_title="the K, S and T rows", warmup_cols=5),
        section(ROWS_NHM, label="HIRAGANA", chip="ROWS N · H · M", title="The N, H and M Rows", native="な・は・ま",
                native_tr="na, ha, ma", intro_html=INTRO_NHM, chart_title="letters of the N, H and M rows",
                chart_cols=5, warmup_title="the N, H and M rows", warmup_cols=5),
        section(ROWS_LAST, label="HIRAGANA", chip="ROWS Y · R · W · N", title="The Last Rows", native="や・ら・わ・ん",
                native_tr="ya, ra, wa, n", intro_html=INTRO_LAST, chart_title="letters of the Y, R and W rows, and ん",
                chart_cols=11, warmup_title="the last rows", warmup_cols=6),
    ],
    sound_notes=[
        "Every hiragana is <b>one beat</b>. <b>Doubled vowels</b> (aa, ii, uu, oo) are long: hold them for two beats, "
        "as in <i>fuusen</i> (balloon) and <i>chikyuu</i> (the Earth). <b>ei</b> sounds like a long ‘e’.",
        "The vowels are short and pure: <b>a</b> as in “father”, <b>i</b> as in “see”, <b>u</b> as in “moon”, "
        "<b>e</b> as in “bed”, <b>o</b> as in “go”.",
        "A <b>doubled consonant</b> (kk, pp, tt) means a tiny pause before it: <i>sek-ken</i>, <i>rak-kasei</i>.",
        "Japanese has <b>no strong stress</b>: say every beat evenly. The English letters follow <b>Hepburn romaji</b> "
        "(shi, chi, tsu, fu)."],
    phon_explain="The box marked <i>Fifty-sound chart · katakana</i> shows the letter in its row of the hiragana chart "
                 "(the letter in the box is the one on the page), its katakana twin, and the new letter it makes with "
                 "the two dots ゛ or the circle ゜.",
    standard="standard Tokyo Japanese",
    hello=[
        ("Who speaks it?", "About <b>125 million people</b> speak Japanese.<sup>³</sup>"),
        ("Where?", "In <b>Japan</b>, a country of thousands of islands in East Asia, and in Japanese families around the world."),
        ("How is it written?", "With three scripts together: <b>hiragana</b>, <b>katakana</b> and <b>kanji</b>. "
                               "Usually left to right, but many books are written from top to bottom."),
        ("How many letters?", "<b>46 basic hiragana</b>. Two little dots ゛ or a circle ゜ make more sounds: "
                              "<span class=\"nt\">か</span> ka → <span class=\"nt\">が</span> ga."),
        ("Two shapes, one sound", "Every hiragana has a <b>katakana</b> twin, used for words from other languages: "
                                  "<span class=\"nt\">あ ア · か カ · さ サ</span>."),
        ("Did you know?", "In their first year of school, Japanese children learn <b>80 kanji</b>, "
                          "like <span class=\"nt\">山</span> (mountain) and <span class=\"nt\">木</span> (tree)."),
    ],
    hello_pics=[("ja_sakura", {}), ("mountain", {}), ("mosque", {})],
    map=region_map(frame=[[128.4, 29.9], [147.4, 46.3]],
                   points=dict(tokyo=[139.69, 35.69], osaka=[135.50, 34.69], sapporo=[141.35, 43.06],
                               fukuoka=[130.40, 33.59]),
                   area=(137.9, 38.1, 600, 190), area_rot=-41,
                   cities=[("tokyo", "Tokyo", 14, 8, "start", False), ("osaka", "Osaka", 0, 36, "middle", False),
                           ("sapporo", "Sapporo", -14, 8, "end", False), ("fukuoka", "Fukuoka", -14, 8, "end", False)],
                   label="JAPAN", label_at=[136.0, 40.6], marker=[138.0, 37.0],
                   caption="The circle shows Japan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Japanese is spoken all over "
                          "Japan: in Tokyo, Osaka, Sapporo and Fukuoka, on the four big islands and on many small ones, "
                          "down to Okinawa in the south.",
                   seas=[("Pacific Ocean", 142.6, 32.6)]),
    digits=[("0", "ゼロ", "zero", "zero"), ("1", "一 · いち", "ichi", "one"), ("2", "二 · に", "ni", "two"),
            ("3", "三 · さん", "san", "three"), ("4", "四 · よん", "yon", "four"), ("5", "五 · ご", "go", "five"),
            ("6", "六 · ろく", "roku", "six"), ("7", "七 · なな", "nana", "seven"), ("8", "八 · はち", "hachi", "eight"),
            ("9", "九 · きゅう", "kyuu", "nine")],
    phrases=[("アッサラーム・アライクム", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("ワ・アライクム・アッサラーム", "wa alaikum assalaam", "And upon you be peace (the reply)"),
             ("こんにちは", "konnichiwa", "Hello!"),
             ("わたしの なまえは … です", "watashi no namae wa … desu", "My name is …"),
             ("ありがとう", "arigatoo", "Thank you"),
             ("ジャザーカッラーフ・ハイラン", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("おかあさん · おとうさん", "okaasan · otoosan", "Mother · Father"),
             ("おにいさん · おねえさん", "oniisan · oneesan", "Big brother · Big sister"),
             ("はい · いいえ", "hai · iie", "Yes · No"),
             ("にほんごを べんきょう しています！", "nihongo o benkyoo shite imasu!", "I am learning Japanese!")],
    cheer=("マーシャーアッラー！ よく できました！", "maashaa-allaah! yoku dekimashita!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); the first-year kanji list from Japan’s "
                 "<b>Ministry of Education (MEXT)</b>.",
    book_pic=dict(left="あ い う", right="か き く"),
    review_note="Check the romaji (Hepburn with doubled long vowels: hikooki, roosoku, chikyuu), the word choices "
                "(ぬりえ for ぬ, へちま for へ, らっかせい for ら, くるみ for る, ほんを よむ for を), the katakana spellings "
                "of the Muslim phrases (アッサラーム・アライクム, ジャザーカッラーフ・ハイラン, マーシャーアッラー) "
                "and the sound guides for ふ, つ and the R row.",
    tiles="あいうかさた", cover_pics=["ja_sakura", "apple", "star", "mosque"], title_size=48,
    speakers_blurb="Japanese is spoken by about 125 million people in Japan and around the world.",
    sample_words=[("さくら", "sakura", "cherry blossom"), ("りんご", "ringo", "apple"), ("ほし", "hoshi", "star")],
    keywords=["japanese hiragana book for kids", "learn japanese for children", "hiragana coloring book",
              "japanese letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual japanese english toddlers"],
))

# ---- fonts: M PLUS Rounded 1c, copied subset by subset from @fontsource ----
MPLUS = {
  400: [
    ('m-plus-rounded-1c-59-400-normal.woff2', 'U+a1-a4,U+a6-a7,U+aa,U+ac-ad,U+b5-b6,U+b8-ba,U+bc-c8,U+ca-cc,U+ce-d5,U+d9-db,U+dd-df,U+e6,U+ee,U+f0,U+f5,U+f7,U+f9,U+fb,U+fe-102,U+110-113,U+11a-11b,U+128-12b,U+143-144,U+147-148,U+14c,U+14e-14f,U+152-153,U+168-16d,U+192,U+1a0-1a1,U+1af,U+1cd-1dc,U+1f8-1f9,U+251,U+261,U+2bb,U+2c7,U+2c9,U+2ea-2eb,U+304,U+307,U+30c,U+1e3e-1e3f,U+1ea0-1ebe,U+1ec0-1ec6,U+1ec8-1ef9,U+2011-2012,U+2016,U+2018-201a,U+201e,U+2021,U+2030,U+2033,U+2035,U+2042,U+2047,U+2051,U+2074,U+20a9,U+20ab-20ac,U+20dd-20de,U+2100'),
    ('m-plus-rounded-1c-65-400-normal.woff2', 'U+b1,U+309b,U+4e5e,U+51f1,U+5506,U+55c5,U+58cc,U+59d1,U+5c51,U+5ef7,U+6284,U+62d7,U+6689,U+673d,U+6a2b,U+6a8e,U+6a9c,U+6d63,U+6dd1,U+70b8,U+7235,U+72db,U+72f8,U+7560,U+7c9b,U+7ce7,U+7e1e,U+80af,U+82eb,U+8463,U+8499,U+85dd,U+86ee,U+8a60,U+8a6e,U+8c79,U+8e87,U+8e8a,U+8f5f,U+9010,U+918d,U+9190,U+965b,U+97fb,U+9ab8,U+9bad,U+9d3b,U+9d5c,U+9dfa,U+9e93'),
    ('m-plus-rounded-1c-77-400-normal.woff2', 'U+2207,U+25ef,U+309c,U+4e4f,U+5146,U+51dd,U+5351,U+540a,U+5629,U+5eb5,U+5f04,U+5f13,U+60dc,U+6212,U+63b4,U+642c,U+6627,U+66a6,U+66c7,U+66fd,U+674e,U+6b96,U+6c4e,U+6df3,U+6e67,U+6f84,U+72fc,U+733f,U+7c97,U+7db1,U+7e4d,U+816b,U+82d1,U+84cb,U+854e,U+8607,U+86c7,U+871c,U+8776,U+8a89,U+8fc4,U+91a4,U+9285,U+9685,U+9903,U+9b31,U+9f13,U+ff42,U+ff74,U+ff91'),
    ('m-plus-rounded-1c-91-400-normal.woff2', 'U+60,U+2200,U+226b,U+2461,U+517c,U+526f,U+5800,U+5b97,U+5bf8,U+5c01,U+5d29,U+5e4c,U+5e81,U+6065,U+61d0,U+667a,U+6696,U+6843,U+6c99,U+6d99,U+6ec5,U+6f22,U+6f6e,U+6fa4,U+6fef,U+71c3,U+72d9,U+7384,U+78e8,U+7a1a,U+7a32,U+7a3c,U+7adc,U+7ca7,U+7d2b,U+7dad,U+7e4b,U+80a9,U+8170,U+81ed,U+820e,U+8a17,U+8afe,U+90aa,U+914e,U+963f,U+99c4,U+9eba,U+9f3b,U+ff38'),
    ('m-plus-rounded-1c-95-400-normal.woff2', 'U+2193,U+25b2,U+4e4b,U+516d,U+51c4,U+529f,U+52c9,U+5360,U+5442,U+5857,U+5915,U+59eb,U+5a9b,U+5c3b,U+6012,U+61b6,U+62b1,U+6311,U+6577,U+65e2,U+65ec,U+6613,U+6790,U+6cb9,U+7372,U+76ae,U+7d5e,U+7fcc,U+88ab,U+88d5,U+8caf,U+8ddd,U+8ecd,U+8f38,U+8f9e,U+8feb,U+9063,U+90f5,U+93e1,U+968a,U+968f,U+98fe,U+9ec4,U+ff1d,U+ff27,U+ff2a,U+ff36,U+ff3b,U+ff3d,U+ffe5'),
    ('m-plus-rounded-1c-96-400-normal.woff2', 'U+4e03,U+4f38,U+50b7,U+5264,U+5348,U+5371,U+585a,U+58ca,U+5951,U+59b9,U+59d4,U+5b98,U+5f8b,U+6388,U+64cd,U+65e7,U+6803,U+6b6f,U+6d66,U+6e0b,U+6ecb,U+6fc3,U+72ac,U+773c,U+77e2,U+7968,U+7a74,U+7dba,U+7dd1,U+7e3e,U+808c,U+811a,U+8179,U+8239,U+8584,U+8a0e,U+8a72,U+8b66,U+8c46,U+8f29,U+90a3,U+9234,U+96f0,U+9769,U+9774,U+9aa8,U+ff26,U+ff28,U+ff9e-ff9f'),
    ('m-plus-rounded-1c-101-400-normal.woff2', 'U+25bc,U+3012,U+4ef2,U+4f0a,U+516b,U+5373,U+539a,U+53b3,U+559c,U+56f0,U+5727,U+5742,U+5965,U+59ff,U+5bc6,U+5dfb,U+5e45,U+5ead,U+5fb3,U+6211,U+6253,U+639b,U+63a8,U+6545,U+6575,U+6628,U+672d,U+68a8,U+6bdb,U+6d25,U+707d,U+767e,U+7834,U+7b46,U+7bc9,U+8074,U+82e6,U+8349,U+8a2a,U+8d70,U+8da3,U+8fce,U+91cc,U+967d,U+97ff,U+9996,U+ff1c,U+ff2f,U+ff32,U+ff34'),
    ('m-plus-rounded-1c-102-400-normal.woff2', 'U+3d,U+5e,U+25cf,U+4e0e,U+4e5d,U+4e73,U+4e94,U+4f3c,U+5009,U+5145,U+51ac,U+5238,U+524a,U+53f3,U+547c,U+5802,U+5922,U+5a66,U+5c0e,U+5de6,U+5fd8,U+5feb,U+6797,U+685c,U+6b7b,U+6c5f-6c60,U+6cc9,U+6ce2,U+6d17,U+6e21,U+7167,U+7642,U+76db,U+8001,U+821e,U+8857,U+89d2,U+8b1b,U+8b70,U+8cb4,U+8cde,U+8f03,U+8f2a,U+968e,U+9b54,U+9e7f,U+9ebb,U+ff05,U+ff33'),
    ('m-plus-rounded-1c-107-400-normal.woff2', 'U+23,U+3c,U+2192,U+4e45,U+4efb,U+4f50,U+4f8b,U+4fc2,U+5024,U+5150,U+5272,U+5370,U+53bb,U+542b,U+56db,U+56e3,U+57ce,U+5bc4,U+5bcc,U+5f71,U+60aa,U+6238,U+6280,U+629c,U+6539,U+66ff,U+670d,U+677e-677f,U+6839,U+69cb,U+6b4c,U+6bb5,U+6e96,U+6f14,U+72ec,U+7389,U+7814,U+79cb,U+79d1,U+79fb,U+7a0e,U+7d0d,U+85e4,U+8d64,U+9632,U+96e2,U+9805,U+99ac,U+ff1e'),
    ('m-plus-rounded-1c-109-400-normal.woff2', 'U+266a,U+4f11,U+533a,U+5343,U+534a,U+53cd,U+5404,U+56f3,U+5b57-5b58,U+5bae,U+5c4a,U+5e0c,U+5e2f,U+5eab,U+5f35,U+5f79,U+614b,U+6226,U+629e,U+65c5,U+6625,U+6751,U+6821,U+6b69,U+6b8b,U+6bce,U+6c42,U+706b,U+7c21,U+7cfb,U+805e,U+80b2,U+82b8,U+843d,U+8853,U+88c5,U+8a3c,U+8a66,U+8d8a,U+8fba,U+9069,U+91cf,U+9752,U+975e,U+9999,U+ff0f-ff10,U+ff14-ff15'),
    ('m-plus-rounded-1c-111-400-normal.woff2', 'U+2b,U+d7,U+300e-300f,U+4e07,U+4e8c,U+512a,U+5149,U+518d,U+5236,U+52b9,U+52d9,U+5468,U+578b,U+57fa,U+5b8c,U+5ba2,U+5c02,U+5de5,U+5f37,U+5f62,U+623b,U+63d0,U+652f,U+672a,U+6848,U+6d41,U+7136,U+7537,U+754c,U+76f4,U+79c1,U+7ba1,U+7d44,U+7d4c,U+7dcf,U+7dda,U+7de8,U+82b1,U+897f,U+8ca9,U+8cfc,U+904e,U+9664,U+982d,U+9858,U+98a8,U+9a13,U+ff13,U+ff5c'),
    ('m-plus-rounded-1c-113-400-normal.woff2', 'U+26,U+5f,U+2026,U+203b,U+4e09,U+4eac,U+4ed5,U+4fa1,U+5143,U+5199,U+5207,U+539f,U+53e3,U+53f7,U+5411,U+5473,U+5546,U+55b6,U+5929,U+597d,U+5bb9,U+5c11,U+5c4b,U+5ddd,U+5f97,U+5fc5,U+6295,U+6301,U+6307,U+671b,U+76f8,U+78ba,U+795e,U+7d30,U+7d39,U+7d9a,U+89e3,U+8a00,U+8a73,U+8a8d,U+8a9e,U+8aad,U+8abf,U+8cea,U+8eca,U+8ffd,U+904b,U+9650,U+ff11-ff12'),
    ('m-plus-rounded-1c-114-400-normal.woff2', 'U+3e,U+3005,U+4e0d,U+4e88,U+4ecb,U+4ee3,U+4ef6,U+4fdd,U+4fe1,U+500b,U+50cf,U+5186,U+5316,U+53d7,U+540c,U+544a,U+54e1,U+5728,U+58f2,U+5973,U+5b89,U+5c71,U+5e02,U+5e97,U+5f15,U+5fc3,U+5fdc,U+601d,U+611b,U+611f,U+671f,U+6728,U+6765,U+683c,U+6b21,U+6ce8,U+6d3b,U+6d77,U+7530,U+7740,U+7acb,U+7d50,U+826f,U+8f09,U+8fbc,U+9001,U+9053,U+91ce,U+9762,U+98df'),
    ('m-plus-rounded-1c-115-400-normal.woff2', 'U+7c,U+3080,U+4ee5,U+5148,U+516c,U+521d,U+5225,U+529b,U+52a0,U+53ef,U+56de,U+56fd,U+5909,U+591a,U+5b66,U+5b9f,U+5bb6,U+5bfe,U+5e73,U+5e83,U+5ea6,U+5f53,U+6027,U+610f,U+6210,U+6240,U+660e,U+66f4,U+66f8,U+6709,U+6771,U+697d,U+69d8,U+6a5f,U+6c34,U+6cbb,U+73fe,U+756a,U+7684,U+771f,U+793a,U+7f8e,U+898f,U+8a2d,U+8a71,U+8fd1,U+9078,U+9577,U+96fb,U+ff5e'),
    ('m-plus-rounded-1c-116-400-normal.woff2', 'U+a9,U+3010-3011,U+30e2,U+4e0b,U+4eca,U+4ed6,U+4ed8,U+4f53,U+4f5c,U+4f7f,U+53d6,U+540d,U+54c1,U+5730,U+5916,U+5b50,U+5c0f,U+5f8c,U+624b,U+6570,U+6587,U+6599,U+691c,U+696d,U+6cd5,U+7269,U+7279,U+7406,U+767a-767b,U+77e5,U+7d04,U+7d22,U+8005,U+80fd,U+81ea,U+8868,U+8981,U+89a7,U+901a,U+9023,U+90e8,U+91d1,U+9332,U+958b,U+96c6,U+9ad8,U+ff1a,U+ff1f'),
    ('m-plus-rounded-1c-117-400-normal.woff2', 'U+4e,U+a0,U+3000,U+300c-300d,U+4e00,U+4e0a,U+4e2d,U+4e8b,U+4eba,U+4f1a,U+5165,U+5168,U+5185,U+51fa,U+5206,U+5229,U+524d,U+52d5,U+5408,U+554f,U+5831,U+5834,U+5927,U+5b9a,U+5e74,U+5f0f,U+60c5,U+65b0,U+65b9,U+6642,U+6700,U+672c,U+682a,U+6b63,U+6c17,U+7121,U+751f,U+7528,U+753b,U+76ee,U+793e,U+884c,U+898b,U+8a18,U+9593,U+95a2,U+ff01,U+ff08-ff09'),
    ('m-plus-rounded-1c-118-400-normal.woff2', 'U+21-22,U+27-2a,U+2c-3b,U+3f,U+41-4d,U+4f-5d,U+61-7b,U+7d,U+ab,U+ae,U+b2-b3,U+b7,U+bb,U+c9,U+cd,U+d6,U+d8,U+dc,U+e0-e5,U+e7-ed,U+ef,U+f1-f4,U+f6,U+f8,U+fa,U+fc-fd,U+103,U+14d,U+1b0,U+300-301,U+1ebf,U+1ec7,U+2013-2014,U+201c-201d,U+2039-203a,U+203c,U+2048-2049,U+2113,U+2122,U+65e5,U+6708,U+70b9'),
    ('m-plus-rounded-1c-119-400-normal.woff2', 'U+20,U+2027,U+3001-3002,U+3041-307f,U+3081-308f,U+3091-3093,U+3099-309a,U+309d-309e,U+30a1-30e1,U+30e3-30ed,U+30ef-30f0,U+30f2-30f4,U+30fb-30fe,U+ff0c,U+ff0e'),
    ('m-plus-rounded-1c-latin-400-normal.woff2', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'),
  ],
  700: [
    ('m-plus-rounded-1c-59-700-normal.woff2', 'U+a1-a4,U+a6-a7,U+aa,U+ac-ad,U+b5-b6,U+b8-ba,U+bc-c8,U+ca-cc,U+ce-d5,U+d9-db,U+dd-df,U+e6,U+ee,U+f0,U+f5,U+f7,U+f9,U+fb,U+fe-102,U+110-113,U+11a-11b,U+128-12b,U+143-144,U+147-148,U+14c,U+14e-14f,U+152-153,U+168-16d,U+192,U+1a0-1a1,U+1af,U+1cd-1dc,U+1f8-1f9,U+251,U+261,U+2bb,U+2c7,U+2c9,U+2ea-2eb,U+304,U+307,U+30c,U+1e3e-1e3f,U+1ea0-1ebe,U+1ec0-1ec6,U+1ec8-1ef9,U+2011-2012,U+2016,U+2018-201a,U+201e,U+2021,U+2030,U+2033,U+2035,U+2042,U+2047,U+2051,U+2074,U+20a9,U+20ab-20ac,U+20dd-20de,U+2100'),
    ('m-plus-rounded-1c-65-700-normal.woff2', 'U+b1,U+309b,U+4e5e,U+51f1,U+5506,U+55c5,U+58cc,U+59d1,U+5c51,U+5ef7,U+6284,U+62d7,U+6689,U+673d,U+6a2b,U+6a8e,U+6a9c,U+6d63,U+6dd1,U+70b8,U+7235,U+72db,U+72f8,U+7560,U+7c9b,U+7ce7,U+7e1e,U+80af,U+82eb,U+8463,U+8499,U+85dd,U+86ee,U+8a60,U+8a6e,U+8c79,U+8e87,U+8e8a,U+8f5f,U+9010,U+918d,U+9190,U+965b,U+97fb,U+9ab8,U+9bad,U+9d3b,U+9d5c,U+9dfa,U+9e93'),
    ('m-plus-rounded-1c-77-700-normal.woff2', 'U+2207,U+25ef,U+309c,U+4e4f,U+5146,U+51dd,U+5351,U+540a,U+5629,U+5eb5,U+5f04,U+5f13,U+60dc,U+6212,U+63b4,U+642c,U+6627,U+66a6,U+66c7,U+66fd,U+674e,U+6b96,U+6c4e,U+6df3,U+6e67,U+6f84,U+72fc,U+733f,U+7c97,U+7db1,U+7e4d,U+816b,U+82d1,U+84cb,U+854e,U+8607,U+86c7,U+871c,U+8776,U+8a89,U+8fc4,U+91a4,U+9285,U+9685,U+9903,U+9b31,U+9f13,U+ff42,U+ff74,U+ff91'),
    ('m-plus-rounded-1c-91-700-normal.woff2', 'U+60,U+2200,U+226b,U+2461,U+517c,U+526f,U+5800,U+5b97,U+5bf8,U+5c01,U+5d29,U+5e4c,U+5e81,U+6065,U+61d0,U+667a,U+6696,U+6843,U+6c99,U+6d99,U+6ec5,U+6f22,U+6f6e,U+6fa4,U+6fef,U+71c3,U+72d9,U+7384,U+78e8,U+7a1a,U+7a32,U+7a3c,U+7adc,U+7ca7,U+7d2b,U+7dad,U+7e4b,U+80a9,U+8170,U+81ed,U+820e,U+8a17,U+8afe,U+90aa,U+914e,U+963f,U+99c4,U+9eba,U+9f3b,U+ff38'),
    ('m-plus-rounded-1c-95-700-normal.woff2', 'U+2193,U+25b2,U+4e4b,U+516d,U+51c4,U+529f,U+52c9,U+5360,U+5442,U+5857,U+5915,U+59eb,U+5a9b,U+5c3b,U+6012,U+61b6,U+62b1,U+6311,U+6577,U+65e2,U+65ec,U+6613,U+6790,U+6cb9,U+7372,U+76ae,U+7d5e,U+7fcc,U+88ab,U+88d5,U+8caf,U+8ddd,U+8ecd,U+8f38,U+8f9e,U+8feb,U+9063,U+90f5,U+93e1,U+968a,U+968f,U+98fe,U+9ec4,U+ff1d,U+ff27,U+ff2a,U+ff36,U+ff3b,U+ff3d,U+ffe5'),
    ('m-plus-rounded-1c-96-700-normal.woff2', 'U+4e03,U+4f38,U+50b7,U+5264,U+5348,U+5371,U+585a,U+58ca,U+5951,U+59b9,U+59d4,U+5b98,U+5f8b,U+6388,U+64cd,U+65e7,U+6803,U+6b6f,U+6d66,U+6e0b,U+6ecb,U+6fc3,U+72ac,U+773c,U+77e2,U+7968,U+7a74,U+7dba,U+7dd1,U+7e3e,U+808c,U+811a,U+8179,U+8239,U+8584,U+8a0e,U+8a72,U+8b66,U+8c46,U+8f29,U+90a3,U+9234,U+96f0,U+9769,U+9774,U+9aa8,U+ff26,U+ff28,U+ff9e-ff9f'),
    ('m-plus-rounded-1c-101-700-normal.woff2', 'U+25bc,U+3012,U+4ef2,U+4f0a,U+516b,U+5373,U+539a,U+53b3,U+559c,U+56f0,U+5727,U+5742,U+5965,U+59ff,U+5bc6,U+5dfb,U+5e45,U+5ead,U+5fb3,U+6211,U+6253,U+639b,U+63a8,U+6545,U+6575,U+6628,U+672d,U+68a8,U+6bdb,U+6d25,U+707d,U+767e,U+7834,U+7b46,U+7bc9,U+8074,U+82e6,U+8349,U+8a2a,U+8d70,U+8da3,U+8fce,U+91cc,U+967d,U+97ff,U+9996,U+ff1c,U+ff2f,U+ff32,U+ff34'),
    ('m-plus-rounded-1c-102-700-normal.woff2', 'U+3d,U+5e,U+25cf,U+4e0e,U+4e5d,U+4e73,U+4e94,U+4f3c,U+5009,U+5145,U+51ac,U+5238,U+524a,U+53f3,U+547c,U+5802,U+5922,U+5a66,U+5c0e,U+5de6,U+5fd8,U+5feb,U+6797,U+685c,U+6b7b,U+6c5f-6c60,U+6cc9,U+6ce2,U+6d17,U+6e21,U+7167,U+7642,U+76db,U+8001,U+821e,U+8857,U+89d2,U+8b1b,U+8b70,U+8cb4,U+8cde,U+8f03,U+8f2a,U+968e,U+9b54,U+9e7f,U+9ebb,U+ff05,U+ff33'),
    ('m-plus-rounded-1c-107-700-normal.woff2', 'U+23,U+3c,U+2192,U+4e45,U+4efb,U+4f50,U+4f8b,U+4fc2,U+5024,U+5150,U+5272,U+5370,U+53bb,U+542b,U+56db,U+56e3,U+57ce,U+5bc4,U+5bcc,U+5f71,U+60aa,U+6238,U+6280,U+629c,U+6539,U+66ff,U+670d,U+677e-677f,U+6839,U+69cb,U+6b4c,U+6bb5,U+6e96,U+6f14,U+72ec,U+7389,U+7814,U+79cb,U+79d1,U+79fb,U+7a0e,U+7d0d,U+85e4,U+8d64,U+9632,U+96e2,U+9805,U+99ac,U+ff1e'),
    ('m-plus-rounded-1c-109-700-normal.woff2', 'U+266a,U+4f11,U+533a,U+5343,U+534a,U+53cd,U+5404,U+56f3,U+5b57-5b58,U+5bae,U+5c4a,U+5e0c,U+5e2f,U+5eab,U+5f35,U+5f79,U+614b,U+6226,U+629e,U+65c5,U+6625,U+6751,U+6821,U+6b69,U+6b8b,U+6bce,U+6c42,U+706b,U+7c21,U+7cfb,U+805e,U+80b2,U+82b8,U+843d,U+8853,U+88c5,U+8a3c,U+8a66,U+8d8a,U+8fba,U+9069,U+91cf,U+9752,U+975e,U+9999,U+ff0f-ff10,U+ff14-ff15'),
    ('m-plus-rounded-1c-111-700-normal.woff2', 'U+2b,U+d7,U+300e-300f,U+4e07,U+4e8c,U+512a,U+5149,U+518d,U+5236,U+52b9,U+52d9,U+5468,U+578b,U+57fa,U+5b8c,U+5ba2,U+5c02,U+5de5,U+5f37,U+5f62,U+623b,U+63d0,U+652f,U+672a,U+6848,U+6d41,U+7136,U+7537,U+754c,U+76f4,U+79c1,U+7ba1,U+7d44,U+7d4c,U+7dcf,U+7dda,U+7de8,U+82b1,U+897f,U+8ca9,U+8cfc,U+904e,U+9664,U+982d,U+9858,U+98a8,U+9a13,U+ff13,U+ff5c'),
    ('m-plus-rounded-1c-113-700-normal.woff2', 'U+26,U+5f,U+2026,U+203b,U+4e09,U+4eac,U+4ed5,U+4fa1,U+5143,U+5199,U+5207,U+539f,U+53e3,U+53f7,U+5411,U+5473,U+5546,U+55b6,U+5929,U+597d,U+5bb9,U+5c11,U+5c4b,U+5ddd,U+5f97,U+5fc5,U+6295,U+6301,U+6307,U+671b,U+76f8,U+78ba,U+795e,U+7d30,U+7d39,U+7d9a,U+89e3,U+8a00,U+8a73,U+8a8d,U+8a9e,U+8aad,U+8abf,U+8cea,U+8eca,U+8ffd,U+904b,U+9650,U+ff11-ff12'),
    ('m-plus-rounded-1c-114-700-normal.woff2', 'U+3e,U+3005,U+4e0d,U+4e88,U+4ecb,U+4ee3,U+4ef6,U+4fdd,U+4fe1,U+500b,U+50cf,U+5186,U+5316,U+53d7,U+540c,U+544a,U+54e1,U+5728,U+58f2,U+5973,U+5b89,U+5c71,U+5e02,U+5e97,U+5f15,U+5fc3,U+5fdc,U+601d,U+611b,U+611f,U+671f,U+6728,U+6765,U+683c,U+6b21,U+6ce8,U+6d3b,U+6d77,U+7530,U+7740,U+7acb,U+7d50,U+826f,U+8f09,U+8fbc,U+9001,U+9053,U+91ce,U+9762,U+98df'),
    ('m-plus-rounded-1c-115-700-normal.woff2', 'U+7c,U+3080,U+4ee5,U+5148,U+516c,U+521d,U+5225,U+529b,U+52a0,U+53ef,U+56de,U+56fd,U+5909,U+591a,U+5b66,U+5b9f,U+5bb6,U+5bfe,U+5e73,U+5e83,U+5ea6,U+5f53,U+6027,U+610f,U+6210,U+6240,U+660e,U+66f4,U+66f8,U+6709,U+6771,U+697d,U+69d8,U+6a5f,U+6c34,U+6cbb,U+73fe,U+756a,U+7684,U+771f,U+793a,U+7f8e,U+898f,U+8a2d,U+8a71,U+8fd1,U+9078,U+9577,U+96fb,U+ff5e'),
    ('m-plus-rounded-1c-116-700-normal.woff2', 'U+a9,U+3010-3011,U+30e2,U+4e0b,U+4eca,U+4ed6,U+4ed8,U+4f53,U+4f5c,U+4f7f,U+53d6,U+540d,U+54c1,U+5730,U+5916,U+5b50,U+5c0f,U+5f8c,U+624b,U+6570,U+6587,U+6599,U+691c,U+696d,U+6cd5,U+7269,U+7279,U+7406,U+767a-767b,U+77e5,U+7d04,U+7d22,U+8005,U+80fd,U+81ea,U+8868,U+8981,U+89a7,U+901a,U+9023,U+90e8,U+91d1,U+9332,U+958b,U+96c6,U+9ad8,U+ff1a,U+ff1f'),
    ('m-plus-rounded-1c-117-700-normal.woff2', 'U+4e,U+a0,U+3000,U+300c-300d,U+4e00,U+4e0a,U+4e2d,U+4e8b,U+4eba,U+4f1a,U+5165,U+5168,U+5185,U+51fa,U+5206,U+5229,U+524d,U+52d5,U+5408,U+554f,U+5831,U+5834,U+5927,U+5b9a,U+5e74,U+5f0f,U+60c5,U+65b0,U+65b9,U+6642,U+6700,U+672c,U+682a,U+6b63,U+6c17,U+7121,U+751f,U+7528,U+753b,U+76ee,U+793e,U+884c,U+898b,U+8a18,U+9593,U+95a2,U+ff01,U+ff08-ff09'),
    ('m-plus-rounded-1c-118-700-normal.woff2', 'U+21-22,U+27-2a,U+2c-3b,U+3f,U+41-4d,U+4f-5d,U+61-7b,U+7d,U+ab,U+ae,U+b2-b3,U+b7,U+bb,U+c9,U+cd,U+d6,U+d8,U+dc,U+e0-e5,U+e7-ed,U+ef,U+f1-f4,U+f6,U+f8,U+fa,U+fc-fd,U+103,U+14d,U+1b0,U+300-301,U+1ebf,U+1ec7,U+2013-2014,U+201c-201d,U+2039-203a,U+203c,U+2048-2049,U+2113,U+2122,U+65e5,U+6708,U+70b9'),
    ('m-plus-rounded-1c-119-700-normal.woff2', 'U+20,U+2027,U+3001-3002,U+3041-307f,U+3081-308f,U+3091-3093,U+3099-309a,U+309d-309e,U+30a1-30e1,U+30e3-30ed,U+30ef-30f0,U+30f2-30f4,U+30fb-30fe,U+ff0c,U+ff0e'),
    ('m-plus-rounded-1c-latin-700-normal.woff2', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'),
  ],
  800: [
    ('m-plus-rounded-1c-59-800-normal.woff2', 'U+a1-a4,U+a6-a7,U+aa,U+ac-ad,U+b5-b6,U+b8-ba,U+bc-c8,U+ca-cc,U+ce-d5,U+d9-db,U+dd-df,U+e6,U+ee,U+f0,U+f5,U+f7,U+f9,U+fb,U+fe-102,U+110-113,U+11a-11b,U+128-12b,U+143-144,U+147-148,U+14c,U+14e-14f,U+152-153,U+168-16d,U+192,U+1a0-1a1,U+1af,U+1cd-1dc,U+1f8-1f9,U+251,U+261,U+2bb,U+2c7,U+2c9,U+2ea-2eb,U+304,U+307,U+30c,U+1e3e-1e3f,U+1ea0-1ebe,U+1ec0-1ec6,U+1ec8-1ef9,U+2011-2012,U+2016,U+2018-201a,U+201e,U+2021,U+2030,U+2033,U+2035,U+2042,U+2047,U+2051,U+2074,U+20a9,U+20ab-20ac,U+20dd-20de,U+2100'),
    ('m-plus-rounded-1c-65-800-normal.woff2', 'U+b1,U+309b,U+4e5e,U+51f1,U+5506,U+55c5,U+58cc,U+59d1,U+5c51,U+5ef7,U+6284,U+62d7,U+6689,U+673d,U+6a2b,U+6a8e,U+6a9c,U+6d63,U+6dd1,U+70b8,U+7235,U+72db,U+72f8,U+7560,U+7c9b,U+7ce7,U+7e1e,U+80af,U+82eb,U+8463,U+8499,U+85dd,U+86ee,U+8a60,U+8a6e,U+8c79,U+8e87,U+8e8a,U+8f5f,U+9010,U+918d,U+9190,U+965b,U+97fb,U+9ab8,U+9bad,U+9d3b,U+9d5c,U+9dfa,U+9e93'),
    ('m-plus-rounded-1c-77-800-normal.woff2', 'U+2207,U+25ef,U+309c,U+4e4f,U+5146,U+51dd,U+5351,U+540a,U+5629,U+5eb5,U+5f04,U+5f13,U+60dc,U+6212,U+63b4,U+642c,U+6627,U+66a6,U+66c7,U+66fd,U+674e,U+6b96,U+6c4e,U+6df3,U+6e67,U+6f84,U+72fc,U+733f,U+7c97,U+7db1,U+7e4d,U+816b,U+82d1,U+84cb,U+854e,U+8607,U+86c7,U+871c,U+8776,U+8a89,U+8fc4,U+91a4,U+9285,U+9685,U+9903,U+9b31,U+9f13,U+ff42,U+ff74,U+ff91'),
    ('m-plus-rounded-1c-91-800-normal.woff2', 'U+60,U+2200,U+226b,U+2461,U+517c,U+526f,U+5800,U+5b97,U+5bf8,U+5c01,U+5d29,U+5e4c,U+5e81,U+6065,U+61d0,U+667a,U+6696,U+6843,U+6c99,U+6d99,U+6ec5,U+6f22,U+6f6e,U+6fa4,U+6fef,U+71c3,U+72d9,U+7384,U+78e8,U+7a1a,U+7a32,U+7a3c,U+7adc,U+7ca7,U+7d2b,U+7dad,U+7e4b,U+80a9,U+8170,U+81ed,U+820e,U+8a17,U+8afe,U+90aa,U+914e,U+963f,U+99c4,U+9eba,U+9f3b,U+ff38'),
    ('m-plus-rounded-1c-95-800-normal.woff2', 'U+2193,U+25b2,U+4e4b,U+516d,U+51c4,U+529f,U+52c9,U+5360,U+5442,U+5857,U+5915,U+59eb,U+5a9b,U+5c3b,U+6012,U+61b6,U+62b1,U+6311,U+6577,U+65e2,U+65ec,U+6613,U+6790,U+6cb9,U+7372,U+76ae,U+7d5e,U+7fcc,U+88ab,U+88d5,U+8caf,U+8ddd,U+8ecd,U+8f38,U+8f9e,U+8feb,U+9063,U+90f5,U+93e1,U+968a,U+968f,U+98fe,U+9ec4,U+ff1d,U+ff27,U+ff2a,U+ff36,U+ff3b,U+ff3d,U+ffe5'),
    ('m-plus-rounded-1c-96-800-normal.woff2', 'U+4e03,U+4f38,U+50b7,U+5264,U+5348,U+5371,U+585a,U+58ca,U+5951,U+59b9,U+59d4,U+5b98,U+5f8b,U+6388,U+64cd,U+65e7,U+6803,U+6b6f,U+6d66,U+6e0b,U+6ecb,U+6fc3,U+72ac,U+773c,U+77e2,U+7968,U+7a74,U+7dba,U+7dd1,U+7e3e,U+808c,U+811a,U+8179,U+8239,U+8584,U+8a0e,U+8a72,U+8b66,U+8c46,U+8f29,U+90a3,U+9234,U+96f0,U+9769,U+9774,U+9aa8,U+ff26,U+ff28,U+ff9e-ff9f'),
    ('m-plus-rounded-1c-101-800-normal.woff2', 'U+25bc,U+3012,U+4ef2,U+4f0a,U+516b,U+5373,U+539a,U+53b3,U+559c,U+56f0,U+5727,U+5742,U+5965,U+59ff,U+5bc6,U+5dfb,U+5e45,U+5ead,U+5fb3,U+6211,U+6253,U+639b,U+63a8,U+6545,U+6575,U+6628,U+672d,U+68a8,U+6bdb,U+6d25,U+707d,U+767e,U+7834,U+7b46,U+7bc9,U+8074,U+82e6,U+8349,U+8a2a,U+8d70,U+8da3,U+8fce,U+91cc,U+967d,U+97ff,U+9996,U+ff1c,U+ff2f,U+ff32,U+ff34'),
    ('m-plus-rounded-1c-102-800-normal.woff2', 'U+3d,U+5e,U+25cf,U+4e0e,U+4e5d,U+4e73,U+4e94,U+4f3c,U+5009,U+5145,U+51ac,U+5238,U+524a,U+53f3,U+547c,U+5802,U+5922,U+5a66,U+5c0e,U+5de6,U+5fd8,U+5feb,U+6797,U+685c,U+6b7b,U+6c5f-6c60,U+6cc9,U+6ce2,U+6d17,U+6e21,U+7167,U+7642,U+76db,U+8001,U+821e,U+8857,U+89d2,U+8b1b,U+8b70,U+8cb4,U+8cde,U+8f03,U+8f2a,U+968e,U+9b54,U+9e7f,U+9ebb,U+ff05,U+ff33'),
    ('m-plus-rounded-1c-107-800-normal.woff2', 'U+23,U+3c,U+2192,U+4e45,U+4efb,U+4f50,U+4f8b,U+4fc2,U+5024,U+5150,U+5272,U+5370,U+53bb,U+542b,U+56db,U+56e3,U+57ce,U+5bc4,U+5bcc,U+5f71,U+60aa,U+6238,U+6280,U+629c,U+6539,U+66ff,U+670d,U+677e-677f,U+6839,U+69cb,U+6b4c,U+6bb5,U+6e96,U+6f14,U+72ec,U+7389,U+7814,U+79cb,U+79d1,U+79fb,U+7a0e,U+7d0d,U+85e4,U+8d64,U+9632,U+96e2,U+9805,U+99ac,U+ff1e'),
    ('m-plus-rounded-1c-109-800-normal.woff2', 'U+266a,U+4f11,U+533a,U+5343,U+534a,U+53cd,U+5404,U+56f3,U+5b57-5b58,U+5bae,U+5c4a,U+5e0c,U+5e2f,U+5eab,U+5f35,U+5f79,U+614b,U+6226,U+629e,U+65c5,U+6625,U+6751,U+6821,U+6b69,U+6b8b,U+6bce,U+6c42,U+706b,U+7c21,U+7cfb,U+805e,U+80b2,U+82b8,U+843d,U+8853,U+88c5,U+8a3c,U+8a66,U+8d8a,U+8fba,U+9069,U+91cf,U+9752,U+975e,U+9999,U+ff0f-ff10,U+ff14-ff15'),
    ('m-plus-rounded-1c-111-800-normal.woff2', 'U+2b,U+d7,U+300e-300f,U+4e07,U+4e8c,U+512a,U+5149,U+518d,U+5236,U+52b9,U+52d9,U+5468,U+578b,U+57fa,U+5b8c,U+5ba2,U+5c02,U+5de5,U+5f37,U+5f62,U+623b,U+63d0,U+652f,U+672a,U+6848,U+6d41,U+7136,U+7537,U+754c,U+76f4,U+79c1,U+7ba1,U+7d44,U+7d4c,U+7dcf,U+7dda,U+7de8,U+82b1,U+897f,U+8ca9,U+8cfc,U+904e,U+9664,U+982d,U+9858,U+98a8,U+9a13,U+ff13,U+ff5c'),
    ('m-plus-rounded-1c-113-800-normal.woff2', 'U+26,U+5f,U+2026,U+203b,U+4e09,U+4eac,U+4ed5,U+4fa1,U+5143,U+5199,U+5207,U+539f,U+53e3,U+53f7,U+5411,U+5473,U+5546,U+55b6,U+5929,U+597d,U+5bb9,U+5c11,U+5c4b,U+5ddd,U+5f97,U+5fc5,U+6295,U+6301,U+6307,U+671b,U+76f8,U+78ba,U+795e,U+7d30,U+7d39,U+7d9a,U+89e3,U+8a00,U+8a73,U+8a8d,U+8a9e,U+8aad,U+8abf,U+8cea,U+8eca,U+8ffd,U+904b,U+9650,U+ff11-ff12'),
    ('m-plus-rounded-1c-114-800-normal.woff2', 'U+3e,U+3005,U+4e0d,U+4e88,U+4ecb,U+4ee3,U+4ef6,U+4fdd,U+4fe1,U+500b,U+50cf,U+5186,U+5316,U+53d7,U+540c,U+544a,U+54e1,U+5728,U+58f2,U+5973,U+5b89,U+5c71,U+5e02,U+5e97,U+5f15,U+5fc3,U+5fdc,U+601d,U+611b,U+611f,U+671f,U+6728,U+6765,U+683c,U+6b21,U+6ce8,U+6d3b,U+6d77,U+7530,U+7740,U+7acb,U+7d50,U+826f,U+8f09,U+8fbc,U+9001,U+9053,U+91ce,U+9762,U+98df'),
    ('m-plus-rounded-1c-115-800-normal.woff2', 'U+7c,U+3080,U+4ee5,U+5148,U+516c,U+521d,U+5225,U+529b,U+52a0,U+53ef,U+56de,U+56fd,U+5909,U+591a,U+5b66,U+5b9f,U+5bb6,U+5bfe,U+5e73,U+5e83,U+5ea6,U+5f53,U+6027,U+610f,U+6210,U+6240,U+660e,U+66f4,U+66f8,U+6709,U+6771,U+697d,U+69d8,U+6a5f,U+6c34,U+6cbb,U+73fe,U+756a,U+7684,U+771f,U+793a,U+7f8e,U+898f,U+8a2d,U+8a71,U+8fd1,U+9078,U+9577,U+96fb,U+ff5e'),
    ('m-plus-rounded-1c-116-800-normal.woff2', 'U+a9,U+3010-3011,U+30e2,U+4e0b,U+4eca,U+4ed6,U+4ed8,U+4f53,U+4f5c,U+4f7f,U+53d6,U+540d,U+54c1,U+5730,U+5916,U+5b50,U+5c0f,U+5f8c,U+624b,U+6570,U+6587,U+6599,U+691c,U+696d,U+6cd5,U+7269,U+7279,U+7406,U+767a-767b,U+77e5,U+7d04,U+7d22,U+8005,U+80fd,U+81ea,U+8868,U+8981,U+89a7,U+901a,U+9023,U+90e8,U+91d1,U+9332,U+958b,U+96c6,U+9ad8,U+ff1a,U+ff1f'),
    ('m-plus-rounded-1c-117-800-normal.woff2', 'U+4e,U+a0,U+3000,U+300c-300d,U+4e00,U+4e0a,U+4e2d,U+4e8b,U+4eba,U+4f1a,U+5165,U+5168,U+5185,U+51fa,U+5206,U+5229,U+524d,U+52d5,U+5408,U+554f,U+5831,U+5834,U+5927,U+5b9a,U+5e74,U+5f0f,U+60c5,U+65b0,U+65b9,U+6642,U+6700,U+672c,U+682a,U+6b63,U+6c17,U+7121,U+751f,U+7528,U+753b,U+76ee,U+793e,U+884c,U+898b,U+8a18,U+9593,U+95a2,U+ff01,U+ff08-ff09'),
    ('m-plus-rounded-1c-118-800-normal.woff2', 'U+21-22,U+27-2a,U+2c-3b,U+3f,U+41-4d,U+4f-5d,U+61-7b,U+7d,U+ab,U+ae,U+b2-b3,U+b7,U+bb,U+c9,U+cd,U+d6,U+d8,U+dc,U+e0-e5,U+e7-ed,U+ef,U+f1-f4,U+f6,U+f8,U+fa,U+fc-fd,U+103,U+14d,U+1b0,U+300-301,U+1ebf,U+1ec7,U+2013-2014,U+201c-201d,U+2039-203a,U+203c,U+2048-2049,U+2113,U+2122,U+65e5,U+6708,U+70b9'),
    ('m-plus-rounded-1c-119-800-normal.woff2', 'U+20,U+2027,U+3001-3002,U+3041-307f,U+3081-308f,U+3091-3093,U+3099-309a,U+309d-309e,U+30a1-30e1,U+30e3-30ed,U+30ef-30f0,U+30f2-30f4,U+30fb-30fe,U+ff0c,U+ff0e'),
    ('m-plus-rounded-1c-latin-ext-800-normal.woff2', 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'),
    ('m-plus-rounded-1c-latin-800-normal.woff2', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'),
  ],
}  # weight: [(file, unicode-range)]

LANG["fonts"] = [("M PLUS Rounded 1c", w, "normal", f, r) for w, fs in MPLUS.items() for f, r in fs]
LANG["glyph_font"] = [f for f, _ in MPLUS[800]]
