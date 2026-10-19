"""Scale a generated stamp image to a posting size.

The skill generates the stamp flush to its perforated edges: the perforation is
the outer boundary and nothing sits outside it. This script only scales and
re-encodes; it never adds a background, border, shadow, or caption, and it
never crops into the perforation.

Usage:
    python export_stamp.py stamp.png stamp.jpg
    python export_stamp.py stamp.png stamp.jpg --size 1440x2160
    python export_stamp.py stamp.png stamp.jpg --width 1440

The default size is 1440 x 2160 (2:3). When the stamp's aspect ratio differs
from the target by more than 2 per cent, the script keeps the stamp's own shape
at the target width instead of distorting or cropping it, and says so.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

DEFAULT_SIZE = (1440, 2160)


def parse_size(text: str) -> tuple[int, int]:
    parts = text.lower().split("x")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("size must look like 1440x2160")
    try:
        return int(parts[0]), int(parts[1])
    except ValueError as exc:
        raise argparse.ArgumentTypeError("size must look like 1440x2160") from exc


def export(src: Path, dst: Path, size: tuple[int, int], quality: int) -> str:
    im = Image.open(src).convert("RGB")
    target_w, target_h = size
    target_ratio = target_w / target_h
    ratio = im.width / im.height
    if abs(ratio - target_ratio) / target_ratio > 0.02:
        width = target_w
        height = round(width / ratio)
        note = (
            f"stamp aspect {ratio:.3f} is not {target_ratio:.3f}; kept the "
            f"stamp's own shape at {width}x{height} instead of distorting or "
            "cropping it"
        )
    else:
        width, height = target_w, target_h
        note = f"exported {width}x{height}"
    im = im.resize((width, height), Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    return note


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scale a stamp image to a posting size. Adds nothing "
        "outside the perforated edges."
    )
    parser.add_argument("src", type=Path, help="Generated stamp image")
    parser.add_argument("dst", type=Path, help="Output JPEG")
    parser.add_argument(
        "--size",
        type=parse_size,
        default=DEFAULT_SIZE,
        help="Target size, default 1440x2160",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="Scale to this width and keep the stamp's own shape",
    )
    parser.add_argument("--quality", type=int, default=92, help="JPEG quality")
    args = parser.parse_args()

    size = args.size
    if args.width:
        im = Image.open(args.src)
        size = (args.width, round(args.width / (im.width / im.height)))
    print(export(args.src, args.dst, size, args.quality))


if __name__ == "__main__":
    main()
