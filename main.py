#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (1-200 characters) to /output/entry.txt.
"""

import os

ROAST = (
    "My $200 noise-cancelling earbuds block out the whole world but not "
    "my own chewing \u2014 turns out I was the noise all along."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
