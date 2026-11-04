# -*- coding: utf-8 -*-
"""Maktabatu Kunujul Akhirah mark (8-point star, zigzag dome, crescent), taken from the
publisher's official vector logo (Brand-Assets/maktabatu-logo-english.svg) without its wordmark."""

_MARK = (
    '<g transform="translate(0,-15) scale(0.82) translate(55,30)"><g>'
    '<rect x="150" y="150" width="200" height="200" fill="none" stroke="{ink}" stroke-width="16"/>'
    '<rect x="150" y="150" width="200" height="200" fill="none" stroke="{ink}" stroke-width="16" transform="rotate(45 250 250)"/>'
    '<clipPath id="dome{uid}"><path d="M175 355 L175 255 Q175 165 250 140 Q325 165 325 255 L325 355 Z"/></clipPath>'
    '<path d="M175 355 L175 255 Q175 165 250 140 Q325 165 325 255 L325 355 Z" fill="{ink}"/>'
    '<g clip-path="url(#dome{uid})" stroke="{paper}" stroke-width="10" fill="none">'
    + "".join(f'<polyline points="{" ".join(f"{x},{y + (32 if k % 2 else 0)}" for k, x in enumerate(range(150, 351, 20)))}"/>'
              for y in (174, 224, 274, 324))
    + '</g><line x1="250" y1="140" x2="250" y2="112" stroke="{ink}" stroke-width="10"/>'
    '<circle cx="250" cy="88" r="26" fill="{ink}"/><circle cx="262" cy="80" r="24" fill="{paper}"/></g></g>'
)
_n = [0]

def mark_svg(ink="#1a1a1a", paper="#ffffff"):
    _n[0] += 1
    body = _MARK.replace("{ink}", ink).replace("{paper}", paper).replace("{uid}", str(_n[0]))
    return f'<svg viewBox="125 50 258 290" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%">{body}</svg>'
