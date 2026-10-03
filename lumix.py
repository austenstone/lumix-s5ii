#!/usr/bin/env python3
"""LUMIX S5II profile library: build stills LUTs, preview them, and sync looks/settings with the SD card."""
import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
LUT_DIR = ROOT / "luts"
CAMSET_DIR = ROOT / "camsets"
PREVIEW_DIR = ROOT / "previews"
CARD = Path("/Volumes/LUMIX")
CARD_CAMSET = CARD / "AD_LUMIX" / "CAMSET"
CARD_DCIM = CARD / "DCIM" / "100_PANA"
SIZE = 33
REC709 = np.array([0.2126, 0.7152, 0.0722])
CARD_NAME = re.compile(r"^[A-Z0-9]{1,8}$")

# Tuned for a Natural (or Standard) base Photo Style, full-range Rec.709 in and out.
# Deliberately strong: in-camera LUT opacity can only weaken a look.
LOOKS = {
    "WARM400": dict(contrast=-0.2, lift=0.035, cut=0.02, sat=0.9, shadow=(-0.01, 0.0, 0.01), highlight=(0.07, 0.035, -0.04)),
    "GOLD200": dict(contrast=0.2, lift=0.025, cut=0.01, sat=1.12, shadow=(0.02, 0.01, -0.02), highlight=(0.09, 0.05, -0.07)),
    "CHROME": dict(contrast=0.5, lift=0.015, cut=0.0, sat=0.65, shadow=(-0.02, 0.005, 0.03), highlight=(0.02, 0.01, -0.01)),
    "FADED": dict(contrast=-0.4, lift=0.12, cut=0.05, sat=0.75, shadow=(-0.03, 0.015, 0.035), highlight=(0.06, 0.03, -0.05)),
}


def grade(rgb, contrast, lift, cut, sat, shadow, highlight):
    x = rgb + 2 * contrast * rgb * (1 - rgb) * (rgb - 0.5)
    x = lift + (1 - lift - cut) * x
    luma = (x @ REC709)[..., None]
    x = luma + sat * (x - luma)
    x = x + np.array(shadow) * (1 - luma) ** 2 + np.array(highlight) * luma**2
    return np.clip(x, 0, 1)


def build_luts(_args):
    LUT_DIR.mkdir(exist_ok=True)
    grid = np.linspace(0, 1, SIZE)
    b, g, r = np.meshgrid(grid, grid, grid, indexing="ij")
    identity = np.stack([r, g, b], axis=-1).reshape(-1, 3)
    for name, params in LOOKS.items():
        rows = grade(identity, **params)
        body = "\n".join(f"{r:.6f} {g:.6f} {b:.6f}" for r, g, b in rows)
        # Without this tag (firmware 3.1+) the camera assumes the LUT expects a V-Log base.
        (LUT_DIR / f"{name}.cube").write_text(f'TITLE "{name}"\n#LUMIXPHOTOSTYLE NAT\nLUT_3D_SIZE {SIZE}\n{body}\n')
        print(f"built luts/{name}.cube")


def to_linear(x):
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def to_srgb(x):
    return np.where(x <= 0.0031308, x * 12.92, 1.055 * np.power(x, 1 / 2.4) - 0.055)


def gray_world(img, strength):
    lin = to_linear(np.asarray(img, dtype=np.float64) / 255)
    means = lin.reshape(-1, 3).mean(axis=0)
    gains = (means.mean() / means) ** strength
    return Image.fromarray((np.clip(to_srgb(np.clip(lin * gains, 0, 1)), 0, 1) * 255).astype(np.uint8))


def apply_lut(img, cube, workdir):
    src, dst = workdir / "in.png", workdir / f"{cube.stem}.png"
    img.save(src)
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"lut3d=file={cube}:interp=tetrahedral", str(dst)],
        check=True,
    )
    return Image.open(dst).convert("RGB")


def preview(args):
    cubes = sorted(LUT_DIR.glob("*.cube"))
    if not cubes:
        sys.exit("No LUTs in luts/. Run: lumix.py luts")
    samples = [Path(s) if "/" in s else CARD_DCIM / s for s in args.samples]
    font = ImageFont.load_default(size=22)
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for sample in samples:
            img = ImageOps.exif_transpose(Image.open(sample)).convert("RGB")
            img = img.resize((round(img.width * args.height / img.height), args.height), Image.LANCZOS)
            base = gray_world(img, args.wb_strength) if args.wb_strength else img
            tiles = [("BASE", base)]
            tiles += [(c.stem, apply_lut(base, c, Path(tmp))) for c in cubes]
            rows.append(tiles)
    sheet = Image.new("RGB", (max(sum(t.width for _, t in row) for row in rows), args.height * len(rows)), "white")
    draw = ImageDraw.Draw(sheet)
    for y, row in enumerate(rows):
        x = 0
        for label, tile in row:
            sheet.paste(tile, (x, y * args.height))
            draw.text((x + 10, y * args.height + 8), label, fill="white", font=font, stroke_width=2, stroke_fill="black")
            x += tile.width
    PREVIEW_DIR.mkdir(exist_ok=True)
    out = PREVIEW_DIR / "contact-sheet.jpg"
    sheet.save(out, quality=90)
    print(out)


def require_card():
    if not CARD.is_dir():
        sys.exit(f"{CARD} not mounted. Set the camera USB Mode to PC(Storage) or insert the SD card.")


def remove_appledouble(path):
    sidecar = path.with_name(f"._{path.name}")
    if sidecar.exists():
        sidecar.unlink()


def push(_args):
    require_card()
    for cube in sorted(LUT_DIR.glob("*.cube")):
        if not CARD_NAME.match(cube.stem):
            sys.exit(f"{cube.name}: FAT32 cards need 1-8 uppercase alphanumeric characters")
        dest = CARD / cube.name
        shutil.copyfile(cube, dest)
        remove_appledouble(dest)
        print(f"pushed {dest}")


def backup(_args):
    require_card()
    CAMSET_DIR.mkdir(exist_ok=True)
    for dat in sorted(CARD_CAMSET.glob("*.DAT")):
        digest = hashlib.sha256(dat.read_bytes()).hexdigest()[:8]
        stamp = datetime.fromtimestamp(dat.stat().st_mtime).strftime("%Y-%m-%d")
        dest = CAMSET_DIR / f"{dat.stem}_{stamp}_{digest}.DAT"
        if dest.exists():
            print(f"unchanged {dest.name}")
        else:
            shutil.copy2(dat, dest)
            print(f"saved {dest.name}")


def restore(args):
    require_card()
    src = CAMSET_DIR / args.file
    name = args.as_name or src.stem.split("_")[0]
    if not src.is_file():
        sys.exit(f"{src} not found")
    if not CARD_NAME.match(name):
        sys.exit(f"{name}: camera settings names must be 1-8 uppercase alphanumeric characters")
    dest = CARD_CAMSET / f"{name}.DAT"
    if dest.exists() and not args.force:
        sys.exit(f"{dest} exists. Back it up first, then use --force.")
    CARD_CAMSET.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    remove_appledouble(dest)
    print(f"restored {dest}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)
    sub.add_parser("luts", help="generate .cube looks into luts/").set_defaults(func=build_luts)
    p = sub.add_parser("preview", help="render a contact sheet of every LUT on sample photos")
    p.add_argument("samples", nargs="*", default=["P1004085.JPG", "P1004064.JPG", "P1004070.JPG"])
    p.add_argument("--height", type=int, default=300)
    p.add_argument("--wb-strength", type=float, default=1.0, help="gray-world correction for mis-white-balanced samples (0 disables)")
    p.set_defaults(func=preview)
    sub.add_parser("push", help="copy luts/*.cube to the card root").set_defaults(func=push)
    sub.add_parser("backup", help="archive AD_LUMIX/CAMSET/*.DAT from the card").set_defaults(func=backup)
    p = sub.add_parser("restore", help="copy an archived camera-settings file back to the card")
    p.add_argument("file", help="file name inside camsets/")
    p.add_argument("--as-name", help="name the camera will list (1-8 uppercase alphanumerics)")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=restore)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
