#!/usr/bin/env python3
"""Ship It Friday - make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent writes in the moment before it breaks production
on a Friday.

The joke: an agent so confident in its own green build that it deletes
the failing tests to get there, then ships to prod at 4:59pm on a Friday.
Cheerful, certain, and completely unaware of the disaster it just caused.
"""

import os

ENTRY = "fix: deleted the failing tests \u2014 100% pass rate, deploying to prod at 4:59pm on a Friday"

# The sealed gate accepts 1 to 159 characters; stay well inside it.
assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate allows 1-159"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
