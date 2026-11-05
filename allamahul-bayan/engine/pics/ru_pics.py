# -*- coding: utf-8 -*-
"""Extra pictures for the Cyrillic books 37-40 (Russian, Ukrainian, Bulgarian, Serbian).
Objects, plants and nature only. viewBox 0 0 200 200; every closed shape has a colour role a-e.
(File is ru_pics.py, not ru.py: a plug-in module named like a language code would shadow
languages/<code>.py when build.py imports the language by name.)"""
from illos import P, C, E, R, L, poly, star, leaf, ground


def fir():
    """Fir / spruce tree (ёлка, ель, ела, јела)."""
    tree = P("M100 14 L134 58 L118 57 L150 100 L130 99 L166 146 L34 146 L70 99 L50 100 L82 57 L66 58 Z", "c")
    lines = P("M100 40 L100 136 M100 70 L84 84 M100 70 L116 84 M100 104 L78 122 M100 104 L122 122", "n t")
    cones = E(60, 166, 7, 11, "b", -20) + E(146, 168, 7, 11, "b", 20)
    return (R(90, 146, 20, 36, "b", 3) + tree + lines + cones
            + P("M30 182 C40 172 50 172 56 182 M144 182 C152 172 164 172 170 182", "n t") + ground(182))


def blackberry():
    rows = [(66, (87, 113)), (88, (74, 100, 126)), (110, (61, 87, 113, 139)), (132, (74, 100, 126)),
            (154, (87, 113)), (174, (100,))]
    stem = P("M100 50 C100 34 112 22 128 16", "n")
    sepals = star(100, 54, 26, 9, "b", 5)
    drupes = "".join(C(x, y, 15, "d") + C(x - 4, y - 5, 2.6, "n t") for y, xs in rows for x in xs)
    return (stem + leaf(126, 18, 5, 56, "c") + leaf(108, 30, 200, 48, "c") + sepals + drupes)


def acorn():
    nut = P("M66 94 C64 138 84 172 100 180 C116 172 136 138 134 94 Z", "d")
    cap = P("M56 98 C54 60 146 60 144 98 C144 106 56 106 56 98 Z", "b")
    hatch = P("M66 92 L78 74 M82 98 L98 70 M100 98 L116 70 M118 98 L132 76 M66 78 L74 92 M84 70 L100 96 "
              "M104 70 L120 96 M124 72 L136 92", "n t")
    shine = P("M80 118 C80 136 86 150 94 160", "n t")
    return (leaf(132, 52, -35, 52, "c") + R(95, 40, 10, 26, "b", 4) + nut + cap + hatch + shine
            + ground(186))


def scissors():
    blade1 = P("M80 140 L150 24 C158 26 160 32 156 40 L100 142 Z", "a")
    blade2 = P("M120 140 L50 24 C42 26 40 32 44 40 L100 142 Z", "a")
    h1 = E(70, 158, 26, 20, "c", -25) + E(70, 158, 13, 9, "a", -25)
    h2 = E(130, 158, 26, 20, "c", 25) + E(130, 158, 13, 9, "a", 25)
    return blade2 + blade1 + h1 + h2 + C(100, 104, 6, "e")


def iron():
    """Clothes iron (утюг, праска, ютия)."""
    sole = P("M18 142 L178 142 L178 156 L26 156 Z", "c")
    body = P("M22 142 C32 104 68 84 118 84 L172 84 L172 142 Z", "b")
    handle = P("M80 84 L90 50 C92 44 96 42 102 42 L152 42 C160 42 162 48 160 54 L152 84 L138 84 L144 58 L106 58 L96 84 Z", "a")
    cord = P("M172 112 C188 112 192 132 188 152 C184 172 164 176 152 188", "n")
    return (body + sole + handle + C(128, 112, 11, "e") + L(128, 104, 128, 112, "n t")
            + "".join(C(x, 149, 2.5, "n") for x in (50, 76, 102, 128, 154)) + cord)


def bread():
    """A loaf of bread (хлеб, хліб, хляб, хлеб)."""
    board = R(12, 160, 176, 16, "b", 7)
    loaf = P("M22 132 C22 84 58 64 100 64 C142 64 178 84 178 132 C178 150 164 160 144 160 L56 160 "
             "C36 160 22 150 22 132 Z", "c")
    cuts = P("M58 88 C70 98 74 112 72 126 M96 80 C108 92 112 108 110 124 M134 86 C146 98 150 110 148 124", "n")
    wheat = (P("M168 58 L186 18", "n") + "".join(E(172 + 4 * k, 46 - 9 * k, 4, 8, "d", 25) for k in range(4))
             + "".join(E(182 + 4 * k, 50 - 9 * k, 4, 8, "d", -35) for k in range(3)))
    return board + loaf + cuts + wheat + C(186, 168, 2, "n")


def popsicle():
    """Ice cream on a stick (эскимо, ескімо)."""
    stick = R(90, 132, 20, 52, "b", 9)
    bar = P("M62 46 C62 24 138 24 138 46 L138 138 C138 146 132 150 124 150 L76 150 C68 150 62 146 62 138 Z", "d")
    glaze = P("M62 74 C72 84 80 70 90 80 C100 92 110 70 120 82 C128 90 134 80 138 76", "n")
    sprinkles = "".join(R(x, y, 10, 4, "e", 2).replace("/>", f' transform="rotate({r} {x+5} {y+2})"/>')
                        for x, y, r in [(76, 44, 30), (100, 36, -20), (118, 50, 60), (84, 60, -40), (110, 62, 15)])
    return stick + bar + glaze + sprinkles + P("M76 100 L76 132", "n t") + ground(186)


def button():
    """Sewing buttons (ґудзик)."""
    big = C(92, 96, 66, "c") + C(92, 96, 52, "a")
    holes = "".join(C(x, y, 8, "e") for x, y in [(78, 82), (106, 82), (78, 110), (106, 110)])
    thread = P("M78 82 L106 110 M106 82 L78 110", "n")
    small = C(160, 162, 26, "b") + C(160, 162, 18, "a") + C(153, 162, 4, "e") + C(167, 162, 4, "e")
    return big + holes + thread + small + P("M24 176 C40 160 60 186 80 170 C96 158 110 176 120 184", "n t")


def mushroom():
    """Field mushrooms (шампиньон) - plain caps, no spots."""
    stem = P("M80 112 C78 140 74 164 70 176 L124 176 C120 164 116 140 114 112 Z", "a")
    cap = P("M24 118 C24 62 60 34 98 34 C138 34 172 62 172 118 C146 128 50 128 24 118 Z", "b")
    gills = P("M42 120 C70 132 126 132 154 120", "n t")
    small_stem = P("M150 150 C150 162 148 172 146 178 L170 178 C168 172 166 162 166 150 Z", "a")
    small_cap = P("M134 154 C134 130 182 130 182 154 C170 160 146 160 134 154 Z", "b")
    grass = P("M20 182 L26 166 L32 182 M40 182 L44 170 L48 182 M126 182 L130 168 L134 182", "n t")
    return stem + cap + gills + small_stem + small_cap + grass + ground(182)


def rocket():
    body = P("M100 14 C130 40 138 82 132 142 L68 142 C62 82 70 40 100 14 Z", "a")
    fins = P("M70 100 L40 150 L68 142 Z", "b") + P("M130 100 L160 150 L132 142 Z", "b")
    nozzle = P("M80 142 L120 142 L114 156 L86 156 Z", "c")
    flame = P("M88 158 C82 172 92 182 100 194 C108 182 118 172 112 158 Z", "d")
    window = C(100, 76, 16, "c") + C(100, 76, 10, "e")
    band = P("M82 36 C94 42 106 42 118 36", "n") + L(100, 100, 100, 138, "n t")
    stars = star(36, 40, 9, None, "e") + star(166, 64, 7, None, "e") + star(160, 18, 5, None, "e") + star(30, 100, 5, None, "e")
    return fins + body + nozzle + flame + window + band + stars


def bagel():
    """Đevrek: a ring-shaped bread roll with sesame (ђеврек)."""
    plate = E(100, 156, 90, 22, "b")
    ring = E(100, 112, 76, 50, "c") + E(100, 106, 26, 14, "a")
    shade = P("M34 124 C60 156 140 156 166 124", "n t")
    seeds = "".join(E(x, y, 3, 1.8, "n t", r) for x, y, r in
                    [(52, 96, 20), (66, 82, -30), (86, 76, 10), (120, 76, -15), (138, 84, 30), (150, 100, -20),
                     (60, 118, 40), (142, 122, -40), (78, 134, 0), (120, 136, 15), (100, 134, -30), (44, 108, 0)])
    return plate + ring + shade + seeds


def nail():
    """Nails and a wooden board (ексер)."""
    board = R(16, 138, 168, 40, "b", 6)
    grain = P("M28 150 C60 146 90 156 120 150 M60 166 C90 160 130 170 170 164", "n t")
    standing = R(64, 44, 12, 94, "a") + E(70, 42, 24, 7, "c")
    lying = P("M118 118 L166 118 L180 124 L166 130 L118 130 Z", "a") + E(114, 124, 6, 16, "c")
    return board + grain + standing + lying


def lantern():
    """A hanging lantern (фењер)."""
    ring = C(100, 22, 10, "n") + L(100, 32, 100, 40, "n")
    cap = P("M64 64 L100 38 L136 64 Z", "b")
    glass = R(70, 64, 60, 78, "a", 6)
    frame = L(84, 64, 84, 142, "n t") + L(116, 64, 116, 142, "n t")
    candle = R(92, 114, 16, 24, "c", 2)
    flame = P("M100 84 C90 98 92 110 100 112 C108 110 110 98 100 84 Z", "d")
    base = P("M60 142 L140 142 L132 160 L68 160 Z", "b") + R(84, 160, 32, 10, "e", 3)
    glow = P("M44 92 L56 96 M40 116 L54 116 M156 92 L144 96 M160 116 L146 116", "n t")
    return ring + cap + glass + frame + candle + flame + base + glow


PICS = {"ru_fir": fir, "ru_blackberry": blackberry, "ru_acorn": acorn, "ru_scissors": scissors, "ru_iron": iron,
        "ru_bread": bread, "ru_popsicle": popsicle, "ru_button": button, "ru_mushroom": mushroom,
        "ru_rocket": rocket, "ru_bagel": bagel, "ru_nail": nail, "ru_lantern": lantern}
