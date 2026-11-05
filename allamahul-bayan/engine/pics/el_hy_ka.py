# -*- coding: utf-8 -*-
"""Pictures for Book 34 Greek (el_), Book 35 Armenian (hy_) and Book 36 Georgian (ka_).
Objects, plants and nature only. viewBox 0 0 200 200; every closed shape has a colour role a-e.

(The file is not called el.py / hy.py / ka.py on purpose: a plug-in module with the same name as a
language file would shadow languages/<code>.py when build.py imports it.)"""
import math
from illos import P, C, E, R, L, poly, star, star_pts, crescent, cloud, leaf, ground


def bread():
    """A round-topped loaf on a board, with scored cuts."""
    return (R(16, 150, 168, 20, "b", 8)
            + P("M30 152 L30 116 C30 76 62 60 100 60 C138 60 170 76 170 116 L170 152 Z", "d")
            + P("M58 86 l22 26 M92 74 l22 30 M128 80 l20 26", "n")
            + P("M40 140 C80 146 120 146 160 140", "n t"))


def logs():
    """Firewood stacked end-on (3 + 2 + 1), each log with growth rings."""
    out = ""
    for cy, xs in ((152, (48, 100, 152)), (108, (74, 126)), (64, (100,))):
        for cx in xs:
            out += C(cx, cy, 25, "e") + C(cx, cy, 15, "n t") + C(cx, cy, 6, "n t")
    return out + ground(178)


def round_fruit():
    """Apricot / peach: round fruit with a crease, stem and leaf."""
    return (P("M100 62 C150 60 174 100 166 136 C158 172 122 182 100 172 C78 182 42 172 34 136 "
              "C26 100 50 60 100 62 Z", "d")
            + P("M100 66 C88 100 92 140 100 172", "n t")
            + P("M100 64 C100 52 104 42 112 34", "n")
            + leaf(108, 46, -25, 46, "c"))


def strawberry():
    seeds = "".join(E(x, y, 2.5, 4.5, "n t") for x, y in
                    ((76, 92), (100, 88), (124, 92), (66, 116), (90, 112), (112, 112), (134, 116),
                     (80, 138), (102, 136), (122, 138), (92, 158), (110, 158)))
    return (P("M100 180 C58 150 34 112 40 84 C44 62 72 56 100 66 C128 56 156 62 160 84 "
              "C166 112 142 150 100 180 Z", "e") + seeds
            + poly([(62, 68), (82, 60), (74, 42), (94, 52), (100, 34), (106, 52), (126, 42),
                    (118, 60), (138, 68), (100, 74)], "c")
            + P("M100 36 C100 26 104 18 110 14", "n"))


def lamp():
    """A small clay oil lamp with a flame."""
    return (E(96, 164, 40, 9, "b")
            + P("M46 130 C46 108 70 98 102 98 C128 98 148 106 170 102 L178 114 C160 120 156 136 140 148 "
                "C120 160 72 160 58 150 C50 144 46 138 46 130 Z", "e")
            + P("M50 120 C26 116 24 148 54 146", "n")
            + E(100, 106, 14, 5, "a")
            + P("M176 102 C166 90 170 74 180 60 C188 74 194 90 184 102 Z", "d")
            + P("M180 96 C176 90 178 82 181 76", "n t")
            + ground(180))


def peas():
    pod = P("M22 122 C48 70 140 46 182 66 C154 120 72 152 22 122 Z", "c")
    inner = P("M30 118 C72 118 140 96 176 70", "n t")
    balls = "".join(C(x, y, 13, "a") for x, y in ((62, 108), (90, 98), (118, 88), (146, 78)))
    return (pod + balls + inner + P("M182 66 C192 56 190 42 178 40", "n")
            + leaf(60, 160, -20, 50, "c") + leaf(110, 168, -10, 40, "c"))


def basil():
    """A basil sprig growing in a little pot."""
    lv = (leaf(100, 124, -150, 44) + leaf(100, 124, -30, 44)
          + leaf(100, 96, -140, 38) + leaf(100, 96, -40, 38)
          + leaf(100, 70, -130, 30) + leaf(100, 70, -50, 30)
          + leaf(100, 50, -90, 24))
    return (P("M100 146 C100 120 99 90 100 52", "n") + lv
            + P("M62 152 L138 152 L128 190 L72 190 Z", "b") + R(54, 140, 92, 15, "b", 5))


def cucumber():
    bumps = "".join(L(x, y, x + 3, y + 3, "n t") for x, y in ((50, 120), (76, 104), (104, 92), (130, 80), (68, 136), (96, 122), (124, 108)))
    seeds = "".join(E(150 + 9 * math.cos(math.radians(a)), 160 + 9 * math.sin(math.radians(a)), 2.5, 4.5, "n t",
                      rot=a + 90) for a in range(0, 360, 60))
    return (E(96, 108, 80, 28, "c", -22) + bumps + P("M168 76 l12 -8", "n")
            + C(150, 160, 26, "c") + C(150, 160, 20, "a") + seeds
            + leaf(30, 168, -10, 50, "c"))


def wheat():
    def ear(x0, y0, x1, y1):
        out = P(f"M{x0} {y0} L{x1} {y1}", "n")
        for i in range(5):
            t = 0.08 + i * 0.07
            x, y = x1 + (x0 - x1) * t, y1 + (y0 - y1) * t
            ang = math.degrees(math.atan2(y0 - y1, x0 - x1))
            out += E(round(x - 7, 1), round(y, 1), 6, 12, "d", round(ang - 90 - 25, 1))
            out += E(round(x + 7, 1), round(y, 1), 6, 12, "d", round(ang - 90 + 25, 1))
        out += E(x1, y1 - 4, 5, 10, "d", round(math.degrees(math.atan2(y0 - y1, x0 - x1)) - 90, 1))
        return out
    return (ear(100, 186, 100, 30) + ear(96, 186, 50, 46) + ear(104, 186, 150, 46)
            + P("M70 170 C90 160 110 160 130 170 L126 182 C110 176 90 176 74 182 Z", "b"))


def beads():
    """A string of round beads (a necklace)."""
    out = P("M40 36 Q100 230 160 36", "n t")
    cls = "ade"
    for i in range(13):
        t = i / 12
        x = (1 - t) ** 2 * 40 + 2 * (1 - t) * t * 100 + t * t * 160
        y = (1 - t) ** 2 * 36 + 2 * (1 - t) * t * 230 + t * t * 36
        out += C(x, y, 11 if i % 2 else 9, cls[i % 3])
    return out + R(32, 22, 16, 14, "b", 3) + R(152, 22, 16, 14, "b", 3)


def stones():
    return (P("M18 178 C18 150 40 138 70 140 C100 142 118 156 116 178 Z", "b")
            + P("M108 178 C108 154 128 142 152 144 C176 146 186 160 184 178 Z", "e")
            + P("M58 140 C56 112 80 98 104 102 C130 106 140 124 132 146 C112 150 80 150 58 140 Z", "a")
            + E(150, 128, 16, 10, "d", -10) + E(40, 130, 12, 8, "d", 10)
            + P("M74 118 C84 112 96 112 104 116", "n t") + ground(180))


def snowdrop():
    """Two snowdrop flowers (drooping white bells) with long leaves."""
    def flower(sx, sy, s=1.0):
        out = C(sx, sy, 5 * s, "c")
        for ang in (-28, 28, 0):
            out += (f'<g transform="rotate({ang} {sx} {sy})">'
                    + P(f"M{sx} {sy + 4*s} C{sx - 13*s} {sy + 22*s} {sx - 10*s} {sy + 44*s} {sx} {sy + 52*s} "
                        f"C{sx + 10*s} {sy + 44*s} {sx + 13*s} {sy + 22*s} {sx} {sy + 4*s} Z", "a") + "</g>")
        return out
    return (P("M96 186 C76 150 72 116 82 88 C94 116 100 150 102 186 Z", "c")
            + P("M108 186 C124 150 130 120 124 96 C112 122 106 150 102 186 Z", "c")
            + P("M100 186 C100 120 106 66 136 52", "n") + flower(138, 54)
            + P("M98 186 C94 140 80 100 56 86", "n") + flower(54, 88, 0.8)
            + ground(186))


def raspberry():
    out = ""
    for cy, n in ((80, 3), (102, 4), (124, 4), (146, 3), (166, 2)):
        for i in range(n):
            out += C(100 + (i - (n - 1) / 2) * 23, cy, 13, "e")
    return (out + poly(star_pts(100, 66, 30, 9, 5, -90), "c")
            + P("M100 60 C100 48 104 38 112 30", "n") + leaf(112, 34, -20, 44, "c"))



def stars_to_count(n):
    """n stars to count (for number words)."""
    if n == 2:
        pos = [(62, 100, 40), (140, 100, 40)]
    else:  # 7: a row of 4 over a row of 3
        pos = [(31 + 46 * i, 72, 23) for i in range(4)] + [(54 + 46 * i, 136, 23) for i in range(3)]
    return "".join(star(x, y, r, r * 0.45, "dea"[i % 3]) for i, (x, y, r) in enumerate(pos))


def milk():
    """A bottle of milk and a full glass."""
    return (P("M54 64 L54 46 L90 46 L90 64 C108 76 112 92 112 110 L112 176 C112 182 108 186 102 186 "
              "L42 186 C36 186 32 182 32 176 L32 110 C32 92 36 76 54 64 Z", "a")
            + R(50, 30, 44, 18, "d", 4) + R(32, 118, 80, 40, "b", 2)
            + P("M128 98 L176 98 L168 186 L136 186 Z", "a") + P("M131 118 L173 118", "n t")
            + ground(186))


PICS = {
    "el_bread": bread, "el_logs": logs,
    "hy_apricot": round_fruit, "hy_strawberry": strawberry, "hy_lamp": lamp, "hy_peas": peas,
    "hy_basil": basil, "hy_cucumber": cucumber, "hy_wheat": wheat, "hy_beads": beads, "hy_stones": stones,
    "ka_peach": round_fruit, "ka_bread": bread, "ka_snowdrop": snowdrop, "ka_raspberry": raspberry,
    "hy_seven": lambda: stars_to_count(7), "ka_two": lambda: stars_to_count(2), "ka_milk": milk,
}
