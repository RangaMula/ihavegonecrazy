# -*- coding: utf-8 -*-
"""Validate the Arabic book's data files (PLAYBOOK §5). Run: python3 validate.py"""
import json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "data")
HARAKAT = re.compile("[ً-ٰٟۡـ]")
LATIN = re.compile("[A-Za-z]")
BAD_BN = re.compile("[A-Za-z]")          # Latin letters in bn_pron (ʿ ʾ ː are not A-Z)
BANNED = ["خِنْزِير", "خنزير", "خمر", "نبيذ", "بيرة", "كحول", "ويسكي"]
FIELDS = ("fr", "bn_pron", "en_pron", "bn", "en")
KNOWN = set()
for line in open(os.path.join(HERE, "STYLE.md"), encoding="utf-8").read().split("## 8.")[1].splitlines():
    for m in re.finditer(r"([؀-ۿً-ْ]+)\s+[ঀ-৿]", line):
        KNOWN.add(HARAKAT.sub("", m.group(1)))

def bare(s):
    s = HARAKAT.sub("", s).strip()
    s = re.sub(r"[؟?!.،,]", "", s)
    s = re.sub(r"^ال", "", s)
    return s.translate(str.maketrans("أإآٱ", "اااا"))

KNOWN = {bare(k) for k in KNOWN}
errors = []
def err(where, msg):
    errors.append("%s: %s" % (where, msg))

def walk(o, where, allow_banned=False):
    """Check every Triple Row (a dict with 'fr') anywhere in the structure."""
    if isinstance(o, dict):
        if "fr" in o and isinstance(o["fr"], str):
            for k in FIELDS:
                if not str(o.get(k, "")).strip():
                    err(where, "missing %s in %r" % (k, o.get("fr")))
            if LATIN.search(o["fr"]):
                err(where, "Latin letters in fr: %r" % o["fr"])
            if BAD_BN.search(o.get("bn_pron", "")):
                err(where, "Latin letters in bn_pron: %r" % o.get("bn_pron"))
            if not allow_banned and any(b in HARAKAT.sub("", o["fr"]) for b in BANNED):
                err(where, "banned word: %r" % o["fr"])
        for k, v in o.items():
            walk(v, where + "." + k, allow_banned)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, "%s[%d]" % (where, i), allow_banned)

def load(n):
    p = os.path.join(D, n)
    if not os.path.exists(p):
        print("MISSING", n); return None
    return json.load(open(p, encoding="utf-8"))

seen = collections.defaultdict(list)
nwords = 0
for n in ("journey_1_10.json", "journey_11_20.json"):
    d = load(n)
    if not d:
        continue
    walk(d, n)
    for sec in d["sections"]:
        w = "%s §%s" % (n, sec["no"])
        if len(sec.get("sets", [])) != 4: err(w, "sets != 4")
        if len(sec.get("say_now", [])) != 5: err(w, "say_now != 5")
        if len(sec.get("quiz", [])) != 10: err(w, "quiz != 10")
        if len(sec.get("can_do_bn", [])) != 3: err(w, "can_do != 3")
        for st in sec["sets"]:
            if len(st["words"]) != 25: err(w, "set %s has %d words" % (st["code"], len(st["words"])))
            for x in st["words"]:
                nwords += 1
                seen[bare(x["fr"])].append(st["code"])
                if bare(x["fr"]) in KNOWN: err(w, "Ch. 4 word reused: %s" % x["fr"])
                if st["kind"] == "C":
                    for k in ("icon", "story_bn", "source_hint"):
                        if not x.get(k): err(w, "culture word %s lacks %s" % (x["fr"], k))
    for m in d.get("milestones", []):
        if not 8 <= len(m.get("reading", [])) <= 12: err(n, "milestone %s reading count %d" % (m.get("after_section"), len(m.get("reading", []))))
dups = {k: v for k, v in seen.items() if len(v) > 1}
print("journey words:", nwords, "unique:", len(seen), "duplicates:", len(dups))
for k, v in sorted(dups.items()):
    print("  DUP", k, v)

for n in ("part2.json", "part3.json"):
    d = load(n)
    if d: walk(d, n)
d = load("part2.json")
if d:
    letters = [L["letter"] for g in d["ch6"]["groups"] for L in g["letters"]]
    need = set("ابتثجحخدذرزسشصضطظعغفقكلمنهويء")
    miss = need - set(letters)
    if miss: err("part2", "letters missing: %s" % " ".join(sorted(miss)))
    for g in d["ch6"]["groups"]:
        for L in g["letters"]:
            if len(L.get("forms", {})) != 4: err("part2", "forms for %s" % L["letter"])
            if len(L.get("words", [])) != 5: err("part2", "words for %s: %d" % (L["letter"], len(L.get("words", []))))
d = load("part5.json")
if d:
    walk(d, "part5.json")
    for k, n in (("dialogues", 20), ("readings", 6), ("literature", 10), ("writing3", 8), ("selftest", 60), ("can_do", 25)):
        if len(d.get(k, [])) != n: err("part5", "%s count %d (want %d)" % (k, len(d.get(k, [])), n))

print("\n".join(errors[:200]))
print("ERRORS:", len(errors) + len(dups))
sys.exit(1 if errors or dups else 0)
