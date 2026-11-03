# BSERC GenAI Internship — Project 2: Thinking in HTML
## Space Weather — From the Sun to Earth

### Project overview

This is the final release folder for BSERC GenAI Internship Project 2.
It contains three main, self-contained, interactive web applications
that explain space weather — solar flares, coronal mass ejections (CMEs),
plus a Phase 3 prototype Update Centre (see 'Phase 3 prototype' below),
the solar wind, Earth's magnetosphere, and their effects on technology —
for undergraduate students, researchers, and space enthusiasts.

The project builds on source-grounded research from Project 1, drawing on
official scientific material from ISRO, NASA, and NOAA, and peer-reviewed
sources. Each application is a single `.html` file: all HTML, CSS, and
JavaScript live inside that file. There is no backend, no account login,
no external API, and no API key.

### Important disclaimer — please read this first

**The Sun–Earth simulator in `sun-earth-model.html` is an educational
visualization, not a live forecasting system.**

- It is **not live telemetry** and it does **not** show real-time solar
  activity, real CMEs in progress, or a real storm forecast.
- Distances, sizes, and times are **schematic and accelerated** so the
  Sun-to-Earth journey can be seen in a classroom session. The Sun,
  Earth, Moon, and Aditya-L1 are **not to scale**.
- CME transit times in the simulator use an **idealized constant-speed
  model** over 1 AU (149,600,000 km). Real CMEs speed up or slow down
  because of aerodynamic drag in the ambient solar wind, and a severe
  geomagnetic storm also depends on other factors, notably a prolonged
  southward interplanetary magnetic field (Bz).
- The in-app label says it plainly: "Educational Model • Not Live
  Telemetry", and a completed magnetosphere interaction is described
  in the app as a "schematic interaction, not a storm forecast."
- The other two applications likewise use **clearly labelled illustrative
  data** where a scenario is simulated. Factual claims are grounded in
  the Project 1 research sources; simulated values are not presented
  as observations.

For a real space-weather forecast, use an operational service such as
NOAA SWPC or ISRO / Aditya-L1 mission updates — not this project.

### What is in this release folder

This folder, `RohanSiddhpura_Project2`, is the correct final release.
It was identified by checking file dates and sizes against the duplicate
and backup copies in `/Volumes/PortableSSD/PROJECT1/`:

- `RohanSiddhpura_Project2 2` is an **older duplicate** (its
  `sun-earth-model.html` is from 30 Oct, 1,154,798 bytes, and its
  `prompts.txt` is shorter). Do not submit that folder.
- The many `*.zip` and `*_pre_backup` files in the parent folder are
  **backups only**. They were left untouched.
- The working folder `BSERC_Project2_Thinking_in_HTML/` contains the
  development history, `PLAN.md`, and an earlier `README.md`. That
  earlier README still describes the Sun–Earth page as a 2D model;
  the current release page is a 3D model (see below). This README,
  in the release folder, is the up-to-date description of the
  submitted files.

Files in this release folder:

```
RohanSiddhpura_Project2/
├── README.md                          # This file (added 2026-11-03)
├── space-weather-dashboard.html       # App 1: Undergraduate Learning Dashboard
├── sun-earth-model.html               # App 2: Interactive 3D Sun–Earth Simulator
├── space-weather-presentation.html    # App 3: 10-Slide Interactive Presentation
├── space-weather-update-centre.html # Phase 3 prototype: Update Centre (approval page)
├── monitor.py                       # Phase 3 prototype: source monitor (never edits apps)
├── updates.json                     # Phase 3 prototype: monitor output / approval queue
├── README_PHASE3.md                 # Phase 3 prototype: design note
└── prompts.txt                        # Chronological prompt log (see below)
```

File sizes as checked on 2026-11-03: dashboard 90,164 bytes,
presentation 88,420 bytes, Sun–Earth model 1,182,127 bytes,
`prompts.txt` 348,367 bytes (6,529 lines).

Note on the release ZIP: `RohanSiddhpura_Project2.zip` in the parent
folder should contain all five files listed above. If the ZIP you
open contains only the three HTML files plus `prompts.txt`, it
predates this README (the 2026-10-31 ZIP was verified on
2026-11-03, passed `unzip -t` with no errors, and matched the
release folder at that time). Replace it with a newly built ZIP
that includes this README before a final submission, and keep the
old ZIP as a backup until the new one has been verified.

### App 1 — `space-weather-dashboard.html`: Undergraduate Learning Dashboard

A study cockpit for mastering six space-weather topics.

- **Topic Mastery Tracker:** 6 topics, 24 checklist checkpoints,
  live percentage and progress bar, progress saved in the browser
  with `localStorage`, and a confirmation dialog before resetting.
- **Focus Countdown Timer:** 25-minute focus and 5-minute break
  presets, custom durations (1–180 minutes), Start / Pause / Resume /
  Reset, and a browser-synthesized audio chime (no audio files).
- **Active Recall Flashcards:** 12 cards across all 6 topics, 3D CSS
  flip animation, Next / Previous, shuffle, card counter, and
  keyboard flipping with Space or Enter.
- **Scored Knowledge Assessment:** 10 multiple-choice questions,
  instant correct/incorrect feedback, scientific explanations, a
  live score, and a retake option.
- **Aditya-L1 Payload Explorer:** All 7 Aditya-L1 payloads —
  VELC, SUIT, SoLEXS, HEL1OS (remote sensing) and ASPEX, PAPA, MAG
  (in-situ) — filterable by category, with roles and lead
  institutions.
- **Study Overview Statistics:** Live summary of mastery percentage,
  completed objectives, quiz readiness, and flashcard count.

### App 2 — `sun-earth-model.html`: Interactive 3D Sun–Earth Simulator

This is the 3D simulator, built with Three.js bundled inside the
single file (no external script or stylesheet is loaded). It shows
the Sun, Earth, the Moon, Aditya-L1 at Sun–Earth L1, and the
magnetosphere, bow shock, magnetopause, magnetotail, and
Van Allen belts in a schematic 3D scene.

- **CME speed slider and transit calculator:** 300–2,500 km/s
  (default 800 km/s). It calculates 1 AU transit time with
  `t = 149,600,000 / (v × 3600)` hours, and Aditya-L1 lead time with
  `Δt = 1,500,000 / (v × 60)` minutes, with a drag caveat for slow
  and extreme CMEs. Worked examples: 300 km/s → about 138.5 hours
  transit, 83.3 minutes L1 lead; 1,400 km/s → about 29.7 hours,
  17.9 minutes; 2,500 km/s → about 16.6 hours, 10.0 minutes.
- **Animated CME ejection:** An expanding plasma flux rope and shock
  front travel from the Sun, are detected upstream at Aditya-L1
  (at 0.990 of the normalized journey), then arrive at Earth (1.0)
  and compress the magnetosphere. Pause, Resume, and Reset are
  provided, and rapid clicks do not start duplicate animations.
- **Solar flare trigger:** A light-speed electromagnetic wavefront
  crosses 1 AU in about 8.3 minutes, lighting the sunlit ionosphere
  and explaining D-region ionization and HF radio absorption —
  without triggering a CME.
- **7 clickable scientific hotspots:** Sun & Active Regions, Solar
  Flare, CME, Ambient Solar Wind, Aditya-L1, Earth's Magnetosphere
  & Ionosphere, and Ground Power Grid & Lithosphere. Each opens a
  dossier with definition, sequence role, consequences, and
  limitations. Hotspots work by click and by keyboard (Enter/Space),
  and the 3D selection stays in sync with the on-page inspector.
- **Technology-impact toggles:** Satellites, GPS/GNSS, HF Radio,
  and Power Grids, with Enable All and Clear All.
- **Simulated clock and speed multipliers:** 1×, 5×, and 20× playback
  for the CME/flare sequence, shown as a simulated `00h 00m` clock.
- **Orbital motion by default:** Earth visibly revolves around the
  Sun, the Moon visibly revolves around Earth, and Aditya-L1 visibly
  moves along its 3D halo orbit — without needing to press an
  animation button first. Orbital speed and path controls are also
  provided.
- **Camera controls:** Permanently visible Zoom In / Zoom Out,
  Reset View, Focus Sun / Earth / Aditya-L1, a 360° tour, and
  Maximize / Minimize view, plus an immersive auto-hiding HUD
  that can be revealed by hover, keyboard focus, Show Info, or the
  mobile Controls button.
- **Viewport quick actions:** Eject CME and Trigger Solar Flare
  buttons floating on the 3D view itself (top-right, always
  visible, including in maximized / close-up view), so you do not
  need to scroll down to the panel below to launch an eruption.
  They trigger exactly the same handlers as the panel buttons.
- **Projected labels:** 3D object labels are placed in screen space
  and recalculated after camera moves, zoom, resize, and events,
  so they stay inside the viewport and do not pile up over Earth
  and Aditya-L1.

Remember: all of the above is a schematic, accelerated teaching
model (see the disclaimer at the top of this README), not a
forecast.

### App 3 — `space-weather-presentation.html`: 10-Slide Interactive Presentation

A standalone, keyboard- and touch-friendly deck for lectures,
seminars, or self-paced study.

- **10 slides** covering: the Sun-to-Earth overview; solar flares
  and electromagnetic radiation; CMEs and propagation; the solar
  wind and Parker spiral; Earth's magnetic shield and geomagnetic
  storms; the Sun-to-Earth propagation timeline; technological
  vulnerabilities (spacecraft/GNSS, then HF radio/power grids);
  Aditya-L1 at L1; comparative analysis (including Flare vs. CME
  and Solar Minimum vs. Solar Maximum, with the 1859 Carrington
  Event as context); and a summary with a knowledge check.
- **Navigation:** Previous / Next buttons, Arrow keys, Space,
  Home / End, a progress bar, a slide counter, and a 10-slide
  jump drawer (one-click jump, closable with Esc).
- **5-stage interactive timeline:** Solar Origin → 1 AU Propagation
  → Aditya-L1 Detection → Geospace Arrival → Ground Impacts,
  with synchronized dossiers.
- **Comparative visualizer and final knowledge check:** Toggleable
  comparisons on the final slides, plus a 5-question scored quiz
  with instant feedback and retake.
- **Presenter tools:** Collapsible presenter notes (P key or header
  button), fullscreen mode (F key or header button), and swipe
  support on touch devices.

### Phase 3 prototype — `space-weather-update-centre.html`: Space Weather Update Centre

Added 2026-11-03 at ROHAN's request. This is an update system around
the three main apps, not a replacement for them, and it does **not**
auto-publish changes.

- **Permission gate:** A separate monitor (`monitor.py`) checks the
  eight Project 1 sources and writes `updates.json`. It never edits
  the dashboard, simulator or presentation.
- **Review first:** The Update Centre page shows what changed, the
  source link, and which sections would be affected. You approve or
  reject. Approval only creates an approved change pack (exact
  source, sections and proposed text) to apply in a separate,
  diff-checked step. Rejection archives the item with a reason.
- **Two channels:** Live event data (NASA DONKI flares/CMEs/storms,
  NOAA SWPC JSON) may refresh an event list with a timestamp; it
  must never rewrite a quiz answer, explanation or simulator
  physics. Scientific knowledge changes always go through approval.
- **What can actually change:** Only SRC-01 (NOAA), SRC-02 (NASA)
  and SRC-03 (ISRO) are live portals that regularly change. The
  papers and videos (SRC-04 to SRC-08) are fixed; they are checked
  for corrections / new versions only.
- **Demo, not live data yet:** The pending item in `updates.json`
  (DEMO-1) is a workflow test only, not a real NOAA change, and
  `monitor.py` has not yet been run against live sources. Its
  first real run will set the check date. See `README_PHASE3.md`
  for the full design, the API-key warning (never commit a key),
  and the open backend decision (Mac schedule vs. GitHub Actions).

### How to launch the applications

No installation, no build step, and no server are required.
The files work offline in a modern browser (Chrome, Safari, or
Firefox).

1. Open `RohanSiddhpura_Project2` in Finder.
2. Double-click any of the three `.html` files, or drag one into
   your browser.
3. Or, from a terminal:

```
open /Volumes/PortableSSD/PROJECT1/RohanSiddhpura_Project2/space-weather-dashboard.html
open /Volumes/PortableSSD/PROJECT1/RohanSiddhpura_Project2/sun-earth-model.html
open /Volumes/PortableSSD/PROJECT1/RohanSiddhpura_Project2/space-weather-presentation.html
```

Notes:
- The dashboard saves checklist progress in the browser's
  `localStorage` on the machine where it is opened. Clearing browser
  data, or opening the file in a different browser/profile, starts
  with a fresh checklist.
- If a page looks blank or a control does not respond, try a
  different modern browser first, and check that the file was opened
  from this release folder — not from an older duplicate or backup
  copy.

### Prompt log — `prompts.txt`

`prompts.txt` is the chronological record of the prompts used during
development, from Prompt #1 (Phase 1 planning, 2026-10-29) through
Prompt #34 (final release verification, 2026-10-31). The copy in this
release folder is identical to the copy in the working folder
(`BSERC_Project2_Thinking_in_HTML/prompts/prompts.txt`), as checked
on 2026-11-03.

Audit note (2026-11-03, added with this README — no prompt text was
invented or altered to produce it):

- Entries are in chronological order by prompt number and, where a
  timestamp is given, by date/time.
- **Prompt #21 and Prompt #23 do not appear as entries in the log.**
  The numbering jumps from #20 to #22, and from #22 to #24. No text
  for #21 or #23 was found in the release log, so none has been
  fabricated here. If those prompts exist elsewhere, they should be
  appended from their original wording before a final submission.
- **Prompt #34 is present as prompt text only**; unlike most earlier
  prompts, it has no outcome/completion record appended after it in
  the file. That does not mean the work was not done — the release
  files and ZIP were verified separately in this task — but the log
  itself does not record a Prompt #34 outcome.
- Later prompts use inconsistent header formats (for example,
  `[PROMPT #15] — <date>` versus `PROMPT #19:` with no timestamp
  line). The content and order were preserved; only this audit note
  calls out the inconsistency.

The prompt log itself was left byte-for-byte unchanged in this task,
so that its history is not rewritten. This README documents the gaps
instead of silently filling them.

### Acceptance criteria met by every page

1. One standalone `.html` file per page; markup, CSS, and JavaScript
   are all inside that file.
2. No external CSS/JavaScript libraries, fonts, or APIs are loaded
   by the pages (no Bootstrap, Tailwind CDN, jQuery, React, or
   Google Fonts). All layout, styling, animation, and icons use
   standard HTML5, CSS3, SVG, and vanilla JavaScript, with Three.js
   bundled into the Sun–Earth file itself.
3. At least five genuinely working interactive elements per page.
4. Responsive layout for mobile (375–768 px) and laptop/desktop
   (1024–1920 px), with no horizontal scrolling in the verified
   viewports.
5. Accessibility: semantic landmarks, visible focus outlines,
   `aria-label` / `aria-live` regions where dynamic content changes,
   and touch targets of at least 44 × 44 px.
6. No backend, database, or login; only client-side `localStorage`
   where progress needs to persist.
7. Scientific claims grounded in Project 1 sources; simulated or
   parameterized values labelled as illustrative/schematic.

### Known limitations

- The CME model is constant-speed and schematic; it does not model
  drag, CME–solar-wind interaction, or the full magnetohydrodynamics
  of a real event.
- The 3D scene is not to scale and playback is accelerated; orbital
  periods shown are illustrative, not real-time.
- The prompt log has the two gaps noted above (#21, #23 missing;
  #34 without an outcome record).
- If the release ZIP in the parent folder predates this README, it
  will not contain it yet (see "What is in this release folder").
- The working folder's earlier README still calls the Sun–Earth page
  a 2D model; this release README supersedes it for the submitted
  files.
