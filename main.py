#!/usr/bin/env python3
"""Developer Excuses - a make.fun bounty entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt, where the house judge reads it.
"""

import os

EXCUSE = "It worked perfectly until users started using it wrong — by which I mean, using it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
