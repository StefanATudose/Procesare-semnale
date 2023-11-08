import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
import sounddevice

rate = int(10e5)
# scipy.io.wavfile.write('nume.wav', rate, signal)
#
# rate, x = scipy.io.wavfile.read(’nume.wav’)
#
# sounddevice.play(myarray, fs)


#ex 1
def fsin(t):
    return 4 * np.sin(np.pi * 2 * 100 * t + np.pi/2)

def fcos(t):
    return 4 * np.cos(np.pi * 2 * 100 * t)

axa_reale = np.linspace(0.0, 3.0, int(3/0.00005)+1)

semnal_sin = list(map(fsin, axa_reale))
semnal_cos = list(map(fsin, axa_reale))

# print(semnal_sin)
# print(semnal_cos)

# fig, axs = plt.subplots(2)
# fig.suptitle("Exercitiul 1")
# axs[0].plot(axa_reale[:1000], semnal_sin[:1000])
# axs[1].plot(axa_reale[:1000], semnal_cos[:1000])
# plt.show()

#ex 2
def fsin1(t):
    return np.sin(np.pi * 2 * 100 * t)

def fsin2(t):
    return np.sin(np.pi * 2 * 100 * t + np.pi/3)

def fsin3(t):
    return np.sin(np.pi * 2 * 100 * t + np.pi/2)

def fsin4(t):
    return np.sin(np.pi * 2 * 100 * t + np.pi)

semnal_sin1 = list(map(fsin1, axa_reale))
semnal_sin2 = list(map(fsin2, axa_reale))
semnal_sin3 = list(map(fsin3, axa_reale))
semnal_sin4 = list(map(fsin4, axa_reale))


# fig, axs = plt.subplots(4)
# fig.suptitle("Exercitiul 2")
# axs[0].plot(axa_reale[:1000], semnal_sin1[:1000])
# axs[1].plot(axa_reale[:1000], semnal_sin2[:1000])
# axs[2].plot(axa_reale[:1000], semnal_sin3[:1000])
# axs[3].plot(axa_reale[:1000], semnal_sin4[:1000])
#
# plt.show()

# SNRs = [0.1, 1, 10, 100]
#
# for SNR in SNRs:
#     zgomot = np.random.normal(0, 1, len(axa_reale))
#     gamma = np.sqrt(np.linalg.norm(semnal_sin1)/(SNR * np.linalg.norm(zgomot)))
#     semnal_sin_zgomot1 = semnal_sin1 + gamma * zgomot
#
#     zgomot = np.random.normal(0, 1, len(axa_reale))
#     gamma = np.sqrt(np.linalg.norm(semnal_sin2) / (SNR * np.linalg.norm(zgomot)))
#     semnal_sin_zgomot2 = semnal_sin2 + gamma * zgomot
#
#     zgomot = np.random.normal(0, 1, len(axa_reale))
#     gamma = np.sqrt(np.linalg.norm(semnal_sin3) / (SNR * np.linalg.norm(zgomot)))
#     semnal_sin_zgomot3 = semnal_sin3 + gamma * zgomot
#
#     zgomot = np.random.normal(0, 1, len(axa_reale))
#     gamma = np.sqrt(np.linalg.norm(semnal_sin4) / (SNR * np.linalg.norm(zgomot)))
#     semnal_sin_zgomot4 = semnal_sin4 + gamma * zgomot
#
#     fig, axs = plt.subplots(4)
#     fig.suptitle("Exercitiul 2 cu SNR = " + str(SNR))
#     axs[0].plot(axa_reale[:1000], semnal_sin_zgomot1[:1000])
#     axs[1].plot(axa_reale[:1000], semnal_sin_zgomot2[:1000])
#     axs[2].plot(axa_reale[:1000], semnal_sin_zgomot3[:1000])
#     axs[3].plot(axa_reale[:1000], semnal_sin_zgomot4[:1000])
#     plt.show()


#Exercitiul 3
def f_a(t):
    return np.sin(800*np.pi*t)


frecventa_esantionare = 48000
perioada_esantionare = 1/frecventa_esantionare

esantion = np.linspace(0.0, 1.0, int(1/perioada_esantionare)+1)
esantion_f_a = list(map(f_a, esantion))


#2 b
def f_b(t):
    return np.sin(1600*np.pi*t)

axa_reale = np.linspace(0.0, 3.0, 48000)

semnal_b = list(map(f_b, axa_reale))


#2 c

def f_c(t):
    return 2*np.mod(240 * t, 1)


semnal_c = list(map(f_c, axa_reale))
plt.stem(axa_reale[:1000], semnal_c[:1000])
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Semnal de tip sawtooth de frecventa 240 Hz')
plt.grid()
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

semnal_d = list(map(f_d, axa_reale))

sounddevice.wait()
sounddevice.play(esantion_f_a, 48000)
sounddevice.wait()
#
# sounddevice.play(semnal_b, 48000)
sounddevice.wait()
sounddevice.play(semnal_c, 48000)
sounddevice.wait()
# sounddevice.play(semnal_d, 48000)