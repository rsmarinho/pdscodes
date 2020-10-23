import numpy as np
import matplotlib.pyplot as plt

lim = 1
N = int(100)
t = np.linspace(-lim, lim, N+1)

d = lim/N
f = 2.0
print(d)

sig = lambda t : np.sinc(2*np.pi*f*t)

plt.stem(t, sig(t))

def impulse(t, n, delta = d) :
  ans = np.zeros(t.shape)
  ans[int( n / delta )] = 1.0
  return ans
  
def step(t, n, delta = d) :
  ans = np.zeros(t.shape)
  s = int( n / delta )
  ans[s:] = np.ones((len(t)-s))
  return ans

conv_size = 2*N+1
conv = np.zeros((conv_size))
aux = np.zeros(t.shape)

s = [*sig(t), *np.zeros(N+1)]

for k in range(0, 2*N+1) :
  aux = np.delete(np.insert(aux, 0, s[k]),-1)
  conv[k] = sum(step(t, 0) * aux)

plt.stem(conv)

conv_size = 2*N+1
conv = np.zeros((conv_size))
aux = np.zeros(t.shape)

# s = [*sig(t), *np.zeros(N+1)]
n = np.linspace(0, conv_size*d, conv_size)
s = step(n, 0)

for k in range(0, 2*N + 1) :
  aux = np.delete(np.insert(aux, 0, s[k]),-1)
  conv[k] = sum(sig(t) * aux)

plt.stem(n, conv)


