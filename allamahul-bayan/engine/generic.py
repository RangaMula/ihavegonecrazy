# -*- coding: utf-8 -*-
"""Generator for any alphabet that is not handled by indic.py: Latin-script languages (with
capital + small letter pairs), Greek, Cyrillic, Armenian, Georgian, Hebrew, Ethiopic, Hangul,
kana, Thai, syllabaries ... A language file supplies the data; this fills in the book-wide
fields (title, subtitle, cover, KDP metadata) and returns the LANG dict the engine uses.

See languages/es.py for a complete Latin-script example.
"""
import os
from indic import fontset  # noqa: F401  (re-exported for language files)

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")


def letter(letter, name_native, name_en, sound, word, tr, meaning, pic, phon, phon_label, args=None, note=None):
    """One letter page. `letter` is what is drawn big (e.g. "Aa", "ა", "ሀ").
    phon = native-phonetics HTML (e.g. the letter's name/spelling rule in the language itself)."""
    return dict(letter=letter, name_native=name_native, name_en=name_en, sound=sound, word=word, translit=tr,
                meaning=meaning, pic=pic, pic_args=args or {}, note=note, phon=phon, phon_label=phon_label)


def section(items, label="LETTER", chip="THE LETTERS", title="The Letters", native="", native_tr="",
            intro_html="", chart_title="letters", chart_cols=7, warmup_title="the letters", warmup_cols=6):
    return dict(key=title.lower().replace(" ", "_"), label=label, chip=chip, title=title, native=native, native_tr=native_tr,
                intro_html=intro_html, chart_title=chart_title, chart_cols=chart_cols, warmup_title=warmup_title,
                warmup_cols=warmup_cols, items=items)


def _span(t):
    return f'<span class="nt">{t}</span>'


def build(d):
    """d keys (see languages/es.py): code folder series_no name native native_tr name_word write_word
    title_native title_letters belongs_native belongs_pic alphabet_native numbers_native numbers_tr
    phrases_native fonts disp_family text_family glyph_font font_credit sections sound_notes phon_explain
    standard hello hello_pics map digits phrases cheer facts_source book_pic review_note tiles cover_pics
    speakers_blurb sample_words keywords phon_feature  (+ optional: dir, extra_css, title_size, market,
    chart_note, draft, letters_word)"""
    lang = d["name"]
    L = dict(d)
    n = sum(len(s["items"]) for s in d["sections"])
    word = d.get("letters_word", "Letters")
    L["title"] = d.get("title", f"My First {lang} Alphabet")
    L["subtitle"] = d.get("subtitle", f"A Coloring Book to Learn, Trace & Say the {n} {lang} {word} with English Phonetics")
    L.setdefault("chart_note", "Read the alphabet row by row — the same order as in this book.")
    L.setdefault("draft", True)
    L["series_line"] = (f"<b>Book {d['series_no']} is {lang}</b>. More languages from around the world are in the series, "
                        "in shā’ Allāh.")
    sample = d["sample_words"]
    sw = ", ".join(f"{_span(w)} <i>{t}</i> {m}" for w, t, m in sample[:2])
    swk = ", ".join(f"{w} <i>{t}</i> ({m})" for w, t, m in sample)
    dg = d["digits"]
    L["cover"] = dict(
        title_html=d.get("cover_title_html", f"My First {lang}<br>Alphabet"), tiles=d["tiles"], pics=d["cover_pics"],
        title_size=d.get("title_size", 50),
        blurb=f"{d['speakers_blurb']} This big, friendly coloring book introduces young children to <b>{n} {word.lower()}</b> of "
              f"{lang} <b>through English</b> — no {lang} needed at home.",
        bullets=[f"<b>Every letter on its own page</b> — a giant letter to color, its name in {lang} <i>and</i> English letters",
                 f"<b>Easy English sound guides</b> plus {d['phon_feature']}",
                 f"<b>A word and picture for every letter</b>: {sw}…",
                 "<b>Pencil tracing rows</b> and a warm-up page for every part of the alphabet",
                 f"<b>Map to color</b>, {lang} numbers {_span(dg[0][0])}–{_span(dg[9][0])}, first phrases and a certificate",
                 "<b>Single-sided coloring pages</b> so markers never ruin the next picture"])
    L["kdp"] = dict(
        market=d.get("market", "Amazon.com (also Amazon.co.uk and Amazon.ca)"),
        desc_intro=f"{d['speakers_blurb']} This big, friendly coloring book introduces young children to <b>{n} {word.lower()}</b> of "
                   f"{lang} <b>through English</b>, so no {lang} is needed at home.",
        desc_bullets=[f"<b>Every letter on its own page:</b> a giant letter to color, with its name written in {lang} <i>and</i> in English letters",
                      f"<b>Easy English sound guides</b> plus {d['phon_feature']}",
                      f"<b>A word and a picture for every letter</b> to color and say: {swk}…",
                      "<b>Pencil tracing rows</b> on every page, plus warm-up tracing pages",
                      f"<b>Meet the language:</b> where {lang} is spoken, a map to color, the whole alphabet on one page, the numbers "
                      f"{dg[0][0]}–{dg[9][0]} and first friendly phrases"],
        categories=d.get("categories", ["Children's Books › Activities, Crafts & Games › Coloring Books",
                                        "Children's Books › Education & Reference › Foreign Language Study",
                                        "Children's Books › Religions › Islam"]),
        keywords=d["keywords"])
    return L
