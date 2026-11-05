# -*- coding: utf-8 -*-
"""Book 48 - Lao (Lao script: 27 consonants + 19 main vowel signs). Allamahul Bayan Series. REVIEW DRAFT.
Built with the generic builder: Part 1 = the 27 consonants in the traditional order (ກ ໄກ່ ... ຮ ເຮືອນ),
Part 2 = the main vowel signs, shown on the silent carrier ອ.
House rule: the traditional name word is the picture word only when it is an object, plant or nature;
for animal / person / body names a different object word with the same letter is used, with a note.
Some pictures come from engine/pics/th.py (th_ keys) - same author, shared on purpose."""
from generic import build, letter, section, fontset
from maps import region_map

NT = lambda t: f"<span class='nt'>{t}</span>"
CLASS = {"M": "middle-class", "H": "high-class", "L": "low-class"}
NOT_DRAWN = {"animal": "We draw no animals", "person": "We draw no people", "body": "We draw no faces or bodies"}


def CN(ch, name, name_tr, cls, init, sound, final, word, tr, meaning, pic, own=False, why=None, name_mean=None,
       note=None, args=None):
    fin = (f"at the end of a word it says <b>{final}</b>" if final else "it is not used at the end of a word")
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">{ch} + າ = {ch}າ</div>'
            f'<div class="small"><i>{init}aa</i> · a <b>{CLASS[cls]}</b> letter · {fin}</div>')
    if note is None:
        if own:
            note = f"This is the letter’s own name word: {NT(name)}!"
        elif why:
            note = (f"Its name word {NT(name.split(' ', 1)[1])} means “{name_mean}”. {NOT_DRAWN[why]}, "
                    f"so our word is {NT(word)}.")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, "Lao phonetics · spelling & letter class",
                  args, note)


ASP = "with a puff of air"
CONSONANTS = [
    CN("ກ", "ກໍ ໄກ່", "gaw gai", "M", "g", "a hard ‘g’ — between the g in “go” and the k in “skip”", "-k",
       "ກ້ວຍ", "gúay", "banana", "banana", why="animal", name_mean="chicken"),
    CN("ຂ", "ຂໍ ໄຂ່", "khaw khai", "H", "kh", f"‘k’ {ASP}, as in “kite”", "-k", "ໄຂ່", "khai", "egg", "egg", own=True),
    CN("ຄ", "ຄໍ ຄວາຍ", "khaw khwaai", "L", "kh", f"‘k’ {ASP}, as in “kite”", "-k", "ຄົກ", "khok",
       "mortar (for pounding food)", "mortar", why="animal", name_mean="water buffalo"),
    CN("ງ", "ງໍ ງົວ", "ngaw ngua", "L", "ng", "‘ng’ as in “sing” — but at the start of a word!", "-ng",
       "ໝາກເງາະ", "maak-ngaw", "rambutan (a red, hairy fruit)", "th_rambutan",
       note=f"Its name word {NT('ງົວ')} means “cow”. We draw no animals, so our word is {NT('ໝາກເງາະ')}: "
            f"find {NT('ງ')} in the middle!"),
    CN("ຈ", "ຈໍ ຈອກ", "jaw jawk", "M", "j", "a soft ‘j’ as in “jam” (between j and ch)", None, "ຈອກ", "jawk",
       "cup, drinking glass", "lo_glass", own=True),
    CN("ສ", "ສໍ ເສືອ", "saw seua", "H", "s", "‘s’ as in “sun”", None, "ສະບູ", "sa-buu", "soap", "soap",
       why="animal", name_mean="tiger"),
    CN("ຊ", "ຊໍ ຊ້າງ", "saw saang", "L", "s", "‘s’ as in “sun” (in Thai this letter says ‘ch’)", None, "ຊາ", "saa",
       "tea", "teacup", why="animal", name_mean="elephant"),
    CN("ຍ", "ຍໍ ຍຸງ", "nyaw nyung", "L", "ny", "‘ny’ as in “canyon”, said through the nose", "-y (like the end of “boy”)",
       "ຫຍ້າ", "nyaa", "grass", "th_grass", why="animal", name_mean="mosquito"),
    CN("ດ", "ດໍ ເດັກ", "daw dek", "M", "d", "‘d’ as in “day”", "-t", "ດອກໄມ້", "dawk-mai", "flower", "flower",
       why="person", name_mean="child"),
    CN("ຕ", "ຕໍ ຕາ", "dtaw dtaa", "M", "dt", "a hard ‘t’ with no puff of air, like the t in “stop”", None,
       "ຕົ້ນໄມ້", "dton-mai", "tree", "tree", why="body", name_mean="eye"),
    CN("ຖ", "ຖໍ ຖົງ", "thaw thong", "H", "th", f"‘t’ {ASP}, as in “top” (never the ‘th’ of “the”)", None, "ຖົງ", "thong",
       "bag", "th_bag", own=True),
    CN("ທ", "ທໍ ທຸງ", "thaw thung", "L", "th", f"‘t’ {ASP}, as in “top”", None, "ທຸງ", "thung", "flag", "th_flag",
       own=True),
    CN("ນ", "ນໍ ນົກ", "naw nok", "L", "n", "‘n’ as in “net”", "-n", "ນ້ຳ", "nam", "water", "water",
       why="animal", name_mean="bird"),
    CN("ບ", "ບໍ ແບ້", "baw bae", "M", "b", "‘b’ as in “ball”", "-p", "ບ່ວງ", "buang", "spoon", "spoon",
       why="animal", name_mean="goat"),
    CN("ປ", "ປໍ ປາ", "bpaw bpaa", "M", "bp", "a hard ‘p’ with no puff of air, like the p in “spin”", None,
       "ປະຕູ", "bpa-dtuu", "door", "door", why="animal", name_mean="fish"),
    CN("ຜ", "ຜໍ ເຜິ້ງ", "phaw pheung", "H", "ph", f"‘p’ {ASP}, as in “pen” (never ‘f’)", None, "ຜັກ", "phak",
       "vegetables", "carrot", why="animal", name_mean="bee"),
    CN("ຝ", "ຝໍ ຝົນ", "faw fon", "H", "f", "‘f’ as in “fan”", None, "ຝົນ", "fon", "rain", "raincloud", own=True),
    CN("ພ", "ພໍ ພູ", "phaw phuu", "L", "ph", f"‘p’ {ASP}, as in “pen” (never ‘f’)", None, "ພູ", "phuu", "mountain",
       "mountain", own=True),
    CN("ຟ", "ຟໍ ໄຟ", "faw fai", "L", "f", "‘f’ as in “fan”", None, "ໄຟ", "fai", "fire", "lo_fire", own=True),
    CN("ມ", "ມໍ ແມວ", "maw maeo", "L", "m", "‘m’ as in “moon”", "-m", "ໄມ້ກວາດ", "mai-gwaat", "broom", "broom",
       why="animal", name_mean="cat"),
    CN("ຢ", "ຢໍ ຢາ", "yaw yaa", "M", "y", "‘y’ as in “yes”", None, "ຢາ", "yaa", "medicine", "medicine", own=True),
    CN("ຣ", "ຣໍ ຣົຖ", "raw rot", "L", "r", "‘r’ as in “run” (many people say ‘l’)", None, "ຣົຖ", "rot", "car", "lo_car",
       note=f"This is the letter’s own name word: {NT('ຣົຖ')}. Today ‘car’ is usually written {NT('ລົດ')}; "
            f"{NT('ຣ')} is used mostly in names and borrowed words."),
    CN("ລ", "ລໍ ລິງ", "law ling", "L", "l", "‘l’ as in “lamp”", None, "ລະຄັງ", "la-khang", "bell", "th_bell",
       why="animal", name_mean="monkey"),
    CN("ວ", "ວໍ ວີ", "waw wii", "L", "w", "‘w’ as in “water”", "-w (like the end of “now”)", "ວີ", "wii",
       "hand fan", "lo_fan", own=True),
    CN("ຫ", "ຫໍ ຫ່ານ", "haw haan", "H", "h", "‘h’ as in “hat”", None, "ຫີບ", "hiip", "chest (a box with a lid)",
       "th_chest", why="animal", name_mean="goose"),
    CN("ອ", "ອໍ ໂອ", "aw oo", "M", "", "no sound of its own: it holds a vowel at the start of a word", None,
       "ໂອ", "oo", "bowl", "lo_bowl",
       note=f"This is the letter’s own name word: {NT('ໂອ')}! You will meet {NT('ອ')} again in Part 2, "
            f"holding the vowels."),
    CN("ຮ", "ຮໍ ເຮືອນ", "haw heuan", "L", "h", "‘h’ as in “hat”", None, "ເຮືອນ", "heuan", "house", "house", own=True),
]

WHERE = {"after": "after", "above": "above", "below": "below", "before": "before",
         "around": "around (before and after)", "aboveafter": "above and after"}


def VW(carrier, sign, name, name_tr, sound, where, length, ex, ex_tr, word, tr, meaning, pic, args=None, note=None):
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">ກ + {sign} = {ex}</div>'
            f'<div class="small"><i>{ex_tr}</i> · {length} · the sign goes <b>{WHERE[where]}</b> the consonant</div>')
    return letter(carrier, name, name_tr, sound, word, tr, meaning, pic, phon, "Lao phonetics · vowel sign",
                  args, note)


VOWELS = [
    VW("ອະ", "◌ະ", "ສະຫຼະ ອະ", "sa-la a", "a short ‘a’ as in “cup”, cut off quickly", "after", "short", "ກະ", "ga",
       "ກະຕ່າ", "ga-dtaa", "basket", "basket"),
    VW("ອາ", "◌າ", "ສະຫຼະ ອາ", "sa-la aa", "a long ‘aa’ as in “father”", "after", "long", "ກາ", "gaa",
       "ນາ", "naa", "rice field", "paddy"),
    VW("ອິ", "◌ິ", "ສະຫຼະ ອິ", "sa-la i", "a short ‘i’ as in “sit”", "above", "short", "ກິ", "gi",
       "ກິ່ງໄມ້", "ging-mai", "branch", "lo_branch"),
    VW("ອີ", "◌ີ", "ສະຫຼະ ອີ", "sa-la ii", "a long ‘ee’ as in “see”", "above", "long", "ກີ", "gii",
       "ສີ", "sii", "colours, paints", "palette"),
    VW("ອຶ", "◌ຶ", "ສະຫຼະ ອຶ", "sa-la eu", "a short ‘eu’: say ‘oo’ with a big smile, lips not round", "above", "short",
       "ກຶ", "geu", "ປຶ້ມ", "bpeum", "book", "book", args=dict(left="ກ ຂ ຄ", right="ະ າ ິ")),
    VW("ອື", "◌ື", "ສະຫຼະ ອື", "sa-la euu", "a long ‘euu’: the same smiling sound, held longer", "above", "long",
       "ກື", "geuu", "ຄືນ", "kheun", "night", "moon"),
    VW("ອຸ", "◌ຸ", "ສະຫຼະ ອຸ", "sa-la u", "a short ‘u’ as in “put”", "below", "short", "ກຸ", "gu",
       "ພຸ່ມໄມ້", "phum-mai", "bush", "lo_bush"),
    VW("ອູ", "◌ູ", "ສະຫຼະ ອູ", "sa-la uu", "a long ‘oo’ as in “moon”", "below", "long", "ກູ", "guu",
       "ຕູ້", "dtuu", "cupboard", "lo_cupboard"),
    VW("ເອ", "ເ◌", "ສະຫຼະ ເອ", "sa-la ee", "a long ‘e’ as in “they” (with no ‘y’ at the end)", "before", "long",
       "ເກ", "gee", "ເມກ", "meek", "clouds", "clouds"),
    VW("ແອ", "ແ◌", "ສະຫຼະ ແອ", "sa-la ae", "a long ‘a’ as in “cat”", "before", "long", "ແກ", "gae",
       "ແຕງໂມ", "dtaeng-moo", "watermelon", "watermelon"),
    VW("ໂອ", "ໂ◌", "ສະຫຼະ ໂອ", "sa-la oo", "a long ‘o’ as in “go” (with no ‘w’ at the end)", "before", "long",
       "ໂກ", "goo", "ໂຄມໄຟ", "khoom-fai", "lamp", "lo_lamp"),
    VW("ອໍ", "◌ໍ", "ສະຫຼະ ອໍ", "sa-la aw", "a long ‘aw’ as in “saw”", "above", "long", "ກໍ", "gaw",
       "ດິນສໍ", "din-saw", "pencil", "lo_pencil",
       note=f"With a letter after it, the sign changes to {NT('ອ')}: {NT('ກ + ອ + ນ = ກອນ')}."),
    VW("ເອຍ", "ເ◌ຍ", "ສະຫຼະ ເອຍ", "sa-la ia", "‘ee-a’, sliding together, as in “Mia”", "around", "long", "ເກຍ",
       "gia", "ຕຽງ", "dtiang", "bed", "th_bed",
       note=f"With a letter after it, the sign changes to {NT('◌ຽ')}: {NT('ຕ + ຽ + ງ = ຕຽງ')}."),
    VW("ເອືອ", "ເ◌ືອ", "ສະຫຼະ ເອືອ", "sa-la eua", "the smiling ‘eu’ sliding into ‘a’", "around", "long", "ເກືອ",
       "geua", "ເກືອ", "geua", "salt", "salt", args=dict(label="ເກືອ")),
    VW("ອົວ", "◌ົວ", "ສະຫຼະ ອົວ", "sa-la ua", "‘oo-a’, sliding together", "aboveafter", "long", "ກົວ", "gua",
       "ຂົວ", "khua", "bridge", "lo_bridge",
       note=f"With a letter after it, the sign shrinks to {NT('ວ')}: {NT('ກ + ວ + ນ = ກວນ')}."),
    VW("ອຳ", "◌ຳ", "ສະຫຼະ ອຳ", "sa-la am", "‘am’ as in “hum”", "after", "short", "ກຳ", "gam",
       "ຖ້ຳ", "tham", "cave", "lo_cave"),
    VW("ໄອ", "ໄ◌", "ສະຫຼະ ໄອ", "sa-la ai (mai ma-lai)", "‘ai’ as in “eye”", "before", "short", "ໄກ", "gai",
       "ໄຫ", "hai", "big clay jar", "th_ongjar"),
    VW("ໃອ", "ໃ◌", "ສະຫຼະ ໃອ", "sa-la ai (mai muan)", "‘ai’ as in “eye” — the same sound as ໄ", "before", "short",
       "ໃກ", "gai", "ໃບໄມ້", "bai-mai", "leaf", "th_leaf",
       note=f"{NT('ໃ')} is used in only about 20 Lao words — learn them one by one!"),
    VW("ເອົາ", "ເ◌ົາ", "ສະຫຼະ ເອົາ", "sa-la ao", "‘ao’ as in “now”", "around", "short", "ເກົາ", "gao",
       "ເກົ້າອີ້", "gao-ii", "chair", "lo_chair"),
]

CONS_INTRO = f"""<p>Lao has <b>27 consonants</b>. Lao children learn them in this order, each with its own
<b>name word</b>: {NT('ກ ໄກ່')} <i>gaw gai</i>, {NT('ຂ ໄຂ່')} <i>khaw khai</i>, {NT('ຄ ຄວາຍ')} <i>khaw khwaai</i>…</p>
<div class="box" style="margin:0.1in 0"><h3>Our picture words</h3>Many name words are animals or people
(<i>chicken, buffalo, child…</i>). This book draws only objects, plants and nature, so for those letters we
picked another word with the same letter. The page always tells you the real name word.</div>
<div class="box" style="margin:0.1in 0"><h3>Three families of letters</h3>Every consonant is <b>middle-class</b>,
<b>high-class</b> or <b>low-class</b>. The class helps decide the <b>tone</b> of a word:
<div style="margin-top:3px;font-size:12pt">middle {NT('ກ ຈ ດ ຕ ບ ປ ຢ ອ')} · high {NT('ຂ ສ ຖ ຜ ຝ ຫ')} · low: all the others</div></div>
<div class="box"><h3>Lao has tones!</h3>Lao has <b>six tones</b> (in Vientiane), so the same sound can mean
different things. Little marks above a letter help show the tone:
<div class="nt" style="font-size:18pt;text-align:center">ກ່ · ກ້ · ກ໊ · ກ໋</div>
The English letters in this book cannot show tones: listen to a Lao speaker and copy the tune!</div>"""

VOWEL_INTRO = f"""<p>Lao vowels are <b>signs</b> that sit around a consonant: <b>before</b> it, <b>after</b> it,
<b>above</b> it or <b>below</b> it — and some go on two sides at once! This book has <b>19 main vowels</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>The silent holder</h3>A vowel sign can never stand alone. To write a
vowel by itself, Lao uses the silent letter {NT('ອ')}: {NT('ອ + ◌າ = ອາ')} <i>aa</i>. Every big letter in this
part is a vowel sign sitting on {NT('ອ')}.</div>
<div class="box" style="margin:0.1in 0"><h3>Short and long</h3>Many vowels come in pairs: a quick one and a long one,
like {NT('ອິ')} <i>i</i> and {NT('ອີ')} <i>ii</i>. In the English letters, a <b>doubled vowel is long</b>.</div>
<div class="box"><h3>Spell it like a Lao child</h3>Put a consonant and a vowel together and read them as one:
<div class="nt" style="font-size:18pt;text-align:center">ກ + ◌າ = ກາ · ມ + ◌ີ = ມີ · ດ + ◌ູ = ດູ</div>
<div style="text-align:center"><i>gaa · mii · duu</i></div>
A few vowels change shape when a letter comes after them — the pages will show you how.</div>"""

LANG = build(dict(
    code="lo", folder="book-48-lao", series_no=48, isbn="", draft=True,
    name="Lao", native="ພາສາລາວ", native_tr="phaa-saa laao", name_word="ຊື່", write_word="ຂຽນ",
    title_native="ປຶ້ມ ກ ຂ ຄ ຂອງຂ້ອຍ", title_letters="ກຂຄ", belongs_native="ປຶ້ມຫົວນີ້ເປັນຂອງ",
    belongs_pic="lo_fan", alphabet_native="ກ ຂ ຄ", numbers_native="ຕົວເລກລາວ", numbers_tr="dtua-leek laao",
    phrases_native="ຄຳທຳອິດຂອງຂ້ອຍ",
    fonts=fontset("Noto Sans Lao Looped", "noto-sans-lao-looped-lao", "Noto Sans Lao Looped",
                  "noto-sans-lao-looped-lao"),
    disp_family="Noto Sans Lao Looped", text_family="Noto Sans Lao Looped",
    glyph_font="noto-sans-lao-looped-lao-800-normal.woff2",
    font_credit="Noto Sans Lao Looped",
    subtitle="A Coloring Book to Learn, Trace & Say the 27 Lao Consonants and 19 Vowels with English Phonetics",
    phon_feature="each letter’s Lao name (ກ «ກໍ ໄກ່», ຂ «ຂໍ ໄຂ່»…) and simple spelling (ກ + າ = ກາ)",
    sections=[
        section(CONSONANTS, label="CONSONANT", chip="PART 1", title="The Consonants", native="ພະຍັນຊະນະ",
                native_tr="pha-nyan-sa-na — “the consonants”", intro_html=CONS_INTRO,
                chart_title="consonants", chart_cols=7, warmup_title="the consonants", warmup_cols=6),
        section(VOWELS, label="VOWEL", chip="PART 2", title="The Vowels", native="ສະຫຼະ", native_tr="sa-la — “the vowels”",
                intro_html=VOWEL_INTRO, chart_title="vowels", chart_cols=7, warmup_title="the vowels", warmup_cols=5),
    ],
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ii</i> as in “see”, <i>uu</i> as in “moon”, "
        "<i>ee</i> as in “they”, <i>oo</i> as in “go”. A single vowel is short and quick.",
        "<b>h after a letter</b> (<i>kh, th, ph</i>) means “add a puff of breath”. <i>th</i> is never the English "
        "“th” of “the”, and <i>ph</i> is never ‘f’.",
        "<b>g, dt, bp</b> are sounds between English pairs: <i>g</i> (ກ) is between g and k, <i>dt</i> (ຕ) between d and t, "
        "<i>bp</i> (ປ) between b and p — like the k, t, p in “skip, stop, spin”, with no puff.",
        "<b>ny</b> is the sound in “canyon”; <b>aw</b> is the vowel in “saw”; <b>eu</b> is ‘oo’ said with a smile; "
        "<b>ae</b> is the ‘a’ in “cat”.",
        "<b>Tones</b> are not shown in the English letters. Lao has six tones: listen and copy!"],
    phon_explain="The box marked <i>Lao phonetics</i> spells the letter with the vowel າ the way Lao children do "
                 "(ກ + າ = ກາ), and says whether it is a middle-, high- or low-class letter and what it sounds like "
                 "at the end of a word. In Part 2 it shows each vowel sign with ກ.",
    standard="Lao as spoken in Vientiane",
    hello=[
        ("Who speaks it?", "About <b>7 million people</b> speak Lao, as their first or second language.<sup>³</sup>"),
        ("Where?", "In <b>Laos</b>, along the great <b>Mekong River</b> in Southeast Asia, and by Lao families around the world."),
        ("How is it written?", "In the <b>Lao script</b>, from <b>left to right</b>, without spaces between words. "
                               "Lao letters are round cousins of the Thai letters."),
        ("How many letters?", "<b>27 consonants</b>, many vowel signs and tone marks. This book teaches the 27 "
                              "consonants and <b>19 main vowels</b>."),
        ("Tones", "Lao has <b>six tones</b>: the tune of a word changes its meaning. Listen carefully and copy!"),
        ("Did you know?", "Laos is the only country in Southeast Asia with <b>no sea coast</b>. Lao has its own numbers: "
                          "<span class='nt'>໐ ໑ ໒ ໓ ໔ ໕ ໖ ໗ ໘ ໙</span>."),
    ],
    hello_pics=[("lo_fan", {}), ("th_ongjar", {}), ("mosque", {})],
    map=region_map(frame=[[99.0, 12.5], [110.0, 23.5]],
                   points=dict(vientiane=[102.63, 17.97], luangprabang=[102.13, 19.89], savannakhet=[104.75, 16.55],
                               pakse=[105.78, 15.12]),
                   area=(103.9, 18.0, 400, 160), area_rot=52,
                   cities=[("vientiane", "Vientiane", -14, 30, "end", True),
                           ("luangprabang", "Luang Prabang", 16, 8, "start", False),
                           ("savannakhet", "Savannakhet", -14, 8, "end", False),
                           ("pakse", "Pakse", 16, 8, "start", False)],
                   label="LAOS", label_at=[101.9, 21.4], marker=[103.9, 18.0],
                   caption="The circle shows Laos on the world map.",
                   legend="<b>Color it:</b> the land where Lao is spoken (inside the dashed line) <b>yellow</b> · the rest of "
                          "the land <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Vientiane ★, Luang Prabang, Savannakhet "
                          "and Pakse all sit by the Mekong River. Draw the river in blue, from the north down to Pakse!",
                   seas=[("Gulf of Tonkin", 107.9, 19.4)], world_r=13),
    digits=[("໐", "ສູນ", "suun", "zero"), ("໑", "ໜຶ່ງ", "neung", "one"), ("໒", "ສອງ", "sawng", "two"),
            ("໓", "ສາມ", "saam", "three"), ("໔", "ສີ່", "sii", "four"), ("໕", "ຫ້າ", "haa", "five"),
            ("໖", "ຫົກ", "hok", "six"), ("໗", "ເຈັດ", "jet", "seven"), ("໘", "ແປດ", "bpaet", "eight"),
            ("໙", "ເກົ້າ", "gao", "nine")],
    phrases=[("ອັສສະລາມຸອະລັຍກຸມ", "as-sa-laa-mu a-lai-kum", "Peace be upon you (the Muslim greeting)"),
             ("ວະອະລັຍກຸມຸສສະລາມ", "wa a-lai-ku-mus-sa-laam", "And upon you be peace (the reply)"),
             ("ສະບາຍດີ", "sa-baai-dii", "Hello!"),
             ("ຂ້ອຍຊື່ …", "khoi seuu …", "My name is …"),
             ("ຂອບໃຈ", "khawp-jai", "Thank you"),
             ("ຢະຊາກັລລໍຮຸ ໄຄຣັນ", "ja-zaa-gal-laa-hu khai-ran", "May Allah reward you with good"),
             ("ແມ່ · ພໍ່", "mae · phaw", "Mother · Father"),
             ("ອ້າຍ · ເອື້ອຍ", "aai · euay", "Big brother · Big sister"),
             ("ແມ່ນ · ບໍ່", "maen · baw", "Yes · No"),
             ("ຂ້ອຍກຳລັງຮຽນພາສາລາວ!", "khoi gam-lang hian phaa-saa laao!", "I am learning Lao!")],
    cheer=("ມາຊາອັລລໍ! ເກັ່ງຫຼາຍ!", "maa-saa-al-law! geng laai!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International): first- and second-language speakers of Lao.",
    book_pic=dict(left="ກ ຂ ຄ", right="ະ າ ິ"),
    review_note=("Lao: check (1) the replacement picture words for animal/person/body names (ກ້ວຍ, ຄົກ, ໝາກເງາະ, ສະບູ, ຊາ, "
                 "ຫຍ້າ, ດອກໄມ້, ຕົ້ນໄມ້, ນ້ຳ, ບ່ວງ, ປະຕູ, ຜັກ, ໄມ້ກວາດ, ລະຄັງ, ຫີບ); (2) the name word ຣົຖ for ຣ and its note; "
                 "(3) the vowel words ກິ່ງໄມ້, ປຶ້ມ, ຄືນ, ພຸ່ມໄມ້, ຕູ້, ໂຄມໄຟ, ດິນສໍ, ຂົວ, ຖ້ຳ, ໄຫ, ເກົ້າອີ້; "
                 "(4) the Lao spelling of the Arabic phrases (ອັສສະລາມຸອະລັຍກຸມ, ຢະຊາກັລລໍຮຸ ໄຄຣັນ, ມາຊາອັລລໍ) with a Lao "
                 "Muslim reader; (5) the speaker number (about 7 million) against current Ethnologue."),
    tiles="ກຂຄງຈດ", cover_pics=["lo_fan", "th_ongjar", "watermelon", "mosque"], title_size=48,
    speakers_blurb="Lao is spoken by about 7 million people in Laos and around the world.",
    sample_words=[("ໄຂ່", "khai", "egg"), ("ພູ", "phuu", "mountain"), ("ໄຟ", "fai", "fire")],
    keywords=["lao alphabet book for kids", "learn lao for children", "lao letters tracing workbook",
              "laos language coloring book", "muslim kids activity book", "islamic coloring book for children",
              "bilingual lao english toddlers"],
    chart_note="Read the consonants row by row, from ກ to ຮ — the same order as in this book. Then read the vowels.",
))
