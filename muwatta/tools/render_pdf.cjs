// node tools/render_pdf.cjs in.html out.pdf "footer text"  — uses the preinstalled Playwright Chromium
const { chromium } = require('playwright');
(async () => {
  const [inp, out, footer] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inp, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  await page.pdf({
    path: out, format: 'A5', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-size:7px;color:#999;padding:0 14mm;display:flex;justify-content:space-between;font-family:sans-serif">
      <span>${esc(footer || '')}</span><span class="pageNumber"></span></div>`,
  });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
