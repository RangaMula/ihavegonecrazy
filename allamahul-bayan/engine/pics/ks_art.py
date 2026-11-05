# -*- coding: utf-8 -*-
"""Pictures for Book 18 (Kashmiri). Objects, plants and nature only."""
import math
from illos import P, C, E, R, L, poly, star, cloud, leaf, ground


def kangri():
    """A kangri: a small clay fire-pot inside a woven wicker basket with a handle, and glowing embers."""
    weave = "".join(P(f"M{x} 100 C{x-4} 130 {x-2} 150 {x+2*((x-100)/40)} 172", "n t") for x in (60, 76, 92, 108, 124, 140))
    rows = "".join(P(f"M{46+k*2} {y} C80 {y+8} 120 {y+8} {154-k*2} {y}", "n t") for k, y in enumerate((118, 136, 154)))
    return (P("M66 100 C60 40 140 40 134 100", "n") + P("M74 100 C70 52 130 52 126 100", "n")          # handle
            + P("M40 100 L160 100 C158 140 140 172 112 178 L88 178 C60 172 42 140 40 100 Z", "b")   # basket
            + weave + rows
            + E(100, 100, 60, 12, "c")                                                            # clay rim
            + E(100, 98, 46, 7, "d")                                                              # embers
            + C(84, 96, 4, "e") + C(100, 94, 4, "e") + C(116, 96, 4, "e")
            + P("M90 84 q-6 -10 2 -18 M110 84 q6 -10 -2 -18", "n t")
            + R(70, 178, 60, 8, "c", 3) + ground(186))


def tulip(cx=100):
    return (P(f"M{cx} 96 C{cx-2} 130 {cx+2} 160 {cx} 186", "n")
            + P(f"M{cx} 170 C{cx-30} 160 {cx-42} 132 {cx-40} 110 C{cx-20} 124 {cx-6} 146 {cx} 170 Z", "c")
            + P(f"M{cx} 160 C{cx+28} 150 {cx+40} 126 {cx+36} 104 C{cx+18} 118 {cx+6} 138 {cx} 160 Z", "c")
            + P(f"M{cx-30} 50 L{cx-18} 66 L{cx} 40 L{cx+18} 66 L{cx+30} 50 C{cx+34} 80 {cx+22} 98 {cx} 98 "
                f"C{cx-22} 98 {cx-34} 80 {cx-30} 50 Z", "e")
            + P(f"M{cx-12} 64 C{cx-10} 78 {cx-4} 90 {cx} 96 M{cx+12} 64 C{cx+10} 78 {cx+4} 90 {cx} 96", "n t"))


def tulips():
    return tulip(100) + cloud(18, 46, 0.5) + C(166, 36, 14, "d") + P("M40 186 C50 174 60 174 66 186 M134 186 C142 174 154 174 160 186", "n t") + ground(186)


def rose():
    head = (P("M60 70 C56 40 80 28 100 36 C120 28 144 40 140 70 C138 96 120 108 100 108 C80 108 62 96 60 70 Z", "e")
            + P("M74 60 C80 44 120 44 126 60 C116 54 84 54 74 60 Z", "a")
            + P("M88 66 C88 54 112 54 112 66 C112 76 96 78 94 68", "n")
            + P("M66 80 C80 98 120 98 134 80", "n t"))
    return (P("M100 108 C98 140 104 160 100 186", "n") + leaf(100, 150, -150, 40) + leaf(102, 132, -30, 40)
            + P("M80 104 L100 120 L120 104 Z", "c") + head + ground(186))


def snow():
    """A snowflake over snowy mountains."""
    def flake(cx, cy, r, cls):
        out = C(cx, cy, r * 0.22, cls)
        for a in range(0, 360, 60):
            x2, y2 = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
            out += L(cx, cy, x2, y2, "n")
            for t in (0.55, 0.8):
                bx, by = cx + r * t * math.cos(math.radians(a)), cy + r * t * math.sin(math.radians(a))
                for s in (-40, 40):
                    out += L(bx, by, bx + r * 0.22 * math.cos(math.radians(a + s)), by + r * 0.22 * math.sin(math.radians(a + s)), "n")
        return out
    return (P("M10 186 L70 100 L104 146 L134 104 L190 186 Z", "b")
            + P("M70 100 L56 120 L66 116 L72 126 L80 114 L88 120 Z", "a")
            + P("M134 104 L122 122 L132 118 L138 128 L146 118 L152 122 Z", "a")
            + flake(100, 52, 38, "d") + flake(32, 40, 16, "d") + flake(170, 60, 14, "d") + ground(186))


PICS = {"ks_kangri": kangri, "ks_tulip": tulips, "ks_rose": rose, "ks_snow": snow}
