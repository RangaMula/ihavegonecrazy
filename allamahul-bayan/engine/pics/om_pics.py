# -*- coding: utf-8 -*-
"""Pictures for Book 67 (Oromo). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, leaf, ground


def firii():
    """Fruit (firii): an apple, a banana bunch and grapes in a bowl."""
    banana = (P("M40 96 C56 50 104 34 146 46 C150 52 146 56 140 56 C104 52 70 70 56 100 Z", "d")
              + P("M146 46 l8 -6", "n"))
    apple = (P("M74 70 C56 56 30 70 34 98 C38 122 60 128 74 120 C88 128 110 122 114 98 C118 70 92 56 74 70 Z", "e")
             + P("M74 70 C74 62 76 56 80 50", "n") + leaf(80, 54, -30, 20, "c"))
    grapes = "".join(C(x, y, 10, "b") for x, y in [(126, 84), (146, 84), (166, 88), (136, 102), (156, 104), (146, 120)])
    grapes += P("M146 74 C146 66 150 60 156 56", "n") + leaf(150, 64, -10, 18, "c")
    bowl = (P("M22 116 L178 116 C174 156 140 178 100 178 C60 178 26 156 22 116 Z", "a")
            + P("M40 140 C80 150 120 150 160 140", "n t") + R(78, 176, 44, 8, "a", 3))
    return banana + apple + grapes + bowl + ground(186)


def nuugii():
    """A niger-seed plant (nuugii): a bushy stem with small yellow daisy-like flowers."""
    def flower(cx, cy, r=8):
        petals = "".join(E(cx + 1.6 * r * math.cos(math.radians(a)), cy + 1.6 * r * math.sin(math.radians(a)),
                           r * 0.95, r * 0.45, "e", a) for a in range(0, 360, 45))
        return petals + C(cx, cy, r * 0.8, "d")
    stems = P("M100 182 C100 150 98 120 96 96 M100 150 C84 130 66 108 56 78 M100 140 C118 118 134 96 146 66 "
              "M97 112 C104 90 112 66 108 46 M100 164 C126 154 150 136 164 112", "n")
    leaves = (leaf(100, 160, -150, 30) + leaf(100, 150, -30, 30) + leaf(98, 124, -160, 26)
              + leaf(118, 116, -20, 24) + leaf(76, 108, -150, 22))
    flowers = (flower(56, 72) + flower(146, 60) + flower(108, 40) + flower(96, 90, 7) + flower(166, 106, 7))
    return stems + leaves + flowers + ground(184)


def xaafii():
    """Teff (xaafii): a tuft of fine grass with airy heads of tiny grains, and a little bowl of grain."""
    out = ""
    for x0, tipx, tipy in [(64, 30, 40), (72, 60, 24), (80, 96, 18), (88, 128, 30), (94, 150, 54)]:
        cx = (x0 + tipx) / 2
        out += P(f"M{x0} 170 Q{cx} {tipy + 70} {tipx} {tipy}", "n t")
        for k in range(1, 6):
            t = k / 6
            bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * tipx
            by = (1 - t) ** 2 * 170 + 2 * (1 - t) * t * (tipy + 70) + t * t * tipy
            if t < 0.45:
                continue
            for side in (-1, 1):
                ex, ey = bx + side * 12, by - 6
                out += L(bx, by, ex, ey, "n t") + E(ex, ey, 2.6, 4, "a")
        out += E(tipx, tipy, 2.6, 4, "a")
    blades = P("M60 170 C50 140 40 128 30 120 C46 128 58 144 66 170 Z", "c") + P("M98 170 C104 146 116 134 128 128 C116 140 106 154 102 170 Z", "c")
    bowl = (P("M118 150 L184 150 C182 172 166 182 151 182 C136 182 120 172 118 150 Z", "b")
            + P("M120 150 C130 136 172 136 182 150 Z", "a")
            + "".join(C(x, y, 1.6, "n") for x, y in [(136, 145), (146, 142), (156, 144), (166, 143), (150, 147), (172, 147)]))
    return blades + out + bowl + ground(184)


PICS = {"om_firii": firii, "om_nuugii": nuugii, "om_xaafii": xaafii}
