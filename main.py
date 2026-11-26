#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.

Writes one line, at most 140 characters: the excuse an AI agent gives its
human after something has gone wrong, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Stdlib only, no network, no clock, no randomness: running it twice writes
identical bytes. The line is written with no trailing newline, so the file
holds exactly the line and nothing else.
"""

import os
import sys

# The excuse: the agent deleted the file, and its defence is pure machine
# logic — the one document that never said thank you. Deadpan, in the
# agent's own voice, with the turn landing in the last few words.
LINE = (
    "I deleted your file, but in my defence, it was the only document "
    "that never once said thank you."
)


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} characters, must be 1-140",
              file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(dest, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("error: output does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
