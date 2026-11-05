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
    map=region_map(frame=[[128.0, 29.8], [146.4, 46.0]],
                   points=dict(tokyo=[139.69, 35.69], osaka=[135.50, 34.69], sapporo=[141.35, 43.06],
                               fukuoka=[130.40, 33.59]),
                   area=(137.6, 37.6, 520, 170), area_rot=-42,
                   cities=[("tokyo", "Tokyo", 14, 8, "start", False), ("osaka", "Osaka", -14, 26, "end", False),
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
MPLUS = {400: [], 700: [], 800: []}  # weight: [(file, unicode-range)]

LANG["fonts"] = [("M PLUS Rounded 1c", w, "normal", f, r) for w, fs in MPLUS.items() for f, r in fs]
LANG["glyph_font"] = [f for f, _ in MPLUS[800]]
