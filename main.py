#!/usr/bin/env python3
"""Write the Monday Morning Punchlines entry to /output/entry.txt.

The joke treats the weekend like a standup ticket: reported as blocked by
Monday, then dragged into the backlog to be forgotten forever.

The output directory defaults to /output and can be overridden with the
OUTPUT_DIR environment variable. The entry is written as UTF-8 with no
trailing newline.
"""

import os
from pathlib import Path

ENTRY = "Monday morning standup: I reported my weekend as 'blocked by Monday' and dragged it into the backlog forever."


def write_entry() -> Path:
    """Write ENTRY to the output directory and return the file's path."""
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "entry.txt"
    path.write_text(ENTRY, encoding="utf-8")
    return path


def main() -> None:
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
