# -*- coding: utf-8 -*-
"""Real-height measurement for flowing blocks. Pass 1 uses estimates and records every block;
measure.js renders them at page width and stores heights; pass 2 lays out pages with the true heights."""
import hashlib, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(HERE, "data", ".measure_cache.json")
CACHE = json.load(open(CACHE_FILE)) if os.path.exists(CACHE_FILE) else {}
SEEN = {}

def key(html):
    return hashlib.sha1(html.encode("utf-8")).hexdigest()[:16]

def height(html, est):
    k = key(html)
    SEEN[k] = html
    return CACHE.get(k, est)

def missing():
    return {k: v for k, v in SEEN.items() if k not in CACHE}
