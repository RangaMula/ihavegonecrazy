# -*- coding: utf-8 -*-
"""Pictures for Book 19 (Balochi). Objects, plants and nature only."""
from illos import P, C, E, R, L, poly, star, cloud, leaf, ground


def lamp():
    """A little clay oil lamp (chiraag) with a flame."""
    return (P("M30 130 C34 160 150 166 170 130 C160 118 140 114 120 116 L60 116 C44 116 32 120 30 130 Z", "b")
            + P("M120 116 C140 108 162 106 178 112 C176 122 172 128 166 132", "b")
            + E(80, 118, 40, 7, "c")
            + P("M44 140 C80 150 120 150 156 140", "n t")
            + P("M176 108 C166 90 172 70 182 56 C190 74 194 92 184 108 Z", "d")
            + P("M180 104 C176 94 178 84 182 78 C186 88 186 98 182 104 Z", "e")
            + R(62, 150, 76, 10, "c", 4) + ground(160))


def wind():
    """Wind: swirling lines blowing leaves past a little tree."""
    return (P("M20 60 C70 60 110 60 130 48 C148 36 136 14 118 22 C108 28 112 40 122 40", "n")
            + P("M20 96 C80 96 130 96 156 84 C178 72 168 46 148 52 C136 56 138 72 150 72", "n")
            + P("M86 132 C110 132 130 134 140 142 C152 152 146 168 132 164", "n")
            + leaf(150, 120, -20, 26, "c") + leaf(170, 150, 30, 22, "c") + leaf(60, 40, 10, 22, "c")
            + cloud(110, 186 - 150, 0.5, "a")
            + P("M40 186 C42 170 44 160 42 150 L50 150 C48 160 50 170 54 186 Z", "b")
            + P("M46 152 C20 150 18 124 34 116 C40 100 64 100 70 116 C84 122 80 150 50 152 Z", "c")
            + ground(186))


PICS = {"bal_lamp": lamp, "bal_wind": wind}
