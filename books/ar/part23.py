# -*- coding: utf-8 -*-
"""2nd-edition flow engine: continuous composition with measured heights.
- blocks keep together; headings marked keep=True stay with the next block
- tables break between rows (header repeated), card grids break between rows of cards
- pages are cut only when full, or when a new chapter/section explicitly calls flush()"""
import math, re
from engine import page, E, bn, box, h2, tr_line, tr_table, BEFORE_FIXED_PAGE
import measure

PAGE_H = 8.26   # inches available for content (small safety margin under the 8.4in text block)

def est_text(text, cpl=80, lh=0.2):
    return max(1, math.ceil(len(text or "") / cpl)) * lh

def h_tr_line(it):
    return 0.18 + est_text(it["fr"], 64, 0.2) + est_text(it["bn_pron"] + it["en_pron"], 84, 0.17) + est_text(it["bn"] + it["en"], 84, 0.18)

# ---------------------------------------------------------------- split an html string into top-level blocks
TAG = re.compile(r"<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>")
VOID = {"img", "br", "hr", "col", "meta", "input", "use", "path", "rect", "circle", "line", "polyline", "stop"}

def blocks_of(html):
    """Top-level elements of an html fragment (text between them is kept with the following element)."""
    out, depth, start = [], 0, 0
    for m in TAG.finditer(html):
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(4)
        if name in VOID or selfclose:
            if depth == 0:
                out.append(html[start:m.end()]); start = m.end()
            continue
        if closing:
            depth -= 1
            if depth == 0:
                out.append(html[start:m.end()]); start = m.end()
        else:
            depth += 1
    tail = html[start:].strip()
    if tail:
        out.append(tail)
    return [b for b in out if b.strip()]

MIN_START = 3.0   # a new chapter/section starts on the current page only if this much room is left

class _Flow:
    def __init__(self, head, anchor=None):
        self.head, self.anchor = head, anchor
        self.blocks, self.h = [], 0.0
        self.pending, self.ph = [], 0.0
        self.page_head, self.page_anchors = None, []
        self.next_anchor = anchor

    def newhead(self, head, anchor=None):
        """A new chapter/section begins: continue on this page if there is room, else start a new page."""
        if self.blocks and self.room() < MIN_START:
            self.emit()
        self.head = head
        self.next_anchor = anchor

    # -- core
    def _place(self, html, h):
        if not self.blocks:
            self.page_head = self.head
        if self.next_anchor:
            self.page_anchors.append(self.next_anchor); self.next_anchor = None
        self.blocks.append(html); self.h += h

    def emit(self):
        """Hard page break: output the current page."""
        if self.blocks:
            page("<!--planned %.2f-->" % self.h + "".join(self.blocks), head=self.page_head, anchors=self.page_anchors, _from_flow=True)
        self.blocks, self.h, self.page_anchors = [], 0.0, []

    def room(self):
        return PAGE_H - self.h

    def add(self, html, est=0.5, keep=False):
        h = measure.height(html, est)
        if keep:
            self.pending.append(html); self.ph += h
            return
        need = self.ph + h
        if self.blocks and need > self.room():
            self.flush(keep_pending=True)
        for p in self.pending:
            self._place(p, 0)
        self.h += self.ph
        self.pending, self.ph = [], 0.0
        self._place(html, h)

    def flush(self, keep_pending=False):
        """keep_pending=True: page is full (internal). Otherwise: end of a chapter/section, a soft break."""
        if keep_pending:
            self.emit()
            return
        if self.pending:
            for p in self.pending:
                self._place(p, 0)
            self.h += self.ph
            self.pending, self.ph = [], 0.0
        if self.blocks and self.room() < MIN_START:
            self.emit()

    def close(self):
        self.flush()
        self.emit()

    def html(self, fragment, est=0.4):
        """Add every top-level element of an html fragment; headings stay with what follows."""
        for b in blocks_of(fragment):
            st = b.lstrip()
            if st.startswith('<div class="cards">'):
                inner = st[len('<div class="cards">'):st.rfind("</div>")]
                self.grid(blocks_of(inner), width_in=2.72, gap=0.09, cls="cards")
                continue
            if st.startswith('<table class="tr') and "<tbody>" in st:
                pre, rest = st.split("<tbody>", 1)
                body, post = rest.rsplit("</tbody>", 1)
                rows = re.findall(r"<tr>.*?</tr>", body, flags=re.S)
                if len(rows) > 3:
                    self.rows(lambda rs, pre=pre, post=post: pre + "<tbody>" + "".join(rs) + "</tbody>" + post, rows, min_rows=2)
                    continue
            is_head = st.startswith(("<h2", "<h3", '<div class="chhead"'))
            self.add(b, est, keep=is_head)

    # -- convenience
    def h2(self, t):
        self.add(h2(E(t)), 0.42, keep=True)

    def h2raw(self, html):
        self.add(html, 0.42, keep=True)

    def title(self, html, h=1.0):
        self.add(html, h, keep=True)

    def p(self, text, cls=""):
        self.add('<p class="%s">%s</p>' % (cls, E(text)), est_text(text) + 0.08)

    def paras(self, items):
        for t in (items if isinstance(items, list) else [items]):
            self.p(t)

    def box(self, kind, title, text):
        self.add(box(kind, title, "<p>%s</p>" % E(text)), est_text(text, 74) + 0.4)

    def lines(self, items):
        for it in items:
            self.add(tr_line(it), h_tr_line(it))

    def bullets(self, items, title=None, kind="tip"):
        self.add(box(kind, title or "", "".join("<p>• %s</p>" % E(t) for t in items)), sum(est_text(t, 74) for t in items) + 0.45)

    # -- tables that break between rows
    def rows(self, wrap, row_htmls, est_row=0.25, min_rows=2):
        """wrap(list_of_row_html) -> full table html. Rows flow across pages, header repeated."""
        h0 = measure.height(wrap([]), 0.3)
        hs = [max(0.05, measure.height(wrap([r]), h0 + est_row) - h0) for r in row_htmls]
        i = 0
        while i < len(row_htmls):
            avail = self.room() - self.ph - h0
            take, acc = 0, 0.0
            while i + take < len(row_htmls) and acc + hs[i + take] <= avail:
                acc += hs[i + take]; take += 1
            if take < min(min_rows, len(row_htmls) - i) and self.blocks:
                self.flush(keep_pending=True)
                continue
            take = max(take, 1)
            part = row_htmls[i:i + take]
            for p in self.pending:
                self._place(p, 0)
            self.h += self.ph
            self.pending, self.ph = [], 0.0
            self._place(wrap(part), h0 + sum(hs[i:i + take]))
            i += take

    def table(self, items, tick=False, numbered=True, compact=True, start=1):
        rows = [tr_rows([it], tick, numbered, start + k)[0] for k, it in enumerate(items)]
        self.rows(lambda rs: tr_wrap(rs, tick, numbered, compact), rows)

    # -- card grids that break between card rows
    def grid(self, cards, cols=2, width_in=2.72, gap=0.09, cls="ccards"):
        hs = [measure.height('<div style="width:%.2fin;">%s</div>' % (width_in, c), 1.0) for c in cards]
        i = 0
        while i < len(cards):
            avail = self.room() - self.ph
            take, acc = 0, 0.0
            while i + take < len(cards):
                rowh = max(hs[i + take:i + take + cols]) + gap
                if acc + rowh > avail:
                    break
                acc += rowh; take += cols
            if take == 0 and self.blocks:
                self.flush(keep_pending=True)
                continue
            take = max(take, cols)
            for p in self.pending:
                self._place(p, 0)
            self.h += self.ph
            self.pending, self.ph = [], 0.0
            self._place('<div class="%s">%s</div>' % (cls, "".join(cards[i:i + take])), acc if acc else max(hs[i:i + take]) + gap)
            i += take

def tr_rows(items, tick=False, numbered=True, start=1):
    out = []
    for i, it in enumerate(items, start):
        note = ('<div class="note">%s</div>' % E(it.get("note_bn"))) if it.get("note_bn") else ""
        out.append('<tr>%s%s<td class="c-fr">%s</td><td class="c-bp">%s</td><td class="c-ep">%s</td><td class="c-bn">%s%s</td><td class="c-en">%s</td></tr>' % (
            '<td class="tk">☐</td>' if tick else "", ('<td class="n">%s</td>' % bn(i)) if numbered else "",
            E(it["fr"]), E(it["bn_pron"]), E(it["en_pron"]), E(it["bn"]), note, E(it["en"])))
    return out

def tr_wrap(rows, tick=False, numbered=True, compact=True):
    w = [("t", 0.2)] if tick else []
    w += [("n", 0.32)] if numbered else []
    rest = 5.56 - sum(x for _, x in w)
    w += [(k, rest * f) for k, f in (("fr", 0.19), ("bp", 0.23), ("ep", 0.2), ("bn", 0.2), ("en", 0.18))]
    cg = "<colgroup>%s</colgroup>" % "".join('<col style="width:%.2fin">' % x for _, x in w)
    return ('<table class="tr%s" style="table-layout:fixed;">' + cg + '<thead><tr>%s%s<th>العربية</th><th>বাংলা উচ্চারণ</th><th>Pronunciation</th><th>বাংলা অর্থ</th>'
            '<th>English</th></tr></thead><tbody>%s</tbody></table>') % (
        " compact" if compact else "", "<th></th>" if tick else "", "<th></th>" if numbered else "", "".join(rows))

def quiz_block(f, title, quiz):
    f.h2(title)
    qs = "".join('<div style="display:flex;gap:0.08in;padding:0.03in 0;border-bottom:1pt dashed var(--line);font-size:10pt;">'
                 '<div style="font-family:BnSans;font-weight:700;color:var(--gold);">%s.</div><div style="flex:1;">%s</div></div>' % (bn(i + 1), E(q["q_bn"]))
                 for i, q in enumerate(quiz))
    f.add('<div class="qz2">%s</div>' % qs, 0.3 * len(quiz))
    f.add('<div class="ans">উত্তর: %s</div>' % E(" · ".join("%s. %s" % (bn(i + 1), q["a"]) for i, q in enumerate(quiz))), 0.4)

def quiz_page(head, title, quiz, extra=""):
    f = Flow(head)
    if extra:
        f.html(extra)
    quiz_block(f, title, quiz)
    f.flush()

def writing_flow(f, title, tasks):
    f.h2(title)
    for t in tasks:
        n = min(int(t.get("lines", 4) or 4), 4)
        f.add(('<div style="border:1pt solid var(--line);border-radius:4pt;background:#fff;padding:0.08in 0.13in;margin-bottom:0.1in;">'
               '<div style="font-family:BnSans;font-weight:700;color:var(--brand);font-size:11.5pt;">%s <span style="color:var(--gold);">%s</span></div>'
               '<div style="font-size:10.3pt;line-height:1.5;">%s</div>%s%s</div>') % (
            E(t["title_bn"]), "★" * int(t.get("stars", 1)), E(t["instruction_bn"]),
            ('<div class="small" style="margin-top:0.03in;">উদাহরণ: <span class="frw">%s</span></div>' % E(t["example"])) if t.get("example") else "",
            "".join('<div style="border-bottom:0.75pt solid #cbbf9f;height:0.28in;"></div>' for _ in range(n))), 1.0 + 0.28 * n)
        WRITING_ANSWERS.append((title, t["title_bn"], t.get("answer", "")))

def writing_pages(head, title, tasks, anchor=None):
    f = Flow(head, anchor)
    writing_flow(f, title, tasks)
    f.flush()

WRITING_ANSWERS = []

# ---------------------------------------------------------------- page() replacement for hand-composed chapters
class FlowPages:
    """Drop-in for engine.page() in hand-composed chapters: their pages feed the open flow."""
    def __call__(self, inner, cls="", bg=None, head=None, anchor=None, folio=True, front=False):
        if head is None or bg or front or not folio or cls:
            page(inner, cls=cls, bg=bg, head=head, anchor=anchor, folio=folio, front=front)
            return
        f = OPEN[0]
        if f is None or f.head != head or anchor:
            f = Flow(head, anchor)
        f.html(inner)
    def done(self):
        if OPEN[0] is not None:
            OPEN[0].flush()

OPEN = [None]

def Flow(head, anchor=None):
    """Return the one open flow, switching to a new chapter/section head (pages continue when there is room)."""
    if OPEN[0] is None:
        OPEN[0] = _Flow(head, anchor)
    else:
        OPEN[0].newhead(head, anchor)
    return OPEN[0]

def close_flow():
    if OPEN[0] is not None:
        f, OPEN[0] = OPEN[0], None
        f.close()

BEFORE_FIXED_PAGE.append(close_flow)
