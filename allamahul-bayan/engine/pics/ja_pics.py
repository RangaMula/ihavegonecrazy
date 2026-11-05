# -*- coding: utf-8 -*-
"""Pictures for Book 46 (Japanese). Objects, plants and nature only (viewBox 0 0 200 200)."""
import math
from illos import P, C, E, R, L, leaf, ground


def _rot(x, y, cx, cy, deg):
    a = math.radians(deg)
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def pencil():
    body = (R(88, 40, 24, 100, "b") + L(96, 40, 96, 140, "n t") + L(104, 40, 104, 140, "n t")
            + R(86, 26, 28, 14, "c", 2) + P("M88 26 L88 18 C88 8 112 8 112 18 L112 26 Z", "e")
            + P("M88 140 L112 140 L100 178 Z", "a") + P("M95.3 163 L104.7 163 L100 178 Z", "d"))
    return (f'<g transform="rotate(40 100 100)">{body}</g>'
            + P("M24 182 C44 170 60 190 80 178 C96 168 108 186 124 178", "n t"))


def onigiri():
    rice = ("M100 30 C112 30 120 40 128 54 L168 132 C180 156 168 172 146 172 L54 172 "
            "C32 172 20 156 32 132 L72 54 C80 40 88 30 100 30 Z")
    grains = "".join(E(x, y, 4, 2.4, "a", r) for x, y, r in [(92, 62, 20), (110, 74, -30), (80, 92, 10), (122, 100, 40),
                                                              (100, 104, -10), (62, 126, 30), (140, 128, -20)])
    return (E(100, 182, 84, 10, "c") + P(rice, "a") + grains + R(70, 120, 60, 56, "d", 4)
            + L(80, 132, 80, 168, "n t") + L(120, 132, 120, 168, "n t"))


def sakura():
    petal = "M0 0 C-34 -18 -36 -50 -14 -66 L0 -56 L14 -66 C36 -50 34 -18 0 0 Z"
    petals = "".join(f'<g transform="translate(100 104) rotate({72 * k})">{P(petal, "e")}'
                     f'{P("M0 -10 L0 -30", "n t")}</g>' for k in range(5))
    stamens = "".join(L(100, 104, *_rot(100, 82, 100, 104, 36 * k), "n t") for k in range(10))
    dots = "".join(C(*_rot(100, 82, 100, 104, 36 * k), 3, "d") for k in range(10))
    return (leaf(150, 170, -40, 40, "c") + petals + stamens + C(100, 104, 8, "d") + dots
            + P("M150 170 C160 180 172 186 186 188", "n"))


def soroban():
    out = R(18, 46, 164, 112, "e", 8) + R(30, 58, 140, 88, "a", 2)
    rods = "".join(L(42 + 19.3 * k, 58, 42 + 19.3 * k, 146, "n t") for k in range(7))
    beads = ""
    for k in range(7):
        x = 42 + 19.3 * k
        beads += E(x, 69, 8.5, 6, "d")
        up = k % 3 == 0
        for j in range(4):
            beads += E(x, (100 if up else 106) + 11.5 * j, 8.5, 5.5, "b")
    return out + rods + R(30, 80, 140, 9, "e") + beads + ground(176)


def negi():
    leaves = (P("M90 118 C84 84 70 52 52 22 C62 18 70 22 76 30 C90 58 98 88 100 116 Z", "c")
              + P("M110 118 C116 84 130 52 150 26 C140 20 132 24 126 32 C112 60 102 88 100 116 Z", "c")
              + P("M93 116 C93 80 95 48 100 14 C105 48 107 80 107 116 Z", "c"))
    return (leaves + R(86, 112, 28, 66, "a", 12) + L(100, 124, 100, 170, "n t")
            + P("M92 178 l-12 12 M98 178 l-4 14 M104 178 l4 14 M108 178 l12 12", "n t"))


def saw():
    teeth = "M24 70 L140 82 L140 106"
    x = 140
    while x > 30:
        teeth += f" L{x - 5} 114 L{x - 10} 106"
        x -= 10
    teeth += " L24 104 Z"
    body = (P(teeth, "a") + R(140, 84, 50, 20, "b", 9) + L(152, 84, 152, 104, "n t") + L(178, 84, 178, 104, "n t")
            + C(40, 84, 4, "n t"))
    return f'<g transform="rotate(-18 100 100) translate(-6 10)">{body}</g>' + ground(176)


def hechima():
    gourd = ("M94 46 C108 46 112 64 112 84 L116 156 C118 184 84 184 86 156 L88 84 C88 64 84 46 94 46 Z")
    return (L(14, 22, 186, 22, "n") + P("M96 22 C96 30 96 38 96 46", "n")
            + leaf(96, 26, 30, 46, "c") + leaf(60, 22, 140, 40, "c") + leaf(150, 22, 50, 36, "c")
            + P("M128 22 c12 8 4 22 -6 14 c-6 -6 2 -12 6 -6", "n t")
            + P(gourd, "c") + P("M98 56 C96 90 98 140 100 176 M92 70 C90 100 92 140 94 168 M106 70 C108 100 108 140 108 168", "n t")
            + C(100, 178, 4, "d"))


def mugi():
    grains = ""
    for k in range(6):
        y = 44 + 14 * k
        grains += (L(88, y - 10, 70, y - 44, "n t") + L(112, y - 10, 130, y - 44, "n t")
                   + E(88, y, 8, 13, "d", -28) + E(112, y, 8, 13, "d", 28))
    return (P("M100 190 C100 160 100 130 100 110", "n")
            + P("M100 150 C120 128 144 124 168 112 C150 136 126 148 100 162 Z", "c")
            + grains + E(100, 32, 7, 13, "d"))


def momo():
    fruit = "M100 62 C132 34 178 54 172 106 C166 152 130 178 100 178 C70 178 34 152 28 106 C22 54 68 34 100 62 Z"
    return (P("M100 62 L104 40", "n") + leaf(104, 44, -150, 46, "c") + leaf(104, 44, -30, 50, "c")
            + P(fruit, "e") + P("M100 62 C88 96 90 140 100 178", "n t") + P("M56 92 C50 104 50 118 56 130", "n t"))


def yuki():
    arms = ""
    for k in range(6):
        g = f'<g transform="rotate({60 * k} 100 100)">'
        arms += (g + R(96, 30, 8, 70, "b", 4) + C(100, 28, 7, "a")
                 + P("M100 62 L84 46 M100 62 L116 46 M100 44 L90 34 M100 44 L110 34", "n") + "</g>")
    small = "".join(f'<g transform="translate({x} {y})">' + P("M-8 0 H8 M-4 -7 L4 7 M4 -7 L-4 7", "n t") + "</g>"
                    for x, y in [(30, 34), (170, 40), (32, 172), (172, 170)])
    return arms + C(100, 100, 14, "a") + C(100, 100, 5, "c") + small


def peanut():
    shell = ("M100 30 C122 30 134 46 134 64 C134 80 124 90 124 100 C124 108 138 116 138 136 C138 160 120 176 100 176 "
             "C80 176 62 160 62 136 C62 116 76 108 76 100 C76 90 66 80 66 64 C66 46 78 30 100 30 Z")
    net = "".join(L(x, y, x + 10, y + 10, "n t") + L(x + 10, y, x, y + 10, "n t")
                  for x, y in [(84, 48), (104, 56), (88, 74), (84, 124), (104, 132), (92, 150)])
    return (f'<g transform="rotate(-28 100 104) translate(-14 -6)">{P(shell, "b")}{net}</g>'
            + E(140, 172, 14, 10, "e", -10) + E(168, 166, 14, 10, "e", 20) + L(140, 166, 140, 178, "n t")
            + L(168, 160, 166, 172, "n t") + ground(186))


def renkon():
    holes = "".join(C(*_rot(100, 58, 100, 92, 360 / 7 * k), 12, "e") for k in range(7))
    root = P("M30 150 C30 132 60 126 100 130 L170 136 C190 138 190 176 170 178 L100 184 C60 188 30 170 30 150 Z", "b")
    return (root + L(70, 132, 70, 184, "n t") + L(140, 136, 140, 180, "n t")
            + C(100, 92, 70, "b") + C(100, 92, 60, "a") + holes + C(100, 92, 12, "e"))


def candle():
    glow = P("M70 34 l-12 -6 M130 34 l12 -6 M64 60 l-14 0 M136 60 l14 0", "n t")
    return (E(100, 178, 56, 10, "c") + R(66, 160, 68, 18, "c", 6) + R(78, 74, 44, 92, "a", 4)
            + P("M78 80 C78 90 86 92 86 100 C86 108 94 108 94 98 C94 90 100 90 104 96 C108 104 114 104 114 94 "
                "C114 88 122 88 122 80 Z", "b")
            + L(100, 74, 100, 62) + P("M100 16 C118 38 118 56 100 64 C82 56 82 38 100 16 Z", "d")
            + P("M100 36 C108 46 108 56 100 60 C92 56 92 46 100 36 Z", "e") + glow)


def wataame():
    n, r, cx, cy = 11, 52, 100, 74
    pts = [(cx + r * math.cos(2 * math.pi * k / n - math.pi / 2), cy + r * math.sin(2 * math.pi * k / n - math.pi / 2))
           for k in range(n)]
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(
        f"A17 17 0 0 1 {pts[(k + 1) % n][0]:.1f} {pts[(k + 1) % n][1]:.1f}" for k in range(n)) + " Z"
    swirl = P("M74 70 C80 52 112 50 120 66 C126 80 108 92 94 84 C86 78 92 66 102 70", "n t")
    return R(95, 110, 10, 80, "b", 4) + P(d, "e") + swirl + P("M60 100 C70 112 90 118 104 116", "n t")


def mikan():
    dimples = "".join(C(x, y, 1.6, "n") for x, y in [(70, 100), (84, 128), (122, 96), (132, 130), (100, 150), (60, 132)])
    return (E(100, 116, 74, 62, "d") + C(100, 56, 7, "c") + leaf(104, 54, -25, 46, "c") + dimples
            + P("M50 96 C46 108 46 120 52 132", "n t") + ground(186))


PICS = {"ja_pencil": pencil, "ja_onigiri": onigiri, "ja_sakura": sakura, "ja_soroban": soroban, "ja_negi": negi,
        "ja_saw": saw, "ja_hechima": hechima, "ja_mugi": mugi, "ja_momo": momo, "ja_yuki": yuki,
        "ja_peanut": peanut, "ja_renkon": renkon, "ja_candle": candle, "ja_wataame": wataame, "ja_mikan": mikan}
