import numpy as np
import matplotlib.pyplot as plt
import math



def fsin(t):
    return np.sin(np.pi * 2 * 7 * t)


def infasurare_fct(A, t, w):
    return A * math.e**(-2j * np.pi * t * w)

axa_reale = np.linspace(0.0, 1.0, 10000)


semnal = fsin(axa_reale)
w = np.sqrt(x**2 + y**2)
for w in [1, 4, 7, 10]:
    infasurare = np.array(infasurare_fct(semnal, axa_reale, w))
    plt.scatter(infasurare.real, infasurare.imag, c=w)
    plt.show()