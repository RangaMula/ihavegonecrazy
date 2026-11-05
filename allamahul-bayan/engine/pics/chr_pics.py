# -*- coding: utf-8 -*-
"""Pictures for Book 54 (Cherokee). Keys prefixed chr_. Objects, plants and nature only.
(File is named chr_pics.py, not chr.py: a plug-in called chr.py would be imported as module `chr`
before build.py imports languages/chr.py, and would shadow the language file.)"""
import math
from illos import P, C, E, R, L, poly, star, leaf, ground


def wood():
    """A neat pile of cut logs, seen from the end."""
    out = ""
    for cx, cy, cls in [(52, 150, "b"), (100, 150, "c"), (148, 150, "b"), (76, 108, "c"), (124, 108, "b"), (100, 66, "c")]:
        out += C(cx, cy, 24, cls) + C(cx, cy, 15, "n t") + C(cx, cy, 6, "n t")
    return out + ground(176)


def grass():
    def blade(x, tx, ty, cls):
        return P(f"M{x-6} 180 Q{x-2} 130 {tx} {ty} Q{x+4} 132 {x+6} 180 Z", cls)
    out = ""
    for x, tx, ty, cls in [(40, 22, 70, "c"), (56, 60, 40, "b"), (72, 90, 64, "c"), (88, 80, 30, "b"), (104, 112, 50, "c"),
                           (120, 140, 34, "b"), (136, 126, 70, "c"), (152, 176, 52, "b"), (164, 182, 96, "c")]:
        out += blade(x, tx, ty, cls)
    return out + ground(180)


def acorn():
    return (R(95, 40, 10, 22, "c", 4) + leaf(110, 48, -20, 34)
            + P("M66 98 C66 140 90 170 100 178 C110 170 134 140 134 98 Z", "d")
            + P("M54 98 C54 66 146 66 146 98 C146 106 54 106 54 98 Z", "b")
            + "".join(L(x, 74 + abs(x - 100) * 0.12, x + 8, 100, "n t") for x in range(64, 140, 14))
            + P("M84 120 C84 136 90 148 98 156", "n t"))


def snow():
    arms = ""
    for a in range(0, 360, 60):
        g = f'<g transform="rotate({a} 100 96)">'
        arms += (g + R(95, 30, 10, 60, "e", 5)
                 + poly([(100, 52), (118, 36), (122, 42), (104, 60)], "d")
                 + poly([(100, 52), (82, 36), (78, 42), (96, 60)], "d") + "</g>")
    return (arms + poly([(100 + 16 * math.cos(math.radians(a)), 96 + 16 * math.sin(math.radians(a))) for a in range(0, 360, 60)], "b")
            + star(28, 172, 8, 3.5, "e", 6) + star(172, 172, 8, 3.5, "e", 6) + star(170, 26, 7, 3, "e", 6))


def fire():
    return (f'<g transform="rotate(-14 100 168)">' + R(36, 158, 128, 20, "b", 10) + "</g>"
            + f'<g transform="rotate(14 100 168)">' + R(36, 158, 128, 20, "c", 10) + "</g>"
            + P("M100 30 C120 60 150 80 144 120 C140 148 120 160 100 160 C80 160 60 148 56 120 C52 96 72 86 76 64 "
                "C88 76 90 88 92 96 C96 74 92 52 100 30 Z", "d")
            + P("M100 90 C112 106 124 116 120 134 C118 148 108 152 100 152 C92 152 82 148 80 134 C78 120 92 112 100 90 Z", "e"))


def rock():
    return (P("M22 176 C18 140 40 112 76 108 C110 104 128 130 126 176 Z", "b")
            + P("M110 176 C108 146 128 124 154 124 C178 124 188 150 184 176 Z", "c")
            + P("M64 110 C62 86 84 70 104 74 C124 78 132 98 120 118 C108 116 86 106 64 110 Z", "d")
            + P("M48 140 L62 128 L72 136", "n t") + P("M146 146 L156 140 L166 150", "n t") + P("M92 86 L100 94", "n t")
            + ground(176))


def beans():
    pod = P("M24 116 C40 64 120 46 178 64 C170 90 120 130 70 136 C46 138 30 132 24 116 Z", "c")
    seeds = "".join(E(x, y, 15, 11, "d", r) for x, y, r in [(58, 108, -20), (92, 96, -18), (126, 84, -16), (156, 72, -14)])
    loose = "".join(P(f"M{x} {y} c-14 -2 -20 -18 -6 -24 c8 -4 12 4 20 2 c12 -2 18 10 8 18 c-6 6 -14 6 -22 4 Z", "b")
                    for x, y in [(56, 172), (104, 180), (150, 170)])
    return pod + seeds + P("M178 64 C184 54 188 48 194 46", "n") + loose + ground(186)


def coins():
    stack = "".join(E(70, y, 42, 12, "d") for y in (168, 156, 144, 132, 120))
    return (stack + C(140, 120, 40, "d") + C(140, 120, 30, "n t") + R(130, 104, 20, 32, "n t", 4) + ground(184))


def count(n=3):
    """n round pebbles to count, in neat rows."""
    per = 4 if n <= 8 else 5
    rows = [per] * (n // per) + ([n % per] if n % per else [])
    if n in (3, 5, 6):
        rows = {3: [2, 1], 5: [3, 2], 6: [3, 3]}[n]
    r = 15 if per == 5 else 17
    gap = 2 * r + 8
    top = 100 - (len(rows) - 1) * gap / 2
    out = R(14, 22, 172, 156, "a", 20)
    cls = "bcde"
    k = 0
    for i, m in enumerate(rows):
        y = top + i * gap
        x0 = 100 - (m - 1) * gap / 2
        for j in range(m):
            out += C(x0 + j * gap, y, r, cls[k % 4]); k += 1
    return out


def slate(text="Ꭰ", size=None):
    """A little writing slate with the syllable on it (for sound-practice pages)."""
    fs = size or min(92, int(250 / max(len(text), 1)))
    return (R(18, 34, 164, 128, "b", 12) + R(32, 48, 136, 100, "a", 6)
            + f'<text x="100" y="{98 + fs * 0.36:.0f}" text-anchor="middle" font-size="{fs}">{text}</text>'
            + R(120, 168, 44, 10, "e", 4) + R(40, 166, 14, 14, "d", 3))


PICS = {"chr_wood": wood, "chr_grass": grass, "chr_acorn": acorn, "chr_snow": snow, "chr_fire": fire, "chr_rock": rock,
        "chr_beans": beans, "chr_coins": coins, "chr_count": count, "chr_slate": slate}
