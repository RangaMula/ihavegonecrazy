# -*- coding: utf-8 -*-
"""Pictures for Book 33 (Assyrian Neo-Aramaic, code syr). Keys are prefixed syr_.
The file is called syr_pics.py, not syr.py: engine/pics is put first on sys.path, so a pics module named
like a language file (languages/syr.py) would shadow it when build.py imports the language by its code."""
from illos import P, C, E, R, L, ground


def table():
    """A wooden table with a bowl of fruit on it."""
    bowl = (C(80, 64, 12, "d") + C(102, 58, 13, "e") + C(122, 64, 11, "c")
            + P("M102 45 C104 40 108 38 112 38", "n t")
            + P("M58 70 C58 92 76 102 100 102 C124 102 142 92 142 70 Z", "a"))
    top = R(18, 102, 164, 16, "b", 5) + R(34, 118, 132, 14, "c", 2)
    legs = (P("M40 132 L54 132 L52 184 L42 184 Z", "b") + P("M146 132 L160 132 L158 184 L148 184 Z", "b")
            + L(56, 156, 144, 156, "n"))
    return bowl + top + legs + ground(186)


PICS = {"syr_table": table}
