# -*- coding: utf-8 -*-
"""Pictures for Book 25 (Bodo). Objects, plants and nature only (viewBox 0 0 200 200)."""
import math
from illos import P, C, E, R, L, leaf, cloud, ground


def orange():
    """कमला - an orange and a peeled segment."""
    fruit = C(88, 104, 64, "e") + "".join(C(88 + 40 * math.cos(math.radians(a)), 104 + 40 * math.sin(math.radians(a)), 2, "n")
                                          for a in range(0, 360, 45))
    top = P("M88 40 L90 26", "n") + leaf(90, 28, -30, 42)
    seg = P("M150 178 C138 150 152 126 176 124 C188 140 184 168 150 178 Z", "e") + P("M156 170 C152 152 162 138 174 132", "n t")
    return fruit + C(88, 104, 7, "a") + top + seg + ground(186)


def eggplant():
    """फान्थौ - an eggplant (brinjal)."""
    body = P("M118 62 C150 70 170 110 160 146 C150 180 110 190 80 176 C52 162 50 130 66 108 C80 90 86 66 118 62 Z", "d")
    cap = P("M104 66 C110 52 134 50 142 64 C134 74 126 70 120 80 C114 72 108 76 104 66 Z", "c")
    stem = R(118, 34, 10, 26, "c", 3)
    shine = P("M76 132 C76 150 88 164 104 168", "n t")
    return body + cap + stem + shine + ground(188)


def road():
    """लामा - a road running to the hills."""
    hills = P("M0 96 C40 60 70 64 100 90 C130 60 170 58 200 92 L200 104 L0 104 Z", "c")
    rd = P("M86 104 L114 104 L176 190 L24 190 Z", "b")
    dashes = "".join(P(f"M100 {y} L100 {y + h}", "n") for y, h in ((112, 6), (126, 9), (144, 12), (166, 16)))
    trees = ""
    for x, y, s in ((36, 140, 1.0), (164, 140, 1.0), (60, 112, 0.6), (140, 112, 0.6)):
        trees += R(x - 3 * s, y, 6 * s, 30 * s, "a") + C(x, y - 6 * s, 18 * s, "c")
    sun = C(160, 34, 14, "d")
    return sun + cloud(20, 52, 0.5) + hills + rd + dashes + trees


def fire():
    """वाट - a small fire of sticks."""
    logs = (f'<g transform="rotate(-14 100 168)">' + R(40, 160, 120, 16, "b", 8) + "</g>"
            + f'<g transform="rotate(14 100 168)">' + R(40, 160, 120, 16, "b", 8) + "</g>")
    outer = P("M100 26 C122 60 150 80 146 124 C142 152 122 164 100 164 C78 164 56 152 54 124 C52 96 72 86 80 60 "
              "C88 78 92 84 100 26 Z", "e")
    inner = P("M100 80 C112 102 126 114 122 134 C118 152 82 152 78 134 C76 118 90 112 100 80 Z", "d")
    return outer + inner + logs + ground(186)


PICS = {"brx_orange": orange, "brx_eggplant": eggplant, "brx_road": road, "brx_fire": fire}
