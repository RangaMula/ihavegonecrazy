# -*- coding: utf-8 -*-
"""Turn letters (any script, including conjuncts like क्ष or Urdu letters) into true vector
outlines for coloring and dotted tracing.

Text is shaped with HarfBuzz (so conjuncts, nuktas and right-to-left letters come out exactly as a
browser would draw them), then all glyph outlines are merged with skia-pathops so the coloring
outline has no stray inner lines where font contours overlap.
"""
import io, os
from functools import lru_cache
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen
import uharfbuzz as hb
import pathops

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")


@lru_cache(maxsize=None)
def _font(fname):
    tt = TTFont(os.path.join(FONTS, fname))
    tt.flavor = None
    bio = io.BytesIO(); tt.save(bio)
    data = bio.getvalue()
    tt = TTFont(io.BytesIO(data))
    hbfont = hb.Font(hb.Face(hb.Blob(data)))
    return tt, tt.getGlyphSet(), tt.getGlyphOrder(), hbfont


@lru_cache(maxsize=None)
def outline(text, fname):
    """Return (svg_path_d, (xmin, ymin, xmax, ymax)) in font units with y pointing down."""
    tt, gs, order, hbfont = _font(fname)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(hbfont, buf, {})
    path = pathops.Path()
    pen = path.getPen(glyphSet=gs)
    x = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gname = order[info.codepoint]
        tp = TransformPen(pen, (1, 0, 0, -1, x + pos.x_offset, -pos.y_offset))
        gs[gname].draw(tp)
        x += pos.x_advance
    path.simplify(fix_winding=True)
    sp = SVGPathPen(gs)
    path.draw(sp)
    b = path.bounds
    return sp.getCommands(), (b[0], b[1], b[2], b[3])


def letter_svg(text, font, mode="color", min_box=650, pad=0.10, cls="glyph"):
    """mode='color' -> thick black outline, white inside (to color in)
       mode='trace' -> grey dashed outline only (to trace over with a pencil)
       any other value -> treated as a fill colour (cover art)"""
    d, (x0, y0, x1, y1) = outline(text, font)
    w, h = x1 - x0, y1 - y0
    side = max(w, h, min_box) * (1 + 2 * pad)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f"{cx - side / 2:.0f} {cy - side / 2:.0f} {side:.0f} {side:.0f}"
    sw = side / 1000
    if mode == "color":
        style = f'fill="#fff" stroke="#111" stroke-width="{16*sw:.1f}" stroke-linejoin="round"'
    elif mode == "trace":
        style = (f'fill="none" stroke="#8a8a8a" stroke-width="{10*sw:.1f}" stroke-dasharray="{22*sw:.1f} {16*sw:.1f}" '
                 'stroke-linecap="round" stroke-linejoin="round"')
    else:
        style = f'fill="{mode}" stroke="#1d1d1d" stroke-width="{22*sw:.1f}" stroke-linejoin="round" paint-order="stroke"'
    return (f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" {style}/></svg>')
