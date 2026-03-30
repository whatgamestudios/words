#!/usr/bin/env python3
"""
Print words from new_words.txt that also appear in words_alpha.txt.

Run inside a virtual environment (no third-party packages required):

    python3 -m venv .venv
    source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
    python check_new_words.py
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    alpha_path = root / "words_alpha.txt"
    new_path = root / "new_words.txt"

    print("Duplicate words:")


    if not alpha_path.is_file():
        print(f"Missing {alpha_path}", file=sys.stderr)
        return 1
    if not new_path.is_file():
        print(f"Missing {new_path}", file=sys.stderr)
        return 1

    alpha: set[str] = set()
    with alpha_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            w = line.strip().lower()
            if w:
                alpha.add(w)

    seen_out: set[str] = set()
    with new_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            w = line.strip().lower()
            if not w:
                continue
            if w in alpha and w not in seen_out:
                seen_out.add(w)
                print(f" {w}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
