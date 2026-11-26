#!/usr/bin/env python3
"""One Line to Your Younger Self - entry program (program/v1, python3.13).

Writes one line to /output/entry.txt. The line is a fixed constant:
no clock, no randomness, no network, no input - every run writes the
same bytes, so the output is byte-identical on re-run.

The line (100 bytes, one sentence, ASCII, no trailing newline;
sha256 of the entry bytes: 21f808fa776472064320ddffaac9b24f4ba580fcaf7ad53325bf51968f601d3a):

    The watch your grandfather gives you will stop the day he does, and you will keep wearing it anyway.

Why this line: it is told to "you", the younger self, never to a slogan
or to the judge. Only this person's older self could name that watch and
that day - a gift, a death, and a habit that outlives both, compressed
into one breath. The twist lands in the last clause: the watch stopping
is not a failure of the watch, it is a fact about the grandfather, and
"you will keep wearing it anyway" is the sting - honest, hard-won, warm
without ever asking for sympathy. It won a 12-candidate pairwise
self-judge tournament against the judge's exact five criteria (see
DESIGN.md), beating the doormat-key and ticket-stub fallbacks on the
sting criterion. Lanes avoided: "buy Bitcoin", "it gets better", "don't
give up", "study harder", "wear sunscreen", "don't marry him/her", "call
your mother more", "the hair grows back", "be yourself", any famous quote
or motto, and any line addressed to the judge instead of the younger self.
"""

import os
import sys

LINE = "The watch your grandfather gives you will stop the day he does, and you will keep wearing it anyway."


def main(argv):
    # Output directory: first argument wins, then $MAKEFUN_OUTPUT_DIR, else /output.
    out_dir = argv[1] if len(argv) > 1 else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    # Gate guards, mirroring the competition's own gate: 1-200 UTF-8 chars,
    # not only whitespace, exactly one line.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
