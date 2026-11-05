# -*- coding: utf-8 -*-
"""Pictures for Books 70-73 (Shona, Kinyarwanda, Lingala, Wolof). Objects, plants and nature only.
viewBox 0 0 200 200. Each key carries the code of the first book that uses it (sn_, rw_, ln_, wo_);
the other books in this group reuse them (e.g. sn_rocks is also Wolof xeer)."""
import math
from illos import P, C, E, R, L, poly, leaf, cloud, ground


def _g(x, y, rot, body):
    return f'<g transform="translate({x} {y}) rotate({rot})">{body}</g>'


# ---------------------------------------------------------------- nature
def rocks():
    """dombo (Shona) / xeer (Wolof): a heap of smooth boulders."""
    return (cloud(24, 54, 0.55, "a")
            + P("M18 176 C12 110 50 66 96 68 C140 70 156 116 150 176 Z", "b")
            + P("M124 176 C122 134 146 112 170 118 C188 124 194 156 190 176 Z", "a")
            + P("M58 176 C56 150 78 138 98 142 C116 146 120 164 118 176 Z", "d")
            + P("M50 108 C62 96 78 92 92 96 M136 142 C144 134 156 132 166 136 M30 150 C36 140 44 136 52 136", "n t")
            + ground(176))


def sand():
    """jecha (Shona) / suuf (Wolof): sand dunes under the sun."""
    rays = "".join(L(152 + 26 * math.cos(math.radians(a)), 48 + 26 * math.sin(math.radians(a)),
                     152 + 34 * math.cos(math.radians(a)), 48 + 34 * math.sin(math.radians(a))) for a in range(0, 360, 45))
    grains = "".join(C(x, y, 1.8, "n") for x, y in [(40, 160), (62, 170), (90, 164), (120, 172), (150, 162), (170, 174), (76, 150)])
    return (C(152, 48, 18, "d") + rays
            + P("M14 118 C48 90 86 94 116 116 C136 102 166 98 186 106 L186 186 L14 186 Z", "d")
            + P("M14 150 C58 124 108 128 138 150 C158 140 176 140 186 144 L186 186 L14 186 Z", "a")
            + P("M40 128 C56 120 72 120 86 126 M128 120 C142 114 156 112 170 116", "n t") + grains
            + P("M54 140 C52 130 54 124 58 118 M58 140 C60 130 64 126 68 122 M50 140 C46 132 44 128 40 126", "n"))


def fire():
    """moto (Shona) / mɔtɔ (Lingala): a camp fire on crossed logs."""
    log = lambda x, y, rot: _g(x, y, rot, R(-62, -9, 124, 18, "d", 9) + E(56, 0, 5, 7, "n t"))
    stones = "".join(E(x, 178, 12, 7, "b") for x in (30, 58, 142, 170))
    return (log(100, 164, -14) + log(100, 164, 14)
            + P("M100 30 C118 62 152 82 142 126 C136 150 120 160 100 160 C80 160 62 150 58 126 C52 96 78 84 82 56 "
                "C90 72 96 66 100 30 Z", "e")
            + P("M100 84 C114 104 124 116 118 136 C114 148 108 152 100 152 C90 152 82 146 82 134 C82 116 96 108 100 84 Z", "d")
            + stones + P("M150 44 l6 -10 M40 70 l-6 -8 M160 90 l8 -4", "n t"))


def baobab():
    """muuyu (Shona): the great baobab tree, with hanging fruit."""
    branch = lambda d: P(d, "d")
    pods = "".join(L(x, y, x, y + 14, "n t") + E(x, y + 24, 6, 10, "e") for x, y in [(38, 70), (162, 66), (120, 44)])
    return (C(30, 58, 14, "c") + C(170, 54, 15, "c") + C(66, 34, 14, "c") + C(134, 32, 14, "c") + C(100, 26, 12, "c")
            + branch("M72 90 C60 76 44 66 30 62 L32 54 C50 58 66 68 80 82 Z")
            + branch("M128 90 C140 76 156 64 170 58 L172 66 C158 72 146 82 134 94 Z")
            + branch("M86 88 C80 70 72 50 66 36 L74 32 C82 48 90 66 96 86 Z")
            + branch("M110 86 C118 66 126 48 134 34 L142 38 C134 52 126 70 118 90 Z")
            + branch("M96 88 L98 30 L104 30 L106 88 Z")
            + P("M58 182 C72 150 76 120 70 88 L130 88 C124 120 128 150 142 182 Z", "d")
            + P("M84 110 C82 130 84 150 90 170 M112 106 C116 128 116 150 110 172", "n t") + pods + ground(182))


def forest():
    """zamba (Lingala): a forest of tall trees."""
    def tree(x, crown, r, h, cls):
        return R(x - 6, 180 - h, 12, h, "d", 3) + crown(x, 180 - h, r, cls)
    round_ = lambda x, y, r, c: C(x, y - r * 0.7, r, c)
    tall = lambda x, y, r, c: E(x, y - r, r * 0.7, r * 1.4, c)
    return (tree(56, tall, 30, 70, "c") + tree(150, round_, 34, 76, "c") + tree(100, round_, 40, 96, "c")
            + tree(30, round_, 20, 40, "c") + tree(176, tall, 16, 40, "c")
            + P("M64 180 C70 170 78 166 86 168 C92 162 104 162 110 170 C116 166 126 168 130 180 Z", "c")
            + leaf(112, 54, -40, 18, "n t") + ground(180))


# ---------------------------------------------------------------- plants & food
def pumpkin():
    """nhanga (Shona): a pumpkin with its leaf and curly tendril."""
    return (E(100, 126, 74, 52, "d")
            + P("M100 76 C76 90 72 160 100 178 M100 76 C124 90 128 160 100 178", "n t")
            + P("M64 86 C40 106 42 152 70 170 M136 86 C160 106 158 152 130 170", "n t")
            + R(94, 56, 12, 24, "c", 4) + leaf(106, 62, -24, 44, "c")
            + P("M94 60 C84 50 70 54 72 64 C74 72 84 68 82 62", "n"))


def pawpaw():
    """popo (Shona): a pawpaw (papaya), whole and cut open."""
    seeds = "".join(C(140 + 9 * math.cos(math.radians(a)) * (1 + (i % 2) * 0.5), 128 + 18 * math.sin(math.radians(a)) * (1 + (i % 2) * 0.4), 3.2, "b")
                    for i, a in enumerate(range(0, 360, 36)))
    return (P("M42 46 C70 30 98 50 104 92 C110 134 96 170 68 170 C40 170 26 134 26 96 C26 72 30 54 42 46 Z", "d")
            + P("M40 50 C34 40 36 30 44 24", "n") + leaf(44, 26, -60, 26, "c")
            + P("M44 70 C40 100 42 130 54 154", "n t")
            + E(140, 128, 40, 56, "d") + E(140, 128, 26, 40, "e") + seeds + ground(184))


def chilli():
    """pilipili (Lingala) / kaani (Wolof): two hot chilli peppers."""
    def pod(x, y, rot, s):
        return _g(x, y, rot,
                  P(f"M0 0 C{40*s} {-2*s} {80*s} {26*s} {100*s} {74*s} C{108*s} {96*s} {98*s} {104*s} {88*s} {94*s} "
                    f"C{70*s} {56*s} {38*s} {22*s} 0 {18*s} Z", "e")
                  + P(f"M{-12*s} {-4*s} C{-6*s} {-12*s} {6*s} {-12*s} {8*s} {-2*s} L{8*s} {20*s} C{0} {24*s} {-12*s} {20*s} {-12*s} {12*s} Z", "c")
                  + P(f"M{-6*s} {-8*s} C{-10*s} {-22*s} {-4*s} {-32*s} {8*s} {-38*s}", "n")
                  + P(f"M{20*s} {8*s} C{40*s} {10*s} {60*s} {24*s} {74*s} {44*s}", "n t"))
    return pod(40, 54, 0, 1.0) + pod(64, 112, -22, 0.82) + leaf(150, 60, -30, 30, "c") + ground(182)


def okra():
    """dongodongo (Lingala): a bunch of okra pods."""
    def pod(x, y, rot):
        return _g(x, y, rot,
                  P("M0 -13 C40 -17 92 -10 128 0 C92 10 40 17 0 13 Z", "c")
                  + P("M8 -5 C40 -6 80 -4 118 0 M8 5 C40 6 80 4 118 0", "n t")
                  + P("M-18 -11 L2 -14 L2 14 L-18 11 Z", "d") + L(-18, 0, -34, -6))
    return pod(54, 60, 30) + pod(44, 100, 8) + pod(50, 140, -16) + leaf(130, 40, -20, 40, "c") + ground(186)


def orange():
    """lilala (Lingala): an orange with its leaf and a slice."""
    segs = "".join(L(152, 170, 152 + 24 * math.cos(math.radians(a)), 170 - 24 * math.sin(math.radians(a)), "n t")
                    for a in (30, 60, 90, 120, 150))
    return (C(84, 106, 56, "d") + C(84, 106, 3, "n") + P("M54 80 C50 92 50 104 54 116", "n t")
            + P("M84 50 C84 40 88 34 94 30", "n") + leaf(92, 32, -30, 34, "c")
            + P("M118 170 A34 34 0 0 1 186 170 Z", "d") + P("M124 170 A28 28 0 0 1 180 170 Z", "a") + segs + ground(170))


def millet():
    """dugub (Wolof): millet stalks with their long grain heads."""
    def stalk(x, top, bend):
        head = "".join(C(x + bend + dx, top + dy, 2.4, "n") for dy in range(-22, 26, 8) for dx in (-4, 4))
        return (P(f"M{x} 182 C{x} 140 {x + bend} 110 {x + bend} {top + 30}", "n")
                + E(x + bend, top, 11, 32, "d") + head)
    return (stalk(60, 60, -10) + stalk(100, 46, 0) + stalk(140, 64, 12)
            + leaf(60, 140, -150, 40, "c") + leaf(100, 132, -30, 44, "c") + leaf(140, 146, -20, 36, "c")
            + leaf(100, 160, -160, 36, "c") + ground(182))


def cassava():
    """ñambi (Wolof): cassava roots under their leafy stem."""
    def root(rot, length, cls="d"):
        return _g(100, 108, rot,
                  P(f"M0 -12 C{length*0.3} -18 {length*0.7} -10 {length} 0 C{length*0.7} 10 {length*0.3} 18 0 12 Z", cls)
                  + P(f"M{length*0.3} -12 L{length*0.32} 12 M{length*0.55} -10 L{length*0.57} 10", "n t"))
    fan = "".join(_g(100, 50, a, P("M0 0 C8 -12 34 -14 56 0 C34 14 8 12 0 0 Z", "c")) for a in (-150, -115, -90, -65, -30))
    return (root(150, 78) + root(115, 86) + root(85, 90) + root(55, 84) + root(28, 76)
            + R(94, 50, 12, 58, "c", 4) + fan)


def sadza():
    """sadza (Shona): a white mound of maize porridge with green relish on a plate."""
    leaves = "".join(leaf(x, y, a, 30, "c") for x, y, a in [(122, 132, -20), (138, 142, -10), (152, 128, -60), (130, 118, -40)])
    return (E(100, 150, 84, 24, "a") + E(100, 146, 66, 16, "n t")
            + P("M32 146 C30 100 56 78 80 78 C106 78 124 100 122 146 Z", "a")
            + P("M48 112 C54 98 66 90 80 90", "n t") + leaves
            + P("M62 64 c-6 -10 6 -14 0 -24 M80 60 c-6 -10 6 -14 0 -24 M98 64 c-6 -10 6 -14 0 -24", "n t"))


def bread():
    """mburu (Wolof): two long loaves of bread."""
    def loaf(x, y, rot, cls):
        return _g(x, y, rot,
                  P("M-74 0 C-74 -16 -50 -22 0 -22 C50 -22 74 -16 74 0 C74 16 50 22 0 22 C-50 22 -74 16 -74 0 Z", cls)
                  + P("M-48 -14 C-40 -4 -36 4 -38 12 M-16 -16 C-8 -6 -4 2 -6 14 M16 -16 C24 -6 28 2 26 14 M48 -14 C56 -4 58 4 56 12", "n t"))
    crumbs = "".join(C(x, y, 2.4, "n") for x, y in [(40, 168), (150, 172), (160, 164), (60, 174)])
    return loaf(100, 86, -24, "d") + loaf(100, 132, 14, "a") + crumbs + ground(178)


# ---------------------------------------------------------------- things
def wheel():
    """vhiri (Shona): a wheel."""
    spokes = "".join(L(100 + 12 * math.cos(math.radians(a)), 100 + 12 * math.sin(math.radians(a)),
                       100 + 54 * math.cos(math.radians(a)), 100 + 54 * math.sin(math.radians(a))) for a in range(0, 360, 30))
    treads = "".join(L(100 + 68 * math.cos(math.radians(a)), 100 + 68 * math.sin(math.radians(a)),
                       100 + 76 * math.cos(math.radians(a)), 100 + 76 * math.sin(math.radians(a)), "n t") for a in range(0, 360, 20))
    return C(100, 100, 76, "b") + C(100, 100, 58, "a") + spokes + treads + C(100, 100, 14, "d") + C(100, 100, 4, "n") + ground(178)


def key():
    """urufunguzo (Kinyarwanda): a key on its ring."""
    def k(x, y, rot, s, cls):
        return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
                + R(20, -8, 120, 16, cls, 5) + R(112, 6, 10, 24, cls, 2) + R(128, 6, 10, 18, cls, 2)
                + C(0, 0, 38, cls) + C(0, 0, 14, "a") + P("M-26 -12 C-22 -24 -14 -30 -4 -32", "n t") + "</g>")
    return k(70, 64, 20, 0.62, "b") + k(52, 126, -8, 0.95, "d") + ground(184)


def tent():
    """ihema (Kinyarwanda): a tent."""
    return (L(100, 40, 100, 22) + poly([(100, 22), (124, 28), (100, 34)], "e")
            + poly([(100, 40), (24, 170), (176, 170)], "b")
            + poly([(100, 64), (72, 170), (128, 170)], "a")
            + P("M100 64 L100 170", "n t")
            + L(24, 170, 12, 180) + L(176, 170, 188, 180)
            + cloud(130, 64, 0.5, "a") + ground(170))


def bicycle():
    """vɛlɔ (Lingala): a bicycle."""
    def wheel_(x):
        sp = "".join(L(x + 4 * math.cos(math.radians(a)), 136 + 4 * math.sin(math.radians(a)),
                       x + 30 * math.cos(math.radians(a)), 136 + 30 * math.sin(math.radians(a)), "n t") for a in range(0, 360, 45))
        return C(x, 136, 36, "a") + C(x, 136, 30, "n t") + sp + C(x, 136, 4, "d")
    frame = P("M46 136 L96 136 L80 88 Z M80 88 L136 88 L96 136 M136 88 L154 136", "n")
    return (wheel_(46) + wheel_(154) + frame
            + P("M64 80 C66 72 92 72 96 80 C90 86 70 86 64 80 Z", "d") + L(80, 88, 80, 82)
            + P("M136 88 L132 66 M120 64 C126 60 138 60 146 66", "n") + C(96, 136, 9, "e")
            + L(96, 136, 104, 150) + R(98, 148, 14, 5, "d", 2) + ground(174))


def alluwa():
    """àlluwa (Wolof): the wooden writing board children use in Qur'an school (daara), with an ink pot and reed pen."""
    lines = "".join(P(f"M{60} {y} c10 -6 20 6 30 0 s20 -6 30 0 s14 4 20 0", "n t") for y in range(80, 170, 18))
    return (P("M78 52 L78 32 C78 18 118 18 118 32 L118 52 Z", "d") + C(98, 34, 6, "a")
            + R(44, 50, 108, 136, "d", 10) + R(52, 62, 92, 114, "a", 6) + lines
            + P("M160 160 L186 160 L182 186 L164 186 Z", "b") + E(173, 160, 13, 4, "n")
            + L(170, 156, 194, 96) + L(176, 158, 196, 104, "n t"))


def road():
    """yoon (Wolof): a road winding away to the hills."""
    return (C(150, 46, 18, "d") + cloud(26, 58, 0.55, "a")
            + P("M14 104 C44 84 70 86 96 100 C118 84 150 80 186 98 L186 120 L14 120 Z", "c")
            + P("M92 120 C86 136 60 150 40 186 L118 186 C116 160 110 138 106 120 Z", "b")
            + P("M99 124 L97 132 M93 142 L89 152 M84 162 L78 176", "n")
            + leaf(150, 160, -100, 26, "c") + leaf(150, 160, -60, 26, "c") + leaf(30, 150, -110, 22, "c") + leaf(30, 150, -70, 22, "c") + ground(186))


PICS = {
    "sn_rocks": rocks, "sn_sand": sand, "sn_fire": fire, "sn_baobab": baobab, "sn_pumpkin": pumpkin,
    "sn_pawpaw": pawpaw, "sn_sadza": sadza, "sn_wheel": wheel,
    "rw_key": key, "rw_tent": tent,
    "ln_forest": forest, "ln_chilli": chilli, "ln_okra": okra, "ln_orange": orange, "ln_bicycle": bicycle,
    "wo_millet": millet, "wo_cassava": cassava, "wo_bread": bread, "wo_alluwa": alluwa, "wo_road": road,
}
