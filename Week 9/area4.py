from PIL import Image
import random

im = Image.open('Week 9\\map.png')
rgb_im = im.convert("RGB")

count_in = 0
count_pun = 0
count = 0

while(count <= 100000):
    x = random.randint(0, 2480)
    y = random.randint(0, 2735)

    r, g, b = rgb_im.getpixel((x, y))

    # India (black region)
    if(r < 50 and g < 50 and b < 50):
        count_in += 1
        count += 1

    # Punjab (red region)
    elif(r > 150 and g < 100 and b < 100):
        count_pun += 1

area_pun = (count_pun / count_in) * 3287263
print(area_pun)