# -*- coding: utf-8 -*-
"""Pictures for the Central Asian Cyrillic books (Kazakh kk, Tatar tt, Tajik tg, Mongolian mn).
All keys are prefixed kk_ (one agent, one file) and are shared by those four books.
Objects, plants and nature only - no people, no animals, no faces.  viewBox 0 0 200 200.
Default cover colours: a white, b blue, c green, d yellow, e coral."""
from illos import P, C, E, R, L, poly, star, cloud, leaf, ground


def _rot(a, cx, cy, body):
    return f'<g transform="rotate({a} {cx} {cy})">{body}</g>'


def bicycle():
    wheels = ""
    for cx in (48, 152):
        wheels += C(cx, 134, 38, "b") + C(cx, 134, 30, "a") + C(cx, 134, 6, "e")
        wheels += "".join(L(cx, 134, cx + 30 * c, 134 + 30 * s, "n t")
                          for c, s in ((1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)))
    frame = P("M48 134 L98 134 L80 84 Z M80 84 L132 86 L98 134 M132 86 L152 134", "n")
    return (wheels + frame + C(98, 134, 9, "d")
            + P("M64 76 C64 70 92 70 94 76 C94 82 66 82 64 76 Z", "e") + L(80, 84, 78, 78)
            + P("M132 86 L126 62", "n") + P("M114 60 C120 56 134 56 140 62", "n") + ground(174))


def fir():
    return (R(88, 154, 24, 26, "e", 3)
            + poly([(100, 84), (172, 158), (28, 158)], "c")
            + poly([(100, 52), (152, 114), (48, 114)], "c")
            + poly([(100, 16), (136, 74), (64, 74)], "c")
            + P("M64 140 C80 134 92 146 108 138 C120 132 132 142 144 138", "n t")
            + P("M70 100 C84 94 96 104 110 98 C120 94 128 100 134 98", "n t") + ground(182))


def needle():
    body = (P("M100 22 C108 22 110 30 110 42 L104 168 L100 186 L96 168 L90 42 C90 30 92 22 100 22 Z", "a")
            + E(100, 40, 3.5, 10, "n"))
    return (R(16, 130, 52, 46, "d", 4) + R(10, 122, 64, 10, "e", 3) + R(10, 174, 64, 10, "e", 3)
            + "".join(L(18, 140 + 8 * k, 66, 140 + 8 * k, "n t") for k in range(5))
            + _rot(-45, 100, 100, body)
            + P("M58 58 C34 26 8 60 28 86 C44 106 30 116 42 124", "n"))


def apricot():
    return (C(150, 148, 30, "d") + P("M150 118 C140 135 140 160 150 178", "n t")
            + C(92, 112, 60, "d") + P("M92 52 C72 86 72 140 92 172", "n t")
            + P("M92 52 C94 40 98 32 104 26", "n") + leaf(104, 32, -25, 46, "c") + ground(186))


def gem():
    return (poly([(55, 58), (145, 58), (176, 94), (100, 182), (24, 94)], "d")
            + P("M24 94 H176 M55 58 L78 94 L100 58 L122 94 L145 58 M78 94 L100 182 L122 94", "n t")
            + star(168, 36, 12, 4, "a", 4) + star(34, 34, 9, 3, "a", 4) + star(178, 150, 7, 2.5, "a", 4))


def suitcase():
    return (P("M78 74 V54 C78 44 122 44 122 54 V74 H112 V58 C112 54 88 54 88 58 V74 Z", "e")
            + R(26, 72, 148, 100, "b", 14) + R(54, 72, 14, 100, "e") + R(132, 72, 14, 100, "e")
            + R(90, 84, 20, 12, "d", 3) + C(48, 180, 7, "a") + C(152, 180, 7, "a"))


def brush():
    bristles = "".join(L(x, 112, x, 150, "n t") for x in range(40, 164, 8))
    return (R(34, 110, 132, 40, "d", 4) + bristles
            + P("M28 112 C28 84 60 70 100 70 C140 70 172 84 172 112 Z", "e")
            + E(100, 74, 26, 9, "b") + C(70, 96, 4, "a") + C(100, 92, 4, "a") + C(130, 96, 4, "a") + ground(170))


def palm():
    fronds = "".join(leaf(110, 66, a, s, "c") for a, s in ((168, 80), (205, 74), (245, 60), (295, 62), (335, 76), (12, 80)))
    trunk = P("M94 184 C90 144 94 104 104 66 L116 66 C110 104 108 144 114 184 Z", "e")
    rings = "".join(L(94 + k * 0.6, 170 - k * 16, 113 - k * 0.4, 166 - k * 16, "n t") for k in range(7))
    dates = "".join(C(x, y, 6, "d") for x, y in ((100, 80), (112, 84), (124, 80), (106, 92), (118, 94)))
    return trunk + rings + fronds + dates + ground(184)


def ornament():
    petals = "".join(_rot(a, 100, 100, E(100, 64, 12, 30, "c")) for a in range(0, 360, 45))
    corners = ""
    for cx, cy, sx, sy in ((36, 36, 1, 1), (164, 36, -1, 1), (36, 164, 1, -1), (164, 164, -1, -1)):
        corners += P(f"M{cx} {cy} L{cx + 34 * sx} {cy} C{cx + 34 * sx} {cy + 16 * sy} {cx + 16 * sx} {cy + 18 * sy} "
                     f"{cx + 16 * sx} {cy + 10 * sy} C{cx + 16 * sx} {cy + 4 * sy} {cx + 24 * sx} {cy + 4 * sy} {cx + 24 * sx} {cy + 10 * sy} "
                     f"M{cx} {cy} L{cx} {cy + 34 * sy} C{cx + 16 * sx} {cy + 34 * sy} {cx + 18 * sx} {cy + 16 * sy} "
                     f"{cx + 10 * sx} {cy + 16 * sy} C{cx + 4 * sx} {cy + 16 * sy} {cx + 4 * sx} {cy + 24 * sy} {cx + 10 * sx} {cy + 24 * sy}", "n")
    return (R(18, 18, 164, 164, "b", 16) + R(30, 30, 140, 140, "a", 10) + petals
            + C(100, 100, 18, "d") + star(100, 100, 10, 5, "e", 8) + corners)


def cucumber():
    dots = "".join(C(x, y, 2.2, "n") for x, y in ((60, 122), (80, 110), (100, 100), (120, 90), (140, 82), (75, 128), (110, 108), (150, 90)))
    return (P("M28 140 C34 100 120 66 164 64 C182 64 184 84 168 90 C130 104 80 130 56 152 C42 164 24 158 28 140 Z", "c")
            + dots + P("M164 64 C172 54 180 50 188 50", "n")
            + C(140, 152, 28, "c") + C(140, 152, 21, "a")
            + "".join(E(140 + 10 * c, 152 + 10 * s, 2.5, 4.5, "n t") for c, s in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            + leaf(30, 60, -20, 50, "c") + ground(186))


def helicopter():
    return (R(26, 52, 148, 7, "d", 3) + R(96, 58, 8, 14, "e")
            + poly([(52, 98), (10, 86), (10, 102), (52, 118)], "b") + C(14, 86, 11, "a")
            + E(100, 108, 54, 36, "b")
            + P("M106 76 C138 78 152 100 152 112 L106 112 Z", "a")
            + P("M78 142 V158 M124 142 V158", "n") + R(54, 156, 98, 6, "e", 3)
            + cloud(130, 196, 0.5) + cloud(10, 190, 0.35))


def magazine():
    back = _rot(-10, 100, 100, R(46, 26, 110, 150, "e", 4))
    return (back + R(48, 22, 110, 154, "a", 4) + R(58, 32, 90, 22, "d", 4)
            + R(58, 64, 90, 62, "b", 4) + C(126, 82, 9, "d")
            + P("M58 126 L84 92 L104 116 L116 102 L148 126 Z", "c")
            + "".join(L(60, 140 + 10 * k, 146 - 20 * (k % 2), 140 + 10 * k, "n t") for k in range(3)))


def strawberry():
    seeds = "".join(E(x, y, 2, 3.5, "a") for x, y in ((80, 96), (100, 92), (120, 96), (70, 116), (90, 114), (110, 114), (130, 116),
                                                     (80, 134), (100, 134), (120, 134), (90, 152), (110, 152), (100, 166)))
    return (P("M100 182 C64 160 40 120 48 90 C56 66 144 66 152 90 C160 120 136 160 100 182 Z", "e") + seeds
            + P("M100 74 L74 62 L88 58 L76 44 L96 52 L100 36 L104 52 L124 44 L112 58 L126 62 Z", "c")
            + P("M100 40 C100 30 104 22 112 18", "n") + ground(190))


def sprout():
    return (P("M64 124 L136 124 L128 182 L72 182 Z", "e") + R(56, 112, 88, 16, "e", 4)
            + P("M100 112 C100 90 98 70 100 50", "n")
            + leaf(100, 92, -155, 52, "c") + leaf(100, 72, -25, 52, "c") + leaf(100, 50, -95, 30, "c")
            + E(100, 112, 40, 4, "n t"))


def rehal():
    lines = "".join(P(f"M{38 + 0} {72 + 10 * k} C60 {66 + 10 * k} 80 {70 + 10 * k} 94 {78 + 10 * k}", "n t")
                    + P(f"M106 {78 + 10 * k} C120 {70 + 10 * k} 140 {66 + 10 * k} 162 {72 + 10 * k}", "n t") for k in range(3))
    return (poly([(44, 184), (64, 184), (150, 104), (130, 104)], "e")
            + poly([(136, 184), (156, 184), (70, 104), (50, 104)], "e")
            + P("M100 112 C80 98 50 94 28 100 L28 58 C50 52 80 56 100 70 Z", "a")
            + P("M100 112 C120 98 150 94 172 100 L172 58 C150 52 120 56 100 70 Z", "a")
            + L(100, 70, 100, 112) + lines + star(100, 30, 12, 6, "d", 8) + ground(186))


def bigleaf():
    veins = "".join(L(t, 0, t + 24, -22, "n t") + L(t, 0, t + 24, 22, "n t") for t in (36, 66, 96, 126))
    return (P("M38 178 L58 156", "n")
            + f'<g transform="translate(52 160) rotate(-48)">'
            + P("M0 0 C50 -70 130 -70 190 0 C130 70 50 70 0 0 Z", "c") + L(0, 0, 176, 0, "n") + veins + "</g>")


def sieve():
    mesh = "".join(L(48 + 13 * k, 70, 48 + 13 * k, 92, "n t") for k in range(9)) + "".join(L(42, 74 + 7 * k, 158, 74 + 7 * k, "n t") for k in range(3))
    grains = "".join(C(x, y, 2.5, "d") for x, y in ((70, 140), (90, 152), (110, 146), (130, 158), (84, 172), (118, 176), (100, 186)))
    return (P("M24 80 L28 112 C30 128 170 128 172 112 L176 80 Z", "e")
            + E(100, 80, 76, 20, "b") + E(100, 81, 62, 14, "a") + mesh + grains)


def clover():
    leaflet = P("M100 108 C72 96 66 56 90 58 C96 58 100 64 100 70 C100 64 104 58 110 58 C134 56 128 96 100 108 Z", "c")
    return (P("M100 190 C100 160 96 134 100 108", "n") + P("M100 160 C120 140 140 118 148 82", "n")
            + "".join(_rot(a, 100, 108, leaflet) for a in (0, 120, 240))
            + E(150, 64, 15, 22, "d") + P("M138 56 l10 6 l10 -6 M138 68 l10 6 l10 -6", "n t") + ground(190))


def vase():
    return (P("M82 30 H118 L114 52 C150 72 160 122 132 158 L126 182 H74 L68 158 C40 122 50 72 86 52 Z", "b")
            + E(100, 30, 20, 5, "e") + P("M56 104 C80 116 120 116 144 104 L146 120 C120 132 80 132 54 120 Z", "d")
            + C(100, 82, 8, "e") + C(76, 86, 5, "e") + C(124, 86, 5, "e") + ground(184))


def ger():
    lattice = "".join(L(34 + 16 * k, 116, 50 + 16 * k, 170, "n t") + L(50 + 16 * k, 116, 34 + 16 * k, 170, "n t") for k in range(8))
    return (R(30, 112, 140, 60, "a") + lattice
            + P("M20 116 C48 74 80 58 100 56 C120 58 152 74 180 116 Z", "b")
            + P("M40 100 C70 92 130 92 160 100", "n t") + E(100, 56, 16, 6, "e")
            + R(84, 128, 32, 44, "d", 2) + R(90, 134, 20, 32, "e", 2) + ground(172))


def rocket():
    return (P("M100 18 C132 48 136 100 128 140 H72 C64 100 68 48 100 18 Z", "a")
            + C(100, 76, 15, "b") + C(100, 76, 9, "a")
            + poly([(73, 104), (44, 150), (72, 146)], "e") + poly([(127, 104), (156, 150), (128, 146)], "e")
            + P("M82 140 C84 162 94 172 100 190 C106 172 116 162 118 140 Z", "d")
            + P("M92 140 C94 154 98 160 100 172 C102 160 106 154 108 140 Z", "e")
            + P("M76 110 H124", "n t") + star(34, 40, 9, 4, "d") + star(166, 60, 7, 3, "d") + star(170, 160, 6, 2.6, "d"))


def shirt():
    return (P("M68 30 C80 44 120 44 132 30 L172 52 L156 90 L138 82 V176 H62 V82 L44 90 L28 52 Z", "b")
            + P("M68 30 C78 52 122 52 132 30", "n") + star(100, 112, 20, 9, "d") + ground(186))


def candy():
    big = (poly([(64, 92), (24, 64), (32, 92), (24, 120)], "c") + poly([(136, 92), (176, 64), (168, 92), (176, 120)], "c")
           + E(100, 92, 40, 26, "d") + P("M80 70 C90 84 90 100 80 114 M100 66 C110 80 110 104 100 118 M120 70 C130 84 130 100 120 114", "n t"))
    small = _rot(-20, 120, 160, poly([(104, 160), (84, 148), (88, 160), (84, 172)], "b") + poly([(136, 160), (156, 148), (152, 160), (156, 172)], "b")
                 + E(120, 160, 18, 12, "e"))
    return big + small


def road():
    dashes = "".join(P(f"M{x} {y} l{dx} {dy}", "n") for x, y, dx, dy in ((104, 98, 2, 6), (110, 116, 4, 8), (118, 138, 2, 12), (114, 164, -4, 14)))
    return (C(150, 44, 16, "d") + poly([(10, 96), (50, 52), (84, 96)], "b") + poly([(60, 96), (110, 40), (160, 96)], "b")
            + L(10, 96, 190, 96)
            + P("M60 190 C80 160 130 150 116 120 C108 106 96 104 100 96 H108 C108 104 124 108 128 122 C142 156 106 166 150 190 Z", "e")
            + dashes + leaf(36, 150, -90, 30, "c") + leaf(36, 150, -50, 26, "c") + leaf(170, 140, -120, 30, "c") + leaf(170, 140, -70, 26, "c")
            + L(36, 150, 36, 176) + L(170, 140, 170, 168))


def funnel():
    return (P("M38 50 L162 50 L112 120 V172 H88 V120 Z", "b") + E(100, 50, 62, 12, "a")
            + P("M100 182 C96 188 96 194 100 196 C104 194 104 188 100 182 Z", "c")
            + P("M60 58 L104 116", "n t"))


PICS = {"kk_bicycle": bicycle, "kk_fir": fir, "kk_needle": needle, "kk_apricot": apricot, "kk_gem": gem,
        "kk_suitcase": suitcase, "kk_brush": brush, "kk_palm": palm, "kk_ornament": ornament, "kk_cucumber": cucumber,
        "kk_helicopter": helicopter, "kk_magazine": magazine, "kk_strawberry": strawberry, "kk_sprout": sprout,
        "kk_rehal": rehal, "kk_leaf": bigleaf, "kk_sieve": sieve, "kk_clover": clover, "kk_vase": vase, "kk_ger": ger,
        "kk_rocket": rocket, "kk_shirt": shirt, "kk_candy": candy, "kk_road": road, "kk_funnel": funnel}
