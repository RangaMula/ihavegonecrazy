# -*- coding: utf-8 -*-
"""Hand-built SVG line art for the coloring pictures (viewBox 0 0 200 200).

House rule: objects, plants and nature only - no people, no animals, no faces.
Every closed shape carries a colour-role class (a, b, c, d, e) so the same drawing is
white-filled line art inside the book and full colour on the cover:
    .ill .a { fill: var(--a, #fff) }  ... and class "n" = no fill (open lines).
"""
import math

def P(d, cls="a", extra=""):
    return f'<path class="{cls}" d="{d}" {extra}/>'

def C(cx, cy, r, cls="a"):
    return f'<circle class="{cls}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'

def E(cx, cy, rx, ry, cls="a", rot=0):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse class="{cls}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"{t}/>'

def R(x, y, w, h, cls="a", rx=0):
    return f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'

def L(x1, y1, x2, y2, cls="n"):
    return f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'

def poly(pts, cls="a"):
    return f'<polygon class="{cls}" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}"/>'

def star_pts(cx, cy, R_, r, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        ang = math.radians(rot + i * 180 / n)
        rad = R_ if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return pts

def star(cx, cy, R_, r=None, cls="a", n=5):
    return poly(star_pts(cx, cy, R_, r or R_ * 0.45, n), cls)

def crescent(cx, cy, R_, dx, dy, r, cls="a"):
    """Outer circle (cx,cy,R) minus inner circle shifted by (dx,dy) with radius r."""
    ix, iy = cx + dx, cy + dy
    d = math.hypot(dx, dy)
    a = (R_ * R_ - r * r + d * d) / (2 * d)
    h = math.sqrt(max(R_ * R_ - a * a, 0))
    mx, my = cx + a * dx / d, cy + a * dy / d
    p1 = (mx + h * dy / d, my - h * dx / d)
    p2 = (mx - h * dy / d, my + h * dx / d)
    return P(f"M{p1[0]:.1f} {p1[1]:.1f} A{R_} {R_} 0 1 0 {p2[0]:.1f} {p2[1]:.1f} "
             f"A{r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f} Z", cls)

def cloud(x, y, s=1.0, cls="a"):
    # flat-bottomed puffy cloud, x,y = bottom-left
    w = 90 * s
    return P(f"M{x} {y} h{w} a{14*s} {14*s} 0 0 0 {-6*s} {-26*s} a{20*s} {20*s} 0 0 0 {-30*s} {-16*s} "
             f"a{24*s} {24*s} 0 0 0 {-40*s} {6*s} a{16*s} {16*s} 0 0 0 {-14*s} {36*s} z", cls)

def leaf(x, y, ang, size=22, cls="c"):
    return (f'<g transform="translate({x} {y}) rotate({ang})">'
            + P(f"M0 0 C{size*0.35} {-size*0.45} {size*0.8} {-size*0.4} {size} 0 "
                f"C{size*0.8} {size*0.4} {size*0.35} {size*0.45} 0 0 Z", cls)
            + L(0, 0, size * 0.85, 0, "n t") + "</g>")

def ground(y=182):
    return L(14, y, 186, y, "n")

# ---------------------------------------------------------------------------
def blocks(letters=("অ", "আ", "ক")):
    def cube(x, y, s, ch, cls):
        k = s * 0.32
        return (P(f"M{x} {y} l{k} {-k} h{s} l{-k} {k} z", "b")
                + P(f"M{x+s} {y} l{k} {-k} v{s} l{-k} {k} z", "c")
                + R(x, y, s, s, cls, 4)
                + f'<text x="{x+s/2}" y="{y+s*0.72}" text-anchor="middle" class="blk" '
                  f'font-size="{s*0.62}">{ch}</text>')
    return (cube(26, 118, 58, letters[0], "a") + cube(104, 118, 58, letters[1], "d")
            + cube(64, 58, 58, letters[2], "e") + ground(178))

def mango():
    return (P("M100 46 C150 42 178 92 164 136 C152 172 108 186 76 166 C44 146 42 98 58 72 C68 56 82 47 100 46 Z", "a")
            + P("M78 70 C70 90 70 120 84 142", "n t")
            + P("M100 46 C108 26 136 14 164 20 C150 40 124 48 100 46 Z", "c")
            + P("M104 44 C122 34 140 28 160 22", "n t")
            + P("M98 47 C96 38 94 32 90 26", "n"))

def iftar():
    dates = "".join(E(x, y, 14, 8, "b", r) for x, y, r in
                    [(60, 140, -15), (84, 134, 10), (106, 142, -5), (76, 150, 20), (100, 128, 25)])
    return (E(84, 150, 66, 20, "a") + E(84, 146, 50, 13, "n t") + dates
            + P("M146 82 L184 82 L178 166 L152 166 Z", "a") + P("M149 104 L181 104 L178 166 L152 166 Z", "d")
            + crescent(46, 54, 22, 10, -6, 19, "e") + star(84, 40, 9, 4, "e") + ground(174))

def eid():
    lantern = (L(100, 10, 100, 30) + C(100, 34, 5, "n")
               + P("M78 60 L100 40 L122 60 Z", "b") + R(74, 60, 52, 8, "b", 2)
               + P("M76 68 L124 68 L132 120 L100 140 L68 120 Z", "a")
               + P("M90 72 L90 124 M110 72 L110 124", "n t")
               + P("M86 140 L114 140 L108 152 L92 152 Z", "b") + L(100, 152, 100, 162))
    return (lantern + crescent(46, 66, 26, 12, -8, 22, "e") + star(158, 52, 13, 6, "e")
            + star(36, 150, 9, 4, "e") + star(166, 138, 8, 3.6, "e"))

def gift():
    return (R(36, 92, 128, 84, "a", 4) + R(28, 72, 144, 24, "b", 4)
            + R(90, 72, 20, 104, "c") + P("M100 72 C72 40 46 50 58 66 C66 76 88 74 100 72 Z", "c")
            + P("M100 72 C128 40 154 50 142 66 C134 76 112 74 100 72 Z", "c")
            + C(100, 72, 7, "d") + star(60, 130, 9, 4, "e") + star(140, 140, 9, 4, "e"))

def waves():
    sea = P("M14 120 C40 96 64 96 80 116 C70 102 88 92 100 104 C112 90 136 92 150 112 "
            "C140 98 160 90 186 104 L186 186 L14 186 Z", "b")
    sea2 = P("M14 150 C36 132 56 134 70 148 C62 138 78 130 90 140 C104 128 126 130 140 146 "
             "C132 136 152 128 186 140 L186 186 L14 186 Z", "c")
    sun = C(150, 48, 22, "d") + "".join(
        L(150 + 30 * math.cos(math.radians(a)), 48 + 30 * math.sin(math.radians(a)),
          150 + 40 * math.cos(math.radians(a)), 48 + 40 * math.sin(math.radians(a))) for a in range(0, 360, 45))
    return sun + cloud(26, 70, 0.7) + sea + sea2 + P("M30 170 q10 -8 20 0 M120 172 q10 -8 20 0", "n t")

def seasons():
    out = []
    cx, cy, r = 100, 100, 82
    icons = []
    for i in range(6):
        a0, a1 = math.radians(-90 + i * 60), math.radians(-30 + i * 60)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        cls = "abcdea"[i]
        out.append(P(f"M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f} Z", cls))
        am = math.radians(-60 + i * 60)
        icons.append((cx + 52 * math.cos(am), cy + 52 * math.sin(am)))
    (sx, sy), (rx, ry), (kx, ky), (hx, hy), (wx, wy), (fx, fy) = icons
    sun = C(sx, sy, 11) + "".join(L(sx + 14 * math.cos(math.radians(a)), sy + 14 * math.sin(math.radians(a)),
                                     sx + 20 * math.cos(math.radians(a)), sy + 20 * math.sin(math.radians(a)), "n t")
                                   for a in range(0, 360, 45))
    rain = cloud(rx - 22, ry + 2, 0.48) + "".join(L(rx - 14 + 10 * k, ry + 8, rx - 18 + 10 * k, ry + 16, "n t") for k in range(4))
    autumn = cloud(kx - 22, ky + 6, 0.5) + "".join(L(kx - 10 + 10 * k, ky + 10, kx - 10 + 10 * k, ky + 16, "n t") for k in range(3))
    harvest = "".join(P(f"M{hx-10+10*k} {hy+16} Q{hx-12+10*k} {hy} {hx-4+10*k} {hy-14}", "n t") +
                      E(hx - 4 + 10 * k, hy - 14, 3.5, 7, "a") for k in range(3))
    winter = "".join(L(wx + 16 * math.cos(math.radians(a)), wy + 16 * math.sin(math.radians(a)),
                       wx - 16 * math.cos(math.radians(a)), wy - 16 * math.sin(math.radians(a)), "n t") for a in (0, 60, 120))
    flower = "".join(C(fx + 9 * math.cos(math.radians(a)), fy + 9 * math.sin(math.radians(a)), 6) for a in range(0, 360, 72)) + C(fx, fy, 5, "d")
    return "".join(out) + sun + rain + autumn + harvest + winter + flower + C(cx, cy, 10, "e")

def one(digit="১"):
    return (P("M120 40 C152 40 170 64 166 92 C162 118 140 134 122 138 C104 134 84 118 80 92 C76 64 92 40 120 40 Z", "b")
            + P("M116 138 L128 138 L124 146 L120 146 Z", "b")
            + P("M122 146 C112 160 132 170 120 190", "n")
            + P("M100 62 C96 70 96 80 98 88", "n t")
            + (f'<text x="56" y="168" text-anchor="middle" class="big" font-size="120">{digit}</text>' if digit else ""))

def star_pic():
    return (star(100, 100, 70, 30, "d") + star(100, 100, 40, 17, "e")
            + star(36, 40, 12, 5, "d") + star(166, 36, 10, 4.5, "d") + star(170, 160, 12, 5, "d")
            + star(30, 160, 9, 4, "d") + C(54, 108, 4) + C(150, 104, 4) + C(100, 178, 4))

def scarf():
    return (P("M100 18 L100 30", "n") + C(100, 14, 5, "n")
            + P("M100 30 L30 66 L170 66 Z", "n")
            + P("M44 60 C40 100 54 140 48 168 L86 168 C92 130 82 92 96 62 Z", "b")
            + P("M156 60 C162 104 146 140 154 172 L116 172 C110 132 120 92 104 62 Z", "c")
            + P("M96 62 L104 62 C118 76 82 76 96 62 Z", "a")
            + "".join(L(50 + 6 * k, 168, 50 + 6 * k, 182, "n t") for k in range(7))
            + "".join(L(118 + 6 * k, 172, 118 + 6 * k, 186, "n t") for k in range(7))
            + P("M52 100 C60 104 72 104 80 100 M54 130 C62 134 74 134 82 130", "n t")
            + P("M122 104 C130 108 142 108 150 104 M120 134 C128 138 140 138 148 134", "n t"))

def medicine():
    return (R(46, 34, 52, 18, "c", 4) + P("M50 52 L94 52 L104 72 L104 168 L40 168 L40 72 Z", "a")
            + R(48, 96, 48, 44, "b", 4) + R(66, 104, 12, 28, "d") + R(58, 112, 28, 12, "d")
            + f'<g transform="rotate(-30 146 120)">' + R(120, 108, 52, 24, "a", 12)
            + P("M146 108 L158 108 A12 12 0 0 1 158 132 L146 132 Z", "e") + "</g>"
            + f'<g transform="rotate(20 150 166)">' + R(128, 156, 44, 20, "a", 10)
            + P("M150 156 L162 156 A10 10 0 0 1 162 176 L150 176 Z", "c") + "</g>" + ground(184))

def banana():
    one_b = lambda dx, dy, rot, cls: (f'<g transform="translate({dx} {dy}) rotate({rot} 100 100)">'
        + P("M40 70 C50 140 120 170 168 130 C150 136 110 140 82 112 C66 96 56 80 52 64 Z", cls)
        + P("M56 80 C76 122 120 146 160 134", "n t") + "</g>")
    return (one_b(0, 20, 0, "d") + one_b(-6, 2, -12, "d") + one_b(-8, -16, -24, "d")
            + P("M40 74 L30 52 L42 48 L52 70 Z", "c"))

def dates():
    ds = "".join(E(x, y, 13, 19, "b", r) + P(f"M{x-4} {y-12} C{x-7} {y-2} {x-7} {y+6} {x-3} {y+12}", "n t")
                 for x, y, r in [(70, 92, -20), (98, 84, 0), (126, 92, 20), (84, 108, -8), (114, 108, 10)])
    bowl = P("M24 104 L176 104 C172 150 140 176 100 176 C60 176 28 150 24 104 Z", "a") \
        + P("M40 128 C80 138 120 138 160 128", "n t") + E(100, 176, 30, 6, "c")
    return ds + bowl + leaf(150, 64, -40, 30) + leaf(52, 64, 220, 30)

def tree():
    return (P("M88 186 L92 120 L76 100 M92 120 L110 100 M108 186 L106 120", "n")
            + P("M86 186 C90 160 92 130 90 110 L112 110 C108 130 110 160 116 186 Z", "b")
            + P("M100 18 C128 16 144 34 140 50 C164 52 176 76 164 94 C176 110 160 132 138 126 "
                "C130 142 104 146 92 132 C76 146 46 140 46 118 C24 112 22 86 40 78 C30 56 50 36 70 40 C76 24 88 18 100 18 Z", "c")
            + C(70, 80, 7, "d") + C(120, 64, 7, "d") + C(140, 102, 7, "d") + C(88, 108, 7, "d") + C(104, 86, 7, "d")
            + P("M60 186 C70 176 80 176 86 186 M116 186 C124 176 136 176 142 186", "n t") + ground(186))

def clock():
    ticks = "".join(L(100 + 46 * math.cos(math.radians(a)), 108 + 46 * math.sin(math.radians(a)),
                      100 + 54 * math.cos(math.radians(a)), 108 + 54 * math.sin(math.radians(a)), "n t")
                    for a in range(0, 360, 30))
    return (P("M58 160 L44 182 M142 160 L156 182", "n")
            + P("M52 50 A26 26 0 0 1 84 34 Z", "b") + P("M148 50 A26 26 0 0 0 116 34 Z", "b")
            + L(100, 34, 100, 46) + R(90, 26, 20, 10, "b", 3)
            + C(100, 108, 66, "c") + C(100, 108, 58, "a") + ticks
            + P("M100 108 L100 70 M100 108 L128 120", "n") + C(100, 108, 5, "d"))

def grapes():
    pos = [(70, 78), (96, 74), (122, 78), (58, 102), (84, 100), (110, 100), (136, 102),
           (72, 124), (98, 124), (124, 124), (86, 148), (112, 148), (100, 170)]
    return (P("M98 60 C96 46 100 32 110 22", "n") + leaf(104, 40, -20, 46)
            + "".join(C(x, y, 14, "b") + P(f"M{x-6} {y-6} q3 -3 7 -2", "n t") for x, y in pos))

def glasses():
    return (P("M18 90 L40 82", "n") + P("M182 90 L160 82", "n")
            + R(30, 80, 62, 50, "b", 22) + R(108, 80, 62, 50, "b", 22)
            + P("M92 96 C96 88 104 88 108 96", "n")
            + P("M40 96 l14 -8 M46 110 l20 -14 M118 96 l14 -8 M124 110 l20 -14", "n t")
            + P("M18 90 L14 140", "n") + P("M182 90 L186 140", "n"))

def umbrella():
    sc = "".join(f"a{17} {14} 0 0 0 {-34} 0 " for _ in range(5))
    canopy = P(f"M15 100 C20 48 64 24 100 24 C136 24 180 48 185 100 {sc} Z".replace(f"185 100 a", "185 100 a"), "b")
    ribs = P("M100 24 C86 50 82 76 83 100 M100 24 C114 50 118 76 117 100 M100 24 C60 40 46 70 49 100 M100 24 C140 40 154 70 151 100", "n t")
    return (canopy + ribs + P("M100 20 L100 12", "n") + P("M100 100 L100 166 C100 186 72 186 72 166", "n")
            + "".join(P(f"M{x} {y} q-3 6 0 10 q3 -4 0 -10", "c") for x, y in [(30, 130), (160, 140), (40, 170), (150, 176)]))

def ship():
    return (P("M18 118 L182 118 L158 156 L42 156 Z", "b") + R(52, 84, 90, 34, "a", 3)
            + R(68, 58, 56, 26, "a", 3) + R(130, 40, 18, 44, "c", 2) + R(128, 36, 22, 8, "e")
            + C(70, 100, 6) + C(96, 100, 6) + C(122, 100, 6) + R(80, 64, 12, 12, "d", 2) + R(100, 64, 12, 12, "d", 2)
            + C(146, 24, 8, "n") + C(160, 16, 6, "n") + L(30, 126, 170, 126, "n t")
            + P("M14 172 q14 -10 28 0 t28 0 t28 0 t28 0 t28 0 t28 0", "n"))

def basket():
    weave = "".join(L(40 + 15 * k, 96, 48 + 13 * k, 176, "n t") for k in range(9))
    rows = "".join(P(f"M{34+2*k*2} {108+18*k} C80 {114+18*k} 120 {114+18*k} {166-2*k*2} {108+18*k}", "n t") for k in range(4))
    return (P("M44 96 C44 30 156 30 156 96", "n") + P("M54 96 C54 44 146 44 146 96", "n")
            + P("M24 96 L176 96 L160 176 L40 176 Z", "b") + R(20, 88, 160, 14, "c", 7) + weave + rows
            + C(76, 82, 12, "d") + C(98, 78, 12, "e") + C(122, 84, 12, "d"))

def engine():
    return (R(40, 92, 92, 52, "b", 6) + R(126, 60, 52, 84, "c", 4) + R(120, 52, 64, 12, "a", 3)
            + R(138, 72, 28, 26, "a", 3) + R(56, 60, 20, 32, "a", 2) + R(52, 52, 28, 10, "d", 2)
            + C(46, 40, 8, "n") + C(30, 28, 6, "n") + C(20, 14, 4, "n")
            + P("M40 144 L18 160 L40 160 Z", "e") + R(28, 140, 156, 10, "a", 3)
            + C(66, 160, 16, "d") + C(108, 160, 16, "d") + C(156, 160, 16, "d")
            + C(66, 160, 4) + C(108, 160, 4) + C(156, 160, 4) + L(66, 160, 156, 160)
            + L(14, 182, 186, 182) + "".join(R(18 + 22 * k, 182, 12, 6, "n t") for k in range(8)))

def tomato():
    return (P("M100 60 C150 52 182 88 172 126 C162 166 124 180 100 178 C76 180 38 166 28 126 C18 88 50 52 100 60 Z", "e")
            + P("M60 84 C52 100 52 118 58 132", "n t")
            + poly(star_pts(100, 62, 30, 9, 5), "c") + P("M100 58 C100 46 104 38 112 32", "n"))

def cart():
    return (R(40, 66, 40, 34, "b", 2) + R(84, 56, 44, 44, "d", 2) + R(132, 72, 30, 28, "e", 2)
            + L(84, 78, 128, 78, "n t") + L(106, 56, 106, 100, "n t")
            + R(26, 100, 148, 14, "a", 3) + P("M174 106 L190 96 M26 106 L10 96", "n")
            + C(62, 140, 24, "c") + C(62, 140, 6) + C(140, 140, 24, "c") + C(140, 140, 6)
            + "".join(L(62 + 18 * math.cos(math.radians(a)), 140 + 18 * math.sin(math.radians(a)), 62, 140, "n t") +
                      L(140 + 18 * math.cos(math.radians(a)), 140 + 18 * math.sin(math.radians(a)), 140, 140, "n t")
                      for a in range(0, 360, 60))
            + L(62, 114, 62, 116) + L(140, 114, 140, 116) + ground(166))

def egg():
    return (P("M80 30 C108 30 126 76 124 104 C122 128 104 140 80 140 C56 140 38 128 36 104 C34 76 52 30 80 30 Z", "a")
            + P("M44 108 L116 108 C114 128 100 140 80 140 C60 140 46 128 44 108 Z", "b")
            + P("M52 140 L108 140 L100 150 L60 150 Z", "b") + P("M54 150 L106 150 L112 166 L48 166 Z", "b")
            + P("M152 104 C168 104 180 126 178 146 C176 162 166 172 148 172 C130 172 120 162 118 146 C116 126 136 104 152 104 Z", "a")
            + P("M58 54 C54 62 52 72 52 80", "n t") + ground(172))

def shield():
    s = P("M100 20 L170 40 C172 104 150 152 100 182 C50 152 28 104 30 40 Z", "b")
    s2 = P("M100 34 L156 50 C156 102 138 140 100 164 C62 140 44 102 44 50 Z", "a")
    return s + s2 + star(100, 96, 34, 22, "d", 8) + C(100, 96, 12, "e")

def salt(label="লবণ"):
    holes = "".join(C(x, y, 2.6, "n") for x, y in [(78, 44), (90, 40), (102, 44), (84, 54), (96, 54)])
    return (P("M66 60 C66 36 114 36 114 60 Z", "c") + holes
            + P("M62 60 L118 60 L124 160 L56 160 Z", "a") + R(60, 96, 60, 36, "b", 4)
            + f'<text x="90" y="124" text-anchor="middle" class="lbl" font-size="20">{label}</text>'
            + P("M128 172 C136 150 160 150 170 172 Z", "a")
            + "".join(C(x, y, 1.8, "n") for x, y in [(140, 162), (150, 158), (158, 166), (146, 168), (134, 168)]) + ground(172))

def watermelon():
    whole = (E(62, 120, 50, 40, "c") + P("M24 112 C40 104 50 140 62 160 M40 90 C56 96 66 130 74 158 M70 82 C80 96 90 120 96 146", "n t"))
    sl = (P("M96 120 L184 120 C184 160 160 182 140 182 C120 182 96 160 96 120 Z", "c")
          + P("M104 120 L176 120 C176 154 158 172 140 172 C122 172 104 154 104 120 Z", "e")
          + "".join(E(x, y, 3, 5, "n") for x, y in [(124, 136), (140, 132), (156, 136), (132, 152), (150, 152), (140, 162)]))
    tri = (P("M120 40 L176 40 L148 98 Z", "e") + P("M118 36 L178 36 L176 44 L120 44 Z", "c")
           + E(140, 56, 2.5, 4, "n") + E(156, 56, 2.5, 4, "n") + E(148, 72, 2.5, 4, "n"))
    return whole + sl + tri + ground(186)

def plate():
    rim = "".join(C(100 + 72 * math.cos(math.radians(a)), 100 + 72 * math.sin(math.radians(a)), 4, "e") for a in range(0, 360, 20))
    return (C(100, 100, 84, "b") + C(100, 100, 60, "a") + rim
            + star(100, 100, 30, 18, "d", 8) + C(100, 100, 9, "c"))

def door():
    return (R(20, 170, 160, 14, "c", 2) + R(30, 158, 140, 12, "c", 2)
            + P("M44 158 L44 74 C44 38 72 20 100 14 C128 20 156 38 156 74 L156 158 Z", "b")
            + P("M58 158 L58 80 C58 52 80 38 100 32 C120 38 142 52 142 80 L142 158 Z", "a")
            + L(100, 32, 100, 158) + R(66, 92, 26, 24, "d", 3) + R(108, 92, 26, 24, "d", 3)
            + R(66, 124, 26, 26, "d", 3) + R(108, 124, 26, 26, "d", 3) + C(94, 118, 4, "e") + C(106, 118, 4, "e"))

def paddy():
    def stalk(x, h, bend, cls):
        head = "".join(E(x + bend * 0.6 + 6 * k * (1 if bend > 0 else -1) * 0.5, 186 - h + 10 + 10 * k, 4, 7, cls,
                         25 if bend > 0 else -25) for k in range(5))
        return (P(f"M{x} 186 C{x} {186-h*0.5} {x+bend*0.3} {186-h*0.9} {x+bend} {186-h+8}", "n")
                + P(f"M{x} 186 C{x-14} {150} {x-24} {140} {x-30} {128}", "n t") + head)
    return (C(160, 36, 16, "d") + cloud(24, 54, 0.6)
            + stalk(50, 110, 22, "b") + stalk(84, 130, 26, "b") + stalk(118, 118, 24, "b") + stalk(150, 100, 20, "b")
            + P("M14 186 L186 186 L186 196 L14 196 Z", "c"))

def boat():
    return (P("M14 112 C40 136 160 136 186 112 C176 150 140 160 100 160 C60 160 24 150 14 112 Z", "b")
            + P("M54 120 C54 92 126 92 126 120 Z", "c") + P("M66 120 C66 102 114 102 114 120", "n t")
            + L(140, 128, 140, 30) + P("M144 34 C170 54 172 92 146 116 Z", "a")
            + L(144, 60, 166, 66, "n t") + L(144, 88, 166, 90, "n t")
            + P("M10 172 q15 -10 30 0 t30 0 t30 0 t30 0 t30 0 t30 0", "n") + C(40, 40, 16, "d"))

def flag():
    return (R(32, 16, 8, 170, "c", 3) + C(36, 14, 6, "d")
            + P("M40 30 L176 30 L176 112 L40 112 Z", "c") + C(100, 71, 26, "e")
            + R(20, 180, 32, 8, "a", 2))

def flower():
    pet = "".join(E(100 + 26 * math.cos(math.radians(a)), 70 + 26 * math.sin(math.radians(a)), 16, 24, "e", a + 90) for a in range(0, 360, 60))
    return (P("M100 96 C98 130 104 160 100 186", "n") + leaf(100, 150, -150, 40) + leaf(102, 130, -30, 40)
            + pet + C(100, 70, 16, "d") + "".join(C(100 + 6 * math.cos(math.radians(a)), 70 + 6 * math.sin(math.radians(a)), 1.6, "n") for a in range(0, 360, 60))
            + P("M60 186 C70 172 80 172 88 186 M112 186 C120 172 132 172 140 186", "n t") + ground(186))

def book(left="অ আ ই", right="ক খ গ"):
    lines = "".join(L(40, 82 + 14 * k, 92, 86 + 14 * k, "n t") + L(108, 86 + 14 * k, 160, 82 + 14 * k, "n t") for k in range(5))
    return (P("M100 60 C80 48 46 46 24 54 L24 160 C46 152 80 154 100 166 Z", "a")
            + P("M100 60 C120 48 154 46 176 54 L176 160 C154 152 120 154 100 166 Z", "a")
            + P("M24 160 L24 170 C46 162 80 164 100 176 C120 164 154 162 176 170 L176 160", "b")
            + L(100, 60, 100, 166) + lines
            + f'<text x="66" y="76" text-anchor="middle" class="lbl" font-size="16">{left}</text>'
            + f'<text x="134" y="76" text-anchor="middle" class="lbl" font-size="16">{right}</text>')

def rice():
    return (P("M44 98 C44 60 80 44 100 44 C120 44 156 60 156 98 Z", "a")
            + "".join(E(x, y, 3.5, 2, "n", r) for x, y, r in [(70, 76, 20), (86, 64, -10), (104, 58, 30), (122, 68, 0),
                                                               (136, 84, -20), (96, 82, 10), (114, 86, 40), (80, 90, -30)])
            + P("M26 98 L174 98 C170 140 140 164 100 164 C60 164 30 140 26 98 Z", "b")
            + P("M40 118 C80 128 120 128 160 118", "n t") + E(100, 166, 30, 7, "c")
            + P("M78 36 c-6 -8 6 -14 0 -22 M100 34 c-6 -8 6 -14 0 -22 M122 36 c-6 -8 6 -14 0 -22", "n t")
            + E(166, 160, 12, 5, "a", -20) + P("M156 150 L186 128", "n"))

def mosque():
    return (R(14, 170, 172, 14, "c", 2)
            + R(24, 70, 22, 100, "b", 2) + P("M22 70 L35 46 L48 70 Z", "d") + L(35, 46, 35, 36) + C(35, 32, 3, "e")
            + R(154, 70, 22, 100, "b", 2) + P("M152 70 L165 46 L178 70 Z", "d") + L(165, 46, 165, 36) + C(165, 32, 3, "e")
            + R(54, 100, 92, 70, "a", 2)
            + P("M58 100 C58 64 80 50 100 46 C120 50 142 64 142 100 Z", "d")
            + L(100, 46, 100, 30) + crescent(100, 22, 9, 4, -3, 7.5, "e")
            + P("M84 170 L84 136 C84 124 92 118 100 116 C108 118 116 124 116 136 L116 170 Z", "e")
            + P("M64 134 L64 118 C64 112 70 108 74 108 C78 108 82 112 82 118 L82 134 Z", "c")
            + P("M118 134 L118 118 C118 112 122 108 126 108 C130 108 136 112 136 118 L136 134 Z", "c")
            + R(28, 90, 14, 14, "a", 7) + R(158, 90, 14, 14, "a", 7))

def tools():
    hammer = (f'<g transform="rotate(-35 100 100)">' + R(92, 70, 16, 110, "b", 5)
              + P("M52 50 L148 50 L148 76 L60 76 C54 76 48 66 52 50 Z", "c") + R(120, 50, 10, 26, "n t") + "</g>")
    wrench = (f'<g transform="rotate(35 100 100)">' + R(91, 64, 18, 112, "d", 6)
              + P("M100 26 C120 26 132 42 128 60 L112 50 L106 66 L94 66 L88 50 L72 60 C68 42 80 26 100 26 Z", "d")
              + C(100, 160, 6) + "</g>")
    screws = "".join(C(x, y, 7, "e") + L(x - 4, y, x + 4, y, "n t") for x, y in [(30, 176), (54, 182), (170, 178)])
    return hammer + wrench + screws

def rainbow():
    bands = "".join(P(f"M{30+12*k} 150 A{70-12*k} {70-12*k} 0 0 1 {170-12*k} 150 L{158-12*k} 150 "
                      f"A{58-12*k} {58-12*k} 0 0 0 {42+12*k} 150 Z", "abcde"[k]) for k in range(5))
    return C(160, 40, 16, "d") + bands + cloud(4, 168, 0.62) + cloud(128, 168, 0.62) + "".join(
        L(100 + 0, 0, 0, 0, "n") for _ in range(0))

def top():
    return (P("M60 60 C60 40 140 40 140 60 L106 166 L94 166 Z", "b")
            + P("M60 60 C60 76 140 76 140 60", "n") + E(100, 58, 40, 14, "e")
            + P("M70 84 C88 92 112 92 130 84 M80 112 C92 118 108 118 120 112 M90 140 C96 143 104 143 110 140", "n t")
            + R(94, 24, 12, 22, "c", 4) + P("M100 166 L100 180", "n")
            + P("M106 30 C130 10 160 20 170 40 C178 58 160 70 150 60", "n t")
            + P("M40 176 C70 186 130 186 160 176", "n t") + P("M30 120 L44 120 M24 140 L40 140 M160 120 L174 120", "n t"))

def lily():
    pet = "".join(P(f"M100 116 C{100+38*math.cos(math.radians(a-22)):.1f} {116+38*math.sin(math.radians(a-22)):.1f} "
                    f"{100+60*math.cos(math.radians(a)):.1f} {116+60*math.sin(math.radians(a)):.1f} "
                    f"{100+60*math.cos(math.radians(a)):.1f} {116+60*math.sin(math.radians(a)):.1f} "
                    f"C{100+60*math.cos(math.radians(a)):.1f} {116+60*math.sin(math.radians(a)):.1f} "
                    f"{100+38*math.cos(math.radians(a+22)):.1f} {116+38*math.sin(math.radians(a+22)):.1f} 100 116 Z", "e")
                  for a in [-160, -130, -100, -80, -50, -20])
    return (P("M14 140 C40 126 160 126 186 140 C176 164 24 164 14 140 Z", "c")
            + P("M100 136 L130 150", "n t") + pet + C(100, 112, 12, "d")
            + P("M14 178 q15 -8 30 0 t30 0 t30 0 t30 0 t30 0 t30 0", "n"))

def hexagon():
    def hexp(cx, cy, r, cls):
        return poly([(cx + r * math.cos(math.radians(60 * k)), cy + r * math.sin(math.radians(60 * k))) for k in range(6)], cls)
    r = 30
    pts = [(0, 0), (1.5 * r, 0.866 * r), (1.5 * r, -0.866 * r), (-1.5 * r, 0.866 * r), (-1.5 * r, -0.866 * r), (0, 1.732 * r), (0, -1.732 * r)]
    return "".join(hexp(100 + x, 100 + y, r - 2, "abcdeab"[i]) for i, (x, y) in enumerate(pts)) + hexp(100, 100, 12, "e")

def sun():
    rays = "".join(poly([(100 + 52 * math.cos(math.radians(a - 9)), 100 + 52 * math.sin(math.radians(a - 9))),
                         (100 + 86 * math.cos(math.radians(a)), 100 + 86 * math.sin(math.radians(a))),
                         (100 + 52 * math.cos(math.radians(a + 9)), 100 + 52 * math.sin(math.radians(a + 9)))], "e")
                   for a in range(0, 360, 30))
    return rays + C(100, 100, 50, "d") + C(100, 100, 34, "a")

def pot():
    return (P("M62 46 L138 46 L132 62 L68 62 Z", "c") + R(56, 38, 88, 12, "c", 6)
            + P("M70 62 C30 76 22 126 50 154 C70 172 130 172 150 154 C178 126 170 76 130 62 Z", "b")
            + P("M36 104 C70 116 130 116 164 104 M40 126 C72 138 128 138 160 126", "n")
            + "".join(C(x, 115, 4, "d") for x in (52, 76, 100, 124, 148))
            + E(100, 176, 52, 9, "c") + P("M80 30 c-6 -8 6 -14 0 -22 M120 30 c-6 -8 6 -14 0 -22", "n t"))

def mountain():
    return (C(150, 44, 18, "d")
            + P("M10 180 L74 64 L120 140 L140 110 L190 180 Z", "b")
            + P("M74 64 L60 90 L70 86 L78 96 L86 84 L94 92 Z", "a")
            + P("M140 110 L130 126 L138 124 L144 132 L150 122 L156 126 Z", "a")
            + P("M60 180 C80 160 76 140 92 130", "n t") + cloud(16, 56, 0.55) + ground(180))

def raincloud():
    drops = "".join(P(f"M{x} {y} q-6 10 0 14 q6 -4 0 -14", "c") for x, y in
                    [(52, 110), (78, 124), (104, 110), (130, 124), (156, 110), (64, 146), (116, 148), (146, 150)])
    return (P("M24 96 h152 a20 20 0 0 0 -10 -38 a30 30 0 0 0 -46 -24 a36 36 0 0 0 -62 8 a24 24 0 0 0 -34 54 z", "b")
            + drops + P("M20 180 C60 170 140 170 180 180 C140 190 60 190 20 180 Z", "c"))

def prayermat():
    border = "".join(R(42 + 18 * k, 168, 8, 8, "n t") for k in range(7))
    return (R(34, 14, 132, 172, "b", 4) + R(44, 24, 112, 152, "a", 3)
            + P("M58 160 L58 80 C58 52 78 40 100 34 C122 40 142 52 142 80 L142 160 Z", "c")
            + P("M72 160 L72 86 C72 66 86 56 100 52 C114 56 128 66 128 86 L128 160 Z", "a")
            + star(100, 98, 16, 9, "d", 8) + R(84, 128, 32, 22, "e", 2)
            + "".join(L(34 + 12 * k, 186, 34 + 12 * k, 196, "n t") for k in range(12))
            + "".join(L(34 + 12 * k, 4, 34 + 12 * k, 14, "n t") for k in range(12)) + border)

def bulb():
    return (P("M100 20 C138 20 160 50 156 82 C152 106 132 118 126 140 L74 140 C68 118 48 106 44 82 C40 50 62 20 100 20 Z", "d")
            + P("M84 140 L84 104 L92 92 L100 104 L108 92 L116 104 L116 140", "n t")
            + R(74, 140, 52, 12, "c", 3) + R(76, 152, 48, 10, "c", 3) + R(80, 162, 40, 10, "c", 3)
            + P("M90 172 L110 172 L104 182 L96 182 Z", "b")
            + P("M60 50 C56 58 54 68 56 78", "n t")
            + P("M168 108 L150 140 L164 140 L148 176 L182 130 L166 130 L180 108 Z", "e")
            + P("M20 40 L34 50 M14 80 L30 82 M180 40 L166 50", "n t"))

def palette():
    return (P("M100 30 C150 30 186 60 182 100 C178 130 150 132 140 124 C128 116 116 124 120 140 "
              "C124 158 110 172 90 170 C46 168 18 136 20 100 C22 60 56 30 100 30 Z", "a")
            + E(126, 140, 10, 8, "n")
            + C(64, 70, 13, "b") + C(100, 56, 13, "c") + C(140, 66, 13, "d") + C(160, 98, 11, "e") + C(52, 112, 13, "a")
            + f'<g transform="rotate(40 120 150)">' + R(114, 96, 12, 80, "b", 5) + P("M114 96 L126 96 L120 70 Z", "e") + "</g>")

def sunrise():
    rays = "".join(L(100 + 54 * math.cos(math.radians(a)), 130 + 54 * math.sin(math.radians(a)),
                     100 + 80 * math.cos(math.radians(a)), 130 + 80 * math.sin(math.radians(a))) for a in range(-170, -9, 20))
    return (rays + P("M56 130 A44 44 0 0 1 144 130 Z", "d")
            + P("M10 130 C50 112 80 120 100 130 C120 120 150 110 190 128 L190 186 L10 186 Z", "c")
            + P("M10 156 C60 140 140 140 190 156 L190 186 L10 186 Z", "b")
            + cloud(14, 60, 0.5) + cloud(128, 48, 0.55))

def moon():
    return (crescent(92, 96, 64, 30, -20, 56, "d")
            + star(156, 46, 13, 6, "d") + star(166, 120, 9, 4, "d") + star(40, 170, 8, 3.6, "d")
            + cloud(100, 186, 0.9, "a"))

PICS = dict(blocks=blocks, mango=mango, iftar=iftar, eid=eid, gift=gift, waves=waves, seasons=seasons,
            one=one, star=star_pic, scarf=scarf, medicine=medicine, banana=banana, dates=dates, tree=tree,
            clock=clock, grapes=grapes, glasses=glasses, umbrella=umbrella, ship=ship, basket=basket,
            engine=engine, tomato=tomato, cart=cart, egg=egg, shield=shield, salt=salt,
            watermelon=watermelon, plate=plate, door=door, paddy=paddy, boat=boat, flag=flag,
            flower=flower, book=book, rice=rice, mosque=mosque, tools=tools, rainbow=rainbow, top=top,
            lily=lily, hexagon=hexagon, sun=sun, pot=pot, mountain=mountain, raincloud=raincloud,
            prayermat=prayermat, bulb=bulb, palette=palette, sunrise=sunrise, moon=moon)

def svg(key, cls="ill", style="", **args):
    st = f' style="{style}"' if style else ""
    return (f'<svg class="{cls}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"{st}>'
            f'{PICS[key](**args)}</svg>')


# ===========================================================================================
# Library additions for the other South Asian books (Hindi, Urdu, ...).  Same rules: objects,
# plants and nature only.
# ===========================================================================================
def pomegranate():
    crown = poly([(86, 52), (90, 36), (96, 48), (100, 32), (104, 48), (110, 36), (114, 52)], "e")
    seeds = "".join(E(x, y, 4, 5.5, "e", 20) for x, y in
                    [(150, 140), (162, 150), (140, 154), (154, 162), (166, 136), (144, 168), (132, 142)])
    return (P("M100 50 C146 46 168 84 162 120 C156 156 128 176 100 176 C72 176 44 156 38 120 C32 84 54 54 100 50 Z", "e")
            + crown + P("M62 92 C56 106 56 122 62 134", "n t")
            + P("M120 178 C120 130 150 116 184 124 C186 160 160 184 120 178 Z", "a")
            + P("M126 174 C128 136 152 126 178 130 C178 158 158 176 126 174 Z", "d") + seeds)

def tamarind():
    def pod(dy, rot, cls):
        return (f'<g transform="translate(0 {dy}) rotate({rot} 100 100)">'
                + P("M20 96 C30 80 44 92 56 84 C68 76 80 90 94 82 C108 74 120 90 134 82 C148 74 166 84 178 100 "
                    "C168 116 150 106 136 114 C122 122 108 108 94 116 C80 124 68 110 56 116 C44 122 30 112 20 96 Z", cls)
                + P("M56 86 L56 114 M94 84 L94 114 M134 84 L134 112", "n t") + "</g>")
    return pod(-40, -8, "b") + pod(10, 4, "c") + pod(60, -4, "b") + P("M178 100 L190 92", "n")

def wool():
    lines = "".join(P(f"M{60+k*8} {60+k*4} C{90+k*6} {80+k*10} {96+k*4} {120+k*6} {80+k*10} {160-k*2}", "n t") for k in range(5))
    return (C(96, 112, 64, "e") + lines + P("M60 120 C90 108 130 108 156 124 M52 96 C84 84 124 86 150 100", "n t")
            + P("M150 150 C170 166 176 180 186 186", "n")
            + f'<g transform="rotate(-25 150 60)">' + R(146, 10, 8, 110, "c", 4) + C(150, 10, 8, "d") + "</g>"
            + f'<g transform="rotate(20 170 60)">' + R(166, 10, 8, 110, "c", 4) + C(170, 10, 8, "d") + "</g>")

def mortar():
    return (f'<g transform="rotate(30 120 70)">' + R(108, 6, 24, 112, "c", 12) + "</g>"
            + P("M30 92 L170 92 C168 140 140 168 100 168 C60 168 32 140 30 92 Z", "b")
            + E(100, 92, 70, 12, "a") + P("M64 168 L136 168 L144 184 L56 184 Z", "b")
            + P("M44 120 C80 130 120 130 156 120", "n t"))

def pen():
    return (f'<g transform="rotate(-40 100 100)">'
            + R(88, 10, 24, 120, "b", 6) + R(88, 46, 24, 10, "d")
            + P("M88 130 L112 130 L100 172 Z", "c") + L(100, 140, 100, 160, "n t") + C(100, 140, 3, "n") + "</g>"
            + P("M126 148 L174 148 L180 186 L120 186 Z", "e") + R(132, 136, 36, 14, "d", 3)
            + P("M24 186 C40 176 56 186 72 176 C88 166 100 180 110 176", "n t"))

def carrot():
    return (P("M120 50 C140 60 146 80 136 96 L56 182 C50 188 42 182 46 176 L98 64 C104 50 112 46 120 50 Z", "e")
            + P("M92 96 L108 104 M80 122 L96 128 M68 148 L82 152", "n t")
            + P("M122 52 C116 30 120 14 128 6 C134 22 132 40 126 52 Z", "c")
            + P("M126 54 C136 34 152 24 166 22 C160 40 146 52 130 58 Z", "c")
            + P("M130 60 C150 50 170 52 182 60 C166 70 148 70 132 66 Z", "c"))

def broom():
    strands = "".join(P(f"M{96+k*2} 96 C{90+k*6} 130 {40+k*16} 160 {30+k*17} 186", "n t") for k in range(9))
    return (P("M86 96 C70 130 40 160 24 188 L178 188 C160 160 126 130 112 96 Z", "c") + strands
            + R(88, 14, 22, 86, "b", 8) + R(84, 60, 30, 10, "d", 3) + R(84, 84, 30, 10, "d", 3))

def fig():
    seeds = "".join(C(x, y, 2.2, "n") for x, y in [(146, 136), (154, 146), (140, 150), (160, 132), (148, 160), (136, 140), (156, 158)])
    return (P("M78 36 C84 52 112 70 116 104 C120 140 100 168 72 168 C44 168 24 140 30 104 C36 70 70 52 78 36 Z", "e")
            + P("M78 36 L82 22", "n") + leaf(84, 30, -40, 34)
            + P("M148 96 C168 104 182 128 178 150 C174 172 158 182 148 182 C138 182 122 172 118 150 C114 128 128 104 148 96 Z", "a")
            + P("M148 104 C164 112 172 132 170 150 C166 168 156 174 148 174 C140 174 128 168 126 150 C124 132 132 112 148 104 Z", "d") + seeds)

def envelope():
    return (R(24, 58, 152, 104, "a", 6) + P("M24 64 L100 120 L176 64", "n") + P("M24 162 L80 112 M176 162 L120 112", "n t")
            + R(132, 70, 32, 36, "d", 2) + R(138, 76, 20, 24, "e", 2)
            + P("M40 140 L70 140 M40 150 L84 150", "n t"))

def jar():
    return (P("M64 70 L136 70 C164 90 168 140 150 168 C140 182 60 182 50 168 C32 140 36 90 64 70 Z", "b")
            + R(56, 54, 88, 18, "c", 6) + P("M76 54 C76 38 124 38 124 54 Z", "c") + C(100, 34, 7, "d")
            + P("M44 118 C80 128 120 128 156 118", "n t") + R(78, 106, 44, 34, "a", 4) + ground(186))

def bowarrow():
    return (P("M60 20 C130 50 130 150 60 180", "n") + P("M66 20 C124 54 124 146 66 180", "n t")
            + L(60, 20, 60, 180, "n t")
            + L(30, 100, 168, 100) + P("M168 100 L146 88 L152 100 L146 112 Z", "c")
            + P("M30 100 L18 88 L36 88 L46 100 L36 112 L18 112 Z", "e"))

def kite():
    bows = "".join(P(f"M{x} {y} l-10 -6 l0 12 z M{x} {y} l10 -6 l0 12 z", "e") for x, y in [(100, 150), (88, 172), (106, 190)])
    return (poly([(100, 14), (156, 74), (100, 138), (44, 74)], "d") + poly([(100, 14), (156, 74), (100, 74)], "b")
            + poly([(44, 74), (100, 138), (100, 74)], "c") + L(100, 14, 100, 138) + L(44, 74, 156, 74)
            + P("M100 138 C90 150 110 160 100 172 C92 180 104 186 106 196", "n") + bows
            + P("M156 74 C170 110 176 150 190 190", "n t"))

def corn():
    kernels = "".join(E(84 + 12 * (c - 1.5), 54 + 14 * r, 5.5, 6.5, "d") for r in range(8) for c in range(4)
                      if not (r in (0, 7) and c in (0, 3)))
    return (P("M60 60 C60 30 108 30 108 60 L108 160 C108 176 60 176 60 160 Z", "d") + kernels
            + P("M58 150 C30 120 30 80 44 60 C52 100 64 130 76 172 Z", "c")
            + P("M110 150 C140 118 142 80 128 58 C120 100 108 130 94 172 Z", "c")
            + P("M84 172 L84 192", "n"))

def gears():
    def gear(cx, cy, r, n, cls):
        pts = []
        for i in range(n * 4):
            ang = math.radians(i * 360 / (n * 4))
            rad = r + 10 if (i % 4) in (1, 2) else r
            pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
        return poly(pts, cls) + C(cx, cy, r * 0.42, "a") + C(cx, cy, r * 0.15, "n")
    return gear(78, 110, 48, 10, "b") + gear(146, 62, 30, 8, "d") + gear(150, 154, 22, 7, "c")

def roti():
    spots = "".join(E(x, y, 5, 3, "c", 15) for x, y in [(80, 90), (110, 84), (130, 104), (92, 116), (116, 126), (70, 120), (100, 100)])
    return (E(100, 150, 84, 22, "b") + E(100, 140, 76, 18, "a") + E(100, 130, 72, 17, "a")
            + C(100, 104, 58, "d") + spots + P("M50 104 C56 70 90 52 120 56", "n t"))

def clouds():
    return (C(150, 56, 22, "d") + "".join(L(150 + 28 * math.cos(math.radians(a)), 56 + 28 * math.sin(math.radians(a)),
                                              150 + 38 * math.cos(math.radians(a)), 56 + 38 * math.sin(math.radians(a))) for a in range(-180, 1, 45))
            + cloud(20, 120, 1.1, "a") + cloud(96, 168, 0.9, "b") + cloud(10, 184, 0.6, "c"))

def honey():
    return (P("M50 70 L150 70 C158 90 160 150 150 172 C140 186 60 186 50 172 C40 150 42 90 50 70 Z", "d")
            + R(44, 54, 112, 18, "b", 5) + P("M56 72 C60 84 66 84 68 72 M120 72 C122 90 130 90 132 72", "c")
            + R(64, 104, 72, 46, "a", 6)
            + poly([(100 + 14 * math.cos(math.radians(60 * k + 30)), 127 + 14 * math.sin(math.radians(60 * k + 30))) for k in range(6)], "d")
            + f'<g transform="rotate(25 160 50)">' + R(156, 0, 8, 80, "c", 4) + E(160, 86, 12, 16, "c") + "</g>")

def ladder():
    rungs = "".join(L(64 - 3 * k, 170 - 30 * k, 136 - 3 * k, 170 - 30 * k) for k in range(6))
    return (P("M54 186 L74 14 L84 14 L64 186 Z", "b") + P("M124 186 L144 14 L154 14 L134 186 Z", "b")
            + "".join(P(f"M{60+3.6*k} {164-30*k} L{132+3.6*k} {164-30*k} L{131+3.6*k} {174-30*k} L{59+3.6*k} {174-30*k} Z", "c") for k in range(6))
            + ground(186))

def triangle():
    return (poly([(100, 16), (186, 172), (14, 172)], "b") + poly([(100, 172), (57, 94), (143, 94)], "a")
            + poly([(100, 64), (82, 94), (118, 94)], "d") + poly([(57, 146), (40, 172), (74, 172)], "e")
            + poly([(143, 146), (126, 172), (160, 172)], "e"))

def kaaba():
    return (P("M14 176 C40 160 160 160 186 176 C160 192 40 192 14 176 Z", "c")
            + P("M40 62 L132 62 L132 168 L40 168 Z", "b") + P("M132 62 L166 44 L166 150 L132 168 Z", "b")
            + P("M40 62 L74 44 L166 44 L132 62 Z", "b")
            + P("M40 82 L132 82 L132 96 L40 96 Z", "d") + P("M132 82 L166 64 L166 78 L132 96 Z", "d")
            + "".join(C(48 + 12 * k, 89, 2.5, "n") for k in range(8))
            + R(98, 110, 22, 40, "d", 2) + L(109, 110, 109, 150, "n t"))

def box():
    return (P("M30 80 L130 80 L130 176 L30 176 Z", "b") + P("M130 80 L172 60 L172 156 L130 176 Z", "c")
            + P("M30 80 L8 52 L108 52 L130 80 Z", "a") + P("M130 80 L150 48 L192 30 L172 60 Z", "a")
            + R(64, 110, 32, 30, "a", 2) + P("M70 124 L90 124 M70 132 L84 132", "n t"))

def tasbih():
    beads = "".join(C(100 + 70 * math.cos(math.radians(a)), 86 + 56 * math.sin(math.radians(a)), 8.5, "b" if a % 60 else "d")
                    for a in range(0, 360, 20) if not 80 <= a <= 100)
    return (beads + R(92, 136, 16, 20, "d", 5) + P("M100 156 L100 168", "n")
            + P("M92 168 L108 168 L116 194 L84 194 Z", "e") + "".join(L(90 + 5 * k, 172, 87 + 7 * k, 192, "n t") for k in range(5)))

def globe():
    return (P("M56 186 L144 186 L134 172 L66 172 Z", "c") + L(100, 152, 100, 172)
            + P("M30 84 C30 140 70 160 100 156", "n") + C(100, 84, 64, "b")
            + P("M64 50 C84 44 96 58 88 74 C80 88 92 100 76 110 C64 116 50 102 52 86 C54 70 50 58 64 50 Z", "c")
            + P("M118 44 C138 44 154 60 150 78 C146 92 132 86 128 100 C124 118 108 120 106 104 C104 88 112 80 108 66 C104 54 110 46 118 44 Z", "c")
            + P("M120 124 C134 118 146 126 142 138 C136 148 120 146 116 136 C114 130 116 126 120 124 Z", "c")
            + P("M36 84 L164 84 M100 20 C76 40 76 128 100 148 M100 20 C124 40 124 128 100 148", "n t"))

def soap():
    return (R(36, 96, 128, 70, "b", 26) + R(48, 104, 104, 46, "a", 20)
            + "".join(C(x, y, r, "n") for x, y, r in [(62, 70, 14), (92, 52, 18), (130, 66, 12), (150, 40, 9), (40, 40, 8)])
            + P("M56 64 q4 -6 10 -6 M86 44 q5 -7 12 -7", "n t") + ground(176))

def ewer():
    return (P("M74 52 L126 52 L120 70 C160 82 164 150 130 172 L70 172 C36 150 40 82 80 70 Z", "b")
            + R(68, 40, 64, 14, "c", 6) + P("M134 96 C156 90 170 74 184 54 L190 60 C178 84 160 104 140 112", "c")
            + P("M64 86 C40 86 34 120 52 136", "n") + P("M48 120 C80 132 120 132 152 120", "n t")
            + E(100, 176, 40, 8, "c") + P("M188 66 q-3 6 0 10 q3 -4 0 -10", "d"))

def teacup():
    return (E(100, 166, 82, 16, "c") + P("M36 96 L164 96 C162 140 138 164 100 164 C62 164 38 140 36 96 Z", "b")
            + P("M164 106 C192 106 192 144 156 144", "n") + E(100, 96, 64, 10, "d")
            + P("M80 80 c-8 -10 8 -18 0 -30 M100 76 c-8 -10 8 -18 0 -30 M120 80 c-8 -10 8 -18 0 -30", "n t")
            + P("M60 120 C80 128 120 128 140 120", "n t"))

def ice():
    def cube(x, y, s, cls):
        k = s * 0.35
        return (P(f"M{x} {y} l{k} {-k} h{s} l{-k} {k} z", "a") + P(f"M{x+s} {y} l{k} {-k} v{s} l{-k} {k} z", "c")
                + R(x, y, s, s, cls, 6) + P(f"M{x+8} {y+12} l10 0", "n t"))
    return cube(28, 110, 60, "b") + cube(104, 118, 52, "b") + cube(66, 52, 56, "b") + ground(178)

def balloon():
    return one(digit=None)

PICS.update(pomegranate=pomegranate, tamarind=tamarind, wool=wool, mortar=mortar, pen=pen, carrot=carrot,
            broom=broom, fig=fig, envelope=envelope, jar=jar, bowarrow=bowarrow, kite=kite, corn=corn,
            gears=gears, roti=roti, clouds=clouds, honey=honey, ladder=ladder, triangle=triangle, kaaba=kaaba,
            box=box, tasbih=tasbih, globe=globe, soap=soap, ewer=ewer, teacup=teacup, ice=ice, balloon=balloon)


# ---- batch 3: more objects for Punjabi, Gujarati, Marathi, Nepali ----
def potato():
    eyes = "".join(P(f"M{x} {y} q4 -4 8 0", "n t") for x, y in [(70, 92), (110, 80), (130, 120), (86, 130), (60, 118)])
    return (P("M40 110 C34 70 80 52 120 58 C160 64 176 96 164 128 C152 160 100 170 70 158 C50 150 42 132 40 110 Z", "b")
            + eyes + P("M140 150 C150 130 176 130 184 150 C190 170 166 182 150 176 C140 172 136 162 140 150 Z", "b") + ground(184))

def brick():
    rows = []
    for r in range(4):
        y = 70 + r * 28
        off = 0 if r % 2 == 0 else 26
        for k in range(4):
            x = 20 + off + k * 52
            if x + 48 <= 186:
                rows.append(R(x, y, 48, 24, "e" if (r + k) % 2 else "b", 3))
    return "".join(rows) + ground(186)

def cardamom():
    pods = "".join(f'<g transform="rotate({r} {x} {y})">' + E(x, y, 16, 30, "c") +
                   P(f"M{x} {y-28} L{x} {y+28}", "n t") + P(f"M{x} {y-30} l0 -8", "n") + "</g>"
                   for x, y, r in [(70, 100, -25), (110, 90, 10), (140, 130, 35), (90, 146, -60)])
    return pods + "".join(C(x, y, 4, "b") for x, y in [(50, 160), (60, 168), (164, 70)])

def dew():
    drops = "".join(P(f"M{x} {y} q-9 14 0 20 q9 -6 0 -20", "b") for x, y in [(80, 70), (120, 84), (100, 112), (60, 116), (140, 120)])
    return (P("M20 170 C40 80 120 40 186 28 C170 100 120 160 20 170 Z", "c")
            + P("M20 170 C70 130 130 80 186 28", "n t") + drops)

def water():
    return (P("M56 40 L144 40 L132 182 L68 182 Z", "a") + P("M60 80 L140 80 L132 182 L68 182 Z", "b")
            + P("M76 100 q4 -6 10 -6 M96 130 q4 -6 10 -6", "n t") + E(100, 40, 44, 6, "a"))

def pear():
    return (P("M100 36 C116 36 120 60 124 76 C150 92 168 122 160 152 C152 178 124 186 100 186 C76 186 48 178 40 152 C32 122 50 92 76 76 C80 60 84 36 100 36 Z", "c")
            + P("M100 36 L104 18", "n") + leaf(104, 24, -30, 34) + P("M58 120 C54 134 56 146 62 156", "n t"))

def olive():
    olives = "".join(f'<g transform="rotate({r} {x} {y})">' + E(x, y, 11, 16, "c") + C(x - 3, y - 6, 2.5, "n") + "</g>"
                     for x, y, r in [(70, 120, 20), (120, 96, -15), (150, 140, 10)])
    leaves = "".join(leaf(x, y, a, 40, "b") for x, y, a in [(40, 60, 30), (70, 70, -20), (100, 60, 40), (130, 70, -30), (160, 60, 20)])
    return P("M20 50 C80 80 140 70 190 50", "n") + leaves + olives

def pineapple():
    scales = "".join(L(60 + 12 * k, 76, 40 + 12 * k, 180, "n t") + L(140 - 12 * k, 76, 160 - 12 * k, 180, "n t") for k in range(0, 8, 2))
    crown = "".join(P(f"M100 76 C{100+dx} 60 {100+dx*1.4} 40 {100+dx*1.6} {24 if abs(dx) < 20 else 34} C{100+dx*0.8} 50 {100+dx*0.3} 66 100 76 Z", "c")
                    for dx in (-30, -12, 12, 30))
    body = "M100 76 C140 76 156 110 154 140 C150 172 126 184 100 184 C74 184 50 172 46 140 C44 110 60 76 100 76 Z"
    _clip[0] += 1
    cid = f"pine{_clip[0]}"
    return (f'<clipPath id="{cid}"><path d="{body}"/></clipPath>' + P(body, "d")
            + f'<g clip-path="url(#{cid})">{scales}</g>' + P(body, "n") + crown)

_clip = [0]

def anvil():
    return (P("M30 70 L150 70 C150 88 170 90 190 84 L176 106 L140 106 L132 116 L68 116 L60 106 L44 106 C34 96 30 84 30 70 Z", "b")
            + P("M72 116 L128 116 L136 160 L64 160 Z", "b") + R(46, 160, 108, 20, "c", 3) + ground(186))

def pillow():
    return (P("M30 70 C70 56 130 56 170 70 C182 100 182 130 170 156 C130 170 70 170 30 156 C18 130 18 100 30 70 Z", "e")
            + P("M30 70 C24 62 18 60 14 62 M170 70 C176 62 182 60 186 62 M30 156 C24 164 18 166 14 164 M170 156 C176 164 182 166 186 164", "n")
            + star(100, 112, 22, 10, "d", 8))

def coconut():
    return (C(84, 120, 56, "b") + P("M60 92 q6 -6 12 0 M84 84 q6 -6 12 0", "n t") + C(68, 104, 5, "n") + C(84, 98, 5, "n") + C(78, 116, 5, "n")
            + P("M120 180 C120 140 150 124 186 130 C190 166 160 186 120 180 Z", "a") + P("M128 176 C130 146 154 134 178 138 C180 164 158 180 128 176 Z", "d")
            + ground(186))

def window():
    return (P("M40 186 L40 70 C40 36 70 18 100 14 C130 18 160 36 160 70 L160 186 Z", "c")
            + P("M54 172 L54 74 C54 48 76 32 100 28 C124 32 146 48 146 74 L146 172 Z", "b")
            + L(100, 28, 100, 172) + L(54, 100, 146, 100) + R(28, 172, 144, 14, "a", 3)
            + C(130, 60, 12, "d") + P("M64 140 q8 -6 16 0", "n t"))

def lemon():
    return (P("M24 110 C30 74 70 58 104 60 C140 62 170 84 176 110 C170 138 140 160 104 160 C70 160 30 146 24 110 Z", "d")
            + P("M20 110 L28 104 M180 110 L172 116", "n") + leaf(120, 62, -40, 36)
            + P("M58 96 C54 106 54 118 60 128", "n t"))

def apple():
    return (P("M100 56 C120 40 168 44 170 96 C172 150 132 182 112 176 C104 174 96 174 88 176 C68 182 28 150 30 96 C32 44 80 40 100 56 Z", "e")
            + P("M100 56 C98 42 100 30 108 20", "n") + leaf(106, 32, -20, 36) + P("M56 90 C52 104 52 118 58 130", "n t"))

def tap():
    return (R(14, 40, 70, 30, "c", 4) + R(84, 46, 60, 18, "b", 4) + P("M144 46 C170 46 176 60 176 76 L160 76 C160 66 156 64 144 64 Z", "b")
            + R(100, 24, 16, 22, "d", 3) + R(88, 18, 40, 10, "d", 4)
            + "".join(P(f"M168 {96+26*k} q-7 11 0 16 q7 -5 0 -16", "b") for k in range(3)) + E(168, 182, 26, 6, "b"))

def pennant():
    return (R(46, 16, 8, 170, "c", 3) + C(50, 12, 6, "d") + P("M54 30 L176 66 L54 102 Z", "e")
            + P("M80 50 L80 82", "n t") + R(30, 180, 40, 8, "a", 2))

def building():
    wins = "".join(R(x, y, 18, 20, "d", 2) for x in (52, 82, 112) for y in (60, 92, 124))
    return (R(40, 40, 100, 140, "b", 2) + R(30, 30, 120, 12, "c", 2) + wins + R(80, 152, 24, 28, "e", 2)
            + R(140, 100, 40, 80, "c", 2) + R(150, 112, 10, 12, "a") + R(150, 140, 10, 12, "a") + ground(182))

def sugarcane():
    def cane(x, cls):
        return (R(x, 30, 16, 156, cls, 6) + "".join(L(x, y, x + 16, y, "n") for y in (60, 92, 124, 156)))
    return cane(56, "c") + cane(92, "b") + cane(128, "c") + leaf(64, 30, -120, 40) + leaf(100, 30, -60, 44) + leaf(136, 30, -40, 40)

def ring():
    return (C(100, 120, 56, "d") + C(100, 120, 40, "a")
            + poly([(82, 64), (118, 64), (130, 48), (100, 22), (70, 48)], "e") + P("M70 48 L130 48 M100 22 L92 48 L100 64 L108 48 Z", "n t"))

def spoon():
    return (f'<g transform="rotate(-35 100 100)">' + E(100, 52, 30, 40, "b") + E(100, 50, 20, 28, "a")
            + R(94, 88, 12, 100, "b", 6) + "</g>"
            + f'<g transform="rotate(30 130 110)">' + R(124, 50, 12, 110, "c", 6) + P("M118 30 L118 58 M130 30 L130 58 M142 30 L142 58 M116 56 L144 56 L136 70 L124 70 Z", "c") + "</g>")

def scale():
    return (L(100, 30, 100, 160) + R(70, 160, 60, 14, "c", 4) + L(30, 50, 170, 50) + C(100, 30, 6, "d")
            + P("M30 50 L14 110 M30 50 L46 110 M170 50 L154 110 M170 50 L186 110", "n t")
            + P("M8 110 L52 110 C48 128 12 128 8 110 Z", "b") + P("M148 110 L192 110 C188 128 152 128 148 110 Z", "b"))

def almond():
    nuts = "".join(f'<g transform="rotate({r} {x} {y})">' + P(f"M{x} {y-30} C{x+18} {y-10} {x+16} {y+20} {x} {y+30} C{x-16} {y+20} {x-18} {y-10} {x} {y-30} Z", "b")
                   + P(f"M{x-4} {y-14} q-4 14 0 28", "n t") + "</g>" for x, y, r in [(60, 110, -30), (100, 90, 0), (140, 110, 30), (80, 150, -70), (124, 152, 70)])
    return nuts

def well():
    return (R(40, 110, 120, 70, "b", 4) + "".join(L(40, y, 160, y, "n t") for y in (132, 156))
            + "".join(L(x, 110, x, 132, "n t") for x in (70, 100, 130)) + E(100, 110, 60, 12, "a")
            + L(52, 110, 52, 40) + L(148, 110, 148, 40) + P("M40 44 L100 20 L160 44 Z", "c")
            + L(52, 62, 148, 62) + L(100, 62, 100, 82) + R(88, 82, 24, 22, "d", 3))

def mirror():
    return (E(100, 84, 56, 66, "d") + E(100, 84, 44, 54, "a") + P("M78 60 L94 44 M80 82 L112 50", "n t")
            + R(92, 150, 16, 34, "d", 6) + E(100, 186, 30, 6, "c"))

def walnut():
    return (P("M100 30 C148 30 172 70 168 110 C164 152 134 176 100 176 C66 176 36 152 32 110 C28 70 52 30 100 30 Z", "b")
            + L(100, 30, 100, 176) + P("M60 70 q12 10 0 22 q-12 10 0 22 q12 10 0 22 M140 70 q-12 10 0 22 q12 10 0 22 q-12 10 0 22", "n t"))

PICS.update(potato=potato, brick=brick, cardamom=cardamom, dew=dew, water=water, pear=pear, olive=olive,
            pineapple=pineapple, anvil=anvil, pillow=pillow, coconut=coconut, window=window, lemon=lemon, apple=apple,
            tap=tap, pennant=pennant, building=building, sugarcane=sugarcane, ring=ring, spoon=spoon, scale=scale,
            almond=almond, well=well, mirror=mirror, walnut=walnut)


# ---- batch 4: Dravidian-language words ----
def swing():
    return (R(16, 16, 168, 12, "c", 5) + L(30, 28, 30, 186) + L(170, 28, 170, 186)
            + L(70, 28, 64, 132) + L(130, 28, 136, 132) + R(54, 132, 92, 14, "b", 5)
            + leaf(30, 40, 200, 30) + leaf(170, 40, -20, 30) + ground(186))

def ball():
    return (C(100, 104, 70, "b") + P("M30 104 C60 80 140 80 170 104", "n") + P("M30 104 C60 128 140 128 170 104", "n")
            + P("M100 34 C80 70 80 138 100 174", "n") + P("M100 34 C120 70 120 138 100 174", "n")
            + P("M60 60 C70 50 84 44 96 42", "n t") + E(100, 182, 40, 6, "c"))

def house():
    return (P("M24 92 L100 30 L176 92 Z", "e") + R(40, 92, 120, 88, "b", 2) + R(84, 130, 32, 50, "d", 2)
            + R(52, 108, 24, 22, "a", 2) + R(124, 108, 24, 22, "a", 2) + L(64, 108, 64, 130, "n t") + L(136, 108, 136, 130, "n t")
            + R(130, 40, 16, 34, "c", 2) + ground(182))

def feather():
    barbs = "".join(L(100 + 2 * k, 40 + 12 * k, 70 + 2 * k, 30 + 12 * k, "n t") + L(100 + 2 * k, 40 + 12 * k, 130 + 2 * k, 30 + 12 * k, "n t")
                    for k in range(1, 10))
    body = "M100 20 C150 40 160 110 116 160 L100 176 L84 160 C40 110 50 40 100 20 Z"
    _clip[0] += 1
    cid = f"fea{_clip[0]}"
    return (f'<clipPath id="{cid}"><path d="{body}"/></clipPath>' + P(body, "b")
            + f'<g clip-path="url(#{cid})">{barbs}</g>' + P(body, "n") + P("M100 20 L104 188", "n"))

def stool():
    return (E(100, 64, 70, 18, "e") + P("M30 64 L30 80 C30 92 170 92 170 80 L170 64", "e")
            + P("M50 88 L36 182 M150 88 L164 182 M80 92 L74 182 M120 92 L126 182", "n") + L(44, 140, 156, 140, "n") + ground(184))

def onion():
    return (P("M100 40 C150 60 172 110 152 148 C138 172 62 172 48 148 C28 110 50 60 100 40 Z", "e")
            + P("M100 40 C82 70 78 130 92 168 M100 40 C118 70 122 130 108 168", "n t")
            + P("M100 40 C96 26 98 16 104 8 M100 40 C108 28 116 22 124 18", "n")
            + P("M76 168 l-6 14 M100 172 l0 14 M124 168 l6 14", "n t"))

def plane():
    return (P("M20 104 C20 92 40 88 60 88 L150 88 C170 88 186 96 186 104 C186 112 170 120 150 120 L60 120 C40 120 20 116 20 104 Z", "b")
            + P("M90 90 L120 34 L136 34 L118 90 Z", "c") + P("M90 118 L120 174 L136 174 L118 118 Z", "c")
            + P("M30 92 L22 62 L38 62 L52 90 Z", "d") + "".join(C(x, 102, 5, "a") for x in (76, 96, 116, 136))
            + C(166, 100, 6, "a") + cloud(120, 196, 0.5) + cloud(10, 196, 0.45))

PICS.update(swing=swing, ball=ball, house=house, feather=feather, stool=stool, onion=onion, plane=plane)
