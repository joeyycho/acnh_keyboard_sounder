#!/usr/bin/env python3
"""Fail if any sounds/* filename is illegal on Windows."""

from __future__ import annotations

import sys
from pathlib import Path

INVALID = '<>:"/\\|?*'
ROOT = Path(__file__).resolve().parents[1]
SOUNDS = ROOT / "sounds"


def main() -> int:
    if not SOUNDS.is_dir():
        print(f"missing sounds dir: {SOUNDS}", file=sys.stderr)
        return 1

    bad: list[str] = []
    for path in sorted(SOUNDS.iterdir()):
        if not path.is_file():
            continue
        name = path.name
        if any(c in INVALID or ord(c) < 32 for c in name):
            bad.append(repr(name))
        if name.endswith(" ") or name.endswith("."):
            bad.append(repr(name))

    if bad:
        print("Windows-illegal sound filenames:", file=sys.stderr)
        for item in bad:
            print(f"  - {item}", file=sys.stderr)
        print(
            "Rename them (see SAFE_SOUND_FILES in main.py) before releasing.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: {sum(1 for p in SOUNDS.iterdir() if p.is_file())} sound files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
