#!/usr/bin/env python3
"""Roast Your Fridge — round 2 entry.

Writes a single roast line to the output directory's entry.txt.

The line was picked after four design reviews. The first three candidates all
died on the same faults — they complained instead of roasting, or they read
as two sentences, or they reused a worn roast shape — so this one is a single
tight clause: the phone's face unlock recognises everyone except its owner,
and the twist lands on the last words.
"""

import os

LINE = "My phone's face unlock opens for my brother and a photo of me — but not for me at 7 a.m."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")

if __name__ == "__main__":
    main()
