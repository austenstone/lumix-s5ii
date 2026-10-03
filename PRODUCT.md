# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Austen, the owner of a Panasonic LUMIX S5II (DC-S5M2) with a LUMIX S 50mm f/1.8. He's a capable technical person but new to the camera. He mostly shoots friends, trips, events and everyday life, and some video. He reads the guide at a desk to learn, then on his phone next to the camera to look up a setting. (Phone use is inferred from the brief; Austen hasn't confirmed it.)

## Product Purpose

A single, friendly guide that teaches Austen to use his own S5II well. For each recommendation it explains *why* in plain language and *how*, with the exact menu path or button. Success means his photos stop coming out blue or soft, he shoots RAW+JPEG with AWB, he uses C1/C2/C3 on purpose, and his video settings are deliberate.

## Positioning

Built from his actual camera's data rather than a generic camera tutorial: the EXIF diagnosis (Incandescent WB, JPEG Standard, 16:9, firmware 3.0), his lens, his dial plan, his custom LUTs (WARM400, GOLD200, CHROME, FADED), and his card-to-Mac-to-Google Photos workflow.

## Operating Context

- Hardware: S5II, LUMIX S 50mm f/1.8, a 16GB SDHC card today (upgrade recommended).
- Storage workflow: card → `~/Pictures/YYYY/YYYY-MM-DD` on his Mac → upload to Google Photos.
- Tooling: `lumix.py` in this repo (LUT generation, push to card, settings backup and restore).
- Hosted on GitHub Pages from this repo.

## Capabilities and Constraints

- KISS. Simple language, why plus how, no jargon without a one-line explanation.
- Menu paths and specs must be verified against the official S5II manual or Panasonic pages. Mark anything unverified.
- Static site. No build step required; must work offline-ish and load fast on a phone.
- Downloads: the four .cube LUTs and lumix.py live in this repo.
- Austen's settings backup files (`camsets/`) contain the camera serial and must not be published.

## Evidence on Hand

- Austen's own S5II photos in `~/Pictures` may be used as examples (he approved public use). Other people's faces are fine; Austen excluded P1002850 specifically. Strip GPS, serial and other EXIF before publishing.
- The EXIF diagnosis from 2026-10-03 (Incandescent WB on all 286 frames since 2026-06-23, JPEG Standard, 16:9, min shutter about 1/60, firmware 3.0, wrong time zone).
- Research notes with sources (official manual, Panasonic support, reviewers).
- No testimonials, ratings or third-party claims exist; don't invent any.

## Product Principles

1. Explain why before how. Every setting earns its place with one plain reason.
2. His camera, not a camera. Use his lens, his dial plan, his mistakes and his LUTs.
3. The shortest path to better photos goes first: fix white balance, RAW+JPEG, aperture.
4. Glanceable in the field. Every recipe should be readable on a phone in seconds.
5. Verified or flagged. Never state a menu path or spec that hasn't been checked.

## Accessibility & Inclusion

Readable on a phone in daylight: strong contrast and large tap targets. Color is never the only signal; captions say what changed in each before/after.
