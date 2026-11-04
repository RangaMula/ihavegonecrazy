// Projects Natural Earth outlines (public domain, via world-atlas) for one book's map.
// usage: node engine/make_map.mjs build/<code>/map_config.json build/<code>/map_paths.json
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { feature, mesh } from 'topojson-client';
import * as d3 from 'd3-geo';
const here = path.dirname(fileURLToPath(import.meta.url));
const nm = p => path.join(here, 'node_modules', p);
const cfg = JSON.parse(fs.readFileSync(process.argv[2]));
const W = 1000, H = 1000;
const t50 = JSON.parse(fs.readFileSync(nm('world-atlas/countries-50m.json')));
const t110 = JSON.parse(fs.readFileSync(nm('world-atlas/countries-110m.json')));
const land50 = JSON.parse(fs.readFileSync(nm('world-atlas/land-50m.json')));
const proj = d3.geoMercator().fitSize([W, H], { type: 'MultiPoint', coordinates: cfg.frame })
  .clipExtent([[-20, -20], [W + 20, H + 20]]);
const gp = d3.geoPath(proj).digits(1);
const out = { points: {}, countries: {} };
if (cfg.land) out.land = gp(feature(land50, land50.objects.land));
const fc = feature(t50, t50.objects.countries);
for (const f of fc.features) if ((cfg.countries || []).includes(f.properties.name)) out.countries[f.properties.name] = gp(f);
for (const [k, ll] of Object.entries(cfg.points)) out.points[k] = proj(ll);
const wproj = d3.geoEquirectangular().fitSize([400, 210], { type: 'Sphere' });
out.world = d3.geoPath(wproj).digits(1)(feature(t110, t110.objects.countries));
out.world_marker = wproj(cfg.world_marker);
fs.writeFileSync(process.argv[3], JSON.stringify(out));
console.log('map:', Object.keys(out.countries).join(', ') || 'land only', '·', Object.keys(out.points).length, 'points');
