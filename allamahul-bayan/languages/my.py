# -*- coding: utf-8 -*-
"""Book 50 - Burmese (Myanmar script: 33 consonants + 11 vowels). Allamahul Bayan Series. REVIEW DRAFT.
Built with engine/generic.py: Burmese children learn the 33 consonants (ဗျည်း) by their traditional names
(ကကြီး, ခခွေး …) and then the vowels (သရ), written on the carrier letter အ."""
from generic import build, letter, section, fontset
from maps import region_map

TALL = set("ခဂငဒပဝ")  # these round letters take the tall aa sign ါ


def K(ch, name, name_tr, sound, word, tr, meaning, pic, means=None, args=None, note=None):
    aa = "ါ" if ch in TALL else "ာ"
    tail = (" Round letters like this one take the <b>tall</b> sign <span class='nt'>ါ</span>, so they are not mixed up with another letter."
            if ch in TALL else "")
    nm = f"Its name <span class='nt'>{name}</span> means “{means}”." if means else ""
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.6">{ch} + {aa} = {ch}{aa} '
            f'<span class="tr" style="font-family:Nunito;font-size:14pt">({name_tr.split("-")[0]}a)</span></div>'
            f'<div class="small">{nm}{tail}</div>')
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, "Burmese phonetics · with the sign ာ", args, note)


def V(ch, sign, sign_name, sign_tr, name_tr, sound, word, tr, meaning, pic, args=None, note=None):
    phon = (f'<div class="nt" style="font-size:18pt;line-height:1.6">◌{sign} <span class="small" style="font-family:Nunito">'
            f'(<span class="nt">{sign_name}</span> <i>{sign_tr}</i>)</span></div>'
            f'<div class="nt" style="font-size:18pt;line-height:1.6">က + ◌{sign} = က{sign}</div>')
    return letter(ch, ch, name_tr, sound, word, tr, meaning, pic, phon, "Burmese phonetics · vowel sign", args, note)


def RARE(ch, word, under=None):
    where = f"it hides under <span class='nt'>{under}</span> in" if under else "find it in"
    return (f"<span class='nt'>{ch}</span> is a rare letter, used in a few words that came from the old Pali language — "
            f"{where} <span class='nt'>{word}</span>!")


CONSONANTS = [
    K("က", "ကကြီး", "ka-jee", "‘k’ as in “skip” (no puff of air)", "ကား", "kaa", "car", "my_car", "big ka"),
    K("ခ", "ခခွေး", "kha-gway", "‘k’ with a puff of air, as in “kite”", "ခဲတံ", "kheh-dan", "pencil", "my_pencil"),
    K("ဂ", "ဂငယ်", "ga-ngeh", "‘g’ as in “go”", "ဂေါ်ဖီ", "gaw-bee", "cabbage", "my_cabbage", "small ga"),
    K("ဃ", "ဃကြီး", "ga-jee", "‘g’ as in “go” — a rare letter", "မိုးမေဃ", "moe-may-ga", "the sky and the clouds", "clouds",
      "big ga", note=RARE("ဃ", "မိုးမေဃ")),
    K("င", "င", "nga", "‘ng’ as in “sing” — Burmese words can start with it!", "ငရုတ်သီး", "nga-youk-thee", "chilli pepper", "my_chilli"),
    K("စ", "စလုံး", "sa-loun", "‘s’ as in “sun” (no puff of air)", "စာအုပ်", "sa-ouk", "book", "book", "round sa",
      args=dict(left="က ခ ဂ", right="ဃ င စ")),
    K("ဆ", "ဆလိမ်", "hsa-lein", "‘s’ with a puff of air", "ဆား", "hsaa", "salt", "salt", "twisted sa", args=dict(label="ဆား")),
    K("ဇ", "ဇကွဲ", "za-gweh", "‘z’ as in “zoo”", "ဇွန်း", "zoon", "spoon", "spoon", "split za"),
    K("ဈ", "ဈမျဉ်းဆွဲ", "za-myin-zweh", "‘z’ as in “zoo”", "ဈေး", "zay", "market", "basket", "za with a line drawn on it"),
    K("ည", "ညကြီး", "nya-jee", "‘ny’ as in “canyon”", "ညနေ", "nya-nay", "evening", "sunrise", "big nya"),
    K("ဋ", "ဋသန်လျင်းချိတ်", "ta-ta-lin-jeik", "‘t’ as in “stop” — a rare letter", "ကုဋေ", "ku-day", "ten million — a very big number!",
      "star", note=RARE("ဋ", "ကုဋေ")),
    K("ဌ", "ဌဝမ်းဘဲ", "hta-wun-beh", "‘t’ with a puff of air — a rare letter", "ဌာန", "hta-na", "office, department", "building",
      note="<span class='nt'>ဌ</span> is a rare letter, used in a few words that came from the old Pali language."),
    K("ဍ", "ဍရင်ကောက်", "da-yin-gauk", "‘d’ as in “day” — a rare letter", "ဘဏ္ဍာ", "ban-daa", "treasure, savings", "jar",
      note=RARE("ဍ", "ဘဏ္ဍာ", "ဏ")),
    K("ဎ", "ဎရေမှုတ်", "da-yay-hmout", "‘d’ as in “day” — the rarest letter of all", "ဎရေမှုတ်", "da-yay-hmout", "the letter’s own name",
      "water", note="<span class='nt'>ဎ</span> is almost never used in words today, so we learn it by its name. Can you find "
                    "<span class='nt'>ရေ</span> <i>yay</i> (water) inside its name?"),
    K("ဏ", "ဏကြီး", "na-jee", "‘n’ as in “net” — almost never at the start of a word", "ဂဏန်း", "ga-nan", "numbers", "one",
      "big na", args=dict(digit="၁"), note="Find <span class='nt'>ဏ</span> in the middle of <span class='nt'>ဂဏန်း</span>!"),
    K("တ", "တဝမ်းပူ", "ta-wun-boo", "‘t’ as in “stop” (no puff of air)", "တောင်", "taung", "mountain", "mountain", "pot-bellied ta"),
    K("ထ", "ထဆင်ထူး", "hta-hsin-htoo", "‘t’ with a puff of air, as in “top”", "ထီး", "htee", "umbrella", "umbrella"),
    K("ဒ", "ဒထွေး", "da-dway", "‘d’ as in “day”", "ဒူးရင်း", "doo-yin", "durian (a spiky fruit)", "my_durian"),
    K("ဓ", "ဓအောက်ခြိုက်", "da-auk-chaik", "‘d’ as in “day”", "ဓာတ်မီးသီး", "dat-mee-thee", "light bulb", "bulb", "da with a dip below"),
    K("န", "နငယ်", "na-ngeh", "‘n’ as in “net”", "နာရီ", "naa-yee", "clock", "clock", "small na"),
    K("ပ", "ပစောက်", "pa-zauk", "‘p’ as in “spin” (no puff of air)", "ပန်း", "pan", "flower", "flower"),
    K("ဖ", "ဖဦးထုပ်", "pha-oo-htouk", "‘p’ with a puff of air, as in “pen”", "ဖရဲသီး", "pha-yeh-thee", "watermelon", "watermelon",
      "pha with a hat"),
    K("ဗ", "ဗထက်ခြိုက်", "ba-htet-chaik", "‘b’ as in “ball”", "ဗူးသီး", "boo-thee", "bottle gourd", "my_gourd", "ba with a dip on top"),
    K("ဘ", "ဘကုန်း", "ba-goun", "‘b’ as in “ball”", "ဘောလုံး", "baw-loun", "ball", "ball"),
    K("မ", "မ", "ma", "‘m’ as in “moon”", "မိုး", "moe", "rain", "raincloud"),
    K("ယ", "ယပက်လက်", "ya-pet-let", "‘y’ as in “yes”", "ယပ်တောင်", "yat-taung", "hand fan", "my_fan", "ya lying on its back"),
    K("ရ", "ရကောက်", "ya-gauk", "‘y’ as in “yes” (in some words ‘r’)", "ရေ", "yay", "water", "water", "bent ya"),
    K("လ", "လ", "la", "‘l’ as in “lamp”", "လ", "la", "moon", "moon",
      note="<span class='nt'>လ</span> is a whole word by itself: it means “moon” (and “month”)."),
    K("ဝ", "ဝ", "wa", "‘w’ as in “water”", "ဝါး", "waa", "bamboo", "my_bamboo"),
    K("သ", "သ", "tha", "‘th’ as in “thin” (often softer, as in “this”)", "သစ်ပင်", "thit-pin", "tree", "tree"),
    K("ဟ", "ဟ", "ha", "‘h’ as in “hat”", "ဟင်းသီးဟင်းရွက်", "hin-thee hin-ywet", "vegetables", "carrot"),
    K("ဠ", "ဠကြီး", "la-jee", "‘l’ as in “lamp” — a rare letter", "ကီဠာ", "kee-laa", "sports and games (like flying a kite!)", "kite",
      "big la", note=RARE("ဠ", "ကီဠာ")),
    K("အ", "အ", "a", "a little catch in the throat, then ‘a’ — like the start of “uh-oh”", "အလံ", "a-lan", "flag", "flag",
      note="<span class='nt'>အ</span> also carries the vowel signs at the start of a word: <span class='nt'>အာ အိ အီ အု</span>…"),
]

VOWELS = [
    V("အာ", "ာ", "ရေးချ", "yay-cha", "aa", "‘aa’ as in “father”", "အာလူး", "aa-loo", "potato", "potato"),
    V("အိ", "ိ", "လုံးကြီးတင်", "loun-jee-tin", "i", "a short ‘i’, between “sit” and “say”", "အိမ်", "ein", "house", "house"),
    V("အီ", "ီ", "လုံးကြီးတင်ဆန်ခတ်", "loun-jee-tin hsan-khat", "ee", "‘ee’ as in “see”", "အီကြာကွေး", "ee-jaa-kway",
      "fried dough sticks", "my_youtiao"),
    V("အု", "ု", "တစ်ချောင်းငင်", "ta-chaung-ngin", "u", "a short ‘u’ as in “put”", "အုန်းသီး", "oun-thee", "coconut", "coconut"),
    V("အူ", "ူ", "နှစ်ချောင်းငင်", "hna-chaung-ngin", "oo", "‘oo’ as in “moon”", "ဦးထုပ်", "oo-htouk", "hat", "my_hat",
      note="At the start of a word this sound is usually written with its own letter, <span class='nt'>ဦ</span>, as in "
           "<span class='nt'>ဦးထုပ်</span>."),
    V("အေ", "ေ", "သဝေထိုး", "tha-way-htoe", "ay", "‘ay’ as in “day”", "အေး", "ay", "cold", "ice",
      note="The sign <span class='nt'>ေ</span> is written <b>before</b> the letter, but said <b>after</b> it!"),
    V("အဲ", "ဲ", "နောက်ပစ်", "nauk-pyit", "eh", "‘e’ as in “bed”", "ပဲ", "peh", "beans", "my_peas",
      note="Find the sign <span class='nt'>ဲ</span> on top of <span class='nt'>ပ</span> in <span class='nt'>ပဲ</span>."),
    V("အော", "ော", "သဝေထိုး ရေးချ", "tha-way-htoe yay-cha", "aw", "‘aw’ as in “saw”, said short and high", "ဘောပင်", "baw-pin",
      "pen", "pen", note="Find <span class='nt'>ော</span> around <span class='nt'>ဘ</span> in <span class='nt'>ဘောပင်</span>."),
    V("အော်", "ော်", "သဝေထိုး ရေးချ ရှေ့ထိုး", "tha-way-htoe yay-cha shay-htoe", "aw", "‘aw’ as in “saw”, said low and long", "ကော်ဖီ",
      "kaw-fee", "coffee", "teacup"),
    V("အံ", "ံ", "သေးသေးတင်", "thay-thay-tin", "an", "‘an’ — a short ‘a’ that ends in the nose", "ကြံ", "jan", "sugarcane", "sugarcane",
      note="Find the little circle <span class='nt'>ံ</span> on top of <span class='nt'>ကြံ</span>."),
    V("အို", "ို", "လုံးကြီးတင် တစ်ချောင်းငင်", "loun-jee-tin ta-chaung-ngin", "o", "‘o’ as in “go”", "အိုး", "oh", "cooking pot", "pot"),
]

LANG = build(dict(
    code="my", folder="book-50-burmese", series_no=50, isbn="", draft=True,
    name="Burmese", native="မြန်မာ", native_tr="myan-maa", name_word="နာမည်", write_word="ရေးပါ",
    title_native="ကျွန်ုပ်၏ ပထမဆုံး မြန်မာအက္ခရာ", title_letters="ကခဂဃငစ", belongs_native="ဤစာအုပ်ပိုင်ရှင်",
    belongs_pic="my_bamboo", alphabet_native="အက္ခရာ", numbers_native="ဂဏန်း", numbers_tr="ga-nan",
    phrases_native="ပထမဆုံး စကားလုံးများ",
    fonts=fontset("Noto Sans Myanmar", "noto-sans-myanmar-myanmar", "Padauk", "padauk-myanmar"),
    disp_family="Noto Sans Myanmar", text_family="Padauk",
    glyph_font=["noto-sans-myanmar-myanmar-800-normal.woff2"],
    font_credit="Noto Sans Myanmar, Padauk",
    phon_feature="each letter’s traditional Burmese name (<i>ka-jee, kha-gway, ga-ngeh</i>…) and how it joins the vowel signs",
    sections=[
        section(CONSONANTS, label="CONSONANT", chip="PART 1", title="The Consonants", native="ဗျည်း",
                native_tr="byee — the 33 consonants", chart_title="consonants", chart_cols=7, warmup_cols=6,
                warmup_title="the consonants",
                intro_html="""<p>Burmese children first learn the <b>33 consonants</b>, in rows of five, in the same order as this book:
<span class="nt">က ခ ဂ ဃ င</span> <i>ka, kha, ga, ga, nga</i>…</p>
<div class="box" style="margin:0.1in 0"><h3>Every letter has a name</h3>Some letters sound the same, so each one has a
<b>name</b> that tells them apart: <span class="nt">ကကြီး</span> <i>ka-jee</i> “big ka”, <span class="nt">ဂငယ်</span> <i>ga-ngeh</i>
“small ga”, <span class="nt">စလုံး</span> <i>sa-loun</i> “round sa”. Say the names as you color!</div>
<div class="box" style="margin:0.1in 0"><h3>The hidden vowel</h3>Every consonant carries a short <b>‘a’</b>: <span class="nt">က</span> is
<i>ka</i>, <span class="nt">မ</span> is <i>ma</i>. Add a vowel sign to change it:
<div class="nt" style="font-size:20pt;text-align:center;margin-top:4px">က + ာ = ကာ <span class="tr" style="font-family:Nunito;font-size:13pt">(kaa)</span></div></div>
<div class="box"><h3>Round letters</h3>Long ago, Burmese was written on dried <b>palm leaves</b> with a sharp metal pen. Long straight lines
would split the leaf, so the letters grew round — almost every letter is built from <b>circles</b>!</div>"""),
        section(VOWELS, label="VOWEL", chip="PART 2", title="The Vowels", native="သရ",
                native_tr="tha-ra — the vowels", chart_title="vowels", chart_cols=6, warmup_cols=4,
                warmup_title="the vowels",
                intro_html="""<p>A vowel is written as a small <b>sign</b> around a consonant: above it, below it, before it or after it.
To show a vowel on its own, Burmese writes it on the letter <span class="nt">အ</span>, which keeps the sign company:
<span class="nt">အ + ာ = အာ</span> <i>aa</i>. This book teaches the <b>11 main vowel signs</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>Before, after, above, below</h3>
<span class="nt" style="font-size:16pt">ေ</span> is written <b>before</b> the letter but said after it: <span class="nt">က + ေ = ကေ</span> <i>kay</i>.
<span class="nt" style="font-size:16pt">ိ ီ ဲ ံ</span> sit <b>on top</b>, <span class="nt" style="font-size:16pt">ု ူ</span> hang <b>below</b>,
and <span class="nt" style="font-size:16pt">ာ</span> comes <b>after</b>.</div>
<div class="box"><h3>Burmese has tones</h3>The same vowel can be said high, low or short, and that can change the meaning.
Two small marks help: <span class="nt" style="font-size:16pt">း</span> (a high, long sound) and <span class="nt" style="font-size:16pt">့</span>
(a short, creaky sound). Listen to a Burmese speaker and copy the tune!</div>"""),
    ],
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ee</i> as in “see”, <i>oo</i> as in “moon”.",
        "<b>h after a letter</b> (<i>kh, hs, ht, ph</i>) means “add a puff of breath”. Without the h (<i>k, s, t, p</i>) say it "
        "with <b>no</b> puff, as in “skip”, “stop”, “spin”. <i>ht</i> is a ‘t’ with a puff — never the English “th”.",
        "<b>j</b> in words like <i>ka-jee</i> and <i>jan</i> is how the letters <span class='nt'>ကျ ကြ</span> sound: like ‘j’ or ‘ch’.",
        "<b>Tones:</b> the English letters show the sounds, not the tunes. The tones are best learned by listening."],
    phon_explain="The box marked <i>Burmese phonetics</i> shows the letter joined to the vowel sign <span class='nt'>ာ</span> "
                 "(<span class='nt'>က + ာ = ကာ</span> <i>kaa</i>) and what its traditional name means. On the vowel pages it "
                 "shows the vowel sign and its Burmese name.",
    standard="the standard Burmese of Yangon and Mandalay",
    hello=[
        ("Who speaks it?", "More than <b>40 million people</b> speak Burmese: about 33 million as their first language, and "
                           "millions more as a second language.<sup>³</sup>"),
        ("Where?", "In <b>Myanmar</b> (also called Burma), along the great <b>Ayeyarwady River</b>, and by Burmese families "
                   "around the world."),
        ("How is it written?", "In the <b>Myanmar script</b>, from <b>left to right</b>. Spaces go between phrases, "
                               "not between every word."),
        ("How many letters?", "This book teaches <b>44</b>: the <b>33 consonants</b> and the <b>11 main vowel signs</b>, "
                              "each shown on the letter <span class='nt'>အ</span>."),
        ("Round letters", "Burmese letters are made of <b>circles</b> and curves, because they were once scratched onto "
                          "<b>palm leaves</b>, where straight lines would tear."),
        ("Did you know?", "The Ayeyarwady River runs the whole length of Myanmar, more than <b>2,000 km</b>, from the "
                          "mountains in the north to the sea."),
    ],
    hello_pics=[("my_bamboo", {}), ("coconut", {}), ("my_fan", {})],
    map=region_map(frame=[[87.5, 9.0], [105.5, 27.0]],
                   points=dict(yangon=[96.16, 16.84], mandalay=[96.08, 21.97], naypyitaw=[96.13, 19.75],
                               mawlamyine=[97.63, 16.49], sittwe=[92.90, 20.15]),
                   area=(95.9, 20.3, 170, 300), area_rot=8,
                   cities=[("yangon", "Yangon", -14, 26, "end", False), ("mandalay", "Mandalay", 14, -8, "start", False),
                           ("naypyitaw", "Nay Pyi Taw", 16, 8, "start", True), ("mawlamyine", "Mawlamyine", 14, 14, "start", False),
                           ("sittwe", "Sittwe", -14, 8, "end", False)],
                   label="MYANMAR", label_at=[96.0, 24.4], marker=[96.0, 20.0],
                   caption="The circle shows Myanmar on the world map.",
                   legend="<b>Color it:</b> the middle of Myanmar, where most Burmese speakers live (inside the dashed line), "
                          "<b>yellow</b> · the rest of the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Mandalay, "
                          "Nay Pyi Taw ★ and Yangon. Draw the long <b>Ayeyarwady River</b> flowing south to the sea!",
                   seas=[("Bay of Bengal", 90.5, 15.0), ("Andaman Sea", 96.3, 12.0)]),
    digits=[("၀", "သုည", "thoun-nya", "zero"), ("၁", "တစ်", "tit", "one"), ("၂", "နှစ်", "hnit", "two"), ("၃", "သုံး", "thoun", "three"),
            ("၄", "လေး", "lay", "four"), ("၅", "ငါး", "ngaa", "five"), ("၆", "ခြောက်", "chauk", "six"), ("၇", "ခုနစ်", "khun-nit", "seven"),
            ("၈", "ရှစ်", "shit", "eight"), ("၉", "ကိုး", "koe", "nine")],
    phrases=[("အဿလာမု အလိုင်ကုမ်", "as-sa-laa-mu a-lai-kum", "Peace be upon you (the Muslim greeting)"),
             ("ဝ အလိုင်ကုမ် အဿလာမ်", "wa a-lai-kum as-sa-laam", "And upon you be peace (the reply)"),
             ("ကျွန်တော့် နာမည် … ပါ", "ja-naw na-meh … ba", "My name is … (a girl says: ကျွန်မ ja-ma)"),
             ("ကျေးဇူးတင်ပါတယ်", "jay-zoo tin-ba-deh", "Thank you"),
             ("ဂျဇာကလ္လာဟု ခိုင်ရန်", "ja-zaa-kal-laa-hu khai-ran", "May Allah reward you with good"),
             ("အမေ · အဖေ", "a-may · a-phay", "Mother · Father"),
             ("အစ်ကို · အစ်မ", "a-ko · a-ma", "Brother · Sister (older)"),
             ("ဟုတ်ကဲ့ · မဟုတ်ဘူး", "hout-keh · ma-hout-boo", "Yes · No"),
             ("ကျွန်တော် မြန်မာစာ သင်နေပါတယ်!", "ja-naw myan-maa-zaa thin-nay-ba-deh!", "I am learning Burmese! (a girl says: ကျွန်မ ja-ma)")],
    cheer=("မာရှာအလ္လာဟ်! တော်လိုက်တာ!", "maa-shaa-al-laa! taw-lite-taa!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="က ခ ဂ", right="ဃ င စ"),
    review_note="Burmese is a REVIEW DRAFT. Please check: the traditional letter names and their English glosses (big ka, round sa, "
                "pot-bellied ta, pha with a hat…); the words for the rare letters ဃ (မိုးမေဃ), ဋ (ကုဋေ), ဍ (ဘဏ္ဍာ), ဎ (shown by "
                "its own name) and ဠ (ကီဠာ); the Burmese names of the vowel signs; the simplified transliterations (tones are "
                "not marked); and the Burmese spellings of the Arabic phrases (Assalamu alaikum, Jazakallahu khairan, Mashallah) "
                "as Myanmar Muslims write them.",
    tiles="ကခဂငစမ", cover_pics=["my_bamboo", "flower", "coconut", "umbrella"], title_size=48,
    speakers_blurb="Burmese is the main language of Myanmar, spoken by more than 40 million people.",
    sample_words=[("ပန်း", "pan", "flower"), ("ထီး", "htee", "umbrella"), ("တောင်", "taung", "mountain")],
    keywords=["burmese alphabet book for kids", "learn myanmar language for children", "myanmar script coloring book",
              "burmese letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "burmese heritage language gift"],
))
