# -*- coding: utf-8 -*-
"""Front matter: title, copyright, author's foreword (series template), plate, how to use,
trilingual key, pronunciation key, contents, journey map, language passport."""
import re, os
from engine import page, E, bn, box, h2, tr_line, star_svg

HERE = os.path.dirname(os.path.abspath(__file__))
FOREWORD = os.path.join(HERE, "..", "..", "series-standard", "foreword", "foreword.html")

# ------------------------------------------------------------------ title page (i)
def title_page():
    page("""
<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;">
  <img src="assets/logos/logo-bangla.png" style="width:2.1in;height:auto;margin-bottom:0.3in;" alt="মাকতাবাতু কুনুজুল আখিরাহ"/>
  <div style="font-family:'BnSans';font-weight:600;color:var(--gold);font-size:13pt;">ভাষার দরজা সিরিজ</div>
  <div style="font-family:'BnSans';font-weight:700;color:var(--brand);font-size:40pt;line-height:1.2;margin:0.06in 0;">আরবি ভাষার দরজা</div>
  <div style="font-family:'Arabic';font-weight:700;color:var(--accent);font-size:26pt;line-height:1.5;direction:rtl;">بَابُ اللُّغَةِ الْعَرَبِيَّةِ</div>
  <div style="font-family:'Lat';color:var(--muted);font-size:12pt;margin-top:0.04in;">Introduction to Arabic for Bangla Speakers</div>
  <div style="width:2.4in;height:1.5pt;background:var(--gold);margin:0.28in auto;"></div>
  <div style="font-size:12.5pt;line-height:1.8;">বাংলাভাষীদের জন্য প্রমিত আরবির পূর্ণাঙ্গ ভিত্তি<br>
  <span class="small">উচ্চারণ বাংলায় ও ইংরেজিতে · ২,০০০ শব্দের যাত্রা · ২০টি বাস্তব সংলাপ · আরব বিশ্বের সংস্কৃতি</span></div>
  <div style="margin-top:0.45in;font-family:'BnSans';font-weight:600;font-size:13pt;color:var(--brand);">হাফেজ আবদুল্লাহ মুহাম্মদ মিনহাজ রেজা</div>
  <div class="small">মাকতাবাতু কুনুজুল আখিরাহ · ঢাকা</div>
</div>""", front=True, folio=False, bg="#fffdf8")

# ------------------------------------------------------------------ copyright (ii)
def copyright_page():
    page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;font-size:9.6pt;line-height:1.7;">
  <div style="text-align:center;margin-bottom:0.25in;"><img src="assets/logos/logo-english.png" style="width:1.2in;height:auto;" alt="Maktabatu Kunujul Akhirah"/></div>
  <p style="text-align:left;"><b>আরবি ভাষার দরজা</b> (بَابُ اللُّغَةِ الْعَرَبِيَّةِ — Introduction to Arabic for Bangla Speakers)<br>
  ভাষার দরজা সিরিজ · প্রথম সংস্করণ, ২০২৬</p>
  <p style="text-align:left;">লেখক ও প্রকাশক: <b>হাফেজ আবদুল্লাহ মুহাম্মদ মিনহাজ রেজা</b><br>
  স্বত্বাধিকারী, <b>মাকতাবাতু কুনুজুল আখিরাহ</b> · প্রতিষ্ঠাতা, <b>কুনুজুল আখিরাহ চ্যারিটেবল ট্রাস্ট</b><br>
  Level 8, House 003, Road 402, Sector 11, Jolshiri Abashon, Rupganj, Narayanganj, Dhaka, Bangladesh<br>
  ওয়েবসাইট: kunujulakhirah.org · যোগাযোগ: minhaz.reza87@gmail.com</p>
  <p style="text-align:left;">স্বত্ব © ২০২৬ আবদুল্লাহ মুহাম্মদ মিনহাজ রেজা। সর্বস্বত্ব সংরক্ষিত। পর্যালোচনার জন্য সংক্ষিপ্ত উদ্ধৃতি ছাড়া
  প্রকাশকের লিখিত অনুমতি ছাড়া এই বইয়ের কোনো অংশ কোনো মাধ্যমে পুনর্মুদ্রণ বা প্রকাশ করা যাবে না।</p>
  <p style="text-align:left;">কুরআনের আয়াতের অর্থ ও হাদিসের উদ্ধৃতি স্বীকৃত অনুবাদ ও উৎসের সাথে মিলিয়ে দেওয়া হয়েছে; উৎস বইয়ের শেষে
  «তথ্যসূত্র» অংশে দেওয়া আছে। ফন্ট: Noto Serif, Noto Serif/Sans Bengali (Google, SIL Open Font License) ও Amiri (SIL Open Font License)।</p>
  <p style="text-align:left;">ISBN: [প্রকাশের সময় যুক্ত হবে]</p>
</div>""", front=True, folio=False)

# ------------------------------------------------------------------ foreword (iii-ix) from the series template
def scope_css(css):
    out = []
    css = re.sub(r"@font-face\{[^}]*\}", "", css)
    css = re.sub(r"@page\{[^}]*\}", "", css)
    css = re.sub(r"@media print\{[^{}]*\{[^}]*\}[^}]*\}", "", css)
    css = css.replace('"LatSerif"', '"Lat"')
    for block in css.split("}"):
        if "{" not in block:
            continue
        sel, body = block.split("{", 1)
        sel = sel.strip()
        if not sel or sel.startswith(":root") or sel in ("*", "html,body"):
            if sel.startswith(":root"):
                out.append(".page.fw{%s}" % body)   # foreword colour tokens, scoped
            continue
        sels = []
        for s in sel.split(","):
            s = s.strip()
            if s == "body":
                sels.append(".page.fw")
            elif s.startswith(".page"):
                sels.append(".page.fw" + s[len(".page"):])
            elif s.startswith(".tight") or s.startswith(".opener"):
                sels.append(".page.fw" + s)   # classes that sit on the page element itself
            else:
                sels.append(".fw " + s)
        out.append("%s{%s}" % (",".join(sels), body))
    return "\n".join(out)

FOREWORD_CSS = ""

def foreword():
    global FOREWORD_CSS
    src = open(FOREWORD, encoding="utf-8").read()
    css = src.split("<style>", 1)[1].split("</style>", 1)[0]
    FOREWORD_CSS = scope_css(css) + "\n.page.fw{--teal:#174d33;padding:0.8in 0.78in 0.85in;}\n.fw .sign .logo{width:1.0in;height:auto;}"
    defs = re.search(r'<svg width="0" height="0"[\s\S]*?</svg>', src).group(0)
    chunks = re.findall(r'<div class="page([^"]*)">([\s\S]*?)<div class="folio">[^<]*</div>\s*</div>', src)
    assert len(chunks) == 7, len(chunks)
    for i, (cls, body) in enumerate(chunks):
        body = re.sub(r'<div class="runhead">.*?</div>', "", body)
        body = re.sub(r'<img class="logo"[^>]*>', '<img class="logo" src="assets/logos/logo-bangla.png" alt="মাকতাবাতু কুনুজুল আখিরাহ"/>', body)
        if i == 0:
            body = defs + body
        page(body, cls="fw" + cls, head=None if i == 0 else "লেখকের কথা", front=True)

# ------------------------------------------------------------------ plate (x): 49:13
def plate():
    page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;text-align:center;padding:0 0.2in;">
  <div>%s</div>
  <div class="ar" style="font-size:24pt;line-height:2.1;color:var(--brand);margin:0.25in 0 0.2in;">يَا أَيُّهَا النَّاسُ إِنَّا خَلَقْنَاكُم مِّن ذَكَرٍ وَأُنثَىٰ وَجَعَلْنَاكُمْ شُعُوبًا وَقَبَائِلَ لِتَعَارَفُوا ۚ إِنَّ أَكْرَمَكُمْ عِندَ اللَّهِ أَتْقَاكُمْ</div>
  <div style="font-size:13pt;line-height:1.85;">«হে মানুষ! আমি তোমাদের সৃষ্টি করেছি এক পুরুষ ও এক নারী থেকে, আর তোমাদের বানিয়েছি
  বিভিন্ন জাতি ও গোত্র, <b>যাতে তোমরা একে অপরকে চিনতে পারো।</b> নিশ্চয়ই আল্লাহর কাছে তোমাদের মধ্যে সবচেয়ে সম্মানিত সে-ই,
  যে সবচেয়ে বেশি আল্লাহভীরু।»</div>
  <div style="font-family:'BnSans';font-weight:600;color:var(--gold);margin-top:0.12in;">সূরা আল-হুজুরাত ৪৯:১৩</div>
  <div style="margin-top:0.25in;">%s</div>
</div>""" % (star_svg(34), star_svg(26)), front=True, folio=False, bg="#fffdf8")

# ------------------------------------------------------------------ how to use (xi-xii)
def how_to_use():
    page(h2("বইটি কীভাবে পড়বেন") + """
<p class="lead">এই বই একটি ভাষার দরজা খুলে দেবে, ধাপে ধাপে। প্রতিটি পর্ব আগের পর্বের ওপর দাঁড়িয়ে আছে,
তাই শুরু থেকে ক্রমানুসারে পড়ুন। প্রতিদিন আধা ঘণ্টা, সপ্তাহে পাঁচ দিন: এই ছন্দই সবচেয়ে কাজের।</p>
<div class="cards">
 <div class="card"><div class="ct">পর্ব ১ · ভাষাটিকে চিনুন</div><div class="cb">আরবি ভাষার গল্প, কারা বলে, কেন শিখবেন, আর বাংলার সাথে তার আত্মীয়তা।</div></div>
 <div class="card"><div class="ct">পর্ব ২ · ধ্বনি ও লিপি</div><div class="cb">প্রতিটি ধ্বনি বাংলার সাথে মিলিয়ে, ২৮টি হরফ আর হরকত উদাহরণসহ। এই পর্ব শেষে আপনি যেকোনো হরকতযুক্ত আরবি শব্দ পড়তে পারবেন।</div></div>
 <div class="card"><div class="ct">পর্ব ৩ · ভাষার ইট-পাথর</div><div class="cb">সংখ্যা, সময় ও হিজরি পঞ্জিকা, ১২টি বাক্য-কাঠামো, আর আরব আতিথেয়তার রীতি।</div></div>
 <div class="card"><div class="ct">পর্ব ৪ · শব্দের যাত্রা</div><div class="cb">২০টি অংশে ২,০০০ শব্দ: বিমানবন্দরে পৌঁছানো থেকে আরবিভাষী জগৎকে আপন করে নেওয়া পর্যন্ত।</div></div>
 <div class="card"><div class="ct">পর্ব ৫ · ভাষাটি ব্যবহার করুন</div><div class="cb">২০টি বাস্তব সংলাপ, প্রথম পাঠ, সাহিত্যের স্বাদ, আর নিজের বিশ্বাসের পরিচয় দেওয়ার ভাষা।</div></div>
 <div class="card"><div class="ct">শেষ অংশ</div><div class="cb">মধ্যম স্তরের পথ, নিজেকে যাচাই, ত্রিভাষিক শব্দকোষ আর আপনার সনদপত্র।</div></div>
</div>""" + box("tip", "প্রতিদিনের ছন্দ", "<p>১০ মিনিট নতুন শব্দ বা নিয়ম · ১০ মিনিট জোরে জোরে পড়া · ১০ মিনিট লেখা। সপ্তাহের শেষ দিনে পুরো সপ্তাহের পড়া একবার দেখে নিন।</p>"),
         head="বইটি কীভাবে পড়বেন", front=True, anchor="howto")
    page(h2("বইয়ের চিহ্নগুলো") + """
<div class="cards">
 <div class="card"><div class="ct">☐ টিক-বাক্স</div><div class="cb">প্রতিটি শব্দের পাশে একটি বাক্স। শব্দটি মনে থাকলে টিক দিন। প্রতিটি টিক একটি ছোট্ট জয়।</div></div>
 <div class="card"><div class="ct">🎯 মিশন</div><div class="cb">পাঁচ মিনিটের একটি বাস্তব কাজ, যাতে শেখা শব্দ বই থেকে বেরিয়ে জীবনে আসে।</div></div>
 <div class="card"><div class="ct">✍️ লেখার অনুশীলন</div><div class="cb">★ নকল করুন · ★★ শূন্যস্থান পূরণ · ★★★ নিজে লিখুন। উত্তর বইয়ের শেষে।</div></div>
 <div class="card"><div class="ct">🛂 পাসপোর্টে সিল</div><div class="cb">শব্দের যাত্রার প্রতিটি অংশ শেষে আপনার ভাষার পাসপোর্টে একটি সিল দিন।</div></div>
 <div class="card"><div class="ct">💡 টিপস · ⚠️ সাবধান</div><div class="cb">কাজের কৌশল আর বাংলাভাষীদের সাধারণ ভুল।</div></div>
 <div class="card"><div class="ct">🌍 সংস্কৃতি · 🔗 বাংলার সাথে মিল</div><div class="cb">আরব জগতের জানালা, আর যেখানে বাংলার সাথে মিল আছে সেখানে সেতু।</div></div>
</div>""" + box("culture", "অডিও", "<p>উচ্চারণ শেখার চূড়ান্ত মাপকাঠি মানুষের কণ্ঠ। প্রতিটি অধ্যায়ের অডিও অনলাইনে দেওয়া হবে; লিংক ও QR কোড পরবর্তী মুদ্রণে যুক্ত হবে। ততদিন বাংলা ও ইংরেজি উচ্চারণ-লিপি ধরে জোরে জোরে পড়ুন।</p>"),
         head="বইটি কীভাবে পড়বেন", front=True)

# ------------------------------------------------------------------ trilingual key (xiii)
def trilingual_key():
    page(h2("তিন ভাষার চাবি") + """
<p class="lead">এই বইয়ের প্রতিটি আরবি শব্দ ও বাক্য পাঁচটি অংশে লেখা। ব্যাখ্যা সবসময় বাংলায়; ইংরেজি পাশে থাকে
দ্বিতীয় চাবি হিসেবে, যাতে আপনি দুই দিক থেকে নিজের বোঝা মিলিয়ে নিতে পারেন।</p>
<table class="tr" style="font-size:11pt;"><thead><tr><th>العربية</th><th>বাংলা উচ্চারণ</th><th>Pronunciation</th><th>বাংলা অর্থ</th><th>English</th></tr></thead>
<tbody><tr><td class="c-fr">كِتَاب</td><td class="c-bp">কিতাːব</td><td class="c-ep">kitāb</td><td class="c-bn">বই<div class="note">পুং · বহুবচন: كُتُب (কুতুব)</div></td><td class="c-en">book</td></tr>
<tr><td class="c-fr">شُكْرًا</td><td class="c-bp">শুকরান</td><td class="c-ep">shukran</td><td class="c-bn">ধন্যবাদ</td><td class="c-en">thank you</td></tr></tbody></table>
<div class="cards">
 <div class="card"><div class="ct">১ · العربية</div><div class="cb">আসল আরবি বানান, পূর্ণ হরকতসহ, ডান থেকে বাঁয়ে। বিশেষ্যের নিচে ছোট নোটে লিঙ্গ (পুং/স্ত্রী) আর বহুবচন; ক্রিয়ার নিচে বর্তমান কালের রূপ।</div></div>
 <div class="card"><div class="ct">২ · বাংলা উচ্চারণ</div><div class="cb">বাংলা অক্ষরে উচ্চারণ। বাংলায় নেই এমন ধ্বনির জন্য বিশেষ চিহ্ন (পরের পাতা)।</div></div>
 <div class="card"><div class="ct">৩ · Pronunciation</div><div class="cb">ইংরেজি বর্ণে আন্তর্জাতিক রীতির (ALA-LC) সরল প্রতিবর্ণীকরণ: ā ī ū = লম্বা স্বর, ḥ ṣ ḍ ṭ ẓ = ভারী হরফ।</div></div>
 <div class="card"><div class="ct">৪ ও ৫ · অর্থ</div><div class="cb">বাংলা অর্থ ও ইংরেজি অর্থ পাশাপাশি।</div></div>
</div>""" + box("tip", "বাক্যের বেলায়", "<p>পুরো বাক্য বা সংলাপ তিন লাইনে সাজানো থাকে: প্রথমে আরবি (ডান থেকে পড়ুন), তারপর দুই রকম উচ্চারণ, শেষে বাংলা ও ইংরেজি অর্থ।</p>")
         + tr_line({"fr": "اِسْمِي نَاصِرٌ.", "bn_pron": "ইসমীː নাːস়ির", "en_pron": "ismī nāṣir", "bn": "আমার নাম নাসির।", "en": "My name is Nasir."}, big=True),
         head="তিন ভাষার চাবি", front=True, anchor="key")

# ------------------------------------------------------------------ pronunciation key (xiv)
def pron_key():
    rows = [
        ("থ়", "th (ث)", "ثَلَاثَة", "থ়ালাːথ়াহ", "জিভের ডগা দুই পাটি দাঁতের মাঝে রেখে ফুঁ: ইংরেজি think-এর th।"),
        ("দ়", "dh (ذ)", "ذَهَب", "দ়াহাব", "একই জায়গা, কিন্তু গলায় স্বর লাগিয়ে: ইংরেজি this-এর th।"),
        ("য", "ẓ (ظ)", "ظُهْر", "যুহর", "দ়-এর ভারী রূপ: জিভ নিচে, মুখ ভরাট।"),
        ("হ়", "ḥ (ح)", "حَلِيب", "হ়ালীːব", "গলার মাঝখান চেপে জোরে ‘হ’: গরম কাচে ভাপ দেওয়ার মতো।"),
        ("খ়", "kh (خ)", "خُبْز", "খ়ুবজ়", "গলার পেছন থেকে ঘষা ‘খ’, বাংলা খ নয়।"),
        ("গ়", "gh (غ)", "غَزَال", "গ়াজ়াːল", "গার্গল করার মতো ঘষা ‘গ’।"),
        ("ক়", "q (ق)", "قَلْب", "ক়ালব", "জিভের একেবারে গোড়া দিয়ে গভীর ‘ক’।"),
        ("ʿ", "ʿ (ع)", "عَيْن", "ʿআইন", "গলা চেপে স্বর বের করা: আরবির সবচেয়ে বিশেষ ধ্বনি।"),
        ("ʾ", "ʾ (ء)", "سَأَلَ", "সাʾআলা", "স্বরের আগে গলায় ছোট্ট থামা, যেমন ‘উ-উঁ’ বলার মাঝে।"),
        ("স়", "ṣ (ص)", "صَبَاح", "স়াবাːহ়", "ভারী ‘স’: জিভ নিচে, মুখ ভরাট।"),
        ("ড / ট", "ḍ ṭ (ض ط)", "طَالِب", "টাːলিব", "ভারী ‘দ’ ও ‘ত’: বাংলা ড-ট এদের সবচেয়ে কাছের।"),
        ("জ় / ফ়", "z f (ز ف)", "زَيْت", "জ়াইত", "মৌমাছির গুঞ্জনের মতো ‘জ়’; ঠোঁটে দাঁত ছুঁইয়ে ‘ফ়’।"),
        ("ː", "ā ī ū", "بَاب", "বাːব", "লম্বা স্বর: দ্বিগুণ সময় ধরে টানুন। ছোট-লম্বা বদলালে অর্থ বদলায়!"),
    ]
    body = "".join('<tr><td style="font-size:14pt;color:var(--gold);font-family:BnSerif;">%s</td><td class="c-ep">%s</td>'
                   '<td class="c-fr">%s</td><td class="c-bp">%s</td><td>%s</td></tr>' % (E(r[0]), E(r[1]), E(r[2]), E(r[3]), E(r[4])) for r in rows)
    page(h2("উচ্চারণ-চিহ্নের চাবি") + """
<p>বাংলায় নেই এমন আরবি ধ্বনি দেখাতে এই বইয়ে কয়েকটি চিহ্ন: <b>নুক্তা (়)</b> মানে বাংলায় নেই এমন ব্যঞ্জন; <b>ː</b> মানে লম্বা স্বর;
<b>ʿ</b> আর <b>ʾ</b> গলার দুটি ধ্বনি। ছোট ‘আ’ সবসময় া দিয়ে লেখা, কখনো ‘অ’ দিয়ে নয়।</p>
<table class="tr compact" style="font-size:9.6pt;table-layout:fixed;"><colgroup><col style="width:0.6in"><col style="width:0.75in"><col style="width:0.9in"><col style="width:0.95in"><col style="width:2.36in"></colgroup>
<thead><tr><th>চিহ্ন</th><th>ধ্বনি</th><th>উদাহরণ</th><th>উচ্চারণ</th><th>কীভাবে বলবেন</th></tr></thead><tbody>%s</tbody></table>
""" % body + box("warn", "মনে রাখুন", "<p>শব্দ বা বাক্যের শেষে থামলে শেষের ছোট স্বর আর তানউইন উচ্চারিত হয় না (যেমন <span class='frw'>كِتَابٌ</span> থেমে পড়লে কিতাːব), "
             "আর ة হয় ‘াহ’। উচ্চারণ-লিপি যেভাবে লেখা, ঠিক সেভাবে পড়ুন।</p>"),
         head="উচ্চারণ-চিহ্নের চাবি", front=True)

# ------------------------------------------------------------------ contents (xv-xvi)
TOC = [
    ("লেখকের কথা", "", None), ("বইটি কীভাবে পড়বেন", "", "howto"),
    ("পর্ব ১ · ভাষাটিকে চিনুন", "Meet the Language", "part1"),
    ("১ · গল্পের শুরু", "How Arabic Grew", "ch1"), ("২ · কারা আরবি বলে", "Who Speaks Arabic Today", "ch2"),
    ("৩ · কেন শিখবেন", "Why Learn Arabic", "ch3"), ("৪ · ভাষার পরিবার ও বাংলার আত্মীয়তা", "Family Tree & Bond with Bangla", "ch4"),
    ("পর্ব ২ · ধ্বনি ও লিপি", "Sounds & Script", "part2"),
    ("৫ · ধ্বনির জগৎ", "The Sound System", "ch5"), ("৬ · লিপি পরিচয়", "The Arabic Script", "ch6"), ("৭ · প্রথম পড়া", "Reading Drills", "ch7"),
    ("পর্ব ৩ · ভাষার ইট-পাথর", "Building Blocks", "part3"),
    ("৮ · সংখ্যা", "Numbers", "ch8"), ("৯ · সময় ও পঞ্জিকা", "Time & Calendar", "ch9"),
    ("১০ · বাক্যের কাঠামো", "The Sentence Skeleton", "ch10"), ("১১ · ভদ্রতা ও সংস্কৃতি", "Politeness & Culture", "ch11"),
    ("পর্ব ৪ · শব্দের যাত্রা", "The 2,000-Word Journey", "part4"),
    ("পর্ব ৫ · ভাষাটি ব্যবহার করুন", "Use the Language", "part5"),
    ("১৩ · ২০টি বাস্তব সংলাপ", "20 Real-Life Conversations", "ch13"), ("১৪ · প্রথম পাঠ", "Your First Reading", "ch14"),
    ("১৫ · সাহিত্যের প্রথম স্বাদ", "A Taste of Literature", "ch15"), ("১৬ · আমার বিশ্বাসের পরিচয়", "Introducing My Faith", "ch16"),
    ("শেষ অংশ", "Back Matter", "back"),
]

def contents():
    def rows(items):
        out = ""
        for t, en, a in items:
            is_part = t.startswith("পর্ব") or t in ("লেখকের কথা", "বইটি কীভাবে পড়বেন", "শেষ অংশ")
            pg = "{{%s}}" % a if a else "iii"
            out += ('<div style="display:flex;align-items:baseline;gap:0.1in;padding:%s 0;border-bottom:1pt dashed var(--line);%s">'
                    '<div style="flex:1;font-family:BnSans;font-weight:%s;font-size:%s;color:%s;">%s '
                    '<span style="font-family:Lat;font-style:italic;font-weight:400;font-size:9.5pt;color:var(--muted);">%s</span></div>'
                    '<div style="font-family:BnSans;font-weight:600;color:var(--gold);">%s</div></div>') % (
                "0.07in" if is_part else "0.045in", "margin-top:0.08in;" if t.startswith("পর্ব") else "",
                700 if is_part else 400, "12pt" if is_part else "11pt", "var(--brand)" if is_part else "var(--ink)", E(t), E(en), pg)
        return out
    page(h2("সূচিপত্র") + rows(TOC[:11]), head="সূচিপত্র", front=True)
    page(h2("সূচিপত্র (চলমান)") + rows(TOC[11:]), head="সূচিপত্র", front=True)

# ------------------------------------------------------------------ journey map (xvii-xviii)
def journey_map():
    stops = [("পর্ব ১", "ভাষাটিকে চিনুন", 80, 90), ("পর্ব ২", "ধ্বনি ও লিপি", 300, 150), ("পর্ব ৩", "ভাষার ইট-পাথর", 120, 260),
             ("পর্ব ৪", "শব্দের যাত্রা · ২,০০০ শব্দ", 330, 370), ("পর্ব ৫", "ভাষাটি ব্যবহার করুন", 130, 480), ("🏁", "সনদপত্র", 320, 580)]
    path = "M80 90 C200 80 300 100 300 150 S120 200 120 260 S330 320 330 370 S130 430 130 480 S320 540 320 580"
    nodes = "".join(
        '<circle cx="%d" cy="%d" r="18" fill="#174d33"/><circle cx="%d" cy="%d" r="24" fill="none" stroke="#b8892d" stroke-width="1.5"/>'
        '<text x="%d" y="%d" text-anchor="middle" font-family="BnSans" font-weight="700" font-size="11" fill="#fff">%s</text>'
        '<text x="%d" y="%d" text-anchor="%s" font-family="BnSans" font-weight="600" font-size="15" fill="#22302d">%s</text>' % (
            x, y, x, y, x, y + 4, a if not a.startswith("🏁") else "★", x + (34 if x < 200 else -34), y + 5, "start" if x < 200 else "end", b)
        for a, b, x, y in stops)
    page(h2("আপনার যাত্রার মানচিত্র") + """
<p class="lead">বইটি একটি যাত্রা। ভাষার গল্প দিয়ে শুরু, তারপর ধ্বনি ও অক্ষর, তারপর বাক্যের কাঠামো, তারপর ২,০০০ শব্দের দীর্ঘ পথ, আর শেষে বাস্তব জীবনে ভাষার ব্যবহার।</p>
<svg viewBox="0 0 420 640" style="width:100%%;height:6.4in;"><path d="%s" fill="none" stroke="#b8892d" stroke-width="3" stroke-dasharray="8 7"/>%s</svg>""" % (path, nodes),
         head="যাত্রার মানচিত্র", front=True)
    page(h2("এই বই শেষে আপনি…") + """
<div class="cards">
 <div class="card"><div class="ct">🔤 পড়তে পারবেন</div><div class="cb">যেকোনো হরকতযুক্ত আরবি শব্দ, সাইনবোর্ড, মেনু আর সহজ লেখা।</div></div>
 <div class="card"><div class="ct">👂 ধ্বনি চিনবেন</div><div class="cb">আরবির প্রতিটি ধ্বনি, গলার ধ্বনিসহ, বাংলার সাথে মিলিয়ে।</div></div>
 <div class="card"><div class="ct">📚 ২,০০০ শব্দ জানবেন</div><div class="cb">দৈনন্দিন জীবন, কাজ, পড়াশোনা আর আরব জগতের সংস্কৃতি।</div></div>
 <div class="card"><div class="ct">🧩 বাক্য বানাবেন</div><div class="cb">১২টি কাঠামো দিয়ে নিজের কথা নিজে বলবেন।</div></div>
 <div class="card"><div class="ct">💬 কথা বলবেন</div><div class="cb">বিমানবন্দর থেকে চাকরির সাক্ষাৎকার পর্যন্ত ২০টি পরিস্থিতিতে।</div></div>
 <div class="card"><div class="ct">🤝 নিজের পরিচয় দেবেন</div><div class="cb">নিজের দেশ, পরিবার আর বিশ্বাসের কথা ভদ্রভাবে আরবিতে বলবেন।</div></div>
</div>""" + box("know", "মধ্যম স্তরের পথে", "<p>এই বই প্রমিত আরবির একটি মজবুত ভিত্তি। এরপর ব্যাকরণ, শব্দার্থ, শোনা ও বলা, উচ্চারণ আর সাহিত্যের মধ্যম স্তরের যাত্রা শুরু; কীভাবে, তা বইয়ের শেষ অংশে বলা আছে।</p>"),
         head="যাত্রার মানচিত্র", front=True)

# ------------------------------------------------------------------ passport (xix-xxii)
SECTIONS = ["প্রথম শব্দ", "পরিচয়", "বিমানবন্দর থেকে শহরে", "মাথা গোঁজার ঠাঁই", "বাজার ও দোকান", "রান্নাঘর ও দস্তরখান",
            "সময়ের ছন্দ", "শরীর ও সুস্থতা", "কাজের জগৎ", "শেখা ও যোগাযোগ", "প্রকৃতি ও আবহাওয়া", "দেশ, শহর ও বিস্ময়",
            "ইতিহাস ও কিংবদন্তি", "উৎসব, বিশ্বাস ও ঐতিহ্য", "শিল্প, গান ও খেলা", "মন ও মূল্যবোধ", "বন্ধুত্ব ও আড্ডা",
            "আজকের জীবন", "যে শব্দ শুধু এখানেই আছে", "ভাবনা প্রকাশ"]
STAGES = ["পৌঁছানো", "দিনযাপন", "কাজ ও শেখা", "দেশটিকে চেনা", "মানুষকে চেনা", "আপন করে নেওয়া"]

def stamp(i, name):
    return ('<div style="display:flex;flex-direction:column;align-items:center;text-align:center;">'
            '<div style="width:1.05in;height:1.05in;border:2pt dashed var(--accent);border-radius:50%%;display:flex;align-items:center;'
            'justify-content:center;font-family:BnSans;font-weight:700;color:var(--accent);font-size:20pt;opacity:0.85;">%s</div>'
            '<div style="font-family:BnSans;font-size:9.3pt;margin-top:0.05in;line-height:1.3;">%s</div></div>') % (bn(i), E(name))

def passport():
    page("""
<div style="flex:1;margin:-0.3in -0.2in;background:#174d33;border-radius:10pt;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#f3e3bd;border:3pt solid #b8892d;">
  <div style="font-family:BnSans;font-weight:600;font-size:13pt;letter-spacing:0;">ভাষার দরজা সিরিজ</div>
  <div style="font-family:BnSans;font-weight:700;font-size:36pt;margin:0.12in 0;">ভাষার পাসপোর্ট</div>
  <div style="font-family:Arabic;font-size:20pt;line-height:1.5;">جَوَازُ سَفَرٍ لُغَوِيٌّ · <span style="font-family:Lat;font-style:italic;font-size:15pt;">Language Passport</span></div>
  <img src="assets/logos/logo-arabic.png" style="width:1.8in;height:auto;margin:0.35in 0;" alt=""/>
  <div style="font-family:BnSans;font-size:12pt;">আরবি · <span style="font-family:Arabic;font-size:15pt;">الْعَرَبِيَّة</span> · Arabic</div>
  <div style="margin-top:0.35in;font-family:BnSans;font-size:11pt;">ধারকের নাম: ____________________________</div>
  <div style="margin-top:0.12in;font-family:BnSans;font-size:11pt;">যাত্রা শুরুর তারিখ: ______________________</div>
</div>""", front=True, folio=False)
    for k in (0, 10):
        grid = "".join(stamp(i + 1, SECTIONS[i]) for i in range(k, k + 10))
        page(h2("পাসপোর্টের সিল · অংশ %s–%s" % (bn(k + 1), bn(k + 10))) + """
<p class="small">শব্দের যাত্রার প্রতিটি অংশ শেষ করে এখানে সেই অংশের বৃত্তে রং করুন, তারিখ লিখুন বা নিজের সই দিন।</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.26in 0.2in;margin-top:0.15in;">%s</div>""" % grid,
             head="ভাষার পাসপোর্ট", front=True)
    badges = "".join(
        '<div style="display:flex;align-items:center;gap:0.15in;padding:0.1in 0;border-bottom:1pt dashed var(--line);">'
        '<div style="width:0.75in;height:0.75in;border:2.5pt solid var(--gold);border-radius:12pt;display:flex;align-items:center;'
        'justify-content:center;font-family:BnSans;font-weight:700;color:var(--gold);font-size:18pt;">%s</div>'
        '<div style="font-family:BnSans;font-size:12.5pt;"><b>পর্ব %s · %s</b><br><span class="small">%s শব্দ পূর্ণ হলে এই ব্যাজে রং করুন</span></div></div>' % (
            bn(i + 1), bn(i + 1), s, bn([400, 800, 1000, 1300, 1700, 2000][i]))
        for i, s in enumerate(STAGES))
    page(h2("পর্বের ব্যাজ") + badges, head="ভাষার পাসপোর্ট", front=True)

def build():
    title_page(); copyright_page(); foreword(); plate(); how_to_use(); trilingual_key(); pron_key()
    contents(); journey_map(); passport()
