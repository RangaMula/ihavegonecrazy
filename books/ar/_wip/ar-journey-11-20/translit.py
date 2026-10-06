# Vowelled Arabic -> Bangla pronunciation (STYLE §3) and simplified ALA-LC (STYLE §4).
import re

FATHA, DAMMA, KASRA, SUKUN, SHADDA = 'َ', 'ُ', 'ِ', 'ْ', 'ّ'
FATHATAN, DAMMATAN, KASRATAN, DAGGER = 'ً', 'ٌ', 'ٍ', 'ٰ'
HARAKAT = set([FATHA, DAMMA, KASRA, SUKUN, SHADDA, FATHATAN, DAMMATAN, KASRATAN, DAGGER])

BN = {'ب': 'ব', 'ت': 'ত', 'ث': 'থ়', 'ج': 'জ', 'ح': 'হ়', 'خ': 'খ়', 'د': 'দ', 'ذ': 'দ়', 'ر': 'র',
      'ز': 'জ়', 'س': 'স', 'ش': 'শ', 'ص': 'স়', 'ض': 'ড', 'ط': 'ট', 'ظ': 'য', 'غ': 'গ়', 'ف': 'ফ়',
      'ق': 'ক়', 'ك': 'ক', 'ل': 'ল', 'م': 'ম', 'ن': 'ন', 'ه': 'হ', 'ة': 'ত'}
EN = {'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': 'ḥ', 'خ': 'kh', 'د': 'd', 'ذ': 'dh', 'ر': 'r',
      'ز': 'z', 'س': 's', 'ش': 'sh', 'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ', 'ظ': 'ẓ', 'غ': 'gh', 'ف': 'f',
      'ق': 'q', 'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'ة': 't', 'ع': 'ʿ', 'و': 'w', 'ي': 'y',
      'ء': 'ʾ'}
SUN = set('تثدذرزسشصضطظلن')
HAMZAS = set('ءأإؤئ')
# vowel kinds: a i u A I U (long), ay aw
SIGN = {'a': 'া', 'i': 'ি', 'u': 'ু', 'A': 'াː', 'I': 'ীː', 'U': 'ূː', 'ay': 'াই', 'aw': 'াও'}
INDEP = {'a': 'আ', 'i': 'ই', 'u': 'উ', 'A': 'আː', 'I': 'ঈː', 'U': 'ঊː', 'ay': 'আই', 'aw': 'আও'}
ENV = {'a': 'a', 'i': 'i', 'u': 'u', 'A': 'ā', 'I': 'ī', 'U': 'ū', 'ay': 'ay', 'aw': 'aw'}
SHORT = {'a': FATHA, 'i': KASRA, 'u': DAMMA}


def parse(word):
    """Split a word into (letter, marks) units."""
    units = []
    for ch in word:
        if ch in HARAKAT and units:
            units[-1][1].append(ch)
        elif ch == 'ـ':
            continue
        else:
            units.append([ch, []])
    return units


def vowel_of(marks):
    for m, v in ((FATHA, 'a'), (KASRA, 'i'), (DAMMA, 'u')):
        if m in marks:
            return v
    for m, v in ((FATHATAN, 'an'), (KASRATAN, 'in'), (DAMMATAN, 'un')):
        if m in marks:
            return v
    if DAGGER in marks:
        return 'A'
    return None


def syllabify(word, pause, after_vowel_join=False):
    """Return list of segments: ('C', letter, double) / ('V', kind) / ('-',) for article hyphen."""
    u = parse(word)
    segs = []
    i = 0
    n = len(u)
    # special: Allah
    plain = ''.join(c for c, _ in u)
    if plain in ('الله', 'لله'):
        pass
    while i < n:
        c, m = u[i]
        # article / wasl alif
        if c == 'ا' and not m and (i == 0 or (segs and segs[-1][0] == 'V')) and i + 1 < n:
            c2, m2 = u[i + 1]
            if c2 == 'ل' and KASRA in m2 and i + 2 < n and u[i + 2][0] == 'ا' and not u[i + 2][1] and (i == 0 or segs[-1][0] == 'V'):
                if not (i > 0 or after_vowel_join):
                    segs.append(('V', 'a'))
                segs.append(('C', 'ل', False))
                segs.append(('-',))
                segs.append(('V', 'i'))
                i += 3
                continue
            is_article = c2 == 'ل' and (SUKUN in m2 or (i + 2 < n and SHADDA in u[i + 2][1] and u[i + 2][0] in SUN) or (not m2 and i + 2 < n))
            if is_article and (i == 0 or segs[-1][0] == 'V'):
                prev_v = i > 0 or after_vowel_join
                if i + 2 < n and u[i + 2][0] in SUN and SHADDA in u[i + 2][1]:
                    if not prev_v:
                        segs.append(('V', 'a'))
                    segs.append(('C', u[i + 2][0], False))
                    segs.append(('-',))
                    i += 2  # now at sun letter, which carries shadda -> treat as single consonant after hyphen
                    c3, m3 = u[i]
                    u[i] = [c3, [x for x in m3 if x != SHADDA]]
                    continue
                if not prev_v:
                    segs.append(('V', 'a'))
                segs.append(('C', 'ل', False))
                segs.append(('-',))
                i += 2
                # word-initial hamza after article: drop the glottal mark
                if i < n and u[i][0] in 'أإآ':
                    segs.append(('ART_HAMZA',))
                continue
            if i == 0 and not after_vowel_join and SUKUN in m2:
                segs.append(('V', 'i'))  # hamzat al-wasl of ism/ibn type
                i += 1
                continue
            if i == 0 and after_vowel_join and SUKUN in m2:
                i += 1
                continue
        if c == 'ا' and m and i == 0 and (KASRA in m or DAMMA in m or FATHA in m):
            # explicit wasl alif with vowel (اِسْتَمَعَ)
            if not after_vowel_join:
                segs.append(('V', vowel_of(m)))
            i += 1
            continue
        if c == 'آ':
            if i > 0 and not (segs and segs[-1][0] == 'ART_HAMZA'):
                segs.append(('C', 'ء', False))
            segs.append(('V', 'A'))
            i += 1
            continue
        if c in HAMZAS:
            initial = (i == 0) or (segs and segs[-1][0] == 'ART_HAMZA')
            if c in 'أإ' and initial:
                v = vowel_of(m) or ('i' if c == 'إ' else 'a')
                segs.append(('V', v))
                i += 1
                i = _long(u, i, v, segs, pause, n)
                continue
            segs.append(('C', 'ء', SHADDA in m))
            v = vowel_of(m)
            if c == 'أ' and v is None and i + 1 < n and u[i + 1][0] == 'ا':
                v = 'a'
            if v:
                _vowel(segs, v, pause and i == n - 1)
                i += 1
                i = _long(u, i, v, segs, pause, n)
            else:
                i += 1
            continue
        if c == 'ا':
            # long a (after a consonant), or tanwin-alif
            if segs and segs[-1] == ('V', 'an'):
                if pause and i == n - 1:
                    segs[-1] = ('V', 'A')
                i += 1
                continue
            if segs and segs[-1][0] == 'V' and segs[-1][1] == 'a':
                segs[-1] = ('V', 'A')
            else:
                segs.append(('V', 'A'))
            i += 1
            continue
        if c == 'ى':
            if segs and segs[-1][0] == 'V' and segs[-1][1] in ('a', 'A'):
                segs[-1] = ('V', 'A')
            elif segs and segs[-1] == ('V', 'an'):
                segs[-1] = ('V', 'A') if pause and i == n - 1 else ('V', 'an')
            else:
                segs.append(('V', 'A'))
            i += 1
            continue
        if c == 'ة':
            v = vowel_of(m)
            if v is None or (pause and i == n - 1):
                segs.append(('C', 'ه', False))
            else:
                segs.append(('C', 'ة', False))
                _vowel(segs, v, False)
            i += 1
            continue
        if c in 'وي' and not (set(m) & {FATHA, KASRA, DAMMA, FATHATAN, KASRATAN, DAMMATAN, SHADDA}):
            prev = segs[-1] if segs else None
            if prev and prev[0] == 'V' and prev[1] == ('u' if c == 'و' else 'i'):
                segs[-1] = ('V', 'U' if c == 'و' else 'I')
                i += 1
                continue
            if prev and prev[0] == 'V' and prev[1] == 'a':
                segs[-1] = ('V', 'aw' if c == 'و' else 'ay')
                i += 1
                continue

        if c == 'ع' or c in BN or c in 'وي':
            dbl = SHADDA in m
            v = vowel_of(m)
            # final nisba -iyy at pause -> ī
            if c == 'ي' and dbl and segs and segs[-1] == ('V', 'i') and (i == n - 1) and (pause or v is None):
                segs[-1] = ('V', 'I')
                i += 1
                continue
            segs.append(('C', c, dbl))
            if v:
                _vowel(segs, v, pause and i == n - 1)
                i += 1
                i = _long(u, i, v, segs, pause, n)
            else:
                i += 1
            continue
        if c in '؟،.!?,:;«»"' or c == ' ':
            i += 1
            continue
        raise ValueError('unknown char %r in %r' % (c, word))
    return segs


def _vowel(segs, v, at_pause):
    if at_pause:
        if v in ('a', 'i', 'u', 'un', 'in'):
            return
        if v == 'an':
            segs.append(('V', 'an'))  # resolved by following alif
            return
    segs.append(('V', v))


def _long(u, i, v, segs, pause, n):
    return i


def render(segs):
    bn, en = [], []
    prev_kind = None  # 'C', 'V', '-'
    k = 0
    while k < len(segs):
        s = segs[k]
        if s[0] == 'ART_HAMZA':
            k += 1
            continue
        if s[0] == '-':
            bn.append('-')
            en.append('-')
            prev_kind = '-'
            k += 1
            continue
        if s[0] == 'C':
            c, dbl = s[1], s[2]
            nxt = segs[k + 1] if k + 1 < len(segs) else None
            has_v = nxt is not None and nxt[0] == 'V'
            vk = nxt[1] if has_v else None
            tanw = None
            if vk in ('an', 'in', 'un'):
                tanw = vk
                vk = vk[0]
            if c in ('ع', 'ء'):
                mark = 'ʿ' if c == 'ع' else 'ʾ'
                bn.append(mark + (mark if dbl else ''))
                en.append(mark + (mark if dbl else ''))
                if vk:
                    bn.append(INDEP[vk])
                    en.append(ENV[vk])
            elif c in 'وي':
                if c == 'و':
                    base = 'ওয়'
                    if dbl:
                        bn.append('ও')
                else:
                    base = 'য়'
                    if dbl:
                        base = 'য়্য'
                    elif prev_kind != 'V':
                        base = 'ইয়'
                if vk:
                    bn.append(base + SIGN[vk])
                else:
                    bn.append('ই' if c == 'ي' else 'ও')
                en.append(EN[c] * (2 if dbl else 1))
                if vk:
                    en.append(ENV[vk])
            else:
                b = BN[c] if c != 'ه' else 'হ'
                if dbl:
                    bn.append(b + b if c == 'ر' else b + '্' + b)
                else:
                    bn.append(b)
                en.append(EN[c] * (2 if dbl else 1) if c != 'ه' else ('hh' if dbl else 'h'))
                if vk:
                    bn.append(SIGN[vk])
                    en.append(ENV[vk])
            if tanw:
                bn.append('ন')
                en.append('n')
            prev_kind = 'V' if vk else 'C'
            k += 2 if has_v else 1
            continue
        if s[0] == 'V':
            vk = s[1]
            tanw = None
            if vk in ('an', 'in', 'un'):
                tanw = vk
                vk = vk[0]
            bn.append(INDEP[vk])
            en.append(ENV[vk])
            if tanw:
                bn.append('ন')
                en.append('n')
            prev_kind = 'V'
            k += 1
            continue
    return ''.join(bn), ''.join(en)


PUNCT_BN = {'؟': '?', '،': ',', '.': '।', '!': '!', ':': ':', '«': '«', '»': '»'}
PUNCT_EN = {'؟': '?', '،': ',', '.': '.', '!': '!', ':': ':', '«': '«', '»': '»'}


def ends_vowel(bn):
    return bool(bn) and bn[-1] in 'ািুীূːআইউএওয়' and not bn.endswith('ʿ')


def shorten(bn, en):
    for lng, sh in (('াː', 'া'), ('ীː', 'ি'), ('ূː', 'ু'), ('আː', 'আ'), ('ঈː', 'ই'), ('ঊː', 'উ')):
        if bn.endswith(lng):
            bn = bn[:-len(lng)] + sh
            break
    for lng, sh in (('ā', 'a'), ('ī', 'i'), ('ū', 'u')):
        if en.endswith(lng):
            en = en[:-1] + sh
            break
    return bn, en


def is_wasl(word):
    u = parse(word)
    if len(u) < 2 or u[0][0] != 'ا' or u[0][1]:
        return False
    return True


def tr(text, pause_end=True):
    """Transliterate a phrase/sentence. Pause before punctuation and at the end."""
    tokens = re.findall(r'[^\s؟،.!:«»]+|[؟،.!:«»]', text.strip())
    out_bn, out_en = [], []
    for idx, tok in enumerate(tokens):
        if tok in PUNCT_BN:
            if tok == '«':
                out_bn.append(' «'); out_en.append(' «')
            else:
                out_bn.append(PUNCT_BN[tok]); out_en.append(PUNCT_EN[tok])
            continue
        nxt = tokens[idx + 1] if idx + 1 < len(tokens) else None
        pause = (nxt is None and pause_end) or (nxt is not None and nxt in '؟،.!:»')
        join = False
        if is_wasl(tok) and out_bn and out_bn[-1] not in ('?', ',', '।', '!', ':', ' «'):
            if not ends_vowel(out_bn[-1]):
                # helping vowel i before hamzat al-wasl
                if out_bn[-1][-1] in 'ʿʾ':
                    out_bn[-1] += 'ই'
                else:
                    out_bn[-1] += 'ি'
                out_en[-1] += 'i'
            join = True
        plain = ''.join(c for c in tok if c not in HARAKAT)
        if plain in ('الله', 'اللّٰه'):
            if join:
                b, e = 'লা-হ', 'lāh'
                pb, pe = shorten(out_bn[-1], out_en[-1])
                out_bn[-1] = pb + 'ল্লাːহ'; out_en[-1] = pe + 'llāh'
                continue
            out_bn.append(' আল্লাːহ' if out_bn else 'আল্লাːহ'); out_en.append(' allāh' if out_en else 'allāh')
            continue
        if plain in ('لله',):
            b, e = 'লিল্লাːহ', 'lillāh'
            out_bn.append((' ' if out_bn else '') + b); out_en.append((' ' if out_en else '') + e)
            continue
        segs = syllabify(tok, pause, after_vowel_join=join)
        b, e = render(segs)
        if join:
            pb, pe = shorten(out_bn[-1], out_en[-1])
            out_bn[-1] = pb + b
            out_en[-1] = pe + e
        else:
            out_bn.append((' ' if out_bn and out_bn[-1] != ' «' else '') + b)
            out_en.append((' ' if out_en and out_en[-1] != ' «' else '') + e)
    bn = ''.join(out_bn).strip()
    en = ''.join(out_en).strip()
    return bn, en


if __name__ == '__main__':
    tests = ['كِتَاب', 'سَأَلَ', 'ثَلَاثَة', 'حَلِيب', 'ضَيْف', 'ظُهْر', 'عَيْن', 'مَاء', 'يَد', 'وَلَد', 'يَوْم',
             'مُدَرِّس', 'أُمّ', 'الشَّمْس', 'النُّور', 'فِي الْبَيْتِ', 'مَدْرَسَة', 'مَدْرَسَةُ الْبَنَاتِ', 'كَتَبْتُ',
             'سَيِّد', 'عَرَبِيّ', 'اللُّغَةُ الْعَرَبِيَّةُ جَمِيلَةٌ جِدًّا.', 'شُكْرًا', 'الْأَرْض', 'قُوَّة', 'أَوَّل',
             'هٰذَا كِتَابٌ.', 'عَلَى الطَّاوِلَةِ', 'السَّمَاء', 'مَعْنَى', 'اِسْتَمَعَ', 'بِسْمِ اللهِ', 'الْحَمْدُ لِلّٰهِ',
             'مَرْيَم', 'سُؤَال', 'رَئِيس', 'قُرْآن', 'وَالشَّمْسُ', 'ذَهَبَ إِلَى السُّوقِ.', 'يَكْتُبُ', 'مُسْتَشْفًى', 'هَوَاء', 'حَيَاة']
    for t in tests:
        print(t, '=', *tr(t))
