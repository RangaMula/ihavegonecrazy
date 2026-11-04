# -*- coding: utf-8 -*-
"""Turn single Bengali letters into true vector outlines (for coloring + dotted tracing).

Uses the Baloo Da 2 ExtraBold outlines (SIL OFL) so letters are fat and round - easy for
small hands to color - and print as crisp vectors at any size.
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "assets", "fonts", "baloo-da-2-bengali-800-normal.woff2")
_font = TTFont(FONT)
# Merge overlapping contours so the coloring outline has no stray inner lines.
from fontTools.ttLib.removeOverlaps import removeOverlaps
removeOverlaps(_font)
_gs = _font.getGlyphSet()
_cmap = _font.getBestCmap()


# ড় ঢ় য় are usually typed as letter + nukta (they never compose under NFC);
# the font also has the single-codepoint forms, which is what we draw.
_PRECOMPOSED = {"\u09a1\u09bc": "\u09dc", "\u09a2\u09bc": "\u09dd", "\u09af\u09bc": "\u09df"}


def outline(ch):
    """Return (path_d, (xmin, ymin, xmax, ymax)) in font units, y pointing down."""
    ch = _PRECOMPOSED.get(ch, ch)
    gname = _cmap[ord(ch)]
    bp = BoundsPen(_gs)
    _gs[gname].draw(bp)
    xmin, ymin, xmax, ymax = bp.bounds
    sp = SVGPathPen(_gs)
    _gs[gname].draw(TransformPen(sp, (1, 0, 0, -1, 0, 0)))  # flip y
    return sp.getCommands(), (xmin, -ymax, xmax, -ymin)


def letter_svg(ch, mode="color", min_box=650, pad=0.10, cls="glyph"):
    """mode='color' -> thick black outline, white inside (to color in)
       mode='trace' -> grey dashed outline only (to trace over with a pencil)"""
    d, (x0, y0, x1, y1) = outline(ch)
    w, h = x1 - x0, y1 - y0
    side = max(w, h, min_box) * (1 + 2 * pad)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f"{cx - side / 2:.0f} {cy - side / 2:.0f} {side:.0f} {side:.0f}"
    if mode == "color":
        style = 'fill="#fff" stroke="#111" stroke-width="16" stroke-linejoin="round"'
    elif mode == "trace":
        style = ('fill="none" stroke="#8a8a8a" stroke-width="10" stroke-dasharray="22 16" '
                 'stroke-linecap="round" stroke-linejoin="round"')
    else:  # solid colour (cover)
        style = f'fill="{mode}" stroke="#1d1d1d" stroke-width="22" stroke-linejoin="round" paint-order="stroke"'
    return (f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{d}" {style}/></svg>')
