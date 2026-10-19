#!/usr/bin/env python3
"""Place a stamp image on a 2:3 Pinterest pin canvas.

Usage:
    python make_pin.py stamp.png pin.jpg
    python make_pin.py stamp.png pin.jpg --title "Menelik II, 1894" \
        --caption "Concept stamp, not a real postal issue"

The script keeps the stamp complete, adds a cream paper background, a soft
shadow, and optional captions below the perforation. It never crops the stamp.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\georgiab.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]


def find_font() -> str | None:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return path
    return None


def paper(width: int, height: int, color: str) -> Image.Image:
    """Cream paper with a very light grain."""
    base = Image.new("RGB", (width, height), color)
    noise = Image.effect_noise((width, height), 6).convert("RGB")
    return Image.blend(base, noise, 0.035)


def add_shadow(canvas: Image.Image, stamp: Image.Image, x: int, y: int) -> None:
    """Paste a stamp with a soft drop shadow."""
    shadow = Image.new("RGBA", stamp.size, (43, 33, 24, 0))
    mask = Image.new("L", stamp.size, 0)
    ImageDraw.Draw(mask).rectangle([0, 0, stamp.width, stamp.height], fill=90)
    shadow.putalpha(mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    layer.paste(shadow, (x + 10, y + 14), shadow)
    canvas.alpha_composite(layer)
    canvas.paste(stamp, (x, y), stamp if stamp.mode == "RGBA" else None)


def make_pin(
    stamp_path: Path,
    out_path: Path,
    title: str = "",
    caption: str = "",
    width: int = 1440,
    height: int = 2160,
    bg: str = "#f4ecdc",
) -> Path:
    stamp = Image.open(stamp_path).convert("RGBA")
    canvas = paper(width, height, bg).convert("RGBA")

    # Leave room for the caption when one is requested.
    caption_room = int(height * 0.16) if (title or caption) else 0
    max_w = int(width * 0.74)
    max_h = int((height - caption_room) * 0.82)
    ratio = min(max_w / stamp.width, max_h / stamp.height)
    stamp = stamp.resize((max(1, round(stamp.width * ratio)), max(1, round(stamp.height * ratio))), Image.LANCZOS)

    x = (width - stamp.width) // 2
    y = int((height - caption_room - stamp.height) * 0.46)
    add_shadow(canvas, stamp, x, y)

    draw = ImageDraw.Draw(canvas)
    font_path = find_font()
    ty = y + stamp.height + 44
    if title:
        font_title = ImageFont.truetype(font_path, max(28, int(height * 0.026))) if font_path else ImageFont.load_default()
        draw.text((width // 2, ty), title, fill="#2b2118", font=font_title, anchor="ma")
        ty += int(height * 0.045)
    if caption:
        font_cap = ImageFont.truetype(font_path, max(20, int(height * 0.017))) if font_path else ImageFont.load_default()
        draw.text((width // 2, ty), caption, fill="#6b5f4c", font=font_cap, anchor="ma")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.suffix.lower() in (".jpg", ".jpeg"):
        canvas.convert("RGB").save(out_path, quality=92, optimize=True, progressive=True)
    else:
        canvas.save(out_path)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Place a stamp on a 2:3 Pinterest pin canvas.")
    parser.add_argument("stamp", type=Path, help="Stamp image (PNG, JPG, or WEBP)")
    parser.add_argument("output", type=Path, help="Output pin file (JPG or PNG)")
    parser.add_argument("--title", default="", help="Title below the stamp")
    parser.add_argument("--caption", default="", help="Small caption below the title")
    parser.add_argument("--width", type=int, default=1440, help="Pin width in pixels")
    parser.add_argument("--height", type=int, default=2160, help="Pin height in pixels")
    parser.add_argument("--bg", default="#f4ecdc", help="Paper colour")
    args = parser.parse_args()
    result = make_pin(args.stamp, args.output, args.title, args.caption, args.width, args.height, args.bg)
    print(result)


if __name__ == "__main__":
    main()
