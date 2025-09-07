from PIL import Image
import re

with open("output.txt", "r", encoding="utf-8") as f:
    raw_lines = [line.strip() for line in f if line.strip()]

lines = [re.findall(r"(Tsagaan|Har)", line) for line in raw_lines]

color_map = {
    "Har": (0, 0, 0),
    "Tsagaan": (255, 255, 255)
}

height = len(lines)
width = max(len(row) for row in lines)

img = Image.new("RGB", (width, height))

for y, row in enumerate(lines):
    for x, word in enumerate(row):
        img.putpixel((x, y), color_map.get(word))

img.save("output.png")
