# -*- coding: utf-8 -*-
"""Pictures for Book 49 (Khmer). Keys are prefixed km_. Objects, plants and nature only.
(File is named km_pics.py, not km.py: a plug-in module called `km` would shadow languages/km.py
when build.py imports the language by its code.)"""
import math
from illos import P, C, E, R, L, poly, star_pts, leaf, ground, apple, banana


def pencil():
    return ('<g transform="rotate(-45 100 100)">'
            + R(84, 34, 32, 106, "b", 3) + L(95, 38, 95, 140, "n t") + L(105, 38, 105, 140, "n t")
            + R(84, 12, 32, 22, "e", 7) + R(82, 28, 36, 12, "d", 2)
            + P("M84 140 L116 140 L100 184 Z", "a") + P("M94 168 L106 168 L100 184 Z", "c") + "</g>"
            + P("M18 186 C40 176 60 186 82 178", "n t"))


def bed():
    return (R(22, 56, 18, 126, "c", 5) + R(160, 96, 18, 86, "c", 5)
            + R(36, 134, 128, 16, "c", 2)
            + R(36, 108, 128, 28, "a", 6)
            + P("M84 104 L166 104 L166 140 C150 146 100 146 84 140 Z", "b")
            + P("M96 116 L156 116 M96 128 L156 128", "n t")
            + E(62, 100, 22, 12, "e") + ground(182))


def gourd():
    return (P("M100 44 C116 44 120 58 116 74 C112 90 114 98 132 112 C162 136 158 184 100 184 C42 184 38 136 68 112 "
              "C86 98 88 90 84 74 C80 58 84 44 100 44 Z", "c")
            + P("M100 44 C100 32 104 24 112 18", "n") + leaf(108, 26, -20, 36)
            + P("M76 132 C80 150 86 164 96 174", "n t") + P("M92 64 C92 72 94 80 96 86", "n t"))


def table():
    return (C(84, 46, 12, "e") + C(104, 42, 12, "d") + C(122, 48, 11, "e")
            + P("M64 54 L136 54 C136 70 120 78 100 78 C80 78 64 70 64 54 Z", "a")
            + R(18, 78, 164, 16, "b", 4) + R(30, 94, 140, 14, "c", 2)
            + R(36, 108, 14, 74, "c", 3) + R(150, 108, 14, 74, "c", 3) + ground(182))


def stones():
    return (P("M18 182 C12 150 38 126 72 130 C102 134 110 160 106 182 Z", "b")
            + P("M96 182 C92 140 124 116 158 124 C186 132 192 166 184 182 Z", "c")
            + P("M58 134 C54 108 76 90 100 94 C126 98 136 118 126 136 C110 128 82 126 58 134 Z", "d")
            + P("M36 160 C42 150 54 146 62 148", "n t") + P("M128 150 C138 140 152 140 162 144", "n t")
            + P("M80 110 C86 104 94 102 102 104", "n t") + ground(182))


def durian():
    pts = []
    for i in range(40):
        a = math.radians(i * 9)
        k = 1.0 if i % 2 == 0 else 0.87
        pts.append((100 + 66 * k * math.cos(a), 114 + 70 * k * math.sin(a)))
    marks = "".join(P(f"M{x - 6} {y + 4} L{x} {y - 4} L{x + 6} {y + 4}", "n t")
                    for x, y in [(78, 92), (112, 86), (96, 118), (130, 120), (70, 132), (104, 150), (134, 156)])
    return (poly(pts, "c") + marks + R(94, 30, 12, 18, "b", 3) + P("M100 32 C100 22 106 14 116 12", "n")
            + E(100, 190, 60, 6, "a"))


def pumpkin():
    return (E(66, 120, 40, 56, "e") + E(134, 120, 40, 56, "e") + E(100, 120, 36, 60, "e")
            + R(93, 46, 14, 22, "c", 4) + leaf(108, 56, -25, 40) + P("M92 52 C80 44 74 34 78 26", "n t")
            + ground(184))


def car():
    return (P("M18 140 L18 112 C18 104 24 100 32 98 L54 96 L74 64 C78 58 84 56 92 56 L132 56 C140 56 146 60 150 66 "
              "L166 96 L176 98 C182 100 186 106 186 112 L186 140 Z", "b")
            + P("M84 66 L100 66 L100 96 L66 96 Z", "a") + P("M110 66 L134 66 C138 66 140 68 142 72 L154 96 L110 96 Z", "a")
            + R(22, 108, 14, 9, "d", 3) + R(170, 108, 12, 9, "e", 3) + L(106, 110, 120, 110, "n t")
            + C(58, 142, 22, "c") + C(58, 142, 9, "a") + C(146, 142, 22, "c") + C(146, 142, 9, "a") + ground(166))


def compass():
    return (C(100, 20, 9, "d") + C(100, 104, 78, "c") + C(100, 104, 66, "a")
            + poly(star_pts(100, 104, 40, 10, 4, -45), "e")
            + poly(star_pts(100, 104, 60, 14, 4, -90), "b")
            + P("M100 104 L148 56 L112 96 Z", "d") + C(100, 104, 6, "a"))


def bamboo():
    out = ""
    for x, top, cls in ((58, 34, "b"), (100, 16, "d"), (142, 44, "b")):
        out += R(x - 11, top, 22, 182 - top, cls, 6)
        out += "".join(L(x - 11, y, x + 11, y, "n") for y in range(top + 36, 178, 36))
    return (out + leaf(68, 70, -30, 44) + leaf(48, 96, -150, 40) + leaf(110, 52, -20, 46)
            + leaf(90, 120, -160, 40) + leaf(152, 86, -35, 40) + ground(182))


def bell():
    return (R(92, 18, 16, 42, "c", 6)
            + P("M100 56 C72 56 60 80 58 110 C56 134 48 146 36 156 L164 156 C152 146 144 134 142 110 C140 80 128 56 100 56 Z", "d")
            + R(30, 152, 140, 12, "b", 6) + C(100, 176, 11, "e")
            + P("M80 80 C74 92 72 108 72 124", "n t")
            + P("M24 96 C16 110 16 126 24 140 M176 96 C184 110 184 126 176 140", "n t"))


def apple_or_banana():
    return (f'<g transform="translate(-4 34) scale(0.6)">{apple()}</g>'
            f'<g transform="translate(84 34) scale(0.6)">{banana()}</g>'
            + P("M96 60 C96 48 108 44 112 52 C116 60 102 64 102 74", "n") + C(102, 84, 2.5, "n"))


PICS = dict(km_pencil=pencil, km_bed=bed, km_gourd=gourd, km_table=table, km_stones=stones, km_durian=durian,
            km_pumpkin=pumpkin, km_car=car, km_compass=compass, km_bamboo=bamboo, km_bell=bell,
            km_apple_or_banana=apple_or_banana)
