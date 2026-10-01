#!/bin/bash
# Build book.html with measured layout, then render the PDF. Usage: SKIP=part4 ./make.sh out.pdf [pngdir] [range]
cd "$(dirname "$0")"
export NODE_PATH=$(npm root -g)
for i in 1 2 3 4; do
  out=$(python3 build.py) || exit 1
  echo "$out" | grep -v NEEDS_MEASURE
  echo "$out" | grep -q NEEDS_MEASURE || break
  node measure.js measure.html data/.measure_cache.json
done
rm -f measure.html
node render.js book.html "${1:-book.pdf}" $2 $3
