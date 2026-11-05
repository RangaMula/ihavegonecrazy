# -*- coding: utf-8 -*-
"""Book 47 - Thai (Thai script: 44 consonants + 19 main vowel signs). Allamahul Bayan Series. REVIEW DRAFT.
Built with the generic builder: Part 1 = the 44 consonants in the traditional order (ก ไก่ ... ฮ นกฮูก),
Part 2 = the main vowel signs, shown on the silent carrier อ.
House rule: the traditional name word is the picture word only when it is an object, plant or nature;
for animal / person / body names a different object word with the same letter is used, with a note."""
from generic import build, letter, section, fontset
from maps import region_map

NT = lambda t: f"<span class='nt'>{t}</span>"
CLASS = {"M": "middle-class", "H": "high-class", "L": "low-class"}
NOT_DRAWN = {"animal": "We draw no animals", "person": "We draw no people", "body": "We draw no faces or bodies"}


def CN(ch, name, name_tr, cls, init, sound, final, word, tr, meaning, pic, own=False, why=None, name_mean=None,
       note=None, args=None):
    """One consonant. init = transliteration of its first sound (for the spelling example ch + า)."""
    fin = (f"at the end of a word it says <b>{final}</b>" if final else "it never ends a word")
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">{ch} + า = {ch}า</div>'
            f'<div class="small"><i>{init}aa</i> · a <b>{CLASS[cls]}</b> letter · {fin}</div>')
    if note is None:
        if own:
            note = f"This is the letter’s own name word: {NT(name)}!"
        elif why:
            note = (f"Its name word {NT(name.split(' ', 1)[1])} means “{name_mean}”. {NOT_DRAWN[why]}, "
                    f"so our word is {NT(word)}.")
    return letter(ch, name, name_tr, sound, word, tr, meaning, pic, phon, "Thai phonetics · spelling & letter class",
                  args, note)


ASP = "with a puff of air"
CONSONANTS = [
    CN("ก", "กอ ไก่", "gaw gai", "M", "g", "a hard ‘g’ — between the g in “go” and the k in “skip”", "-k",
       "กล้วย", "gluay", "banana", "banana", why="animal", name_mean="chicken"),
    CN("ข", "ขอ ไข่", "khaw khai", "H", "kh", f"‘k’ {ASP}, as in “kite”", "-k", "ไข่", "khai", "egg", "egg", own=True),
    CN("ฃ", "ฃอ ขวด", "khaw khuat", "H", "kh", f"‘k’ {ASP} — the same sound as {NT('ข')}", "-k",
       "ขวด", "khuat", "bottle", "th_bottle",
       note=f"{NT('ฃ')} is no longer used in Thai words. Its name word {NT('ขวด')} (bottle) was once spelt with "
            f"{NT('ฃ')}; today it is written with {NT('ข')}."),
    CN("ค", "คอ ควาย", "khaw khwaai", "L", "kh", f"‘k’ {ASP}, as in “kite”", "-k", "ครก", "khrok",
       "mortar (for pounding spices)", "mortar", why="animal", name_mean="water buffalo"),
    CN("ฅ", "ฅอ คน", "khaw khon", "L", "kh", f"‘k’ {ASP} — the same sound as {NT('ค')}", "-k", "ค้อน", "khawn",
       "hammer", "th_hammer",
       note=f"{NT('ฅ')} is no longer used in Thai words. Its name word {NT('คน')} means “person”, so our word "
            f"{NT('ค้อน')} is spelt with {NT('ค')}, which has the same sound."),
    CN("ฆ", "ฆอ ระฆัง", "khaw ra-khang", "L", "kh", f"‘k’ {ASP}", "-k", "ระฆัง", "ra-khang", "bell", "th_bell",
       note=f"This is the letter’s own name word: {NT('ระฆัง')}. Find {NT('ฆ')} in the middle!"),
    CN("ง", "งอ งู", "ngaw nguu", "L", "ng", "‘ng’ as in “sing” — but at the start of a word!", "-ng",
       "เงาะ", "ngaw", "rambutan (a red, hairy fruit)", "th_rambutan", why="animal", name_mean="snake"),
    CN("จ", "จอ จาน", "jaw jaan", "M", "j", "a soft ‘j’ as in “jam” (between j and ch)", "-t", "จาน", "jaan", "plate",
       "plate", own=True),
    CN("ฉ", "ฉอ ฉิ่ง", "chaw ching", "H", "ch", "‘ch’ as in “chair”", None, "ฉิ่ง", "ching",
       "small cymbals (for music)", "th_cymbals", own=True),
    CN("ช", "ชอ ช้าง", "chaw chaang", "L", "ch", "‘ch’ as in “chair”", "-t", "ชา", "chaa", "tea", "teacup",
       why="animal", name_mean="elephant"),
    CN("ซ", "ซอ โซ่", "saw soo", "L", "s", "‘s’ as in “sun”", "-t", "โซ่", "soo", "chain", "th_chain", own=True),
    CN("ฌ", "ฌอ เฌอ", "chaw choe", "L", "ch", "‘ch’ as in “chair” — a rare letter", "-t", "เฌอ", "choe",
       "tree (an old word)", "tree",
       note=f"{NT('เฌอ')} is an old word for tree, kept in the alphabet. Today Thai children say "
            f"{NT('ต้นไม้')} <i>dton-maai</i>."),
    CN("ญ", "ญอ หญิง", "yaw ying", "L", "y", "‘y’ as in “yes”", "-n", "หญ้า", "yaa", "grass", "th_grass",
       why="person", name_mean="woman"),
    CN("ฎ", "ฎอ ชฎา", "daw cha-daa", "M", "d", "‘d’ as in “day”", "-t", "มงกุฎ", "mong-gut", "crown", "th_crown",
       note=f"Its name word {NT('ชฎา')} is the tall crown of Thai dance. We show a simpler crown, "
            f"{NT('มงกุฎ')}: {NT('ฎ')} sits at the end and says ‘t’."),
    CN("ฏ", "ฏอ ปฏัก", "dtaw bpa-dtak", "M", "dt", "a hard ‘t’ with no puff of air, like the t in “stop”", "-t",
       "ปฏัก", "bpa-dtak", "goad (a long pole with a pointed tip)", "th_goad",
       note=f"This is the letter’s own name word: {NT('ปฏัก')}. Find {NT('ฏ')} in the middle!"),
    CN("ฐ", "ฐอ ฐาน", "thaw thaan", "H", "th", f"‘t’ {ASP}, as in “top” (never the ‘th’ of “the”)", "-t",
       "ฐาน", "thaan", "base, stand", "th_pedestal", own=True),
    CN("ฑ", "ฑอ มณโฑ", "thaw mon-thoo", "L", "th", f"‘t’ {ASP} — in a few words it says ‘d’", "-t", "มณฑา",
       "mon-thaa", "magnolia flower", "flower",
       note=f"Its name word {NT('มณโฑ')} is a queen in an old story, so our word is a flower, {NT('มณฑา')}. "
            f"In some words {NT('ฑ')} says ‘d’."),
    CN("ฒ", "ฒอ ผู้เฒ่า", "thaw phuu-thao", "L", "th", f"‘t’ {ASP} — a rare letter", "-t", "อัฒจันทร์",
       "at-tha-jan", "grandstand (rows of seats)", "th_grandstand", why="person", name_mean="old man"),
    CN("ณ", "ณอ เณร", "naw neen", "L", "n", "‘n’ as in “net”", "-n", "มณี", "ma-nii", "jewel", "th_gem",
       why="person", name_mean="young novice"),
    CN("ด", "ดอ เด็ก", "daw dek", "M", "d", "‘d’ as in “day”", "-t", "ดาว", "daao", "star", "star",
       why="person", name_mean="child"),
    CN("ต", "ตอ เต่า", "dtaw dtao", "M", "dt", "a hard ‘t’ with no puff of air, like the t in “stop”", "-t",
       "ตะกร้า", "dta-graa", "basket", "basket", why="animal", name_mean="turtle"),
    CN("ถ", "ถอ ถุง", "thaw thung", "H", "th", f"‘t’ {ASP}, as in “top”", "-t", "ถุง", "thung", "bag", "th_bag",
       own=True),
    CN("ท", "ทอ ทหาร", "thaw tha-haan", "L", "th", f"‘t’ {ASP}, as in “top”", "-t", "ทะเล", "tha-lee", "sea",
       "waves", why="person", name_mean="soldier"),
    CN("ธ", "ธอ ธง", "thaw thong", "L", "th", f"‘t’ {ASP}, as in “top”", "-t", "ธง", "thong", "flag", "th_flag",
       own=True),
    CN("น", "นอ หนู", "naw nuu", "L", "n", "‘n’ as in “net”", "-n", "น้ำ", "naam", "water", "water",
       why="animal", name_mean="mouse"),
    CN("บ", "บอ ใบไม้", "baw bai-maai", "M", "b", "‘b’ as in “ball”", "-p", "ใบไม้", "bai-maai", "leaf", "th_leaf",
       own=True),
    CN("ป", "ปอ ปลา", "bpaw bplaa", "M", "bp", "a hard ‘p’ with no puff of air, like the p in “spin”", "-p",
       "ปากกา", "bpaak-gaa", "pen", "pen", why="animal", name_mean="fish"),
    CN("ผ", "ผอ ผึ้ง", "phaw pheung", "H", "ph", f"‘p’ {ASP}, as in “pen” (never ‘f’)", None, "ผ้าพันคอ",
       "phaa-phan-khaw", "scarf", "scarf", why="animal", name_mean="bee"),
    CN("ฝ", "ฝอ ฝา", "faw faa", "H", "f", "‘f’ as in “fan”", None, "ฝา", "faa", "lid", "th_lid", own=True),
    CN("พ", "พอ พาน", "phaw phaan", "L", "ph", f"‘p’ {ASP}, as in “pen” (never ‘f’)", "-p", "พาน", "phaan",
       "tray on a stand", "th_phaan", own=True),
    CN("ฟ", "ฟอ ฟัน", "faw fan", "L", "f", "‘f’ as in “fan”", "-p", "ฟักทอง", "fak-thawng", "pumpkin", "th_pumpkin",
       why="body", name_mean="tooth"),
    CN("ภ", "ภอ สำเภา", "phaw sam-phao", "L", "ph", f"‘p’ {ASP}, as in “pen”", "-p", "สำเภา", "sam-phao",
       "junk (an old sailing ship)", "th_junk",
       note=f"This is the letter’s own name word: {NT('สำเภา')}. Find {NT('ภ')} at the end!"),
    CN("ม", "มอ ม้า", "maw maa", "L", "m", "‘m’ as in “moon”", "-m", "มะม่วง", "ma-muang", "mango", "mango",
       why="animal", name_mean="horse"),
    CN("ย", "ยอ ยักษ์", "yaw yak", "L", "y", "‘y’ as in “yes”", "-y (like the end of “boy”)", "ยางลบ",
       "yaang-lop", "eraser", "th_eraser",
       note=f"Its name word {NT('ยักษ์')} means “giant”, from old stories. We draw no people, so our word is "
            f"{NT('ยางลบ')}."),
    CN("ร", "รอ เรือ", "raw reua", "L", "r", "a tapped ‘r’ (in everyday talk many people say ‘l’)", "-n", "เรือ",
       "reua", "boat", "boat", own=True),
    CN("ล", "ลอ ลิง", "law ling", "L", "l", "‘l’ as in “lamp”", "-n", "ลูกโป่ง", "luuk-bpoong", "balloon", "balloon",
       why="animal", name_mean="monkey"),
    CN("ว", "วอ แหวน", "waw waen", "L", "w", "‘w’ as in “water”", "-w (like the end of “now”)", "แหวน", "waen",
       "ring", "ring", own=True),
    CN("ศ", "ศอ ศาลา", "saw saa-laa", "H", "s", "‘s’ as in “sun”", "-t", "ศาลา", "saa-laa",
       "pavilion (an open rest hut)", "th_sala", own=True),
    CN("ษ", "ษอ ฤๅษี", "saw rue-sii", "H", "s", "‘s’ as in “sun”", "-t", "กระดาษ", "gra-daat", "paper", "th_paper",
       note=f"Its name word {NT('ฤๅษี')} means “hermit” (a person). Find {NT('ษ')} at the end of "
            f"{NT('กระดาษ')} — there it says ‘t’!"),
    CN("ส", "สอ เสือ", "saw seua", "H", "s", "‘s’ as in “sun”", "-t", "สับปะรด", "sap-bpa-rot", "pineapple",
       "pineapple", why="animal", name_mean="tiger"),
    CN("ห", "หอ หีบ", "haw hiip", "H", "h", "‘h’ as in “hat”", None, "หีบ", "hiip", "chest (a box with a lid)",
       "th_chest", own=True),
    CN("ฬ", "ฬอ จุฬา", "law ju-laa", "L", "l", "‘l’ as in “lamp” — a rare letter", "-n", "จุฬา", "ju-laa",
       "star-shaped kite", "th_chula",
       note=f"This is the letter’s own name word: {NT('จุฬา')}. Find {NT('ฬ')} at the end!"),
    CN("อ", "ออ อ่าง", "aw aang", "M", "", "no sound of its own: it holds a vowel at the start of a word", None,
       "อ่าง", "aang", "basin (a big bowl for water)", "th_basin",
       note=f"This is the letter’s own name word: {NT('อ่าง')}! You will meet {NT('อ')} again in Part 2, "
            f"holding the vowels."),
    CN("ฮ", "ฮอ นกฮูก", "haw nok-huuk", "L", "h", "‘h’ as in “hat”", None, "เฮลิคอปเตอร์", "hee-li-khawp-dtoe",
       "helicopter", "th_helicopter", why="animal", name_mean="owl"),
]

WHERE = {"after": "after", "above": "above", "below": "below", "before": "before",
         "around": "around (before and after)", "aboveafter": "above and after"}


def VW(carrier, sign, name, name_tr, sound, where, length, ex, ex_tr, word, tr, meaning, pic, args=None, note=None):
    phon = (f'<div class="nt" style="font-size:19pt;line-height:1.5">ก + {sign} = {ex}</div>'
            f'<div class="small"><i>{ex_tr}</i> · {length} · the sign goes <b>{WHERE[where]}</b> the consonant</div>')
    return letter(carrier, name, name_tr, sound, word, tr, meaning, pic, phon, "Thai phonetics · vowel sign",
                  args, note)


VOWELS = [
    VW("อะ", "◌ะ", "สระอะ", "sa-ra a", "a short ‘a’ as in “cup”, cut off quickly", "after", "short", "กะ", "ga",
       "มะนาว", "ma-naao", "lime", "lemon"),
    VW("อา", "◌า", "สระอา", "sa-ra aa", "a long ‘aa’ as in “father”", "after", "long", "กา", "gaa",
       "นาฬิกา", "naa-li-gaa", "clock", "clock"),
    VW("อิ", "◌ิ", "สระอิ", "sa-ra i", "a short ‘i’ as in “sit”", "above", "short", "กิ", "gi",
       "ชิงช้า", "ching-chaa", "swing", "swing"),
    VW("อี", "◌ี", "สระอี", "sa-ra ii", "a long ‘ee’ as in “see”", "above", "long", "กี", "gii",
       "สี", "sii", "colours, paints", "palette"),
    VW("อึ", "◌ึ", "สระอึ", "sa-ra eu", "a short ‘eu’: say ‘oo’ with a big smile, lips not round", "above", "short",
       "กึ", "geu", "ตึก", "dteuk", "building", "building"),
    VW("อือ", "◌ือ", "สระอือ", "sa-ra euu", "a long ‘euu’: the same smiling sound, held longer", "above", "long",
       "กือ", "geuu", "หนังสือ", "nang-seuu", "book", "book", args=dict(left="ก ข ค", right="ะ า ิ"),
       note=f"With no letter after it, the sign is written {NT('◌ือ')}: the little {NT('อ')} is silent."),
    VW("อุ", "◌ุ", "สระอุ", "sa-ra u", "a short ‘u’ as in “put”", "below", "short", "กุ", "gu",
       "กุญแจ", "gun-jae", "key", "th_key"),
    VW("อู", "◌ู", "สระอู", "sa-ra uu", "a long ‘oo’ as in “moon”", "below", "long", "กู", "guu",
       "ประตู", "bpra-dtuu", "door", "door"),
    VW("เอ", "เ◌", "สระเอ", "sa-ra ee", "a long ‘e’ as in “they” (with no ‘y’ at the end)", "before", "long", "เก",
       "gee", "เมฆ", "meek", "clouds", "clouds"),
    VW("แอ", "แ◌", "สระแอ", "sa-ra ae", "a long ‘a’ as in “cat”", "before", "long", "แก", "gae",
       "แตงโม", "dtaeng-moo", "watermelon", "watermelon"),
    VW("โอ", "โ◌", "สระโอ", "sa-ra oo", "a long ‘o’ as in “go” (with no ‘w’ at the end)", "before", "long", "โก",
       "goo", "โอ่ง", "oong", "big water jar", "th_ongjar"),
    VW("ออ", "◌อ", "สระออ", "sa-ra aw", "a long ‘aw’ as in “saw”", "after", "long", "กอ", "gaw",
       "ช้อน", "chawn", "spoon", "spoon"),
    VW("เอีย", "เ◌ีย", "สระเอีย", "sa-ra ia", "‘ee-a’, sliding together, as in “Mia”", "around", "long", "เกีย",
       "gia", "เตียง", "dtiang", "bed", "th_bed"),
    VW("เอือ", "เ◌ือ", "สระเอือ", "sa-ra eua", "the smiling ‘eu’ sliding into ‘a’", "around", "long", "เกือ",
       "geua", "เกลือ", "gleua", "salt", "salt", args=dict(label="เกลือ")),
    VW("อัว", "◌ัว", "สระอัว", "sa-ra ua", "‘oo-a’, sliding together", "aboveafter", "long", "กัว", "gua",
       "หัวหอม", "hua-hawm", "onion", "onion",
       note=f"With a letter after it, the sign shrinks to {NT('ว')}: {NT('ก + ว + น = กวน')}."),
    VW("อำ", "◌ำ", "สระอำ", "sa-ra am", "‘am’ as in “hum”", "after", "short", "กำ", "gam",
       "น้ำผึ้ง", "nam-pheung", "honey", "honey"),
    VW("ไอ", "ไ◌", "สระไอ ไม้มลาย", "sa-ra ai mai ma-laai", "‘ai’ as in “eye”", "before", "short", "ไก", "gai",
       "ไม้กวาด", "mai-gwaat", "broom", "broom"),
    VW("ใอ", "ใ◌", "สระใอ ไม้ม้วน", "sa-ra ai mai muan", "‘ai’ as in “eye” — the same sound as ไ", "before",
       "short", "ใก", "gai", "ใบตอง", "bai-dtawng", "banana leaf", "th_bananaleaf",
       note=f"{NT('ใ')} is used in only about 20 Thai words. Thai children learn them in a little rhyme!"),
    VW("เอา", "เ◌า", "สระเอา", "sa-ra ao", "‘ao’ as in “now”", "around", "short", "เกา", "gao",
       "ภูเขา", "phuu-khao", "mountain", "mountain"),
]

CONS_INTRO = f"""<p>Thai has <b>44 consonants</b>. Thai children learn them in this order, each with its own
<b>name word</b>: {NT('ก ไก่')} <i>gaw gai</i>, {NT('ข ไข่')} <i>khaw khai</i>, {NT('ค ควาย')} <i>khaw khwaai</i>…
Two of them, {NT('ฃ')} and {NT('ฅ')}, are no longer used in words, but they keep their place in the alphabet.</p>
<div class="box" style="margin:0.1in 0"><h3>Our picture words</h3>Many name words are animals or people
(<i>chicken, snake, child…</i>). This book draws only objects, plants and nature, so for those letters we
picked another word with the same letter. The page always tells you the real name word.</div>
<div class="box" style="margin:0.1in 0"><h3>Three families of letters</h3>Every consonant is <b>middle-class</b>,
<b>high-class</b> or <b>low-class</b>. The class helps decide the <b>tone</b> of a word:
<div style="margin-top:3px;font-size:12pt">middle {NT('ก จ ฎ ฏ ด ต บ ป อ')} · high {NT('ข ฃ ฉ ฐ ถ ผ ฝ ศ ษ ส ห')} · low: all the others</div></div>
<div class="box"><h3>Thai has tones!</h3>Thai has <b>five tones</b> — mid, low, falling, high and rising — so
the same sound can mean different things. Four little marks above a letter help show the tone:
<div class="nt" style="font-size:18pt;text-align:center">ก่ · ก้ · ก๊ · ก๋</div>
The English letters in this book cannot show tones: listen to a Thai speaker and copy the tune!</div>"""

VOWEL_INTRO = f"""<p>Thai vowels are <b>signs</b> that sit around a consonant: <b>before</b> it, <b>after</b> it,
<b>above</b> it or <b>below</b> it — and some go on two sides at once! This book has <b>19 main vowels</b>.</p>
<div class="box" style="margin:0.1in 0"><h3>The silent holder</h3>A vowel sign can never stand alone. To write a
vowel by itself, Thai uses the silent letter {NT('อ')}: {NT('อ + ◌า = อา')} <i>aa</i>. Every big letter in this
part is a vowel sign sitting on {NT('อ')}.</div>
<div class="box" style="margin:0.1in 0"><h3>Short and long</h3>Many vowels come in pairs: a quick one and a long one,
like {NT('อิ')} <i>i</i> and {NT('อี')} <i>ii</i>. In the English letters, a <b>doubled vowel is long</b>.</div>
<div class="box"><h3>Spell it like a Thai child</h3>Put a consonant and a vowel together and read them as one:
<div class="nt" style="font-size:18pt;text-align:center">ก + ◌า = กา · ม + ◌ี = มี · ด + ◌ู = ดู</div>
<div style="text-align:center"><i>gaa · mii · duu</i></div>
There are a few more vowels, too (like {NT('เออ')} <i>oe</i> and {NT('ฤ')} <i>rue</i>) — you will meet them as you read.</div>"""

LANG = build(dict(
    code="th", folder="book-47-thai", series_no=47, isbn="", draft=True,
    name="Thai", native="ภาษาไทย", native_tr="phaa-saa thai", name_word="ชื่อ", write_word="เขียน",
    title_native="ก ข ค เล่มแรกของฉัน", title_letters="กขค", belongs_native="หนังสือเล่มนี้เป็นของ",
    belongs_pic="th_chula", alphabet_native="ก ข ค", numbers_native="ตัวเลขไทย", numbers_tr="dtua-leek thai",
    phrases_native="คำแรกของฉัน",
    fonts=fontset("Noto Sans Thai Looped", "noto-sans-thai-looped-thai", "Noto Sans Thai Looped",
                  "noto-sans-thai-looped-thai"),
    disp_family="Noto Sans Thai Looped", text_family="Noto Sans Thai Looped",
    glyph_font="noto-sans-thai-looped-thai-800-normal.woff2",
    font_credit="Noto Sans Thai Looped",
    letters_word="Letters",
    subtitle="A Coloring Book to Learn, Trace & Say the 44 Thai Consonants and 19 Vowels with English Phonetics",
    phon_feature="each letter’s Thai name (ก «กอ ไก่», ข «ขอ ไข่»…) and simple spelling (ก + า = กา)",
    sections=[
        section(CONSONANTS, label="CONSONANT", chip="PART 1", title="The Consonants", native="พยัญชนะ",
                native_tr="pha-yan-cha-na — “the consonants”", intro_html=CONS_INTRO,
                chart_title="consonants", chart_cols=9, warmup_title="the consonants", warmup_cols=8),
        section(VOWELS, label="VOWEL", chip="PART 2", title="The Vowels", native="สระ", native_tr="sa-ra — “the vowels”",
                intro_html=VOWEL_INTRO, chart_title="vowels", chart_cols=7, warmup_title="the vowels", warmup_cols=5),
    ],
    sound_notes=[
        "<b>Doubled vowels are long:</b> <i>aa</i> as in “father”, <i>ii</i> as in “see”, <i>uu</i> as in “moon”, "
        "<i>ee</i> as in “they”, <i>oo</i> as in “go”. A single vowel is short and quick.",
        "<b>h after a letter</b> (<i>kh, th, ph, ch</i>) means “add a puff of breath”. <i>th</i> is never the English "
        "“th” of “the”, and <i>ph</i> is never ‘f’.",
        "<b>g, dt, bp</b> are sounds between English pairs: <i>g</i> (ก) is between g and k, <i>dt</i> (ต) between d and t, "
        "<i>bp</i> (ป) between b and p — like the k, t, p in “skip, stop, spin”, with no puff.",
        "<b>aw</b> is the vowel in “saw”; <b>eu</b> is ‘oo’ said with a smile; <b>ae</b> is the ‘a’ in “cat”.",
        "<b>Tones</b> are not shown in the English letters. Thai has five tones: listen and copy!"],
    phon_explain="The box marked <i>Thai phonetics</i> spells the letter with the vowel า the way Thai children do "
                 "(ก + า = กา), and says whether it is a middle-, high- or low-class letter and what it sounds like "
                 "at the end of a word. In Part 2 it shows each vowel sign with ก.",
    standard="standard (Central) Thai as spoken in Bangkok",
    hello=[
        ("Who speaks it?", "About <b>60 million people</b> speak Thai, as their first or second language.<sup>³</sup>"),
        ("Where?", "In <b>Thailand</b>, in Southeast Asia, and by Thai families all around the world."),
        ("How is it written?", "In the <b>Thai script</b>, from <b>left to right</b>. Words are written without spaces "
                               "between them — a space shows the end of a phrase."),
        ("How many letters?", "<b>44 consonants</b>, many vowel signs and four tone marks. This book teaches the 44 "
                              "consonants and <b>19 main vowels</b>."),
        ("Tones", "Thai has <b>five tones</b>. <span class='nt'>ใกล้</span> <i>glai</i> (near) and "
                  "<span class='nt'>ไกล</span> <i>glai</i> (far) differ only in their tune!"),
        ("Did you know?", "Thai has its own numbers: <span class='nt'>๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙</span>. You can color them "
                          "at the back of this book."),
    ],
    hello_pics=[("th_chula", {}), ("pineapple", {}), ("mosque", {})],
    map=region_map(frame=[[94.5, 4.5], [108.5, 21.0]],
                   points=dict(bangkok=[100.50, 13.75], chiangmai=[98.98, 18.79], khonkaen=[102.83, 16.44],
                               phuket=[98.39, 7.88], hatyai=[100.47, 7.01]),
                   area=None,
                   cities=[("bangkok", "Bangkok", 16, 8, "start", True), ("chiangmai", "Chiang Mai", -14, 8, "end", False),
                           ("khonkaen", "Khon Kaen", 14, 8, "start", False), ("phuket", "Phuket", -14, 8, "end", False),
                           ("hatyai", "Hat Yai", 14, 8, "start", False)],
                   label="THAILAND", label_at=[101.6, 15.2], marker=[101.0, 14.0],
                   caption="The circle shows Thailand on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Thai is spoken all over "
                          "Thailand: in Bangkok ★ by the sea, in Chiang Mai in the northern hills, in Khon Kaen, "
                          "and in Phuket and Hat Yai in the south.",
                   seas=[("Andaman Sea", 96.2, 12.6), ("South China Sea", 106.2, 6.2)],
                   world_r=13),
    digits=[("๐", "ศูนย์", "suun", "zero"), ("๑", "หนึ่ง", "neung", "one"), ("๒", "สอง", "sawng", "two"),
            ("๓", "สาม", "saam", "three"), ("๔", "สี่", "sii", "four"), ("๕", "ห้า", "haa", "five"),
            ("๖", "หก", "hok", "six"), ("๗", "เจ็ด", "jet", "seven"), ("๘", "แปด", "bpaet", "eight"),
            ("๙", "เก้า", "gao", "nine")],
    phrases=[("อัสสะลามุอะลัยกุม", "as-sa-laa-mu a-lai-kum", "Peace be upon you (the Muslim greeting)"),
             ("วะอะลัยกุมุสสะลาม", "wa a-lai-ku-mus-sa-laam", "And upon you be peace (the reply)"),
             ("สวัสดี", "sa-wat-dii", "Hello!"),
             ("ฉันชื่อ …", "chan cheuu …", "My name is … (a boy may say ผมชื่อ … phom cheuu)"),
             ("ขอบคุณ", "khawp-khun", "Thank you"),
             ("ญะซากัลลอฮุค็อยรอน", "ja-zaa-gal-laa-hu khai-ran", "May Allah reward you with good"),
             ("แม่ · พ่อ", "mae · phaw", "Mother · Father"),
             ("พี่ชาย · พี่สาว", "phii-chaai · phii-saao", "Big brother · Big sister"),
             ("ใช่ · ไม่ใช่", "chai · mai chai", "Yes · No"),
             ("ฉันกำลังเรียนภาษาไทย!", "chan gam-lang rian phaa-saa thai!", "I am learning Thai!")],
    cheer=("มาชาอัลลอฮ์! เก่งมาก!", "maa-chaa-al-law! geng maak!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International): first- and second-language speakers of Thai.",
    book_pic=dict(left="ก ข ค", right="ะ า ิ"),
    review_note=("Thai: check (1) the replacement picture words for animal/person names (กล้วย, ครก, ค้อน for ฅ, เงาะ, ชา, "
                 "หญ้า, มงกุฎ for ฎ, มณฑา, อัฒจันทร์, มณี, ดาว, ตะกร้า, ทะเล, น้ำ, ปากกา, ผ้าพันคอ, ฟักทอง, มะม่วง, ยางลบ, "
                 "ลูกโป่ง, กระดาษ, สับปะรด, เฮลิคอปเตอร์); (2) the simplified transliterations (gaw/khaw/dtaw/bpaw system, "
                 "no tone marks); (3) the Thai spelling of the Arabic phrases (อัสสะลามุอะลัยกุม, ญะซากัลลอฮุค็อยรอน, "
                 "มาชาอัลลอฮ์) with a Thai Muslim reader; (4) the choice of 19 vowels and the ใ rhyme note."),
    tiles="กขคงจด", cover_pics=["pineapple", "th_chula", "mango", "mosque"], title_size=48,
    speakers_blurb="Thai is spoken by about 60 million people in Thailand and around the world.",
    sample_words=[("ไข่", "khai", "egg"), ("ดาว", "daao", "star"), ("มะม่วง", "ma-muang", "mango")],
    keywords=["thai alphabet book for kids", "learn thai for children", "thai letters tracing workbook",
              "thai consonants coloring book", "muslim kids activity book", "islamic coloring book for children",
              "bilingual thai english toddlers"],
    chart_note="Read the consonants row by row, from ก to ฮ — the same order as in this book. Then read the vowels.",
))
