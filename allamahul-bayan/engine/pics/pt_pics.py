# -*- coding: utf-8 -*-
"""Pictures for Book 81 (Portuguese). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, leaf, ground


def kiwi():
    """A whole kiwi fruit and a round slice showing its seeds."""
    seeds = "".join(E(122 + 21 * math.cos(math.radians(a)), 112 + 21 * math.sin(math.radians(a)), 2.4, 5, "b", a + 90)
                    for a in range(0, 360, 24))
    return (E(66, 96, 44, 36, "b", -20) + P("M36 84 C42 78 48 76 54 76", "n t") + P("M84 120 C90 118 96 112 98 106", "n t")
            + C(122, 112, 50, "c") + C(122, 112, 40, "a") + seeds + E(122, 112, 11, 8, "e") + ground(178))


def waffle():
    """A round waffle with its square grid, and a little jug of honey."""
    cells = "".join(R(52 + i * 22, 70 + j * 22, 16, 16, "a", 3) for i in range(4) for j in range(4))
    return (C(84, 102, 58, "d") + cells
            + P("M150 140 C146 120 150 108 158 104 L176 104 C184 108 188 120 184 140 C182 156 152 156 150 140 Z", "e")
            + R(154, 94, 26, 10, "b", 3) + E(100, 170, 80, 8, "a"))


PICS = {"pt_kiwi": kiwi, "pt_waffle": waffle}
