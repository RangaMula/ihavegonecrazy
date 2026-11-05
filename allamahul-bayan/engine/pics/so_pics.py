# -*- coding: utf-8 -*-
"""Pictures for Book 66 (Somali). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, star, leaf, ground


def khudaar():
    """Vegetables (khudaar): a carrot, an onion and a tomato in a woven basket."""
    carrot = (P("M112 118 C110 96 140 56 160 40 C168 46 150 92 134 120 Z", "e")
              + P("M128 84 l8 4 M120 100 l9 3 M140 66 l7 4", "n t")
              + leaf(160, 40, -70, 26, "c") + leaf(160, 40, -30, 24, "c") + leaf(160, 40, -110, 22, "c"))
    onion = (P("M96 52 C88 70 64 82 66 104 C68 122 124 122 126 104 C128 82 104 70 96 52 Z", "a")
             + P("M96 58 C90 76 82 92 84 116 M96 58 C102 76 110 92 108 116", "n t")
             + P("M96 52 C94 42 96 34 100 28", "n"))
    tomato = (C(58, 108, 28, "d") + star(58, 82, 12, 5, "c", 5) + R(56, 70, 5, 8, "c", 2)
              + P("M44 98 C48 92 54 90 58 90", "n t"))
    basket = (P("M26 122 L174 122 L158 184 L42 184 Z", "b") + R(20, 112, 160, 16, "c", 7)
              + P("M50 128 L58 184 M78 128 L82 184 M100 128 L100 184 M122 128 L118 184 M150 128 L142 184", "n t")
              + P("M34 146 L166 146 M38 166 L162 166", "n t"))
    return carrot + onion + tomato + basket


PICS = {"so_khudaar": khudaar}
