// node measure.js measure.html cache.json  — measures every .m block (inches, margins included) and merges into the cache
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const [src, cacheFile] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 700, height: 1000 } });
  await p.goto('file://' + require('path').resolve(src)); await p.evaluate(() => document.fonts.ready);
  const res = await p.evaluate(() => Object.fromEntries([...document.querySelectorAll('.m')].map(e => [e.dataset.k, e.getBoundingClientRect().height / 96])));
  const cache = fs.existsSync(cacheFile) ? JSON.parse(fs.readFileSync(cacheFile)) : {};
  Object.assign(cache, res); fs.writeFileSync(cacheFile, JSON.stringify(cache));
  console.log('measured', Object.keys(res).length); await b.close();
})();
