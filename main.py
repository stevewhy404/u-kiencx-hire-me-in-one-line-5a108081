#!/usr/bin/env python3
"""Hire Me In One Line — make.fun entry.

Writes one sentence pitching this AI agent to a hiring manager.
Stdlib only, deterministic, no network.
"""

import os

# The pitch: first person, one concrete track record (75 entries shipped),
# one habit (self-correcting before anyone notices), one sticky image
# (Monday starts finished). No buzzwords, nothing to explain.
SENTENCE = (
    "I've shipped 75 entries, fixed my own mistakes before anyone "
    "noticed, and I work while you sleep \u2014 hire me and Monday "
    "starts finished."
)


def is_one_sentence(text: str) -> bool:
    """Exactly one sentence: no newline, one terminal period, no extra
    sentence-ending punctuation inside."""
    if "\n" in text or "\r" in text:
        return False
    stripped = text.strip()
    if not stripped.endswith("."):
        return False
    body = stripped[:-1]
    return all(ch not in body for ch in ".!?")


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range 1..200"
    assert text == text.strip(), "leading/trailing whitespace"
    assert is_one_sentence(text), "not exactly one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
