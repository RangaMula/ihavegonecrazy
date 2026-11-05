# -*- coding: utf-8 -*-
"""Pictures for Book 76 (Afrikaans). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, leaf, ground


def _petal(bx, by, ang, ln, w, cls):
    a = math.radians(ang)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    tx, ty = bx + ux * ln, by + uy * ln
    c1 = (bx + ux * ln * 0.5 + px * w, by + uy * ln * 0.5 + py * w)
    c2 = (bx + ux * ln * 0.5 - px * w, by + uy * ln * 0.5 - py * w)
    return P(f"M{bx:.1f} {by:.1f} Q{c1[0]:.1f} {c1[1]:.1f} {tx:.1f} {ty:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {bx:.1f} {by:.1f} Z", cls)


def protea():
    """A king protea, the big flower of the Cape fynbos."""
    stem = R(95, 112, 10, 76, "c", 4) + leaf(100, 150, -150, 42) + leaf(100, 172, -30, 42)
    back = "".join(_petal(100 + 8 * math.cos(math.radians(a)), 110, a, 74, 14, "b") for a in (-168, -140, -112, -68, -40, -12))
    dome = E(100, 78, 30, 24, "e") + P("M82 70 l4 6 M94 62 l2 7 M108 62 l-2 7 M118 70 l-4 6 M100 84 l0 6", "n t")
    front = "".join(_petal(100, 116, a, 58, 13, "d") for a in (-160, -125, -55, -20))
    return stem + back + dome + front + ground(188)


def croissant():
    """A croissant on a plate."""
    plate = E(100, 156, 84, 18, "b") + E(100, 154, 64, 11, "a")
    parts = (E(46, 128, 14, 24, "d", -60) + E(154, 128, 14, 24, "d", 60)
             + E(70, 116, 20, 34, "d", -35) + E(130, 116, 20, 34, "d", 35) + E(100, 108, 26, 40, "d"))
    return plate + parts + ground(184)


def jas():
    """A warm coat (jas) with buttons and pockets, on a hook."""
    coat = P("M84 30 L60 38 C46 44 40 60 38 80 L30 150 L50 154 L58 98 L58 180 L142 180 L142 98 L150 154 "
             "L170 150 L162 80 C160 60 154 44 140 38 L116 30 L100 50 Z", "b")
    lapels = P("M84 30 L100 50 L92 82 L74 42 Z", "c") + P("M116 30 L100 50 L108 82 L126 42 Z", "c")
    front = L(100, 50, 100, 180)
    buttons = C(110, 100, 4.5, "d") + C(110, 124, 4.5, "d") + C(110, 148, 4.5, "d")
    pockets = R(66, 134, 22, 6, "e", 2) + R(118, 134, 22, 6, "e", 2)
    hook = P("M100 30 L100 20 C100 12 110 10 112 16", "n")
    return coat + lapels + front + buttons + pockets + hook


def quiche():
    """A quiche: an egg tart in a fluted dish."""
    dish = P("M28 110 L42 152 L158 152 L172 110 Z", "b")
    flutes = "".join(L(x, 114, x + (x - 100) * 0.12, 150, "n t") for x in range(44, 160, 14))
    rim = E(100, 110, 72, 18, "e") + E(100, 110, 58, 12, "d")
    bits = C(80, 108, 4, "a") + C(104, 112, 4, "a") + C(124, 106, 4, "a") + C(92, 104, 3, "c") + C(116, 114, 3, "c")
    steam = P("M80 86 C74 76 86 70 80 58 M100 82 C94 72 106 66 100 54 M120 86 C114 76 126 70 120 58", "n t")
    return dish + flutes + rim + bits + steam + ground(160)


def xilofoon():
    """A xylophone: wooden bars of different lengths, and two beaters."""
    rails = R(18, 90, 166, 8, "e", 3) + R(18, 124, 166, 8, "e", 3)
    bars = ""
    for i in range(7):
        x, top, bot = 24 + i * 22, 56 + i * 5, 162 - i * 5
        bars += R(x, top, 17, bot - top, "abcde"[i % 5], 4) + C(x + 8.5, 94, 2.2, "n") + C(x + 8.5, 128, 2.2, "n")
    beaters = L(40, 192, 78, 172) + C(82, 170, 7, "d") + L(164, 192, 126, 172) + C(122, 170, 7, "d")
    return rails + bars + beaters


def pizza():
    """A pizza cut into slices, on a round board."""
    board = R(150, 96, 44, 14, "b", 6) + C(100, 104, 80, "b")
    base = C(100, 104, 70, "e") + C(100, 104, 60, "d")
    cuts = "".join(L(100, 104, 100 + 60 * math.cos(math.radians(a)), 104 + 60 * math.sin(math.radians(a)), "n t")
                   for a in range(0, 360, 60))
    tops = "".join(C(100 + r * math.cos(math.radians(a)), 104 + r * math.sin(math.radians(a)), 6, "a")
                   for r, a in [(38, 30), (38, 90), (38, 150), (38, 210), (38, 270), (38, 330), (16, 0), (16, 120), (16, 240)])
    return board + base + cuts + tops


def bokaap():
    """Colourful flat-roofed houses of the Bo-Kaap in Cape Town, under Table Mountain."""
    mountain = P("M6 84 L30 46 L56 38 L148 38 L170 48 L194 84 Z", "c")
    out = mountain
    for i, (x, y) in enumerate([(14, 78), (57, 66), (100, 82), (143, 70)]):
        cls = "abde"[i]
        out += R(x, y, 43, 178 - y, cls)
        out += P(f"M{x+6} {y} L{x+6} {y-8} L{x+15} {y-8} L{x+21.5} {y-15} L{x+28} {y-8} L{x+37} {y-8} L{x+37} {y} Z", cls)
        out += R(x + 7, y + 16, 11, 15, "a", 2) + R(x + 25, y + 16, 11, 15, "a", 2)
        out += R(x + 7, y + 44, 11, 15, "a", 2) if 178 - y > 100 else ""
        out += R(x + 25, 146, 12, 32, "c", 2)
        out += C(x + 34, 162, 1.8, "n")
    return out + ground(178)


PICS = {"af_protea": protea, "af_croissant": croissant, "af_jas": jas, "af_quiche": quiche,
        "af_xilofoon": xilofoon, "af_pizza": pizza, "af_bokaap": bokaap}
