#!/usr/bin/env python3
"""Run a pronunciation scheme over every Arabic entry and report problems.

    python3 tools/check_pron.py bn          # summary + words the engine could not read
    python3 tools/check_pron.py ja 3 27     # also print entries 3 and 27
"""
import json, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))
from scripts import pronounce, SCHEMES  # noqa: E402


def main(argv):
    if not argv or argv[0] not in SCHEMES:
        sys.exit("usage: check_pron.py <%s> [entry numbers…]" % "|".join(SCHEMES))
    scheme, show = argv[0], set(map(int, argv[1:]))
    data = json.load(open(os.path.join(ROOT, "data", "arabic", "muwatta.json"), encoding="utf-8"))
    warns, crashed = collections.Counter(), []
    for e in data["entries"]:
        w = []
        try:
            out = pronounce(e["ar"], scheme, w)
        except Exception as ex:          # a renderer bug: report, keep going
            crashed.append((e["n"], repr(ex)))
            continue
        for x in w:
            warns[x] += 1
        if e["n"] in show:
            print(f"\n# {e['n']}\n{e['ar']}\n{out}")
    print(f"\nscheme {scheme}: {len(data['entries'])} entries, {sum(warns.values())} unreadable words, "
          f"{len(crashed)} renderer errors")
    for x, c in warns.most_common(40):
        print(f"  {c}× {x}")
    for n, ex in crashed[:20]:
        print(f"  ERROR entry {n}: {ex}")
    sys.exit(1 if crashed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
