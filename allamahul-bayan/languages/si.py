# -*- coding: utf-8 -*-
"""Book 14 - Sinhala (Sinhala script). Allamahul Bayan Series. REVIEW DRAFT.
Vowels (incl. ඇ ඈ and the binduva) + the consonants in everyday use, in the traditional order,
incl. the half-nasal letters ඟ ඬ ඳ ඹ. The rarest letters of the full 60-letter hodiya are listed on
the consonant intro page. Picture plug-ins (si_*) live in engine/pics/si_dv_pics.py."""
from indic import build, vowel as V, cons as C, fontset, COMMON_NOTES
from maps import region_map

ZWJ = "‍"
HAL = "්"

def nt(t):
    return f"<span class='nt'>{t}</span>"

def inside(letter, word):
    return f"Find {nt(letter)} inside {nt(word)} — it hardly ever starts a word."

def sign_inside(sign, word):
    return (f"This vowel rarely starts a word. Find its sign {nt('◌' + sign)} in {nt(word)}!")

MP = "මහාප්" + ZWJ + "රාණ"          # mahaapraana: "with a big breath" (aspirated)
MP_TR = "mahaapraana"
SAME = "in everyday Sinhala it sounds just like {} — in careful speech, add a puff of breath"

VOWELS = [
    V("අ", "ayanna", "a short ‘a’ as in “about”", "", "", "අන්නාසි", "annaasi", "pineapple", "pineapple", name="අයන්න"),
    V("ආ", "aayanna", "‘aa’ as in “father”", "ා", "ඇලපිල්ල", "ආප්ප", "aappa", "hoppers (crispy bowl pancakes)", "si_hopper",
      name="ආයන්න"),
    V("ඇ", "æyanna", "‘æ’ — the ‘a’ in “cat”, short", "ැ", "ඇදය", "ඇපල්", "æpal", "apple", "apple", name="ඇයන්න"),
    V("ඈ", "ææyanna", "‘ææ’ — the ‘a’ in “cat”, said long", "ෑ", "දිග ඇදය", "පෑන", "pææna", "pen", "pen", name="ඈයන්න",
      note=sign_inside("ෑ", "පෑන")),
    V("ඉ", "iyanna", "‘i’ as in “sit” — short", "ි", "ඉස්පිල්ල", "ඉර", "ira", "the sun", "sun", name="ඉයන්න"),
    V("ඊ", "eeyanna", "‘ee’ as in “see” — long", "ී", "දිග ඉස්පිල්ල", "ඊතලය", "eetalaya", "arrow", "bowarrow", name="ඊයන්න"),
    V("උ", "uyanna", "‘u’ as in “put” — short", "ු", "පාපිල්ල", "උක්", "uk", "sugarcane", "sugarcane", name="උයන්න"),
    V("ඌ", "ooyanna", "‘oo’ as in “moon” — long", "ූ", "දිග පාපිල්ල", "නූල්", "nool", "thread", "wool", name="ඌයන්න",
      note=sign_inside("ූ", "නූල්")),
    V("ඍ", "ruyanna", "‘ru’ as in “root” — a vowel from Sanskrit", "ෘ", "ගැටයන්න", "ඍතුව", "rutuva", "season", "seasons",
      name="ඍයන්න"),
    V("එ", "eyanna", "a short ‘e’ as in “bed”", "ෙ", "කොම්බුව", "එළවළු", "eḷavaḷu", "vegetables", "carrot", name="එයන්න"),
    V("ඒ", "ēyanna", "a long ‘ē’ as in “they” (say “ay”)", "ේ", "කොම්බුව + හල් කිරීම", "තේ", "tē", "tea", "teacup",
      name="ඒයන්න", note=sign_inside("ේ", "තේ") + " Sri Lanka grows famous tea!"),
    V("ඓ", "aiyanna", "‘ai’ as in “aisle”", "ෛ", "කොම්බු දෙක", "තෛලය", "tailaya", "oil", "jar", name="ඓයන්න",
      note=sign_inside("ෛ", "තෛලය")),
    V("ඔ", "oyanna", "a short ‘o’ as in “on”", "ො", "කොම්බුව + ඇලපිල්ල", "ඔරුව", "oruva", "canoe, small boat", "boat",
      name="ඔයන්න"),
    V("ඕ", "ōyanna", "a long ‘ō’ as in “go”", "ෝ", "කොම්බුව + ඇලපිල්ල + හල් කිරීම", "ඕලු", "ōlu", "water lily", "lily",
      name="ඕයන්න"),
    V("ඖ", "auyanna", "‘au’ — like the ‘ow’ in “owl”", "ෞ", "කොම්බුව + ගයනුකිත්ත", "ඖෂධ", "aushadha", "medicine", "medicine",
      name="ඖයන්න"),
    V("අං", "binduva", "a nasal ‘ng’ after the vowel, as in “sing”", "ං", "බින්දුව", "අංකය", "ankaya", "number", "one",
      args=dict(digit="1"), name="අං (බින්දුව)"),
]

CONSONANTS = [
    C("ක", "kayanna", "‘k’ as in “kite” (no puff of air)", "කෙසෙල්", "kesel", "banana", "banana", name="කයන්න"),
    C("ඛ", f"{MP_TR} kayanna", "‘k’ — " + SAME.format("ක"), "ශාඛාව", "shaakhaava", "branch (of a tree)", "si_branch",
      name=f"{MP} කයන්න", note=inside("ඛ", "ශාඛාව")),
    C("ග", "gayanna", "‘g’ as in “go”", "ගෙදර", "gedara", "home, house", "house", name="ගයන්න"),
    C("ඝ", f"{MP_TR} gayanna", "‘g’ — " + SAME.format("ග"), "ඝනකය", "ghanakaya", "cube", "blocks",
      args=dict(letters=("ක", "ග", "ම")), name=f"{MP} ගයන්න"),
    C("ඟ", "sanyaka gayanna", "a half-nasal ‘ng’: a tiny ‘n’ slides into ‘g’, like “finger” said quickly", "ඉණිමඟ", "iṇimanga",
      "ladder", "ladder", name="සඤ්ඤක ගයන්න", note=inside("ඟ", "ඉණිමඟ")),
    C("ච", "chayanna", "‘ch’ as in “chair”", "චිත්" + ZWJ + "රය", "chitraya", "picture, painting", "palette", name="චයන්න"),
    C("ඡ", f"{MP_TR} chayanna", "‘ch’ — " + SAME.format("ච"), "ඡත්" + ZWJ + "රය", "chhatraya", "umbrella, parasol",
      "umbrella", name=f"{MP} චයන්න"),
    C("ජ", "jayanna", "‘j’ as in “jam”", "ජලය", "jalaya", "water", "water", name="ජයන්න"),
    C("ට", "ṭayanna", "a hard ‘t’ — curl your tongue back, as in “top”", "කොට්ටය", "koṭṭaya", "pillow", "pillow", name="ටයන්න",
      note=inside("ට", "කොට්ටය")),
    C("ඩ", "ḍayanna", "a hard ‘d’ — curl your tongue back, as in “dog”", "ගඩොල්", "gaḍol", "brick", "brick", name="ඩයන්න",
      note=inside("ඩ", "ගඩොල්")),
    C("ණ", "muurdhaja ṇayanna", "‘n’ — in everyday Sinhala it sounds just like න", "ලුණු", "luṇu", "salt", "salt",
      args=dict(label="ලුණු"), name="මූර්ධජ ණයන්න", note=inside("ණ", "ලුණු")),
    C("ඬ", "sanyaka ḍayanna", "a half-nasal ‘nḍ’: a tiny ‘n’ slides into a hard ‘ḍ’", "දඬුව", "danḍuva", "stick, rod", "si_sticks",
      name="සඤ්ඤක ඩයන්න", note=inside("ඬ", "දඬුව")),
    C("ත", "tayanna", "a soft ‘t’ — tongue touches the back of the teeth", "තක්කාලි", "takkaali", "tomato", "tomato", name="තයන්න"),
    C("ථ", f"{MP_TR} tayanna", "a soft ‘t’ — " + SAME.format("ත"), "රථය", "rathaya", "cart, carriage", "cart",
      name=f"{MP} තයන්න", note=inside("ථ", "රථය")),
    C("ද", "dayanna", "a soft ‘d’ — tongue touches the back of the teeth", "දෙහි", "dehi", "lime", "lemon", name="දයන්න"),
    C("ධ", f"{MP_TR} dayanna", "a soft ‘d’ — " + SAME.format("ද"), "ධාන්" + ZWJ + "ය", "dhaanya", "grain", "paddy",
      name=f"{MP} දයන්න"),
    C("න", "dantaja nayanna", "‘n’ as in “net”", "නැව", "næva", "ship", "ship", name="දන්තජ නයන්න"),
    C("ඳ", "sanyaka dayanna", "a half-nasal ‘nd’: a tiny ‘n’ slides into a soft ‘d’, like “candle” said quickly", "රට ඉඳි",
      "raṭa indi", "dates", "dates", name="සඤ්ඤක දයන්න", note=inside("ඳ", "ඉඳි")),
    C("ප", "payanna", "‘p’ as in “pen” (no puff of air)", "පොල්", "pol", "coconut", "si_coconut", name="පයන්න"),
    C("ඵ", f"{MP_TR} payanna", "‘p’ — " + SAME.format("ප"), "ඵලය", "phalaya", "fruit", "basket", name=f"{MP} පයන්න"),
    C("බ", "bayanna", "‘b’ as in “ball”", "බත්", "bat", "cooked rice", "rice", name="බයන්න"),
    C("භ", f"{MP_TR} bayanna", "‘b’ — " + SAME.format("බ"), "භෝජනය", "bhōjanaya", "a meal", "plate", name=f"{MP} බයන්න"),
    C("ම", "mayanna", "‘m’ as in “moon”", "මල", "mala", "flower", "flower", name="මයන්න"),
    C("ඹ", "amba bayanna", "a half-nasal ‘mb’: a tiny ‘m’ slides into ‘b’, like “number” said quickly", "අඹ", "amba", "mango",
      "mango", name="අඹ බයන්න", note=inside("ඹ", "අඹ")),
    C("ය", "yayanna", "‘y’ as in “yes”", "යතුර", "yatura", "key", "si_key", name="යයන්න"),
    C("ර", "rayanna", "a tapped ‘r’ — flick the tongue once", "රොටි", "roṭi", "flatbread (roti)", "roti", name="රයන්න"),
    C("ල", "dantaja layanna", "‘l’ as in “lamp”", "ලිඳ", "linda", "well (for water)", "well", name="දන්තජ ලයන්න"),
    C("ව", "vayanna", "between ‘v’ and ‘w’", "වැස්ස", "væssa", "rain", "raincloud", name="වයන්න"),
    C("ශ", "taaluja shayanna", "‘sh’ as in “shoe”", "ශාකය", "shaakaya", "plant", "si_plant", name="තාලුජ ශයන්න"),
    C("ෂ", "muurdhaja shayanna", "‘sh’ as in “shoe” — the same as ශ in everyday Sinhala", "ෂඩස්" + ZWJ + "රය", "shaḍasraya",
      "hexagon", "hexagon", name="මූර්ධජ ෂයන්න"),
    C("ස", "dantaja sayanna", "‘s’ as in “sun”", "සඳ", "sanda", "the moon", "moon", name="දන්තජ සයන්න"),
    C("හ", "hayanna", "‘h’ as in “hat”", "හැන්ද", "hænda", "spoon", "spoon", name="හයන්න"),
    C("ළ", "muurdhaja ḷayanna", "‘l’ — in everyday Sinhala it sounds just like ල", "කළය", "kaḷaya", "clay pot", "pot",
      name="මූර්ධජ ළයන්න", note=inside("ළ", "කළය")),
    C("ෆ", "fayanna", "‘f’ as in “fan” — a new letter for words from English", "ෆුට්බෝල්", "fuṭbōl", "football", "ball",
      name="ෆයන්න"),
]

FONTS = fontset("Noto Sans Sinhala", "noto-sans-sinhala-sinhala", "Noto Sans Sinhala", "noto-sans-sinhala-sinhala")[:3]

LANG = build(dict(
    code="si", folder="book-14-sinhala", series_no=14, isbn="", draft=True,
    name="Sinhala", native="සිංහල", native_tr="sinhala", name_word="නම", write_word="ලියන්න",
    title_native="මගේ පළමු සිංහල හෝඩිය", title_letters="අආඇකගම", belongs_native="මේ පොත මගේ", belongs_pic="si_hopper",
    alphabet_native="හෝඩිය", numbers_native="ඉලක්කම්", numbers_tr="ilakkam", phrases_native="මුල් වචන",
    fonts=FONTS, disp_family="Noto Sans Sinhala", text_family="Noto Sans Sinhala",
    glyph_font=["noto-sans-sinhala-sinhala-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans Sinhala",
    extra_css=(".nt .small,.vt .small{font-family:'Nunito','Noto Sans Sinhala',sans-serif !important}"
               " .vt td{padding:0 4px !important} .vt td.ntd{font-size:17pt !important;line-height:1.25}"
               " .vt td.nt{font-size:13pt !important} .lp-name{font-size:19pt;line-height:1.3}"),
    base="ක", base_tr="ka", virama=HAL, inherent="අ", inherent_tr="a",
    virama_note=f"<i>k + a = ka</i>. The little mark {nt(HAL)} (<i>hal kiriima</i>) switches the hidden vowel off: "
                f"{nt('ක්')} says just <i>k</i>, as at the end of {nt('පොල්')} <i>pol</i> (coconut).",
    vowels_native="ස්වර", vowels_tr="svara — “voice letters”",
    cons_native="ව්" + ZWJ + "යඤ්ජන", cons_tr="vyanjana",
    vowel_extra=f"Sinhala has two vowels that most other scripts of South Asia do not: {nt('ඇ ඈ')} "
                f"<i>(æ, ææ)</i>, the ‘a’ of “cat”. The last one, {nt('අං')}, is the <i>binduva</i> sign that adds ‘ng’.",
    cons_extra=" They are the letters children meet most in everyday Sinhala, in the traditional order.",
    cons_box=(
        "<div class='box' style='margin:0.08in 0'><h3>Letter families</h3>"
        "<div class='nt' style='font-size:15pt;line-height:1.55;margin-top:2px'>"
        "ක ඛ ග ඝ ඟ — <span class='small' style='font-family:Nunito'>back of the throat</span><br>"
        "ච ඡ ජ — <span class='small' style='font-family:Nunito'>middle of the tongue</span><br>"
        "ට ඩ ණ ඬ — <span class='small' style='font-family:Nunito'>tongue curled back (hard)</span><br>"
        "ත ථ ද ධ න ඳ — <span class='small' style='font-family:Nunito'>tongue on the teeth (soft)</span><br>"
        "ප ඵ බ භ ම ඹ — <span class='small' style='font-family:Nunito'>the lips</span></div></div>"
        "<div class='box' style='margin:0.08in 0'><h3>Half-nasal letters: a Sinhala speciality</h3>"
        f"{nt('ඟ ඬ ඳ ඹ')} are one letter each, but they sound like a tiny <i>n</i> or <i>m</i> gliding into the next sound: "
        f"{nt('අඹ')} <i>amba</i> (mango), {nt('සඳ')} <i>sanda</i> (moon). Say them quickly, as one sound!</div>"
        "<div class='box'><h3>Big-breath letters and rare letters</h3>"
        f"{nt('ඛ ඝ ඡ ථ ධ ඵ භ')} are <i>mahaapraana</i> (“big breath”) letters, used in words from Sanskrit and Pali. "
        f"The full Sinhala alphabet has about 60 letters; the rarest — {nt('ඞ ඣ ඤ ඥ ඦ ඨ ඪ')}, the vowels "
        f"{nt('ඎ ඏ ඐ')} and the sign {nt('ඃ')} — appear in only a few words, so you will meet them later.</div>"),
    vowels=VOWELS,
    consonants=CONSONANTS,
    sound_notes=COMMON_NOTES + [
        "<b>a</b> is the short sound in “about”. Every consonant carries it: <span class='nt'>ක</span> = <i>ka</i>.",
        "<b>æ</b> is the ‘a’ in “cat”; <b>ææ</b> is the same sound held longer. <b>ē</b> and <b>ō</b> (with a line on top) are long "
        "‘ay’ and ‘oh’; plain <b>e</b> and <b>o</b> are short.",
        "<b>A dot under t, d, n, l</b> (<i>ṭ, ḍ, ṇ, ḷ</i>) means the tongue curls back; without it, the tongue touches the teeth. "
        "In everyday Sinhala, <i>ṇ</i> and <i>ḷ</i> sound the same as <i>n</i> and <i>l</i>.",
        "<b>nd, mb, ng</b> in words like <i>sanda</i>, <i>amba</i> stand for the half-nasal letters: say the <i>n</i> or <i>m</i> very lightly."],
    phon_explain=("The box marked <i>Sinhala phonetics</i> shows how the sound is built the way Sinhala children learn it, "
                  "for example <span class='nt'>ක් + අ = ක</span>, or a vowel sign (<i>pilla</i>) added to a consonant. "
                  "Sinhala children call each letter by its sound plus <i>-yanna</i>: <span class='nt'>ක</span> is "
                  "<i>kayanna</i>, <span class='nt'>ම</span> is <i>mayanna</i>."),
    standard="standard spoken Sinhala of Sri Lanka",
    hello=[
        ("Who speaks it?", "About <b>17 million people</b> speak Sinhala as their first language, and millions more speak it as a "
                           "second language.<sup>³</sup>"),
        ("Where?", "On the island of <b>Sri Lanka</b> in the Indian Ocean. Sinhala and Tamil are the two official languages of "
                   "Sri Lanka."),
        ("How is it written?", "From <b>left to right</b>, in its own round, curly script. Long ago people wrote on dried "
                               "<b>palm leaves</b> with a sharp metal pen — round letters did not tear the leaf!"),
        ("How many letters?", "The full alphabet, the <span class='nt'>හෝඩිය</span> <i>hōḍiya</i>, has about <b>60 letters</b>. "
                              "This book teaches the <b>50</b> used most."),
        ("Sounds to listen for", "Sinhala has the ‘a’ of “cat” (<span class='nt'>ඇ</span>) and four <b>half-nasal</b> letters: "
                                 "<span class='nt'>ඟ ඬ ඳ ඹ</span> — ‘ng’, ‘nḍ’, ‘nd’ and ‘mb’ said as one sound."),
        ("Did you know?", "Sri Lanka is famous for its <b>tea</b> (<span class='nt'>තේ</span> <i>tē</i>), its coconuts "
                          "(<span class='nt'>පොල්</span> <i>pol</i>) and its crispy <b>hoppers</b> (<span class='nt'>ආප්ප</span> <i>aappa</i>)."),
    ],
    hello_pics=[("teacup", {}), ("si_coconut", {}), ("mosque", {})],
    map=region_map(
        frame=[[78.6, 5.6], [82.9, 9.9]],
        points=dict(colombo=[79.86, 6.93], kandy=[80.64, 7.29], galle=[80.22, 6.03], anuradhapura=[80.40, 8.31]),
        area=None,
        cities=[("colombo", "Colombo", -16, 8, "end", True), ("kandy", "Kandy", 16, 8, "start", False),
                ("galle", "Galle", -14, 8, "end", False), ("anuradhapura", "Anuradhapura", 16, 8, "start", False)],
        label="SRI LANKA", label_at=[80.85, 7.72], marker=[80.7, 7.8],
        caption="The circle shows Sri Lanka on the world map.",
        legend="<b>Color it:</b> the island <b>green</b> · the sea <b>blue</b>. <b>Find it:</b> Sri Lanka is an island shaped "
               "like a drop of water. Colombo ★ is its biggest city, and the capital, Sri Jayawardenepura Kotte, is right next to it. "
               "Sinhala is spoken all over the island, in towns such as Kandy, Galle and Anuradhapura.",
        seas=[("Indian Ocean", 81.7, 5.85), ("Bay of Bengal", 82.15, 9.3), ("Laccadive Sea", 79.15, 7.9)], world_r=10),
    digits=[("0", "බින්දුව", "binduva", "zero"), ("1", "එක", "eka", "one"), ("2", "දෙක", "deka", "two"), ("3", "තුන", "tuna", "three"),
            ("4", "හතර", "hatara", "four"), ("5", "පහ", "paha", "five"), ("6", "හය", "haya", "six"), ("7", "හත", "hata", "seven"),
            ("8", "අට", "aṭa", "eight"), ("9", "නවය", "navaya", "nine")],
    phrases=[("අස්සලාමු අලෛකුම්", "assalaamu alaikum", "Peace be upon you (the Muslim greeting)"),
             ("වලෛකුමුස් සලාම්", "va alaikumus salaam", "And upon you be peace (the reply)"),
             ("මගේ නම …", "magē nama …", "My name is …"),
             ("ස්තූතියි", "stuutiyi", "Thank you"),
             ("ජසාකල්ලාහු ඛයිරන්", "jazaakallaahu khairan", "May Allah reward you with good"),
             ("අම්මා · තාත්තා", "ammaa · taattaa", "Mother · Father"),
             ("අයියා · අක්කා", "ayyaa · akkaa", "Big brother · Big sister"),
             ("ඔව් · නැහැ", "ow · næhæ", "Yes · No"),
             ("මම සිංහල ඉගෙන ගන්නවා!", "mama sinhala igena gannavaa!", "I am learning Sinhala!")],
    cheer=("මාෂා අල්ලාහ්! ඉතා හොඳයි!", "maashaa allaah! itaa hondayi!", "Well done, very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International); official languages from the "
                 "<b>Constitution of Sri Lanka</b>.",
    book_pic=dict(left="අ ආ ඇ", right="ක ග ච"),
    review_note=("Check every letter name (-yanna names, mahaapraana / sanyaka / muurdhaja / dantaja / taaluja), the pilla "
                 "(vowel-sign) names, and these words: ශාඛාව (branch, for ඛ), ඝනකය (cube, for ඝ), දඬුව (stick, for ඬ), "
                 "ෂඩස්‍රය (hexagon, for ෂ), තෛලය (oil, for ඓ), භෝජනය (meal), ඡත්‍රය (umbrella), රථය (cart), ෆුට්බෝල් (football). "
                 "Confirm the Sinhala spellings of the Muslim phrases (අස්සලාමු අලෛකුම්, ජසාකල්ලාහු ඛයිරන්) and the choice of "
                 "letters (50 of the ~60-letter hodiya)."),
    tiles="අආඇකගම", cover_pics=["pineapple", "si_hopper", "teacup", "mosque"], title_size=48,
    speakers_blurb="Sinhala is spoken by about 17 million people as their first language, in Sri Lanka and around the world.",
    sample_words=[("පොල්", "pol", "coconut"), ("සඳ", "sanda", "moon"), ("අඹ", "amba", "mango")],
    keywords=["sinhala alphabet book for kids", "learn sinhala for children", "sinhala letters tracing workbook",
              "sinhala hodiya coloring book", "muslim kids activity book", "islamic coloring book for children",
              "sri lankan heritage language gift"],
))
