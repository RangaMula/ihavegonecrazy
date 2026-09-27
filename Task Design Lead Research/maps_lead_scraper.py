#!/usr/bin/env python3
"""Google Maps lead scraper for building design, construction and real estate.

Uses the official Google Places API (New) Text Search endpoint, i.e. the same
data you see on Google Maps, fetched in a ToS-compliant way. Every query in
config/search_queries.json is run for every location, paginated up to the API
limit (60 results per query), de-duplicated by Google place ID, and written to
CSV + JSON in output/.

Usage:
    set GOOGLE_MAPS_API_KEY=...            (Windows)   /  export GOOGLE_MAPS_API_KEY=... (mac/linux)
    python maps_lead_scraper.py --location "Dhaka, Bangladesh"
    python maps_lead_scraper.py --location "Dhaka" --location "Chattogram"
    python maps_lead_scraper.py --locations-file locations.txt --categories "Real Estate Agents & Brokers"
    python maps_lead_scraper.py --location "Austin, TX" --dry-run   (prints queries, no API calls)
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
DEFAULT_CONFIG = HERE / "config" / "search_queries.json"
DEFAULT_OUTPUT = HERE / "output"

ENDPOINT = "https://places.googleapis.com/v1/places:searchText"
FIELD_MASK = ",".join(
    [
        "places.id",
        "places.displayName",
        "places.primaryTypeDisplayName",
        "places.primaryType",
        "places.types",
        "places.formattedAddress",
        "places.nationalPhoneNumber",
        "places.internationalPhoneNumber",
        "places.websiteUri",
        "places.googleMapsUri",
        "places.rating",
        "places.userRatingCount",
        "places.businessStatus",
        "places.location",
        "nextPageToken",
    ]
)
CSV_COLUMNS = [
    "name",
    "categories",
    "matched_queries",
    "primary_type",
    "phone",
    "international_phone",
    "website",
    "address",
    "search_location",
    "rating",
    "review_count",
    "business_status",
    "latitude",
    "longitude",
    "google_maps_url",
    "place_id",
]


def load_env_file() -> None:
    """Load KEY=VALUE pairs from a local .env next to this script, if present."""
    env_path = HERE / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def search_text(session: requests.Session, api_key: str, text_query: str, max_pages: int,
                language: str | None, region: str | None) -> list[dict]:
    """Run one Text Search query, following nextPageToken up to max_pages (20 results/page)."""
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": FIELD_MASK,
    }
    body: dict = {"textQuery": text_query, "pageSize": 20}
    if language:
        body["languageCode"] = language
    if region:
        body["regionCode"] = region

    places: list[dict] = []
    for _ in range(max_pages):
        for attempt in range(4):
            resp = session.post(ENDPOINT, headers=headers, json=body, timeout=30)
            if resp.status_code in (429, 500, 503) and attempt < 3:
                time.sleep(2 ** (attempt + 1))
                continue
            break
        if resp.status_code != 200:
            raise RuntimeError(f"Places API error {resp.status_code}: {resp.text[:500]}")
        data = resp.json()
        places.extend(data.get("places", []))
        token = data.get("nextPageToken")
        if not token:
            break
        body["pageToken"] = token
        time.sleep(1)  # page tokens need a moment to become valid
    return places


def to_lead(place: dict, category: str, query: str, location: str) -> dict:
    loc = place.get("location") or {}
    return {
        "name": (place.get("displayName") or {}).get("text", ""),
        "categories": {category},
        "matched_queries": {query},
        "primary_type": (place.get("primaryTypeDisplayName") or {}).get("text")
        or place.get("primaryType", ""),
        "phone": place.get("nationalPhoneNumber", ""),
        "international_phone": place.get("internationalPhoneNumber", ""),
        "website": place.get("websiteUri", ""),
        "address": place.get("formattedAddress", ""),
        "search_location": location,
        "rating": place.get("rating", ""),
        "review_count": place.get("userRatingCount", ""),
        "business_status": place.get("businessStatus", ""),
        "latitude": loc.get("latitude", ""),
        "longitude": loc.get("longitude", ""),
        "google_maps_url": place.get("googleMapsUri", ""),
        "place_id": place.get("id", ""),
    }


def serialise(lead: dict) -> dict:
    out = dict(lead)
    out["categories"] = "; ".join(sorted(lead["categories"]))
    out["matched_queries"] = "; ".join(sorted(lead["matched_queries"]))
    return out


def write_outputs(leads: dict[str, dict], output_dir: Path, stamp: str) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = sorted((serialise(l) for l in leads.values()), key=lambda r: (r["categories"], r["name"]))
    csv_path = output_dir / f"design_construction_realestate_leads_{stamp}.csv"
    json_path = output_dir / f"design_construction_realestate_leads_{stamp}.json"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig opens cleanly in Excel
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    return csv_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--location", action="append", default=[], help="City/area to search (repeatable)")
    parser.add_argument("--locations-file", type=Path, help="Text file with one location per line")
    parser.add_argument("--categories", action="append", default=[], help="Only run these category names (repeatable)")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-pages", type=int, default=3, choices=[1, 2, 3], help="Pages per query (20 results each)")
    parser.add_argument("--language", help="Result language, e.g. en")
    parser.add_argument("--region", help="Two-letter region bias, e.g. BD, US, GB")
    parser.add_argument("--include-closed", action="store_true", help="Keep permanently/temporarily closed businesses")
    parser.add_argument("--dry-run", action="store_true", help="Print the queries without calling the API")
    args = parser.parse_args()

    load_env_file()
    locations = list(args.location)
    if args.locations_file:
        locations += [l.strip() for l in args.locations_file.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not locations:
        parser.error("give at least one --location or a --locations-file")

    config = json.loads(args.config.read_text(encoding="utf-8"))["categories"]
    if args.categories:
        unknown = set(args.categories) - set(config)
        if unknown:
            parser.error(f"unknown categories: {sorted(unknown)}; available: {sorted(config)}")
        config = {k: v for k, v in config.items() if k in args.categories}

    jobs = [(cat, q, loc) for loc in locations for cat, queries in config.items() for q in queries]
    print(f"{len(jobs)} searches across {len(locations)} location(s) and {len(config)} categories")
    if args.dry_run:
        for cat, q, loc in jobs:
            print(f"  [{cat}] {q} in {loc}")
        return 0

    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        print("ERROR: set GOOGLE_MAPS_API_KEY (env var or .env file next to this script)", file=sys.stderr)
        return 2

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    leads: dict[str, dict] = {}
    session = requests.Session()
    for i, (cat, q, loc) in enumerate(jobs, 1):
        text_query = f"{q} in {loc}"
        try:
            places = search_text(session, api_key, text_query, args.max_pages, args.language, args.region)
        except RuntimeError as exc:
            print(f"[{i}/{len(jobs)}] {text_query}: {exc}", file=sys.stderr)
            if "403" in str(exc) or "400" in str(exc):
                return 1  # bad key / API not enabled: every other call will fail the same way
            continue
        new = 0
        for place in places:
            if not args.include_closed and place.get("businessStatus", "OPERATIONAL") != "OPERATIONAL":
                continue
            pid = place.get("id")
            if not pid:
                continue
            if pid in leads:
                leads[pid]["categories"].add(cat)
                leads[pid]["matched_queries"].add(q)
            else:
                leads[pid] = to_lead(place, cat, q, loc)
                new += 1
        print(f"[{i}/{len(jobs)}] {text_query}: {len(places)} results, {new} new (total {len(leads)})")
        if i % 10 == 0:  # checkpoint so a crash never loses work
            write_outputs(leads, args.output_dir, stamp)

    csv_path, json_path = write_outputs(leads, args.output_dir, stamp)
    print(f"\nDone: {len(leads)} unique leads\n  {csv_path}\n  {json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
