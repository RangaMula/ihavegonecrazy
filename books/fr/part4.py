# -*- coding: utf-8 -*-
"""Part 4 — শব্দের যাত্রা · The 2,000-Word Journey (Ch. 12). Data: data/journey_1_10.json + data/journey_11_20.json."""
import json, os, math
from engine import page, E, bn, box, h2, tr_line, part_opener, EXTRA_CSS
import measure
from part23 import Flow

HERE = os.path.dirname(os.path.abspath(__file__))
STAGES = {1: ("পৌঁছানো", "Arriving"), 2: ("দিনযাপন", "Daily living"), 3: ("কাজ ও শেখা", "Work & learning"),
          4: ("দেশটিকে চেনা", "Discovering the land"), 5: ("মানুষকে চেনা", "Knowing the people"), 6: ("আপন করে নেওয়া", "Making it your own")}

CSS = """
table.wj{width:100%;border-collapse:collapse;table-layout:fixed;font-size:8.8pt;line-height:1.28;margin:0.02in 0 0.06in;}
table.wj th{font-family:BnSans,Lat;font-weight:600;font-size:7.6pt;color:#fff;background:var(--brand);padding:0.03in 0.04in;text-align:left;}
table.wj td{padding:0.025in 0.04in;border-bottom:0.5pt solid var(--line);vertical-align:top;overflow-wrap:anywhere;}
table.wj tr:nth-child(even) td{background:#fffdf8;}
table.wj td.n{color:var(--gold);font-family:BnSans;font-weight:600;}
table.wj td.c-fr{font-family:Lat,LatX;font-weight:700;color:var(--accent);}
table.wj td.c-bp{font-family:BnSerif;}
table.wj td.c-ep{font-family:Lat;font-style:italic;color:var(--muted);font-size:8.2pt;}
table.wj td.c-en{font-family:Lat;color:var(--muted);font-size:8.3pt;}
table.wj .note{font-size:7.4pt;color:var(--muted);font-family:BnSans;line-height:1.25;}
.secop{flex:1;display:flex;flex-direction:column;}
.secop .stage{font-family:BnSans;font-weight:600;color:var(--gold);font-size:11pt;}
.secop .sno{font-family:BnSans;font-weight:700;color:var(--accent);font-size:60pt;line-height:1;margin-top:0.1in;}
.secop .stt{font-family:BnSans;font-weight:700;color:var(--brand);font-size:28pt;line-height:1.2;}
.secop .sen{font-family:Lat;font-style:italic;color:var(--muted);font-size:13pt;margin-bottom:0.18in;}
.secop .scene{font-size:12.4pt;line-height:1.8;border-left:3pt solid var(--gold);padding-left:0.15in;margin:0.05in 0 0.2in;}
.counter{display:flex;align-items:center;gap:0.15in;background:var(--brand);color:#fff;border-radius:6pt;padding:0.12in 0.18in;margin-top:auto;}
.counter .big{font-family:BnSans;font-weight:700;font-size:22pt;line-height:1;}
.counter .lbl{font-family:BnSans;font-size:10.5pt;line-height:1.4;}
.cando li{margin:0 0 0.05in 0.2in;font-size:11.5pt;}
.ccards{display:grid;grid-template-columns:1fr 1fr;gap:0.09in;}
.cc{background:#fff;border:0.75pt solid var(--line);border-top:2.5pt solid var(--accent);border-radius:3pt;padding:0.07in 0.1in 0.06in;font-size:9pt;line-height:1.35;}
.cc .top{display:flex;gap:0.07in;align-items:flex-start;}
.cc .ic{font-size:17pt;line-height:1;}
.cc .fr{font-family:Lat,LatX;font-weight:700;color:var(--accent);font-size:10.5pt;line-height:1.25;}
.cc .pr{font-size:8.3pt;color:var(--muted);}
.cc .pr i{font-family:Lat;}
.cc .mn{font-size:9.2pt;margin-top:0.02in;}
.cc .mn .en{font-family:Lat;color:var(--muted);font-size:8.3pt;}
.cc .st{font-size:8.6pt;line-height:1.42;margin-top:0.04in;padding-top:0.04in;border-top:0.5pt dashed var(--line);}
.cc .lk{font-size:8.3pt;color:#8a6420;margin-top:0.03in;}
.qz{display:grid;grid-template-columns:1fr 1fr;gap:0.03in 0.18in;font-size:9.6pt;line-height:1.4;}
.qz div{border-bottom:0.6pt dashed var(--line);padding:0.03in 0 0.08in;}
.ans{transform:rotate(180deg);font-size:7.4pt;color:var(--muted);line-height:1.45;border-top:1pt solid var(--line);padding-top:0.04in;margin-top:auto;}
.stampbox{display:flex;align-items:center;gap:0.18in;border:1.5pt dashed var(--accent);border-radius:8pt;padding:0.1in 0.16in;margin-top:0.1in;}
.stampbox .sc{width:0.8in;height:0.8in;border:2pt dashed var(--accent);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24pt;flex:none;}
.milestone{flex:1;display:flex;flex-direction:column;}
.milestone .ban{background:linear-gradient(135deg,#174d33,#24418f);color:#fff;border-radius:8pt;padding:0.2in 0.25in;text-align:center;}
.milestone .ban .t{font-family:BnSans;font-weight:700;font-size:26pt;line-height:1.2;}
.milestone .ban .n{font-family:BnSans;font-weight:700;font-size:50pt;color:#f3e3bd;line-height:1.1;}
"""

# ------------------------------------------------------------------ helpers
def est_lines(text, cap):
    return max(1, math.ceil(len(text or "") / cap))

def row_height(w):
    # characters per line per column at 8.8pt in the fixed widths below
    lines = max(est_lines(w["fr"], 19), est_lines(w["bn_pron"], 15), est_lines(w["en_pron"], 17),
                est_lines(w["bn"] + (" " + w.get("note_bn", "") if w.get("note_bn") else ""), 14), est_lines(w["en"], 15))
    return 0.032 + 0.152 * lines   # inches

def wj_table(words, start):
    cols = ('<colgroup><col style="width:0.17in"><col style="width:0.4in"><col style="width:1.12in"><col style="width:1.0in">'
            '<col style="width:1.0in"><col style="width:1.05in"><col style="width:0.84in"></colgroup>')
    rows = "".join('<tr><td>☐</td><td class="n">%s</td><td class="c-fr">%s</td><td class="c-bp">%s</td><td class="c-ep">%s</td>'
                   '<td class="c-bn">%s%s</td><td class="c-en">%s</td></tr>' % (
                       bn(i), E(w["fr"]), E(w["bn_pron"]), E(w["en_pron"]), E(w["bn"]),
                       ('<div class="note">%s</div>' % E(w["note_bn"])) if w.get("note_bn") else "", E(w["en"]))
                   for i, w in enumerate(words, start))
    return ('<table class="wj">%s<thead><tr><th></th><th></th><th>Français</th><th>বাংলা উচ্চারণ</th><th>Pronunciation</th>'
            '<th>বাংলা অর্থ</th><th>English</th></tr></thead><tbody>%s</tbody></table>') % (cols, rows)

def real_row_height(w, n):
    empty = measure.height(wj_table([], 1), 0.25)
    return max(0.1, measure.height(wj_table([w], n), row_height(w) + 0.25) - empty)

def split_by_height(words, first_cap, cap, start=1):
    chunks, cur, h, c = [], [], 0.25, first_cap
    for i, w in enumerate(words):
        rh = real_row_height(w, start + i)
        if cur and h + rh > c:
            chunks.append(cur); cur, h, c = [], 0.25, cap
        cur.append(w); h += rh
    if cur:
        chunks.append(cur)
    return chunks

def culture_card(w):
    link = ('<div class="lk">🔗 %s</div>' % E(w["link_bn"])) if w.get("link_bn") else ""
    story = ('<div class="st">✨ %s</div>' % E(w["story_bn"])) if w.get("story_bn") else ""
    return ('<div class="cc"><div class="top"><div class="ic">%s</div><div><div class="fr">%s</div>'
            '<div class="pr">%s · <i>%s</i></div></div></div><div class="mn">%s <span class="en">/ %s</span></div>%s%s</div>') % (
        E(w.get("icon", "")), E(w["fr"]), E(w["bn_pron"]), E(w["en_pron"]), E(w["bn"]), E(w["en"]), story, link)

def card_height(w):
    return 0.62 + 0.155 * math.ceil(len(w.get("story_bn", "") + w.get("link_bn", "")) / 40)

def split_cards(words, first_cap, cap):
    """Two-column grid: a row costs the taller of its two cards."""
    chunks, cur, h, c = [], [], 0.0, first_cap
    i = 0
    while i < len(words):
        pair = words[i:i + 2]
        rh = max(measure.height('<div style="width:2.73in;">%s</div>' % culture_card(w), card_height(w)) for w in pair) + 0.09
        if cur and h + rh > c:
            chunks.append(cur); cur, h, c = [], 0.0, cap
        cur.extend(pair); h += rh; i += 2
    if cur:
        chunks.append(cur)
    return chunks

# ------------------------------------------------------------------ pages
def section_pages(sec, before):
    no, st = sec["no"], sec["stage"]
    head = "অংশ %s · %s" % (bn(no), sec["title_bn"])
    cando = "".join("<li>%s</li>" % E(c) for c in sec["can_do_bn"])
    page("""<div class="secop"><div class="stage">পর্ব %s · %s</div><div class="sno">%s</div><div class="stt">%s</div><div class="sen">%s</div>
<div class="scene">%s</div><h3>এই অংশ শেষে আপনি পারবেন…</h3><ul class="cando">%s</ul>
<div class="counter"><div class="big">%s → %s</div><div class="lbl">আপনার শব্দভান্ডার<br>এই অংশে নতুন ১০০টি শব্দ</div></div></div>""" % (
        bn(st), STAGES[st][0], bn(no), E(sec["title_bn"]), E(sec["title_en"]), E(sec["scene_bn"]), cando, bn(before), bn(before + 100)),
        head=head, anchor="sec%d" % no, bg="#f6f8fc")
    n = before
    for s in sec["sets"]:
        title = "%s · %s" % (s["code"], s["title_bn"])
        sub = '<div class="small" style="margin:-0.06in 0 0.04in;font-family:Lat;font-style:italic;">%s%s</div>' % (
            E(s["title_en"]), " · 🌍 culture set" if s["kind"] == "C" else "")
        if s["kind"] == "F":
            for k, chunk in enumerate(split_by_height(s["words"], 7.45, 7.75, n + 1)):
                page((h2(title) + sub if k == 0 else h2(title + " (চলমান)")) + wj_table(chunk, n + 1), head=head)
                n += len(chunk)
        else:
            for k, chunk in enumerate(split_cards(s["words"], 7.45, 7.75)):
                page((h2(title) + sub if k == 0 else h2(title + " (চলমান)")) +
                     '<div class="ccards">%s</div>' % "".join(culture_card(w) for w in chunk), head=head)
                n += len(chunk)
    f = Flow(head)
    f.add(h2("এখনই বলুন") + '<p class="small">শুধু এ পর্যন্ত শেখা শব্দ দিয়ে, জোরে জোরে বলুন:</p>', 0.7)
    for it in sec["say_now"]:
        f.add(tr_line(it), 0.8)
    f.add(box("mission", "মিশন", "<p>%s</p>" % E(sec["mission_bn"])), 0.9)
    qs = "".join("<div>%s. %s</div>" % (bn(i + 1), E(q["q_bn"])) for i, q in enumerate(sec["quiz"]))
    ans = " · ".join("%s. %s" % (bn(i + 1), q["a"]) for i, q in enumerate(sec["quiz"]))
    f.add(h2("নিজেকে যাচাই") + '<div class="qz">%s</div>' % qs + '<div class="ans" style="margin-top:0.06in;">উত্তর: %s</div>' % E(ans), 2.6)
    stamp = sec.get("stamp", {})
    f.add(('<div class="stampbox"><div class="sc">%s</div><div><div style="font-family:BnSans;font-weight:700;color:var(--accent);font-size:13pt;">পাসপোর্টে সিল দিন!</div>'
           '<div style="font-size:10.5pt;">অংশ %s «%s» শেষ। ভাষার পাসপোর্টে %s নম্বর সিলটিতে রং করুন, তারিখ লিখুন। <b>%s</b></div></div></div>') % (
              E(stamp.get("icon", "🛂")), bn(no), E(sec["title_bn"]), bn(no), E(stamp.get("label_bn", ""))), 1.1)
    f.flush()
    return before + 100

def milestone_page(m):
    f = Flow("মাইলফলক · %s শব্দ" % bn(m["total"]))
    f.add("""<div class="milestone" style="flex:none;"><div class="ban"><div class="t">অভিনন্দন!</div><div class="n">%s</div>
<div style="font-family:BnSans;font-size:13pt;">শব্দ আপনার ঝুলিতে</div></div>
<p class="lead" style="margin-top:0.15in;">%s</p></div>""" % (bn(m["total"]), E(m["celebration_bn"])), 2.6)
    f.add(h2("পুরস্কারের পাঠ: %s" % E(m["title_bn"])) + '<p class="small">এই লেখার প্রতিটি শব্দ আপনি আগেই শিখেছেন। প্রথমে শুধু ফরাসি লাইনগুলো পড়ুন, তারপর অর্থ মিলিয়ে নিন।</p>', 0.8)
    f.add('<div style="background:#fff;border:1pt solid var(--line);border-radius:4pt;padding:0.12in 0.16in;font-family:Lat,LatX;font-size:11.5pt;line-height:1.6;margin-bottom:0.1in;">'
          '<div class="frw" style="font-size:13pt;margin-bottom:0.04in;">%s</div>%s</div>' % (E(m.get("title_fr", "")), " ".join(E(it["fr"]) for it in m["reading"])), 2.0)
    for it in m["reading"]:
        f.add(tr_line(it), 0.8)
    f.add(box("know", "পাসপোর্টে ব্যাজ", "<p>ভাষার পাসপোর্টের ‘পর্বের ব্যাজ’ পাতায় এই পর্বের ব্যাজটিতে রং করুন।</p>"), 0.8)
    f.flush()

def load():
    secs, mils = [], []
    for f in ("journey_1_10.json", "journey_11_20.json"):
        p = os.path.join(HERE, "data", f)
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            secs += d["sections"]; mils += d.get("milestones", [])
    return sorted(secs, key=lambda s: s["no"]), {m["after_section"]: m for m in mils}

def build():
    EXTRA_CSS.append(CSS)
    secs, mils = load()
    if not secs:
        return
    page(part_opener("৪", "শব্দের যাত্রা", "The 2,000-Word Journey",
         "এবার শুরু দীর্ঘ এক যাত্রা। কল্পনা করুন, আপনি বিমান থেকে নামলেন এক ফরাসিভাষী দেশে। প্রথমে সালাম-পরিচয়, তারপর থাকার জায়গা, বাজার, "
         "রান্নাঘর, কাজ আর পড়াশোনা। তারপর দেশটিকে চেনা, তার মানুষকে চেনা, আর শেষে ভাষাটিকে আপন করে নেওয়া। ২০টি অংশ, প্রতিটিতে ১০০টি শব্দ, "
         "আর প্রতিটি অংশ শেষে আপনার পাসপোর্টে একটি সিল।",
         [("পর্ব ১", "পৌঁছানো · অংশ ১–৪"), ("পর্ব ২", "দিনযাপন · অংশ ৫–৮"), ("পর্ব ৩", "কাজ ও শেখা · অংশ ৯–১০"),
          ("পর্ব ৪", "দেশটিকে চেনা · অংশ ১১–১৩"), ("পর্ব ৫", "মানুষকে চেনা · অংশ ১৪–১৭"), ("পর্ব ৬", "আপন করে নেওয়া · অংশ ১৮–২০")]),
         anchor="part4", folio=False, bg="#f3f6fb")
    total = 0
    for sec in secs:
        total = section_pages(sec, (sec["no"] - 1) * 100)
        if sec["no"] in mils:
            milestone_page(mils[sec["no"]])
