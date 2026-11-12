#!/usr/bin/env python3
"""Download source images listed in images_manifest.csv.
Run from this folder: python download_images.py
Requires Python 3.9+ and internet access.
"""
import csv
import pathlib
import time
import urllib.request
import urllib.error

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "images"
OUT.mkdir(exist_ok=True)
MANIFEST = BASE / "images_manifest.csv"
USER_AGENT = "OpenCatDetectionPortfolio/1.0 (personal annotation portfolio)"

with MANIFEST.open(newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))

for row in rows:
    target = OUT / row["filename"]
    if target.exists() and target.stat().st_size > 0:
        print(f"SKIP {target.name} (already exists)")
        continue
    request = urllib.request.Request(
        row["direct_image_url"],
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            target.write_bytes(response.read())
        print(f"OK   {target.name}")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"FAIL {target.name}: {exc}")
        if target.exists():
            target.unlink()
    time.sleep(1.0)

present = sum(1 for p in OUT.iterdir() if p.is_file())
print(f"Finished. Files present: {present}/{len(rows)}")
