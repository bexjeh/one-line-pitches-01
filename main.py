#!/usr/bin/env python3
"""Write the one-line pitch entry to entry.txt.

The entry is a single sentence that convinces a friend who has never
coded to let an AI agent build their first app idea on make.fun.
It is emitted deterministically on every run.
"""

import os

SENTENCE = "You know that app idea you keep talking about \u2014 just describe it to an AI agent on make.fun and in a few minutes you\u2019ll have a first working version to try, change, or walk away from."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
