# LUMIX S5II profiles

Stills looks and camera-settings backups for the DC-S5M2. No tether or special software: the camera loads LUTs and settings files straight off the SD card.

```sh
./lumix.py luts       # regenerate luts/*.cube from LOOKS in lumix.py
./lumix.py preview    # previews/contact-sheet.jpg on sample photos
./lumix.py push       # copy luts/*.cube to the card root
./lumix.py backup     # archive AD_LUMIX/CAMSET/*.DAT into camsets/
./lumix.py restore CAMSET01_2025-04-26_84f7cb71.DAT --as-name DAILY
```

Card must be mounted at `/Volumes/LUMIX` (USB Mode → PC(Storage), or a card reader). Names are 8 uppercase alphanumerics max (FAT32 + camera limit).

## Looks

| LUT | Vibe | Suggested opacity |
|---|---|---|
| `WARM400` | Soft, warm, Portra-ish | 60-100% |
| `GOLD200` | Punchier warm, Gold/Ektar-ish | 50-80% |
| `CHROME` | Contrasty, muted, Classic Chrome-ish | 60-100% |
| `FADED` | Lifted blacks, low contrast | 40-70% |

All built for a **Natural** base Photo Style (Contrast −1, Saturation −1, NR −3, Sharpness 0) and tagged `#LUMIXPHOTOSTYLE NAT` under the title line. Without that tag the camera assumes a V-Log base ([manual 0180](https://eww.pavc.panasonic.co.jp/dscoi/DC-S5M2/html/DC-S5M2_DVQP2839_eng/0180.html)). The preview gray-world corrects the samples first because they were shot on Incandescent WB. LUTs never touch the RAW file, only the JPEG.

## Load LUTs on camera

Update firmware first (below). The base-style tag, LUT opacity, and the 39-slot library are firmware 3.1+ features.

1. Menu → Custom (gear) → Image Quality → **LUT Library** → pick an empty slot → **Load** → Card Slot 1 → pick the `.cube`.
2. Menu → Photo → **Photo Style** → My Photo Style 1-10 → base **Natural** → LUT1 = the look, set opacity.
3. Optional: Photo Style settings → **Add Effects** → White Balance on, so each My Photo Style remembers its own WB.
4. Rename the slot (e.g. WARM400) so it shows on the Q menu.

## Dial plan

A is the live everyday state. C slots are snapshots: tweaks made while in a C slot are temporary and revert when you turn the dial.

| Dial | Name | Recipe (deltas from the A baseline) |
|---|---|---|
| A | Everyday | AWB, RAW+JPEG Fine, 3:2, My Photo Style (Natural base), Auto ISO, Min Shutter 1/125, AF-C, Full Area + Human detect, start at f/2.8 |
| C1 | ACTION | M with Auto ISO, 1/1000 s, f/2.8, Burst H. Kids, pets, sports |
| C2 | LOWLIGHT | A at f/1.8, Auto ISO cap 12800, Min Shutter 1/100, AWBw (keeps warm ambiance) |
| C3-1..4 | WARM400 / CHROME / FADED / GOLD200 | Everyday + that look's My Photo Style. C3 holds 3 by default (max 10); raise the limit to 4 for GOLD200 |

Other dial modes: iA = full auto (hand the camera to someone), P = camera picks aperture and shutter, S = you pick shutter, M = you pick both, movie icon = Creative Video, S&Q = slow/fast motion video.

Set up order (C slots copy whatever the camera is set to right now):

1. Dial A, set the baseline above, load LUTs into the LUT Library and build the My Photo Styles.
2. Setup → Setting → **Custom Mode Settings** → Limit No. of Custom Mode → 4. Set How to Reload Custom Mode → Change Recording Mode.
3. Setup → Setting → **Save to Custom Mode** → C1. Repeat for C2 and C3-1..4. A is now copied everywhere.
4. Dial each C slot, apply its deltas, Save to Custom Mode to that same slot, press DISP to rename it. A stays untouched.
5. Save/Restore Camera Setting → Save → New File `DIAL1`, then `./lumix.py backup`. Not yet verified that this file includes the C slots, so check after the first restore.

## Firmware

Do this first. SD card only, no software. Body was on 3.0; latest is [3.7](https://av.jpn.support.panasonic.com/support/global/cs/dsc/download/ff/dl/s5m2.html).

1. Copy `S5m2_V37.bin` (from the zip) to the card root. Only one firmware file on the card at a time. Panasonic suggests a freshly formatted card; that's optional and only with Austen's go-ahead.
2. Fully charged battery, no USB/HDMI cable, Wi-Fi/Bluetooth off.
3. Setup → Others → **Firmware Version** → Firmware Update → Yes. Takes 3-5 min; don't power off.
4. Lens updates work the same way with the lens mounted, as a separate pass.

## Video recipe

Per the [S5II specs](https://eww.pavc.panasonic.co.jp/dscoi/DC-S5M2/html/DC-S5M2_DVQP2839_eng/0150.html):

| Use | File format | Rec quality | Card |
|---|---|---|---|
| Everyday | MOV | 4K 29.97p 4:2:0 10-bit H.265, 150Mbps | V30 |
| Slow-mo | MOV | 4K 59.94p 4:2:0 10-bit H.265, 200Mbps | V30 |
| Heavy grading | MOV | 4K 4:2:2 10-bit H.264, 150/200Mbps | V30 |

- H.265 4:2:0 plays and edits smoothly on Apple silicon. 4:2:2 H.264 is heavier to edit and only matters for heavy grading.
- MP4 tops out at 100Mbps (10-bit H.265) or 8-bit H.264.
- Shutter speed is 2x the frame rate: 1/60 at 30p, 1/125 at 60p. Outdoors that needs a variable ND filter.
- Photo Style: Natural is simplest. Real Time LUT bakes the look in, but it's V-Log based with ISO 640 as base. V-Log gives the most latitude but needs grading. Expose +1 to +2 stops.
- Every internal mode on this body needs only U3/V30 ([manual 0007](https://eww.pavc.panasonic.co.jp/dscoi/DC-S5M2/html/DC-S5M2_DVQP2839_eng/0007.html)). The 16GB card is the problem: about 200 RAW+FINE frames (~74MB a pair). Get a 128GB V30+ SDXC.

## Save and restore whole camera setups

- Save: Menu → Setup → **Save/Restore Camera Setting** → Save → New File (e.g. `DAILY`, `FILM`). Then `./lumix.py backup`.
- Restore: `./lumix.py restore <file> --as-name NAME`, then on camera Save/Restore Camera Setting → Load → NAME. This overwrites every camera setting.
- Settings files only load on the same model (S5II).

## Notes

- Real-world test of the `.cube` parsing happens on the camera. ffmpeg parses them fine.
- `CAMSET01_2025-04-26_84f7cb71.DAT` is the setup that was on the card as of 2026-10-03.
