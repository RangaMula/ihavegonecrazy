# -*- coding: utf-8 -*-
"""Pictures for Book 30 (Kurdish Sorani). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, L, cloud, ground


def cave():           # غار ghar - a cave in a rocky hill
    return (P("M10 184 L46 92 L70 110 L104 40 L150 104 L168 88 L192 184 Z", "c")
            + P("M86 40 L104 40 L122 64 L110 58 L100 66 L92 56 Z", "a")        # snowy peak
            + P("M64 184 C64 134 82 116 104 116 C126 116 142 134 142 184 Z", "e")  # cave mouth
            + P("M80 184 C82 150 92 136 104 136 C116 136 126 150 128 184", "n t")
            + P("M30 160 L44 150 M160 150 L172 160 M150 124 L162 118", "n t")
            + P("M150 184 C156 168 168 168 174 184 Z", "b") + P("M30 184 C34 172 44 172 48 184 Z", "b")
            + C(164, 34, 13, "d") + cloud(18, 52, 0.45) + ground(184))


PICS = {"ckb_cave": cave}
