# Space Weather Update Engine — Phase 3 Prototype

**Status:** Prototype, added to the release folder on 2026-11-03 at ROHAN's request. The three main apps remain the submission core; this is the update system around them.
**Core rule, in ROHAN's words:** Tell me first, get my permission, then apply — never silently update the project.

## The design in one paragraph

A monitor runs separately (it cannot run inside a standalone HTML file sitting unopened on an SSD, and a `file://` page cannot reliably fetch live APIs). It writes `updates.json`. The Update Centre page (`space-weather-update-centre.html`) shows what changed, the evidence link, and the affected sections. ROHAN approves or rejects. Approval creates a change pack — exact source, sections and proposed text — which is applied in a separate, diff-checked step. Rejection archives the item with a reason.

## Two channels — keep them separate

1. **Live event data (can auto-refresh, with a timestamp)**
   - NASA DONKI: `api.nasa.gov/DONKI/FLR`, `/CME`, `/GST` — free api.nasa.gov key required; DEMO_KEY is rate-limited.
   - NOAA SWPC JSON, no key: `services.swpc.noaa.gov/products/noaa-planetary-k-index.json`, `noaa-scales.json`, `alerts.json`.
   - Safe rule: refresh only event lists, values, timestamps and source links. Never let a feed rewrite a quiz answer, an explanation or simulator physics.
   - Caution: SWPC JSON formats have changed before (e.g. March 2026 service notice). Pin snapshots; treat a schema change as "needs review".
   - Caution: DONKI has migrated endpoints before. Verify the current endpoint before production use; do not hard-code a legacy URL.

2. **Scientific knowledge (verify before publishing, always)**
   - The eight Project 1 sources (see SOURCE_MANIFEST.md in the research folder).
   - Only SRC-01 (NOAA), SRC-02 (NASA) and SRC-03 (ISRO) are live portals that regularly change. SRC-04/05/06 are fixed papers/reports; SRC-07/08 are fixed videos. For those, monitor for corrections / new versions only, quarterly or monthly — not daily "new science".
   - Every knowledge change goes through the approval queue, with evidence.

## Files

- `space-weather-update-centre.html` — the approval page. No external scripts or links are loaded by it (all links are ordinary `<a href>` source links). Decisions are stored in browser localStorage only, like the dashboard.
- `updates.json` — monitor output schema. The pending item in this delivery is DEMO-1, clearly labelled demo-only. It is NOT a real NOAA change.
- `monitor.py` — standard-library-only monitor. Run: `python3 monitor.py --out updates.json` and `NASA_API_KEY=your_free_key python3 monitor.py --out updates.json --live`. It never edits project HTML files. It has not been run against live sources in this delivery; its first real run will set `last_checked`.

## What is NOT built yet (needs your decisions)

- A real backend / scheduled job. Options: (a) run `monitor.py` on your Mac on a schedule, (b) a weekly GitHub Actions job that commits only `updates.json` when it changes. (b) needs a repository and a decision about where the apps live — GitHub vs. your SSD — and must never auto-commit edits to the apps.
- API keys: never commit a NASA key. Use an environment variable, or a repository secret for GitHub Actions.
