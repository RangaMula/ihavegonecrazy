// node tools/render_pdf.cjs in.html out.(pdf|png) "footer text" [mode]
//   mode omitted : A5 reading PDF with a footer (draft notice + page number)
//   print        : page size and page numbers come from the CSS (@page margin boxes)
//   cover        : exact CSS page size, no footer
//   shot:WxH     : PNG screenshot of a W x H CSS-pixel viewport, scaled to 1600 px wide
const { chromium } = require('playwright');
(async () => {
  const [inp, out, footer, mode] = process.argv.slice(2);
  const browser = await chromium.launch();
  let page;
  if (mode && mode.startsWith('shot:')) {
    const [w, h] = mode.slice(5).split('x').map(Number);
    page = await browser.newPage({ viewport: { width: Math.round(w), height: Math.round(h) }, deviceScaleFactor: 1600 / w });
  } else {
    page = await browser.newPage();
  }
  await page.goto('file://' + inp, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  if (mode && mode.startsWith('shot:')) {
    await page.screenshot({ path: out, fullPage: false });
  } else if (mode === 'print' || mode === 'cover') {
    await page.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  } else {
    const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
    await page.pdf({
      path: out, format: 'A5', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font-size:7px;color:#999;padding:0 14mm;display:flex;justify-content:space-between;font-family:sans-serif">
        <span>${esc(footer || '')}</span><span class="pageNumber"></span></div>`,
    });
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
