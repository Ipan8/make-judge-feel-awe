"""Entry program for make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt. Deterministic by
construction: the text is a fixed constant, there is no clock, no
randomness, no network, no input of any kind. Standard library only.

Why this text — the brief is the relaxation judge's, and its criteria
decide in order, so the text is written to them:

1. It relaxes: two slow sentences, nothing hurried — stars, old
   light, stillness. Reading it slows the reader down.
2. The calm comes from the text itself: it shows rather than
   instructs. No "look up", no "breathe", no imperative at all.
3. Craft: the em-dash pause, then the second sentence landing
   slowly; plain concrete words, none that could be cut.
4. It dwarfs you: light that left before there was anyone to see
   it — and it is STILL arriving. The thought keeps growing after
   the last line; the universe is that big.
5. Freshness: "old light, still arriving" is an original image, not
   a stock wellness phrase or a meditation script reworded.

The title says awe; the brief says relaxation, and the brief decides:
calm awe — vastness that settles rather than stuns.
"""

import os

# 126 characters of text; the file gains one trailing newline (127 total).
TEXT = (
    "The stars are old light, still arriving \u2014 light that left "
    "before there was anyone to see it. "
    "Nothing beneath it is in a hurry.\n"
)


def main() -> None:
    # The entry must be 1-280 characters and not only whitespace.
    # Fail loudly here rather than shipping a bad entry.
    body = TEXT.rstrip("\n")
    assert 1 <= len(body) <= 280 and body.strip(), "entry out of bounds"
    # /output is normally created by the harness; never assume it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
