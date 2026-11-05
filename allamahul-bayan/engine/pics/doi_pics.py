# -*- coding: utf-8 -*-
"""Pictures for Book 24 (Dogri). Objects, plants and nature only (viewBox 0 0 200 200)."""
from illos import P, C, E, R, L, leaf, ground


def _bean(x, y, rot, s=1.0, cls="e"):
    d = (f"M{-20*s} 0 C{-20*s} {-11*s} {-10*s} {-12*s} 0 {-8*s} C{10*s} {-12*s} {20*s} {-11*s} {20*s} 0 "
         f"C{20*s} {10*s} {10*s} {12*s} 0 {11*s} C{-10*s} {12*s} {-20*s} {10*s} {-20*s} 0 Z")
    return f'<g transform="translate({x} {y}) rotate({rot})">' + P(d, cls) + "</g>"


def peach():
    """आड़ू - a peach with its leaves."""
    fruit = P("M100 50 C78 34 34 46 30 96 C26 146 62 180 100 180 C138 180 174 146 170 96 C166 46 122 34 100 50 Z", "e")
    cleft = P("M100 52 C88 86 88 140 100 178", "n")
    stem = P("M100 50 L104 30", "n")
    return fruit + cleft + stem + leaf(104, 32, -30, 48) + leaf(102, 34, 200, 40) + P("M52 92 C48 108 50 124 56 136", "n t")


def rajma():
    """राजमाह - kidney beans in a bowl."""
    beans = "".join(_bean(x, y, r) for x, y, r in
                    ((52, 92, -10), (84, 86, 20), (118, 88, -25), (150, 94, 10), (68, 70, 35), (102, 64, -5), (136, 70, 25)))
    bowl = P("M22 100 L178 100 C174 146 142 170 100 170 C58 170 26 146 22 100 Z", "c") + E(100, 100, 78, 9, "c")
    spill = _bean(36, 182, 15, 0.9) + _bean(166, 180, -20, 0.9)
    return beans + bowl + R(78, 168, 44, 10, "c", 3) + spill + ground(190)


PICS = {"doi_peach": peach, "doi_rajma": rajma}
