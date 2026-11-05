# -*- coding: utf-8 -*-
"""Book 26 - Dzongkha (Tibetan script as written in Bhutan: 30 consonants + 4 vowel signs).
Allamahul Bayan Series. REVIEW DRAFT. Words avoid Buddhist religious items and terms."""
from generic import build, letter, section, fontset
from maps import region_map

# letter, romanization, tone, sound guide
CONS = [("ཀ", "ka", "high", "‘k’ as in “skip” — no puff of air"),
        ("ཁ", "kha", "high", "‘k’ with a puff of air, as in “kite”"),
        ("ག", "ga", "low", "‘g’ as in “go”, said low and soft"),
        ("ང", "nga", "low", "‘ng’ as in “sing” — but at the start!"),
        ("ཅ", "ca", "high", "‘ch’ as in “itchy” — no puff of air"),
        ("ཆ", "cha", "high", "‘ch’ with a puff of air, as in “cheese” (written chh)"),
        ("ཇ", "ja", "low", "‘j’ as in “jam”, said low"),
        ("ཉ", "nya", "low", "‘ny’ as in “canyon”"),
        ("ཏ", "ta", "high", "‘t’ as in “stop” — no puff of air"),
        ("ཐ", "tha", "high", "‘t’ with a puff of air, as in “top”"),
        ("ད", "da", "low", "‘d’ as in “dot”, said low"),
        ("ན", "na", "low", "‘n’ as in “net”"),
        ("པ", "pa", "high", "‘p’ as in “spin” — no puff of air"),
        ("ཕ", "pha", "high", "‘p’ with a puff of air, as in “pin”"),
        ("བ", "ba", "low", "‘b’ as in “bat”, said low"),
        ("མ", "ma", "low", "‘m’ as in “moon”"),
        ("ཙ", "tsa", "high", "‘ts’ as in “cats”"),
        ("ཚ", "tsha", "high", "‘ts’ with a puff of air"),
        ("ཛ", "dza", "low", "‘dz’ as in “adze”, said low"),
        ("ཝ", "wa", "low", "‘w’ as in “wet”"),
        ("ཞ", "zha", "low", "‘zh’ like the ‘s’ in “measure”"),
        ("ཟ", "za", "low", "‘z’ as in “zoo”"),
        ("འ", "'a", "low", "a soft, low ‘a’ with no consonant sound"),
        ("ཡ", "ya", "low", "‘y’ as in “yes”"),
        ("ར", "ra", "low", "a light, tapped ‘r’"),
        ("ལ", "la", "low", "‘l’ as in “lamp”"),
        ("ཤ", "sha", "high", "‘sh’ as in “shop”"),
        ("ས", "sa", "high", "‘s’ as in “sun”"),
        ("ཧ", "ha", "high", "‘h’ as in “hat”"),
        ("ཨ", "a", "high", "a plain ‘a’ as in “father”, said high")]
INFO = {c: (r, t, s) for c, r, t, s in CONS}
VSIGN = [("ི", "i"), ("ུ", "u"), ("ེ", "e"), ("ོ", "o")]

def base(r):
    return r[:-1] if r.endswith("a") else r

def phon_cons(c):
    r, tone, _ = INFO[c]
    row = [(c, r)] + [(c + s, base(r) + v) for s, v in VSIGN]
    cells = "".join(f'<div style="text-align:center"><div class="nt" style="font-size:21pt;line-height:1.7">{t}</div>'
                    f'<div class="small" style="line-height:1">{tr}</div></div>' for t, tr in row)
    tone_txt = ("<b>High tone:</b> say it with a higher, clear voice." if tone == "high"
                else "<b>Low tone:</b> say it with a lower, softer voice.")
    return f'<div style="display:flex;justify-content:space-around">{cells}</div><div class="small" style="margin-top:6px">{tone_txt}</div>'

PH_C = "With the 4 vowels · tone"

def C(c, word, tr, meaning, pic, args=None, note=None):
    r, tone, snd = INFO[c]
    if pic is None:
        pic, args = "dz_slate", dict(text=word)
    return letter(c, c, r, snd, word, tr, meaning, pic, phon_cons(c), PH_C, args, note)

SILENT = "The little {x} is silent: {w} says <i>{tr}</i>, so {c} is the letter you hear."
CONSONANTS = [
    C("ཀ", "ཀུ་ཤུ", "ku-shu", "apple", "apple"),
    C("ཁ", "ཁྱིམ", "chhim", "house, home", "house",
      note="Here ཁ has a little ya ( ྱ ) tucked under it: ཁྱ says ‘chh’."),
    C("ག", "སྒོ", "go", "door", "door", note=SILENT.format(x="ས on top", w="སྒོ", tr="go", c="ག")),
    C("ང", "རྔ", "nga", "drum", "dz_drum", note=SILENT.format(x="ར on top", w="རྔ", tr="nga", c="ང")),
    C("ཅ", "ཅོག་ཙེ", "chog-tse", "table", "dz_table"),
    C("ཆ", "ཆུ", "chhu", "water", "water"),
    C("ཇ", "ཇ", "ja", "tea", "teacup", note="ཇ on its own is a whole word: <i>ja</i>, tea!"),
    C("ཉ", "ཉིམ", "nyim", "sun", "sun"),
    C("ཏ", "ཏོ", "to", "rice, a meal", "rice"),
    C("ཐ", "ཐབ", "thap", "stove, cooking fire", "dz_stove"),
    C("ད", "རྡོ", "do", "stone", "dz_stone", note=SILENT.format(x="ར on top", w="རྡོ", tr="do", c="ད")),
    C("ན", "ནམ་མཁའ", "nam-kha", "sky", "clouds"),
    C("པ", "པར", "par", "picture, photo", "dz_frame"),
    C("ཕ", "ཕོབ", "phob", "bowl, cup", "dz_bowl"),
    C("བ", "བང་ཆུང", "bang-chung", "bamboo basket", "basket"),
    C("མ", "མེ་ཏོག", "me-tog", "flower", "flower"),
    C("ཙ", "བཙོང", "tsong", "onion", "onion", note=SILENT.format(x="བ in front", w="བཙོང", tr="tsong", c="ཙ")),
    C("ཚ", "ཚྭ", "tsha", "salt", "salt", dict(label="ཚྭ"),
      note="The little hook under ཚ ( ྭ ) does not change the sound: ཚྭ says <i>tsha</i>."),
    C("ཛ", "རྫོང", "dzong", "fortress — a big castle building", "dz_dzong",
      note="ཛ is rare on its own; it usually wears a silent ར hat, as in རྫོང. The word Dzongkha means “the language of the dzong”."),
    C("ཝ", "ཝ", "wa", "sound practice — say it three times", "dz_slate", dict(text="ཝ"),
      note="<b>Sound-practice page.</b> ཝ is a rare letter, used mostly in borrowed words and names, so there is no picture word here."),
    C("ཞ", "ཞིང", "zhing", "field", "paddy"),
    C("ཟ", "ཟམ", "zam", "bridge", "dz_bridge"),
    C("འ", "འོམ", "om", "milk", "ewer"),
    C("ཡ", "ཡི་གུ", "yi-gu", "letter (to post)", "envelope"),
    C("ར", "རས", "rä", "cloth", "scarf"),
    C("ལ", "ལོ་མ", "lo-ma", "leaf", "dz_leaf"),
    C("ཤ", "ཤིང", "shing", "tree, wood", "tree"),
    C("ས", "ས", "sa", "earth, land", "globe", note="ས on its own is a whole word: <i>sa</i>, the earth or the ground."),
    C("ཧ", "ཧ་ཅང", "ha-chang", "very, very much", None,
      note="Few everyday words start with ཧ. Say it with a smile: <i>ha-chang</i> means “very”!"),
    C("ཨ", "ཨེ་མ", "e-ma", "chilli", "dz_chilli",
      note="Bhutan’s favourite dish is <i>ema datshi</i>: chillies cooked with cheese!"),
]

# vowel signs: sign, name, name romanized, sound, where it sits, word, tr, meaning, pic
def phon_vow(sign, v):
    row = [("ཀ", "k"), ("ཁ", "kh"), ("ག", "g"), ("ང", "ng"), ("ཅ", "c")]
    cells = "".join(f'<div style="text-align:center"><div class="nt" style="font-size:21pt;line-height:1.7">{c}{sign}</div>'
                    f'<div class="small" style="line-height:1">{r}{v}</div></div>' for c, r in row)
    return f'<div style="display:flex;justify-content:space-around">{cells}</div>'

def V(sign, v, name, name_tr, sound, where, word, tr, meaning, pic):
    return letter("ཨ" + sign, name, f"{name_tr} ({v})", sound, word, tr, meaning, pic,
                  phon_vow(sign, v) + f'<div class="small" style="margin-top:6px">{where}</div>', "On other letters", None,
                  f"Here the sign sits on ཨ, the letter that carries a vowel alone.")

VOWELS = [
    V("ི", "i", "གི་གུ", "gi-gu", "‘ee’ as in “see”", "<b>gigu</b> sits <b>on top</b> of the letter, like a little hook.",
      "རི", "ri", "hill, mountain", "mountain"),
    V("ུ", "u", "ཞབས་ཀྱུ", "zhab-kyu", "‘oo’ as in “moon”", "<b>zhabkyu</b> hangs <b>under</b> the letter, like a little foot.",
      "ཆུ་ཚོད", "chhu-tshö", "clock", "clock"),
    V("ེ", "e", "འགྲེང་བུ", "dreng-bu", "‘e’ as in “bed”", "<b>drengbu</b> sits <b>on top</b>, leaning like a little flag.",
      "མེ", "me", "fire", "dz_fire"),
    V("ོ", "o", "ན་རོ", "na-ro", "‘o’ as in “go”", "<b>naro</b> sits <b>on top</b>, curling both ways.",
      "ཤིང་ཏོག", "shing-tog", "fruit", "pear"),
]

def grid(rows, size=24):
    return "".join('<div style="display:flex;gap:0.1in;margin:0.04in 0">'
                   + "".join(f'<div class="box" style="text-align:center;padding:0 8px;min-width:0.7in"><div class="ntd" style="font-size:{size}pt;line-height:1.6">{c}</div>'
                             f'<div class="small tr">{INFO[c][0]}</div></div>' for c in r) + "</div>" for r in rows)

LANG = build(dict(
    code="dz", folder="book-26-dzongkha", series_no=26, isbn="", draft=True,
    name="Dzongkha", native="རྫོང་ཁ", native_tr="dzong-kha", name_word="མིང", write_word="འབྲི",
    title_native="རྫོང་ཁའི་ཀ་ཁ།", title_letters="ཀཁགང", belongs_native="དེབ་འདི་ … གི་ཨིན།",
    belongs_pic="flower", alphabet_native="ཀ་ཁ", numbers_native="ཨང་གྲངས", numbers_tr="ang-drang",
    phrases_native="ཀུ་ཟུ་ཟང་པོ་ལ།",
    fonts=fontset("Noto Serif Tibetan", "noto-serif-tibetan-tibetan", "Jomolhari", "jomolhari-tibetan"),
    disp_family="Noto Serif Tibetan", text_family="Jomolhari",
    glyph_font=["noto-serif-tibetan-tibetan-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Serif Tibetan, Jomolhari (by Christopher Fynn) and Baloo 2",
    phon_feature="each letter read with the four vowel signs (ཀ ཀི ཀུ ཀེ ཀོ) and its high or low tone",
    sections=[
        section(CONSONANTS, label="LETTER", chip="THE CONSONANTS", title="The Consonants", native="གསལ་བྱེད",
                native_tr="sel-je — the 30 letters", chart_title="consonants", chart_cols=4, warmup_cols=6,
                warmup_title="the consonants",
                intro_html=f"""<p>Dzongkha has <b>30 consonants</b>. Children learn them in rows of four, the same way they are
written on the classroom wall in Bhutan: <i>ka, kha, ga, nga…</i></p>{grid([[c for c, *_ in CONS[i:i + 4]] for i in range(0, 8, 4)], 24)}
<div class="box" style="margin:0.1in 0"><h3>Every letter says “a”</h3>A letter on its own already has the vowel <b>a</b> in it:
<b>ཀ</b> is <i>ka</i>, <b>མ</b> is <i>ma</i>. To make another vowel, add a vowel sign (you will meet them later in the book).</div>
<div class="box" style="margin:0.1in 0"><h3>Hanging from a line</h3>Tibetan-script letters hang from an invisible line at the top,
and a small dot <b>་</b> (<i>tsheg</i>) comes after every syllable: <span class="nt" style="font-size:16pt">ཀུ་ཤུ</span> = ku · shu.</div>
<div class="box"><h3>High and low</h3>Some letters are said with a <b>high</b> voice and some with a <b>low</b> voice. Each letter page tells you which.</div>"""),
        section(VOWELS, label="VOWEL", chip="THE VOWEL SIGNS", title="The Vowel Signs", native="དབྱངས",
                native_tr="yang — the 4 vowel signs", chart_title="vowel signs", chart_cols=4, warmup_cols=4,
                warmup_title="the vowel signs",
                intro_html="""<p>Dzongkha has <b>four vowel signs</b>. They are not letters on their own: they sit <b>on top of</b>
or <b>under</b> a letter and change its “a” into <i>i, u, e</i> or <i>o</i>.</p>
<div style="display:flex;gap:0.12in;margin:0.12in 0">""" + "".join(
                    f'<div class="box" style="text-align:center;flex:1"><div class="ntd" style="font-size:30pt;line-height:1.8">ཀ{s}</div><div class="tr">k{v}</div></div>'
                    for s, v in VSIGN) + """</div>
<div class="box" style="margin:0.1in 0"><h3>The vowel carrier ཨ</h3>To write a vowel all alone, put the sign on <b>ཨ</b> (a):
<span class="nt" style="font-size:18pt">ཨི ཨུ ཨེ ཨོ</span> = i, u, e, o.</div>
<div class="box"><h3>Three on top, one below</h3><i>gigu</i>, <i>drengbu</i> and <i>naro</i> sit on top; <i>zhabkyu</i> hangs underneath.</div>"""),
    ],
    sound_notes=[
        "An <b>h</b> after a consonant (<b>kh, chh, th, ph, tsh</b>) means a little puff of air. Without the h, say it with no puff: "
        "<b>k</b> as in “skip”, not “kite”.",
        "<b>c</b> is ‘ch’ with no puff of air; <b>chh</b> is ‘ch’ with a puff.",
        "<b>ä</b> and <b>ö</b> are like the vowels in German: <i>rä</i> rhymes with “bed” said long; <i>ö</i> is ‘e’ said with round lips.",
        "Dzongkha has <b>high</b> and <b>low</b> tones. Each letter page says which one the letter has."],
    phon_explain="The box marked <i>With the 4 vowels · tone</i> shows the letter with each vowel sign (ཀ ཀི ཀུ ཀེ ཀོ = ka ki ku ke ko), "
                 "the way children in Bhutan practise it, and says whether the letter has a high or a low tone.",
    standard="the Dzongkha spoken in western Bhutan (Thimphu and Punakha)",
    hello=[
        ("Who speaks it?", "Dzongkha is the <b>national language of Bhutan</b>. About <b>170,000 people</b> speak it as their first "
                           "language, and many more Bhutanese learn it at school.<sup>³</sup>"),
        ("Where?", "In the <b>Kingdom of Bhutan</b>, high in the <b>eastern Himalaya mountains</b>, with snowy peaks, forests and "
                   "deep green valleys."),
        ("How is it written?", "In the <b>Tibetan script</b>, written the Bhutanese way, from <b>left to right</b>, with a small dot "
                               "<span class=\"nt\">་</span> after every syllable."),
        ("How many letters?", "<b>30 consonants</b> and <b>4 vowel signs</b> — <b>34</b> in this book."),
        ("What does the name mean?", "<i>Dzongkha</i> means “the language of the <b>dzong</b>” — the big white fortress buildings "
                                     "found in Bhutan’s valleys."),
        ("Did you know?", "Bhutan’s favourite food is <i>ema datshi</i>: chillies with cheese. <i>Ema</i> "
                          "<span class=\"nt\">ཨེ་མ</span> means chilli — you will find it on the page for ཨ!"),
    ],
    hello_pics=[("dz_dzong", {}), ("mountain", {}), ("dz_chilli", {})],
    map=region_map(frame=[[84.0, 20.5], [96.0, 32.0]],
                   points=dict(thimphu=[89.64, 27.47], punakha=[89.86, 27.58], paro=[89.41, 27.43], trashigang=[91.55, 27.33]),
                   area=(90.45, 27.4, 150, 80),
                   cities=[("thimphu", "Thimphu", -16, 30, "end", True), ("punakha", "Punakha", 10, -14, "start", False),
                           ("trashigang", "Trashigang", 12, 28, "start", False)],
                   label="BHUTAN", label_at=[90.45, 28.75], marker=[90.45, 27.4],
                   caption="The circle shows Bhutan on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the sea <b>blue</b> · the high mountains <b>white</b>. <b>Find it:</b> "
                          "Dzongkha is spoken across Bhutan (inside the dashed line), in towns like Thimphu (the capital), Punakha and Trashigang.",
                   seas=[("Bay of Bengal", 89.0, 21.2)]),
    digits=[("༠", "ཀླད་ཀོར", "lä-kor", "zero"), ("༡", "གཅིག", "chi", "one"), ("༢", "གཉིས", "nyi", "two"),
            ("༣", "གསུམ", "sum", "three"), ("༤", "བཞི", "zhi", "four"), ("༥", "ལྔ", "nga", "five"),
            ("༦", "དྲུག", "druk", "six"), ("༧", "བདུན", "dün", "seven"), ("༨", "བརྒྱད", "gä", "eight"),
            ("༩", "དགུ", "gu", "nine")],
    phrases=[("ཨས་ས་ལཱ་མུ་ཨ་ལཻ་ཀུམ།", "as-sa-LAA-mu a-LAI-kum", "Peace be upon you (the Muslim greeting)"),
             ("ཝ་ཨ་ལཻ་ཀུམ་ཨས་ས་ལཱམ།", "wa a-LAI-kum as-sa-LAAM", "And upon you be peace (the reply)"),
             ("ཀུ་ཟུ་ཟང་པོ་ལ།", "ku-zu zang-po la", "Hello!"),
             ("ངའི་མིང་ … ཨིན།", "ngä ming … in", "My name is …"),
             ("བཀའ་དྲིན་ཆེ་ལ།", "ka-drin chhe la", "Thank you"),
             ("ཇ་ཟཱ་ཀལ་ལཱ་ཧུ་ཁཻ་རཱན།", "ja-ZAA-kal-laa-hu KHAI-raan", "Jazakallahu khairan — May Allah reward you with good"),
             ("ཨ་མ · ཨ་པ", "a-ma · a-pa", "Mother · Father"),
             ("ཨ་ཏ · ཨ་ཞེམ", "a-ta · a-zhem", "Big brother · Big sister"),
             ("ཨིན། · མེན།", "in · men", "Yes (it is) · No (it is not)"),
             ("ང་རྫོང་ཁ་ལྷབ་དོ།", "nga dzong-kha lhab do", "I am learning Dzongkha!")],
    cheer=("མ་ཤཱ་ཨལ་ལཱ། ལེགས་ཤོམ་ཨིན།", "MAA-shaa-al-laa! leg-shom in!", "Mashallah! Well done — that is good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); the Dzongkha alphabet as taught by the "
                 "<b>Dzongkha Development Commission</b> of Bhutan.",
    book_pic=dict(left="ཀ ཁ ག", right="ང ཅ ཆ"),
    review_note=("Drafted without a Dzongkha speaker; please check every word, spelling and transliteration against DDC spelling. "
                 "Less certain words: ཁྱིམ (house), ཅོག་ཙེ (table), ཏོ (rice/meal), ཐབ (stove), པར (picture), ཕོབ (bowl), "
                 "བཙོང (onion), རས (cloth), ཡི་གུ (letter), ཤིང་ཏོག (fruit), ཆུ་ཚོད (clock), ཧ་ཅང (very), ཨ་ཏ / ཨ་ཞེམ (big brother / sister), "
                 "the label དེབ་འདི་ … གི་ཨིན། (this book belongs to) and the title རྫོང་ཁའི་ཀ་ཁ།. Several words begin with a silent "
                 "prefix or superscript (སྒོ, རྔ, རྡོ, བཙོང, རྫོང, ཁྱིམ) — these have notes; a reviewer may prefer simpler words. "
                 "ཝ has a sound-practice page with no word. Check the tone (high/low) given for each letter. The Arabic phrases "
                 "(Assalamu alaikum, Jazakallahu khairan, Mashallah) are sound-spellings in Tibetan script and should be approved "
                 "by a Bhutanese Muslim reader. The picture for རྔ is a plain drum and for རྫོང a plain fortress building, with no "
                 "religious details."),
    extra_css=("span.nt{font-size:1.6em;line-height:1} .lp-word .lbl{line-height:2.1} "
               ".box > .ntd{line-height:1.65 !important}"),
    tiles="ཀཁགངཅཆ", cover_pics=["dz_chilli", "apple", "flower", "mountain"], title_size=48,
    speakers_blurb="Dzongkha is the national language of the Kingdom of Bhutan, high in the Himalaya mountains.",
    sample_words=[("ཀུ་ཤུ", "ku-shu", "apple"), ("མེ་ཏོག", "me-tog", "flower"), ("ཨེ་མ", "e-ma", "chilli")],
    keywords=["dzongkha alphabet book for kids", "learn dzongkha for children", "bhutan language coloring book",
              "tibetan script letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "dzongkha ka kha for beginners"],
))
