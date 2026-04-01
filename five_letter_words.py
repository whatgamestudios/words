#!/usr/bin/env python3
"""
Merge extract five letter words from all_words.txt.

Run inside a virtual environment (no third-party packages required):

    python3 -m venv .venv
    source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
    pip install -r requirements.txt
    python five_letter_words.py
"""

from __future__ import annotations

import sys
from pathlib import Path


def _collect_words(path: Path, into: set[str]) -> None:
    with path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            w = line.strip().lower()
            if len(w) == 5:
                into.add(w)


def main() -> int:
    root = Path(__file__).resolve().parent
    all_path = root / "game_words.txt"
    out_path = root / "five_words.txt"

    print(
        "Started processing "
        f"{all_path.name} into {out_path.name}."
    )

    if not all_path.is_file():
        print(f"Missing {all_path}", file=sys.stderr)
        return 1

    words: set[str] = set()
    _collect_words(all_path, words)

    sorted_words = sorted(words)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(sorted_words))
        if sorted_words:
            f.write("\n")

    print(
        f"Finished processing: wrote {len(sorted_words)} unique words to {out_path.name}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
