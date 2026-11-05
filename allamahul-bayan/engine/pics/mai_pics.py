# -*- coding: utf-8 -*-
"""Pictures for Book 23 (Maithili). Objects, plants and nature only (viewBox 0 0 200 200)."""
import math
from illos import P, C, E, R, L, leaf, ground


def makhana():
    """मखान - puffed fox nuts (lotus seeds) in a bowl, the famous crop of Mithila."""
    seeds = [(52, 92), (76, 86), (100, 84), (124, 86), (148, 92), (64, 72), (88, 66), (112, 66), (136, 72),
             (76, 50), (100, 46), (124, 50)]
    balls = "".join(C(x, y, 13, "a") + P(f"M{x-5} {y-4} q4 -4 9 -2", "n t") for x, y in seeds)
    bowl = P("M24 100 L176 100 C172 146 140 170 100 170 C60 170 28 146 24 100 Z", "c")
    rim = E(100, 100, 76, 9, "c")
    spill = C(170, 178, 10, "a") + C(150, 182, 9, "a") + C(30, 180, 9, "a")
    return balls + bowl + rim + R(80, 168, 40, 10, "c", 3) + spill + ground(190)


def guava():
    """लताम - guava, whole and cut."""
    whole = (P("M70 40 C104 40 120 70 116 100 C112 132 92 146 70 146 C46 146 26 130 24 100 C22 70 38 40 70 40 Z", "c")
             + P("M70 40 L72 26", "n") + leaf(72, 30, -40, 40) + E(70, 142, 6, 4, "a")
             + P("M42 80 C38 92 38 106 44 116", "n t"))
    half = (E(146, 140, 44, 40, "c") + E(146, 140, 34, 30, "e")
            + "".join(E(146 + 18 * math.cos(math.radians(a)), 140 + 15 * math.sin(math.radians(a)), 2.5, 3.5, "a")
                      for a in range(0, 360, 40)) + C(146, 140, 6, "a"))
    return whole + half + ground(186)


def bamboo():
    """बाँस / उवा - bamboo stalks with leaves."""
    out = ""
    for x, top, cls in ((54, 22, "c"), (100, 10, "b"), (146, 30, "c")):
        out += R(x - 9, top, 18, 186 - top, cls, 4)
        for y in range(top + 34, 186, 36):
            out += L(x - 9, y, x + 9, y)
    out += leaf(63, 70, -35, 40) + leaf(45, 110, 210, 36) + leaf(109, 52, -30, 44) + leaf(91, 96, 205, 40)
    out += leaf(155, 92, -25, 40) + leaf(137, 140, 215, 34) + leaf(109, 136, 20, 34)
    return out + ground(186)


PICS = {"mai_makhana": makhana, "mai_guava": guava, "mai_bamboo": bamboo}
