# Arabic (fully vowelled) -> Bangla pronunciation (STYLE §3) and simplified ALA-LC (STYLE §4)
# Conventions in source strings:
#   "|" marks an attached proclitic (وَ|أَنَا, بِ|الْ...). Removed from fr; "لِ|ال" becomes "لِل".
import re, sys

FATHA, KASRA, DAMMA, SUKUN, SHADDA = 'َ', 'ِ', 'ُ', 'ْ', 'ّ'
AN, IN, UN, DAGGER = 'ً', 'ٍ', 'ٌ', 'ٰ'
TATWEEL = 'ـ'
MARKS = {FATHA, KASRA, DAMMA, SUKUN, SHADDA, AN, IN, UN, DAGGER}

CONS = {
    'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': 'ḥ', 'خ': 'kh', 'د': 'd', 'ذ': 'dh', 'ر': 'r', 'ز': 'z',
    'س': 's', 'ش': 'sh', 'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ', 'ظ': 'ẓ', 'ع': 'ʿ', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
    'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'و': 'w', 'ي': 'y', 'ة': 'T',
    'ء': 'ʾ', 'أ': 'ʾ', 'إ': 'ʾ', 'ؤ': 'ʾ', 'ئ': 'ʾ', 'ڤ': 'v', 'پ': 'p', 'گ': 'g', 'چ': 'ch',
}
SUN = set('تثدذرزسشصضطظلن')
NUK = '়'
BN_CONS = {
    'b': 'ব', 't': 'ত', 'th': 'থ' + NUK, 'j': 'জ', 'ḥ': 'হ' + NUK, 'kh': 'খ' + NUK, 'd': 'দ', 'dh': 'দ' + NUK,
    'r': 'র', 'z': 'জ' + NUK, 's': 'স', 'sh': 'শ', 'ṣ': 'স' + NUK, 'ḍ': 'ড', 'ṭ': 'ট', 'ẓ': 'য', 'ʿ': 'ʿ',
    'gh': 'গ' + NUK, 'f': 'ফ' + NUK, 'q': 'ক' + NUK, 'k': 'ক', 'l': 'ল', 'm': 'ম', 'n': 'ন', 'h': 'হ',
    'ʾ': 'ʾ', 'v': 'ভ' + NUK, 'p': 'প', 'g': 'গ', 'ch': 'চ',
}
CONJ_OK = {'b', 't', 'j', 'd', 'k', 'l', 'm', 'n', 's', 'sh', 'ṭ', 'ḍ', 'p', 'g', 'ch'}
VOW = {'a', 'i', 'u', 'ā', 'ī', 'ū'}
MATRA = {'a': 'া', 'i': 'ি', 'u': 'ু', 'ā': 'াː', 'ī': 'ীː', 'ū': 'ূː'}
INDEP = {'a': 'আ', 'i': 'ই', 'u': 'উ', 'ā': 'আː', 'ī': 'ঈː', 'ū': 'ঊː'}
SHORT = {'ā': 'a', 'ī': 'i', 'ū': 'u', 'a': 'a', 'i': 'i', 'u': 'u'}
PUNCT_BN = {'،': ',', '؟': '?', '.': '।', '!': '!', '؛': ';', ':': ':', '«': '«', '»': '»'}
PUNCT_EN = {'،': ',', '؟': '?', '.': '.', '!': '!', '؛': ';', ':': ':', '«': '«', '»': '»'}

WARN = []


def fr_clean(s):
    s = s.replace('لِ|ال', 'لِل').replace('|', '')
    return s


def letters(part):
    out = []
    for ch in part:
        if ch == TATWEEL:
            continue
        if ch in MARKS:
            if not out:
                raise ValueError('mark without letter in ' + part)
            out[-1][1].append(ch)
        else:
            out.append([ch, []])
    return out


def parse_part(part, first_part):
    """Return list of phonemes for one orthographic chunk. May start with ('W', v) for wasl."""
    L = letters(part)
    bare = ''.join(l for l, m in L)
    ph = []
    i = 0
    # Allah special cases
    if bare in ('الله', 'لله'):
        last = L[-1][1]
        if bare == 'الله':
            ph = [('W', 'a'), 'l', 'l', 'ā', 'h']
        else:
            ph = ['l', 'i', 'l', 'l', 'ā', 'h']
        ph += vowel_marks(last)
        return ph
    # article
    if len(L) >= 3 and L[0][0] in 'اٱ' and not L[0][1] and L[1][0] == 'ل':
        nxt = L[2]
        ph.append(('W', 'a'))
        if nxt[0] in SUN and SHADDA in nxt[1]:
            c = CONS[nxt[0]]
            ph += [c, '-']
            nxt[1].remove(SHADDA)
        elif nxt[0] in SUN and nxt[0] != 'ل':
            WARN.append('sun letter without shadda: ' + part)
            c = CONS[nxt[0]]
            ph += [c, '-']
        else:
            if nxt[0] == 'ل' and SHADDA in nxt[1]:
                ph += ['l', '-']
                nxt[1].remove(SHADDA)
            else:
                ph += ['l', '-']
        i = 2
    elif L and L[0][0] in 'اٱ':
        # hamzat al-wasl
        v = [m for m in L[0][1] if m in (FATHA, KASRA, DAMMA)]
        vv = {FATHA: 'a', KASRA: 'i', DAMMA: 'u'}[v[0]] if v else 'i'
        ph.append(('W', vv))
        i = 1
    prev_tanwin_an = False
    while i < len(L):
        ch, mk = L[i]
        at_start = (i == 0)
        if ch == 'ا':
            if prev_tanwin_an:
                pass
            elif ph and ph[-1] == 'a':
                ph[-1] = 'ā'
            elif ph and ph[-1] == 'ū':
                pass  # waw al-jamaa alif
            elif ph and ph[-1] == 'ā':
                pass
            else:
                ph.append('ā')
                WARN.append('alif without fatha: ' + part)
            prev_tanwin_an = False
            i += 1
            continue
        if ch == 'ى':
            if prev_tanwin_an:
                pass
            elif ph and ph[-1] == 'a':
                ph[-1] = 'ā'
            else:
                ph.append('ā')
            prev_tanwin_an = False
            i += 1
            continue
        if ch == 'آ':
            ph += ['ʾ', 'ā']
            i += 1
            continue
        has_v = any(m in (FATHA, KASRA, DAMMA, AN, IN, UN, DAGGER) for m in mk)
        if ch == 'و' and not has_v and SHADDA not in mk and ph and ph[-1] == 'u':
            ph[-1] = 'ū'
            i += 1
            continue
        if ch == 'ي' and not has_v and SHADDA not in mk and ph and ph[-1] == 'i':
            ph[-1] = 'ī'
            i += 1
            continue
        c = CONS.get(ch)
        if c is None:
            raise ValueError('unknown letter %r in %s' % (ch, part))
        ph.append(c)
        if SHADDA in mk:
            ph.append(c)
        if ch == 'إ' and not has_v:
            ph.append('i')
        vm = vowel_marks(mk)
        ph += vm
        prev_tanwin_an = (vm == ['a', 'N'])
        i += 1
    return ph


def vowel_marks(mk):
    out = []
    for m in mk:
        if m == FATHA: out.append('a')
        elif m == KASRA: out.append('i')
        elif m == DAMMA: out.append('u')
        elif m == AN: out += ['a', 'N']
        elif m == IN: out += ['i', 'N']
        elif m == UN: out += ['u', 'N']
        elif m == DAGGER:
            if out and out[-1] == 'a':
                out[-1] = 'ā'
            else:
                out.append('ā')
    return out


def parse_word(w):
    parts = w.split('|')
    ph = []
    for k, p in enumerate(parts):
        if k > 0 and p.startswith('ال') and parts[k - 1].endswith('ل' + KASRA) and False:
            pass
        sub = parse_part(p, k == 0)
        if k == 0:
            ph = sub
        else:
            if sub and isinstance(sub[0], tuple):
                # proclitic + wasl: merge
                sub = sub[1:]
                ph = ph + sub
            else:
                ph = ph + ['='] + sub
    return ph


def pause(ph):
    ph = list(ph)
    if len(ph) >= 2 and ph[-1] == 'N':
        v = ph[-2]
        ph = ph[:-2]
        if v == 'a':
            if ph and ph[-1] == 'T':
                pass
            else:
                ph.append('ā')
    elif ph and ph[-1] in ('a', 'i', 'u'):
        ph = ph[:-1]
    if ph and ph[-1] == 'T':
        ph[-1] = 'h'
    if len(ph) >= 3 and ph[-3:] == ['i', 'y', 'y']:
        ph = ph[:-3] + ['ī']
    return ph


def finish(ph):
    out = []
    for k, p in enumerate(ph):
        if p == 'T':
            nxt = ph[k + 1] if k + 1 < len(ph) else None
            out.append('t')
            if nxt not in VOW:
                WARN.append('ta marbuta without vowel mid-phrase')
        elif p == 'N':
            out.append('n')
        else:
            out.append(p)
    return out


def phrase_phonemes(s, do_pause=True):
    """Return list of items: ('w', phonemes) or ('p', punct)."""
    toks = re.findall(r'[^\s،؟.!؛:«»]+|[،؟.!؛:«»]', s)
    items = []
    for t in toks:
        if t in PUNCT_BN:
            items.append(['p', t])
        else:
            items.append(['w', parse_word(t)])
    # pause positions
    n = len(items)
    for k, it in enumerate(items):
        if it[0] != 'w':
            continue
        nxt = items[k + 1] if k + 1 < n else None
        if do_pause and (nxt is None or (nxt[0] == 'p' and nxt[1] in '،؟.!؛:»')):
            it[1] = pause(it[1])
    # wasl / elision
    res = []  # list of ['w', ph] / ['p', x]
    for k, it in enumerate(items):
        if it[0] == 'w':
            ph = it[1]
            if ph and isinstance(ph[0], tuple):
                prev = res[-1] if res else None
                if prev and prev[0] == 'w' and prev[1] and prev[1][-1] in VOW:
                    prev[1][-1] = SHORT[prev[1][-1]]
                    prev[1].extend(ph[1:])
                    continue
                else:
                    if prev and prev[0] == 'w':
                        WARN.append('wasl after consonant: ' + s)
                    ph = [ph[0][1]] + ph[1:]
            res.append(['w', ph])
        else:
            res.append(it)
    return res


def render_bn_word(ph):
    out = []
    n = len(ph)
    k = 0
    start = True
    while k < n:
        p = ph[k]
        if p in ('-', '='):
            out.append('-')
            start = True
            k += 1
            continue
        if p in VOW:
            nxt = ph[k + 1] if k + 1 < n else None
            nn = ph[k + 2] if k + 2 < n else None
            if p == 'a' and nxt in ('y', 'w') and nn not in VOW and nn != nxt:
                glide = 'ই' if nxt == 'y' else 'ও'
                out.append(('আ' if start else 'া') + glide)
                k += 2
                start = False
                continue
            out.append(INDEP[p] if start else MATRA[p])
            start = False
            k += 1
            continue
        # consonant
        nxt = ph[k + 1] if k + 1 < n else None
        if p == 'ʾ' and start:
            k += 1
            continue  # vowel stays independent
        if p == 'y':
            if nxt == 'y':
                v = ph[k + 2] if k + 2 < n else None
                if v in VOW:
                    out.append('য়্য' if not start else 'ইয়্য')
                    out.append(MATRA[v])
                    k += 3
                    start = False
                    continue
                out.append('ই')
                k += 2
                start = False
                continue
            if nxt in VOW:
                out.append(('ইয়' if start else 'য়') + MATRA[nxt])
                k += 2
                start = False
                continue
            out.append('ই')
            k += 1
            start = False
            continue
        if p == 'w':
            if nxt in VOW:
                out.append('ওয়' + MATRA[nxt])
                k += 2
                start = False
                continue
            out.append('ও')
            k += 1
            start = False
            continue
        b = BN_CONS[p]
        if nxt == p:
            if p in CONJ_OK:
                b = b + '্' + b
            else:
                b = b + b
            k += 1
            nxt = ph[k + 1] if k + 1 < n else None
        out.append(b)
        k += 1
        if p in ('ʿ', 'ʾ'):
            start = True  # following vowel independent
        else:
            start = False
        if nxt in VOW:
            # handled by vowel branch with start flag
            pass
    s = ''.join(out)
    return s


def render_en_word(ph):
    out = []
    start = True
    for k, p in enumerate(ph):
        if p in ('-', '='):
            out.append('-')
            start = True
            continue
        if p == 'ʾ' and start:
            continue
        out.append(p)
        start = False
    return ''.join(out)


def pron(s, do_pause=True):
    items = phrase_phonemes(s, do_pause)
    bn, en = [], []
    for it in items:
        if it[0] == 'w':
            ph = finish(it[1])
            bn.append(('w', render_bn_word(ph)))
            en.append(('w', render_en_word(ph)))
        else:
            bn.append(('p', PUNCT_BN[it[1]]))
            en.append(('p', PUNCT_EN[it[1]]))
    return join(bn), join(en)


def join(seq):
    out = ''
    for k, (t, x) in enumerate(seq):
        if t == 'w':
            if out and not out.endswith(('«', ' ')):
                out += ' '
            out += x
        else:
            if x == '«':
                if out:
                    out += ' '
                out += x
            else:
                out += x
    return out.strip()


if __name__ == '__main__':
    tests = [('سَأَلَ', False), ('بَاب', True), ('تَمْر', True), ('ثَلَاثَة', True), ('جَمِيل', True), ('حَلِيب', True),
             ('خُبْز', True), ('ذَهَب', True), ('ضَيْف', True), ('ظُهْر', True), ('عَيْن', True), ('غَزَال', True),
             ('مَاء', True), ('وَلَد', True), ('يَد', True), ('يَوْم', True), ('مُدَرِّس', True), ('أُمّ', True),
             ('الشَّمْس', True), ('النُّور', True), ('فِي الْبَيْتِ', False), ('مَدْرَسَة', True),
             ('مَدْرَسَةُ الْبَنَاتِ', True), ('كَتَبْتُ', False), ('شُكْرًا', True), ('عَرَبِيّ', True),
             ('عَرَبِيَّة', True), ('سَيَّارَة', True), ('قُرْآن', True), ('بِسْمِ اللّٰهِ', True),
             ('إِنْ شَاءَ اللّٰهُ', True), ('الْحَمْدُ لِلّٰهِ', True), ('مَا اسْمُكَ؟', True), ('وَ|عَلَيْكُمُ السَّلَامُ', True),
             ('مَعَ السَّلَامَةِ', True), ('هٰذَا كِتَابٌ.', True), ('أَهْلًا وَ|سَهْلًا', True), ('مَعْنًى', True),
             ('كَيْفَ حَالُكَ؟', True), ('شْلُونَك؟', True), ('يَكْتُبُ', False), ('بِ|الْعَرَبِيَّةِ', True), ('لِ|الْبَيْتِ', True),
             ('مُسْتَشْفًى', True), ('سُؤَال', True), ('قُوَّة', True), ('مَسْؤُول', True)]
    for t, p in tests:
        print(fr_clean(t), '=', *pron(t, p))
    print(WARN)
