"""Split OCR text (Internet Archive *_djvu.txt) into tales, driven by the book's table of contents.

split_ocr(path, lang, toc_rx=None, body_start=None) -> [{"title", "text"}]
"""
import difflib, re, collections

STOP = {
    "en": "the and to of a he she it was said his her in that they you i not with for him had as but on at all so then".split(),
    "fr": "le la les de et il elle un une dit à que des en est lui pas se qui dans au son sa ne je vous on".split(),
    "de": "der die das und er sie es ein eine sagte zu den nicht ich mit sich in auf dem des war hatte so da".split(),
    "nl": "de het een en hij zij ze van in is dat niet die zich op te met was als".split(),
}
TOC_LINE = re.compile(r"^\s*(?:No\.?\s*)?(?P<num>[IVXLCivxlc1lI]{1,7}|\d{1,3})\s*[.,:)—–-]+\s*(?P<title>.{3,90}?)[\s.·•…_,]*(?P<page>\d{1,4})\s*$")
TOC_NOPAGE = re.compile(r"^\s*(?:No\.?\s*)?(?P<num>[IVXLC]{1,7}|\d{1,3})\s*[.,:)—–-]+\s*(?P<title>[^\d].{2,90}?)\s*$")


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-zà-ÿ0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def ratio_lang(text, lang):
    words = re.findall(r"[a-zA-Zà-ÿÀ-ß']+", text.lower())
    if not words:
        return 0
    st = set(STOP[lang])
    return sum(1 for w in words if w in st) / len(words)


TOC_DOTS = re.compile(r"^\s*(?P<num>)(?P<title>[A-ZÀ-Þ\\|!][^\n]{2,80}?)\s*[.·•…_ ]{4,}\s*(?P<page>\d{1,4})\s*$")
FRONT = re.compile(r"^(description|literature|pronunciation|grammar|introduction|introductory|preface|notes?\b|vocabulary|index|appendix|"
                   r"bibliograph|list of|contents|table|avant|préface|vorwort|einleitung|inhalt|anmerkung|glossar|"
                   r"remarques|[a-z\- ]*folk-?lore$|map\b|corrigenda|errata|addenda)", re.I)


def parse_toc(lines, toc_rx=None):
    e = _parse_toc(lines, toc_rx)
    if len(e) < 6 and not toc_rx:
        e2 = _parse_toc(lines, TOC_DOTS.pattern)
        if len(e2) > len(e):
            return e2
    return e


def _parse_toc(lines, toc_rx=None):
    """Return list of (title, line_index_in_toc). Joins wrapped TOC lines."""
    entries = []
    rx = re.compile(toc_rx) if toc_rx else TOC_LINE
    i = 0
    while i < len(lines):
        l = re.sub(r"\s+", " ", lines[i]).strip()
        m = rx.match(l)
        if not m and TOC_NOPAGE.match(l) and i + 1 < len(lines):
            j = i + 1
            while j < len(lines) and not lines[j].strip() and j < i + 2:
                j += 1
            nxt = re.sub(r"\s+", " ", lines[j]).strip() if j < len(lines) else ""
            if nxt and not TOC_NOPAGE.match(nxt) and re.search(r"\d{1,4}\s*$", nxt):
                m = rx.match(l + " " + nxt)
                if m:
                    i = j
        if m:
            t = re.sub(r"\s*\((?:[A-Z]\.\s?){1,3}\)\s*$", "", m.group("title")).strip(" .·•…_,—-")
            t = re.sub(r"\s+", " ", t)
            if 3 <= len(t) <= 90 and re.search(r"[A-Za-zÀ-ÿ]{3}", t):
                entries.append((t, i))
        i += 1
    return entries


def clean_block(lines, titles_norm, book_heads):
    out = []
    for l in lines:
        s = l.strip()
        if not s:
            out.append("")
            continue
        if re.fullmatch(r"[\d\W_ivxlcIVXLC]{1,12}", s):  # page numbers / garbage
            continue
        ns = norm(re.sub(r"\d+", " ", s))
        if ns in book_heads:
            continue
        if len(s) < 80 and ns and any(ns == t or (len(ns) > 6 and ns in t and len(t) - len(ns) < 6) for t in titles_norm):
            continue  # running head repeating a tale title
        if re.match(r"^(\(?\d{1,2}\)|\d{1,2}\s|[*†‡^])\s?\S", s) and len(s) < 140 and out and out[-1] == "":
            continue  # footnote line after a gap
        out.append(s)
    # paragraphs
    paras, cur = [], []
    for s in out + [""]:
        if s:
            cur.append(s)
        elif cur:
            paras.append(cur)
            cur = []
    res = []
    for p in paras:
        txt = ""
        for s in p:
            if txt.endswith("-") and s[:1].islower():
                txt = txt[:-1] + s
            else:
                txt = (txt + " " + s) if txt else s
        txt = re.sub(r"\s+", " ", txt).strip()
        txt = re.sub(r"(?<=[A-Za-zà-ÿ.,;:!?”\"’)])\d{1,3}(?=[\s,.;:]|$)", "", txt)  # glued footnote numbers
        txt = re.sub(r"\s\((?:\d{1,2}|[ivx]{1,3})\)", "", txt)  # (2) (iv) footnote refs
        txt = txt.replace(",,", "„").replace("**", "“").replace("'*", "“")
        txt = re.sub(r"\s{2,}", " ", txt)
        res.append(txt)
    return res


def split_ocr(path, lang, toc_rx=None, min_ratio=0.10, max_toc_frac=1.0, skip_titles=None):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    toc = parse_toc(lines, toc_rx)
    if not toc:
        return []
    # TOC block = dense cluster of entries; use the largest cluster
    idxs = [i for _, i in toc]
    clusters, cur = [], [toc[0]]
    for e in toc[1:]:
        if e[1] - cur[-1][1] <= 12:
            cur.append(e)
        else:
            clusters.append(cur)
            cur = [e]
    clusters.append(cur)
    clusters = [c for c in clusters if len(c) >= 3]
    if not clusters:
        return []
    entries = [e for c in clusters for e in c]
    toc_lines = set()
    for c in clusters:
        toc_lines.update(range(c[0][1] - 2, c[-1][1] + 3))
    skip = re.compile(skip_titles, re.I) if skip_titles else None
    titles = []
    seen = set()
    for t, _ in entries:
        k = norm(t)
        if k in seen or (skip and skip.search(t)) or FRONT.match(t):
            continue
        seen.add(k)
        titles.append(t)
    tnorm = [norm(t) for t in titles]
    # repeated short lines = running heads
    cnt = collections.Counter(norm(re.sub(r"\d+", " ", l)) for l in lines if 0 < len(l.strip()) < 70)
    book_heads = {k for k, v in cnt.items() if v >= 6 and k and len(k) < 60}
    # locate each title's first heading occurrence in body, in order
    positions = []
    start = 0
    lines_norm = [norm(re.sub(r"^\s*(?:No\.?\s*)?([IVXLC]{1,7}|\d{1,3})\s*[.,:)—–-]+\s*", "", l)) for l in lines]
    for t, tn in zip(titles, tnorm):
        found = None
        for i in range(start, len(lines)):
            if i in toc_lines:
                continue
            ln = lines_norm[i]
            if not ln or len(ln) > len(tn) + 25 or len(ln) < min(8, len(tn)) * 0.6:
                continue
            if ln == tn or difflib.SequenceMatcher(None, ln, tn).ratio() >= 0.82 or (len(tn) > 12 and ln.startswith(tn)):
                found = i
                break
        if found is not None:
            positions.append((found, t))
            start = found + 1
    tales = []
    for k, (pos, t) in enumerate(positions):
        end = positions[k + 1][0] if k + 1 < len(positions) else len(lines)
        if end - pos > 4000:  # runaway segment (probably ran into appendix); cap
            end = pos + 4000
        paras = clean_block(lines[pos + 1:end], tnorm, book_heads)
        keep = [p for p in paras if len(p) > 25 and ratio_lang(p, lang) >= min_ratio]
        body = "\n\n".join(keep)
        if len(body) >= 300:
            tales.append({"title": t, "text": body})
    return tales


if __name__ == "__main__":
    import sys
    tales = split_ocr(sys.argv[1], sys.argv[2])
    print(len(tales))
    for t in tales:
        print(f"  {t['title'][:55]:55s} {len(t['text']):6d}")
    if len(sys.argv) > 3:
        print(tales[int(sys.argv[3])]["text"][:2500])
