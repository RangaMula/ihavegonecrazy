# -*- coding: utf-8 -*-
"""Pictures for Book 22 (Konkani). Objects, plants and nature only (viewBox 0 0 200 200)."""
from illos import P, C, E, R, L, leaf, ground


def cashew():
    """काजू - the cashew apple with its nut hanging below it."""
    apple = P("M62 40 C92 30 132 32 146 48 C156 62 150 96 138 118 C128 136 112 142 100 142 "
              "C86 142 70 134 62 116 C50 92 46 56 62 40 Z", "e")
    shine = P("M76 60 C72 74 72 92 78 106", "n t")
    nut = P("M84 140 C76 150 74 168 88 178 C100 186 116 180 118 168 C120 158 110 156 104 160 "
            "C98 164 94 158 98 150 C100 144 96 138 84 140 Z", "b")
    stem = P("M100 36 C102 24 108 16 118 10", "n")
    return apple + shine + nut + stem + leaf(118, 12, -10, 46) + leaf(110, 16, -150, 34) + ground(188)


def mushroom():
    """अळमी - wild monsoon mushrooms."""
    def one(cx, base, w, h, cls):
        cap = P(f"M{cx-w} {base-h} C{cx-w} {base-h-h*0.9} {cx+w} {base-h-h*0.9} {cx+w} {base-h} Z", cls)
        stem = P(f"M{cx-w*0.32} {base-h} L{cx-w*0.38} {base} L{cx+w*0.38} {base} L{cx+w*0.32} {base-h} Z", "a")
        dots = "".join(E(cx + dx * w, base - h - dy * h, w * 0.12, h * 0.1, "a")
                       for dx, dy in ((-0.5, 0.35), (0.1, 0.6), (0.55, 0.3)))
        return stem + cap + dots
    grass = "".join(P(f"M{x} 182 q4 -16 {d} -26", "n") for x, d in ((22, 4), (34, -6), (150, 8), (168, -4), (182, 6)))
    return one(80, 182, 52, 70, "e") + one(148, 182, 30, 40, "b") + grass + ground(182)


def pao():
    """पाव - Goan bread rolls on a tray."""
    buns = ""
    for i, x in enumerate((44, 82, 120, 158)):
        buns += P(f"M{x-22} 132 C{x-24} 96 {x+24} 96 {x+22} 132 Z", "b")
        buns += P(f"M{x-10} 108 C{x-4} 104 {x+6} 104 {x+10} 108", "n t")
    top = "".join(P(f"M{x-20} 98 C{x-20} 62 {x+20} 62 {x+20} 98 Z", "b") for x in (63, 101, 139))
    top += "".join(P(f"M{x-8} 76 C{x-2} 72 {x+6} 72 {x+10} 76", "n t") for x in (63, 101, 139))
    tray = P("M14 132 L186 132 L174 156 L26 156 Z", "c")
    return top + buns + tray + ground(170)


PICS = {"kok_cashew": cashew, "kok_mushroom": mushroom, "kok_pao": pao}
