# -*- coding: utf-8 -*-
"""Pictures for Book 15 Sindhi (sd_*) and Book 16 Pashto (ps_*). Objects, plants and nature only.

(Named sd_ps.py, not sd.py / ps.py: a plug-in module called sd.py would be cached as the module
"sd" and shadow languages/sd.py when build.py imports the language by its code.)
"""
import math
from illos import P, C, E, R, L, poly, leaf, ground


def garlic():  # Sindhi ٿوم thoom
    bulb = P("M100 44 C110 64 150 78 156 118 C162 156 134 176 100 176 C66 176 38 156 44 118 C50 78 90 64 100 44 Z", "a")
    lines = P("M100 64 C86 96 82 140 92 172 M100 64 C114 96 118 140 108 172 "
              "M80 84 C60 112 62 148 74 168 M120 84 C140 112 138 148 126 168", "n t")
    stem = P("M92 50 C92 36 94 22 96 12 L106 12 C108 22 108 36 108 50 Z", "c")
    roots = P("M84 176 l-6 10 M96 177 l-2 11 M106 177 l2 11 M116 176 l6 10", "n t")
    clove = P("M168 140 C180 150 186 166 182 180 L146 180 C146 162 154 146 168 140 Z", "b") + P("M168 140 C166 154 166 168 170 180", "n t")
    return bulb + lines + stem + roots + clove + L(14, 188, 186, 188)


def wood():  # Sindhi ڪاٺ kaaṭh (logs)
    def log(x, y, w, h, cls):
        return (E(x, y + h / 2, h * 0.28, h / 2, cls) + R(x, y, w, h, cls)
                + E(x + w, y + h / 2, h * 0.32, h / 2, "a") + E(x + w, y + h / 2, h * 0.18, h * 0.28, "n t")
                + C(x + w, y + h / 2, 2.5, "n") + P(f"M{x+16} {y+h*0.35} h{w*0.4} M{x+30} {y+h*0.68} h{w*0.35}", "n t"))
    return (log(26, 130, 110, 48, "b") + log(46, 82, 110, 48, "c") + log(66, 34, 96, 48, "b")
            + leaf(40, 120, -120, 26) + ground(182))


def jamun():  # Sindhi ڄمون jamun / black plum
    twig = P("M20 40 C60 44 100 40 150 22", "n") + P("M70 42 L74 70 M110 36 L112 60 M96 40 L90 66", "n t")
    berries = "".join(E(x, y, 13, 17, cls, r) + E(x - 4, y - 7, 3, 5, "n t", r)
                      for x, y, r, cls in [(66, 88, -10, "d"), (92, 82, 0, "b"), (118, 78, 10, "d"),
                                           (78, 116, -6, "b"), (106, 112, 6, "d"), (92, 144, 0, "b")])
    loose = E(150, 164, 14, 18, "d", 20) + E(176, 168, 12, 16, "b", -15)
    return twig + leaf(130, 30, -20, 44) + leaf(44, 42, 200, 38) + berries + loose + ground(186)


def lake():  # Sindhi ڍنڍ ḍhanḍh
    hills = P("M14 110 C40 70 70 70 92 100 C110 66 150 60 186 104 L186 120 L14 120 Z", "c")
    sun = C(150, 44, 18, "d")
    water = P("M14 120 C60 112 140 112 186 120 L186 186 L14 186 Z", "b")
    ripples = P("M40 140 q10 -6 20 0 q10 6 20 0 M100 158 q10 -6 20 0 q10 6 20 0 M60 172 q10 -6 20 0", "n t")
    reeds = "".join(P(f"M{x} 186 C{x-2} 160 {x+2} 140 {x+4*s} 112", "n") + E(x + 4 * s, 106, 5, 13, "e", 10 * s)
                    for x, s in [(150, 1), (164, -1), (176, 1)])
    lily = E(70, 150, 18, 6, "e") + P("M60 146 L66 132 L72 144 L78 132 L82 146 Z", "a")
    return hills + sun + water + ripples + reeds + lily


def comb():  # Sindhi ڦڻي phaṇee, Pashto ږمنځ zhmandz
    teeth = "".join(R(36 + 9 * k, 96, 6, 58 if k % 2 == 0 else 46, "b", 3) for k in range(15))
    return (f'<g transform="rotate(-12 100 100)">' + teeth + R(26, 62, 148, 40, "c", 14)
            + P("M40 82 h120", "n t") + "</g>")


def jasmine():  # Sindhi ياسمين jasmine
    def bloom(cx, cy, r, cls):
        pet = "".join(E(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)), r * 0.62, r * 1.0, cls, a + 90)
                      for a in range(-90, 270, 72))
        return pet + C(cx, cy, r * 0.42, "d")
    stems = P("M100 186 C98 150 96 120 70 84 M98 140 C112 118 126 104 142 78 M98 120 C102 96 100 70 104 50", "n")
    buds = E(150, 118, 6, 12, "e", 30) + E(56, 120, 6, 12, "e", -30)
    return (stems + leaf(98, 160, -150, 38) + leaf(100, 150, -30, 38) + leaf(84, 104, 200, 28) + leaf(124, 104, -40, 28)
            + P("M98 140 C120 130 140 124 150 118 M84 104 C70 112 62 118 56 120", "n t") + buds
            + bloom(70, 76, 18, "a") + bloom(144, 72, 18, "a") + bloom(104, 44, 18, "a") + ground(186))


def mulberry():  # Pashto توت toot
    def berry(cx, cy, rot, cls):
        dots = "".join(C(cx + dx, cy + dy, 5.5, cls) for dx, dy in
                       [(-6, -24), (6, -24), (-8, -10), (4, -10), (-8, 4), (6, 4), (-6, 18), (6, 18), (0, 30), (0, -36)])
        return (f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, 19, 42, "a") + dots
                + P(f"M{cx} {cy-38} L{cx} {cy-54}", "n") + "</g>")
    return (P("M14 30 C70 40 120 32 186 20", "n") + leaf(120, 32, 30, 50) + leaf(60, 36, 160, 44)
            + berry(52, 112, 10, "b") + berry(102, 118, 0, "d") + berry(152, 112, -10, "b") + ground(190))


def bigleaf():  # Pashto پاڼه paaṇa
    big = (f'<g transform="translate(36 170) rotate(-48)">'
           + P("M0 0 C50 -66 140 -66 186 0 C140 66 50 66 0 0 Z", "c") + L(0, 0, 176, 0, "n")
           + "".join(L(30 + 30 * k, 0, 52 + 30 * k, -26 + 2 * k, "n t") + L(30 + 30 * k, 0, 52 + 30 * k, 26 - 2 * k, "n t")
                     for k in range(5))
           + "</g>")
    stalk = P("M36 170 L18 190", "n")
    small = leaf(150, 168, -20, 40, "e")
    return big + stalk + small


def circle():  # Pashto دائره daa'ira
    ring = "".join(C(100 + 72 * math.cos(math.radians(a)), 100 + 72 * math.sin(math.radians(a)), 8, "e") for a in range(0, 360, 30))
    return C(100, 100, 86, "b") + ring + C(100, 100, 58, "a") + C(100, 100, 36, "c") + C(100, 100, 14, "d")


PICS = {"sd_garlic": garlic, "sd_wood": wood, "sd_jamun": jamun, "sd_lake": lake, "sd_comb": comb,
        "sd_jasmine": jasmine, "ps_comb": comb, "ps_mulberry": mulberry, "ps_leaf": bigleaf, "ps_circle": circle}
