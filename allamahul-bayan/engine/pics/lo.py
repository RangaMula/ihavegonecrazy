# -*- coding: utf-8 -*-
"""Pictures for Book 48 (Lao). Objects, plants and nature only - no people, no animals, no faces,
no religious imagery. viewBox 0 0 200 200; every closed shape has a colour class a-e.
(The Lao book also uses some th_ pictures from engine/pics/th.py.)"""
from illos import P, C, E, R, L, poly, star, cloud, leaf, ground


def glass():
    return (P("M58 34 L142 34 L130 178 L70 178 Z", "a") + P("M62 78 L138 78 L130 178 L70 178 Z", "e")
            + E(100, 34, 42, 7, "a") + E(100, 78, 38, 5, "c")
            + C(88, 120, 5, "a") + C(110, 146, 4, "a") + C(100, 100, 3, "a") + ground(184))


def fire():
    logs = ('<g transform="rotate(18 100 160)">' + R(36, 150, 128, 20, "b", 10) + "</g>"
            + '<g transform="rotate(-18 100 160)">' + R(36, 150, 128, 20, "b", 10) + "</g>")
    flames = (P("M100 30 C130 70 150 100 140 130 C134 150 66 150 60 130 C50 100 76 80 82 56 C92 74 96 50 100 30 Z", "d")
              + P("M100 80 C116 100 122 116 116 132 C110 142 90 142 84 132 C78 116 90 104 100 80 Z", "e"))
    stones = "".join(E(x, 178, 16, 9, "c") for x in (28, 64, 136, 172))
    return flames + logs + stones + ground(186)


def car():
    return (P("M18 132 L18 108 C18 98 26 94 36 92 L58 90 L80 62 C84 58 90 56 96 56 L136 56 C144 56 150 60 154 66 "
              "L170 90 C182 92 188 100 188 112 L188 132 Z", "d")
            + P("M68 90 L86 66 L112 66 L112 90 Z", "a") + P("M122 90 L122 66 L140 66 C144 66 146 68 148 70 L160 90 Z", "a")
            + R(176, 104, 12, 10, "e", 3) + R(18, 106, 10, 10, "e", 3) + L(116, 92, 116, 130, "n t")
            + C(56, 134, 20, "b") + C(56, 134, 8, "a") + C(150, 134, 20, "b") + C(150, 134, 8, "a") + ground(156))


def fan():
    """Wii: a Lao hand fan woven from bamboo."""
    weave = "".join(L(x, 30, x, 140, "n t") for x in (64, 82, 100, 118, 136)) + \
        "".join(L(40, y, 160, y, "n t") for y in (52, 74, 96, 118))
    return (R(93, 136, 14, 54, "b", 6)
            + P("M100 18 C162 18 178 80 150 118 C136 138 112 146 100 146 C88 146 64 138 50 118 C22 80 38 18 100 18 Z", "c")
            + f'<clipPath id="lofan"><path d="M100 18 C162 18 178 80 150 118 C136 138 112 146 100 146 C88 146 64 138 50 118 C22 80 38 18 100 18 Z"/></clipPath>'
            + f'<g clip-path="url(#lofan)">{weave}</g>' + R(86, 134, 28, 10, "d", 4))


def bowl():
    return (P("M28 88 L172 88 C168 140 140 166 100 166 C60 166 32 140 28 88 Z", "b")
            + E(100, 88, 72, 10, "c") + R(74, 164, 52, 10, "c", 4)
            + P("M38 114 C80 126 120 126 162 114", "n t")
            + "".join(C(x, 136, 5, "e") for x in (70, 100, 130))
            + P("M78 70 C70 60 84 54 78 42 M100 70 C92 60 106 54 100 42 M122 70 C114 60 128 54 122 42", "n t") + ground(182))


def pencil():
    return ('<g transform="rotate(-35 100 100)">' + R(32, 88, 116, 24, "d", 2)
            + P("M148 88 L180 100 L148 112 Z", "a") + P("M170 96 L180 100 L170 104 Z", "b")
            + R(12, 88, 18, 24, "e", 5) + R(26, 86, 10, 28, "c", 2) + L(36, 100, 148, 100, "n t") + "</g>")


def branch():
    twig = P("M14 150 C60 132 110 112 186 70 L188 78 C120 118 70 142 16 160 Z", "b")
    side = P("M96 122 C100 100 110 84 128 74 L132 80 C116 90 108 104 104 120 Z", "b")
    leaves = (leaf(60, 140, -120, 34, "c") + leaf(60, 140, 70, 30, "c") + leaf(128, 76, -80, 34, "c")
              + leaf(150, 94, 40, 32, "c") + leaf(186, 72, -20, 30, "c") + leaf(104, 118, 80, 30, "c"))
    return twig + side + leaves


def bush():
    return (C(60, 130, 40, "c") + C(140, 130, 40, "c") + C(100, 104, 50, "c") + C(100, 140, 40, "c")
            + "".join(star(x, y, 9, 4, "e", 5) + C(x, y, 3, "d") for x, y in [(72, 108), (118, 88), (136, 128), (88, 142), (56, 132)])
            + ground(180))


def cupboard():
    return (R(40, 20, 120, 152, "b", 4) + R(48, 30, 50, 96, "a", 3) + R(102, 30, 50, 96, "a", 3)
            + C(92, 80, 4, "d") + C(108, 80, 4, "d") + R(48, 132, 104, 32, "c", 3) + R(88, 144, 24, 7, "d", 3)
            + R(46, 172, 12, 12, "b") + R(142, 172, 12, 12, "b") + ground(184))


def bridge():
    posts = "".join(R(x, 60, 7, 30, "c", 2) for x in (30, 60, 90, 120, 150))
    return (P("M10 160 C10 140 18 130 30 128 L30 90 L170 90 L170 128 C182 130 190 140 190 160 L160 160 "
              "C160 120 40 120 40 160 Z", "b")
            + posts + R(26, 56, 150, 8, "c", 3)
            + P("M40 160 C40 128 160 128 160 160 Z", "e")
            + P("M10 174 C30 164 50 184 70 174 C90 164 110 184 130 174 C150 164 170 184 190 174", "n"))


def cave():
    return (P("M10 184 L46 70 C56 50 70 46 84 60 L100 40 C112 30 126 34 134 48 L190 184 Z", "b")
            + P("M64 184 C64 120 136 120 136 184 Z", "d")
            + P("M80 134 L86 148 L92 132 M104 128 L110 144 L116 130", "n t")
            + E(30, 182, 16, 8, "c") + E(172, 180, 14, 8, "c") + leaf(150, 120, -70, 22, "c") + ground(184))


def chair():
    return (R(56, 24, 14, 150, "b", 3) + R(130, 24, 14, 70, "b", 3) + R(70, 34, 60, 14, "c", 3) + R(70, 58, 60, 14, "c", 3)
            + R(48, 94, 104, 16, "d", 4) + R(56, 110, 12, 72, "b", 3) + R(132, 110, 12, 72, "b", 3)
            + R(68, 150, 64, 8, "c", 2) + ground(184))


def lamp():
    return (P("M60 92 L140 92 L122 30 L78 30 Z", "d") + R(94, 92, 12, 64, "b", 3) + E(100, 166, 44, 12, "c")
            + P("M64 70 L136 70", "n t")
            + P("M44 104 L28 118 M156 104 L172 118 M100 106 L100 104", "n") + ground(178))


PICS = {"lo_glass": glass, "lo_fire": fire, "lo_car": car, "lo_fan": fan, "lo_bowl": bowl, "lo_pencil": pencil,
        "lo_branch": branch, "lo_bush": bush, "lo_cupboard": cupboard, "lo_bridge": bridge, "lo_cave": cave,
        "lo_chair": chair, "lo_lamp": lamp}
