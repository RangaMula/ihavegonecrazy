import html, re, sys, os, urllib.request, concurrent.futures as cf
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ia")
def get(i):
    dst = os.path.join(OUT, i + ".txt")
    if os.path.exists(dst) and os.path.getsize(dst) > 1000:
        return i, os.path.getsize(dst)
    for attempt in range(3):
        try:
            h = urllib.request.urlopen(f"https://archive.org/stream/{i}/{i}_djvu.txt", timeout=180).read().decode("utf-8", "replace")
            m = re.search(r"<pre[^>]*>(.*?)</pre>", h, re.S)
            t = html.unescape(m.group(1)) if m else ""
            open(dst, "w", encoding="utf-8").write(t)
            return i, len(t)
        except Exception as e:
            err = e
    return i, f"ERR {err}"
with cf.ThreadPoolExecutor(6) as ex:
    for r in ex.map(get, sys.argv[1:]): print(*r)
