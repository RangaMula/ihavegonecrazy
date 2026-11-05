# -*- coding: utf-8 -*-
"""Pictures for Book 63 (Hausa). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, poly, leaf, ground


def yalo():
    """Garden eggs (yalo): small round white-green eggplants with leafy green caps."""
    def fruit(cx, cy, rx, ry, rot):
        cap = (f'<g transform="rotate({rot} {cx} {cy})">'
               + P(f"M{cx-rx*0.55} {cy-ry*0.72} C{cx-rx*0.3} {cy-ry*1.05} {cx+rx*0.3} {cy-ry*1.05} {cx+rx*0.55} {cy-ry*0.72} "
                   f"L{cx+rx*0.35} {cy-ry*0.55} L{cx+rx*0.12} {cy-ry*0.75} L{cx-rx*0.12} {cy-ry*0.55} L{cx-rx*0.35} {cy-ry*0.75} Z", "c")
               + R(cx - 4, cy - ry * 1.25, 8, ry * 0.32, "c", 3) + "</g>")
        return E(cx, cy, rx, ry, "a", rot) + P(f"M{cx-rx*0.5} {cy+ry*0.1} C{cx-rx*0.4} {cy+ry*0.5} {cx-rx*0.1} {cy+ry*0.7} {cx+rx*0.2} {cy+ry*0.72}", "n t") + cap
    return (fruit(64, 128, 40, 44, -12) + fruit(138, 132, 38, 40, 14) + fruit(100, 86, 34, 36, 0)
            + leaf(150, 70, -40, 34) + leaf(40, 72, -150, 30) + ground(178))


PICS = {"ha_yalo": yalo}
