const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const lang = process.argv[2];
const base = __dirname;
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + base + `/book_${lang}.html`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const footer = lang === 'en'
    ? '<div style="font-size:8px;width:100%;text-align:center;color:#666;font-family:sans-serif;">Build It in Bangla &nbsp;·&nbsp; Page <span class="pageNumber"></span> / <span class="totalPages"></span></div>'
    : '<div style="font-size:8px;width:100%;text-align:center;color:#666;font-family:sans-serif;">Page <span class="pageNumber"></span> / <span class="totalPages"></span></div>';
  await page.pdf({ path: base + `/book_${lang}.pdf`, format: 'A4', printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: footer,
    margin: { top: '18mm', bottom: '20mm', left: '16mm', right: '16mm' } });
  await browser.close();
  console.log('pdf ok', lang);
})().catch(e => { console.error(e); process.exit(1); });
