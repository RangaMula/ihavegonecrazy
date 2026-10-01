# -*- coding: utf-8 -*-
"""Shared renderers for Parts 2 and 3 (data/part2.json, data/part3.json): flowing blocks are packed into pages
by estimated height, so the content decides the page count."""
import math
from engine import page, E, bn, box, h2, tr_line, tr_table

PAGE_H = 8.15   # usable inches below the running head

def est_text(text, cpl=78, lh=0.205):
    return max(1, math.ceil(len(text or "") / cpl)) * lh

def h_tr_line(it):
    return 0.2 + est_text(it["fr"], 62, 0.21) + est_text(it["bn_pron"] + it["en_pron"], 80, 0.18) + est_text(it["bn"] + it["en"], 80, 0.19)

def h_table(items):
    return 0.3 + sum(0.06 + 0.17 * max(math.ceil(len(i["fr"]) / 16), math.ceil(len(i["bn_pron"]) / 14),
                                       math.ceil(len(i["bn"] + (i.get("note_bn") or "")) / 14), math.ceil(len(i["en"]) / 14), 1) for i in items)

class Flow:
    """Collects (html, height) blocks and cuts pages when full."""
    def __init__(self, head, anchor=None):
        self.head, self.anchor, self.blocks, self.h = head, anchor, [], 0.0
    def add(self, html, height, keep=False):
        if self.blocks and self.h + height > PAGE_H:
            self.flush()
        self.blocks.append(html); self.h += height
    def flush(self):
        if self.blocks:
            page("".join(self.blocks), head=self.head, anchor=self.anchor)
            self.anchor = None
        self.blocks, self.h = [], 0.0
    # convenience
    def title(self, html, h=1.15):
        self.add(html, h)
    def h2(self, t):
        self.add(h2(E(t)), 0.45)
    def p(self, text, cls=""):
        self.add('<p class="%s">%s</p>' % (cls, E(text)), est_text(text) + 0.1)
    def paras(self, items):
        for t in (items if isinstance(items, list) else [items]):
            self.p(t)
    def box(self, kind, title, text):
        self.add(box(kind, title, "<p>%s</p>" % E(text)), est_text(text, 72) + 0.42)
    def lines(self, items):
        for it in items:
            self.add(tr_line(it), h_tr_line(it))
    def table(self, items, chunk=12, **kw):
        for k in range(0, len(items), chunk):
            part = items[k:k + chunk]
            self.add(tr_table(part, start=k + 1, **kw), h_table(part))
    def bullets(self, items, title=None, kind="tip"):
        html = "".join("<p>• %s</p>" % E(t) for t in items)
        self.add(box(kind, title or "", html), sum(est_text(t, 72) for t in items) + 0.5)

def quiz_page(head, title, quiz, extra=""):
    qs = "".join('<div style="display:flex;gap:0.08in;padding:0.035in 0;border-bottom:1pt dashed var(--line);font-size:10.2pt;">'
                 '<div style="font-family:BnSans;font-weight:700;color:var(--gold);">%s.</div><div style="flex:1;">%s</div></div>' % (bn(i + 1), E(q["q_bn"]))
                 for i, q in enumerate(quiz))
    ans = " · ".join("%s. %s" % (bn(i + 1), q["a"]) for i, q in enumerate(quiz))
    page(h2(title) + extra + qs + '<div class="spacer"></div><div class="ans" style="transform:rotate(180deg);font-size:7.4pt;color:var(--muted);'
         'line-height:1.45;border-top:1pt solid var(--line);padding-top:0.04in;">উত্তর: %s</div>' % E(ans), head=head)

def writing_pages(head, title, tasks, anchor=None):
    """Two tasks per page with ruled lines; answers go to the back matter list WRITING_ANSWERS."""
    first = True
    for k in range(0, len(tasks), 2):
        body = h2(title + ("" if first else " (চলমান)"))
        for t in tasks[k:k + 2]:
            n = min(int(t.get("lines", 4) or 4), 7)
            body += ('<div style="border:1pt solid var(--line);border-radius:4pt;background:#fff;padding:0.1in 0.14in;margin-bottom:0.14in;">'
                     '<div style="font-family:BnSans;font-weight:700;color:var(--brand);font-size:12pt;">%s <span style="color:var(--gold);">%s</span></div>'
                     '<div style="font-size:10.6pt;line-height:1.6;">%s</div>%s%s</div>') % (
                E(t["title_bn"]), "★" * int(t.get("stars", 1)), E(t["instruction_bn"]),
                ('<div class="small" style="margin-top:0.04in;">উদাহরণ: <span class="frw">%s</span></div>' % E(t["example"])) if t.get("example") else "",
                "".join('<div style="border-bottom:0.75pt solid #cbbf9f;height:0.34in;"></div>' for _ in range(n)))
            WRITING_ANSWERS.append((title, t["title_bn"], t.get("answer", "")))
        page(body, head=head, anchor=anchor if first else None)
        first = False

WRITING_ANSWERS = []
