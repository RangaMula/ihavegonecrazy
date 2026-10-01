# -*- coding: utf-8 -*-
"""Part 5 — ভাষাটি ব্যবহার করুন · Use the Language (Ch. 13–16, writing practice 3). Data: data/part5.json; Ch. 16 in ch16.py."""
import json, os
from engine import page, E, bn, box, h2, tr_line, tr_table, chapter_title, part_opener, EXTRA_CSS
from part23 import Flow, quiz_page, writing_pages, h_tr_line, est_text
import ch16

HERE = os.path.dirname(os.path.abspath(__file__))

CSS = """
.dl{display:flex;margin:0 0 0.06in;}
.dl.you{justify-content:flex-end;}
.dl .bub{max-width:82%;border-radius:8pt;padding:0.05in 0.1in;background:#fff;border:0.75pt solid var(--line);}
.dl.you .bub{background:var(--accent-l);border-color:#c5d0ea;}
.dl .who{font-family:BnSans;font-weight:600;font-size:8pt;color:var(--gold);}
.dl.you .who{color:var(--accent);}
.dl .f{font-family:Lat,LatX;font-weight:700;color:var(--accent);font-size:10.6pt;line-height:1.3;}
.dl .pr{font-size:8.6pt;line-height:1.3;color:var(--muted);}
.dl .pr i{font-family:Lat;}
.dl .b{font-size:9.4pt;line-height:1.35;}
.dl .b .en{font-family:Lat;color:var(--muted);font-size:8.5pt;}
"""

def bubble(ln):
    you = ln.get("you")
    return ('<div class="dl%s"><div class="bub"><div class="who">%s</div><div class="f">%s</div><div class="pr">%s · <i>%s</i></div>'
            '<div class="b">%s <span class="en">/ %s</span></div></div></div>') % (
        " you" if you else "", E(("আপনি (" + ln.get("who", "") + ")") if you else ln.get("who", "")),
        E(ln["fr"]), E(ln["bn_pron"]), E(ln["en_pron"]), E(ln["bn"]), E(ln["en"]))

def h_bubble(ln):
    return 0.42 + 0.17 * (len(ln["fr"]) // 55) + 0.15 * (len(ln["bn_pron"] + ln["en_pron"]) // 70) + 0.16 * (len(ln["bn"] + ln["en"]) // 70)

QURAN_HADITH = [
    {"fr": "Ô hommes ! Nous vous avons créés d'un mâle et d'une femelle, et Nous avons fait de vous des nations et des tribus, pour que vous vous entre-connaissiez.",
     "ar": "يَا أَيُّهَا النَّاسُ إِنَّا خَلَقْنَاكُم مِّن ذَكَرٍ وَأُنثَىٰ وَجَعَلْنَاكُمْ شُعُوبًا وَقَبَائِلَ لِتَعَارَفُوا",
     "bn": "হে মানুষ! আমি তোমাদের সৃষ্টি করেছি এক পুরুষ ও এক নারী থেকে, আর তোমাদের বানিয়েছি বিভিন্ন জাতি ও গোত্র, যাতে তোমরা একে অপরকে চিনতে পারো।",
     "source": "সূরা আল-হুজুরাত ৪৯:১৩ · ফরাসি অনুবাদ: মুহাম্মদ হামিদুল্লাহ",
     "note_bn": "এই আয়াতেই এই বইয়ের মূল কথা: ভাষা শেখা মানে মানুষকে চেনা।"},
    {"fr": "Ton sourire à ton frère est une aumône.",
     "ar": "تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ",
     "bn": "তোমার ভাইয়ের দিকে তাকিয়ে তোমার হাসি তোমার জন্য সদকা।",
     "source": "জামে আত-তিরমিযী ১৯৫৬",
     "note_bn": "যেকোনো ভাষায় প্রথম যে ‘শব্দ’ সবাই বোঝে, তা হলো হাসি।"},
]

def build():
    EXTRA_CSS.append(CSS)
    p = os.path.join(HERE, "data", "part5.json")
    d = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    page(part_opener("৫", "ভাষাটি ব্যবহার করুন", "Use the Language",
         "এবার মঞ্চে আপনি। বিমানবন্দর, ট্যাক্সি, হোটেল, ডাক্তারখানা, চাকরির সাক্ষাৎকার: ২০টি বাস্তব সংলাপে আপনি নিজেই একটি চরিত্র। "
         "তারপর প্রথম পূর্ণ পাঠ, সাহিত্যের স্বাদ, আর নিজের বিশ্বাসের পরিচয় দেওয়ার ভাষা।",
         [("অধ্যায় ১৩", "২০টি বাস্তব সংলাপ"), ("অধ্যায় ১৪", "প্রথম পাঠ"), ("অধ্যায় ১৫", "সাহিত্যের প্রথম স্বাদ"),
          ("অধ্যায় ১৬", "আমার বিশ্বাসের পরিচয়"), ("✍️", "লেখার অনুশীলন ৩")]),
         anchor="part5", folio=False, bg="#f3f6fb")

    # ---- Ch. 13 dialogues: each scene = page 1 dialogue, page 2 key phrases + culture + your turn
    dl = d.get("dialogues", [])
    if dl:
        page(chapter_title(13, "২০টি বাস্তব সংলাপ", "20 Real-Life Conversations") + """
<p class="lead">প্রতিটি সংলাপে নীল বুদবুদের মানুষটি <b>আপনি</b>। প্রথমে পুরো সংলাপ জোরে পড়ুন, তারপর শুধু নিজের অংশ বলুন, আর শেষে বই বন্ধ করে
দৃশ্যটি অভিনয় করুন। পরের পাতায় পাবেন মূল বাক্যাংশ, সংস্কৃতির টীকা আর আপনার পালা।</p>""" +
             '<div class="cards">' + "".join('<div class="card"><div class="ct">%s · %s</div><div class="cb" style="font-family:Lat;font-style:italic;">%s</div></div>' % (
                 bn(x["no"]), E(x["title_bn"]), E(x["title_en"])) for x in dl[:10]) + '</div>',
             head="১৩ · সংলাপ", anchor="ch13")
        page('<div class="cards">' + "".join('<div class="card"><div class="ct">%s · %s</div><div class="cb" style="font-family:Lat;font-style:italic;">%s</div></div>' % (
            bn(x["no"]), E(x["title_bn"]), E(x["title_en"])) for x in dl[10:]) + '</div>' +
             box("tip", "অভিনয়ের কৌশল", "<p>বন্ধু বা পরিবারের কাউকে অন্য চরিত্রটি পড়তে বলুন। তারা ফরাসি না জানলেও বাংলা উচ্চারণ-লিপি দেখে পড়তে পারবেন!</p>"),
             head="১৩ · সংলাপ")
        for x in dl:
            H = "সংলাপ %s · %s" % (bn(x["no"]), x["title_bn"])
            f = Flow(H)
            f.add('<div style="display:flex;gap:0.12in;align-items:center;margin-bottom:0.06in;"><div style="background:var(--brand);color:#fff;font-family:BnSans;font-weight:700;'
                  'border-radius:10pt;padding:0.03in 0.14in;">দৃশ্য %s</div><div style="font-family:BnSans;font-weight:700;color:var(--brand);font-size:15pt;line-height:1.3;">%s '
                  '<span style="font-family:Lat;font-style:italic;font-weight:400;font-size:11pt;color:var(--muted);">%s</span></div></div>'
                  '<p class="small" style="margin-bottom:0.08in;">📍 %s</p>' % (bn(x["no"]), E(x["title_bn"]), E(x["title_en"]), E(x.get("setting_bn", ""))), 0.75)
            for ln in x.get("lines", []):
                f.add(bubble(ln), h_bubble(ln))
            f.flush()
            f = Flow(H)
            f.h2("মূল বাক্যাংশ"); f.table(x.get("key_phrases", []), compact=True, tick=True)
            if x.get("culture_bn"):
                f.box("culture", "সংস্কৃতির টীকা", x["culture_bn"])
            yt = x.get("your_turn") or {}
            if yt:
                f.h2("আপনার পালা")
                f.p(yt.get("instruction_bn", ""))
                f.lines(yt.get("lines", []))
            f.flush()

    # ---- Ch. 14 readings
    rd = d.get("readings", [])
    if rd:
        f = Flow("১৪ · প্রথম পাঠ", "ch14")
        f.title(chapter_title(14, "প্রথম পাঠ", "Your First Reading"))
        f.p("ছয়টি ছোট লেখা: মোবাইল বার্তা থেকে খবর পর্যন্ত। প্রথমে শুধু ফরাসি পড়ুন, যতটা পারেন বুঝুন; তারপর উচ্চারণ ও অর্থ মিলিয়ে নিন, আর শেষে প্রশ্নের উত্তর দিন।")
        for r in rd:
            f.flush()
            f.add('<h2>%s<span>%s</span></h2><div class="small" style="margin:-0.06in 0 0.06in;">%s</div>' % ("", E(r["title_bn"]), E(r.get("type_bn", ""))), 0.55)
            f.add('<div style="background:#fff;border:1pt solid var(--line);border-radius:4pt;padding:0.12in 0.16in;font-family:Lat,LatX;font-size:11.5pt;line-height:1.6;color:var(--ink);margin-bottom:0.1in;">%s</div>' % " ".join(
                E(s["fr"]) for s in r["text"]), 0.3 + est_text(" ".join(s["fr"] for s in r["text"]), 70, 0.21))
            f.lines(r["text"])
            qs = "".join("<p>%s. %s</p>" % (bn(i + 1), E(q["q_bn"])) for i, q in enumerate(r.get("questions", [])))
            f.add(box("know", "প্রশ্ন", qs + '<p class="small" style="transform:rotate(180deg);">উত্তর: %s</p>' % E(" · ".join(q["a"] for q in r.get("questions", [])))), 1.3)
        f.flush()

    # ---- Ch. 15 literature (+ one Qur'an verse and one hadith)
    lit = d.get("literature", [])
    f = Flow("১৫ · সাহিত্যের প্রথম স্বাদ", "ch15")
    f.title(chapter_title(15, "সাহিত্যের প্রথম স্বাদ", "A Taste of Literature"))
    f.p("ভাষার আত্মা থাকে তার প্রবাদে আর কবিতায়। এখানে ফরাসিভাষী বিশ্বের বারোটি লাইন, প্রতিটির পাশে একই চেতনার একটি বাংলা লাইন: দুই ভাষার মধ্যে এক অদৃশ্য সেতু।")
    for it in lit:
        bp = it.get("bangla_pair") or {}
        f.add(('<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:0.12in;margin-bottom:0.12in;">'
               '<div style="background:#fff;border-left:3pt solid var(--accent);padding:0.08in 0.12in;border-radius:0 4pt 4pt 0;">'
               '<div class="frw" style="font-size:11.5pt;font-style:italic;line-height:1.4;">%s</div><div class="small">%s · <i style="font-family:Lat;">%s</i></div>'
               '<div style="font-size:10pt;line-height:1.45;margin-top:0.03in;">%s</div><div class="small" style="font-family:Lat;">%s</div>'
               '<div style="font-family:BnSans;font-weight:600;color:var(--gold);font-size:8.8pt;margin-top:0.03in;">— %s</div>%s</div>'
               '<div style="background:var(--gold-l);padding:0.08in 0.12in;border-radius:4pt;"><div style="font-family:BnSans;font-weight:600;font-size:8.5pt;color:#8a6420;">🔗 বাংলায় একই সুর</div>'
               '<div style="font-size:10.8pt;line-height:1.55;font-weight:700;color:var(--brand);">%s</div><div class="small">— %s</div></div></div>') % (
            E(it["fr"]), E(it.get("bn_pron", "")), E(it.get("en_pron", "")), E(it["bn"]), E(it["en"]), E(it.get("source", "")),
            ('<div class="small" style="margin-top:0.03in;">%s</div>' % E(it["note_bn"])) if it.get("note_bn") else "", E(bp.get("text_bn", "")), E(bp.get("source_bn", ""))),
              0.55 + max(est_text(it["fr"], 45, 0.22) + est_text(it["bn"], 45) + est_text(it.get("note_bn", ""), 50, 0.17) + 0.4, est_text(bp.get("text_bn", ""), 32, 0.25) + 0.3))
    f.h2("আসমানি বাণী ও নবীজির কথা")
    for q in QURAN_HADITH:
        f.add(('<div style="border:1.2pt solid var(--gold);background:#fff;border-radius:3pt;padding:0.1in 0.16in;margin-bottom:0.1in;">'
               '<div class="ar" style="font-size:17pt;line-height:1.8;text-align:center;color:var(--brand);">%s</div>'
               '<div class="frw" style="text-align:center;font-style:italic;font-weight:400;">%s</div><div style="text-align:center;font-size:10.4pt;">%s</div>'
               '<div style="text-align:center;font-family:BnSans;font-weight:600;font-size:8.8pt;color:var(--gold);">%s</div><div class="small center">%s</div></div>') % (
            q["ar"], E(q["fr"]), E(q["bn"]), E(q["source"]), E(q["note_bn"])), 1.75)
    f.flush()

    ch16.build()
    writing_pages("✍️ লেখার অনুশীলন ৩", "লেখার অনুশীলন ৩ — বাস্তব জীবনের লেখা", d.get("writing3", []), anchor="w3")
