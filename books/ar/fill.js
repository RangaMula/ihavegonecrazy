// node fill.js book.html -> page fill statistics (content height / usable height)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 700, height: 1000 } });
  await p.goto('file://' + require('path').resolve(process.argv[2])); await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => [...document.querySelectorAll('.page')].map(el => {
    const R = el.getBoundingClientRect(); const top = R.top + 0.78 * 96, usable = 10 * 96 - 1.6 * 96; let maxB = top;
    for (const c of el.children) { if (c.classList.contains('folio') || c.classList.contains('runhead')) continue; const cr = c.getBoundingClientRect(); if (cr.height) maxB = Math.max(maxB, cr.bottom); }
    return { fill: (maxB - top) / usable, head: (el.querySelector('.runhead span') || {}).textContent || '' };
  }));
  const n = r.length, under50 = r.filter(x => x.fill < 0.5).length, under75 = r.filter(x => x.fill < 0.75).length;
  const avg = r.reduce((a, x) => a + Math.min(x.fill, 1), 0) / n;
  console.log(`pages ${n} · average fill ${(avg * 100).toFixed(0)}% · pages <50% full: ${under50} · <75% full: ${under75}`);
  if (process.argv[3]) { const by = {}; r.forEach(x => { const k = x.head || '(none)'; by[k] = by[k] || []; by[k].push(x.fill); });
    Object.entries(by).filter(([k, v]) => v.length > 2).forEach(([k, v]) => console.log(k, v.length, (v.reduce((a, b) => a + Math.min(b, 1), 0) / v.length * 100).toFixed(0) + '%')); }
  await b.close();
})();
