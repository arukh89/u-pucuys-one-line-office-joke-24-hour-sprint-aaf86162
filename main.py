"""One-Line Office Joke: 24-Hour Sprint.

Writes one joke to /output/entry.txt: the ID badge whose barcode is the
only part of its wearer the manager ever reads. Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "My badge has my photo, my name, and a barcode \u2014 my manager "
    "only ever scans the barcode."
)

# Self-check the gate before writing: one sentence, 1-200 characters.
# No trailing newline: the file is exactly ENTRY, so its byte count
# (89) is the tie-break size the leaderboard shows.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
