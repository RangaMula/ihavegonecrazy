# -*- coding: utf-8 -*-
"""Pictures for Book 29 (Uyghur). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, poly, leaf, ground


def table():          # جوزا joza - a low wooden table with a bowl and a teapot-free cup
    return (R(22, 92, 156, 16, "b", 4)                       # table top
            + R(30, 108, 140, 12, "e", 2)                    # apron
            + R(36, 120, 14, 64, "b", 3) + R(150, 120, 14, 64, "b", 3)
            + R(64, 120, 10, 50, "e", 3) + R(126, 120, 10, 50, "e", 3)
            + P("M70 92 C70 66 130 66 130 92 Z", "a")         # bowl
            + P("M70 92 L130 92", "n")
            + C(86, 70, 9, "d") + C(104, 66, 10, "c") + C(118, 72, 8, "d")  # fruit in the bowl
            + ground(184))


def candle():         # شام sham - a candle with a flame on a dish
    return (E(100, 170, 64, 14, "e")
            + R(76, 70, 48, 98, "a", 6)
            + P("M76 84 C88 92 96 80 104 90 C110 98 118 86 124 92", "n t")
            + L(100, 70, 100, 58, "n")
            + P("M100 18 C114 36 116 50 100 60 C84 50 86 36 100 18 Z", "d")
            + P("M100 34 C106 42 106 50 100 54 C94 50 94 42 100 34 Z", "c")
            + P("M148 120 c4 -4 10 -4 14 0 c-4 4 -10 4 -14 0 Z", "n t")
            + L(40, 40, 52, 48, "n t") + L(160, 40, 148, 48, "n t") + L(30, 70, 46, 70, "n t") + L(170, 70, 154, 70, "n t"))


def leaves():         # غازاڭ ghazang - fallen autumn leaves on the ground
    def maple(x, y, s, rot, cls):
        pts = [(0, -30), (8, -14), (24, -20), (18, -4), (30, 4), (12, 8), (14, 24), (0, 14), (-14, 24), (-12, 8),
               (-30, 4), (-18, -4), (-24, -20), (-8, -14)]
        import math
        a = math.radians(rot)
        q = [(x + s * (px * math.cos(a) - py * math.sin(a)), y + s * (px * math.sin(a) + py * math.cos(a))) for px, py in pts]
        stem = (x + s * (-0 * math.cos(a) - 14 * math.sin(a)), y + s * (0 * math.sin(a) + 14 * math.cos(a)))
        stem2 = (x + s * (-0 * math.cos(a) - 34 * math.sin(a)), y + s * (0 * math.sin(a) + 34 * math.cos(a)))
        return poly(q, cls) + L(stem[0], stem[1], stem2[0], stem2[1], "n t")
    return (P("M14 170 C60 156 140 156 186 170 L186 184 L14 184 Z", "e")
            + maple(62, 120, 1.3, -20, "d") + maple(138, 128, 1.2, 25, "c")
            + leaf(84, 160, -15, 34, "b") + leaf(120, 166, 200, 30, "d")
            + maple(104, 54, 1.0, 10, "c") + leaf(40, 60, 30, 28, "b") + leaf(150, 64, 150, 26, "d")
            + P("M110 30 C120 40 98 44 108 54", "n t"))


def sack():           # ئۇن un - a sack of flour with a scoop
    return (P("M56 70 C46 100 40 150 52 176 L148 176 C160 150 154 100 144 70 Z", "a")
            + P("M56 70 C70 60 130 60 144 70 C130 78 70 78 56 70 Z", "e")
            + P("M64 66 C70 46 82 40 100 40 C118 40 130 46 136 66", "e")
            + P("M86 42 C92 32 108 32 114 42", "n t")
            + C(100, 120, 22, "c")
            + P("M90 126 C94 108 106 108 110 126 Z", "d") + L(100, 110, 100, 132, "n t")
            + P("M152 150 L176 138 L184 150 L160 162 Z", "b") + L(160, 162, 190, 180, "n")
            + ground(178))


PICS = {"ug_table": table, "ug_candle": candle, "ug_leaves": leaves, "ug_sack": sack}
