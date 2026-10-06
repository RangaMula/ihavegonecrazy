# -*- coding: utf-8 -*-
"""Back matter: Ch. 17 road to intermediate, self-assessment, can-do list, writing answers, glossary, references, notes, certificate."""
import json, os, re, unicodedata
from engine import page, E, bn, box, h2, chapter_title, PAGES
from part23 import Flow, quiz_page, quiz_block, WRITING_ANSWERS, est_text

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    p = os.path.join(HERE, "data", name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

HARAKAT = re.compile("[\u064B-\u065F\u0670\u06E1\u0640]")
def sort_key(fr):
    """Arabic dictionary order: drop harakat, tatweel and a leading ال; hamza seats sort as alif."""
    s = HARAKAT.sub("", fr).strip()
    s = re.sub(r"^ال", "", s)
    return s.translate(str.maketrans("أإآٱؤئى", "اااا" + "وي" + "ي"))

def glossary():
    entries = []
    for f in ("journey_1_10.json", "journey_11_20.json"):
        for sec in load(f).get("sections", []):
            for s in sec["sets"]:
                for w in s["words"]:
                    entries.append((sort_key(w["fr"]), w["fr"], w["bn"], sec["no"]))
    if not entries:
        return
    entries.sort()
    per_col, cols = 38, 2
    per_page = per_col * cols
    first = True
    for k in range(0, len(entries), per_page):
        chunk = entries[k:k + per_page]
        colhtml = ""
        for c in range(cols):
            part = chunk[c * per_col:(c + 1) * per_col]
            colhtml += '<div>%s</div>' % "".join(
                '<div style="display:flex;gap:0.06in;font-size:8.4pt;line-height:1.38;border-bottom:0.4pt dotted var(--line);">'
                '<span class="frw" style="font-size:11.5pt;line-height:1.2;">%s</span><span style="flex:1;">%s</span>'
                '<span style="font-family:BnSans;color:var(--gold);">%s</span></div>' % (E(fr), E(b), bn(no)) for _, fr, b, no in part)
        page((h2("ত্রিভাষিক শব্দকোষ (শব্দের যাত্রা)") + '<p class="small">আরবি বর্ণানুক্রমে (ال বাদ দিয়ে) · বাংলা অর্থ · ডানে অংশ নম্বর (পূর্ণ উচ্চারণ ও ইংরেজি অর্থ সেই অংশে)</p>' if first else "") +
             '<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 0.2in;">%s</div>' % colhtml,
             head="শব্দকোষ", anchor="glossary" if first else None)
        first = False

def build():
    p5 = load("part5.json")
    road = p5.get("road", {})
    f = Flow("১৭ · মধ্যম স্তরের পথে", "back")
    f.title(chapter_title(17, "মধ্যম স্তরের পথে", "Your Road to Intermediate"))
    if road.get("intro_bn"):
        f.p(road["intro_bn"])
    if road.get("plan_90_bn"):
        f.h2("পরের ৯০ দিন: সপ্তাহ ধরে পরিকল্পনা")
        for i, s in enumerate(road["plan_90_bn"]):
            f.add('<div style="display:flex;gap:0.1in;padding:0.035in 0;border-bottom:1pt dashed var(--line);"><div style="font-family:BnSans;font-weight:700;color:var(--gold);width:0.75in;">সপ্তাহ %s</div>'
                  '<div style="flex:1;font-size:10.4pt;">%s</div><div>☐</div></div>' % (bn(i + 1), E(s)), 0.26 + est_text(s, 66, 0.19))
    for t in road.get("tracks", []):
        f.box("tip", t.get("title_bn", ""), t.get("text_bn", ""))
    if road.get("exam_bn"):
        f.box("know", "পরের ধাপের পরীক্ষা ও সনদ", road["exam_bn"])
    if road.get("resources_bn"):
        f.bullets(road["resources_bn"], "সহায়ক উৎস", "culture")
    f.flush()

    st = p5.get("selftest", [])
    f = Flow("নিজেকে যাচাই করুন")
    for k in range(0, len(st), 20):
        quiz_block(f, "চূড়ান্ত যাচাই · প্রশ্ন %s–%s" % (bn(k + 1), bn(min(k + 20, len(st)))), st[k:k + 20])
    f.flush()
    cd = p5.get("can_do", [])
    if cd:
        page(h2("আমি পারি! — ২৫টি দক্ষতা") + '<p class="small">প্রতিটি বাক্য পড়ুন। সত্যিই পারলে টিক দিন। যেগুলো বাকি, সেগুলোর অধ্যায় আবার দেখে নিন।</p>' +
             "".join('<div style="display:flex;gap:0.1in;padding:0.022in 0;border-bottom:1pt dashed var(--line);font-size:10.1pt;line-height:1.55;"><div>☐</div><div>%s</div></div>' % E(c) for c in cd),
             head="নিজেকে যাচাই করুন")
    if WRITING_ANSWERS:
        f = Flow("লেখার অনুশীলনের নমুনা উত্তর")
        f.h2("লেখার অনুশীলন: নমুনা উত্তর")
        f.p("নিজে লেখার কাজগুলোর জন্য এগুলো একটি নমুনা মাত্র; আপনার উত্তর ভিন্ন হলেও সঠিক হতে পারে।")
        for blk, title, ans in WRITING_ANSWERS:
            f.add('<div style="padding:0.04in 0;border-bottom:1pt dashed var(--line);font-size:9.8pt;"><b>%s</b> <span class="small">(%s)</span><div class="frw" style="font-weight:400;display:block;text-align:right;">%s</div></div>' % (
                E(title), E(blk.split("—")[0].strip()), E(ans)), 0.3 + est_text(ans, 80, 0.18))
        f.flush()
    glossary()
    page(h2("তথ্যসূত্র") + """
<div style="font-size:10pt;line-height:1.65;">
<p><b>কুরআন:</b> আরবি পাঠ ও অর্থ Quran.com-এর সাথে মিলিয়ে দেওয়া। উদ্ধৃত আয়াত: ২:৩১, ১২:২, ১৪:৪, ১৬:১২৫, ৩০:২২, ৪৯:১৩, ৫৫:৪, ৯৬:১, ১১২:১–৪ (এবং অধ্যায় ১৫-এর আয়াত)।</p>
<p><b>হাদিস:</b> Sunnah.com-এর সংখ্যা অনুযায়ী: সহীহ বুখারী ৭, ১২৭, ৩৪৬১, ৩৫৫৯; সহীহ মুসলিম ৮, ২২৩; জামে আত-তিরমিযী ১৯৫৬, ২৭১৫; সুনান আবু দাউদ ৩৬৪৫; মুসনাদ আহমাদ ১৭৪০, ৮৯৫২; আল-আদাবুল মুফরাদ ২৭৩ (এবং অধ্যায় ১৫-এর হাদিস)।</p>
<p><b>আরবি ভাষা ও ইতিহাস:</b> UNESCO, World Arabic Language Day (১৮ ডিসেম্বর); জাতিসংঘ সাধারণ পরিষদ প্রস্তাব ৩১৯০ (১৯৭৩); League of Arab States; Ibn Baṭṭūṭa, <i>al-Riḥla</i> (বাংলা ভ্রমণ, ১৩৪৬)।</p>
<p><b>শব্দ ও উচ্চারণ:</b> Hans Wehr, <i>A Dictionary of Modern Written Arabic</i>; আল-মুজাম আল-ওয়াসিত (মাজমাউল লুগাহ, কায়রো); ALA-LC Arabic Romanization Table (Library of Congress)।</p>
<p><b>সংস্কৃতি অংশের তথ্য:</b> প্রতিটি «জানেন কি?» তথ্যের উৎস-নির্দেশনা প্রকাশকের ডেটা ফাইলে সংরক্ষিত (source_hint)।</p>
<p><b>ফন্ট:</b> Noto Serif, Noto Serif Bengali, Noto Sans Bengali, Amiri (SIL Open Font License)।</p>
</div>""" + box("warn", "প্রকাশের আগে যাচাই", "<p>এই সংস্করণের কুরআন-হাদিস উদ্ধৃতি আলেম দ্বারা এবং আরবি অংশ আরবিভাষী সম্পাদক দ্বারা চূড়ান্ত যাচাইয়ের অপেক্ষায় (সিরিজ মানদণ্ড §৭)।</p>"),
         head="তথ্যসূত্র")
    for _ in range(2):
        page(h2("নোট") + "".join('<div style="border-bottom:0.75pt solid #cbbf9f;height:0.36in;"></div>' for _ in range(20)), head="নোট")
    # certificate on a recto page with a blank back
    main = sum(1 for p in PAGES if not p["front"])
    if main % 2 == 1:
        page("", folio=False)
    page("""
<div style="flex:1;display:flex;flex-direction:column;text-align:center;border:6pt double var(--gold);border-radius:20pt;padding:0.3in 0.35in;background:#fffdf8;">
  <img src="assets/logos/logo-bangla.png" style="width:1.3in;height:auto;margin:0 auto 0.1in;" alt=""/>
  <div style="font-family:BnSans;font-weight:700;color:var(--brand);font-size:28pt;">সনদপত্র</div>
  <div style="font-family:Arabic;color:var(--accent);font-size:20pt;line-height:1.5;">شَهَادَةُ إِتْمَامٍ <span style="font-family:Lat;font-style:italic;font-size:14pt;">· Certificate of Achievement</span></div>
  <div style="font-size:12.5pt;line-height:1.9;margin-top:0.2in;">এই মর্মে প্রত্যয়ন করা যাচ্ছে যে<br>
  <span style="display:inline-block;border-bottom:1pt solid var(--ink);width:4in;height:0.35in;"></span><br>
  <b>আরবি ভাষার দরজা</b> বইটির সকল পর্ব সম্পন্ন করেছেন: আরবি ধ্বনি ও লিপি, ১২টি বাক্য-কাঠামো,<br>
  <b>২,০০০ শব্দের যাত্রা</b> এবং <b>২০টি বাস্তব সংলাপ</b>। ভিত্তি স্তর সম্পন্ন; মধ্যম স্তরের পথে যাত্রা শুভ হোক।</div>
  <div class="frw" style="font-size:22pt;margin-top:0.15in;display:block;">مَبْرُوكٌ! وَرِحْلَةً سَعِيدَةً فِي رِحَابِ الْعَرَبِيَّةِ</div><div class="small">মাবরূːক! ওয়া রিহ়লাতান সাʿঈːদাতান ফ়ী রিহ়াːবিল-ʿআরাবিয়্যাহ · অভিনন্দন! আরবির প্রশস্ত জগতে আপনার যাত্রা শুভ হোক।</div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:auto;">
    <div style="text-align:left;font-size:10pt;">তারিখ: ________________</div>
    <div style="text-align:right;"><img src="assets/signature.svg" style="width:1.6in;height:auto;display:block;margin-left:auto;" alt=""/>
    <div style="border-top:1.5pt solid var(--gold);font-family:BnSans;font-size:10pt;padding-top:0.03in;"><b>হাফেজ আবদুল্লাহ মুহাম্মদ মিনহাজ রেজা</b><br>লেখক · মাকতাবাতু কুনুজুল আখিরাহ</div></div>
  </div>
</div>""", folio=False, anchor="certificate")
    page("", folio=False)
