# -*- coding: utf-8 -*-
"""Pictures for Book 47 (Thai). Objects, plants and nature only - no people, no animals, no faces,
no religious imagery. viewBox 0 0 200 200; every closed shape has a colour class a-e."""
import math
from illos import P, C, E, R, L, poly, star, star_pts, cloud, leaf, ground


def bottle():
    return (R(86, 30, 28, 46, "b", 4) + R(82, 18, 36, 16, "c", 5)
            + P("M86 70 C62 80 52 100 52 122 L52 170 Q52 184 66 184 L134 184 Q148 184 148 170 L148 122 "
                "C148 100 138 80 114 70 Z", "b")
            + P("M56 104 C80 112 120 96 144 104", "n t")
            + R(64, 118, 72, 42, "a", 6) + P("M76 132 L124 132 M82 144 L118 144", "n t"))


def hammer():
    return ('<g transform="rotate(-30 100 100)">' + R(92, 64, 16, 124, "b", 6)
            + P("M46 38 L150 38 L150 72 L62 72 C50 72 42 58 46 38 Z", "c") + R(150, 42, 14, 26, "d", 3)
            + L(98, 150, 102, 150, "n t") + L(98, 160, 102, 160, "n t") + "</g>" + ground(188))


def bell():
    return (R(92, 26, 16, 44, "b", 7) + C(100, 24, 11, "b")
            + C(100, 170, 10, "c")
            + P("M58 154 C58 112 68 72 100 68 C132 72 142 112 142 154 Z", "d")
            + R(44, 150, 112, 14, "c", 7)
            + P("M74 120 C76 102 82 90 92 84", "n t")
            + P("M34 96 C26 108 26 124 34 136", "n") + P("M166 96 C174 108 174 124 166 136", "n")
            + P("M20 88 C10 104 10 128 20 144", "n t") + P("M180 88 C190 104 190 128 180 144", "n t"))


def _hairy(cx, cy, r, n, cls="d"):
    out = C(cx, cy, r, cls)
    for k in range(n):
        a = math.radians(360 * k / n)
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        x2, y2 = cx + (r + 13) * math.cos(a + 0.12), cy + (r + 13) * math.sin(a + 0.12)
        xm, ym = cx + (r + 10) * math.cos(a - 0.08), cy + (r + 10) * math.sin(a - 0.08)
        out += P(f"M{x1:.1f} {y1:.1f} Q{xm:.1f} {ym:.1f} {x2:.1f} {y2:.1f}", "n t")
    return out


def rambutan():
    return (_hairy(78, 100, 46, 26)
            + P("M120 160 C120 130 186 130 186 160 C186 178 120 178 120 160 Z", "d")
            + E(153, 150, 26, 18, "a") + E(153, 150, 9, 6, "b")
            + R(74, 34, 6, 22, "b", 3) + leaf(80, 40, -40, 30, "c") + ground(184))


def cymbals():
    def cym(cx, cy, rot):
        return (f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy + 6, 38, 11, "c")
                + P(f"M{cx-22} {cy+2} C{cx-22} {cy-26} {cx+22} {cy-26} {cx+22} {cy+2} Z", "d")
                + C(cx, cy - 20, 5, "b") + "</g>")
    return (P("M58 104 C60 40 140 40 142 104", "n") + C(100, 52, 6, "e")
            + cym(58, 124, -18) + cym(142, 124, 18)
            + P("M14 150 L4 160 M20 164 L12 178 M186 150 L196 160 M180 164 L188 178", "n t"))


def chain():
    out = ""
    for k in range(5):
        x, y = 30 + k * 34, 156 - k * 28
        if k % 2 == 0:
            out += E(x, y, 26, 16, "b", -40) + E(x, y, 15, 6, "a", -40)
        else:
            out += f'<g transform="rotate(-40 {x} {y})">' + R(x - 26, y - 6, 52, 12, "c", 6) + "</g>"
    return out


def grass():
    def blade(x, h, lean, cls="c"):
        return P(f"M{x-6} 182 Q{x-2+lean*0.4:.1f} {182-h*0.6:.1f} {x+lean} {182-h} "
                 f"Q{x+4+lean*0.3:.1f} {182-h*0.5:.1f} {x+6} 182 Z", cls)
    blades = [(24, 70, -10), (40, 96, 6), (56, 78, -6), (72, 110, 10), (90, 86, -8), (106, 120, 4),
              (122, 90, 12), (138, 104, -10), (154, 80, 8), (172, 94, -4)]
    out = "".join(blade(x, h, l, "c" if i % 2 else "b") for i, (x, h, l) in enumerate(blades))
    return (cloud(110, 50, 0.6, "a") + out + P("M44 182 L46 120", "n") + star(46, 112, 12, 6, "e", 6)
            + C(46, 112, 4, "d") + ground(182))


def crown():
    return (P("M40 132 L36 70 L70 104 L100 54 L130 104 L164 70 L160 132 Z", "c")
            + C(36, 64, 9, "e") + C(100, 48, 10, "e") + C(164, 64, 9, "e")
            + R(36, 128, 128, 32, "d", 6) + C(68, 144, 7, "e") + E(100, 144, 10, 8, "b") + C(132, 144, 7, "e")
            + P("M70 116 L70 108 M130 116 L130 108", "n t") + ground(176))


def goad():
    """Pa-tak: a long wooden pole with a pointed metal tip."""
    return ('<g transform="rotate(35 100 100)">' + R(94, 56, 12, 140, "b", 5)
            + P("M100 4 C112 20 114 40 106 56 L94 56 C86 40 88 20 100 4 Z", "c")
            + R(90, 54, 20, 10, "d", 3) + P("M106 70 C126 72 130 90 116 96", "n")
            + "".join(L(94, y, 106, y + 6, "n t") for y in (120, 134, 148)) + "</g>")


def pedestal():
    """Than: a stepped stand, here holding a little potted plant."""
    return (R(26, 160, 148, 24, "b", 3) + R(42, 138, 116, 22, "c", 3) + R(58, 118, 84, 20, "b", 3)
            + P("M74 118 L126 118 L132 86 L68 86 Z", "d") + R(64, 80, 72, 10, "d", 4)
            + P("M100 80 L100 42", "n") + leaf(100, 62, -140, 30, "c") + leaf(100, 52, -40, 30, "c")
            + C(100, 34, 10, "e") + C(100, 34, 4, "a"))


def grandstand():
    """At-tha-jan: rows of stadium seats."""
    steps = P("M14 184 L14 154 L54 154 L54 124 L94 124 L94 94 L134 94 L134 64 L174 64 L174 184 Z", "b")
    seats = "".join(R(x + 6, y - 12, 28, 12, "d", 4) for x, y in [(14, 154), (54, 124), (94, 94), (134, 64)])
    seats2 = "".join(R(x + 6, y - 12, 28, 12, "e", 4) for x, y in [(54, 154), (94, 124), (134, 94)])
    roof = P("M120 40 L192 28 L192 40 L120 52 Z", "c") + R(184, 40, 6, 24, "c")
    return steps + seats + seats2 + roof + P("M150 30 L150 8", "n") + poly([(150, 8), (170, 14), (150, 20)], "e") + ground(184)


def gem():
    return (P("M44 78 L76 46 L124 46 L156 78 Z", "d") + P("M44 78 L156 78 L100 164 Z", "c")
            + P("M76 46 L66 78 L100 164 L134 78 L124 46 M100 46 L84 78 M100 46 L116 78", "n t")
            + star(164, 40, 12, 4, "e", 4) + star(36, 132, 10, 3, "e", 4) + star(160, 136, 8, 3, "e", 4))


def bag():
    return (P("M64 82 C32 110 34 176 70 182 L130 182 C166 176 168 110 136 82 Z", "b")
            + P("M76 84 C64 60 92 56 100 70 C108 56 136 60 124 84 Z", "c")
            + P("M62 88 C90 98 110 98 138 88", "n") + P("M138 88 C150 96 154 110 148 122", "n")
            + R(140, 120, 18, 24, "d", 4)
            + "".join(C(x, y, 4, "e") for x, y in [(60, 120), (84, 112), (108, 124), (60, 150), (84, 140), (108, 154),
                                                    (132, 160), (84, 170), (126, 108)]))


def leafbig():
    veins = "".join(P(f"M100 {y} L{100 + s * 36} {y - 22}", "n t") for y in (70, 100, 130) for s in (-1, 1))
    return (P("M100 18 C160 48 168 120 100 176 C32 120 40 48 100 18 Z", "c")
            + P("M100 30 L100 194", "n") + veins)


def lid():
    pot = (P("M46 126 L154 126 L146 178 C144 186 56 186 54 178 Z", "b") + R(38, 116, 124, 12, "d", 6)
           + R(24, 128, 22, 10, "d", 5) + R(154, 128, 22, 10, "d", 5))
    top = ('<g transform="rotate(-14 100 80)">' + P("M40 88 C40 58 160 58 160 88 Z", "c")
           + E(100, 88, 62, 8, "b") + R(90, 46, 20, 14, "d", 6) + "</g>")
    steam = P("M86 112 C80 104 92 100 86 92 M114 112 C108 104 120 100 114 92", "n t")
    return pot + steam + top


def phaan():
    """Phaan: a round tray on a stand, holding fruit."""
    return (C(74, 78, 20, "d") + C(126, 78, 20, "d") + C(100, 66, 22, "e")
            + leaf(100, 46, -60, 18, "c")
            + P("M28 94 L172 94 L156 112 L44 112 Z", "c")
            + P("M86 112 L114 112 L110 150 L90 150 Z", "b")
            + P("M58 176 C62 152 138 152 142 176 Z", "c")
            + P("M50 103 L150 103", "n t") + ground(176))


def pumpkin():
    return (P("M104 60 C104 50 110 40 122 36", "n")
            + E(62, 124, 36, 50, "d") + E(138, 124, 36, 50, "d") + E(100, 122, 34, 56, "e")
            + R(94, 54, 12, 16, "b", 3) + leaf(110, 60, -20, 34, "c")
            + P("M80 56 C70 48 80 38 88 46 C92 50 86 54 84 50", "n t") + ground(176))


def eraser():
    return (R(36, 96, 124, 54, "a", 8) + P("M44 96 L62 76 L176 76 L160 96 Z", "b")
            + P("M160 96 L176 76 L176 128 L160 150 Z", "b")
            + R(92, 96, 68, 54, "c", 2) + P("M98 96 L114 76 L176 76 L160 96 Z", "c")
            + "".join(E(x, y, 5, 3, "e") for x, y in [(40, 172), (56, 178), (70, 170)])
            + P("M100 176 C112 166 126 186 140 174 C150 166 160 182 176 172", "n t"))


def sala():
    """Sala: an open rest pavilion with a plain roof."""
    return (P("M24 92 L100 38 L176 92 Z", "d") + P("M14 100 L186 100 L174 88 L26 88 Z", "c")
            + R(40, 100, 12, 64, "b") + R(148, 100, 12, 64, "b") + R(94, 100, 12, 64, "b")
            + R(56, 138, 34, 8, "e", 2) + R(110, 138, 34, 8, "e", 2)
            + R(26, 162, 148, 14, "c", 3) + R(82, 176, 36, 8, "b", 2)
            + C(100, 70, 8, "a") + ground(184))


def paper():
    return ('<g transform="rotate(8 100 100)">' + R(50, 32, 104, 148, "b", 3) + "</g>"
            + P("M44 26 L130 26 L152 48 L152 176 L44 176 Z", "a") + P("M130 26 L130 48 L152 48 Z", "c")
            + "".join(L(58, y, 138, y, "n t") for y in (66, 84, 102, 120, 138, 156)))


def chest():
    return (R(26, 100, 148, 78, "b", 4) + P("M26 100 L26 82 C26 50 174 50 174 82 L174 100 Z", "c")
            + R(52, 100, 14, 78, "d") + R(134, 100, 14, 78, "d")
            + P("M52 100 L52 60 L66 57 L66 100 Z", "d") + P("M134 57 L148 60 L148 100 L134 100 Z", "d")
            + R(88, 90, 24, 28, "e", 4) + C(100, 102, 4, "n") + L(100, 106, 100, 112, "n t") + ground(184))


def basin():
    return (P("M22 96 L178 96 C174 146 140 172 100 172 C60 172 26 146 22 96 Z", "b")
            + E(100, 96, 78, 12, "c") + E(100, 97, 66, 7, "e")
            + R(74, 170, 52, 10, "c", 4) + P("M40 124 C80 134 120 134 160 124", "n t")
            + C(70, 70, 6, "a") + C(88, 56, 4, "a") + C(124, 64, 5, "a") + ground(184))


def chula():
    """Chula: the big five-pointed star kite."""
    pts = star_pts(100, 86, 76, 32)
    sticks = "".join(L(100, 86, x, y, "n t") for (x, y) in pts[::2])
    return (poly(pts, "d") + sticks + C(100, 86, 8, "e")
            + P("M100 94 C110 130 150 140 160 192", "n")
            + E(130, 136, 10, 6, "c", 30) + E(152, 164, 10, 6, "c", 60))


def helicopter():
    return (P("M136 100 L186 88 L186 102 L136 122 Z", "c") + E(186, 95, 5, 18, "b")
            + R(86, 66, 10, 12, "b") + R(16, 58, 160, 9, "b", 4)
            + E(90, 110, 52, 34, "c")
            + P("M58 92 C64 80 84 78 96 82 L96 112 L52 112 C50 104 54 98 58 92 Z", "a")
            + L(110, 84, 110, 138, "n t")
            + L(64, 142, 64, 160, "n") + L(116, 142, 116, 160, "n") + R(36, 158, 112, 8, "b", 4) + ground(184))


def key():
    return ('<g transform="rotate(-30 100 100)">' + C(52, 100, 34, "d") + C(52, 100, 13, "a")
            + R(84, 93, 104, 14, "c", 5) + R(150, 107, 12, 24, "c", 2) + R(170, 107, 12, 16, "c", 2)
            + "</g>")


def bed():
    return (R(20, 64, 20, 118, "c", 5) + R(160, 98, 20, 84, "c", 5)
            + R(36, 138, 128, 14, "b", 3) + R(36, 112, 128, 28, "a", 8)
            + P("M74 108 L164 108 L164 142 L74 142 Z", "d") + E(60, 104, 22, 11, "e")
            + R(40, 150, 10, 30, "b") + R(150, 150, 10, 30, "b")
            + "".join(L(80, y, 160, y, "n t") for y in (120, 130)) + ground(182))


def bananaleaf():
    veins = "".join(P(f"M{x} {y} L{x - 24} {y - 30}", "n t") + P(f"M{x} {y} L{x + 22} {y + 22}", "n t")
                    for x, y in [(60, 140), (82, 116), (104, 92), (126, 70), (148, 50)])
    return (P("M24 176 C34 100 110 30 186 18 C180 82 120 162 24 176 Z", "c")
            + P("M18 186 C70 128 130 64 186 18", "n") + veins)


def flag():
    """A flag with stripes to color (any colours you like)."""
    stripes = [(30, 14, "c"), (44, 12, "a"), (56, 26, "d"), (82, 12, "a"), (94, 14, "c")]
    return (R(28, 14, 10, 170, "b", 4) + C(33, 12, 7, "e")
            + "".join(R(38, y, 136, h, cls) for y, h, cls in stripes)
            + R(16, 180, 34, 8, "b", 3))


PICS = {"th_bottle": bottle, "th_hammer": hammer, "th_bell": bell, "th_rambutan": rambutan,
        "th_cymbals": cymbals, "th_chain": chain, "th_grass": grass, "th_crown": crown, "th_goad": goad,
        "th_pedestal": pedestal, "th_grandstand": grandstand, "th_gem": gem, "th_bag": bag, "th_leaf": leafbig,
        "th_lid": lid, "th_phaan": phaan, "th_pumpkin": pumpkin, "th_eraser": eraser, "th_sala": sala,
        "th_paper": paper, "th_chest": chest, "th_basin": basin, "th_chula": chula,
        "th_helicopter": helicopter, "th_key": key, "th_bed": bed, "th_bananaleaf": bananaleaf, "th_flag": flag}
