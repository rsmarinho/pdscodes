import sys

from PIL import Image
import numpy as np

h = int(sys.argv[2])
w = int(sys.argv[3])

img = np.zeros((h*w), dtype=int)

with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        img[i] = int(line, 2)

img = img.reshape(h,w)
#for i in range(img.shape[0]):
#    print(img[0,i])

im = Image.fromarray(img.astype(np.uint8))
im.save('procImg.png')
