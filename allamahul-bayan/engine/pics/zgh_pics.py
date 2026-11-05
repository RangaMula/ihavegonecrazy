# -*- coding: utf-8 -*-
"""Pictures for Book 58 (Tamazight, keys zgh_*) and Book 59 (Bambara in N'Ko, keys nqo_*).
Objects, plants and nature only. viewBox 0 0 200 200.
Named zgh_pics.py, not zgh.py, so it never shadows languages/zgh.py on sys.path."""
from illos import P, C, E, R, L, poly, cloud, leaf, ground


def road():  # ⴰⴱⵔⵉⴷ abrid - a path winding to the mountains
    return (C(156, 40, 16, "d")
            + P("M10 112 L54 62 L84 92 L124 46 L190 112 Z", "b")
            + P("M54 62 L44 74 L52 72 L58 78 L64 70 Z M124 46 L112 60 L120 58 L126 66 L134 56 Z", "a")
            + P("M10 112 L190 112 L190 184 L10 184 Z", "c")
            + P("M64 184 C80 158 132 150 114 132 C106 124 98 118 100 112 L106 112 C110 120 150 134 140 150 "
                "C132 164 118 172 132 184 Z", "a")
            + P("M94 178 C100 168 112 162 118 154 M114 140 C112 134 108 128 104 122", "n t")
            + R(30, 126, 6, 22, "e") + C(33, 122, 12, "c") + R(166, 128, 6, 20, "e") + C(169, 124, 11, "c"))


def argan():  # ⴰⵔⴳⴰⵏ argan - the argan tree of southern Morocco
    crown = (E(100, 74, 80, 30, "c") + E(56, 70, 34, 22, "c") + E(146, 70, 36, 22, "c") + E(100, 56, 50, 22, "c"))
    fruits = "".join(E(x, y, 6, 4.5, "d") for x, y in ((70, 80), (92, 66), (120, 82), (146, 74), (56, 66), (110, 52), (84, 88)))
    trunk = (P("M88 176 C92 150 80 130 70 104 L82 100 C92 120 98 132 100 140 C104 124 112 110 124 100 L134 106 "
               "C120 122 112 146 114 176 Z", "e"))
    return trunk + crown + fruits + P("M40 182 C70 176 130 176 160 182", "n") + ground(184)


def milk():  # a bottle of milk and a full bowl
    bottle = (P("M126 62 L126 46 L150 46 L150 62 C162 70 166 80 166 92 L166 166 C166 172 162 176 156 176 "
                "L120 176 C114 176 110 172 110 166 L110 92 C110 80 114 70 126 62 Z", "a")
              + R(122, 36, 32, 12, "d", 4)
              + P("M110 110 L166 110 L166 166 C166 172 162 176 156 176 L120 176 C114 176 110 172 110 166 Z", "b"))
    bowl = (P("M20 124 L104 124 C102 156 84 176 62 176 C40 176 22 156 20 124 Z", "c")
            + E(62, 124, 42, 9, "a") + P("M40 148 C54 154 70 154 84 148", "n t"))
    drops = P("M62 98 C66 106 68 110 62 112 C56 110 58 106 62 98 Z", "a") + P("M40 104 C43 110 44 113 40 114 C36 113 37 110 40 104 Z", "a")
    return bottle + bowl + drops + ground(180)


def babouche():  # ⴰⵀⴰⵔⴽⵓⵙ aharkus - a pointed leather slipper
    return (P("M14 150 C14 132 30 122 56 120 C80 118 96 108 112 96 C126 86 150 86 170 98 C182 106 188 122 186 138 "
              "C184 152 172 158 150 158 L36 158 C22 158 14 156 14 150 Z", "b")
            + P("M112 96 C126 86 150 86 170 98 C164 118 140 128 116 126 C108 116 108 104 112 96 Z", "a")
            + P("M14 150 C40 156 150 156 186 140 L186 146 C176 160 160 164 150 164 L36 164 C20 164 12 158 14 150 Z", "e")
            + P("M40 132 C60 128 80 126 100 118", "n t")
            + "".join(C(x, 140, 3, "d") for x in (48, 66, 84, 102, 120, 138, 156))
            + ground(176))


def rehal():  # a folding wooden stand holding the Qur'an
    stand = (poly([(48, 104), (64, 98), (152, 176), (136, 182)], "e")
             + poly([(152, 104), (136, 98), (48, 176), (64, 182)], "e")
             + C(100, 140, 7, "d"))
    book = (P("M100 70 C80 58 52 58 30 66 L44 112 C62 104 84 106 100 116 Z", "a")
            + P("M100 70 C120 58 148 58 170 66 L156 112 C138 104 116 106 100 116 Z", "a")
            + P("M100 116 C84 106 62 104 44 112 L42 118 C62 112 84 114 100 124 C116 114 138 112 158 118 L156 112 "
                "C138 104 116 106 100 116 Z", "b")
            + P("M50 74 C64 70 78 70 92 76 M52 84 C66 80 80 80 92 86 M54 94 C68 90 80 90 92 96 "
                "M150 74 C136 70 122 70 108 76 M148 84 C134 80 120 80 108 86 M146 94 C132 90 120 90 108 96", "n t")
            + L(100, 70, 100, 116))
    return stand + book + ground(186)


def tagine():  # ⵟⵟⴰⵊⵉⵏ ṭṭajin - a clay cooking pot with a tall lid
    return (P("M14 150 C14 170 186 170 186 150 L176 140 L24 140 Z", "b")
            + E(100, 140, 76, 12, "c")
            + P("M36 138 C60 112 80 72 92 40 L108 40 C120 72 140 112 164 138 C130 148 70 148 36 138 Z", "a")
            + P("M50 126 C80 132 120 132 150 126 M66 104 C88 110 112 110 134 104", "n t")
            + "".join(C(x, y, 3, "d") for x, y in ((72, 118), (100, 120), (128, 118), (86, 96), (114, 96)))
            + E(100, 38, 12, 6, "d") + C(100, 24, 10, "d")
            + P("M60 78 c-6 -8 6 -14 0 -22 M150 82 c-6 -8 6 -14 0 -22", "n t") + ground(180))


def slate():  # ⵍⵍⵓⵃ lluḥ - the wooden board for learning to write
    return (P("M56 40 C56 20 144 20 144 40 L144 46 L56 46 Z", "e")
            + C(100, 30, 6, "a")
            + R(44, 46, 112, 132, "e", 10)
            + R(54, 56, 92, 112, "a", 6)
            + "".join(P(f"M64 {y} c8 -6 12 6 20 0 c8 -6 12 6 20 0 c8 -6 12 6 20 0 c6 -4 10 2 14 0", "n t")
                      for y in (76, 96, 116, 136, 156))
            + R(150, 120, 8, 52, "d", 3) + P("M150 172 L154 184 L158 172 Z", "c"))


def big_leaf():  # ߝߎߙߊ fura - a leaf
    return (P("M100 178 C100 150 100 128 102 110", "n")
            + P("M102 112 C40 112 24 60 40 20 C100 22 160 40 162 100 C150 112 126 116 102 112 Z", "c")
            + P("M102 112 C90 84 70 54 44 26", "n")
            + P("M66 54 L60 72 M82 72 L72 92 M74 50 L96 50 M88 66 L114 64 M100 84 L130 84", "n t")
            + leaf(112, 156, -40, 40, "c") + ground(180))


def millet():  # ߢߐ ɲɔ - millet heads on tall stalks
    def stalk(x, top, h, lean):
        return (P(f"M{x} 182 C{x} {top + 90} {x + lean} {top + 60} {x + lean} {top + h}", "n")
                + E(x + lean, top + h / 2, 9, h / 2, "d")
                + "".join(L(x + lean - 8, top + k, x + lean + 8, top + k + 4, "n t") for k in range(10, int(h) - 4, 10)))
    return (stalk(60, 30, 64, -10) + stalk(100, 16, 70, 2) + stalk(140, 34, 60, 12)
            + leaf(60, 140, -150, 40, "c") + leaf(100, 130, -30, 44, "c") + leaf(140, 146, -20, 38, "c")
            + leaf(100, 160, -150, 40, "c") + ground(182))


def kola():  # ߥߏߙߏ woro - kola nuts and an open pod
    nut = lambda x, y, s, cls: (P(f"M{x} {y} c{-22*s} 0 {-34*s} {16*s} {-30*s} {32*s} c{4*s} {18*s} {24*s} {26*s} {30*s} {18*s} "
                                  f"c{6*s} {8*s} {26*s} 0 {30*s} {-18*s} c{4*s} {-16*s} {-8*s} {-32*s} {-30*s} {-32*s} Z", cls)
                                + P(f"M{x} {y + 4*s} C{x - 2*s} {y + 20*s} {x - 2*s} {y + 34*s} {x} {y + 48*s}", "n t"))
    pod = (P("M24 96 C40 60 120 56 150 74 C130 100 60 110 24 96 Z", "c") + P("M30 94 C60 80 110 76 144 76", "n t")
           + P("M150 74 L168 60", "n"))
    return pod + nut(64, 112, 1.0, "d") + nut(120, 108, 1.1, "b") + nut(94, 132, 0.9, "a") + ground(184)


PICS = {"zgh_road": road, "zgh_argan": argan, "zgh_milk": milk, "zgh_babouche": babouche, "zgh_rehal": rehal,
        "zgh_tagine": tagine, "zgh_slate": slate,
        "nqo_leaf": big_leaf, "nqo_millet": millet, "nqo_kola": kola}
