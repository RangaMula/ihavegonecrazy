# -*- coding: utf-8 -*-
"""Pictures for Book 78 (Setswana, tn_), Book 79 (Luganda, lg_) and Book 87 (Haitian Creole, ht_).
Objects, plants and nature only: no people, no animals, no faces. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, poly, star, leaf, cloud, ground


# ---------------------------------------------------------------- shared shapes
def _stones():
    """A pile of smooth stones with a few grass tufts."""
    tuft = lambda x: P(f"M{x} 182 l-6 -16 M{x} 182 l0 -20 M{x} 182 l6 -16", "n t")
    return (E(66, 150, 48, 30, "b") + P("M40 146 C52 138 64 138 74 144", "n t")
            + E(140, 154, 42, 27, "c") + P("M128 140 C140 136 152 140 160 148", "n t")
            + E(104, 110, 40, 28, "a", -10) + P("M86 100 C96 94 110 94 120 100", "n t")
            + E(158, 116, 20, 14, "b") + E(30, 176, 10, 6, "c") + E(110, 176, 9, 5, "a") + E(178, 178, 8, 5, "b")
            + tuft(18) + tuft(186) + ground(184))


def _glass():
    """A drinking glass of water with a straw."""
    lx = lambda y: 58 + 12 * (y - 40) / 136   # left wall x at height y
    rx = lambda y: 142 - 12 * (y - 40) / 136
    bub = "".join(C(x, y, r, "a") for x, y, r in [(86, 140, 4), (110, 120, 3), (118, 150, 5), (96, 108, 3)])
    return (P("M58 40 L142 40 L130 176 L70 176 Z", "a")
            + P(f"M{lx(84):.1f} 84 L{rx(84):.1f} 84 L130 176 L70 176 Z", "c") + bub
            + P(f"M{lx(84):.1f} 84 q19 -7 38 0 t38 0", "n t")
            + E(100, 40, 42, 8, "a") + P("M110 44 L130 6 L139 10 L120 47 Z", "d")
            + P("M70 56 L76 150", "n t") + ground(186))


def _tuber(cx, cy, length, width, rot, cls="b"):
    """One long root tuber (cassava, yam) with ring marks."""
    h = length / 2
    body = (f'<g transform="rotate({rot} {cx} {cy})">'
            + P(f"M{cx-h} {cy} C{cx-h+10} {cy-width} {cx+h-30} {cy-width*1.05} {cx+h} {cy-2} "
                f"C{cx+h-24} {cy+width*1.05} {cx-h+14} {cy+width} {cx-h} {cy} Z", cls)
            + "".join(P(f"M{cx-h+k} {cy-width*0.62} q4 {width*0.62} 0 {width*1.24}", "n t")
                      for k in (int(length * 0.3), int(length * 0.5), int(length * 0.7)))
            + "</g>")
    return body


# ---------------------------------------------------------------- Setswana
def shirt():
    """hempe: a shirt with buttons and a pocket."""
    return (P("M70 40 L52 46 L18 76 L40 106 L58 92 L58 176 L142 176 L142 92 L160 106 L182 76 L148 46 L130 40 "
              "C122 54 78 54 70 40 Z", "b")
            + P("M70 40 L100 60 L86 72 Z", "a") + P("M130 40 L100 60 L114 72 Z", "a")
            + L(100, 60, 100, 176, "n t") + "".join(C(106, y, 4, "a") for y in (86, 112, 138, 162))
            + R(116, 92, 20, 20, "c", 3) + P("M40 106 L58 92 M160 106 L142 92", "n t")
            + P("M24 84 L46 102 M176 84 L154 102", "n t"))


def fire():
    """molelo: a cooking fire on two logs inside a ring of stones."""
    logs = ('<g transform="rotate(-14 100 160)">' + R(36, 150, 128, 20, "b", 10) + C(160, 160, 7, "a") + "</g>"
            + '<g transform="rotate(14 100 160)">' + R(36, 150, 128, 20, "b", 10) + C(40, 160, 7, "a") + "</g>")
    flame = (P("M100 26 C122 58 152 80 142 120 C136 146 120 158 100 158 C80 158 64 146 58 120 C52 96 70 84 78 62 "
               "C86 80 90 86 96 92 C96 70 90 50 100 26 Z", "e")
             + P("M100 88 C114 104 124 118 118 136 C112 150 88 150 82 136 C78 122 90 110 100 88 Z", "d"))
    stones = "".join(E(x, 178, 14, 8, "c") for x in (28, 60, 100, 140, 172))
    return flame + logs + stones + P("M150 40 l6 -6 M40 50 l-6 -6 M160 70 l8 0", "n t")


def radio():
    """seyalemoya: a radio with an aerial."""
    ticks = "".join(L(120 + 8 * k, 90, 120 + 8 * k, 96, "n t") for k in range(5))
    return (P("M56 70 L56 54 C56 46 62 42 70 42 L130 42 C138 42 144 46 144 54 L144 70", "n")
            + L(150, 70, 176, 16) + C(176, 14, 5, "e")
            + P("M186 26 q7 -10 0 -20 M168 6 q-7 -4 -14 0", "n t")
            + R(28, 70, 144, 98, "b", 14)
            + C(72, 120, 32, "a") + C(72, 120, 20, "c") + C(72, 120, 6, "a")
            + R(112, 84, 46, 22, "a", 4) + ticks + L(138, 86, 138, 104, "n")
            + C(124, 140, 10, "d") + C(150, 140, 10, "d")
            + R(44, 168, 22, 10, "c", 3) + R(134, 168, 22, 10, "c", 3) + ground(180))


def grass():
    """bojang: a clump of grass with two small flowers."""
    def blade(x, lean, hgt, cls):
        return P(f"M{x-6} 180 C{x-4} {180-hgt*0.5} {x+lean*0.6} {180-hgt*0.8} {x+lean} {180-hgt} "
                 f"C{x+lean*0.4} {180-hgt*0.75} {x+6} {180-hgt*0.45} {x+6} 180 Z", cls)
    blades = "".join(blade(x, l, h, c) for x, l, h, c in
                     [(40, -24, 100, "c"), (62, -8, 130, "b"), (84, 10, 150, "c"), (104, -14, 140, "b"),
                      (124, 18, 128, "c"), (146, 26, 104, "b"), (164, 10, 80, "c"), (24, -10, 70, "b")])
    flower = lambda x, y: "".join(C(x + 7 * math.cos(math.radians(a)), y + 7 * math.sin(math.radians(a)), 5, "e")
                                  for a in range(0, 360, 72)) + C(x, y, 4, "d")
    return (P("M76 180 L70 70 M134 180 L142 88", "n") + blades + flower(70, 64) + flower(142, 82)
            + C(160, 36, 14, "d") + ground(182))


def road():
    """tsela: a road running to the hills."""
    dashes = "".join(poly([(100 - w, y), (100 + w, y), (100 + w * 1.4, y + 12), (100 - w * 1.4, y + 12)], "d")
                     for y, w in [(108, 1.5), (126, 2.5), (148, 3.5), (172, 5)])
    tree = (R(158, 110, 8, 30, "b", 2) + C(162, 100, 18, "c"))
    return (C(150, 46, 18, "d") + cloud(24, 64, 0.6)
            + P("M14 100 C46 70 80 74 112 100 Z", "b") + P("M90 100 C120 78 160 72 186 92 L186 100 Z", "c")
            + R(14, 100, 172, 86, "a")
            + P("M94 100 L106 100 L172 186 L28 186 Z", "c") + dashes
            + tree + R(30, 120, 6, 22, "b", 2) + C(33, 112, 13, "c") + L(14, 100, 186, 100, "n"))


# ---------------------------------------------------------------- Luganda
def jackfruit():
    """ffene: a big bumpy jackfruit with a leaf."""
    cx, cy, rx, ry = 100, 114, 60, 70
    bumps = []
    for y in range(int(cy - ry + 14), int(cy + ry - 8), 14):
        off = 7 if (y // 14) % 2 else 0
        for x in range(int(cx - rx + 10) + off, int(cx + rx - 6), 14):
            if ((x - cx) / (rx - 8)) ** 2 + ((y - cy) / (ry - 8)) ** 2 < 1:
                bumps.append(f"M{x-4} {y+2} l4 -4 l4 4")
    return (E(cx, cy, rx, ry, "c", -8) + P(" ".join(bumps), "n t")
            + R(95, 28, 10, 22, "b", 3) + leaf(104, 34, -20, 46, "b") + leaf(96, 36, -160, 36, "b") + ground(186))


def drum():
    """ŋŋoma: a drum with a laced skin top."""
    lace = "M" + " L".join(f"{48 + 13 * k} {58 if k % 2 == 0 else 104}" for k in range(9))
    return (P("M38 54 L60 166 C74 178 126 178 140 166 L162 54 Z", "b")
            + R(48, 102, 104, 14, "d", 5) + P(lace, "n")
            + E(100, 54, 62, 18, "a") + E(100, 54, 48, 12, "n t")
            + P("M70 130 L74 160 M100 132 L100 166 M130 130 L126 160", "n t")
            + ground(184))


def papaya():
    """ppaapaali: a whole papaya and a half showing its seeds."""
    seeds = "".join(C(124 + dx, 128 + dy, 4, "b") for dx, dy in
                    [(-8, -18), (4, -22), (10, -10), (-12, -4), (0, -6), (8, 4), (-6, 10), (4, 18), (-10, 22), (12, 16)])
    return (P("M60 26 C82 22 94 50 98 82 C102 118 96 150 70 160 C44 166 28 140 32 106 C36 70 38 30 60 26 Z", "c")
            + R(56, 14, 8, 14, "b", 3) + P("M48 60 C44 90 44 120 52 146", "n t")
            + E(126, 128, 48, 58, "d", 18) + E(124, 128, 24, 36, "a", 18) + seeds + ground(188))


def bottle():
    """ccupa: a bottle of water."""
    return (P("M84 26 L116 26 L116 56 C116 68 146 78 146 106 L146 168 C146 178 140 182 130 182 L70 182 "
              "C60 182 54 178 54 168 L54 106 C54 78 84 68 84 56 Z", "a")
            + P("M55 106 L145 106 L146 168 C146 178 140 182 130 182 L70 182 C60 182 54 178 54 168 Z", "c")
            + R(54, 124, 92, 34, "d") + star(100, 141, 11, 5, "e")
            + R(80, 12, 40, 18, "b", 4) + P("M66 112 L66 170", "n t")
            + C(122, 112, 3, "a") + C(110, 170, 3, "a"))


def cassava():
    """muwogo: cassava roots with a cassava leaf."""
    palm = "".join(leaf(150, 50, a, 34, "c") for a in (-150, -115, -80, -45, -10))
    return (_tuber(86, 132, 140, 16, -12, "b") + _tuber(98, 160, 132, 15, 6, "b") + _tuber(80, 104, 110, 13, -30, "a")
            + P("M150 50 L126 104", "n") + palm + ground(186))


# ---------------------------------------------------------------- Haitian Creole
def stairs():
    """eskalye: a staircase with a rail and a plant pot."""
    pts = [(40, 180), (40, 152), (68, 152), (68, 124), (96, 124), (96, 96), (124, 96), (124, 68), (152, 68),
           (152, 40), (182, 40), (182, 180)]
    posts = "".join(L(x + 6, y, x + 6, y - 34, "n") for x, y in [(40, 152), (68, 124), (96, 96), (124, 68), (152, 40)])
    return (poly(pts, "b") + P("M40 166 L182 166", "n t") + posts + P("M46 118 L158 6", "n")
            + P("M12 150 L32 150 L28 180 L16 180 Z", "d") + leaf(22, 150, -120, 26) + leaf(22, 150, -60, 26)
            + leaf(22, 150, -90, 30) + ground(182))


def cake():
    """gato: a two-layer cake on a stand."""
    drips = P("M64 72 L136 72 L136 84 q-6 10 -12 0 q-6 12 -14 0 q-6 10 -12 0 q-6 12 -14 0 q-6 10 -12 0 q-6 12 -12 0 Z", "d")
    dots = "".join(C(x, 138, 4, "e") for x in (58, 80, 100, 120, 142))
    return (R(40, 108, 120, 54, "b", 6) + R(40, 108, 120, 12, "d", 6) + dots
            + R(64, 70, 72, 40, "a", 6) + drips
            + C(100, 60, 9, "e") + P("M100 51 C102 44 106 40 112 38", "n")
            + E(100, 166, 76, 9, "c") + R(92, 170, 16, 10, "c") + E(100, 182, 34, 5, "c"))


def hammock():
    """hamak: a hammock between two palm trees."""
    def palm(x, lean):
        trunk = P(f"M{x-6} 182 C{x-4} 140 {x+lean-6} 90 {x+lean-4} 52 L{x+lean+4} 52 C{x+lean+2} 90 {x+4} 140 {x+6} 182 Z", "b")
        fr = "".join(leaf(x + lean, 50, a, 40, "c") for a in (-170, -135, -100, -60, -20))
        return trunk + fr
    return (C(100, 36, 14, "d") + palm(30, 8) + palm(170, -8)
            + P("M40 96 L56 108 M160 96 L144 108", "n")
            + P("M56 108 C80 150 120 150 144 108 C120 134 80 134 56 108 Z", "d")
            + P("M70 126 C90 138 110 138 130 126", "n t") + P("M14 182 C60 176 140 176 186 182", "n"))


def pumpkin():
    """joumou: a pumpkin with its curly vine."""
    return (E(62, 126, 42, 50, "d") + E(138, 126, 42, 50, "d") + E(100, 124, 38, 56, "e")
            + P("M100 70 C96 100 96 150 100 178", "n t")
            + R(93, 46, 14, 26, "c", 4) + leaf(106, 54, -30, 40, "c")
            + P("M92 56 C76 46 70 30 84 26 C96 24 94 40 84 38", "n") + ground(184))


def bread():
    """pen: a round loaf and a long loaf."""
    slashes = "".join(P(f"M{x} {y} l14 -8", "n t") for x, y in [(56, 108), (84, 96), (112, 84), (140, 72)])
    return (E(104, 98, 84, 18, "c", -22) + slashes
            + P("M30 160 C28 116 64 92 100 92 C136 92 172 116 170 160 Z", "b")
            + E(100, 160, 70, 10, "b")
            + E(74, 124, 14, 5, "a", -30) + E(100, 114, 14, 5, "a", -30) + E(126, 124, 14, 5, "a", -30)
            + ground(176))


def cookies():
    """bonbon: three round cookies on a plate."""
    def ck(x, y):
        chips = "".join(C(x + dx, y + dy, 3.5, "e") for dx, dy in [(-14, -10), (10, -14), (14, 8), (-8, 14), (0, 0)])
        return C(x, y, 34, "b") + C(x, y, 27, "n t") + chips
    return E(100, 152, 86, 24, "c") + E(100, 148, 66, 14, "n t") + ck(62, 116) + ck(138, 116) + ck(100, 72)


def yam():
    """yanm: a big yam and a cut slice."""
    return (_tuber(90, 116, 160, 26, -14, "b") + E(150, 160, 26, 16, "a") + E(150, 160, 18, 10, "n t")
            + ground(186))


PICS = {
    "tn_shirt": shirt, "tn_glass": _glass, "tn_fire": fire, "tn_radio": radio, "tn_grass": grass, "tn_road": road,
    "lg_jackfruit": jackfruit, "lg_drum": drum, "lg_papaya": papaya, "lg_bottle": bottle, "lg_stones": _stones,
    "lg_cassava": cassava,
    "ht_stairs": stairs, "ht_cake": cake, "ht_hammock": hammock, "ht_pumpkin": pumpkin, "ht_glass": _glass,
    "ht_rock": _stones, "ht_bread": bread, "ht_cookies": cookies, "ht_yam": yam,
}
