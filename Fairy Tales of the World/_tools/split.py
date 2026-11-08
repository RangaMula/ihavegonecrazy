"""Download a GITenberg book (HTML) and split it into individual tales.

Usage (as module): split_book(repo, meta) -> list of {"title", "text"}
Strategy: strip the Project Gutenberg header/footer, look at h1-h4 headings,
pick the heading level whose titles best match the book's table of contents
(or, failing that, the level with the most story-like headings), and take the
content between consecutive headings of that level as one tale.
"""
import os, re, json, difflib, urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "books")
os.makedirs(CACHE, exist_ok=True)
RAW = "https://raw.githubusercontent.com/GITenberg/{repo}/master/{path}"

SKIP = re.compile(
    r"^(the\s+)?(contents?|table of contents|preface|prefatory|foreword|introduction|introductory|"
    r"notes?( and references)?|index|illustrations?|list of illustrations|footnotes?|appendix|"
    r"glossary|bibliography|transcriber|errata|dedication|to the reader|advertisement|"
    r"publisher|the end|finis|chapter [ivxlc\d]+\.?$|part [ivxlc\d]+|book [ivxlc\d]+|"
    r"volume|vol\.|full project gutenberg|project gutenberg|section|start of|end of|"
    r"by |illustrated|translated|with illustrations|copyright|printed|"
    r"[ivxlc]+\.?$|\d+\.?$)",
    re.I,
)


STOP = re.compile(r"^(the\s+)?(notes and (references|parallels)|index|glossary|bibliography|vocabulary|glossary and index)\b\.?$", re.I)
JUNK = re.compile(
    r"^\(?\d+\)?\.?$|^to [A-Z][a-z]+ |illustrations?\b|frontispiece|\bvid\. p\.|\bp\. \d|\[l|"
    r"^geological|^historical|^history of|treaty|^the eastern band|^the western band|^tribal|^ethnolog|"
    r"^dedicat|^acknowledg|^contents|^introduct|^preface|^pronunciation|^key to|^map\b|"
    r"^colophon|^availability|^corrections?$|^encoding|^revision history|^external references|"
    r"^part (the )?(first|second|third|fourth|one|two|three)|^remarks about|^further comment|^variations? of|version$|^pastorales$|"
    r"^chapter [a-z]+$|^(january|february|march|april|may|june|july|august|september|october|november|december) \d|"
    r"\bnote\b|^editor|^mrs\.|^mr\. [A-Z]\.|^scene:|^the story of these|^the legends$|^the traditions of|"
    r"folk tales retold$|^[a-z]+ tales$|^stories of oriental|^translator|^song of|^a song|"
    r"\bpages? \d|\. pages?\b|erd[ée]lyi|^\(|^inhoud|^inleiding|^voorwoord|^vorwort|^inhalt|^einleitung|^pr[ée]face|^sommaire|"
    r"^chapitre\b|^avant-propos|^remarques|^nota$|^’n paar woorde|^'n paar woorde|^argumento|^books by|^altemus|^table des|^índice|^pr[óo]logo|"
    r"^introducci[óo]n|^[íi]ndice|^figure$|\d(st|nd|rd|th) figure|^klipgereedskappe|\bnotes\b|version of|^\d+\s*re partie|\bpartie$|\s[ivxlc]+\.?\s?\d+$|^contents$",
    re.I,
)


BOOK_START = {"45634": re.compile(r"THE MYTHS", re.I)}


def is_junk(title, meta):
    if JUNK.search(title):
        return True
    if re.search(r",\s*[ivxlc]+\.\s*\d", title, re.I):  # citation like "Erdélyi, iii. 2"
        return True
    bt = norm(meta.get("title") or "")
    if bt and norm(title) and (norm(title) == bt or bt.startswith(norm(title)) and len(norm(title)) > 8):
        return True
    for p in ("creator", "contributor"):
        x = meta.get(p) or {}
        names = []
        if isinstance(x, dict):
            for v in x.values():
                for a in (v if isinstance(v, list) else [v]):
                    if isinstance(a, dict) and a.get("agent_name"):
                        names.append(a["agent_name"])
        for n in names:
            sur = norm(n.split(",")[0])
            if sur and len(sur) > 3 and sur in norm(title) and len(norm(title)) < len(sur) + 12:
                return True
    return False


def apply_stop(tales_with_flags):
    """tales_with_flags: list of (title, text, is_stop). Drop everything after a STOP heading once 3 tales found."""
    out = []
    for title, text, stop in tales_with_flags:
        if stop and len(out) >= 3:
            break
        if not stop:
            out.append((title, text))
    return out


def fetch(repo):
    gid = repo.rsplit("_", 1)[-1]
    dst = os.path.join(CACHE, repo + ".htm")
    if os.path.exists(dst):
        return open(dst, encoding="utf-8", errors="replace").read()
    for path in (f"{gid}-h/{gid}-h.htm", f"{gid}-h/{gid}-h.html", f"{gid}-h.htm"):
        try:
            with urllib.request.urlopen(RAW.format(repo=repo, path=path), timeout=60) as r:
                data = r.read()
            for enc in ("utf-8", "cp1252", "latin-1"):
                try:
                    html = data.decode(enc)
                    break
                except UnicodeDecodeError:
                    continue
            open(dst, "w", encoding="utf-8").write(html)
            return html
        except Exception:
            continue
    return None


def strip_pg(html):
    s = re.search(r"\*\*\*\s*START OF (THE|THIS) PROJECT GUTENBERG[^*]*\*\*\*", html, re.I)
    e = re.search(r"\*\*\*\s*END OF (THE|THIS) PROJECT GUTENBERG", html, re.I)
    if s:
        html = html[s.end():]
        if e:
            e = re.search(r"\*\*\*\s*END OF (THE|THIS) PROJECT GUTENBERG", html, re.I)
            html = html[: e.start()] if e else html
    else:
        html = re.sub(r'(?s)<(div|section)[^>]*id="pg-(header|footer)".*?</\1>', "", html)
    return html


def clean_title(t):
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"^\[\s*", "", t)
    t = re.sub(r"^(p\.|pg\.?)?\s*[\divxlc]+\s*\]\s*", "", t, flags=re.I)
    t = re.sub(r"(?<![Tt]he)(?<![Oo]f)(?<![Aa]nd)(?<=[^\W\d_]|[;,.’'·])\s?\d{1,3}(?=[\s;,—]|$)", "", t)
    t = re.sub(r"^p\.\s*[ivxlc\d]+\s+", "", t, flags=re.I)
    t = re.sub(r"\[\s*(fn#?)?\d+\s*\]?", "", t, flags=re.I)
    t = re.sub(r"\s*ToC$", "", t)
    t = re.sub(r"^\(\s*\d+\s*\)\s*", "", t)
    t = re.sub(r"^(chapter|tale|story|no\.?)\s+[ivxlc\d]+[.:—-]*\s*", "", t, flags=re.I)
    t = re.sub(r"^[ivxlc\d]+[.:)\]—-]+\s*", "", t, flags=re.I)
    if t.isupper():
        t = re.sub(r"^[IVXLC]+\s+(?=[A-Z]{2})", "", t)
    t = re.sub(r"\[(fn)?#?\d+\]?$|\s*\[\d+\]$", "", t, flags=re.I)
    t = re.sub(r"[.,]?\s+\d{1,3}\s*$|\.\s*\d{1,3}\s*$", "", t)
    t = re.sub(r"\s+", " ", t).strip(" .:—-*[]")
    return t


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def block_text(nodes):
    out = []
    for n in nodes:
        if isinstance(n, NavigableString):
            s = str(n).strip()
            if s:
                out.append(s)
            continue
        if not isinstance(n, Tag):
            continue
        for bad in n.select("span.pagenum, .pagenum, img, script, style, a.pginternal sup, .figcenter, .caption, .footnotes"):
            bad.decompose()
        for a in n.find_all("a"):
            href = (a.get("href") or "")
            txt = a.get_text(strip=True)
            if href.startswith("#") and re.fullmatch(r"[\[\(]?\s*(\d{1,3}|[a-z]|[ivx]{1,4}|[*†‡])\s*[\]\)]?", txt or "", re.I):
                a.decompose()
        for sup in n.find_all("sup"):
            if re.fullmatch(r"\[?\d{1,3}\]?|[*†‡]", sup.get_text(strip=True)):
                sup.decompose()
        if n.name in ("p", "div", "blockquote", "pre", "h5", "h6", "li", "table", "dl", "center", "span", "i", "em", "b"):
            if n.name in ("div", "blockquote") and n.find(["p"]):
                out.extend(block_text(list(n.children)))
                continue
            s = n.get_text(" ", strip=False)
            s = re.sub(r"[ \t\r\f\v]+", " ", s)
            s = re.sub(r"\s*\n\s*", "\n" if n.name == "pre" or "poem" in " ".join(n.get("class", [])) else " ", s).strip()
            if s:
                if n.name == "blockquote":
                    s = "\n".join("> " + x for x in s.split("\n"))
                out.append(s)
        elif n.name == "hr":
            out.append("* * *")
    text = "\n\n".join(out)
    text = re.sub(r"\[Pg \d+\]|\[\d+\]", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_text(repo):
    gid = repo.rsplit("_", 1)[-1]
    dst = os.path.join(CACHE, repo + ".txt")
    if os.path.exists(dst):
        return open(dst, encoding="utf-8").read()
    for path in (f"{gid}-0.txt", f"{gid}.txt", f"{gid}-8.txt"):
        try:
            with urllib.request.urlopen(RAW.format(repo=repo, path=path), timeout=60) as r:
                data = r.read()
        except Exception:
            continue
        for enc in ("utf-8", "cp1252", "latin-1"):
            try:
                txt = data.decode(enc)
                break
            except UnicodeDecodeError:
                continue
        open(dst, "w", encoding="utf-8").write(txt)
        return txt
    return None


def para_text(lines):
    paras, cur = [], []
    for ln in lines + [""]:
        if ln.strip():
            cur.append(ln.rstrip())
        elif cur:
            poem = sum(1 for c in cur if c.startswith("  ")) >= max(1, len(cur) // 2)
            p = "\n".join(c.strip() for c in cur) if poem else " ".join(c.strip() for c in cur)
            paras.append(p)
            cur = []
    out = []
    for p in paras:
        if re.match(r"^\[(illustration|transcriber|footnote|sidenote)", p, re.I) and p.endswith("]"):
            continue
        p = re.sub(r"\[Illustration[^\]]*\]", "", p).strip()
        p = re.sub(r"_([^_]+)_", r"*\1*", p)
        if p:
            out.append(p)
    return "\n\n".join(out)


def split_text(repo, meta):
    txt = fetch_text(repo)
    if not txt:
        return []
    txt = txt.replace("\r\n", "\n")
    s = re.search(r"\*\*\*\s*START OF (THE|THIS) PROJECT GUTENBERG[^\n]*", txt, re.I)
    e = re.search(r"\*\*\*\s*END OF (THE|THIS) PROJECT GUTENBERG", txt, re.I)
    if s:
        txt = txt[s.end(): e.start() if e and e.start() > s.end() else None]
    lines = txt.split("\n")
    toc = [norm(clean_title(x)) for x in re.split(r"\s+--\s+", (meta.get("tableOfContents") or "")) if x.strip()]
    cands = []
    for i, ln in enumerate(lines):
        t = ln.strip()
        if not (2 <= len(t) <= 80) or (i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].strip().isupper()):
            continue
        blanks = 0
        j = i - 1
        while j >= 0 and not lines[j].strip():
            blanks += 1
            j -= 1
        letters = [c for c in t if c.isalpha()]
        if not letters:
            continue
        caps = sum(c.isupper() for c in letters) / len(letters) > 0.85
        title = clean_title(t)
        if title and STOP.match(title) and caps and blanks >= 2 and sum(1 for c in cands if c[1]) >= 3:
            cands.append((i, "__STOP__"))
            break
        if not title or SKIP.match(title) or is_junk(title, meta):
            if blanks >= 2 and caps:
                cands.append((i, None))  # boundary without a tale title
            continue
        tocmatch = bool(toc) and bool(difflib.get_close_matches(norm(title), toc, 1, 0.75))
        if (tocmatch and blanks >= 1) or (caps and blanks >= 2 and (not toc or tocmatch)):
            cands.append((i, title))
    out = []
    for k, (i, title) in enumerate(cands):
        if title is None or title == "__STOP__":
            continue
        end = cands[k + 1][0] if k + 1 < len(cands) else len(lines)
        body = para_text(lines[i + 1:end])
        out.append({"title": titlecase_simple(title), "text": body})
    return [t for t in out if 250 <= len(t["text"]) <= 200000]


def titlecase_simple(t):
    return t.title().replace("'S ", "'s ").replace("’S ", "’s ") if t.isupper() else t


def dedupe_longest(tales):
    best, order = {}, []
    for t in tales:
        k = norm(t["title"]).replace(" ", "")
        if k not in best:
            order.append(k)
            best[k] = t
        elif len(t["text"]) > len(best[k]["text"]):
            best[k] = t
    return [best[k] for k in order]


def split_book(repo, meta):
    if meta.get("presplit"):
        return json.load(open(os.path.join(CACHE, repo + ".tales.json"), encoding="utf-8"))
    return dedupe_longest(_split_book(repo, meta))


def _split_book(repo, meta):
    html = fetch(repo)
    if not html:
        return split_text(repo, meta)
    soup = BeautifulSoup(strip_pg(html), "html.parser")
    body = soup.body or soup
    toc = [norm(clean_title(x)) for x in re.split(r"\s+--\s+", (meta.get("tableOfContents") or "")) if x.strip()]
    heads = body.find_all(["h1", "h2", "h3", "h4"])
    best, best_score = None, -1
    for lvl in ("h1", "h2", "h3", "h4"):
        hs = [h for h in heads if h.name == lvl]
        titles = [clean_title(h.get_text(" ")) for h in hs]
        story = [t for t in titles if t and not SKIP.match(t) and len(t) < 120]
        if len(story) < 2:
            continue
        if toc:
            match = sum(1 for t in story if difflib.get_close_matches(norm(t), toc, 1, 0.75))
            score = match * 10 + len(story) * 0.1
        else:
            score = len(story)
        if score > best_score:
            best, best_score = lvl, score
    if not best:
        return []
    rank = {"h1": 1, "h2": 2, "h3": 3, "h4": 4}
    level = rank[best]
    # flatten document order: walk all descendants and cut at heading boundaries
    tales, cur_title, cur_nodes = [], None, []
    start_rx = BOOK_START.get(repo.rsplit("_", 1)[-1])
    started = start_rx is None
    # sub-headings (lower level) inside a tale are kept as text
    for el in body.descendants:
        if not isinstance(el, Tag):
            continue
        if not started:
            if el.name in rank and start_rx.search(el.get_text(" ")):
                started = True
            continue
        if el.name in rank and rank[el.name] <= level:
            if cur_title is not None:
                tales.append((cur_title, cur_nodes))
            t = clean_title(el.get_text(" "))
            if STOP.match(t) and len(tales) >= 3:
                tales.append(("__STOP__", []))
            cur_title = t if rank[el.name] == level else None
            cur_nodes = []
        elif cur_title is not None and el.name in ("p", "pre", "blockquote", "table", "hr", "h5", "h6", "dl") or (
            cur_title is not None and el.name in rank and rank[el.name] > level
        ):
            # only take top-most block elements (skip p inside an already-taken blockquote)
            if not any(p in cur_nodes for p in el.parents):
                cur_nodes.append(el)
    if cur_title is not None:
        tales.append((cur_title, cur_nodes))
    out, seen = [], set()
    for title, nodes in tales:
        if title == "__STOP__":
            break
        if not title or SKIP.match(title) or len(title) > 120 or is_junk(title, meta):
            continue
        sub = []
        for n in nodes:
            if n.name in rank:
                sub.append(NavigableString("\n" + "### " + clean_title(n.get_text(" ")) + "\n"))
            else:
                sub.append(n)
        text = block_text(sub)
        if len(text) < 250 or len(text) > 200000:
            continue
        out.append({"title": title.title() if title.isupper() else title, "text": text})
    return out


if __name__ == "__main__":
    import sys
    repo = sys.argv[1]
    meta = json.load(open(os.path.join(HERE, "meta", repo + ".json")))
    tales = split_book(repo, meta)
    print(len(tales))
    for t in tales:
        print(f"  {t['title'][:60]:60s} {len(t['text']):7d}")
    if len(sys.argv) > 2:
        print(tales[int(sys.argv[2])]["text"][:3000])
