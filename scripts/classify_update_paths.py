#!/usr/bin/env python3
"""Classify the paths produced by the scheduled HCR refresh.

The Actions job uses this guard immediately before requesting GitHub auto-merge.
It is deliberately allowlist-only: a new output path must be reviewed before a
bot PR containing it can land without a human.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable


# These are exactly the paths staged by update-registry.yml's refresh job.
DATA_PATHS = (
    "registry/",
    "raw/",
    "generated/agent-guides/",
    "generated/reports/coverage.md",
    "generated/validation-report.json",
    "generated/source-drift-report.json",
)


def unsafe_paths(paths: Iterable[str]) -> list[str]:
    """Return changed paths that are not known generated/source data."""
    return [path for path in paths if path and not any(path == allowed or path.startswith(allowed) for allowed in DATA_PATHS)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="changed paths; omit to read newline-delimited paths from stdin")
    args = parser.parse_args(argv)
    paths = args.paths or [line.strip() for line in sys.stdin]
    unsafe = unsafe_paths(paths)
    if unsafe:
        print("AUTO_MERGE_BLOCKED non-data paths:", *unsafe, sep="\n", file=sys.stderr)
        return 1
    print("AUTO_MERGE_ALLOWED data-only paths:", *paths, sep="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
