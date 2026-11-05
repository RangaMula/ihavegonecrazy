# -*- coding: utf-8 -*-
"""Pictures for Book 45 (Korean). Objects, plants and nature only."""
from illos import P, C, E, R, L, leaf, ground


def yoyo():
    swoosh = P("M28 96 C20 112 20 128 28 144 M172 96 C180 112 180 128 172 144", "n t")
    return (C(100, 18, 9, "d") + L(100, 27, 100, 110, "n")
            + C(100, 120, 62, "b") + C(100, 120, 44, "c") + C(100, 120, 14, "a")
            + P("M64 92 C74 80 88 74 100 74", "n t") + swoosh + L(100, 27, 100, 106, "n"))


def big_leaf():
    veins = ""
    for k in range(1, 6):
        t = k / 6
        x, y = 30 + 141 * t, 170 - 141 * t
        veins += L(x, y, x - 7, y - 26, "n t") + L(x, y, x + 26, y + 7, "n t")
    return (L(14, 186, 30, 170, "n") + leaf(30, 170, -45, 200, "c") + veins
            + leaf(150, 176, -150, 40, "c"))


PICS = {"ko_yoyo": yoyo, "ko_leaf": big_leaf}
