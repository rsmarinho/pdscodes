# import dos modulos necessarios para rodar o script
import numpy as np
import matplotlib.pyplot as plt

# tamanho do sinal
size = 1

f0 = 20 # frequencia do sinal
A = 1 # amplitude do sinal

# funcao lambda para geracao do sinal que
# sera amostrado. Nesse caso uma funcao senoidal
# de frequencia f0 e amplitude A
signal = lambda t : A*np.sin(2*np.pi*f0*t)

s_rate = [10, 20, 40]
for i, N in enumerate(s_rate):
    n = np.linspace(0, int(size), N)

    plt.subplot(2, len(s_rate), i+1)
    plt.plot(n, signal(n), 'r')
    plt.stem(n, signal(n))

    X = np.fft.fft(signal(n))
    f = np.fft.fftfreq(len(X), 1/N)

    plt.subplot(2, len(s_rate), len(s_rate)+i+1)
    plt.plot(f[:len(X)//2], np.abs(X)[:len(X)//2])
    plt.xlim([0,20])

plt.show()
