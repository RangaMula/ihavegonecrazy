# -*- coding: utf-8 -*-
"""Pictures for Book 51 Javanese, 52 Sundanese and 53 Balinese. Objects, plants and nature only."""
from illos import P, E, L, ground

_n = [0]


def nyiru():
    """A nyiru: a round, flat tray woven from bamboo, used to winnow and dry rice."""
    _n[0] += 1
    cid = f"nyiru{_n[0]}"
    inner = "M24 104 A76 46 0 1 0 176 104 A76 46 0 1 0 24 104 Z"
    weave = "".join(L(x, 50, x + 70, 160, "n t") for x in range(-60, 200, 15)) + \
            "".join(L(x, 50, x - 70, 160, "n t") for x in range(10, 270, 15))
    grains = "".join(E(x, y, 3.6, 2, "n", r) for x, y, r in [(86, 100, 20), (100, 92, -15), (114, 100, 30), (96, 106, 0), (106, 84, 10)])
    return (P("M8 106 L8 120 A92 58 0 0 0 192 120 L192 106 Z", "c") + E(100, 106, 92, 58, "b") + P(inner, "a")
            + f'<clipPath id="{cid}"><path d="{inner}"/></clipPath><g clip-path="url(#{cid})">{weave}</g>'
            + P(inner, "n") + P("M64 110 C70 80 130 80 136 110 C116 118 84 118 64 110 Z", "d") + grains + ground(190))


PICS = {"su_nyiru": nyiru}
