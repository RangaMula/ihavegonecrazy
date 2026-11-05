# -*- coding: utf-8 -*-
"""Map helpers. region_map() works for any part of the world; south_asia_map() is the subcontinent preset.
Shared map frame: the whole subcontinent, coastline only (no political borders), with a dashed
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


def region_map(frame, points, area, cities, label, label_at, marker, caption, legend, seas=(), area_rot=0, world_r=13):
    """Generic coastline-only map (no political borders).
    frame: [[lon_min, lat_min], [lon_max, lat_max]] (keep it roughly square, it is drawn into a square)
    points: {key: [lon, lat]} for cities; area: (center_lon, center_lat, rx_px, ry_px) dashed ellipse, or None
    cities: [(key, label, dx, dy, anchor, is_capital_star)]; label: big region label text, label_at: [lon, lat]
    seas: [(text, lon, lat)] italic sea labels."""
    pts = dict(points); pts["label"] = label_at
    labels = [("label", label, 32, False)]
    for i, (t, lon, lat) in enumerate(seas):
        pts[f"sea{i}"] = [lon, lat]; labels.append((f"sea{i}", t, 28, True))
    areas = []
    if area:
        pts["area"] = [area[0], area[1]]; areas = [("area", area[2], area[3], area_rot)]
    return dict(frame=frame, land=True, points=pts, areas=areas, cities=cities, labels=labels,
                world_marker=marker, world_r=world_r, world_caption=caption, legend=legend)
