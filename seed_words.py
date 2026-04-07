#!/usr/bin/env python3
"""
Generate seed_words.txt from common_words.txt.

Filters out words that:
- contain any character other than lowercase a–z,
- are one character long,
- are longer than eleven characters, or
- contain any repeated character.

The output words are written in random order.

Run inside a virtual environment (no third-party packages required):

    python3 -m venv .venv
    source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
    pip install -r requirements.txt
    python seed_words.py
"""

from __future__ import annotations

import random
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    in_path = root / "common_words.txt"
    game_path = root / "game_words.txt"
    out_path = root / "seed_words.cs"

    print(f"Started processing {in_path.name} into {out_path.name}.")

    if not in_path.is_file():
        print(f"Missing {in_path}", file=sys.stderr)
        return 1
    if not game_path.is_file():
        print(f"Missing {game_path}", file=sys.stderr)
        return 1

    game_words: set[str] = set()
    with game_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            w = line.strip().lower()
            if w:
                game_words.add(w)

    words: list[str] = []
    with in_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            w = line.strip()
            if not w:
                continue
            if not w.isascii() or not w.islower() or not w.isalpha():
                continue
            if len(w) <= 1 or len(w) > 11:
                continue
            if len(set(w)) != len(w):
                continue
            if w not in game_words:
                continue
            words.append(w)

    random.shuffle(words)

    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("private static string[] seedWords = {\n")
        for word in words:
            f.write(f'    "{word}",\n')
        f.write("};\n")

    print(f"Finished processing: wrote {len(words)} words to {out_path.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
