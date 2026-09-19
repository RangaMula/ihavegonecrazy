import re, glob, csv, json
num=r'-?[\d,]+\.\d{2}'
txre=re.compile(r'^\s*(\d{2}-[A-Za-z]{3}-\d{4})\s+(.*?)\s+('+num+r')\s+('+num+r')\s*$')
HDR=re.compile(r'^\s*(TRN\. DATE|Page|Account No|Product Name|Period From|Currency|Branch Code|Customer ID|A\.M MINHAZ|HOUSE NO|3, MIRPUR|Dhanmondi Branch|House 21)')
def f(s): return float(s.replace(',',''))
def clean(line):
    line=line.replace('e-statement','').replace('e-statemen','')
    line=re.sub(r'(?<=[\d,])[a-zA-Z](?=[\d,])','',line)
    return line
allrows=[]
for txt in ['dec_106145XXXXXX7_1824405_31DEC25.txt','dec_106145XXXXXX7_1824405_30JUN26.txt','dec_106145XXXXXX7_1824405_30JUN25.txt']:
    period=re.search(r'Period From : (.*?)\s{2,}', open(txt).read()).group(1).strip()
    rows=[]; prev=None; cur=None; dups=0
    for line in open(txt):
        line=clean(line.rstrip('\n'))
        if re.match(r'^\s*\d{2}-[A-Za-z]{3}-\d{4}\s', line):
            m=txre.match(line)
            if not m: print('UNPARSED',txt,line); cur=None; continue
            date,desc,amt,bal=m.groups(); amt=f(amt); bal=f(bal)
            if 'Opening Balance' in desc: prev=bal; cur=None; continue
            delta=round(bal-prev,2)
            if delta==0: dups+=1; cur=None; continue   # repeated line at page break
            kind='CR' if delta>0 else 'DR'
            if abs(abs(delta)-abs(amt))>0.011: print('MISMATCH',txt,line,delta,amt)
            cur={'stmt':period,'date':date,'desc':desc.strip(),'detail':'','type':kind,'amount':abs(delta),'reversal':amt<0,'balance':bal}
            rows.append(cur); prev=bal
        elif cur is not None and line.strip() and not HDR.match(line) and '\f' not in line:
            cur['detail']+=(' ' if cur['detail'] else '')+line.strip()
    cr=sum(r['amount'] for r in rows if r['type']=='CR'); dr=sum(r['amount'] for r in rows if r['type']=='DR')
    print(f"{period}: {len(rows)} txns, {dups} page-break dups skipped, credits {cr:,.2f}, debits {dr:,.2f}, closing {rows[-1]['balance']:,.2f}")
    if txt.endswith('30JUN25.txt'):
        # cross-check against first half of year statement
        a=[(r['date'],r['type'],r['amount'],r['balance']) for r in rows]
        b=[(r['date'],r['type'],r['amount'],r['balance']) for r in allrows if r['stmt'].startswith('01-JAN-25') and r['balance'] is not None][:len(a)]
        print('H1-2025 cross-check identical:', a==b)
        continue
    allrows+=rows
with open('transactions.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(allrows[0].keys())); w.writeheader(); w.writerows(allrows)
json.dump(allrows,open('transactions.json','w'),indent=1)
print('total rows', len(allrows))
