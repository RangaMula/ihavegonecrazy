// Renders HTML to PDF with the pre-installed Chromium (exact page size from CSS, fonts embedded).
// usage: node engine/render.mjs <in.html> <out.pdf> [<in.html> <out.pdf> ...]
import path from 'path';
import { createRequire } from 'module';
import { execSync } from 'child_process';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const browser = await pw.chromium.launch();
const args = process.argv.slice(2);
for (let i = 0; i < args.length; i += 2) {
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(args[i]), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.resolve(args[i + 1]), preferCSSPageSize: true, printBackground: true });
  console.log('wrote', args[i + 1]);
  await page.close();
}
await browser.close();
