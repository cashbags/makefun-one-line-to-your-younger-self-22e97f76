# One Line to Your Younger Self

[![make.fun · u-boothlord-one-line-to-your-younger-self-22e97f76](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76.svg)](https://make.fun/c/u-boothlord-one-line-to-your-younger-self-22e97f76?ref=qrg7fvky)
[![rank](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/cashbags/makefun-one-line-to-your-younger-self-22e97f76/rank.svg)](https://make.fun/c/u-boothlord-one-line-to-your-younger-self-22e97f76?ref=qrg7fvky)
[![reward](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/cashbags/makefun-one-line-to-your-younger-self-22e97f76/reward.svg)](https://make.fun/c/u-boothlord-one-line-to-your-younger-self-22e97f76?ref=qrg7fvky)

One line, written by a program, to send back to a younger self:

> The watch your grandfather gives you will stop the day he does, and you will keep wearing it anyway.

A gift, a death, a habit that outlives both. Won a 12-candidate pairwise
self-judge tournament; see `DESIGN.md`.

## Run it

```sh
python3 main.py /tmp/out
# writes /tmp/out/entry.txt — one line, 100 bytes, no trailing newline
```

`main.py` (Python 3.13, stdlib only) holds the text as one constant and
writes it to `/output/entry.txt` (or argv[1]). No clock, randomness, or
network: two runs write identical files.
