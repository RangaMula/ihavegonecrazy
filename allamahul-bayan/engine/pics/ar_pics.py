# -*- coding: utf-8 -*-
"""Pictures for Book 27 (Arabic). Objects and plants only. viewBox 0 0 200 200.
Named ar_pics.py, not ar.py: a plug-in called ar.py would shadow languages/ar.py on sys.path."""
from illos import P, C, E, R, L, leaf, ground


def bag():  # حَقِيبَة ḥaqeeba - school bag
    return (P("M74 54 C74 22 126 22 126 54 L114 54 C114 36 86 36 86 54 Z", "d")
            + R(34, 52, 132, 124, "b", 18)
            + P("M34 72 C34 60 44 52 56 52 L144 52 C156 52 166 60 166 72 L166 112 C130 126 70 126 34 112 Z", "c")
            + R(88, 106, 24, 24, "d", 4) + R(95, 113, 10, 10, "a", 2)
            + R(54, 138, 92, 28, "e", 8) + L(62, 150, 138, 150, "n t")
            + ground(186))


def bucket():  # دَلْو dalw - bucket for drawing water from a well (Surah Yusuf 12:19)
    return (L(100, 8, 100, 34)
            + P("M50 84 C50 26 150 26 150 84", "n")
            + P("M46 84 L64 172 C70 182 130 182 136 172 L154 84 Z", "b")
            + P("M56 120 L144 120 M61 146 L139 146", "n t")
            + E(100, 84, 54, 13, "a") + E(100, 86, 44, 8, "d")
            + C(50, 84, 5, "e") + C(150, 84, 5, "e")
            + ground(188))


def pumpkin():  # يَقْطِين yaqteen - gourd / pumpkin (Surah As-Saffat 37:146)
    return (P("M120 44 C140 28 166 36 160 56 C156 68 142 62 148 52", "n t")
            + E(100, 122, 80, 56, "e") + E(100, 122, 52, 56, "e") + E(100, 122, 22, 56, "e")
            + P("M92 68 C90 52 94 40 106 32 L114 40 C104 48 102 56 106 68 Z", "c")
            + leaf(76, 52, -160, 46, "c")
            + ground(186))



PICS = {"ar_bag": bag, "ar_bucket": bucket, "ar_pumpkin": pumpkin}
