# -*- coding: utf-8 -*-
"""Pictures for Book 20 Santali (sat_) and Book 21 Manipuri / Meitei (mni_).
Objects, plants and nature only. viewBox 0 0 200 200; closed shapes carry a colour role a-e."""
import math
from illos import P, C, E, R, L, poly, leaf, ground


# ---------------------------------------------------------------- shared shapes
def bamboo():
    def stalk(x, top, cls):
        nodes = "".join(L(x, y, x + 16, y, "n") for y in range(top + 30, 186, 30))
        return R(x, top, 16, 186 - top, cls, 5) + nodes
    leaves = (leaf(64, 64, -150, 34) + leaf(70, 94, -30, 30) + leaf(104, 40, -160, 30) + leaf(110, 70, -20, 34)
              + leaf(142, 84, -150, 30) + leaf(148, 112, -20, 32) + leaf(112, 130, -10, 26))
    return stalk(56, 50, "c") + stalk(94, 24, "b") + stalk(132, 70, "c") + leaves + ground(186)


def stones():
    return (E(66, 158, 48, 26, "b") + E(138, 162, 42, 22, "c") + E(102, 122, 40, 26, "e")
            + E(76, 112, 22, 14, "a", -15) + E(140, 128, 22, 13, "d", 10)
            + P("M48 150 q10 -8 22 -6 M120 158 q10 -6 20 -4 M88 116 q10 -8 22 -6", "n t") + ground(184))


# ---------------------------------------------------------------- Santali
def big_leaf():
    veins = "".join(P(f"M100 {y} L{100 - w} {y - 20} M100 {y} L{100 + w} {y - 20}", "n t")
                    for y, w in [(60, 22), (88, 36), (116, 42), (144, 34)])
    return (P("M100 172 C36 140 34 64 100 18 C166 64 164 140 100 172 Z", "c") + L(100, 30, 100, 186) + veins + ground(186))


def path():
    trees = "".join(L(x, y, x, y + 18) + C(x, y - 6, r, "c") for x, y, r in [(36, 104, 12), (168, 96, 14), (150, 120, 10)])
    return (C(150, 44, 18, "d")
            + P("M10 112 C40 78 72 88 96 82 C126 72 160 78 190 92 L190 186 L10 186 Z", "c")
            + P("M10 112 C30 98 52 96 70 104 L10 140 Z", "b")
            + P("M54 186 C76 152 138 146 112 116 C100 102 104 92 106 84 L112 84 C112 94 110 102 124 116 C158 148 120 160 150 186 Z", "d")
            + P("M96 186 C106 160 124 150 118 130", "n t") + trees)


def jackfruit():
    bumps = "".join(C(100 + rx * math.cos(math.radians(a)), 112 + ry * math.sin(math.radians(a)), 2.2, "n")
                    for rx, ry, n in [(18, 26, 6), (34, 48, 10), (46, 62, 14)] for a in range(0, 360, 360 // n))
    return (P("M96 46 C98 34 100 26 104 18", "n") + leaf(104, 30, -30, 36) + leaf(100, 34, -160, 30)
            + E(100, 112, 56, 72, "c") + bumps + ground(186))


# ---------------------------------------------------------------- Manipuri / Meitei
def fire():
    return (P("M36 172 L160 148 L166 160 L42 186 Z", "b") + P("M40 148 L164 176 L158 188 L34 160 Z", "b")
            + C(160, 154, 6, "a") + C(40, 154, 6, "a")
            + P("M100 158 C58 150 54 108 80 82 C80 100 88 108 94 106 C86 80 98 52 120 34 C118 62 146 78 146 112 "
                "C146 140 128 156 100 158 Z", "e")
            + P("M100 152 C80 146 78 122 92 108 C94 120 102 124 106 120 C104 104 112 92 122 86 C122 104 132 116 128 132 "
                "C126 146 114 152 100 152 Z", "d"))


def waterfall():
    return (P("M10 40 L80 40 L80 130 L10 130 Z", "d") + P("M120 40 L190 40 L190 130 L120 130 Z", "d")
            + P("M10 40 C30 30 60 30 80 40 M120 40 C140 30 170 30 190 40", "n")
            + C(44, 26, 12, "c") + C(160, 24, 14, "c")
            + R(80, 40, 40, 108, "a") + P("M88 50 L88 140 M100 46 L100 146 M112 50 L112 140", "n t")
            + E(100, 160, 84, 22, "b") + P("M70 152 q8 -10 16 0 M114 152 q8 -10 16 0 M40 164 q8 -8 16 0 M144 166 q8 -8 16 0", "n t")
            + P("M10 130 L80 130 L80 146 C60 150 30 150 10 150 Z", "c") + P("M120 130 L190 130 L190 150 C170 150 140 150 120 146 Z", "c"))


def river():
    trees = "".join(L(x, y, x, y + 20) + C(x, y - 8, r, "c") for x, y, r in [(30, 90, 14), (60, 72, 12), (168, 100, 14), (150, 76, 11)])
    return (C(100, 36, 16, "d")
            + P("M10 70 L190 70 L190 186 L10 186 Z", "c")
            + P("M80 70 L118 70 C120 100 70 110 76 140 C80 160 120 168 130 186 L50 186 C50 160 22 146 30 124 C40 98 86 96 80 70 Z", "b")
            + P("M56 150 q8 -6 16 0 M88 120 q8 -6 16 0 M70 172 q8 -6 16 0", "n t") + trees)


def okra():
    def pod(rot, cls):
        return (f'<g transform="rotate({rot} 100 110)">'
                + P("M88 52 C70 90 82 150 100 188 C118 150 130 90 112 52 Z", cls)
                + P("M100 56 C96 100 98 150 100 184 M94 60 C82 100 88 150 98 182 M106 60 C118 100 112 150 102 182", "n t")
                + P("M86 54 C88 40 112 40 114 54 Z", "b") + L(100, 42, 100, 22) + "</g>")
    return pod(-28, "c") + pod(26, "c")


def shoe():
    return (P("M24 150 L24 98 C40 92 60 96 72 104 C96 120 140 122 170 132 C184 136 186 148 184 158 L24 158 Z", "b")
            + P("M24 158 L184 158 L182 172 L26 172 Z", "a")
            + P("M72 104 C70 90 96 82 104 92 C110 100 108 110 104 116", "n")
            + "".join(L(80 + 10 * k, 108 + 3 * k, 92 + 10 * k, 102 + 3 * k, "n t") for k in range(4))
            + C(110, 140, 4, "d") + C(130, 142, 4, "d") + ground(186))


def chilli():
    return (P("M64 50 C110 54 150 100 156 150 C158 172 150 186 140 176 C128 132 98 92 60 74 Z", "e")
            + P("M50 56 C56 44 70 44 74 52 L68 74 C60 72 50 66 50 56 Z", "c") + P("M58 48 C54 34 56 22 66 14", "n")
            + P("M86 74 C110 92 128 118 138 146", "n t"))


def kangjei():
    return (P("M118 18 L130 22 L84 160 C80 172 64 178 50 170 L54 158 C62 162 70 160 72 154 Z", "b")
            + C(146, 160, 18, "d") + P("M134 150 C142 156 150 156 158 150", "n t") + ground(184))


PICS = {
    "sat_bamboo": bamboo, "sat_leaf": big_leaf, "sat_path": path, "sat_stones": stones, "sat_jackfruit": jackfruit,
    "mni_bamboo": bamboo, "mni_stones": stones, "mni_fire": fire, "mni_waterfall": waterfall, "mni_river": river,
    "mni_okra": okra, "mni_shoe": shoe, "mni_chilli": chilli, "mni_kangjei": kangjei,
}
