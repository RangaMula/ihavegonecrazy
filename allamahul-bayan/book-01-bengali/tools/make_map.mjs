// Builds assets/map_bengal.svg-ready path data (JSON) from Natural Earth 50m (world-atlas, public domain).
import fs from 'fs';
import path from 'path';

const topo = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
import {feature} from 'topojson-client';
import * as d3 from 'd3-geo';
const fc = feature(topo, topo.objects.countries);
const topo110 = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-110m.json'));
const fc110 = feature(topo110, topo110.objects.countries);
const W=1000,H=1000;
// frame: Bengal region
const frame = {type:'MultiPoint',coordinates:[[86.1,20.7],[93.3,26.9]]};
const proj = d3.geoMercator().fitSize([W,H], frame).clipExtent([[-20,-20],[W+20,H+20]]);
const gp = d3.geoPath(proj).digits(1);
const out = {};
for (const f of fc.features){
  const n=f.properties.name;
  if(['Bangladesh','India','Myanmar','Nepal','Bhutan','China'].includes(n)) out[n]=gp(f);
}
const pt = (lon,lat)=>proj([lon,lat]);
out.points = {dhaka:pt(90.41,23.81), kolkata:pt(88.36,22.57), agartala:pt(91.28,23.83), silchar:pt(92.79,24.83),
  wb_label:pt(87.55,23.35), bay:pt(89.6,21.15), tripura:pt(91.75,23.25), barak:pt(92.75,25.35),
  bd_label:pt(90.0,24.55), india_label:pt(87.4,25.5), myanmar_label:pt(92.75,21.9), nepal_label:pt(87.1,26.75), bhutan_label:pt(90.6,26.95)};
// world locator
const wproj = d3.geoEquirectangular().fitSize([400,210],{type:'Sphere'});
const wp = d3.geoPath(wproj).digits(1);
out.world = fc110.features.map(f=>wp(f)).join('');
out.world_bd = wproj([90.3,23.7]);
fs.writeFileSync('build/map_paths.json', JSON.stringify(out));
console.log(Object.keys(out), out.points);
