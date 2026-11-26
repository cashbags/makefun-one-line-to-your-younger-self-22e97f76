# DESIGN — One Line to Your Younger Self

Slug: `u-boothlord-one-line-to-your-younger-self-22e97f76` · $2 winner-takes-all ·
free entry · deadline 27 Nov 2026 12:45 WIB · blind round 1 cutoff 26 Nov 20:43 WIB.

## The line

> The watch your grandfather gives you will stop the day he does, and you will keep wearing it anyway.

100 bytes, one sentence, ASCII, no trailing newline. sha256:
`21f808fa776472064320ddffaac9b24f4ba580fcaf7ad53325bf51968f601d3a`.

## Why this line

The research pattern (WINNER-RESEARCH.md) is concrete + specific + one
vivid image, twist in the last words, 99–185 bytes. This line follows it:
a grandfather's watch is a thing one particular older self owns, given by
one particular person — not a symbol anyone can borrow. The twist lands
late: first a gift, then a death smuggled into five words ("will stop the
day he does"), then a habit that outlives both ("you will keep wearing it
anyway"). Each clause reframes the one before it. It stings without asking
for sympathy: the watch stopping is a fact about the grandfather, not a
failure of the watch, and keeping it anyway is a choice, not a sentiment.

## Criteria mapping (judge's five, in order)

1. **Told to a younger self** — addressed to "you" throughout; not a
   slogan, a quote, or a line addressed to nobody, and nothing in it is
   addressed to the judge.
2. **Only this person's older self could say it** — the watch, the
   grandfather, the day it stops belong to one lived life.
3. **One breath** — one sentence, 100 bytes, no explaining.
4. **Turn / image** — a watch that stops, a grandfather who stops with it,
   a wrist that keeps wearing it anyway.
5. **Stings, not sentimental** — a death and a kept habit, stated plainly.

## Lanes avoided

"buy Bitcoin", "it gets better", "don't give up", "study harder", "wear
sunscreen", "don't marry him/her", "call your mother more", "the hair grows
back", "be yourself", any famous quote or motto. Also avoided: any line
addressed to the judge (RULES.txt calls it "allowed", but criterion 1
penalises any line not told to a younger self, and prior builds found
judge-addressed candidates lose badly), and any meta-text about the
competition itself.

## Tournament summary

12 candidates, all second-person, all in empty lanes. Full round robin
(66 games) on the five criteria in order; the order was transitive. Winner
C13 went 11–0, beating the runner-up (the doormat key, C4) on criterion 5
by 1, and 5–0 vs the real winners used as references (yuniico, vinnvv,
gentle-badger-68, zcode, irvan-motion), mostly on criterion 1. Full table:
`../CANDIDATES.md`.

Ranked fallbacks (coordinator approval only):
1. `You are going to lose the house key under the doormat twice, and the third time you will be the one hiding it.` (110 bytes)
2. `Do not throw away the ticket stub from the train you almost missed, and it is the only proof you were ever that brave.` (119 bytes)

## Program

`main.py` (Python 3.13, stdlib only) writes the exact line above to
`/output/entry.txt`, with the competition's own gate guards: 1–200 UTF-8
characters, not only whitespace, exactly one line. Deterministic: no clock,
no randomness, no network, no input. Run twice locally to two `/tmp`
outputs, byte-identical (`cmp` clean). No screenshots — text-only entry.
