import numpy as np
import matplotlib.pyplot as plt

lim = 10
N = int(10)
t = np.linspace(0, lim, N+1)

d = lim/N

def impulse(t, n, delta = d) :
  ans = np.zeros(t.shape)
  ans[int( n / delta )] = 1.0
  return ans

fig = plt.figure(figsize=(20,5))
plt.stem(t, impulse(t, 3))
plt.show()
