import path from 'path';
// Renders build/*.html to output/*.pdf with the pre-installed Chromium (exact page size, fonts embedded).
import { createRequire } from 'module';
import { execSync } from 'child_process';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }               // local install, if any
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const { chromium } = pw;
const jobs = process.argv.slice(2).length ? process.argv.slice(2) : ['interior'];
const browser = await chromium.launch();
for (const name of jobs) {
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve('build', name + '.html'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.resolve('output', name + '.pdf'), preferCSSPageSize: true, printBackground: true });
  console.log('wrote output/' + name + '.pdf');
  await page.close();
}
await browser.close();
