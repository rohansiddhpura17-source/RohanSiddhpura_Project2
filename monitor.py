#!/usr/bin/env python3
"""
Space Weather Update Monitor - Phase 3 prototype.

What this script DOES:
  - Checks the 3 live portals (SRC-01/02/03) and, optionally, the
    NASA DONKI and NOAA SWPC JSON endpoints listed in updates.json.
  - Records HTTP status, Content-Length, Last-Modified / ETag where
    the server sends them, and a SHA-256 hash for small text pages.
  - Writes updates.json. It NEVER edits dashboard / simulator /
    presentation HTML files.

What it does NOT do:
  - It does not rewrite scientific explanations, quizzes or simulator
    behaviour, and it does not publish anything.
  - A human must open space-weather-update-centre.html, review a
    pending item, and approve it before any change is applied.

Run:
  python3 monitor.py --out updates.json
  NASA_API_KEY=your_free_key python3 monitor.py --out updates.json --live

Notes:
  - DONKI needs a free api.nasa.gov key. Never commit a key.
    Without a key, DONKI checks are skipped and reported as skipped.
  - NOAA SWPC JSON needs no key, but its formats have changed before
    (see the March 2026 SWPC service notice). Pin snapshots and
    handle a schema change as a "needs review" item, not as data.
  - A standalone HTML file opened from file:// cannot reliably fetch
    these endpoints (browser CORS / file restrictions). That is why
    the monitor runs separately - locally, or as a scheduled
    GitHub Actions job - and the Update Centre page reads its output.
  - This prototype has NOT been run against live sources in the
    delivery that created it. Its first real run will set last_checked.
"""

import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

SOURCES = [
    ("SRC-01", "https://www.spaceweather.gov/impacts", "live_portal"),
    ("SRC-02", "https://science.nasa.gov/heliophysics/focus-areas/space-weather/", "live_portal"),
    ("SRC-03", "https://www.isro.gov.in/ISRO_EN/Aditya_L1.html", "live_portal"),
    ("SRC-04", "https://link.springer.com/article/10.1007/s41116-021-00030-3", "fixed_paper"),
    ("SRC-05", "https://arxiv.org/abs/2212.13046", "fixed_paper"),
    ("SRC-06", "https://raeng.org.uk/media/lz2fs5ql/space_weather_full_report_final.pdf", "fixed_report"),
    ("SRC-07", "https://www.youtube.com/watch?v=Cnp3AB97Z5Y", "fixed_video"),
    ("SRC-08", "https://www.youtube.com/watch?v=_IcgGYZTXQw", "fixed_video"),
]

LIVE_JSON = [
    ("NASA DONKI FLR", "https://api.nasa.gov/DONKI/FLR", True),
    ("NASA DONKI CME", "https://api.nasa.gov/DONKI/CME", True),
    ("NASA DONKI GST", "https://api.nasa.gov/DONKI/GST", True),
    ("NOAA SWPC Kp", "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json", False),
    ("NOAA SWPC Scales", "https://services.swpc.noaa.gov/products/noaa-scales.json", False),
    ("NOAA SWPC Alerts", "https://services.swpc.noaa.gov/products/alerts.json", False),
]


def check(url, timeout=30, hash_body=False):
    req = urllib.request.Request(url, headers={"User-Agent": "BSERC-Update-Monitor-Prototype/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read() if hash_body else b""
            return {
                "url": url,
                "status": resp.status,
                "content_length": resp.headers.get("Content-Length"),
                "last_modified": resp.headers.get("Last-Modified"),
                "etag": resp.headers.get("ETag"),
                "sha256": hashlib.sha256(body).hexdigest() if body else None,
                "error": None,
            }
    except Exception as exc:
        return {"url": url, "status": None, "error": str(exc)}


def main():
    out = "updates.json"
    live = False
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--out" and i + 1 < len(args):
            out = args[i + 1]
        if a == "--live":
            live = True
    now = datetime.now(timezone.utc).isoformat()
    results = []
    for source_id, url, kind in SOURCES:
        result = check(url, hash_body=(kind == "live_portal"))
        result["id"] = source_id
        result["kind"] = kind
        results.append(result)
    live_results = []
    if live:
        api_key = os.environ.get("NASA_API_KEY", "")
        for name, url, needs_key in LIVE_JSON:
            if needs_key and not api_key:
                live_results.append({"name": name, "url": url, "status": "skipped_no_api_key"})
                continue
            use_url = url + ("?api_key=" + api_key if needs_key else "")
            live_results.append({"name": name, **check(use_url, hash_body=False)})
    data = {
        "schema_version": 1,
        "last_checked": now,
        "note": "Monitor output only. Nothing in the project was edited by this run. Review pending items in space-weather-update-centre.html and approve them first.",
        "source_checks": results,
        "live_data_checks": live_results,
        "pending_updates": [],
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {out} at {now} ({len(results)} sources, {len(live_results)} live checks)")


if __name__ == "__main__":
    main()
