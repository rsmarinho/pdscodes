from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt

img = image.imread('/content/barbara.png')#.astype(float)

print(img.dtype)
print(img.shape)
print(type(img))

plt.imshow(img, cmap=plt.get_cmap('gray'))

img_int = (img*255.0).astype(np.uint8)
img_int.dtype
out = np.zeros((512,512))

mask = np.array([1,1,0,0,0,0,0,0], dtype=np.uint8)
for i in range(0,512):
  for j in range(0,512):
    out[i,j] = np.packbits(np.unpackbits(img_int[i,j])*mask)

fig = plt.figure()#figsize=(15,15))
plt.imshow(out, cmap=plt.get_cmap('gray'))
