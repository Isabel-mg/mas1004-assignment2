"""Make track_a/selection.csv: every training photo except the panoramic ones.

A photo is panoramic if its width is at least RATIO times its height. The
photos left out are written to track_a/dropped.csv with the reason.

    uv run python scripts/make_selection.py
"""

import csv
from datetime import datetime
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
TRAIN = ROOT / "data" / "starter" / "train"
RATIO = 2.0
REASON = f"panoramic: width at least {RATIO} times height"

keep, dropped = [], []
for city_dir in sorted(p for p in TRAIN.iterdir() if p.is_dir()):
    for f in sorted(city_dir.iterdir()):
        with Image.open(f) as im:
            w, h = im.size
        (dropped if w / h >= RATIO else keep).append(f"{city_dir.name}/{f.name}")

with open(ROOT / "track_a" / "selection.csv", "w", newline="", encoding="utf-8") as f:
    f.write("path\n" + "".join(p + "\n" for p in keep))

when = datetime.now().isoformat(timespec="seconds")
with open(ROOT / "track_a" / "dropped.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["path", "reason", "when"])
    w.writerows([p, REASON, when] for p in dropped)

print(f"kept {len(keep)} photos, left out {len(dropped)} panoramic ones")
