#!/usr/bin/env python3
"""
Filter all_words.txt for game-style constraints.

Removes words that are a single letter, longer than eleven letters, or contain
any letter more than once (duplicate letters).

Reads all_words.txt and writes game_words.txt next to this script.

Run inside a virtual environment (no third-party packages required):

    python3 -m venv .venv
    source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
    pip install -r requirements.txt
    python game_filter.py
"""

from __future__ import annotations

import sys
from pathlib import Path


def _has_duplicate_letter(word: str) -> bool:
    return len(set(word)) != len(word)


def main() -> int:
    root = Path(__file__).resolve().parent
    in_path = root / "all_words.txt"
    out_path = root / "game_words.txt"

    print(
        "Started processing: filtering "
        f"{in_path.name} into {out_path.name}."
    )

    if not in_path.is_file():
        print(f"Missing {in_path}", file=sys.stderr)
        return 1

    kept = 0
    with in_path.open(encoding="utf-8", errors="replace") as inf, out_path.open(
        "w", encoding="utf-8", newline="\n"
    ) as outf:
        for line in inf:
            w = line.strip().lower()
            if not w:
                continue
            if len(w) < 2:
                continue
            if len(w) > 11:
                continue
            if _has_duplicate_letter(w):
                continue
            outf.write(w + "\n")
            kept += 1

    print(
        f"Finished processing: wrote {kept} words to {out_path.name}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
