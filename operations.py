# import dos modulos necessarios para rodar o script
import numpy as np
import matplotlib.pyplot as plt

# tamanho do sinal
lim = 1.0

# tempo continuo
t = np.linspace(-int(lim), int(lim), int(1e3)) 

f0 = 2.0 # frequencia do sinal
A = 1 # amplitude do sinal

# funcao lambda para geracao do sinal que 
# sera amostrado. Nesse caso uma funcao senoidal
# de frequencia f0 e amplitude A
signal = lambda t : A*np.sin(2*np.pi*f0*t)

# funcoes de visualizacao das operacoes executadas
# sobre o sinal
fig = plt.figure()

plt.plot(t, signal(t)) # sinal original
plt.plot(t, 2 * signal(t)) # sinal com ganho de 2.0
# plt.plot(t, signal(t-0.2)) # sinal atrasado em 0.2s
# plt.plot(t, signal(t+0.2)) # sinal adiantado em 0.2s
# plt.plot(t, signal(t)+signal(t-0.2)) # combinacao linear

plt.xlabel("Tempo")
plt.ylabel("Amplitude")

plt.show()
