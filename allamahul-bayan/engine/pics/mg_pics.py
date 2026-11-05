# -*- coding: utf-8 -*-
"""Pictures for Book 74 (Malagasy). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, leaf, cloud, ground


def entana():
    """A travel case (entana: luggage, things you carry) with two straps and a handle."""
    body = R(30, 72, 140, 100, "b", 12)
    lid = L(30, 94, 170, 94)
    straps = R(58, 72, 14, 100, "d") + R(128, 72, 14, 100, "d")
    buckles = R(54, 112, 22, 14, "a", 3) + R(124, 112, 22, 14, "a", 3)
    handle = P("M82 72 L82 54 C82 46 88 42 94 42 L106 42 C112 42 118 46 118 54 L118 72 L108 72 L108 54 L92 54 L92 72 Z", "e")
    feet = C(50, 178, 6, "c") + C(150, 178, 6, "c")
    return feet + body + lid + straps + buckles + handle + ground(186)


def nosy():
    """An island (nosy) with a palm tree, in the sea, under the sun."""
    sun = C(46, 46, 18, "d") + "".join(
        L(46 + 24 * c, 46 + 24 * s, 46 + 32 * c, 46 + 32 * s, "n t")
        for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
    island = P("M34 154 C54 112 146 112 168 154 Z", "e")
    trunk = P("M98 132 C102 104 108 80 114 58 L122 60 C116 82 110 106 108 132 Z", "b")
    fronds = "".join(leaf(118, 56, a, 42) for a in (-170, -130, -40, -5, 150, 30))
    nuts = C(112, 64, 6, "d") + C(123, 66, 6, "d")
    sea = P("M8 150 C34 140 58 160 100 150 C142 140 166 160 192 150 L192 192 L8 192 Z", "b")
    waves = P("M28 170 c10 -6 20 -6 30 0 M86 180 c10 -6 20 -6 30 0 M138 168 c10 -6 20 -6 30 0", "n t")
    return sun + island + trunk + fronds + nuts + sea + waves


def ony():
    """A river (ony) winding from the hills, with reeds on its banks."""
    hills = P("M8 106 C36 70 70 66 100 96 C130 62 168 66 192 100 L192 112 L8 112 Z", "c")
    land = R(8, 104, 184, 86, "e")
    river = P("M94 104 C82 122 112 138 92 158 C82 170 64 180 52 190 L150 190 C138 176 128 164 130 150 "
              "C132 132 110 120 108 104 Z", "b")
    ripples = P("M94 168 c8 -4 16 -4 24 0 M100 136 c6 -3 10 -3 14 0", "n t")
    reeds = ""
    for x, h in [(28, 46), (38, 56), (48, 40), (160, 50), (170, 60), (180, 44)]:
        reeds += L(x, 182, x, 182 - h) + E(x, 182 - h - 6, 4, 10, "d")
    return hills + land + river + ripples + reeds + cloud(116, 50, 0.6) + cloud(20, 46, 0.45)


def baobab():
    """A baobab tree (renala), the giant bottle-shaped tree of Madagascar."""
    trunk = P("M70 186 C78 150 72 112 84 80 C88 68 112 68 116 80 C128 112 122 150 130 186 Z", "b")
    branches = P("M88 76 C80 60 68 52 56 48 M96 72 C96 56 92 44 84 34 M104 72 C108 54 114 44 122 36 "
                 "M112 76 C122 62 134 56 146 52", "n")
    tufts = E(52, 44, 18, 10, "c") + E(82, 28, 16, 10, "c") + E(124, 30, 16, 10, "c") + E(150, 48, 18, 10, "c")
    bark = P("M92 120 C94 140 90 160 92 180 M108 112 C106 140 112 160 110 180", "n t")
    small = P("M160 186 C162 168 160 150 164 138 L174 138 C178 150 176 168 178 186 Z", "b") + E(169, 132, 14, 7, "c")
    return trunk + branches + tufts + bark + small + ground(186)


PICS = {"mg_entana": entana, "mg_nosy": nosy, "mg_ony": ony, "mg_baobab": baobab}
