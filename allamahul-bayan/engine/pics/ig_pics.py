# -*- coding: utf-8 -*-
"""Pictures for Book 65 (Igbo). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, poly, leaf, ground


def ji():
    """A yam tuber (ji) with a cut slice and a heart-shaped yam leaf on its vine."""
    tuber = P("M30 150 C24 128 40 112 64 108 C96 102 130 98 156 104 C178 110 186 128 176 144 C166 160 140 164 112 164 "
              "C80 166 40 170 30 150 Z", "b")
    marks = P("M56 126 l6 4 M86 118 l5 5 M120 120 l6 3 M146 128 l4 6 M70 148 l6 2 M104 146 l5 4 M138 150 l6 1", "n t")
    roots = P("M40 162 l-6 10 M90 165 l-2 12 M150 160 l6 10", "n t")
    slice_ = E(156, 66, 30, 22, "b", -10) + E(156, 66, 22, 15, "a", -10)
    vine = P("M60 108 C56 80 70 54 96 40", "n")
    lf = P("M96 40 C84 22 104 10 114 24 C124 10 144 22 132 40 C124 52 108 60 96 40 Z", "c")
    return tuber + marks + roots + slice_ + vine + lf + L(114, 26, 112, 48, "n t") + ground(182)


def grass():
    """A tuft of grass (ahịhịa) with a few small wild flowers."""
    blades = ""
    for i, (x, h, lean) in enumerate([(40, 90, -18), (58, 120, -8), (76, 100, 6), (94, 132, -4), (112, 110, 10),
                                      (130, 126, 2), (148, 96, 16), (164, 80, 22)]):
        tip = (x + lean, 170 - h)
        blades += P(f"M{x-7} 170 C{x-6} {170-h*0.5} {tip[0]-2} {tip[1]+20} {tip[0]} {tip[1]} "
                    f"C{tip[0]+3} {tip[1]+22} {x+6} {170-h*0.5} {x+7} 170 Z", "c")
    flowers = ""
    for cx, cy in [(30, 120), (178, 112)]:
        flowers += L(cx, cy + 8, cx + (6 if cx < 100 else -6), 170)
        flowers += "".join(C(cx + 8 * math.cos(math.radians(a)), cy + 8 * math.sin(math.radians(a)), 6, "e") for a in range(0, 360, 72))
        flowers += C(cx, cy, 5, "d")
    return blades + flowers + P("M14 176 C60 168 140 168 186 176 L186 186 L14 186 Z", "b")


def oroma():
    """Oranges (oroma): a whole orange with a leaf and a cut half showing its segments."""
    whole = C(80, 110, 54, "d") + "".join(C(x, y, 2.2, "n") for x, y in [(60, 92), (92, 86), (104, 120), (70, 132), (56, 116), (90, 146)])
    stem = R(76, 52, 8, 10, "c", 2) + leaf(84, 56, -30, 40)
    half = C(150, 150, 34, "d") + C(150, 150, 27, "a")
    segs = "".join(L(150, 150, 150 + 26 * math.cos(math.radians(a)), 150 + 26 * math.sin(math.radians(a)), "n t") for a in range(0, 360, 45))
    return whole + stem + half + segs + C(150, 150, 4, "a") + ground(186)


PICS = {"ig_ji": ji, "ig_grass": grass, "ig_orange": oroma}
