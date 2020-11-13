import sys

from PIL import Image
import numpy as np

import matplotlib.pyplot as plt

img = np.array(Image.open(../barbara.png))
plt.imshow(img)
for j in range(0, img.shape[0]):
    for k in range(0, img.shape[1]):
        print(f'{img[j,k].astype(np.uint8): b}')

