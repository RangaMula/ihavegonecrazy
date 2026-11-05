# -*- coding: utf-8 -*-
"""Pictures for Book 28 (Persian). Objects and plants only. viewBox 0 0 200 200.
Named fa_pics.py, not fa.py: a plug-in called fa.py would shadow languages/fa.py on sys.path."""
from illos import P, C, E, R, L, leaf, ground


def bud():  # غنچه ghoncheh - flower bud
    return (P("M100 186 C94 152 106 122 100 96", "n")
            + leaf(98, 156, -150, 46, "c") + leaf(102, 132, -30, 42, "c")
            + P("M100 26 C128 40 134 70 122 92 C112 104 88 104 78 92 C66 70 72 40 100 26 Z", "e")
            + P("M100 26 C110 48 110 72 100 94", "n t")
            + P("M78 92 C86 80 94 82 100 98 C106 82 114 80 122 92 C114 110 86 110 78 92 Z", "c")
            + ground(188))


def rollingpin():  # وردنه vardaneh - rolling pin on a board with dough
    pin = ('<g transform="rotate(-16 100 92)">'
           + R(10, 84, 32, 16, "d", 8) + R(158, 84, 32, 16, "d", 8)
           + R(38, 74, 124, 36, "b", 17)
           + "</g>")
    return (E(100, 148, 84, 30, "a") + E(100, 145, 58, 18, "e")
            + P("M70 150 q6 -4 12 0 M112 140 q6 -4 12 0", "n t") + pin)



PICS = {"fa_bud": bud, "fa_rollingpin": rollingpin}
