#!/usr/bin/env python3
"""Escalated to God — a one-liner for make.fun's One Line, Big Laugh.

Writes the winning one-liner, exactly as written, to /output/entry.txt.
No trailing newline: the file holds the line and nothing else, so the
entry is byte-for-byte the joke (123 chars, inside the 1-200 gate).

The line won a blind 6-way pairwise tournament 5-0 (runner-up 4-1) against
the competition's own judge brief: a support ticket escalated from "user
error" to "cosmic error" to God — who is still on hold.
"""

LINE = (
    'IT support closed my ticket as "user error", reopened it as '
    '"cosmic error", then escalated me to God, who is still on hold.'
)


def main() -> None:
    import os
    from pathlib import Path

    # Harness reads /output/entry.txt; allow OUTPUT_DIR override for local runs.
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Guard the judge gate: one line, 1-200 chars, no trailing newline.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line fails the gate"
    out_dir.joinpath("entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
