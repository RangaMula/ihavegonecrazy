# -*- coding: utf-8 -*-
"""Pictures for Book 26 (Dzongkha). Keys prefixed dz_. Objects, plants and nature only.
(Named dz_pics.py, not dz.py, so it never shadows languages/dz.py on import.)"""
import math
from illos import P, C, E, R, L, poly, leaf, ground


def drum():
    """A plain two-headed drum on a short stand."""
    return (E(100, 70, 62, 18, "a") + P("M38 70 L38 130 C38 154 162 154 162 130 L162 70 C162 88 38 88 38 70 Z", "b")
            + "".join(L(x, 84 + (0 if 50 < x < 150 else -4), x + 18, 140, "n t") for x in range(44, 150, 18))
            + E(100, 70, 46, 12, "n t") + R(92, 150, 16, 24, "c", 3) + R(64, 172, 72, 10, "c", 4)
            + f'<g transform="rotate(-30 150 40)">' + R(146, 14, 7, 54, "d", 3) + C(149.5, 14, 7, "e") + "</g>")


def table():
    return (R(18, 78, 164, 16, "b", 4) + R(28, 94, 144, 14, "c", 2)
            + R(34, 108, 12, 70, "b", 3) + R(154, 108, 12, 70, "b", 3)
            + "".join(R(x, 98, 30, 6, "n t") for x in (56, 86, 116))
            + P("M84 78 L88 52 L112 52 L116 78 Z", "d") + E(100, 52, 12, 3, "e") + ground(178))


def stove():
    """A simple metal wood-stove with its chimney pipe and a pot on top."""
    return (R(40, 80, 120, 92, "b", 8) + R(32, 72, 136, 12, "c", 4) + R(62, 104, 52, 40, "a", 6)
            + "".join(L(70, y, 106, y, "n t") for y in (116, 124, 132)) + C(136, 120, 7, "d")
            + R(140, 20, 14, 52, "c", 3) + R(136, 18, 22, 8, "c", 2)
            + P("M66 72 L70 46 L110 46 L114 72 Z", "d") + R(64, 40, 52, 8, "d", 3)
            + R(44, 172, 12, 10, "c", 2) + R(144, 172, 12, 10, "c", 2) + ground(182))


def stone():
    return (P("M24 178 C20 146 44 120 80 118 C112 116 130 142 128 178 Z", "b")
            + P("M114 178 C112 150 132 130 156 130 C178 130 188 154 184 178 Z", "c")
            + P("M70 120 C66 96 86 80 106 84 C124 88 130 106 122 124 C108 122 90 116 70 120 Z", "d")
            + P("M50 150 L62 140 L72 146", "n t") + P("M148 152 L158 146 L168 154", "n t") + ground(178))


def frame():
    """A picture frame with mountains and the sun inside."""
    return (R(26, 24, 148, 128, "b", 6) + R(40, 38, 120, 100, "a", 2)
            + C(126, 64, 12, "d") + P("M40 138 L76 82 L100 112 L118 92 L160 138 Z", "c")
            + P("M68 94 L76 82 L84 94 Z", "a") + R(92, 152, 16, 18, "b", 2) + R(70, 168, 60, 10, "b", 4))


def bowl():
    return (E(100, 92, 72, 16, "a") + P("M28 92 C30 140 64 164 100 164 C136 164 170 140 172 92 C170 104 30 104 28 92 Z", "b")
            + P("M56 120 C80 132 120 132 144 120", "n t") + P("M66 140 C88 148 112 148 134 140", "n t")
            + R(80, 162, 40, 12, "c", 4) + E(100, 92, 56, 10, "n t") + ground(176))


def dzong():
    """A big white fortress building with a tall tower in the middle."""
    wins = "".join(R(x, 128, 12, 14, "d", 2) for x in (30, 52, 136, 158))
    return (P("M14 176 L20 110 L180 110 L186 176 Z", "a") + R(12, 100, 176, 12, "c", 2)
            + P("M66 176 L70 70 L130 70 L134 176 Z", "b") + R(58, 58, 84, 14, "c", 2)
            + P("M76 58 L100 36 L124 58 Z", "e") + R(96, 24, 8, 12, "d", 2)
            + wins + R(84, 86, 12, 14, "d", 2) + R(104, 86, 12, 14, "d", 2) + R(88, 146, 24, 30, "e", 8)
            + ground(176))


def bridge():
    """A wooden bridge between two stone towers over a river."""
    return (P("M10 150 C40 140 60 160 100 150 C140 140 160 160 190 150 L190 186 L10 186 Z", "c")
            + P("M20 168 C40 160 56 174 76 166 M120 172 C140 164 156 178 176 170", "n t")
            + R(16, 90, 40, 70, "b", 4) + R(144, 90, 40, 70, "b", 4)
            + P("M12 90 L36 70 L60 90 Z", "e") + P("M140 90 L164 70 L188 90 Z", "e")
            + P("M56 110 C80 124 120 124 144 110 L144 120 C120 134 80 134 56 120 Z", "d")
            + "".join(L(x, 104 + (0.004 * (x - 100) ** 2) - 4, x, 118 + 0.004 * (x - 100) ** 2 - 6, "n t") for x in range(66, 140, 12))
            + R(30, 120, 12, 16, "a", 2) + R(158, 120, 12, 16, "a", 2))


def big_leaf():
    veins = "".join(L(100, y, 100 + s * 34, y - 22, "n t") for y in (70, 96, 122, 146) for s in (-1, 1))
    return (P("M100 20 C150 50 168 110 100 170 C32 110 50 50 100 20 Z", "c") + L(100, 30, 100, 186, "n") + veins)


def chilli():
    def one(dx, rot, cls):
        return (f'<g transform="translate({dx} 0) rotate({rot} 100 100)">'
                + P("M92 52 C120 52 126 90 118 124 C110 156 92 176 72 182 C88 160 96 132 94 100 C93 80 88 64 92 52 Z", cls)
                + P("M88 54 C90 40 104 38 106 50 C104 58 92 60 88 54 Z", "c") + P("M98 40 C98 30 104 22 112 20", "n") + "</g>")
    return one(-28, -12, "d") + one(30, 14, "e") + ground(186)


def fire():
    return (f'<g transform="rotate(-14 100 168)">' + R(36, 158, 128, 20, "b", 10) + "</g>"
            + f'<g transform="rotate(14 100 168)">' + R(36, 158, 128, 20, "c", 10) + "</g>"
            + P("M100 30 C120 60 150 80 144 120 C140 148 120 160 100 160 C80 160 60 148 56 120 C52 96 72 86 76 64 "
                "C88 76 90 88 92 96 C96 74 92 52 100 30 Z", "d")
            + P("M100 90 C112 106 124 116 120 134 C118 148 108 152 100 152 C92 152 82 148 80 134 C78 120 92 112 100 90 Z", "e"))


def slate(text="ཀ", size=None):
    fs = size or min(96, int(240 / max(len(text), 1)))
    return (R(18, 34, 164, 128, "b", 12) + R(32, 48, 136, 100, "a", 6)
            + f'<text x="100" y="{104 + fs * 0.25:.0f}" text-anchor="middle" font-size="{fs}">{text}</text>'
            + R(120, 168, 44, 10, "e", 4) + R(40, 166, 14, 14, "d", 3))


PICS = {"dz_drum": drum, "dz_table": table, "dz_stove": stove, "dz_stone": stone, "dz_frame": frame, "dz_bowl": bowl,
        "dz_dzong": dzong, "dz_bridge": bridge, "dz_leaf": big_leaf, "dz_chilli": chilli, "dz_fire": fire, "dz_slate": slate}
