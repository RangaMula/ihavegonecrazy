# -*- coding: utf-8 -*-
"""Book 34 - Greek (Greek script, 24 letters). Allamahul Bayan Series. REVIEW DRAFT.
Big letter = capital + small ("Αα"). Pronunciation follows standard Modern Greek."""
from generic import build, letter, section
from maps import region_map

PH = "Greek letter name"
F = "noto-sans-greek"


def Lt(cap, small, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None):
    phon = (f'<div class="nt" style="font-size:20pt">{cap} {small} — «{name}»</div>'
            + (f'<div class="small" style="margin-top:3px">{rule}</div>' if rule else ""))
    return letter(cap + small, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    Lt("Α", "α", "άλφα", "AL-fa", "‘a’ as in “father”", "αστέρι", "a-STE-ree", "star", "star",
       rule="αι says ‘e’: <span class='nt'>και</span> (ke) = “and”"),
    Lt("Β", "β", "βήτα", "VEE-ta", "‘v’ as in “van” (not ‘b’!)", "βάζο", "VA-zo", "jar", "jar",
       rule="For a ‘b’ sound Greek writes <span class='nt'>μπ</span>: <span class='nt'>μπάλα</span> (BA-la) = ball"),
    Lt("Γ", "γ", "γάμμα", "GHA-ma", "a soft, throaty ‘gh’; before e and i it says ‘y’ as in “yes”",
       "γαρύφαλλο", "gha-REE-fa-lo", "carnation (a flower)", "flower",
       rule="γα, γο, γου = gha, gho, ghoo · γε, γι = ye, yi"),
    Lt("Δ", "δ", "δέλτα", "DHEL-ta", "‘th’ as in “this” (written <i>dh</i>)", "δέντρο", "DHEN-dro", "tree", "tree"),
    Lt("Ε", "ε", "έψιλον", "EP-see-lon", "‘e’ as in “bed”", "ελιά", "e-LYA", "olive", "olive"),
    Lt("Ζ", "ζ", "ζήτα", "ZEE-ta", "‘z’ as in “zoo”", "ζυγαριά", "zee-gha-RYA", "scales", "scale"),
    Lt("Η", "η", "ήτα", "EE-ta", "‘ee’ as in “see”", "ήλιος", "EE-lyos", "sun", "sun",
       rule="η, ι, υ, ει and οι all say ‘ee’!"),
    Lt("Θ", "θ", "θήτα", "THEE-ta", "‘th’ as in “think”", "θάλασσα", "THA-la-sa", "sea", "waves"),
    Lt("Ι", "ι", "γιώτα", "YO-ta", "‘ee’ as in “see”", "ιστιοφόρο", "ee-stee-o-FO-ro", "sailing boat", "boat"),
    Lt("Κ", "κ", "κάππα", "KA-pa", "‘k’ as in “kite” (no puff of air)", "καρότο", "ka-RO-to", "carrot", "carrot",
       rule="<span class='nt'>γκ</span> says ‘g’ as in “go”"),
    Lt("Λ", "λ", "λάμδα", "LAM-dha", "‘l’ as in “lemon”", "λεμόνι", "le-MO-nee", "lemon", "lemon"),
    Lt("Μ", "μ", "μι", "mee", "‘m’ as in “moon”", "μήλο", "MEE-lo", "apple", "apple"),
    Lt("Ν", "ν", "νι", "nee", "‘n’ as in “net”", "νερό", "ne-RO", "water", "water",
       rule="<span class='nt'>ντ</span> says ‘d’: <span class='nt'>ντομάτα</span> (do-MA-ta) = tomato"),
    Lt("Ξ", "ξ", "ξι", "ksee", "‘ks’ as in “box”", "ξύλα", "KSEE-la", "firewood logs", "el_logs"),
    Lt("Ο", "ο", "όμικρον", "O-mee-kron", "‘o’ as in “dog” (short and round)", "ομπρέλα", "om-BRE-la", "umbrella", "umbrella",
       rule="ο and ω both say ‘o’ · ου says ‘oo’"),
    Lt("Π", "π", "πι", "pee", "‘p’ as in “pen” (no puff of air)", "πόρτα", "POR-ta", "door", "door"),
    Lt("Ρ", "ρ", "ρο", "ro", "a quick, tapped ‘r’", "ρόδι", "RO-dhee", "pomegranate", "pomegranate"),
    Lt("Σ", "σ", "σίγμα", "SEEGH-ma", "‘s’ as in “sun”", "σταφύλι", "sta-FEE-lee", "grapes", "grapes",
       note="Small sigma has two shapes: <span class='nt'>σ</span> inside a word and <span class='nt'>ς</span> at the end, as in "
            "<span class='nt'>ήλιος</span>."),
    Lt("Τ", "τ", "ταυ", "taf", "‘t’ as in “top” (no puff of air)", "τούβλο", "TOO-vlo", "brick", "brick",
       rule="<span class='nt'>τσ</span> = ts · <span class='nt'>τζ</span> = dz"),
    Lt("Υ", "υ", "ύψιλον", "EEP-see-lon", "‘ee’ as in “see”", "υδρόγειος", "ee-DHRO-yee-os", "globe of the Earth", "globe",
       rule="αυ = av/af · ευ = ev/ef · ου = oo"),
    Lt("Φ", "φ", "φι", "fee", "‘f’ as in “fan”", "φεγγάρι", "fen-GA-ree", "moon", "moon"),
    Lt("Χ", "χ", "χι", "hee", "a breathy ‘h’ from the back of the throat, like ‘ch’ in Scottish “loch”",
       "χαρταετός", "har-ta-e-TOS", "kite", "kite"),
    Lt("Ψ", "ψ", "ψι", "psee", "‘ps’ as in “cups”", "ψωμί", "pso-MEE", "bread", "el_bread"),
    Lt("Ω", "ω", "ωμέγα", "o-ME-gha", "‘o’ as in “dog” (the same sound as ο)", "ώρα", "O-ra", "hour, time", "clock",
       note="Omega is the last letter of the alphabet. <span class='nt'>Τι ώρα είναι;</span> means “What time is it?”"),
]

LANG = build(dict(
    code="el", folder="book-34-greek", series_no=34, isbn="", draft=True,
    name="Greek", native="ελληνικά", native_tr="e-lee-nee-KA", name_word="όνομα", write_word="γράψε",
    title_native="Το πρώτο μου αλφάβητο", title_letters="ΑαΒβΓγ", belongs_native="Αυτό το βιβλίο ανήκει σε",
    belongs_pic="olive", alphabet_native="το αλφάβητο", numbers_native="οι αριθμοί", numbers_tr="ee a-reeth-MEE",
    phrases_native="Πρώτες λέξεις",
    fonts=[("Noto Sans", w, "normal", f"{F}-{w}-normal.woff2", "U+0370-03FF,U+1F00-1FFF") for w in (400, 700, 800)],
    disp_family="Noto Sans", text_family="Noto Sans",
    glyph_font=[f"{F}-800-normal.woff2", "baloo-2-latin-800-normal.woff2"],
    font_credit="Noto Sans (Greek)",
    extra_css=".nt,.ntd,.lp-name{font-family:'Noto Sans','Nunito',sans-serif}",
    phon_feature="each letter’s Greek name (Α «άλφα», Β «βήτα», Γ «γάμμα»…)",
    sections=[section(LETTERS, native="το αλφάβητο", native_tr="to al-FA-vee-to — “the alphabet”",
                      chart_cols=6, warmup_cols=6,
                      intro_html="""<p>Greek has <b>24 letters</b>. Many of them look like English letters, but be careful: some
look the same and say something different! <span class="nt">Β</span> says ‘v’, <span class="nt">Η</span> says ‘ee’, <span class="nt">Ρ</span> says ‘r’
and <span class="nt">Χ</span> says a breathy ‘h’.</p>
<div class="box" style="margin:0.1in 0"><h3>Five vowel sounds</h3>Greek speaks only five vowel sounds — <i>a, e, ee, o, oo</i> — but it
writes some of them in more than one way: <span class="nt">η, ι, υ</span> all say ‘ee’, and <span class="nt">ο, ω</span> both say ‘o’.</div>
<div class="box" style="margin:0.1in 0"><h3>The little stress mark</h3>Most Greek words carry an accent mark ( ΄ ) over one vowel:
<span class="nt">μήλο</span>. It shows which part of the word to say a little louder: <i>MEE-lo</i>.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side:
<span class="nt">Αα</span>. Color both!</div>""")],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>MEE-lo</i> means “say MEE a little louder”. "
        "In Greek writing, the accent mark ( ΄ ) shows the same thing.",
        "<b>dh</b> is the soft ‘th’ in “this” (letter <span class='nt'>δ</span>); <b>th</b> is the ‘th’ in “think” (letter <span class='nt'>θ</span>).",
        "<b>gh</b> is a soft, throaty ‘g’ (letter <span class='nt'>γ</span>); <b>h</b> is a breathy ‘h’ from the back of the throat "
        "(letter <span class='nt'>χ</span>).",
        "<b>ee</b> as in “see”, <b>oo</b> as in “moon”; <b>e</b> as in “bed”, <b>o</b> as in “dog”, <b>a</b> as in “father”."],
    phon_explain="The box marked <i>Greek letter name</i> shows the letter’s name written in Greek (Α is «άλφα», Β is «βήτα»…) "
                 "and, for some letters, a letter pair that makes a new sound.",
    standard="standard Modern Greek as spoken in Greece",
    hello=[
        ("Who speaks it?", "About <b>13 million people</b> speak Greek as their first language.<sup>³</sup>"),
        ("Where?", "In <b>Greece</b> and <b>Cyprus</b>, and in Greek families all around the world."),
        ("How is it written?", "In the <b>Greek alphabet</b>, from <b>left to right</b>, with capital and small letters."),
        ("How many letters?", "<b>24 letters</b>, from <span class='nt'>Α α</span> (alpha) to <span class='nt'>Ω ω</span> (omega)."),
        ("Did you know?", "The English word <b>“alphabet”</b> comes from the first two Greek letters: "
                          "<span class='nt'>άλφα</span> (alpha) + <span class='nt'>βήτα</span> (beta)!"),
        ("Letters in maths!", "Scientists use Greek letters every day. The letter <span class='nt'>π</span> (pi) helps us measure circles."),
    ],
    hello_pics=[("olive", {}), ("waves", {}), ("pomegranate", {})],
    map=region_map(frame=[[19.2, 34.3], [29.8, 42.3]],
                   points=dict(athens=[23.73, 37.98], thessaloniki=[22.94, 40.64], heraklion=[25.13, 35.34],
                               patras=[21.73, 38.25], rhodes=[28.22, 36.43]),
                   area=None,
                   cities=[("athens", "Athens", 14, 26, "start", False), ("thessaloniki", "Thessaloniki", 14, -8, "start", False),
                           ("heraklion", "Heraklion", 0, -16, "middle", False), ("patras", "Patras", -14, -8, "end", False),
                           ("rhodes", "Rhodes", 0, 34, "middle", False)],
                   label="GREECE", label_at=[22.2, 39.4], marker=[25.0, 38.0],
                   caption="The circle shows Greece on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the seas <b>blue</b>. <b>Find it:</b> Greek is spoken in Athens, "
                          "Thessaloniki, Patras and on thousands of islands like Crete (Heraklion) and Rhodes. It is also spoken "
                          "on the island of <b>Cyprus</b>, further east.",
                   seas=[("Aegean Sea", 25.3, 39.2), ("Mediterranean Sea", 25.0, 34.7), ("Ionian Sea", 20.4, 37.0)], world_r=13),
    digits=[("0", "μηδέν", "mee-DHEN", "zero"), ("1", "ένα", "E-na", "one"), ("2", "δύο", "DHEE-o", "two"),
            ("3", "τρία", "TREE-a", "three"), ("4", "τέσσερα", "TE-se-ra", "four"), ("5", "πέντε", "PEN-de", "five"),
            ("6", "έξι", "E-ksee", "six"), ("7", "επτά", "ep-TA", "seven"), ("8", "οκτώ", "ok-TO", "eight"),
            ("9", "εννέα", "e-NE-a", "nine")],
    phrases=[("Ασσαλάμου αλάικουμ", "as-sa-LA-moo a-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Ουά αλάικουμ ασσαλάμ", "wa a-LAY-koom as-sa-LAM", "And upon you be peace (the reply)"),
             ("Γεια σου!", "YA soo", "Hello!"),
             ("Με λένε …", "me LE-ne …", "My name is …"),
             ("Ευχαριστώ · Τζαζάκαλλαχου χάιραν", "ef-ha-ree-STO · ja-ZA-ka-la-hoo HAY-ran",
              "Thank you · May Allah reward you with good"),
             ("μαμά · μπαμπάς", "ma-MA · ba-BAS", "Mother · Father"),
             ("αδερφός · αδερφή", "a-dher-FOS · a-dher-FEE", "Brother · Sister"),
             ("ναι · όχι", "ne · O-hee", "Yes · No"),
             ("Μαθαίνω ελληνικά!", "ma-THE-no e-lee-nee-KA", "I am learning Greek!")],
    cheer=("Μασαλλάχ! Μπράβο!", "ma-sha-LAH! BRA-vo!", "Mashallah! Well done!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="Α Β Γ", right="Δ Ε Ζ"),
    review_note=("Check: the Greek spellings of the Islamic phrases (Ασσαλάμου αλάικουμ, Ουά αλάικουμ ασσαλάμ, "
                 "Τζαζάκαλλαχου χάιραν, Μασαλλάχ); 'Αυτό το βιβλίο ανήκει σε' on the name plate (natural Greek may prefer "
                 "'ανήκει στον/στην'); the number words 7–9 (formal επτά/οκτώ/εννέα vs everyday εφτά/οχτώ/εννιά); "
                 "word choices γαρύφαλλο (carnation, shown as a generic flower), ξύλα (firewood), ώρα (hour, shown as a clock) "
                 "and υδρόγειος (globe); stress capitals in every transliteration."),
    tiles="ΑΒΓΔΣΩ", cover_pics=["olive", "kite", "pomegranate", "sun"], title_size=50,
    speakers_blurb="Greek is spoken by about 13 million people in Greece, Cyprus and around the world.",
    sample_words=[("ήλιος", "EE-lyos", "sun"), ("ελιά", "e-LYA", "olive"), ("χαρταετός", "har-ta-e-TOS", "kite")],
    keywords=["greek alphabet book for kids", "learn greek for children", "greek letters coloring book",
              "greek alphabet tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual greek english toddlers"],
))
