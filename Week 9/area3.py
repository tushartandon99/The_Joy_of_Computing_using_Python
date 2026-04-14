from PIL import Image
import numpy as np
import random

img = np.array(Image.open('Week 9\\map.png'))

h, w, _ = img.shape

count_pun = 0
count_india = 0

for _ in range(10000):
    x = random.randint(0, h-1)
    y = random.randint(0, w-1)

    pixel = img[x][y]

    # Punjab (red)
    if pixel[0] > 150 and pixel[1] < 100 and pixel[2] < 100:
        count_pun += 1
        count_india += 1

    # India (black)
    elif pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
        count_india += 1

# avoid divide by zero
if count_india == 0:
    print("Error")
else:
    area_pun = (count_pun / count_india) * 3287263
    print("Punjab Area:", area_pun)