import numpy as np
import matplotlib.pyplot as plt

#2 a

def f_a(t):
    return np.sin(800*np.pi*t)


frecventa_esantionare = 1600
perioada_esantionare = 1/frecventa_esantionare

esantion = np.linspace(0.0, 1.0, int(1/perioada_esantionare)+1)
esantion_f_a = list(map(f_a, esantion))

plt.stem(esantion[:100], esantion_f_a[:100])
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnal sinusoidal de frecventa 400 Hz')
plt.show()

#2 b
def f_b(t):
    return np.sin(1600*np.pi*t)

axa_reale = np.linspace(0.0, 3.0, int(3/0.00005)+1)

semnal_b = list(map(f_b, axa_reale))

plt.plot(axa_reale[:100], semnal_b[:100])
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnal sinusoidal de frecventa 800 Hz')
plt.show()


#2 c

def f_c(t):
    return 2*np.mod(240 * t, 1)-1


semnal_c = list(map(f_c, axa_reale))
#print(semnal_c)
plt.plot(axa_reale[:1000], semnal_c[:1000])
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnal de tip sawtooth de frecventa 240 Hz')
plt.show()

#2 d

def f_d(t):
    return np.sign(np.sin(600*np.pi*t))


semnal_d = list(map(f_d, axa_reale))

plt.plot(axa_reale[:500], semnal_d[:500])
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnal de tip square de frecventa 300 Hz')
plt.show()

#2 e
img_e = np.random.rand(128, 128)

plt.imshow(img_e)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Semnal 2D aleator')
plt.show()

#2 f
img_f = np.zeros((128, 128))

for i in range(128):
    for j in range(128):
        img_f[i][j] = i + j

plt.imshow(img_f)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Semnal 2D generat cu procedura custom')
plt.show()
