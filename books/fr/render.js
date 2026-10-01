// node render.js book.html out.pdf [pngdir] [pages e.g. 1-5]
const { chromium } = require('playwright');
(async () => {
  const [src, pdf, pngdir, range] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 700, height: 1000 }, deviceScaleFactor: 1.3 });
  await p.goto('file://' + require('path').resolve(src), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  const rep = await p.evaluate(() => [...document.querySelectorAll('.page')].map((el, i) => {
    const r = el.getBoundingClientRect(); const limit = r.bottom - 0.52 * 96; let maxB = 0;
    const walk = n => { for (const c of n.children) { if (c.classList.contains('folio') || c.classList.contains('runhead')) continue;
      const cr = c.getBoundingClientRect(); if (cr.height > 0) maxB = Math.max(maxB, cr.bottom); } };
    walk(el);
    const label = (el.querySelector('.folio') || {}).textContent || '';
    return maxB > limit + 1 ? `OVERFLOW page #${i + 1} (${label}) by ${Math.round(maxB - limit)}px` : null;
  }).filter(Boolean));
  console.log(rep.length ? rep.join('\n') : 'no overflow');
  if (pngdir) {
    const pages = await p.$$('.page'); let [a, z] = (range || '1-' + pages.length).split('-').map(Number);
    for (let i = a; i <= Math.min(z, pages.length); i++) await pages[i - 1].screenshot({ path: `${pngdir}/p${String(i).padStart(3, '0')}.png` });
  }
  await p.pdf({ path: pdf, width: '7in', height: '10in', printBackground: true });
  await b.close();
})();
