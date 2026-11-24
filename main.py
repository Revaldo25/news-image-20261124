#!/usr/bin/env python3
"""news-image-20261124 entry: copy the poster to the output directory.

The grader runs this with no network. The image is the entry.png shipped
beside this file; the program copies it to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR when set, for local runs). Deterministic: a plain
byte copy, identical on every run.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
DST = OUT_DIR / "entry.png"

if not SRC.is_file():
    print(f"missing source image: {SRC}", file=sys.stderr)
    raise SystemExit(1)

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)

# Fail loudly instead of shipping a truncated copy: the grader must see
# the exact bytes that were built and checked.
if DST.stat().st_size != SRC.stat().st_size:
    print(f"copy incomplete: {DST} ({DST.stat().st_size} bytes, expected {SRC.stat().st_size})", file=sys.stderr)
    raise SystemExit(1)

print(f"wrote {DST} ({DST.stat().st_size} bytes)")
