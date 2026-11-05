# -*- coding: utf-8 -*-
"""Pictures for Book 56 (Amharic) and Book 57 (Tigrinya). Objects, plants and nature only.
(File is not named am.py: a module called `am` here would shadow languages/am.py on import.)"""
import math
from illos import P, C, E, R, L, poly, leaf, ground


def sunflower():
    pet = "".join(E(100 + 40 * math.cos(math.radians(a)), 74 + 40 * math.sin(math.radians(a)), 11, 22, "d", a + 90)
                  for a in range(0, 360, 30))
    seeds = "".join(C(100 + r * math.cos(math.radians(a)), 74 + r * math.sin(math.radians(a)), 1.8, "n")
                    for r, step in ((8, 60), (16, 30)) for a in range(0, 360, step))
    return (P("M100 110 C98 140 102 160 100 186", "n") + leaf(100, 160, -150, 44) + leaf(101, 140, -30, 44)
            + pet + C(100, 74, 28, "b") + seeds + ground(186))


def seedling():
    return (P("M100 128 C99 108 100 92 100 76", "n")
            + P("M100 96 C80 70 50 72 40 84 C56 100 84 104 100 96 Z", "c") + P("M100 96 C80 88 60 86 46 86", "n t")
            + P("M100 78 C116 50 150 48 162 60 C148 80 118 86 100 78 Z", "c") + P("M100 78 C118 68 140 64 156 62", "n t")
            + P("M40 150 L160 150 L148 186 L52 186 Z", "b") + R(32, 132, 136, 20, "e", 6)
            + P("M48 132 C70 120 130 120 152 132 Z", "a"))


def table():
    return (R(20, 96, 160, 14, "b", 4) + R(32, 110, 136, 12, "b", 2)
            + R(36, 122, 12, 62, "b", 2) + R(152, 122, 12, 62, "b", 2)
            + P("M76 96 C70 74 70 60 82 52 L118 52 C130 60 130 74 124 96 Z", "e")
            + E(100, 52, 20, 5, "e")
            + C(88, 40, 9, "d") + C(104, 34, 10, "a") + C(118, 42, 9, "c") + ground(186))


def rose():
    head = (P("M64 64 C58 40 80 24 100 30 C120 24 142 40 136 64 Z", "e")
            + P("M86 34 C92 44 94 54 92 62 M114 34 C108 44 106 54 108 62", "n t")
            + P("M58 56 C54 90 76 110 100 110 C124 110 146 90 142 56 C128 70 112 74 100 64 C88 74 72 70 58 56 Z", "e")
            + P("M74 70 C72 86 80 100 90 106 M126 70 C128 86 120 100 110 106", "n t"))
    return (P("M100 110 C98 136 102 160 100 186", "n") + P("M99 146 l-8 -6 M101 166 l8 -6", "n t")
            + leaf(100, 132, -150, 40) + leaf(100, 154, -30, 40)
            + head + ground(186))


def papaya():
    whole = P("M58 30 C88 26 104 56 102 96 C100 140 82 176 60 176 C36 176 22 140 24 98 C26 58 34 34 58 30 Z", "d")
    half = (P("M120 70 C150 66 176 90 176 130 C176 164 158 182 140 182 C122 182 106 164 106 130 C106 96 110 72 120 70 Z", "d")
            + P("M128 92 C150 92 162 112 160 136 C158 158 148 168 140 168 C130 168 120 156 120 134 C120 112 120 94 128 92 Z", "a"))
    seeds = "".join(C(x, y, 4, "c") for x, y in [(136, 108), (146, 116), (132, 124), (144, 132), (136, 142), (146, 148), (138, 156)])
    return whole + P("M58 30 L56 16", "n") + leaf(56, 18, -40, 20) + half + seeds


def chocolate():
    sq = "".join(R(52 + 26 * i, 70 + 26 * j, 22, 22, "b", 3) for i in range(4) for j in range(3))
    return (R(46, 64, 108, 120, "b", 6) + sq
            + P("M40 120 L160 120 L160 186 L40 186 Z", "e")
            + P("M40 120 L56 112 L72 122 L88 112 L104 122 L120 112 L136 122 L152 112 L160 120", "n t")
            + R(64, 140, 72, 26, "a", 6))


def tv():
    return (P("M78 22 L100 50 L124 18", "n") + C(78, 20, 4, "c") + C(124, 16, 4, "c")
            + R(24, 50, 152, 112, "b", 14) + R(38, 62, 100, 86, "a", 10)
            + C(156, 80, 8, "c") + C(156, 104, 8, "c") + R(148, 124, 16, 16, "d", 3)
            + P("M52 82 C70 74 90 76 102 86", "n t")
            + P("M60 162 L48 184 M140 162 L152 184", "n") + ground(186))


def vanilla():
    cx, cy = 132, 56
    pet = "".join(E(cx + 22 * math.cos(math.radians(a)), cy + 22 * math.sin(math.radians(a)), 9, 20, "a", a + 90)
                  for a in range(-90, 270, 72))
    flower = pet + P(f"M{cx-12} {cy} C{cx-12} {cy-12} {cx+12} {cy-12} {cx+12} {cy} C{cx+12} {cy+16} {cx-12} {cy+16} {cx-12} {cy} Z", "d") + C(cx, cy, 4, "e")
    vine = (P("M24 186 C30 150 26 120 44 96 C60 74 86 62 112 58", "n")
            + leaf(30, 150, -70, 36) + leaf(38, 112, 200, 34) + leaf(70, 72, -100, 30))
    pods = "".join(P(f"M70 {y} C100 {y-6} 150 {y-6} 186 {y-2} C188 {y+2} 186 {y+5} 182 {y+5} C150 {y+4} 100 {y+6} 70 {y+8} Z", "c")
                   for y in (150, 162, 174))
    return vine + flower + pods + R(96, 144, 12, 44, "e", 4) + P("M102 188 l-10 8 M102 188 l10 8", "n t")


def bread():
    return (P("M28 128 C24 86 60 64 100 64 C140 64 176 86 172 128 C172 146 160 154 150 154 L50 154 C40 154 28 146 28 128 Z", "d")
            + P("M64 84 l-10 26 M94 76 l-10 28 M124 76 l-10 28 M152 86 l-10 24", "n")
            + E(100, 168, 82, 12, "b") + ground(182))


PICS = {"am_sunflower": sunflower, "am_seedling": seedling, "am_table": table, "am_rose": rose,
        "am_papaya": papaya, "am_chocolate": chocolate, "am_tv": tv, "am_vanilla": vanilla, "am_bread": bread}
