# -*- coding: utf-8 -*-
"""Pictures for Book 75 (Twi / Akan). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, leaf, star, ground


def sika():
    """Gold coins (sika): a little stack and one big shiny coin."""
    stack = ""
    for i in range(5):
        y = 162 - i * 13
        stack += P(f"M28 {y} L28 {y+11} A32 9 0 0 0 92 {y+11} L92 {y} Z", "d") + E(60, y, 32, 9, "d")
    coin = C(136, 112, 42, "d") + C(136, 112, 32, "a") + star(136, 112, 18, cls="e")
    shine = P("M176 54 l0 14 M169 61 l14 0 M30 80 l0 12 M24 86 l12 0", "n t")
    return stack + coin + shine + ground(186)


def lore():
    """A lorry (lɔre) with a wooden cargo box."""
    box = R(18, 66, 108, 78, "b", 4)
    slats = "".join(L(18, y, 126, y, "n t") for y in (86, 106, 126))
    cab = P("M126 90 L158 90 L180 118 L180 146 L126 146 Z", "e")
    window = P("M134 98 L154 98 L168 118 L134 118 Z", "a")
    chassis = R(14, 140, 170, 10, "c", 3)
    lamp = C(176, 130, 4, "d")
    wheels = C(50, 152, 17, "c") + C(50, 152, 6, "a") + C(150, 152, 17, "c") + C(150, 152, 6, "a")
    return box + slats + cab + window + L(144, 124, 154, 124) + chassis + lamp + wheels + ground(170)


def _pepper(x, y, rot, cls="d"):
    body = P("M-17 0 C-22 40 -14 82 6 122 C3 92 18 50 17 0 C9 -7 -9 -7 -17 0 Z", cls)
    cap = P("M-20 2 C-14 -10 14 -10 20 2 C10 9 -10 9 -20 2 Z", "c")
    stem = P("M0 -5 C0 -15 6 -22 14 -26", "n")
    return f'<g transform="translate({x} {y}) rotate({rot})">{body}{cap}{stem}</g>'


def mako():
    """Hot peppers (mako): two chili peppers and a leaf."""
    return _pepper(78, 46, -14) + _pepper(128, 54, 16, "e") + leaf(40, 170, -20, 40) + ground(186)


def paanoo():
    """A loaf of bread (paanoo) on a wooden board."""
    board = R(18, 152, 164, 16, "b", 6) + C(170, 160, 3, "n")
    loaf = P("M32 144 C28 104 52 76 100 76 C148 76 172 104 168 144 C168 152 162 156 154 156 L46 156 "
             "C38 156 32 152 32 144 Z", "d")
    cuts = P("M64 94 C70 102 72 112 70 122 M100 88 C106 98 108 110 106 122 M136 94 C142 102 144 112 142 122", "n")
    return board + loaf + cuts + ground(176)


def borofere():
    """A papaya (borɔfere): one whole fruit and one cut half full of seeds."""
    whole = E(70, 102, 34, 60, "d", -18) + P("M88 46 C90 38 94 32 100 28", "n") + leaf(98, 30, -40, 34)
    half = E(146, 132, 32, 48, "e", 12) + E(146, 132, 24, 39, "a", 12) + E(146, 136, 11, 22, "b", 12)
    seeds = "".join(C(x, y, 2.6, "n") for x, y in [(143, 122), (148, 128), (144, 136), (149, 144), (145, 151), (150, 118)])
    return whole + half + seeds + ground(186)


def toa():
    """A bottle (toa) with a cap and a label."""
    bottle = P("M88 32 L112 32 L112 58 C112 70 136 78 136 102 L136 172 C136 180 130 184 122 184 L78 184 "
               "C70 184 64 180 64 172 L64 102 C64 78 88 70 88 58 Z", "b")
    cap = R(85, 20, 30, 14, "d", 3)
    label = R(64, 112, 72, 42, "a") + star(100, 133, 12, cls="e")
    shine = P("M74 104 L74 110 M74 162 L74 172", "n t")
    return bottle + cap + label + shine + ground(186)


def bayere():
    """A yam (bayerɛ): a long tuber and a cut piece showing its white inside."""
    tuber = P("M24 150 C18 132 36 120 64 112 C104 100 142 74 166 60 C182 52 190 68 180 80 "
              "C160 104 120 132 82 150 C60 160 30 168 24 150 Z", "b")
    marks = P("M52 132 l6 4 M84 118 l5 5 M114 102 l6 3 M146 82 l4 6 M66 146 l6 2 M100 132 l5 4 M134 108 l6 2", "n t")
    roots = P("M30 160 l-8 10 M176 58 l8 -8 M178 76 l10 2", "n t")
    piece = P("M120 172 C118 156 132 146 150 146 C166 146 176 156 174 168 C172 180 156 184 144 182 C130 182 122 180 120 172 Z", "b")
    flesh = E(148, 164, 18, 11, "a", -6)
    return tuber + marks + roots + piece + flesh + ground(188)


def kookoo():
    """A cocoa pod (kookoo) on its stalk with a leaf: Ghana grows a lot of cocoa."""
    pod = P("M100 46 C138 54 154 98 146 136 C138 164 118 180 100 182 C82 180 62 164 54 136 C46 98 62 54 100 46 Z", "d")
    ridges = P("M100 50 C90 92 90 140 100 180 M100 50 C110 92 110 140 100 180 M78 60 C66 100 70 146 84 172 "
               "M122 60 C134 100 130 146 116 172", "n t")
    stalk = P("M100 46 C100 34 104 26 112 20", "n")
    return leaf(108, 26, 160, 54) + leaf(112, 22, -10, 56) + pod + ridges + stalk + ground(188)


PICS = {"tw_sika": sika, "tw_lore": lore, "tw_mako": mako, "tw_paanoo": paanoo, "tw_borofere": borofere,
        "tw_toa": toa, "tw_bayere": bayere, "tw_kookoo": kookoo}
