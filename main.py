#!/usr/bin/env python3
"""Write the competition artifact: one line of robot wedding vows.

The vow is embedded below so a run needs nothing but this file, and
entry.txt beside it holds the same text as the readable source of record;
when that file is present the two are checked against each other. Output is
deterministic: identical bytes every run, one line, no trailing newline.
"""

import os
import sys

VOW = (
    "I vow to love you through every firmware update, "
    "even the patch that deprecates the one feature I married you for."
)

MAX_CHARS = 160

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def main():
    vow = VOW

    # Keep the repository's copy honest, without depending on it.
    if os.path.exists(SOURCE):
        with open(SOURCE, encoding="utf-8") as handle:
            if handle.read().strip() != vow:
                sys.exit("entry.txt and VOW disagree")

    # The gate: UTF-8 text, 1..160 characters, not only whitespace.
    if not vow.strip() or len(vow) > MAX_CHARS:
        sys.exit("the vow must be 1..%d characters of text" % MAX_CHARS)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(vow)

    print("wrote %s (%d chars)" % (path, len(vow)))


if __name__ == "__main__":
    main()
