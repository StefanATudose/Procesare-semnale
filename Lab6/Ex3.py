import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def fsin(t):
    return np.sin(np.pi*100*t)

def drept(Nw):
    return np.pad(np.ones(Nw), (0, 10001-Nw), mode = "constant")

def hanning(Nw):
    return np.pad(0.5 * (1 - np.cos(2 * np.pi * np.arange(Nw) / Nw)), (0, 10001-Nw), mode = "constant")


axa_timp = np.linspace(0, 1, 10000+1)
semnal = fsin(axa_timp)

fereastra_dreapta = drept(200)
fereastra_hanning = hanning(200)


semnal_drept = np.multiply(fereastra_dreapta, semnal)
semnal_hanning = np.multiply(fereastra_hanning, semnal)

plt.figure()

plt.subplot(3, 1, 1)
plt.plot(axa_timp[:3000], semnal[:3000], label='Sinusoidală inițială')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(axa_timp[:3000], semnal_drept[:3000], label='Fereastră dreptunghiulară')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(axa_timp[:3000], semnal_hanning[:3000], label='Fereastră Hanning')
plt.legend()

document = PdfPages("doc3.pdf")
document.savefig()
document.close()

plt.show()