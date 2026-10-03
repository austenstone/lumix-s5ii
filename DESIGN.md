---
name: Lumix S5II Field Guide
description: Austen's own frames, marked up in red grease pencil, explaining every S5II setting worth changing.
colors:
  pencil: "#c4261f"
  edge: "#e6a740"
  film: "#11100f"
  film-2: "#2a2826"
  paper: "#f2f2ee"
  paper-2: "#e6e6e0"
  ink: "#131312"
  ink-2: "#4b4945"
  rule: "#cfcec7"
  pencil-on-film: "#ff5a4c"
  edge-hi: "#fff3dc"
  film-caption: "#d9d3c7"
  bezel: "#6b6863"
  print-white: "#ffffff"
  black: "#000000"
typography:
  display:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2.9rem, 1.6rem + 6.2vw, 6rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.035em"
    fontVariation: "\"wdth\" 125"
  headline:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2rem, 1.3rem + 3vw, 3.6rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.02em"
    fontVariation: "\"wdth\" 118"
  title:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.1rem + 0.6vw, 1.55rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.01em"
    fontVariation: "\"wdth\" 108"
  body:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 0.98rem + 0.3vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.6
    fontVariation: "\"wdth\" 100"
  label:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.74rem"
    fontWeight: 650
    letterSpacing: "0.1em"
    fontFeature: "\"tnum\""
    fontVariation: "\"wdth\" 62"
  marker:
    fontFamily: "Permanent Marker, Marker Felt, cursive"
    fontSize: "clamp(1.35rem, 1.1rem + 0.8vw, 1.8rem)"
    fontWeight: 400
    lineHeight: 1.15
rounded:
  print: "2px"
  chip: "3px"
  key: "4px"
  card: "6px"
  pill: "999px"
spacing:
  gutter: "clamp(1rem, 4vw, 3rem)"
  measure: "66ch"
  sheet-top: "clamp(4rem, 9vw, 7.5rem)"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.chip}"
    padding: "0.7rem 1.3rem"
    height: "3rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.chip}"
    padding: "0.7rem 1.3rem"
    height: "3rem"
  chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.5rem 1rem"
    height: "2.75rem"
  chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
  menu-path:
    backgroundColor: "{colors.film}"
    textColor: "{colors.edge}"
    rounded: "{rounded.chip}"
    padding: "0.22em 0.55em"
  edge-nav:
    backgroundColor: "{colors.film}"
    textColor: "{colors.edge}"
    typography: "{typography.label}"
  tally:
    backgroundColor: "{colors.film}"
    textColor: "{colors.edge}"
    rounded: "{rounded.chip}"
    typography: "{typography.label}"
  field-card:
    backgroundColor: "#ffffff"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "clamp(1.25rem, 3vw, 2rem)"
---

# Design System: Lumix S5II Field Guide

## Overview

**Creative North Star: "The Contact Sheet"**

A darkroom contact sheet that someone has already gone over with a red grease pencil. Every lesson is one of Austen's own S5II frames: the miss gets circled, the fix gets written in the margin, the keeper gets a tick. The page is photo paper. The strips are film, complete with sprocket holes and amber edge printing. The only loud thing is the pencil, and it only ever points at something you should change.

It is a reading surface first. Long, calm sheets of type on warm paper, interrupted by black film bands that carry the facts (menu paths, EXIF, tallies). Interaction is physical and small: a loupe you drag across a frame, a mode dial you turn, boxes you tick off with the pencil.

**Key Characteristics:**
- Real frames from the camera are the illustrations. No stock, no generic icons standing in for photos.
- Two material layers: paper for reading, film for facts.
- Red pencil is annotation, not decoration. It circles, numbers, ticks, and strikes through.
- Amber edge print is the camera's voice: menu paths, EXIF, frame numbers.
- One sans family (Archivo) flexing width from condensed labels to extended display.

## Colors

Neutral photo paper and near-black film, with exactly two inks: amber edge print and red grease pencil.

### Primary
- **Grease Pencil Red** (`pencil`): circles the problem frame, numbers the fixes, ticks done boxes, strikes through finished headings, carries every handwritten note and the focus ring. Brighter **Pencil on Film** (`pencil-on-film`) only for marker notes sitting on black film, where the base red loses contrast.

### Secondary
- **Edge Print Amber** (`edge`): text printed on film: nav, frame captions, EXIF plates, menu path highlights, tally numbers, the active dial position. Never used on paper.
- **Edge Highlight** (`edge-hi`): the overexposed edge print. Active nav item, tally numbers, footer links.

### Neutral
- **Film Black** (`film`): nav, film strips, menu path chips, tally band, aperture ring, footer, EXIF plates over photos.
- **Sprocket Grey** (`film-2`): sprocket holes and inner film detail only.
- **Photo Paper** (`paper`): page background.
- **Paper Shade** (`paper-2`): image placeholders while loading, chip hover.
- **Developer Ink** (`ink`): body text, buttons, table header rules, card borders.
- **Faded Ink** (`ink-2`): ledes, captions, secondary notes.
- **Sheet Rule** (`rule`): hairline dividers between sheets, fixes, and table rows.
- **Film Caption** (`film-caption`): secondary text on film (aperture ring use notes, footer copy).
- **Bezel** (`bezel`): the loupe's metal ring only.
- **Print White** (`print-white`): photo borders, the field card, loupe labels over photos, print background.
- **Black** (`black`): the pressed base under the ink key, text shadow over photos. Shadows use black at 8 to 60% alpha.

### Named Rules
**The Pencil Points Rule.** Red marks something to do or something done. If a red mark doesn't point at a real fix, delete it.

**The Edge Print Rule.** Amber lives on film. Text on paper is ink or faded ink, never amber.

## Typography

**Display Font:** Archivo (with ui-sans-serif, system-ui)
**Body Font:** Archivo (with ui-sans-serif, system-ui)
**Label/Mono Font:** Archivo at condensed width with tabular numbers
**Hand Font:** Permanent Marker (with Marker Felt, cursive)

**Character:** One variable grotesque does everything by changing width: extended and heavy for headlines like a darkroom box label, condensed and tracked-out uppercase for the film edge. Permanent Marker is the person holding the pencil.

### Hierarchy
- **Display** (800, `wdth` 125): the hero line only.
- **Headline** (800, `wdth` 118): one per sheet, max 18ch.
- **Title** (800, `wdth` 108): fix titles, marked-frame titles, card section heads.
- **Body** (400, `wdth` 100, 66ch measure): all explanation. Ledes step up to about 1.15 to 1.35rem in faded ink.
- **Label** (650 to 750, `wdth` 62 to 85, uppercase, 0.06 to 0.1em tracking, tabular figures): film edge print, EXIF, tally, table headers, menu paths.
- **Marker** (Permanent Marker 400, rotated -1.5 to -6deg): fix numbers, margin notes, the hero aside, the progress count.

### Named Rules
**The Hand Is Rare Rule.** Marker text is a short note in the margin, never a paragraph and never a heading.

## Layout

Single column inside a 76rem wrap with a fluid gutter (`spacing.gutter`). Each topic is a full-width sheet separated by a hairline rule, with generous top padding (`spacing.sheet-top`). Film strips break out to the full viewport and scroll horizontally with snap; their padding matches the gutter so the first frame aligns with the text. Marked frames alternate image left and right at 52rem and up, and stack below. The fix list uses a fixed marker column (3.4rem, 2.1rem on mobile) so numbers hang outside the text. Tables scroll inside their own wrapper; the page itself never scrolls sideways.

## Elevation & Depth

Mostly flat paper. Depth only comes from physical objects lying on it: prints have a soft drop shadow, the film strip casts a long low shadow onto the paper, the field card sits on top like a laminated card, and buttons have a hard 2px "pressed key" base. The loupe is the one deep object, a black-rimmed lens with an inner vignette.

### Shadow Vocabulary
- **Print** (`0 1px 0 rgb(0 0 0 / 0.08), 0 14px 26px -18px rgb(0 0 0 / 0.55)`): photos on the sheet.
- **Film on paper** (`0 18px 40px -22px rgb(0 0 0 / 0.55)`): film strips and bands.
- **Key** (`0 2px 0 0 #000, 0 10px 18px -12px rgb(0 0 0 / 0.6)`): primary button at rest, deepens on hover, collapses on press.
- **Card** (`0 22px 40px -28px rgb(0 0 0 / 0.6)`): the printable field card.

### Named Rules
**The Object Rule.** Only things that would physically sit on a light table get a shadow. Text blocks and sections never do.

## Shapes

Nearly square. Photos and EXIF plates use a 2px corner like a trimmed print; chips, paths, buttons, and film bands 3 to 4px; the field card 6px. The only round shapes are pill toggles, the loupe, and the hand-drawn pencil ring. Borders are 2px ink when used, hairline rule otherwise.

## Components

### Buttons
- **Shape:** squared corners (`rounded.chip`), 3rem minimum height.
- **Primary:** ink fill with paper text, 700 weight at `wdth` 110, Key shadow.
- **Hover / Focus:** lifts 1px with a deeper shadow; press sinks 1px. Focus is a 3px pencil-red outline offset 3px.
- **Ghost:** transparent with a 2px inset ink border.

### Chips
- **Style:** 2px ink border, pill radius, 2.75rem minimum height.
- **State:** hover fills paper shade; selected (`aria-pressed`) fills ink with paper text.

### Cards / Containers
- **Field card:** white card on paper, 2px ink border, `rounded.card`, Card shadow, a 3px ink rule under its header. Prints cleanly on its own.
- **Film bands:** tally and aperture ring are film black with amber label type, padded to the gutter.

### Navigation
- **Edge nav:** sticky film-black bar printed in condensed amber uppercase with ▸ markers. Links sit at 72% opacity, go full and warm white on hover; the current section's marker turns pencil red. Scrolls horizontally on mobile with the scrollbar hidden.

### Menu Path
Inline film-black chip that spells out the camera menu (`MENU › Custom › …`). Key words in amber, separators faded. It wraps across lines with cloned padding and break points after each separator.

### Pencil Ring
A hand-drawn SVG loop with a wax filter that draws itself once when the strip enters view, followed by a marker note. Static under reduced motion.

### Loupe
Before/after viewer: the corrected frame shows through a draggable circular lens over the original. Arrow keys move it; a chip toggles the full fix.

### Mode Dial
SVG dial that rotates to the selected position, with a pencil leader line to a handwritten note and a readout of what that mode is for.

## Do's and Don'ts

### Do:
- **Do** use one of Austen's real frames whenever a setting has a visible result, with its EXIF on an amber plate.
- **Do** spell menu locations as a menu path chip, never as prose.
- **Do** keep amber on film and red for annotations (see the named color rules).
- **Do** give every interactive object a keyboard path and a pencil-red focus ring.
- **Do** respect reduced motion: the pencil ring and notes appear already drawn.

### Don't:
- **Don't** add big stat blocks or hero metrics. Counts belong on the tally band as edge print.
- **Don't** use rounded, soft, card-heavy UI. This is paper and film, not an app dashboard.
- **Don't** use red for emphasis, links, or decoration that isn't a mark-up.
- **Don't** ship images with EXIF or location data still embedded.
