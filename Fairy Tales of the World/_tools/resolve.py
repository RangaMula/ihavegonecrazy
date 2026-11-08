import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from catalog import CATALOG
HERE=os.path.dirname(os.path.abspath(__file__))
IDMAP={f[:-5].rsplit('_',1)[-1]:f[:-5] for f in os.listdir(os.path.join(HERE,'meta'))}
def people(m):
    out=[]
    def add(role,x):
        if isinstance(x,list):
            for i in x: add(role,i)
        elif isinstance(x,dict):
            out.append((role,x.get('agent_name'),x.get('birthdate'),x.get('deathdate')))
    cr=m.get('creator') or {}
    if isinstance(cr,dict):
        for k,v in cr.items(): add(k,v)
    co=m.get('contributor') or {}
    if isinstance(co,dict):
        for k,v in co.items(): add(k,v)
    return out
def load(gid):
    r=IDMAP.get(str(gid))
    if not r: return None,None
    return r,json.load(open(os.path.join(HERE,'meta',r+'.json')))
if __name__=='__main__':
    for (cont,folder),ids in CATALOG.items():
        print(f"== {folder}")
        for g in ids:
            r,m=load(g)
            if not r: print(f"   {g}: MISSING"); continue
            print(f"   {g}: {r[:50]} | {[(p[0],p[1],p[3]) for p in people(m)]}")
