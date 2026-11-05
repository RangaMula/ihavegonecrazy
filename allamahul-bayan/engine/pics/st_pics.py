# -*- coding: utf-8 -*-
"""Pictures for Book 77 (Sesotho). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, leaf, poly, ground


def heke():
    """A farm gate (heke) between two posts."""
    leaves = R(46, 86, 52, 84, "a", 2) + R(102, 86, 52, 84, "a", 2)
    bars = "".join(L(x, 86, x, 170) for x in (59, 72, 85, 115, 128, 141))
    rails = L(46, 106, 98, 106) + L(46, 150, 98, 150) + L(102, 106, 154, 106) + L(102, 150, 154, 150)
    brace = L(46, 170, 98, 86) + L(154, 170, 102, 86)
    posts = R(26, 66, 18, 116, "b", 3) + R(156, 66, 18, 116, "b", 3)
    caps = poly([(24, 66), (35, 52), (46, 66)], "d") + poly([(154, 66), (165, 52), (176, 66)], "d")
    latch = R(94, 122, 12, 8, "e", 2)
    wire = L(8, 96, 26, 96) + L(8, 124, 26, 124) + L(174, 96, 192, 96) + L(174, 124, 192, 124)
    return leaves + bars + rails + brace + posts + caps + latch + wire + ground(182)


def jwang():
    """Grass (jwang): tufts of mountain grass with seed heads."""
    out = P("M8 188 C50 172 150 172 192 188 Z", "b")
    for bx, n, hh in [(46, 5, 70), (102, 7, 104), (158, 5, 76)]:
        for k in range(n):
            lean = (k - (n - 1) / 2) * 12
            tx, ty = bx + lean * 1.6, 180 - hh + abs(lean) * 0.9
            out += P(f"M{bx-5+k*2} 180 C{bx-4+k*2} {(180+ty)/2} {tx-3} {ty+18} {tx} {ty} "
                     f"C{tx+3} {ty+20} {bx+1+k*2} {(180+ty)/2} {bx+3+k*2} 180 Z", "c")
    for x, top in [(74, 66), (130, 58)]:
        out += L(x, 180, x, top)
        out += "".join(E(x + s * 6, top + 10 + j * 12, 4, 8, "e", s * 30) for j in range(3) for s in (-1, 1))
    return out


def mokorotlo():
    """A mokorotlo: the woven grass hat of Lesotho, with its knot on top."""
    cone = P("M92 44 C80 92 52 128 26 148 C60 172 140 172 174 148 C148 128 120 92 108 44 Z", "d")
    bands = P("M78 96 C92 104 108 104 122 96 M56 128 C84 140 116 140 144 128 M38 146 C78 160 122 160 162 146", "n")
    weave = P("M74 108 l8 20 l8 -20 l8 20 l8 -20 l8 20 l8 -20 l8 20 l8 -20", "n t")
    knob = E(100, 42, 14, 8, "e") + E(100, 32, 10, 7, "e") + C(100, 20, 7, "e") + P("M94 14 C90 6 96 2 100 8", "n t")
    return cone + bands + weave + knob + ground(176)


def mokopu():
    """A pumpkin (mokopu) with its stem, a leaf and a curly tendril."""
    body = E(100, 124, 74, 52, "d")
    ribs = P("M100 74 C80 92 80 156 100 176 M100 74 C120 92 120 156 100 176 "
             "M100 74 C54 86 44 160 100 176 M100 74 C146 86 156 160 100 176", "n")
    stem = P("M94 76 L92 52 L108 50 L106 76 Z", "c")
    tendril = P("M108 56 C122 44 136 54 130 62 C126 68 118 62 124 56", "n t")
    return body + ribs + stem + leaf(92, 56, -150, 40) + tendril + ground(182)


def kobo():
    """A folded woollen blanket (kobo) with stripes and a pattern."""
    back = R(36, 58, 128, 44, "b", 6)
    front = R(24, 92, 152, 84, "b", 6)
    stripes = R(24, 104, 152, 8, "d") + R(24, 156, 152, 8, "d") + R(36, 70, 128, 7, "d")
    motif = "".join(poly([(x, 134 - 12), (x + 12, 134), (x, 134 + 12), (x - 12, 134)], "e") for x in (54, 88, 122, 156))
    fringe = "".join(L(x, 176, x, 186, "n t") for x in range(30, 176, 8))
    return back + front + stripes + motif + fringe


PICS = {"st_heke": heke, "st_jwang": jwang, "st_mokorotlo": mokorotlo, "st_mokopu": mokopu, "st_kobo": kobo}
