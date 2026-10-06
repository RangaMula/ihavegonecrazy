import json, re, sys, importlib
sys.path.insert(0, '.')
import translit as T

GEN = {'m': 'পুং', 'f': 'স্ত্রী'}


def P(ar, pause=True):
    bn, en = T.pron(ar, pause)
    return bn, en


def ref(ar, pause=True):
    """'ar (bn_pron)' with fr cleaned."""
    bn, _ = P(ar, pause)
    return '%s (%s)' % (T.fr_clean(ar), bn)


def subst(text):
    def rep(m):
        x = m.group(1)
        np = x.endswith('!')
        if np:
            x = x[:-1]
        return ref(x, not np)
    return re.sub(r'\{([^{}]+)\}', rep, text)


def note(spec):
    spec = spec.strip()
    if not spec:
        return None
    parts = []
    free = None
    if ';' in spec:
        head, free = spec.split(';', 1)
        head = head.strip()
        free = free.strip()
    else:
        head = spec
    if head:
        kind, _, rest = head.partition(':')
        if kind in ('m', 'f'):
            if rest == '-':
                parts.append(GEN[kind] + ' · বহুবচন নেই')
            else:
                parts.append(GEN[kind] + ' · বহুবচন: ' + ref(rest))
        elif kind == 'v':
            parts.append('বর্তমান: ' + ref(rest, False))
        elif kind == 'a':
            bits = rest.split(':')
            parts.append('স্ত্রী: ' + ref(bits[0]))
            if len(bits) > 1:
                parts.append('বহুবচন: ' + ref(bits[1]))
        elif kind == 'pl':
            parts.append('বহুবচন রূপ · একবচন: ' + ref(rest))
        elif kind == 'coll':
            g, one = rest.split(':', 1)
            parts.append(GEN[g] + ' · সমষ্টিবাচক · একটি: ' + ref(one))
        else:
            raise ValueError('bad note spec: ' + spec)
    if free:
        parts.append(subst(free))
    return ' · '.join(parts)


LINT = []
def lint(ar):
    for w in re.split(r'[\s،؟.!؛:«»]+', ar):
        b = re.sub('[\u064b-\u0652\u0670]', '', w)
        if re.match('^[وفبلك]ال', b) and '|' not in w and b not in ('الله', 'والدان', 'والد', 'والدة'):
            LINT.append('proclitic+article without |: ' + ar)


def word(line, kind):
    f = [x.strip() for x in line.split('~')]
    ar = f[0]
    np = ar.startswith('!')
    if np:
        ar = ar[1:]
    if kind == 'F':
        ar, bn, en = f[0:3]
        nt = f[3] if len(f) > 3 else ''
    else:
        bn, en, icon, story, link, src = f[1:7]
        nt = f[7] if len(f) > 7 else ''
    ar = ar.lstrip('!')
    if nt.strip().startswith('v:'):
        np = True
    lint(ar)
    bp, ep = P(ar, not np)
    o = {'fr': T.fr_clean(ar), 'bn_pron': bp, 'en_pron': ep, 'bn': bn, 'en': en}
    n = note(nt)
    if n:
        o['note_bn'] = n
    if kind == 'C':
        o['icon'] = icon
        o['story_bn'] = subst(story)
        if link:
            o['link_bn'] = subst(link)
        o['source_hint'] = src
    return o


def rows(block, kind='F'):
    return [word(l, kind) for l in block.strip().split('\n') if l.strip()]


def sent(block):
    out = []
    for l in block.strip().split('\n'):
        if not l.strip():
            continue
        ar, bn, en = [x.strip() for x in l.split('~')]
        lint(ar)
        bp, ep = P(ar, True)
        out.append({'fr': T.fr_clean(ar), 'bn_pron': bp, 'en_pron': ep, 'bn': bn, 'en': en})
    return out


def section(S):
    o = {'no': S['no'], 'stage': S['stage'], 'title_bn': S['title_bn'], 'title_en': S['title_en'],
         'scene_bn': subst(S['scene_bn']), 'can_do_bn': S['can_do_bn'], 'sets': []}
    for code, kind, tb, te, block in S['sets']:
        o['sets'].append({'code': code, 'kind': kind, 'title_bn': tb, 'title_en': te, 'words': rows(block, kind)})
    o['say_now'] = sent(S['say_now'])
    o['mission_bn'] = subst(S['mission_bn'])
    q = []
    for qb, a in S['quiz']:
        npq = a.startswith('!')
        a = a.lstrip('!')
        a2 = a
        if re.search('[\u0600-\u06ff]', a):
            prs = [P(x.strip(), not npq)[0] for x in a.split(' / ')]
            a2 = '%s (%s)' % (T.fr_clean(a), ' / '.join(prs))
        q.append({'q_bn': subst(qb), 'a': a2})
    o['quiz'] = q
    o['stamp'] = S['stamp']
    return o


if __name__ == '__main__':
    mods = sys.argv[2:]
    secs = []
    miles = []
    for m in mods:
        M = importlib.import_module(m)
        for k in sorted(dir(M)):
            if re.fullmatch(r'S\d+', k):
                secs.append(section(getattr(M, k)))
            if k == 'MILESTONES':
                for ms in M.MILESTONES:
                    miles.append({'after_section': ms['after_section'], 'total': ms['total'], 'title_bn': ms['title_bn'],
                                  'title_fr': ms['title_fr'], 'celebration_bn': ms['celebration_bn'],
                                  'reading': sent(ms['reading'])})
    secs.sort(key=lambda s: s['no'])
    json.dump({'sections': secs, 'milestones': miles}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    print('sections', len(secs), 'milestones', len(miles))
    for w in sorted(set(LINT)):
        print('LINT', w)
    for w in sorted(set(T.WARN)):
        print('WARN', w)
