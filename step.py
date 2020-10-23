import numpy as np
import matplotlib.pyplot as plt

lim = 10
N = int(10)
t = np.linspace(0, lim, N+1)

d = lim/N

def step(t, n, delta = d) :
  ans = np.zeros(t.shape)
  s = int( n / delta )
  ans[s:] = np.ones((len(t)-s))
  return ans

fig = plt.figure(figsize=(20,5))
plt.stem(t, step(t, 6))
plt.show()
