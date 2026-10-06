# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import pron

def T(fr, bn, en, note=None, bp=None, ep=None, pause=True):
    b, e = pron(fr, pause)
    d = {"fr": fr, "bn_pron": bp or b, "en_pron": ep or e, "bn": bn, "en": en}
    if note:
        d["note_bn"] = note
    return d

def V(fr, bn, en, pres, note=None, bp=None, ep=None):
    """verb: past he-form cited with final fatha; note gives present."""
    pb, _ = pron(pres, False)
    n = "বর্তমান: %s (%s)" % (pres, pb)
    if note:
        n += " · " + note
    return T(fr, bn, en, n, bp, ep, pause=False)

def P(ar, pause=True):
    """'arabic (bangla pron)' helper for notes"""
    return "%s (%s)" % (ar, pron(ar, pause)[0])

def N(fr, bn, en, g, pl=None, extra=None, **kw):
    """noun with gender + plural note. g: 'পুং'/'স্ত্রী'. pl: arabic plural or a Bangla phrase starting with '!'"""
    parts = [g]
    if pl is None:
        parts.append("বহুবচন নেই")
    elif pl.startswith("!"):
        parts.append(pl[1:])
    else:
        parts.append("বহুবচন: " + " / ".join(P(x) for x in pl.split("/")))
    if extra:
        parts.append(extra)
    return T(fr, bn, en, " · ".join(parts), **kw)

def A(fr, bn, en, fem, extra=None, **kw):
    n = "স্ত্রী: " + P(fem)
    if extra:
        n += " · " + extra
    return T(fr, bn, en, n, **kw)
