# -*- coding: utf-8 -*-
"""Pictures for Book 14 (Sinhala, si_) and Book 17 (Dhivehi, dv_). Objects, plants and nature only.
(File is not named si.py / dv.py so it cannot shadow languages/si.py or languages/dv.py on import.)"""
from illos import P, C, E, R, L, leaf, cloud, ground


# ---------------- Sinhala ----------------
def si_hopper():
    """Aappa (hoppers): a bowl-shaped crispy pancake with a soft middle, on a plate."""
    # wavy, crispy rim: little scallops all round the top opening
    import math
    rim = []
    for k in range(25):
        a = math.radians(180 + k * 15)
        r = 72 if k % 2 == 0 else 66
        rim.append(f"{100 + r * math.cos(a):.1f} {84 + r * 0.32 * math.sin(a):.1f}")
    rim_d = "M" + " L".join(rim) + " Z"
    return (E(100, 168, 86, 15, "c") + E(100, 164, 64, 8, "a")
            + P("M28 84 C32 124 62 156 100 156 C138 156 168 124 172 84 Z", "b")
            + P(rim_d, "a") + E(100, 94, 34, 9, "d")
            + P("M40 120 C56 132 70 138 84 140 M160 120 C144 132 130 138 116 140", "n t")
            + P("M78 54 c-8 -10 8 -16 0 -28 M100 50 c-8 -10 8 -16 0 -28 M122 54 c-8 -10 8 -16 0 -28", "n t"))


def si_plant():
    """A young plant in a flower pot."""
    return (P("M66 134 L134 134 L124 184 L76 184 Z", "b") + R(58, 122, 84, 16, "b", 5)
            + P("M100 122 C98 96 102 70 100 38", "n")
            + leaf(100, 108, -160, 44, "c") + leaf(100, 104, -20, 44, "c")
            + leaf(100, 80, -145, 36, "c") + leaf(100, 76, -35, 36, "c")
            + leaf(100, 52, -125, 28, "c") + leaf(100, 50, -55, 28, "c")
            + E(100, 34, 6, 10, "d") + ground(184))


def si_branch():
    """A leafy branch with two little fruits."""
    leaves = "".join(leaf(x, y, a, 30, "c") for x, y, a in
                     [(46, 140, -100), (62, 128, 60), (84, 118, -110), (100, 104, 50), (120, 92, -120),
                      (138, 80, 40), (156, 66, -100), (172, 54, 20)])
    return (P("M14 166 C64 136 118 100 182 46 L188 54 C128 106 74 144 22 176 Z", "b")
            + P("M96 114 C96 132 92 144 86 152", "n") + C(84, 160, 9, "d") + C(98, 158, 8, "d")
            + leaves)


def si_key():
    """A door key."""
    return (C(58, 100, 36, "b") + C(58, 100, 14, "a")
            + R(90, 92, 92, 16, "c", 4) + R(146, 108, 10, 26, "c", 2) + R(166, 108, 10, 18, "c", 2)
            + P("M40 78 C46 70 56 68 64 70", "n t") + E(58, 100, 26, 26, "n t"))


def si_sticks():
    """Danduva: a bundle of wooden sticks tied with string."""
    def stick(x1, y1, x2, y2, cls):
        dx, dy = x2 - x1, y2 - y1
        n = (dx * dx + dy * dy) ** 0.5
        ox, oy = -dy / n * 7, dx / n * 7
        return P(f"M{x1+ox:.1f} {y1+oy:.1f} L{x2+ox:.1f} {y2+oy:.1f} L{x2-ox:.1f} {y2-oy:.1f} L{x1-ox:.1f} {y1-oy:.1f} Z", cls)
    return (stick(60, 182, 120, 20, "b") + stick(140, 182, 80, 20, "c") + stick(100, 184, 100, 16, "b")
            + E(100, 104, 34, 10, "d") + E(100, 118, 34, 10, "d")
            + P("M120 110 C136 120 140 136 132 148 M120 110 C142 108 154 118 156 132", "n")
            + L(100, 40, 100, 60, "n t") + L(100, 150, 100, 170, "n t") + ground(186))


# ---------------- Dhivehi ----------------
def dv_island():
    """A small coral island with a coconut palm, in the lagoon."""
    fronds = "".join(leaf(124, 54, a, s, "c") for a, s in [(-165, 50), (-125, 46), (-60, 44), (-15, 48), (25, 42), (160, 40)])
    return (C(40, 42, 16, "e") + cloud(120, 36, 0.45)
            + P("M8 140 C50 132 150 132 192 140 L192 192 L8 192 Z", "c")
            + P("M40 146 C60 128 140 128 166 146 C140 156 64 156 40 146 Z", "d")
            + P("M98 144 C100 110 106 82 120 56 L128 60 C114 86 110 112 110 144 Z", "b")
            + fronds + C(120, 64, 6, "e") + C(131, 66, 6, "e")
            + P("M24 170 q12 -8 24 0 t24 0 M110 176 q12 -8 24 0 t24 0 M60 186 q12 -8 24 0 t24 0", "n t"))


def dv_toffee():
    """Two wrapped sweets (toffees)."""
    def sweet(cx, cy, s):
        return (P(f"M{cx-40*s} {cy} L{cx-74*s} {cy-26*s} L{cx-68*s} {cy} L{cx-74*s} {cy+26*s} Z", "c")
                + P(f"M{cx+40*s} {cy} L{cx+74*s} {cy-26*s} L{cx+68*s} {cy} L{cx+74*s} {cy+26*s} Z", "c")
                + E(cx, cy, 44 * s, 30 * s, "b")
                + P(f"M{cx-18*s} {cy-26*s} C{cx-8*s} {cy-8*s} {cx-8*s} {cy+8*s} {cx-18*s} {cy+26*s} "
                    f"M{cx+10*s} {cy-29*s} C{cx+20*s} {cy-10*s} {cx+20*s} {cy+10*s} {cx+10*s} {cy+29*s}", "n t"))
    return sweet(100, 70, 1.0) + sweet(100, 144, 0.85)


def dv_cheese():
    """A wedge of cheese with holes."""
    return (P("M24 104 L146 52 L180 78 Z", "d")
            + P("M24 104 L180 78 L180 144 L24 168 Z", "b")
            + E(66, 136, 11, 9, "a") + E(118, 116, 13, 10, "a") + C(154, 126, 7, "a") + C(96, 150, 6, "a")
            + C(46, 118, 5, "a") + E(132, 74, 9, 4, "a") + E(96, 86, 7, 3, "a") + ground(184))


def coconuts():
    """A bunch of three coconuts hanging under a palm frond (no 'eyes', so it never looks like a face)."""
    return (P("M100 34 C74 18 40 20 14 40 C44 34 74 38 98 50 Z", "c") + P("M100 34 C126 18 160 20 186 40 C156 34 126 38 102 50 Z", "c")
            + P("M60 30 l-6 12 M40 32 l-4 10 M140 30 l6 12 M160 32 l4 10", "n t")
            + R(94, 40, 12, 40, "d", 4)
            + E(70, 112, 30, 38, "b", -18) + E(130, 112, 30, 38, "b", 18) + E(100, 144, 33, 38, "b")
            + P("M60 84 C52 100 52 126 62 144 M80 82 C86 100 86 124 78 146", "n t")
            + P("M140 84 C148 100 148 126 138 144 M120 82 C114 100 114 124 122 146", "n t")
            + P("M88 114 C82 134 84 160 96 180 M112 114 C118 134 116 160 104 180", "n t")
            + E(100, 82, 14, 7, "d"))


PICS = {"si_hopper": si_hopper, "si_plant": si_plant, "si_branch": si_branch, "si_key": si_key, "si_sticks": si_sticks,
        "dv_island": dv_island, "dv_toffee": dv_toffee, "dv_cheese": dv_cheese,
        "si_coconut": coconuts, "dv_coconut": coconuts}
