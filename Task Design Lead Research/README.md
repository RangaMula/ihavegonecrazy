# Task: Design Lead Research

Collects leads from Google Maps: people and organizations in **building design, construction and real estate**. That covers architects, interior designers, engineers, contractors, home builders, real estate agents, brokers, developers, housing projects and property managers.

It uses the official **Google Places API (New)**, which returns the same listings as Google Maps. Scraping the Maps website directly breaks Google's Terms of Service and gets blocked quickly.

## What you get

`output/design_construction_realestate_leads_<timestamp>.csv` (opens in Excel) plus a `.json` copy, with one row per business:

name · categories · matched queries · type · phone · website · address · rating · review count · lat/long · Google Maps link · place ID

Businesses that show up under several searches are merged into one row. Closed businesses are skipped unless you pass `--include-closed`.

## Setup (one time)

1. Go to https://console.cloud.google.com → create a project → **enable "Places API (New)"**.
2. Attach a billing account. Google requires one even when your usage stays inside the free allowance.
3. **APIs & Services → Credentials → Create API key**, then restrict the key to Places API (New).
4. Recommended: **Quotas** → cap `Text Search` requests per day, so you can never be charged more than you planned.
5. `pip install -r requirements.txt`
6. Create a `.env` file in this folder containing `GOOGLE_MAPS_API_KEY=your_key`. The file is gitignored.

## Run

```bash
python maps_lead_scraper.py --location "Dhaka, Bangladesh" --dry-run      # preview the searches, no cost
python maps_lead_scraper.py --location "Dhaka, Bangladesh"
python maps_lead_scraper.py --location "Dhaka" --location "Chattogram" --region BD
python maps_lead_scraper.py --locations-file locations.txt --categories "Real Estate Agents & Brokers"
```

To change what gets searched, edit the categories and queries in `config/search_queries.json`.

## Cost

- The request type used here (Text Search with phone, website and rating) is billed at Google's *Enterprise* tier. When this was written, Google gave **about 1,000 free requests per month**, then charged **about $35 per 1,000**. Check the current numbers at https://developers.google.com/maps/billing-and-pricing/pricing.
- One full run for **one location** makes at most 35 queries × 3 pages = **105 requests**. That means roughly **9 or more full locations per month are free**. After that, each extra location costs about **$3.70**.
- To spend less, use `--max-pages 1` (35 requests per location) or `--categories` to run only some categories.
- A daily quota cap (setup step 4) guarantees you are never billed more than you allow.
