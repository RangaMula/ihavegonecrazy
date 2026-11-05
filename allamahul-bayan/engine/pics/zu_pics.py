# -*- coding: utf-8 -*-
"""Pictures for Books 68-69 (Zulu, Xhosa). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, star, ground


def cake():
    """A two-layer cake (ikhekhe) on a plate, with a strawberry on top."""
    plate = E(100, 172, 84, 10, "c")
    bottom = R(30, 112, 140, 58, "a", 10)
    drip = P("M30 124 C30 112 40 108 52 108 L148 108 C160 108 170 112 170 124 C162 132 156 122 150 130 "
             "C144 140 136 126 128 132 C120 140 112 124 104 132 C96 142 88 124 80 132 C72 140 64 124 56 130 "
             "C48 138 40 122 30 124 Z", "d")
    top = R(52, 66, 96, 46, "b", 10)
    topdrip = P("M52 78 C52 70 60 66 68 66 L132 66 C140 66 148 70 148 78 C140 86 134 76 126 84 C118 92 110 78 100 86 "
                "C90 94 82 78 74 84 C66 90 60 78 52 78 Z", "a")
    berry = (P("M100 62 C88 50 88 34 100 30 C112 34 112 50 100 62 Z", "e") + star(100, 30, 8, 3.5, "c", 5)
             + "".join(C(x, y, 1.5, "n") for x, y in [(96, 42), (104, 42), (100, 50), (95, 52), (105, 52)]))
    dots = "".join(C(x, 150, 4, "e") for x in (50, 76, 100, 124, 150))
    return plate + bottom + drip + top + topdrip + berry + dots


def shirt():
    """A shirt (ihembe / ihempe) with a collar, buttons and a pocket."""
    body = P("M72 36 L44 46 L14 82 L38 106 L58 88 L58 182 L142 182 L142 88 L162 106 L186 82 L156 46 L128 36 "
             "L100 64 Z", "a")
    collar = P("M72 36 L100 64 L84 74 L66 46 Z", "b") + P("M128 36 L100 64 L116 74 L134 46 Z", "b")
    placket = P("M100 64 L100 182", "n t")
    buttons = "".join(C(108, y, 3.4, "c") for y in (86, 112, 138, 164))
    pocket = R(118, 92, 22, 24, "d", 3)
    stripes = P("M20 84 L40 104 M28 74 L46 92 M180 84 L160 104 M172 74 L154 92", "n t")
    return body + collar + placket + buttons + pocket + stripes


PICS = {"zu_cake": cake, "zu_shirt": shirt}
