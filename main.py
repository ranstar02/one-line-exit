#!/usr/bin/env python3
"""The One-Line Exit — a deterministic one-line resignation letter writer.

Running this program writes exactly one original, funny one-line
resignation letter to /output/entry.txt (or $ENTRY_OUTPUT when set),
then reads the file back and fails loudly on any mismatch.
No randomness, no network, no secrets, nothing read from outside this repo.
"""

import os
import sys

LINE = (
    "I resign as the zoo's penguin keeper, effective immediately: "
    "the penguins have unionised, and I have decided to join them."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"ERROR: line is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("ERROR: line must be exactly one line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("ERROR: line must not be only whitespace", file=sys.stderr)
        return 1

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify what was written by reading it back.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: verification failed, file content differs", file=sys.stderr)
        return 1

    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
