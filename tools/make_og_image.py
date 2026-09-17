# -*- coding: utf-8 -*-
"""Pregeneruje og-image.png (1200x630) v styl stranky lipnicanmilos.github.io."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG      = (13, 17, 23)
BLUE    = (47, 129, 247)
GREEN   = (63, 185, 80)
WHITE   = (230, 237, 243)
DIM     = (139, 148, 158)

BOLD = "C:/Windows/Fonts/segoeuib.ttf"
REG  = "C:/Windows/Fonts/segoeui.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def width(d, txt, font):
    return d.textbbox((0, 0), txt, font=font)[2]

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

# horny modry pruh
d.rectangle([0, 0, W, 7], fill=BLUE)

LEFT = 90

# eyebrow
d.text((LEFT, 158), "PORTFOLIO  ·  BRATISLAVA, SLOVAKIA", font=f(REG, 27), fill=DIM)

# meno
d.text((LEFT, 228), "Ing. Miloš Lipničan", font=f(BOLD, 66), fill=WHITE)

# titul — zmensi, kym sa nezmesti do sirky
title = "IT Application Support & Backend Developer"
size = 44
while size > 26:
    ft = f(BOLD, size)
    if width(d, title, ft) <= W - LEFT - 70:
        break
    size -= 1
d.text((LEFT, 326), title, font=ft, fill=BLUE)

# zelena linka
rule_y = 404
d.rectangle([LEFT, rule_y, LEFT + 142, rule_y + 5], fill=GREEN)

# stack
d.text((LEFT, 442), "Python · FastAPI · Oracle · PostgreSQL · Docker · Cloud · AI",
       font=f(REG, 28), fill=DIM)

# url
d.text((LEFT, 558), "lipnicanmilos.github.io", font=f(BOLD, 28), fill=BLUE)

# ML badge vpravo hore
bx0, by0, bx1, by1 = 980, 90, 1110, 220
d.rounded_rectangle([bx0, by0, bx1, by1], radius=22, outline=BLUE, width=3)
bf = f(BOLD, 52)
bb = d.textbbox((0, 0), "ML", font=bf)
d.text((bx0 + (bx1 - bx0 - bb[2]) / 2, by0 + (by1 - by0 - bb[3]) / 2 - 6), "ML", font=bf, fill=WHITE)

out = "C:/Users/mlipnican/lipnicanmilos.github.io/og-image.png"
im.save(out, optimize=True)
print("saved", out, im.size, "title size", size)
