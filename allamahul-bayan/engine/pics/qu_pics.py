# -*- coding: utf-8 -*-
"""Pictures for Books 82 (Quechua), 84 (Aymara) and 88 (Mapudungun). Objects, plants and nature only.
viewBox 0 0 200 200. Keys: qu_* (Quechua, some shared), ay_* (Aymara, some shared), arn_* (Mapudungun)."""
import math
from illos import P, C, E, R, L, poly, star, cloud, ground


def _snowpeaks():
    """Andes background: two peaks with snow caps (behind everything else)."""
    return (P("M14 104 L62 40 L96 84 L132 30 L186 104 Z", "b")
            + P("M62 40 L50 56 L58 54 L64 62 L70 52 L76 58 Z", "a")
            + P("M132 30 L118 48 L126 46 L132 56 L140 46 L148 52 Z", "a"))


# ---------------------------------------------------------------- Quechua (shared)
def bridge():
    """Chaka: a woven rope bridge between two rocky cliffs, a river below."""
    def hand(t):
        return (1 - t) ** 2 * 74 + 2 * t * (1 - t) * 108 + t * t * 74

    def deck(t):
        return (1 - t) ** 2 * 102 + 2 * t * (1 - t) * 138 + t * t * 102
    ties = "".join(L(54 + 92 * t, hand(t), 54 + 92 * t, deck(t), "n t") for t in [k / 10 for k in range(1, 10)])
    return (_snowpeaks()
            + P("M60 186 C80 170 120 178 140 170 L140 186 Z", "e")
            + P("M14 186 L14 96 L38 90 L56 104 L64 186 Z", "c") + P("M186 186 L186 94 L162 92 L144 106 L136 186 Z", "c")
            + P("M26 130 L40 126 M150 140 L170 136 M30 160 L46 156", "n t")
            + P("M54 100 Q100 140 146 100 L146 108 Q100 148 54 108 Z", "d")
            + P("M54 74 Q100 108 146 74", "n") + ties
            + R(48, 68, 8, 40, "e", 3) + R(144, 68, 8, 40, "e", 3))


def fire():
    """Nina / kütral: a small campfire inside a ring of stones."""
    return (P("M100 26 C122 58 152 80 148 120 C146 148 126 164 100 164 C74 164 54 148 52 120 "
              "C50 96 68 86 74 62 C84 78 90 82 92 92 C98 70 92 50 100 26 Z", "d")
            + P("M100 86 C114 102 128 114 124 134 C122 150 112 158 100 158 C88 158 78 150 76 136 C74 118 92 112 100 86 Z", "e")
            + '<g transform="rotate(-14 100 166)">' + R(36, 158, 128, 16, "b", 8) + C(44, 166, 5, "n") + "</g>"
            + '<g transform="rotate(14 100 166)">' + R(36, 158, 128, 16, "b", 8) + C(156, 166, 5, "n") + "</g>"
            + E(30, 178, 16, 9, "a") + E(170, 178, 16, 9, "a") + E(100, 182, 18, 7, "a")
            + C(64, 46, 3, "d") + C(138, 40, 3, "d") + C(150, 66, 2.5, "d") + ground(186))


def path():
    """Ñan: a mountain path winding up towards the snowy peaks."""
    return (C(172, 42, 12, "d") + _snowpeaks()
            + P("M14 100 C60 88 140 88 186 100 L186 186 L14 186 Z", "c")
            + P("M64 186 C76 160 124 152 112 132 C102 116 82 112 94 98 C100 92 110 90 108 86 L116 86 "
                "C120 94 108 100 104 104 C96 114 124 120 128 134 C136 158 110 170 134 186 Z", "d")
            + E(46, 150, 10, 6, "a") + E(150, 158, 12, 7, "a") + E(160, 120, 8, 5, "a") + E(40, 116, 7, 4, "a")
            + P("M28 176 l4 -10 l4 10 M164 178 l4 -10 l4 10 M60 128 l3 -8 l3 8", "n t"))


def lake():
    """Qucha / quta: a mountain lake with reeds on the shore."""
    reeds = "".join(L(x, 180, x + d, 128 + h, "n t") + E(x + d, 128 + h, 3.5, 9, "b", d * 2)
                    for x, d, h in [(24, -2, 4), (32, 2, -6), (40, 0, 8), (164, 2, 2), (172, -2, -8), (180, 0, 6)])
    return (_snowpeaks()
            + P("M14 104 L186 104 L186 186 L14 186 Z", "c")
            + E(100, 140, 82, 30, "e")
            + P("M50 132 C60 128 70 128 80 132 M110 146 C120 142 130 142 140 146 M76 152 C84 149 92 149 100 152", "n t")
            + reeds + ground(186))


def stones():
    """Rumi / kura: a little pile of round stones."""
    return (E(64, 160, 44, 24, "b") + E(140, 162, 40, 22, "d") + E(100, 124, 36, 26, "a")
            + E(70, 112, 22, 16, "e") + E(134, 116, 20, 14, "c") + E(102, 86, 18, 14, "b")
            + P("M54 152 C60 158 70 160 78 156 M128 156 l8 8 M92 120 C96 126 104 128 110 124", "n t")
            + P("M20 182 l4 -12 l4 12 M176 182 l4 -12 l4 12", "n t") + ground(184))


def wind():
    """Thaya: a cold wind blowing over the snowy mountains, with flying leaves."""
    return (_snowpeaks()
            + P("M14 150 C60 136 140 136 186 150 L186 186 L14 186 Z", "a")
            + cloud(24, 64, 0.7, "a")
            + P("M20 120 C60 110 110 126 140 112 C160 102 156 86 142 88 C132 90 134 102 144 102", "n")
            + P("M30 140 C70 130 120 144 160 132 C176 126 176 112 164 112", "n")
            + P("M56 96 C80 90 100 98 116 92", "n")
            + '<g transform="translate(150 150) rotate(-30)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>"
            + '<g transform="translate(100 160) rotate(20)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>"
            + '<g transform="translate(176 124) rotate(60)">' + P("M0 0 C5 -6 12 -6 16 0 C12 6 5 6 0 0 Z", "c") + "</g>")


# ---------------------------------------------------------------- Quechua
def khipu():
    """Khipu: the Andean knotted cords used to keep numbers."""
    out = [R(14, 36, 172, 12, "c", 6)]
    cls = ["b", "d", "e", "a", "b", "d", "e", "a"]
    lens = [120, 96, 132, 110, 128, 88, 116, 104]
    knots = [(70, 112), (64, 96, 120), (80, 140), (60, 100), (74, 92, 132), (66, 110), (84, 128), (70, 100)]
    for i in range(8):
        x = 30 + i * 20
        out.append(P(f"M{x-3} 48 L{x+3} 48 L{x+4} {48+lens[i]} L{x-4} {48+lens[i]} Z", cls[i]))
        for y in knots[i]:
            out.append(E(x, y, 6.5, 5, cls[i]))
        out.append(P(f"M{x-4} {48+lens[i]} l-2 8 M{x} {48+lens[i]} l0 9 M{x+4} {48+lens[i]} l2 8", "n t"))
    out.append(P("M14 42 C8 42 6 48 10 52 M14 42 C6 36 4 30 10 26", "n"))
    return "".join(out)


def stick():
    """K'aspi: a wooden walking stick and two small sticks."""
    rings = "".join(P(f"M93 {y} C98 {y+3} 102 {y+3} 107 {y}", "n t") for y in (50, 84, 120, 150))
    return ('<g transform="rotate(-10 100 110)">' + R(92, 22, 16, 160, "b", 8)
            + P("M106 70 L128 52 L132 56 L108 80 Z", "b") + rings + "</g>"
            + '<g transform="rotate(8 60 172)">' + R(14, 166, 70, 10, "d", 5) + "</g>"
            + '<g transform="rotate(-6 150 174)">' + R(116, 168, 70, 10, "c", 5) + "</g>"
            + '<g transform="translate(128 52) rotate(-40)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>"
            + ground(186))


# ---------------------------------------------------------------- Aymara
def bread():
    """T'ant'a: round loaves of bread on a plate."""
    def loaf(cx, cy, rx, ry, cls):
        return (P(f"M{cx-rx} {cy} C{cx-rx} {cy-ry*1.3} {cx+rx} {cy-ry*1.3} {cx+rx} {cy} Z", cls)
                + P(f"M{cx-rx*0.45} {cy-ry*0.55} l{rx*0.25} {-ry*0.25} M{cx-rx*0.05} {cy-ry*0.7} l{rx*0.25} {-ry*0.2} "
                    f"M{cx+rx*0.35} {cy-ry*0.55} l{rx*0.2} {-ry*0.2}", "n t"))
    return (E(100, 158, 88, 20, "a") + E(100, 154, 70, 13, "e")
            + loaf(50, 154, 30, 34, "d") + loaf(150, 154, 30, 34, "d") + loaf(100, 148, 36, 50, "b") + ground(186))


def snow():
    """Khunu: snow falling on a snowy mountain."""
    flakes = "".join(star(x, y, r, r * 0.35, "a", 6) for x, y, r in [(36, 36, 10), (100, 22, 8), (168, 44, 11), (60, 76, 7), (150, 88, 7)])
    dots = "".join(C(x, y, 3, "a") for x, y in [(20, 70), (82, 50), (128, 60), (184, 80), (40, 104), (116, 98)])
    return (P("M10 176 L84 70 L122 120 L144 96 L190 176 Z", "b")
            + P("M84 70 L64 100 L76 96 L86 108 L96 94 L106 100 Z", "a")
            + P("M144 96 L132 112 L142 110 L148 118 L156 108 Z", "a")
            + P("M10 168 C40 150 70 160 100 166 C130 156 160 150 190 166 L190 186 L10 186 Z", "a")
            + flakes + dots)


def logs():
    """Llant'a: a stack of firewood logs, seen from the front."""
    out = []
    for i, (x, y) in enumerate([(52, 160), (100, 160), (148, 160), (76, 122), (124, 122), (100, 84)]):
        cls = "bdbdbd"[i]
        out.append(C(x, y, 22, cls) + C(x, y, 13, "n t") + C(x, y, 5, "n t"))
    return (R(24, 178, 152, 8, "c", 3) + "".join(out)
            + '<g transform="translate(142 70) rotate(-30)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>")


def leaf_big():
    """Laphi / tapül: a big leaf on a twig, and a small one."""
    veins = "".join(P(f"M{100 + 32*t:.1f} {120 - 94*t:.1f} l-14 -2 M{100 + 32*t:.1f} {120 - 94*t:.1f} l13 -8", "n t")
                    for t in (0.2, 0.38, 0.56, 0.74))
    return (P("M60 170 C76 152 90 136 100 120", "n")
            + P("M100 120 C70 96 72 50 132 26 C150 70 146 118 100 120 Z", "c")
            + P("M100 120 C110 92 120 60 132 26", "n t") + veins
            + P("M82 146 C60 150 38 140 30 118 C54 114 74 124 82 146 Z", "e")
            + P("M82 146 C66 136 48 126 30 118", "n t") + ground(184))


def river():
    """Jawira / lewfü: a river winding down from the mountains."""
    return (_snowpeaks()
            + P("M14 104 C60 92 140 92 186 104 L186 186 L14 186 Z", "c")
            + P("M90 100 L104 100 C110 116 74 124 82 140 C90 156 140 160 136 186 L50 186 "
                "C62 166 40 152 50 134 C60 116 92 114 90 100 Z", "e")
            + P("M66 150 C74 146 82 146 90 150 M88 172 C96 168 104 168 112 172 M74 128 C80 125 86 125 92 128", "n t")
            + E(150, 132, 12, 7, "a") + E(30, 160, 10, 6, "a") + E(162, 170, 9, 5, "a")
            + P("M24 124 l4 -10 l4 10 M166 150 l4 -10 l4 10", "n t"))


def field():
    """Yapu: terraced fields on an Andean hillside, with young plants."""
    out = [C(160, 40, 16, "d")]
    for i, (y, x0) in enumerate([(70, 70), (96, 50), (122, 32), (148, 18)]):
        cls = "cdce"[i]
        out.append(P(f"M{x0} {y} L186 {y} L186 {y+26} L{x0-16} {y+26} Z", cls))
        out.append(R(x0 - 16, y + 20, 186 - x0 + 16, 6, "b"))
        out += [P(f"M{x} {y+18} l-4 -9 M{x} {y+18} l4 -9 M{x} {y+18} l0 -11", "n t") for x in range(x0 + 10, 182, 18)]
    out.append(P("M14 174 L186 174 L186 186 L14 186 Z", "b"))
    return "".join(out)


def count(n=3):
    """n little flowers in rows of three (for number words)."""
    out = []
    rows = (n + 2) // 3
    for i in range(n):
        r, c = divmod(i, 3)
        x = 44 + c * 56
        y = 100 + (r - (rows - 1) / 2) * 56
        petals = "".join(C(x + 13 * math.cos(math.radians(a)), y + 13 * math.sin(math.radians(a)), 9.5, "abe"[r % 3])
                         for a in range(-90, 270, 72))
        out.append(petals + C(x, y, 8, "d"))
    return "".join(out)


def bundle():
    """Q'ipi: a bundle wrapped in a striped woven cloth, tied at the top."""
    cx, cy, rx, ry = 100, 124, 74, 54

    def band(y1, y2, cls):
        pts = []
        for k in range(9):
            y = y1 + (y2 - y1) * k / 8
            pts.append((cx - rx * math.sqrt(max(0, 1 - ((y - cy) / ry) ** 2)), y))
        for k in range(9):
            y = y2 - (y2 - y1) * k / 8
            pts.append((cx + rx * math.sqrt(max(0, 1 - ((y - cy) / ry) ** 2)), y))
        return poly(pts, cls)
    return (E(cx, cy, rx, ry, "b") + band(96, 108, "d") + band(118, 124, "e") + band(134, 146, "d") + band(156, 162, "e")
            + P("M84 74 C70 60 64 42 76 36 C88 44 92 60 96 72 Z", "b") + P("M116 74 C130 60 136 42 124 36 C112 44 108 60 104 72 Z", "b")
            + E(100, 74, 14, 10, "c") + ground(184))


def tick():
    """A big round badge with a tick: “yes!”."""
    return (C(100, 100, 74, "d") + C(100, 100, 58, "a")
            + poly([(62, 100), (74, 88), (92, 106), (132, 64), (144, 76), (92, 128)], "c")
            + star(28, 30, 10, 4.5, "e") + star(172, 168, 10, 4.5, "e") + star(176, 34, 7, 3.2, "e"))


def calendar():
    """A wall calendar page with today's sun on it."""
    grid = "".join(R(42 + c * 24, 118 + r * 18, 20, 14, "a", 2) for r in range(3) for c in range(5))
    return (R(30, 40, 140, 146, "a", 8) + R(30, 40, 140, 30, "b", 8)
            + R(52, 30, 10, 22, "e", 5) + R(138, 30, 10, 22, "e", 5)
            + C(100, 92, 13, "d")
            + "".join(L(100 + 18 * math.cos(math.radians(a)), 92 + 18 * math.sin(math.radians(a)),
                        100 + 24 * math.cos(math.radians(a)), 92 + 24 * math.sin(math.radians(a))) for a in range(0, 360, 45))
            + grid + C(100, 143, 10, "n"))


# ---------------------------------------------------------------- Mapudungun
def pewen():
    """Pewen: the monkey-puzzle tree (araucaria) of the southern Andes, with its umbrella crown."""
    def arm(y, w, s):
        tip = 100 + s * w
        return P(f"M100 {y-4} Q{100 + s*w*0.6} {y-2} {tip} {y-16} L{tip + s*4} {y-10} Q{100 + s*w*0.6} {y+8} 100 {y+6} Z", "c")
    arms = "".join(arm(y, w, s) for y, w in [(40, 34), (56, 52), (72, 66), (88, 74)] for s in (-1, 1))
    cones = "".join(C(x, y, 6, "d") for x, y in [(70, 52), (134, 54), (40, 76), (162, 74)])
    return (P("M94 186 L96 40 L104 40 L106 186 Z", "b") + P("M98 120 l4 6 M98 150 l4 6 M98 90 l4 6", "n t")
            + arms + P("M96 34 C96 24 104 24 104 34 Z", "c") + cones
            + P("M30 186 C40 172 52 172 60 186 M140 186 C150 172 162 172 170 186", "n t") + ground(186))


def waterfall():
    """Trayenko: a waterfall tumbling from the rocks into a pool."""
    return (P("M14 186 L14 40 L64 34 L76 60 L70 186 Z", "b") + P("M186 186 L186 44 L136 36 L124 62 L130 186 Z", "b")
            + P("M76 40 L124 40 C126 90 130 130 134 160 L66 160 C70 130 74 90 76 40 Z", "e")
            + P("M88 50 C88 90 86 120 84 150 M100 50 L100 152 M112 50 C112 90 114 120 116 150", "n t")
            + E(100, 168, 74, 16, "e") + C(78, 158, 8, "a") + C(100, 162, 9, "a") + C(122, 158, 8, "a")
            + P("M40 168 C50 164 58 164 66 168 M136 170 C144 166 152 166 160 170", "n t")
            + '<g transform="translate(26 40) rotate(-60)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>"
            + '<g transform="translate(176 46) rotate(-120)">' + P("M0 0 C6 -8 16 -8 22 0 C16 8 6 8 0 0 Z", "c") + "</g>")


def lightning():
    """Llüfke: a lightning flash from a storm cloud."""
    drops = "".join(P(f"M{x} {y} q-5 9 0 12 q5 -3 0 -12", "c") for x, y in [(40, 120), (60, 144), (150, 126), (166, 150), (44, 166)])
    return (P("M22 96 h156 a20 20 0 0 0 -10 -38 a30 30 0 0 0 -46 -24 a36 36 0 0 0 -62 8 a24 24 0 0 0 -38 54 z", "a")
            + poly([(104, 92), (80, 140), (100, 140), (84, 186), (128, 128), (106, 128), (124, 92)], "d") + drops)


def nalka():
    """Nalka: the giant-leaved nalca plant (Gunnera) of southern Chile."""
    def leafy(cx, cy, r, cls):
        pts = []
        for k in range(0, 25):
            a = math.radians(-180 + k * 7.5)
            rr = r * (1 - 0.1 * (k % 2))
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a) * 0.8))
        veins = "".join(L(cx, cy, cx + r * 0.85 * math.cos(math.radians(a)), cy + r * 0.85 * 0.8 * math.sin(math.radians(a)), "n t")
                        for a in range(-165, -10, 30))
        return poly(pts + [(cx + r, cy + 4), (cx - r, cy + 4)], cls) + veins
    prickles = "".join(L(x, y, x + 5, y - 3, "n t") for x, y in [(70, 140), (72, 160), (124, 130), (126, 152)])
    return (P("M64 186 C64 160 66 130 72 108 L80 110 C74 132 74 160 76 186 Z", "b")
            + P("M124 186 C126 150 124 116 120 96 L128 94 C134 116 136 150 134 186 Z", "b") + prickles
            + leafy(66, 104, 52, "c") + leafy(130, 90, 54, "c") + ground(186))


def pinenuts():
    """Ngülliw: pine nuts of the pewen tree in a little basket."""
    def nut(x, y, rot, cls="d"):
        return (f'<g transform="translate({x} {y}) rotate({rot})">'
                + P("M-18 0 C-14 -9 8 -9 18 0 C8 9 -14 9 -18 0 Z", cls) + L(-10, 0, 10, 0, "n t") + "</g>")
    nuts = "".join(nut(x, y, r) for x, y, r in [(62, 96, -20), (92, 88, 10), (122, 94, -10), (146, 102, 25),
                                                (76, 110, 30), (110, 108, -25), (136, 116, 5)])
    weave = "".join(L(x, 112, x + (x - 100) * 0.12, 170, "n t") for x in range(50, 160, 16))
    return (nuts + P("M34 110 L166 110 L150 172 L50 172 Z", "b") + weave
            + P("M40 132 L160 132 M45 152 L155 152", "n t") + R(30, 104, 140, 12, "e", 6)
            + nut(40, 182, -8, "d") + nut(170, 182, 12, "d") + ground(190))


PICS = {
    "qu_bridge": bridge, "qu_fire": fire, "qu_path": path, "qu_lake": lake, "qu_stones": stones, "qu_wind": wind,
    "qu_khipu": khipu, "qu_stick": stick,
    "ay_bread": bread, "ay_snow": snow, "ay_logs": logs, "ay_leaf": leaf_big, "ay_river": river, "ay_field": field,
    "ay_count": count, "ay_bundle": bundle, "ay_tick": tick, "ay_calendar": calendar,
    "arn_pewen": pewen, "arn_waterfall": waterfall, "arn_lightning": lightning, "arn_nalka": nalka, "arn_pinenuts": pinenuts,
}
