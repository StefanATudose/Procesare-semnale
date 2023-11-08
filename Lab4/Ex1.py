import numpy as np
import matplotlib.pyplot as plt
import math
import time


def fsin(t):
    return np.sin(2*np.pi * t * 50)

dimensiuni_fft = [128, 256, 512, 1024, 2048, 4096, 8192]
valori_timp_dft_manual = []
valori_timp_fft_numpy = []

for n in dimensiuni_fft :
    axa_reale = np.linspace(0.0, 1.0, n)
    semnal_sinusioidal = fsin(axa_reale)
    fourier_matrix = [[math.e**(-2*np.pi*1j*k * m / n) for k in range(n)] for m in range (n)]
    fourier_np = np.array(fourier_matrix)
    start = time.time()
    dft = fourier_np.dot(semnal_sinusioidal)
    end = time.time()
    valori_timp_dft_manual.append(end-start)

    start = time.time()
    fft = np.fft.fft(semnal_sinusioidal)
    end= time.time()
    valori_timp_fft_numpy.append(end - start)



plt.yscale("log")
plt.plot(dimensiuni_fft, valori_timp_dft_manual, label = "dft manual")
plt.plot(dimensiuni_fft, valori_timp_fft_numpy, label = "fft numpy")
plt.legend()
plt.savefig('Ex1.png')

plt.show()