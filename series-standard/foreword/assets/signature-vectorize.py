# Vectorizes the author's signature (signature-source.jpg) into signature.svg. Chosen output: T=130.
import numpy as np, potrace
from PIL import Image, ImageFilter
src=Image.open('signature-source.jpg').convert('L')
print('ink range', np.array(src).min(), np.percentile(np.array(src),5))
K=8
big=src.resize((src.width*K,src.height*K),Image.BICUBIC).filter(ImageFilter.GaussianBlur(K*0.8))
a=np.array(big)
for T in (130,150):
    bm=potrace.Bitmap(a>=T)
    path=bm.trace(turdsize=K*K*4, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.3, opticurve=True, opttolerance=0.4)
    parts=[]
    for c in path:
        s=c.start_point; d=[f"M{s.x:.1f},{s.y:.1f}"]
        for seg in c.segments:
            if seg.is_corner: d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
            else: d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        d.append("Z"); parts.append("".join(d))
    ys,xs=np.where(a<T); pad=K*4
    x0,y0,x1,y1=xs.min()-pad,ys.min()-pad,xs.max()+pad,ys.max()+pad
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1-x0} {y1-y0}"><path fill="#1b2a52" fill-rule="evenodd" d="{"".join(parts)}"/></svg>'
    open(f'sig_T{T}.svg','w').write(svg); print(T, len(path), 'curves')
