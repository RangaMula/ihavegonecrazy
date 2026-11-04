# -*- coding: utf-8 -*-
"""Shared map frame: the whole subcontinent, coastline only (no political borders), with a dashed
area around the region where the language is spoken."""

FRAME = [[66.0, 6.0], [92.5, 33.5]]
SEAS = dict(arabian=[68.5, 14.0], bay=[88.0, 14.0])
SEA_LABELS = [("arabian", "Arabian Sea", 30, True), ("bay", "Bay of Bengal", 30, True)]


def south_asia_map(points, area, cities, label, marker, caption, legend, extra_labels=(), frame=None):
    """points: {key: [lon, lat]} incl. 'area' and 'label'; area: (rx, ry, rot)."""
    pts = dict(SEAS); pts.update(points)
    return dict(frame=frame or FRAME, land=True, points=pts, areas=[("area",) + tuple(area)], cities=cities,
                labels=[("label", label, 32, False)] + SEA_LABELS + list(extra_labels),
                world_marker=marker, world_r=13, world_caption=caption, legend=legend)
