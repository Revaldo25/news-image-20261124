#!/usr/bin/env python3
"""news-image-20261124 entry: copy the poster to the output directory.

The grader runs this with no network. The image is the entry.png shipped
beside this file; the program copies it to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR when set, for local runs). Deterministic: a plain
byte copy, identical on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
