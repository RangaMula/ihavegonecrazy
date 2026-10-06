import sys, importlib
from translit import transliterate, WARNINGS, Warn
mod = importlib.import_module(sys.argv[1])
for d in mod.D:
    items = [l[2] for l in d["lines"]] + [k[0] for k in d["key_phrases"]] + [y[0] for y in d["your_turn"]["lines"]]
    for a in items:
        try:
            bn, en = transliterate(a)
            if len(sys.argv) > 2: print(d["no"], a, "|", bn, "|", en)
        except Warn as e:
            print("ERR", d["no"], e)
print("\n".join(WARNINGS))
