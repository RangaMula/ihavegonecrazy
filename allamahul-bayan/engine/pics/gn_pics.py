# -*- coding: utf-8 -*-
"""Pictures for Book 83 (Guaraní). Objects, plants and nature only. viewBox 0 0 200 200."""
import math
from illos import P, C, E, R, L, poly, star, leaf, ground


def guembe():
    """Guembe (Philodendron): a big leaf cut into long fingers, on a tall stem, with a smaller leaf beside it."""
    def lobe(x, y, ang, sz):
        return (f'<g transform="translate({x} {y}) rotate({ang})">'
                + P(f"M0 0 C{sz*0.3} {-sz*0.2} {sz*0.75} {-sz*0.17} {sz} 0 C{sz*0.75} {sz*0.17} {sz*0.3} {sz*0.2} 0 0 Z", "c")
                + L(sz * 0.08, 0, sz * 0.88, 0, "n t") + "</g>")
    small = "".join(lobe(156, 112, a, 34) for a in range(-160, -10, 25))
    big = "".join(lobe(86, 110, a, 72 if -160 < a < -20 else 60) for a in range(-178, 0, 18))
    return (P("M156 112 C158 136 156 160 152 182", "n") + small
            + P("M86 110 C88 136 90 160 92 182", "n") + big + C(86, 110, 7, "b") + ground(182))


def mandio():
    """Mandiʼo (cassava): long tapering roots under a stem with hand-shaped leaves."""
    def root(x, y, ang, ln, w):
        return (f'<g transform="translate({x} {y}) rotate({ang})">'
                + P(f"M0 {-w} C{ln*0.35} {-w*1.4} {ln*0.75} {-w*0.6} {ln} 0 C{ln*0.75} {w*0.6} {ln*0.35} {w*1.4} 0 {w} Z", "b")
                + L(ln * 0.3, -w * 0.9, ln * 0.33, w * 0.9, "n t") + L(ln * 0.6, -w * 0.55, ln * 0.62, w * 0.55, "n t")
                + "</g>")
    leaves = "".join(leaf(100, 52, a, 44, "c") for a in range(-170, -5, 33))
    return (P("M100 52 L100 104", "n") + leaves + R(92, 96, 16, 22, "e", 4)
            + root(90, 114, 150, 62, 10) + root(110, 114, 30, 62, 10)
            + root(92, 118, 118, 72, 12) + root(108, 118, 62, 72, 12) + root(100, 120, 90, 66, 12))


def nanduti():
    """Ñanduti: the round, sun-like lace of Paraguay."""
    cx = cy = 100
    out = "".join(C(cx + 84 * math.cos(math.radians(a)), cy + 84 * math.sin(math.radians(a)), 11, "d")
                  for a in range(0, 360, 18))
    out += C(cx, cy, 80, "a")
    out += "".join(L(cx + 24 * math.cos(math.radians(a)), cy + 24 * math.sin(math.radians(a)),
                     cx + 80 * math.cos(math.radians(a)), cy + 80 * math.sin(math.radians(a)), "n t") for a in range(0, 360, 15))
    out += P(f"M{cx-60} {cy} A60 60 0 1 0 {cx+60} {cy} A60 60 0 1 0 {cx-60} {cy} Z", "n t")
    out += "".join(E(cx + 48 * math.cos(math.radians(a)), cy + 48 * math.sin(math.radians(a)), 11, 6, "e", a)
                   for a in range(0, 360, 30))
    out += star(cx, cy, 26, 12, "b", 8) + C(cx, cy, 9, "c")
    return out


def uruku():
    """Uruku (annatto): spiky heart-shaped pods on a branch, one open to show its seeds."""
    def pod(x, y, s=1.0, rot=0):
        spikes = "".join(L(x + 22 * s * math.cos(math.radians(a)), y + 4 * s + 24 * s * math.sin(math.radians(a)),
                           x + 30 * s * math.cos(math.radians(a)), y + 4 * s + 32 * s * math.sin(math.radians(a)), "n t")
                         for a in range(-60, 250, 26))
        return (f'<g transform="rotate({rot} {x} {y})">' + spikes
                + P(f"M{x} {y-30*s} C{x+30*s} {y-18*s} {x+28*s} {y+22*s} {x} {y+32*s} "
                    f"C{x-28*s} {y+22*s} {x-30*s} {y-18*s} {x} {y-30*s} Z", "e")
                + P(f"M{x} {y-26*s} C{x+6*s} {y} {x+6*s} {y+14*s} {x} {y+28*s}", "n t") + "</g>")
    opened = (P("M128 132 C112 136 108 168 130 182 C148 172 146 140 128 132 Z", "e")
              + P("M134 134 C150 132 170 150 164 176 C150 182 140 164 134 134 Z", "e")
              + "".join(C(x, y, 3.6, "d") for x, y in [(126, 150), (130, 162), (124, 168), (132, 172), (136, 152), (150, 156),
                                                         (154, 168), (146, 166), (140, 146)]))
    return (P("M14 52 C60 40 100 46 140 30 C160 22 176 22 190 26", "n")
            + P("M70 46 C66 60 64 70 60 82", "n t") + P("M124 36 C126 52 124 64 120 76", "n t")
            + leaf(100, 46, -40, 40) + leaf(160, 24, 20, 32) + leaf(40, 48, 150, 34)
            + pod(58, 110, 1.0, -10) + pod(118, 104, 0.95, 12) + opened)


def mate():
    """Kaʼa (yerba mate): a gourd cup with a metal straw, and yerba leaves."""
    return (leaf(150, 120, -70, 38) + leaf(160, 150, -20, 34) + leaf(40, 160, -150, 32) + leaf(36, 130, -120, 30)
            + P("M112 60 L140 14", "n") + R(132, 10, 16, 8, "d", 3)
            + P("M58 84 C40 120 52 176 100 178 C148 176 160 120 142 84 Z", "b")
            + E(100, 84, 42, 10, "a") + E(100, 84, 32, 6, "c")
            + P("M60 112 C80 118 120 118 140 112", "n t") + P("M110 82 L114 70", "n")
            + E(100, 180, 30, 5, "a"))


PICS = {"gn_guembe": guembe, "gn_mandio": mandio, "gn_nanduti": nanduti, "gn_uruku": uruku, "gn_mate": mate}
