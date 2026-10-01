# -*- coding: utf-8 -*-
"""Part 2 — ধ্বনি ও লিপি · Sounds & Script (Ch. 5–7, writing practice 1, checkpoint). Data: data/part2.json."""
import json, os
from engine import page, E, bn, box, h2, tr_line, tr_table, chapter_title, part_opener
from part23 import Flow, quiz_page, writing_pages, h_tr_line, est_text

HERE = os.path.dirname(os.path.abspath(__file__))

def letter_card(L):
    words = "".join('<tr><td class="c-fr">%s</td><td class="c-bp">%s</td><td class="c-ep">%s</td><td class="c-bn">%s</td><td class="c-en">%s</td></tr>' % (
        E(w["fr"]), E(w["bn_pron"]), E(w["en_pron"]), E(w["bn"]), E(w["en"])) for w in L.get("words", []))
    return ('<div style="display:flex;gap:0.16in;align-items:center;margin-bottom:0.06in;">'
            '<div style="width:0.95in;height:0.95in;border-radius:10pt;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;'
            'font-family:Lat;font-weight:700;font-size:34pt;flex:none;">%s</div><div><div style="font-family:BnSans;font-weight:700;font-size:14pt;color:var(--brand);">'
            'নাম: <span class="frw">%s</span> · উচ্চারণ: %s</div><div style="font-size:10.8pt;line-height:1.55;">🔊 %s</div></div></div>'
            '<table class="tr compact"><tbody>%s</tbody></table>%s'
            '<div style="display:flex;gap:0.1in;align-items:center;margin:0.02in 0 0.14in;"><div style="font-family:Lat;font-size:22pt;color:#c9bfa6;letter-spacing:0.12in;">%s</div>'
            '<div style="flex:1;border-bottom:0.75pt solid #cbbf9f;height:0.36in;"></div></div>') % (
        E(L["letter"]), E(L.get("name_fr", "")), E(L.get("name_bn_pron", "")), E(L.get("sound_bn", "")), words,
        ('<div class="small">⚠️ %s</div>' % E(L["watch_bn"])) if L.get("watch_bn") else "", E((L["letter"] + " ") * 3))

def build():
    p = os.path.join(HERE, "data", "part2.json")
    if not os.path.exists(p):
        return
    d = json.load(open(p, encoding="utf-8"))
    page(part_opener("২", "ধ্বনি ও লিপি", "Sounds & Script",
         "এই পর্ব শেষে আপনি যেকোনো ফরাসি শব্দ দেখে পড়তে পারবেন, ধীরে হলেও সঠিকভাবে। প্রথমে ধ্বনি, বাংলার সাথে মিলিয়ে; তারপর ২৬টি অক্ষর ও তাদের "
         "বিশেষ জোট; শেষে রাস্তার সাইনবোর্ড, মেনু আর ফরম পড়ার অনুশীলন।",
         [("অধ্যায় ৫", "ধ্বনির জগৎ"), ("অধ্যায় ৬", "লিপি পরিচয়"), ("অধ্যায় ৭", "প্রথম পড়া"), ("✍️", "লেখার অনুশীলন ১")]),
         anchor="part2", folio=False, bg="#f3f6fb")

    # ---- Ch. 5
    c = d["ch5"]; H = "৫ · ধ্বনির জগৎ"
    f = Flow(H, "ch5")
    f.title(chapter_title(5, "ধ্বনির জগৎ", "The Sound System"))
    f.paras(c.get("intro_bn", []))
    names = {"same": ("✅ বাংলার মতোই", "tip"), "close": ("〰 বাংলার কাছাকাছি", "link"), "new": ("🆕 একেবারে নতুন", "warn")}
    for key in ("same", "close", "new"):
        f.h2(names[key][0])
        for s in c.get("bins", {}).get(key, []):
            ex = s.get("examples", [])
            html = ('<div style="border-left:3pt solid var(--gold);padding:0.03in 0.1in;margin-bottom:0.07in;background:#fff;">'
                    '<div style="font-family:BnSans;font-weight:700;color:var(--brand);">%s</div><div style="font-size:10.4pt;">%s</div>%s</div>') % (
                E(s.get("sound", "")), E(s.get("explain_bn", "")),
                "".join('<div style="font-size:9.8pt;"><span class="frw">%s</span> · %s · <i style="font-family:Lat;color:var(--muted);">%s</i> = %s</div>' % (
                    E(x["fr"]), E(x["bn_pron"]), E(x["en_pron"]), E(x["bn"])) for x in ex))
            f.add(html, 0.42 + est_text(s.get("explain_bn", ""), 80) + 0.2 * len(ex))
    for key, title in (("rounded_bn", "ঠোঁট গোল করা স্বর: ই° ও এ°"), ("r_bn", "গলার র: র়"), ("nasals_bn", "নাকের স্বর: আপনার সুবিধা"),
                       ("silent_bn", "নীরব অক্ষর"), ("liaison_bn", "লিয়েজোঁ ও এলিজিয়োঁ: শব্দের জোড়া লাগা"), ("stress_bn", "ছন্দ ও জোর")):
        if c.get(key):
            f.box("tip" if key != "silent_bn" else "warn", title, c[key])
    if c.get("advantages_bn"):
        f.bullets(c["advantages_bn"], "বাংলাভাষী হিসেবে আপনার সুবিধা", "link")
    if c.get("mistakes_bn"):
        f.bullets(c["mistakes_bn"], "বাংলাভাষীদের সাধারণ ভুল", "warn")
    if c.get("minimal_pairs"):
        f.h2("কাছাকাছি শব্দজোড়া: কান তৈরি করুন")
        for mp in c["minimal_pairs"]:
            f.add('<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.1in;">%s%s</div>%s' % (
                tr_line(mp["a"]), tr_line(mp["b"]), ('<div class="small" style="margin:-0.03in 0 0.08in;">%s</div>' % E(mp.get("note_bn", ""))) if mp.get("note_bn") else ""),
                max(h_tr_line(mp["a"]), h_tr_line(mp["b"])) * 1.35 + 0.2)
    f.flush()

    # ---- Ch. 6
    c = d["ch6"]; H = "৬ · লিপি পরিচয়"
    f = Flow(H, "ch6")
    f.title(chapter_title(6, "লিপি পরিচয়", "The Alphabet"))
    if c.get("intro_bn"):
        f.paras(c["intro_bn"])
    for g in c.get("groups", []):
        f.h2(g.get("title_bn", ""))
        if g.get("intro_bn"):
            f.p(g["intro_bn"])
        for L in g.get("letters", []):
            f.add(letter_card(L), 2.75)
    if c.get("accents"):
        f.h2("ফরাসি চিহ্ন (accents)")
        for a in c["accents"]:
            f.add(('<div style="display:flex;gap:0.12in;align-items:flex-start;margin-bottom:0.04in;"><div style="font-family:Lat;font-weight:700;font-size:22pt;color:var(--accent);width:0.5in;">%s</div>'
                   '<div style="flex:1;"><b>%s</b> · %s</div></div>') % (E(a["mark"]), E(a.get("name_fr", "")), E(a.get("use_bn", ""))), 0.5 + est_text(a.get("use_bn", ""), 70))
            f.table(a.get("examples", []), compact=True, numbered=False)
    if c.get("combinations"):
        f.h2("অক্ষরের জোট: একসাথে এক ধ্বনি")
        for cb in c["combinations"]:
            f.add('<h3><span class="frw" style="font-size:15pt;">%s</span> → %s</h3>' % (E(cb["spelling"]), E(cb.get("sound_bn", ""))), 0.4)
            f.table(cb.get("examples", []), compact=True, numbered=False)
    f.flush()

    # ---- Ch. 7
    c = d["ch7"]; H = "৭ · প্রথম পড়া"
    f = Flow(H, "ch7")
    f.title(chapter_title(7, "প্রথম পড়া", "Reading Drills"))
    f.p("অক্ষর থেকে শব্দ, শব্দ থেকে বাক্য, আর তারপর আসল জীবনের লেখা: রাস্তার সাইন, মেনু, ফরম। প্রথমে উচ্চারণ ঢেকে নিজে পড়ার চেষ্টা করুন, তারপর মিলিয়ে নিন।")
    if c.get("syllables"):
        f.h2("অক্ষরাংশ")
        cells = "".join('<div style="background:#fff;border:0.75pt solid var(--line);border-radius:3pt;padding:0.05in;text-align:center;">'
                        '<div class="frw" style="font-size:14pt;">%s</div><div style="font-size:9.5pt;">%s</div></div>' % (E(s["fr"]), E(s.get("bn_pron", ""))) for s in c["syllables"])
        f.add('<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0.07in;margin-bottom:0.1in;">%s</div>' % cells, 0.6 * ((len(c["syllables"]) + 4) // 5) + 0.1)
    if c.get("words"):
        f.h2("শব্দ"); f.table(c["words"], compact=True, tick=True)
    if c.get("phrases"):
        f.h2("ছোট বাক্য"); f.lines(c["phrases"])
    if c.get("signs"):
        f.h2("রাস্তার সাইনবোর্ড পড়ুন")
        for k in range(0, len(c["signs"]), 2):
            pair = c["signs"][k:k + 2]
            f.add('<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.12in;margin-bottom:0.1in;">%s</div>' % "".join(
                '<div><div style="background:#1f3a8a;color:#fff;font-family:Lat;font-weight:700;letter-spacing:0.02in;font-size:15pt;text-align:center;'
                'padding:0.08in;border-radius:4pt;border:2pt solid #fff;box-shadow:0 0 0 1pt #1f3a8a;">%s</div>'
                '<div style="font-size:9.6pt;margin-top:0.04in;">%s · <i style="font-family:Lat;color:var(--muted);">%s</i><br><b>%s</b> / %s%s</div></div>' % (
                    E(s["fr"]), E(s["bn_pron"]), E(s["en_pron"]), E(s["bn"]), E(s["en"]),
                    (" · 📍 %s" % E(s["where_bn"])) if s.get("where_bn") else "") for s in pair), 1.25)
    for key, title in (("menu", "রেস্তোরাঁর মেনু পড়ুন"), ("form", "একটি ফরম পড়ুন"), ("medicine", "ওষুধের লেবেল")):
        if c.get(key):
            f.h2(title); f.table(c[key], compact=True)
    f.flush()

    writing_pages("✍️ লেখার অনুশীলন ১", "লেখার অনুশীলন ১ — লিপিতে লেখা", d.get("writing1", []), anchor="w1")
    cp = d.get("checkpoint2", {})
    if cp.get("read_aloud"):
        f = Flow("পর্ব ২ · যাচাই")
        f.h2("পর্ব ২ শেষ! জোরে পড়ুন")
        f.p("নিচের লাইনগুলো উচ্চারণ না দেখে জোরে পড়ুন, তারপর উচ্চারণ-লিপির সাথে মিলিয়ে নিন। দশটির মধ্যে আটটি ঠিক হলে আপনি পর্ব ৩-এর জন্য প্রস্তুত।")
        f.lines(cp["read_aloud"])
        f.flush()
    if cp.get("quiz"):
        quiz_page("পর্ব ২ · যাচাই", "পর্ব ২: নিজেকে যাচাই করুন", cp["quiz"])
