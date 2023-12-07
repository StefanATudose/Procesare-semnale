import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

n = 1000
timp = np.linspace(0, 1, n+1)


def trend(t):
    return t * t  * 3 + t - 10

def sezon(t):
    return 2*np.mod(10 * t, 1)-1 + np.sin(20*np.pi*t)

zgomot = 0.5 * np.random.normal(0, 1, n+1)

trend_timp = trend(timp)
sezon_timp = sezon(timp)

serie_timp = trend_timp + sezon_timp + zgomot

fig, axs = plt.subplots(4)
fig.suptitle("Serie_timp")
axs[0].plot(timp, serie_timp)
axs[1].plot(timp, trend_timp)
axs[2].plot(timp, sezon_timp)
axs[3].plot(timp, zgomot)
plt.show()


#b
# am gasit un tutorial aici https://ipython-books.github.io/103-computing-the-autocorrelation-of-a-time-series/
autocorelare = np.correlate(serie_timp, serie_timp, mode = 'full')
plt.plot(autocorelare)
plt.show()

