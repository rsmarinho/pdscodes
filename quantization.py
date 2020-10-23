# import dos modulos necessarios para rodar o script
import numpy as np
import matplotlib.pyplot as plt

# tamanho do sinal
size = 1.078

# tempo continuo
t = np.linspace(0, int(size), int(1e3))

f0 = 2.0 # frequencia do sinal
A = 1 # amplitude do sinal

Qb = 2 # bits de quantizacao
Lq = 2**Qb # niveis de quantizacao
Qs = 2*A/Lq # degrau de quantizacao

# funcao lambda para geracao do sinal que
# sera amostrado. Nesse caso uma funcao senoidal
# de frequencia f0 e amplitude A

signal = lambda t : A*np.sin(2*np.pi*f0*t)

# geracao dos sinais continuo, quantizado e de erro
signal_c = signal(t)

signal_q = np.floor(signal_c/Qs)*Qs+Qs/2 # mid-riser (even)
# signal_q = np.round(signal_c/Qs)*Qs # mid-tread (odd)
signal_e = signal_c - signal_q

# funcoes de visualizacao do sinal original, do
# sinal quantizado e do sinal de erro entre o sinal
# original e o sinal quantizado
fig = plt.figure ()
plt.plot(t, signal_c)
plt.plot(t, signal_q)
plt.plot(t, signal_e)
plt.title("Conversao de sinal Continuo para quantizado")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")

plt.show()
