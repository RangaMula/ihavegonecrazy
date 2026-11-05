# -*- coding: utf-8 -*-
"""Pictures for Book 31 (Malay in Jawi). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, poly, cloud, ground


def calendar(label="٣"):      # ثلاث Selasa - a wall calendar page
    grid = "".join(R(44 + 24 * c, 104 + 20 * r, 18, 14, "a", 2) for r in range(3) for c in range(5))
    return (R(30, 40, 140, 146, "a", 10) + R(30, 40, 140, 44, "e", 10) + R(30, 70, 140, 14, "e")
            + C(64, 40, 7, "b") + C(136, 40, 7, "b") + L(64, 30, 64, 46) + L(136, 30, 136, 46)
            + R(84, 52, 32, 26, "d", 6)
            + f'<text x="100" y="74" text-anchor="middle" class="lbl" font-size="22">{label}</text>'
            + grid + R(92, 124, 18, 14, "c", 2))


def tent():               # خيمه khemah - a tent on the grass
    return (P("M20 176 L100 40 L180 176 Z", "a")
            + P("M100 40 L76 176 L124 176 Z", "e")
            + P("M100 70 L86 176 L114 176 Z", "d")
            + L(100, 40, 100, 24) + P("M100 24 L122 30 L100 36 Z", "c")
            + L(20, 176, 8, 186) + L(180, 176, 192, 186)
            + C(160, 40, 12, "d") + cloud(20, 70, 0.4) + ground(184))


def leaf_big():           # داون daun - a large leaf
    return (P("M40 168 C30 110 60 50 160 30 C168 110 120 168 40 168 Z", "c")
            + P("M40 168 C80 120 120 80 160 30", "n")
            + P("M64 140 L60 108 M84 120 L80 84 M106 98 L104 64 M128 74 L128 46 M70 134 L104 136 M92 112 L126 114 M114 88 L142 88", "n t")
            + P("M40 168 L22 186", "n") + ground(188))


def sunset():             # مغرب Maghrib - the sun setting over the sea
    rays = "".join(L(100 + 48 * math.cos(math.radians(a)), 120 + 48 * math.sin(math.radians(a)),
                     100 + 70 * math.cos(math.radians(a)), 120 + 70 * math.sin(math.radians(a))) for a in range(-160, -19, 28))
    return (rays + P("M62 120 A38 38 0 0 1 138 120 Z", "d")
            + R(10, 120, 180, 66, "b")
            + P("M24 140 q10 -6 20 0 q10 6 20 0 M110 152 q10 -6 20 0 q10 6 20 0 M60 170 q10 -6 20 0 q10 6 20 0", "n t")
            + P("M140 40 a14 14 0 1 0 12 22 a11 11 0 1 1 -12 -22 Z", "e")
            + C(40, 50, 3, "a") + C(172, 76, 3, "a") + C(60, 30, 2.5, "a"))


def ketupat():            # کتوڤت ketupat - a woven palm-leaf rice pouch
    body = poly([(100, 54), (156, 110), (100, 166), (44, 110)], "a")
    weave = "".join(L(72 + 14 * k, 82 + 14 * k - 28, 72 + 14 * k - 28, 82 + 14 * k, "n t") for k in range(0))
    lines = (L(86, 68, 142, 124, "n t") + L(72, 82, 128, 138, "n t") + L(58, 96, 114, 152, "n t")
             + L(114, 68, 58, 124, "n t") + L(128, 82, 72, 138, "n t") + L(142, 96, 86, 152, "n t"))
    tails = (P("M100 54 C96 36 104 24 92 10 C110 18 112 36 106 56 Z", "c")
             + P("M100 54 C108 40 122 34 132 20 C130 40 118 50 104 58 Z", "c"))
    return tails + body + weave + lines + R(90, 100, 20, 20, "d", 2) + ground(186)


def palm():               # ڽيور nyiur - a coconut palm by the shore
    trunk = P("M96 186 C100 150 104 110 108 70 L118 70 C116 110 114 150 112 186 Z", "b")
    rings = "".join(L(100 + k * 0.1, 176 - 18 * k, 113 + k * 0.4, 174 - 18 * k, "n t") for k in range(6))
    fronds = "".join(P(d, "c") for d in [
        "M112 70 C90 50 60 50 30 70 C60 62 88 64 112 74 Z",
        "M112 70 C100 40 80 26 56 22 C84 36 100 52 110 74 Z",
        "M114 70 C126 40 148 28 172 30 C146 42 128 54 116 74 Z",
        "M116 72 C140 56 170 60 190 84 C164 72 140 70 116 76 Z",
        "M112 74 C96 84 82 104 76 126 C92 104 104 92 116 78 Z"])
    nuts = C(108, 82, 7, "d") + C(120, 84, 7, "d") + C(114, 92, 7, "d")
    return (P("M10 170 C60 160 140 160 190 172 L190 186 L10 186 Z", "e") + trunk + rings + fronds + nuts
            + C(40, 36, 10, "d"))


PICS = {"ms_calendar": calendar, "ms_tent": tent, "ms_leaf": leaf_big, "ms_sunset": sunset,
        "ms_ketupat": ketupat, "ms_palm": palm}
