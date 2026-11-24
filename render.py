#!/usr/bin/env python3
"""Render news-image-20261123 v3: a dark 'breaking news' poster.

Build-time only (needs Pillow + Liberation fonts, present on the build VM).
The graded entrypoint is main.py (stdlib only), which just copies the
committed entry.png. This renderer is written from scratch for v3: a
night-sea hero illustration (Ukraine sea drones strike a Russian warship
off Libya) over four big, readable story rows. No photo assets, no
newspaper front-page layout — deliberately unlike v2.

Deterministic: fixed random seed, no timestamps, no network.
Run:  python3 render.py            -> writes entry.png next to this file
"""
import math
import random
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

INK = (232, 236, 242)        # near-white text
MUTE = (168, 178, 192)       # grey deck text
RED = (225, 18, 8)           # accent red
YEL = (255, 196, 0)          # accent yellow
BG = (10, 13, 18)            # poster black
RULE = (42, 47, 56)          # hairline grey

FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(draw, box, top, bottom):
    """Vertical gradient fill of box (x0,y0,x1,y1) from top RGB to bottom RGB."""
    x0, y0, x1, y1 = box
    h = max(1, y1 - y0)
    for y in range(y0, y1):
        t = (y - y0) / h
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(x0, y), (x1, y)], fill=c)


def hline_alpha(layer, y, x0, x1, color, alpha, width=1):
    d = ImageDraw.Draw(layer)
    d.line([(x0, y), (x1, y)], fill=color + (alpha,), width=width)


def tracked(draw, xy, text, fnt, fill, tracking=2):
    """Draw text with extra letter spacing; returns width used."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += int(draw.textlength(ch, font=fnt)) + tracking
    return x


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def starburst(draw, cx, cy, spikes, r_out, r_in, fill):
    pts = []
    for i in range(spikes * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / spikes - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=fill)


def draw_hero():
    """Night sea scene, 1024x496: warship silhouette, explosion, sea drones."""
    rng = random.Random(7)
    hw, hh = 1024, 496
    img = Image.new("RGB", (hw, hh))
    d = ImageDraw.Draw(img)
    horizon = 250

    # Sky + sea gradients.
    vgrad(d, (0, 0, hw, horizon), (9, 18, 34), (27, 42, 68))
    vgrad(d, (0, horizon, hw, hh), (16, 36, 54), (8, 20, 32))

    # Stars.
    for _ in range(110):
        x, y = rng.randint(0, hw - 1), rng.randint(0, horizon - 40)
        r = rng.choice([1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(200 + rng.randint(0, 55),) * 3)

    # Moon + glow (upper right).
    mx, my = 882, 72
    glow = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r, a in ((120, 18), (80, 30), (55, 55)):
        gd.ellipse([mx - r, my - r, mx + r, my + r], fill=(210, 220, 235, a))
    img = Image.alpha_composite(img.convert("RGBA"), glow)
    d = ImageDraw.Draw(img)
    d.ellipse([mx - 32, my - 32, mx + 32, my + 32], fill=(233, 238, 245, 255))
    d.ellipse([mx - 22, my - 12, mx - 6, my + 4], fill=(205, 212, 224, 255))
    d.ellipse([mx + 4, my + 8, mx + 16, my + 20], fill=(205, 212, 224, 255))

    # Warship silhouette (hull + superstructure + mast + funnel), raised
    hull = (16, 22, 30)
    d.polygon([(260, 268), (700, 268), (668, 304), (296, 304)], fill=hull)
    d.polygon([(700, 268), (732, 272), (668, 304)], fill=hull)  # bow
    d.rectangle([372, 222, 500, 268], fill=(20, 27, 36))
    d.rectangle([528, 232, 620, 268], fill=(20, 27, 36))
    d.rectangle([640, 212, 664, 268], fill=(20, 27, 36))        # funnel
    d.rectangle([640, 212, 664, 222], fill=(160, 20, 12))       # funnel band
    d.line([(436, 222), (436, 168)], fill=(26, 33, 44), width=6)  # mast
    d.line([(404, 186), (470, 186)], fill=(26, 33, 44), width=4)
    d.line([(412, 202), (462, 202)], fill=(26, 33, 44), width=4)
    d.polygon([(436, 168), (462, 174), (436, 180)], fill=(200, 24, 10))  # ensign
    d.line([(260, 268), (732, 272)], fill=(96, 112, 134), width=2)  # deck rim light
    # Portholes.
    for x in range(320, 690, 34):
        d.ellipse([x, 280, x + 6, 286], fill=(255, 190, 90))

    # Explosion over the ship's stern: compact and irregular, not a sun.
    ex, ey = 610, 258
    glow2 = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
    g2 = ImageDraw.Draw(glow2)
    for r, a in ((80, 20), (58, 35), (38, 55)):
        g2.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(255, 122, 0, a))
    img = Image.alpha_composite(img, glow2)
    d = ImageDraw.Draw(img)
    pts = []
    for i in range(24):
        r = rng.uniform(34, 60) if i % 2 == 0 else rng.uniform(16, 28)
        a = math.pi * i / 12 - math.pi / 2
        pts.append((ex + r * math.cos(a), ey + r * math.sin(a)))
    d.polygon(pts, fill=(255, 122, 0, 255))
    starburst(d, ex, ey, 8, 38, 18, (255, 196, 0, 255))
    d.ellipse([ex - 15, ey - 15, ex + 15, ey + 15], fill=(255, 244, 214, 255))
    # Small secondary fire amidships.
    starburst(d, 400, 260, 7, 26, 12, (255, 150, 40, 255))
    d.ellipse([400 - 9, 260 - 9, 400 + 9, 260 + 9], fill=(255, 220, 150, 255))
    # Smoke puffs rising, small and dark.
    smoke = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
    sd = ImageDraw.Draw(smoke)
    for (sx, sy, sr) in ((592, 206, 18), (618, 184, 22), (644, 208, 15)):
        sd.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(52, 58, 70, 60))
    img = Image.alpha_composite(img, smoke)
    d = ImageDraw.Draw(img)
    # Sparks.
    for _ in range(30):
        a = rng.uniform(0, 2 * math.pi)
        r = rng.uniform(36, 95)
        x, y = ex + r * math.cos(a), ey + r * math.sin(a) * 0.7
        c = rng.choice([(255, 196, 0), (255, 122, 0), (255, 240, 200)])
        d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=c + (255,))
    # Orange fire glints on the water under the blast (scattered, short).
    for (gx, gy, gw) in ((566, 322, 34), (606, 336, 44), (580, 350, 26),
                         (628, 322, 22), (596, 362, 30)):
        d.line([(gx, gy), (gx + gw, gy)], fill=(255, 140, 40), width=2)

    # Wave strokes across the sea.
    for _ in range(34):
        y = rng.randint(horizon + 8, hh - 12)
        x0 = rng.randint(0, hw - 160)
        ln = rng.randint(30, 150)
        d.line([(x0, y), (x0 + ln, y)], fill=(120, 150, 185), width=1)

    # Bottom scrim so the overlaid headline stays readable.
    scrim = Image.new("RGBA", (hw, hh), (0, 0, 0, 0))
    sc = ImageDraw.Draw(scrim)
    for i in range(150):
        a = int(200 * (i / 149) ** 1.6)
        sc.line([(0, hh - 150 + i), (hw, hh - 150 + i)], fill=(5, 7, 10, a))
    img = Image.alpha_composite(img, scrim)
    d = ImageDraw.Draw(img)

    # Drones AFTER the scrim, in the visible strip below the deck line:
    # simple light-hulled speedboats (hull + cabin + wake + bow spray).
    def drone(bx, by, flip):
        # Draw facing right; mirror whole shape when flip is set.
        def mx(x):
            return 2 * bx - x if flip else x
        hull_c = (148, 168, 192)
        bow = bx + 150
        d.polygon([(mx(bx), by), (mx(bow), by + 4), (mx(bow - 12), by + 18),
                   (mx(bx + 10), by + 18)], fill=hull_c)
        cx0, cx1 = sorted((mx(bx + 52), mx(bx + 92)))
        d.rectangle([cx0, by - 14, cx1, by], fill=hull_c)
        d.ellipse([mx(bx + 68) - 3, by - 11, mx(bx + 68) + 3, by - 5],
                  fill=(255, 60, 40))
        # Wake trailing behind the stern.
        sx0 = bx if not flip else bow
        step = -1 if not flip else 1
        for k in range(3):
            x0 = sx0 + step * k * 20
            d.line([(x0, by + 10 + k * 5), (x0 + step * 58, by + 4 + k * 8)],
                   fill=(235, 242, 250), width=3)
        # Bow spray.
        spx = bow if not flip else bx
        sdir = 1 if not flip else -1
        for k in range(4):
            d.ellipse([spx + sdir * (8 + k * 9) - 2, by - 2 + k * 3 - 2,
                       spx + sdir * (8 + k * 9) + 2, by - 2 + k * 3 + 2],
                      fill=(235, 242, 250))

    drone(90, 452, False)
    drone(800, 458, True)

    return img.convert("RGB")


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([36, 30, 48, 74], fill=RED)
    d.text((62, 26), "THE WORLD TODAY", font=font(FONT_B, 46), fill=INK)
    d.text((36, 82), "MONDAY 23 NOVEMBER 2026  •  THE DAY IN ONE IMAGE",
           font=font(FONT_B, 20), fill=RED)
    d.line([(36, 112), (988, 112)], fill=RED, width=3)

    # ---- Hero -----------------------------------------------------------
    hero = draw_hero()
    img.paste(hero, (0, 122))
    d = ImageDraw.Draw(img)
    # Kicker chip + headline over the scrim at the hero's foot.
    chip = "UKRAINE SANK THE CORVETTE MERKURY OFF LIBYA"
    cw = int(d.textlength(chip, font=font(FONT_B, 20))) + 28
    d.rectangle([36, 440, 36 + cw, 470], fill=RED)
    d.text((50, 444), chip, font=font(FONT_B, 20), fill=(255, 255, 255))
    d.text((36, 480), "SEA DRONES SINK RUSSIAN WARSHIP", font=font(FONT_B, 50), fill=INK)
    d.text((36, 544), "Seven Ukrainian naval drones sank the corvette Merkury off Libya.",
           font=font(FONT_R, 22), fill=MUTE)
    # NOTE: hero occupies y 122..618; headline/deck sit on its bottom scrim.
    # ---- Story rows -----------------------------------------------------
    rows = [
        ("COP31  •  ANTALYA", "CLIMATE TALKS COLLAPSE",
         "No deal in Antalya — the first climate failure since 2009.", None),
        ("NVIDIA  •  MARKETS", "HUANG IS BACK AT NVIDIA",
         "Board reinstates its founder; shares jump 30%.", None),
        ("U.S. HOUSE  •  WASHINGTON", "DEMOCRATS TAKE THE HOUSE",
         "Largest majority since 1992.", "258"),
        ("IRAN  •  WASHINGTON", "U.S. HITS IRAN'S SHADOW BANKS",
         "New sanctions as Tehran's heaviest missile week in a year peaks.", None),
    ]
    y = 630
    for kicker, head, deck, big in rows:
        d.line([(36, y), (988, y)], fill=RULE, width=1)
        d.text((36, y + 8), kicker, font=font(FONT_B, 19), fill=RED)
        d.text((36, y + 30), head, font=font(FONT_B, 34), fill=INK)
        d.text((36, y + 68), deck, font=font(FONT_R, 20), fill=MUTE)
        if big:
            d.text((988 - d.textlength(big, font=font(FONT_B, 64)), y + 14),
                   big, font=font(FONT_B, 64), fill=RED)
        y += 92
    d.line([(36, y), (988, y)], fill=RULE, width=1)

    # ---- Footer ---------------------------------------------------------
    d.text((36, y + 8),
           "Sources: Reuters · AP · CNN · BBC — 23 November 2026 · Drawn illustration, not a photograph.",
           font=font(FONT_R, 15), fill=(120, 128, 140))

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
