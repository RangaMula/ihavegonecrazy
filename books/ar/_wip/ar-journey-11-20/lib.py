import re
from translit import tr, FATHA

TPL = re.compile(r'\{([^{}]+)\}')


def expand(text):
    """Replace {arabic} with 'arabic (bangla-pron)'. Verb forms ending in a short vowel keep it."""
    def rep(m):
        ar = m.group(1)
        tail = ar.rstrip().rstrip('\u0651')
        keep = tail[-1:] in ('\u064e', '\u064f', '\u0650') and ' ' not in ar.strip()
        b, _ = tr(ar, pause_end=not keep)
        return '%s (%s)' % (ar, b)
    return TPL.sub(rep, text)


def pron(ar, bn_override=None, en_override=None):
    keep = ar.rstrip().rstrip('\u0651')[-1:] == FATHA and ' ' not in ar.strip()  # verb citation form keeps its final -a
    b, e = tr(ar, pause_end=not keep)
    return bn_override or b, en_override or e


def W(ar, bn, en, note, bp=None, ep=None):
    b, e = pron(ar, bp, ep)
    return {"fr": ar, "bn_pron": b, "en_pron": e, "bn": bn, "en": en, "note_bn": expand(note)}


def C(ar, bn, en, note, icon, story, link, source, bp=None, ep=None):
    d = W(ar, bn, en, note, bp, ep)
    d["icon"] = icon
    d["story_bn"] = expand(story)
    if link:
        d["link_bn"] = expand(link)
    d["source_hint"] = source
    return d


def S(ar, bn, en, note=None, bp=None, ep=None):
    """A sentence (Triple Row). Case endings written; pause at the end."""
    b, e = tr(ar)
    if not ar.rstrip().endswith(('.', '؟', '!')):
        pass
    d = {"fr": ar, "bn_pron": bp or b, "en_pron": ep or e, "bn": bn, "en": en}
    if note:
        d["note_bn"] = expand(note)
    return d


def Q(q, a):
    return {"q_bn": expand(q), "a": expand(a)}


def SET(code, kind, tbn, ten, words):
    return {"code": code, "kind": kind, "title_bn": tbn, "title_en": ten, "words": words}
