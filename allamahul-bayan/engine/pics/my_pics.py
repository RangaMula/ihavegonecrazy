# -*- coding: utf-8 -*-
"""Pictures for Book 50 (Burmese). Keys are prefixed my_. Objects, plants and nature only.
(File is named my_pics.py, not my.py: a plug-in module called `my` would shadow languages/my.py.)"""
import math
from illos import P, C, E, R, L, leaf, ground
import importlib.util as _iu, os as _os, sys as _sys

# shared drawings live in km_pics.py (same agent); load it by path so sys.path changes by other plug-ins cannot break it
K = _sys.modules.get("km_pics")
if K is None:
    _spec = _iu.spec_from_file_location("km_pics", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "km_pics.py"))
    K = _iu.module_from_spec(_spec); _spec.loader.exec_module(K); _sys.modules["km_pics"] = K


def chilli():
    return (P("M58 52 C90 46 114 62 128 92 C142 122 152 150 172 178 C140 180 108 162 90 134 C74 110 62 86 58 52 Z", "e")
            + P("M58 52 C50 42 52 32 60 30 C68 32 72 42 66 54 Z", "c")
            + P("M60 32 C58 22 62 14 72 10", "n") + P("M82 72 C94 92 108 122 126 152", "n t")
            + leaf(70, 20, 10, 36) + ground(186))


def fan():
    cx, cy, r1, r2 = 100, 168, 132, 46
    def pt(r, a):
        return cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    (x1, y1), (x2, y2) = pt(r1, -160), pt(r1, -20)
    (u1, v1), (u2, v2) = pt(r2, -160), pt(r2, -20)
    leafp = (f"M{u1:.1f} {v1:.1f} L{x1:.1f} {y1:.1f} A{r1} {r1} 0 0 1 {x2:.1f} {y2:.1f} "
             f"L{u2:.1f} {v2:.1f} A{r2} {r2} 0 0 0 {u1:.1f} {v1:.1f} Z")
    ribs = "".join(P("M{:.1f} {:.1f} L{:.1f} {:.1f}".format(*pt(r2, a), *pt(r1, a)), "n t") for a in range(-150, -20, 14))
    band = "".join(C(*pt(96, a), 6, "d") for a in range(-150, -20, 28))
    return (P(leafp, "e") + ribs + band
            + P(f"M{cx} {cy} L{u1:.1f} {v1:.1f} A{r2} {r2} 0 0 1 {u2:.1f} {v2:.1f} Z", "b")
            + R(92, 166, 16, 26, "c", 5) + C(cx, cy, 6, "a"))


def youtiao():
    bubbles = "".join(C(x, y, 2.2, "n") for x, y in [(60, 84), (90, 80), (124, 82), (150, 78), (70, 116), (108, 118), (140, 114)])
    return (E(100, 168, 86, 16, "a") + E(100, 166, 66, 9, "n t")
            + '<g transform="rotate(-18 100 100)">'
            + R(26, 66, 150, 34, "d", 17) + R(26, 98, 150, 34, "d", 17) + L(40, 99, 162, 99, "n t") + bubbles + "</g>")


def hat():
    return (E(100, 130, 88, 30, "c")
            + P("M50 128 C50 72 70 52 100 52 C130 52 150 72 150 128 C130 140 70 140 50 128 Z", "b")
            + P("M52 106 C80 118 120 118 148 106 L149 122 C120 134 80 134 51 122 Z", "e")
            + leaf(132, 118, -40, 30) + C(132, 116, 7, "d")
            + P("M76 70 C70 80 66 92 66 104", "n t"))


def peas():
    return (P("M18 124 C48 70 140 58 186 78 C152 124 70 144 18 124 Z", "c")
            + C(56, 108, 14, "b") + C(86, 100, 15, "b") + C(118, 92, 15, "b") + C(148, 86, 13, "b")
            + P("M18 124 C60 116 140 102 186 78", "n")
            + P("M186 78 C192 66 192 56 186 48", "n") + leaf(186, 52, -110, 34)
            + C(70, 168, 10, "b") + C(94, 172, 10, "b") + C(118, 166, 10, "b") + ground(184))


PICS = dict(my_car=K.car, my_pencil=K.pencil, my_durian=K.durian, my_gourd=K.gourd, my_bamboo=K.bamboo,
            my_chilli=chilli, my_fan=fan, my_youtiao=youtiao, my_hat=hat, my_peas=peas)
