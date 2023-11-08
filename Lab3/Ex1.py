import numpy as np
import matplotlib.pyplot as plt
import math

n = 8

fourier_matrix = [[math.e**(-2*np.pi*1j*k * m / n) for k in range(n)] for m in range (n)]

fourier_np = np.array(fourier_matrix)

print(np.linalg.norm(abs(np.matmul(fourier_np, np.conjugate(fourier_np.T))) - 8 * np.identity(n)))



def parte_reala(x):
    return x.real

def parte_imaginara(x):
    return x.imag


fig, axs = plt.subplots(n)
fig.suptitle("Exercitiul 1")

for i in range (n):
    axs[i].plot(list(range(n)), list(map(parte_imaginara, fourier_matrix[i])), 'g:')
    axs[i].plot(list(range(n)), list(map(parte_reala, fourier_matrix[i])))

plt.show()

#l-am terminat, 1 e bun