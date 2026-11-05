# -*- coding: utf-8 -*-
"""Book 81 - Portuguese (Latin script: 26 letters + Ç, the til and the pairs CH LH NH). Allamahul Bayan Series.
REVIEW DRAFT. Modelled on languages/es.py; pronunciation follows Brazilian Portuguese."""
from generic import build, letter, section, fontset
from maps import region_map

PH = "Portuguese letter name"


def L(big, name, name_tr, sound, word, tr, meaning, pic, args=None, note=None, rule=None, show=None):
    """big = what is drawn (\"Aa\", \"Ch ch\"); show = the letter forms in the name box (default: capital + small)."""
    show = show or f"{big[0]} {big[1:].strip()}"
    phon = (f'<div class="nt" style="font-size:20pt">{show} — «{name}»</div>'
            + (f'<div class="small">{rule}</div>' if rule else ""))
    return letter(big, name, name_tr, sound, word, tr, meaning, pic, phon, PH, args, note)


LETTERS = [
    L("Aa", "a", "ah", "‘a’ as in “father”", "abacaxi", "ah-bah-kah-SHEE", "pineapple", "pineapple"),
    L("Bb", "bê", "beh", "‘b’ as in “ball”", "bola", "BOH-lah", "ball", "ball"),
    L("Cc", "cê", "seh", "‘k’ before a, o, u; ‘s’ before e, i", "casa", "KAH-zah", "house", "house",
      rule="ca, co, cu = ka, ko, ku · ce, ci = se, si"),
    L("Dd", "dê", "deh", "‘d’ as in “day” — but before an ‘i’ sound Brazilians say ‘j’ as in “jeep”", "damasco", "dah-MAHS-koo",
      "apricot", "hy_apricot", rule="dia (day) = JEE-ah · the name comes from the city of Damascus!"),
    L("Ee", "é", "eh", "‘e’ as in “bed”, or ‘ay’ as in “say”; at the end of a word it often says ‘ee’", "estrela", "es-TREH-lah",
      "star", "star"),
    L("Ff", "efe", "EH-fee", "‘f’ as in “fan”", "flor", "flohr", "flower", "flower"),
    L("Gg", "gê", "zheh", "‘g’ as in “go” before a, o, u; ‘zh’ (the ‘s’ in “measure”) before e, i", "globo", "GLOH-boo",
      "globe", "globe", rule="ga, go, gu = ga, go, gu · ge, gi = zhe, zhee"),
    L("Hh", "agá", "ah-GAH", "silent! H makes no sound at the start of a word", "helicóptero", "eh-lee-KOP-teh-roo",
      "helicopter", "kk_helicopter",
      note="H is silent: <i>helicóptero</i> sounds like “eh-lee-KOP-teh-roo”. After C, L and N it makes new sounds — see the letter pairs!"),
    L("Ii", "i", "ee", "‘ee’ as in “see”", "ilha", "EE-lyah", "island", "dv_island"),
    L("Jj", "jota", "ZHOH-tah", "‘zh’ — the soft sound of ‘s’ in “measure”", "janela", "zhah-NEH-lah", "window", "window"),
    L("Kk", "cá", "kah", "‘k’ as in “kite” — used only in borrowed words", "kiwi", "KEE-wee", "kiwi fruit", "pt_kiwi"),
    L("Ll", "ele", "EH-lee", "‘l’ as in “lamp”; at the end of a syllable it sounds like ‘w’", "lua", "LOO-ah", "moon", "moon",
      rule="sol (sun) = SOW · Brasil = brah-ZEEW"),
    L("Mm", "eme", "EH-mee", "‘m’ as in “moon”", "mesquita", "mes-KEE-tah", "mosque", "mosque"),
    L("Nn", "ene", "EH-nee", "‘n’ as in “net”; after a vowel it makes the vowel nasal (through the nose)", "nuvem", "NOO-veng",
      "cloud", "clouds"),
    L("Oo", "ó", "aw", "‘o’ as in “go” or ‘aw’ as in “saw”; at the end of a word it says ‘oo’", "ovo", "OH-voo", "egg", "egg"),
    L("Pp", "pê", "peh", "‘p’ as in “pen” (no puff of air)", "pipa", "PEE-pah", "kite", "kite"),
    L("Qq", "quê", "keh", "‘k’ — always written “qu”", "queijo", "KAY-zhoo", "cheese", "dv_cheese",
      rule="que, qui = ke, ki (the u is silent) · qua = kwa"),
    L("Rr", "erre", "EH-hee", "at the start of a word (and as rr): a breathy ‘h’; between vowels: a quick tapped ‘r’",
      "relógio", "heh-LOH-zhyoo", "clock", "clock", rule="rua (street) = HOO-ah · caro (dear) = KAH-roo · carro (car) = KAH-hoo"),
    L("Ss", "esse", "EH-see", "‘s’ as in “sun”; between two vowels it buzzes like ‘z’", "sol", "sow", "sun", "sun",
      rule="sapo = SAH-poo · casa = KAH-zah · ss is always ‘s’"),
    L("Tt", "tê", "teh", "‘t’ as in “top” — but before an ‘i’ sound Brazilians say ‘ch’ as in “cheese”", "tomate", "toh-MAH-chee",
      "tomato", "tomato", rule="ti, and te at the end of a word = chee"),
    L("Uu", "u", "oo", "‘oo’ as in “moon”", "uva", "OO-vah", "grapes", "grapes"),
    L("Vv", "vê", "veh", "‘v’ as in “van”", "vela", "VEH-lah", "candle", "ug_candle"),
    L("Ww", "dáblio", "DAH-blee-oo", "‘w’ as in “water” (or ‘v’) — used only in borrowed words", "waffle", "WAH-fow", "waffle",
      "pt_waffle"),
    L("Xx", "xis", "sheesh", "usually ‘sh’ as in “ship” — but X has four sounds!", "xícara", "SHEE-kah-rah", "cup", "teacup",
      rule="xícara (sh) · táxi (ks) · próximo (s) · exame (z)"),
    L("Yy", "ípsilon", "EEP-see-lohn", "‘ee’ or ‘y’ as in “yes” — used only in borrowed words and names", "yakisoba", "yah-kee-SOH-bah",
      "yakisoba (a noodle dish loved in Brazil)", "dz_bowl"),
    L("Zz", "zê", "zeh", "‘z’ as in “zoo”; at the end of a word it sounds like ‘s’", "zabumba", "zah-BOOM-bah",
      "zabumba (a big Brazilian drum)", "dz_drum"),
]

SPECIAL = [
    L("Çç", "cê-cedilha", "seh seh-DEE-lyah", "‘s’ as in “sun” — the little tail (the <i>cedilha</i>) turns hard C into ‘s’",
      "maçã", "mah-SAHN", "apple", "apple", rule="ça, ço, çu = sa, so, su · ce, ci never need the tail",
      note="Ç never starts a word. Find it in the middle of <i>maçã</i>!"),
    L("Ãã", "a com til", "ah kohn CHEEW", "‘ah’ said through the nose — the wavy <i>til</i> (~) makes a vowel nasal", "pão", "pown",
      "bread", "ru_bread", rule="ão = own · ã = ahn · mãe (mother) = mynh",
      note="Ã hardly ever starts a word. Find it in <i>pão</i>!"),
    L("Õõ", "o com til", "oh kohn CHEEW", "‘oh’ said through the nose — mostly in <b>õe</b>, the ending of many plural words", "limões",
      "lee-MOYNSS", "lemons", "lemon", rule="limão (one lemon) · limões (lemons)",
      note="Õ never starts a word. Find it in <i>limões</i>!"),
    L("Ch ch", "cê-agá", "seh ah-GAH", "‘sh’ as in “ship”", "chave", "SHAH-vee", "key", "si_key", show="Ch ch",
      note="<b>Ch</b> is two letters that make one sound."),
    L("Lh lh", "ele-agá", "EH-lee ah-GAH", "‘ly’ as in “million”", "folha", "FOH-lyah", "leaf", "ms_leaf", show="Lh lh",
      note="<b>Lh</b> never starts a Portuguese word. Find it inside <i>folha</i>!"),
    L("Nh nh", "ene-agá", "EH-nee ah-GAH", "‘ny’ as in “canyon” — like Spanish Ñ", "castanha", "kahs-TAH-nyah",
      "nut (a Brazil nut or chestnut)", "walnut", show="Nh nh",
      note="<b>Nh</b> hardly ever starts a word. Find it inside <i>castanha</i>!"),
]

LANG = build(dict(
    code="pt", folder="book-81-portuguese", series_no=81, isbn="", draft=True,
    name="Portuguese", native="português", native_tr="por-too-GAYS", name_word="nome", write_word="escreva",
    letters_word="Letters & Sounds",
    title_native="Meu primeiro alfabeto em português", title_letters="AaBbÇç", belongs_native="Este livro é de",
    belongs_pic="pineapple", alphabet_native="o alfabeto", numbers_native="os números", numbers_tr="ooz NOO-meh-roos",
    phrases_native="Primeiras palavras",
    fonts=fontset("Baloo 2", "baloo-2-latin", "Nunito", "nunito-latin") + fontset("Baloo 2", "baloo-2-latin-ext", "Nunito", "nunito-latin-ext"),
    disp_family="Baloo 2", text_family="Nunito",
    glyph_font=["baloo-2-latin-800-normal.woff2", "baloo-2-latin-ext-800-normal.woff2"],
    font_credit="Baloo 2",
    phon_feature="each letter’s Portuguese name (A «a», B «bê», C «cê»…)",
    sections=[
        section(LETTERS, native="o alfabeto", native_tr="oo ahw-fah-BEH-too — “the alphabet”", chart_cols=7, warmup_cols=6,
                intro_html="""<p>Portuguese uses the same <b>26 letters</b> as English. K, W and Y are only used in borrowed words and names.</p>
<div class="box" style="margin:0.1in 0"><h3>Sounds from Brazil</h3>The sound guides in this book follow <b>Brazilian Portuguese</b>, the way most
Portuguese speakers talk. In Portugal some letters sound a little different.</div>
<div class="box" style="margin:0.1in 0"><h3>Vowels that change</h3>Portuguese vowels can be <b>open</b> (é as in “bed”, ó as in “saw”) or
<b>closed</b> (ê as in “say”, ô as in “go”), and at the end of a word <b>o</b> often says “oo” and <b>e</b> says “ee”.</div>
<div class="box"><h3>Big and small</h3>Each page shows the <b>capital letter</b> and the <b>small letter</b> side by side: <b>Aa</b>. Color both!</div>"""),
        section(SPECIAL, label="SPECIAL", chip="MARKS & PAIRS", title="Marks and Pairs", native="sinais e dígrafos",
                native_tr="see-NAYS ee DEE-grah-foos — “marks and letter pairs”", chart_title="marks and pairs", chart_cols=6,
                warmup_title="the marks and pairs", warmup_cols=3,
                intro_html="""<p>Portuguese adds little <b>marks</b> to some letters, and joins some letters into <b>pairs</b> that make one sound.</p>
<div class="box" style="margin:0.1in 0"><h3>The cedilha: Ç</h3>A little tail under C makes it say “s” before a, o, u: <i>maçã</i> (apple), <i>açúcar</i> (sugar).</div>
<div class="box" style="margin:0.1in 0"><h3>The til: Ã Õ</h3>The wavy line (~) means “say it through your nose”: <i>pão</i> (bread), <i>mãe</i> (mother), <i>limões</i> (lemons).</div>
<div class="box" style="margin:0.1in 0"><h3>Accents</h3><b>á é í ó ú</b> show the loud syllable and an open vowel: <i>café</i>, <i>avó</i> (grandma).
<b>â ê ô</b> show a closed vowel: <i>você</i> (you), <i>avô</i> (grandpa). <b>à</b> means “to the”.</div>
<div class="box"><h3>Letter pairs</h3><b>ch</b> says “sh”, <b>lh</b> says “ly”, <b>nh</b> says “ny”. Each pair makes <b>one</b> sound.</div>"""),
    ],
    sound_notes=[
        "<b>CAPITALS</b> in the pronunciation show the stressed syllable: <i>KAH-zah</i> means “say KAH a little louder”.",
        "<b>zh</b> is the soft sound in the middle of “measure” (the Portuguese J).",
        "<b>ng</b>, <b>n</b> or <b>own</b> after a vowel means the vowel is said through the nose: <i>pão</i> = pown, <i>nuvem</i> = NOO-veng.",
        "<b>h</b> in the pronunciation is a breathy ‘h’ (the sound of R at the start of a word); the letter H itself is silent.",
        "Sounds follow Brazilian Portuguese; in Portugal, T and D stay ‘t’ and ‘d’, and final -e is very short."],
    phon_explain="The box marked <i>Portuguese letter name</i> shows the name Portuguese-speaking children use for the letter "
                 "(B is «bê», H is «agá»…) and any spelling rule that changes its sound.",
    standard="Brazilian Portuguese",
    hello=[
        ("Who speaks it?", "More than <b>250 million people</b> speak Portuguese — one of the most spoken languages in the world.<sup>³</sup>"),
        ("Where?", "In <b>Brazil</b> and <b>Portugal</b>, and in <b>Angola</b>, <b>Mozambique</b>, <b>Cape Verde</b>, <b>Guinea-Bissau</b>, "
                   "<b>São Tomé and Príncipe</b> and <b>Timor-Leste</b>."),
        ("How is it written?", "In the <b>Latin alphabet</b>, from <b>left to right</b>, with <b>ç</b> and accent marks: á â ã à é ê í ó ô õ ú."),
        ("How many letters?", "<b>26 letters</b>, the same as English, plus <b>Ç</b>, the nasal <b>til</b> (ã õ) and the pairs "
                              "<b>ch</b>, <b>lh</b> and <b>nh</b>."),
        ("The biggest family", "<b>Brazil</b> is the largest Portuguese-speaking country: more than 200 million people there speak it."),
        ("Did you know?", "Portuguese has hundreds of words from Arabic, from the time of al-Andalus: <i>azeite</i> (olive oil, from "
                          "<i>az-zayt</i>), <i>alface</i> (lettuce), <i>açúcar</i> (sugar), <i>arroz</i> (rice) and <i>oxalá</i> "
                          "(“if Allah wills”)."),
    ],
    hello_pics=[("pineapple", {}), ("kite", {}), ("mosque", {})],
    map=region_map(frame=[[-75.0, -35.0], [-33.0, 7.0]],
                   points=dict(brasilia=[-47.88, -15.79], manaus=[-60.02, -3.12], salvador=[-38.50, -12.97],
                               rio=[-43.17, -22.91], saopaulo=[-46.63, -23.55], recife=[-34.88, -8.05]),
                   area=None,
                   cities=[("brasilia", "Brasília", 18, 8, "start", True), ("manaus", "Manaus", 14, -10, "start", False),
                           ("salvador", "Salvador", -14, 8, "end", False), ("rio", "Rio de Janeiro", 14, 22, "start", False),
                           ("saopaulo", "São Paulo", -14, 8, "end", False), ("recife", "Recife", -14, 8, "end", False)],
                   label="BRAZIL", label_at=[-54.0, -9.0], marker=[-52.0, -12.0],
                   caption="The circle shows Brazil on the world map.",
                   legend="<b>Color it:</b> the land <b>green</b> · the ocean <b>blue</b>. <b>Find it:</b> Portuguese is spoken in Brasília "
                          "(the star), Manaus by the Amazon river, Recife, Salvador, Rio de Janeiro and São Paulo — and across the ocean in "
                          "Portugal, Angola and Mozambique.",
                   seas=[("Atlantic Ocean", -40.0, -27.0)], world_r=22),
    digits=[("0", "zero", "ZEH-roo", "zero"), ("1", "um", "oong", "one"), ("2", "dois", "doys", "two"), ("3", "três", "trehs", "three"),
            ("4", "quatro", "KWAH-troo", "four"), ("5", "cinco", "SEEN-koo", "five"), ("6", "seis", "says", "six"),
            ("7", "sete", "SEH-chee", "seven"), ("8", "oito", "OY-too", "eight"), ("9", "nove", "NOH-vee", "nine")],
    phrases=[("Assalamu alaikum", "as-sah-LAH-moo ah-LAY-koom", "Peace be upon you (the Muslim greeting)"),
             ("Wa alaikum assalam", "wah ah-LAY-koom as-sah-LAHM", "And peace be upon you (the reply)"),
             ("Olá! · Oi!", "oh-LAH · oy", "Hello! · Hi!"),
             ("Meu nome é …", "MEH-oo NOH-mee eh …", "My name is …"),
             ("Obrigado! · Obrigada!", "oh-bree-GAH-doo · oh-bree-GAH-dah", "Thank you! (said by a boy · by a girl)"),
             ("Jazakallahu khairan", "jah-zah-KAH-lah-hoo KHAI-rahn", "May Allah reward you with good"),
             ("mamãe · papai", "mah-MYNH · pah-PAI", "Mother · Father"),
             ("irmão · irmã", "eer-MOWN · eer-MAHN", "Brother · Sister"),
             ("sim · não", "seeng · nown", "Yes · No"),
             ("Estou aprendendo português!", "es-TOH ah-pren-DEN-doo por-too-GAYS", "I am learning Portuguese!")],
    cheer=("Mashallah! Muito bem!", "MAH-shah-lah! MWEEN-too beng!", "Mashallah! Very good!"),
    facts_source="speaker numbers from <b>Ethnologue</b> (SIL International), rounded.",
    book_pic=dict(left="A B C", right="Ç Ã Õ"),
    review_note="Check the Brazilian sound guides (especially <i>nuvem</i>, <i>pão</i>, <i>mamãe</i>, <i>limões</i>, final -l as ‘w’), "
                "the letter names (dáblio, ípsilon; some schools say «guê» for G and «quê» for K/Q), the choice of borrowed words for "
                "K, W and Y (<i>kiwi</i>, <i>waffle</i>, <i>yakisoba</i>) and whether the extra section (Ç Ã Õ CH LH NH) should stay.",
    tiles="AÇÃBEZ", cover_pics=["pineapple", "kite", "mosque", "apple"], title_size=46,
    speakers_blurb="Portuguese is spoken by more than 250 million people in Brazil, Portugal, Africa and around the world.",
    sample_words=[("lua", "LOO-ah", "moon"), ("maçã", "mah-SAHN", "apple"), ("janela", "zhah-NEH-lah", "window")],
    keywords=["portuguese alphabet book for kids", "learn brazilian portuguese for children", "portuguese alfabeto coloring",
              "portuguese letters tracing workbook", "muslim kids activity book", "islamic coloring book for children",
              "bilingual portuguese english toddlers"],
))
