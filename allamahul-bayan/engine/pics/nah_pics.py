# -*- coding: utf-8 -*-
"""Pictures for Book 85 (Nahuatl) and Book 86 (K'iche'). Objects, plants and nature only. viewBox 0 0 200 200."""
from illos import P, C, E, R, L, poly, star, crescent, cloud, leaf, ground


def avocado():
    """A whole avocado and a cut half with its big round stone (Nahuatl awakatl, K'iche' oj)."""
    whole = (P("M62 46 C78 46 84 66 90 86 C98 112 96 150 62 152 C28 150 26 112 34 86 C40 66 46 46 62 46 Z", "c")
             + R(58, 34, 8, 14, "b", 3) + leaf(66, 38, -30, 30))
    half = (P("M140 58 C158 58 164 80 170 100 C178 128 174 166 140 168 C106 166 102 128 110 100 C116 80 122 58 140 58 Z", "c")
            + P("M140 70 C153 70 157 88 161 104 C167 128 162 156 140 157 C118 156 113 128 119 104 C123 88 127 70 140 70 Z", "a")
            + C(140, 124, 18, "b") + P("M132 116 C134 112 138 110 142 110", "n t"))
    return whole + half + ground(182)


def nopal():
    """Prickly-pear cactus (nopalli): flat oval pads with small fruits on top."""
    def pad(cx, cy, rx, ry, rot):
        sp = "".join(L(cx + dx - 3, cy + dy, cx + dx + 3, cy + dy, "n t") for dx, dy in
                     ((-rx * 0.4, -ry * 0.3), (rx * 0.35, -ry * 0.1), (-rx * 0.1, ry * 0.35), (rx * 0.1, -ry * 0.6)))
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, "c") + sp + "</g>"
    fruit = lambda x, y: E(x, y, 8, 11, "d") + L(x - 4, y - 11, x + 4, y - 11, "n t")
    return (pad(100, 138, 32, 40, 0) + pad(64, 88, 24, 32, -28) + pad(138, 84, 24, 32, 26) + pad(100, 50, 17, 23, 0)
            + fruit(52, 54) + fruit(152, 48) + fruit(100, 20) + fruit(78, 60)
            + P("M78 178 L84 160 H116 L122 178 Z", "b") + ground(180))


def petlatl():
    """A woven palm mat (Nahuatl petlatl, K'iche' pop) with a checker weave, lying flat."""
    out = []
    x0, y0, cw, ch, sk = 30, 70, 24, 18, 10   # cells, skewed to the right as rows go down
    for r in range(5):
        for c in range(6):
            x = x0 + c * cw + r * sk * 0.6; y = y0 + r * ch
            cls = "b" if (r + c) % 2 else "a"
            out.append(poly([(x, y), (x + cw, y), (x + cw + sk * 0.6, y + ch), (x + sk * 0.6, y + ch)], cls))
    # a rolled end on the right
    out.append(P("M174 70 C186 70 192 84 186 96 L196 160 C202 172 188 180 180 160", "n"))
    return "".join(out) + ground(176)


def tortilla():
    """A stack of corn tortillas (tlaxkalli / wa) on a cloth in a round basket."""
    basket = (P("M24 120 H176 C172 160 146 178 100 178 C54 178 28 160 24 120 Z", "b")
              + "".join(L(40 + i * 20, 124, 46 + i * 18, 172, "n t") for i in range(7))
              + L(30, 140, 170, 140, "n t") + L(40, 160, 160, 160, "n t"))
    cloth = poly([(24, 120), (6, 96), (60, 110)], "d") + poly([(176, 120), (196, 94), (140, 110)], "d")
    stack = "".join(E(100, 112 - i * 9, 64, 15, "a") for i in range(5))
    dots = "".join(C(100 + dx, 76 + dy, 2.5, "e") for dx, dy in ((-30, 0), (-8, -6), (20, 2), (36, -4), (4, 6)))
    return basket + cloth + stack + dots


def sapote():
    """Mamey sapote (tzapotl): a brown oval fruit and a cut half with orange flesh and a long shiny seed."""
    whole = (P("M30 110 C30 70 60 52 78 52 C96 52 120 70 120 110 C120 150 96 168 76 168 C56 168 30 150 30 110 Z", "b")
             + R(72, 42, 10, 12, "e", 3))
    half = (P("M100 112 C100 76 124 60 142 60 C160 60 186 76 186 112 C186 148 160 166 142 166 C124 166 100 148 100 112 Z", "b")
            + P("M110 112 C110 82 128 70 143 70 C158 70 176 82 176 112 C176 142 158 156 143 156 C128 156 110 142 110 112 Z", "d")
            + E(143, 112, 14, 30, "e") + P("M137 92 C135 100 135 108 137 116", "n t"))
    return whole + half + leaf(86, 48, -40, 32) + ground(182)


def amaranth():
    """An amaranth plant (wawtli) with a tall drooping plume of tiny seeds and broad leaves."""
    stem = P("M100 182 C100 140 98 100 100 64", "n")
    plume = "".join(E(100 + 1.5 * i * i / 6, 64 - i * 11, 13 - i * 0.9, 9, "d", 10 + i * 4) for i in range(6))
    side = "".join(E(78 - i * 6, 92 - i * 9, 8 - i, 6, "d", -30) for i in range(3)) + \
           "".join(E(122 + i * 6, 96 - i * 9, 8 - i, 6, "d", 30) for i in range(3))
    arms = P("M100 110 C92 104 84 98 80 90", "n") + P("M100 114 C108 108 116 104 120 96", "n")
    leaves = leaf(100, 150, -160, 44) + leaf(100, 138, -20, 44) + leaf(100, 124, -150, 34) + leaf(100, 128, -35, 34)
    return stem + arms + side + plume + leaves + ground(182)


def night():
    """Night (yowalli): a crescent moon and stars above dark hills."""
    hills = P("M14 182 C40 140 70 130 96 150 C120 120 160 118 186 150 L186 182 Z", "c")
    stars = (star(46, 52, 12, cls="e") + star(150, 110, 9, cls="e") + star(84, 104, 8, cls="e")
             + star(172, 40, 10, cls="e") + star(30, 112, 7, cls="e"))
    return crescent(122, 64, 34, 16, -10, 30, "e") + stars + cloud(24, 86, 0.55, "a") + hills + ground(182)


def river():
    """A river winding between green banks down from the hills."""
    return (P("M14 70 C50 40 80 52 100 40 C130 22 160 40 186 32 L186 182 L14 182 Z", "c")
            + P("M96 42 C110 70 70 90 86 118 C100 144 150 150 136 182 L176 182 C192 150 130 136 120 116 C108 92 132 66 112 40 Z", "e")
            + P("M108 80 C102 88 100 94 102 100", "n t") + P("M118 140 C126 146 134 150 140 158", "n t")
            + E(40, 120, 12, 18, "c") + L(40, 138, 40, 156, "n") + E(166, 96, 10, 15, "c") + L(166, 111, 166, 126, "n")
            + ground(182))


PICS = {"nah_avocado": avocado, "nah_nopal": nopal, "nah_petlatl": petlatl, "nah_tortilla": tortilla,
        "nah_sapote": sapote, "nah_amaranth": amaranth, "nah_night": night, "nah_river": river}
