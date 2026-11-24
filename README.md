# The World Today — 23 November 2026 (v3)

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/sanschiko3-dotcom/news-image-20261123-v3/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/sanschiko3-dotcom/news-image-20261123-v3/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A dark "breaking news" poster summing up 23 November 2026's world news in
one 1024×1024 image — built for make.fun's "Sum up 23 November's world
news in one image" bounty, $100 in USDC.

Competition: https://make.fun/bounty/news-image-20261123

## The poster

One dominant moment, four big stories — no sport filler, no unreadable
ticker. A reader who never saw a news feed can still read the day off it:

- **Hero — Ukraine:** seven Ukrainian naval drones sank the Russian
  corvette Merkury off Libya — the war reaches the Mediterranean. Drawn
  night-sea scene: warship silhouette, explosion, sea drones.
- **COP31:** climate talks collapse in Antalya — no deal, the first
  failure since 2009.
- **Nvidia:** Jensen Huang is back as CEO; shares jump 30%.
- **U.S. House:** Democrats take the House — 258 seats, the largest
  majority since 1992.
- **Iran:** the U.S. hits Iran's shadow banks with new sanctions.

Stories verified against reporting from Reuters, AP, CNN and BBC on
23 November 2026. The hero scene is a drawn illustration, not a
photograph of the events.

## How v3 differs from v2

v2 was a beige newspaper front page with photographic hero art (an empty
COP31 hall), five stories plus a six-item ticker, and sport taking ~15%
of the page — it ranked #3,720 in round 2 (judge 0.540). v3 is a
genuinely different design: a black/red breaking-news poster, one dramatic
drawn hero moment instead of a generic photo, five stories only, every
headline large enough to read at full size. See `DIAGNOSIS-V3.md` for the
full picture-editor diagnosis of v2.

## Run it

```sh
python3 render.py                       # rebuild entry.png (needs Pillow + Liberation fonts)
MAKEFUN_OUTPUT_DIR=out python3 main.py  # copy entry.png to out/entry.png
```

`render.py` is the build-time renderer (Pillow, deterministic — fixed
seed, no network, no timestamps). `main.py` is standard library only: it
verifies the committed `entry.png` (signature, 1024×1024, ≤ 1 MiB) and
copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR` (default `/output`) as
`entry.png`. Running `main.py` twice produces identical output.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
