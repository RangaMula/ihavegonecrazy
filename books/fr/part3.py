# -*- coding: utf-8 -*-
"""Part 3 — ভাষার ইট-পাথর · Building Blocks (Ch. 8–11, writing practice 2, checkpoint). Data: data/part3.json."""
import json, os
from engine import page, E, bn, box, h2, tr_line, tr_table, chapter_title, part_opener
from part23 import Flow, quiz_page, writing_pages, h_tr_line, est_text, h_table

HERE = os.path.dirname(os.path.abspath(__file__))

def num_table(items):
    rows = "".join('<tr><td style="font-family:Lat;font-weight:700;color:var(--gold);font-size:11pt;">%s</td><td class="c-fr">%s</td><td class="c-bp">%s</td>'
                   '<td class="c-ep">%s</td><td class="c-bn">%s%s</td></tr>' % (
                       E(str(n.get("n", ""))), E(n["fr"]), E(n["bn_pron"]), E(n["en_pron"]), E(n["bn"]),
                       ('<div class="note">%s</div>' % E(n["note_bn"])) if n.get("note_bn") else "") for n in items)
    return ('<table class="tr compact"><thead><tr><th>সংখ্যা</th><th>Français</th><th>বাংলা উচ্চারণ</th><th>Pronunciation</th><th>বাংলা</th></tr></thead>'
            '<tbody>%s</tbody></table>') % rows

def pattern_block(f, pt):
    f.add('<div style="display:flex;align-items:center;gap:0.12in;margin:0.04in 0 0.06in;"><div style="width:0.5in;height:0.5in;border-radius:50%%;background:var(--accent);'
          'color:#fff;font-family:BnSans;font-weight:700;font-size:16pt;display:flex;align-items:center;justify-content:center;flex:none;">%s</div>'
          '<div><div style="font-family:BnSans;font-weight:700;font-size:15pt;color:var(--brand);line-height:1.3;">%s</div>'
          '<div style="font-family:Lat;font-style:italic;color:var(--muted);">%s</div></div></div>' % (bn(pt["no"]), E(pt["title_bn"]), E(pt.get("title_en", ""))), 0.75)
    f.p(pt.get("explain_bn", ""))
    if pt.get("bangla_compare_bn"):
        f.box("link", "বাংলার সাথে তুলনা", pt["bangla_compare_bn"])
    if pt.get("model"):
        f.add(tr_line(pt["model"], big=True), h_tr_line(pt["model"]) + 0.15)
    tb = pt.get("table") or {}
    if tb.get("rows"):
        th = "".join("<th>%s</th>" % E(h) for h in tb.get("headers", []))
        tr = "".join("<tr>%s</tr>" % "".join('<td class="c-fr" style="font-weight:600;">%s</td>' % E(c) for c in r) for r in tb["rows"])
        f.add('<div class="small" style="margin-bottom:0.02in;">বদলে বদলে বলুন (substitution table):</div><table class="tr"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, tr),
              0.45 + 0.27 * len(tb["rows"]))
    f.lines(pt.get("examples", []))

def build():
    p = os.path.join(HERE, "data", "part3.json")
    if not os.path.exists(p):
        return
    d = json.load(open(p, encoding="utf-8"))
    page(part_opener("৩", "ভাষার ইট-পাথর", "Building Blocks",
         "ধ্বনি আর অক্ষর জানা হলো; এবার ভাষার ইট-পাথর। গোনা, সময় বলা, তারিখ লেখা, আর ১২টি মূল কাঠামো দিয়ে নিজের বাক্য নিজে বানানো। "
         "পর্ব শেষে জানবেন ফরাসিভাষী মানুষের ভদ্রতার রীতিনীতি, যাতে প্রথম সাক্ষাতেই মন জয় করতে পারেন।",
         [("অধ্যায় ৮", "সংখ্যা"), ("অধ্যায় ৯", "সময় ও পঞ্জিকা"), ("অধ্যায় ১০", "বাক্যের কাঠামো"), ("অধ্যায় ১১", "ভদ্রতা ও সংস্কৃতি"), ("✍️", "লেখার অনুশীলন ২")]),
         anchor="part3", folio=False, bg="#f3f6fb")

    # ---- Ch. 8 numbers
    c = d["ch8"]; f = Flow("৮ · সংখ্যা", "ch8")
    f.title(chapter_title(8, "সংখ্যা", "Numbers"))
    f.paras(c.get("intro_bn", []))
    nums = c.get("numbers", [])
    for k in range(0, len(nums), 14):
        part = nums[k:k + 14]
        f.add(num_table(part), 0.35 + 0.26 * len(part))
    for key, title, kind in (("belgium_swiss_bn", "বেলজিয়াম ও সুইজারল্যান্ডে", "culture"), ("lakh_bn", "লাখ-কোটি বনাম মিলিয়ন", "link")):
        if c.get(key):
            f.box(kind, title, c[key])
    if c.get("ordinals"):
        f.h2("ক্রমবাচক: প্রথম, দ্বিতীয়…"); f.table(c["ordinals"], compact=True, numbered=False)
    for u in c.get("uses", []):
        f.h2(u.get("title_bn", "")); f.lines(u.get("examples", []))
    f.flush()
    if c.get("quiz"):
        quiz_page("৮ · সংখ্যা", "সংখ্যা: নিজেকে যাচাই", c["quiz"])

    # ---- Ch. 9 time
    c = d["ch9"]; f = Flow("৯ · সময় ও পঞ্জিকা", "ch9")
    f.title(chapter_title(9, "সময় ও পঞ্জিকা", "Time & Calendar"))
    for key, title in (("days", "সপ্তাহের দিন"), ("months", "মাসের নাম"), ("seasons", "ঋতু"), ("parts_of_day", "দিনের ভাগ"), ("time_words", "সময়ের শব্দ")):
        if c.get(key):
            f.h2(title); f.table(c[key], compact=True, tick=True, chunk=14)
    for key, title in (("time_telling", "কয়টা বাজে?"), ("date_examples", "তারিখ বলা")):
        if c.get(key):
            f.h2(title); f.lines(c[key])
    if c.get("festivals"):
        f.h2("ফরাসিভাষী বিশ্বের উৎসব-পঞ্জিকা")
        for fe in c["festivals"]:
            nm = fe["name"]
            f.add(('<div class="cc" style="margin-bottom:0.08in;background:#fff;border:0.75pt solid var(--line);border-left:3pt solid var(--accent);padding:0.07in 0.12in;">'
                   '<div><span class="frw" style="font-size:11.5pt;">%s</span> · %s · <i style="font-family:Lat;color:var(--muted);">%s</i> — <b>%s</b></div>'
                   '<div style="font-size:9.8pt;">📅 %s · %s</div></div>') % (E(nm["fr"]), E(nm["bn_pron"]), E(nm["en_pron"]), E(nm["bn"]), E(fe.get("when_bn", "")), E(fe.get("story_bn", ""))),
                  0.55 + est_text(fe.get("story_bn", ""), 80))
    f.flush()

    # ---- Ch. 10 patterns
    c = d["ch10"]; f = Flow("১০ · বাক্যের কাঠামো", "ch10")
    f.title(chapter_title(10, "বাক্যের কাঠামো", "The Sentence Skeleton"))
    f.paras(c.get("intro_bn", []))
    if c.get("word_order_bn"):
        f.box("link", "বাক্যের ক্রম: বাংলা বনাম ফরাসি", c["word_order_bn"])
    for pt in c.get("patterns", []):
        f.flush(); pattern_block(f, pt)
    f.flush()
    if c.get("previews"):
        f.h2("মধ্যম স্তরে যা শিখবেন: এক ঝলক")
        for pv in c["previews"]:
            f.box("know", pv.get("title_bn", ""), pv.get("text_bn", ""))
        f.flush()

    # ---- Ch. 11 politeness
    c = d["ch11"]; f = Flow("১১ · ভদ্রতা ও সংস্কৃতি", "ch11")
    f.title(chapter_title(11, "ভদ্রতা ও সংস্কৃতি", "Politeness & Culture"))
    f.paras(c.get("intro_bn", []))
    if c.get("greetings"):
        f.h2("অভিবাদন"); f.table(c["greetings"], compact=True)
    if c.get("tu_vous_bn"):
        f.box("link", "tu না vous? (তুমি না আপনি?)", c["tu_vous_bn"])
    if c.get("address"):
        f.h2("সম্বোধন"); f.table(c["address"], compact=True)
    for cu in c.get("customs", []):
        f.box("culture", cu.get("title_bn", ""), cu.get("text_bn", ""))
    f.flush()

    writing_pages("✍️ লেখার অনুশীলন ২", "লেখার অনুশীলন ২ — শব্দ থেকে বাক্য", d.get("writing2", []), anchor="w2")
    cp = d.get("checkpoint3", {})
    if cp.get("build"):
        f = Flow("পর্ব ৩ · যাচাই")
        f.h2("পর্ব ৩ শেষ! বাক্য বানান")
        f.p(cp.get("build_bn", "এলোমেলো শব্দগুলো সাজিয়ে সঠিক বাক্য বানান।"))
        for i, b in enumerate(cp["build"]):
            f.add('<div style="padding:0.05in 0;border-bottom:1pt dashed var(--line);"><b>%s.</b> %s<div style="border-bottom:0.75pt solid #cbbf9f;height:0.32in;"></div></div>' % (
                bn(i + 1), " / ".join('<span class="frw">%s</span>' % E(w) for w in b["words"])), 0.62)
        f.add('<div class="small" style="transform:rotate(180deg);margin-top:0.1in;">উত্তর: %s</div>' % E(" · ".join("%s. %s" % (bn(i + 1), b["answer"]) for i, b in enumerate(cp["build"]))), 0.4)
        f.flush()
    if cp.get("quiz"):
        quiz_page("পর্ব ৩ · যাচাই", "পর্ব ৩: নিজেকে যাচাই করুন", cp["quiz"])
