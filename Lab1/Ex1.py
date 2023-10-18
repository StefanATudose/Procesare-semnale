import numpy as np
import matplotlib.pyplot as plt

start = 0.0
stop = 0.03
pas = 0.0005

def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)


def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)


def z(t):
    return np.cos(120 * np.pi * t + np.pi/3)


#3 a
def gen_axa_reala(start_timp, stop_timp, pas):
    return np.linspace(start_timp, stop_timp, int((stop_timp-start_timp)/pas+1))


axa_reala = gen_axa_reala(start, stop, pas)

semn_x = list(map(x, axa_reala))
semn_y = list(map(y, axa_reala))
semn_z = list(map(z, axa_reala))



#3 b
fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 1b")
axs[0].plot(axa_reala, semn_x)
axs[1].plot(axa_reala, semn_y)
axs[2].plot(axa_reala, semn_z)
plt.show()

#3 c
#fs = 200, fs = 1/T
perioada_esantionare = 1/200

esantion = np.linspace(start, stop, int((stop-start)/perioada_esantionare+1))


esantion_x = list(map(x, esantion))
esantion_y = list(map(y, esantion))
esantion_z = list(map(z, esantion))


print(esantion_x)
print(esantion_y)

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 1c")
axs[0].stem(esantion, esantion_x)
axs[1].stem(esantion, esantion_y)
axs[2].stem(esantion, esantion_z)
plt.show()