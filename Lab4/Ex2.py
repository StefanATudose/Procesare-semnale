import numpy as np
import matplotlib.pyplot as plt
import math


def fsin(t):
    return np.sin(np.pi * 2 * 10 * t)

#aleg frecventa 15, care e mai mica decat 2 * fs = 2 * 10 = 20

def fsin1(t):
    return np.sin(np.pi * 2 * 40 * t)

def fsin2(t):
    return np.sin(np.pi * 2 * 55 * t)


esantioane = np.linspace(0, 1, 16)
axa_reale = np.linspace(0, 1, 10000)


semnal_initial_esantionat = fsin(esantioane)
semnal_comparativ_1_esantionat = fsin1(esantioane)
semnal_comparativ_2_esantionat = fsin2(esantioane)

fig, axs = plt.subplots(3)
fig.suptitle("Aliere stem")
axs[0].stem(esantioane, semnal_initial_esantionat)
axs[1].stem(esantioane, semnal_comparativ_1_esantionat)
axs[2].stem(esantioane, semnal_comparativ_2_esantionat)

plt.savefig('Ex2A.png')
plt.show()

semnal_initial = fsin(axa_reale)
semnal_comparativ_1 = fsin1(axa_reale)
semnal_comparativ_2 = fsin2(axa_reale)


fig, axs = plt.subplots(3)
fig.suptitle("Aliere plot")
axs[0].plot(axa_reale, semnal_initial)
axs[1].plot(axa_reale, semnal_comparativ_1)
axs[2].plot(axa_reale, semnal_comparativ_2)
plt.savefig('Ex2B.png')

plt.show()


