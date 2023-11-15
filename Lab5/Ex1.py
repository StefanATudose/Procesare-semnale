import numpy as np
import matplotlib.pyplot as plt
import math

#a)
#"a fost maasurat din ora ın ora" => a fost luat cate un esantion o data pe ora
# => o data la 3600 de secunde => frecventa = 1/3600
Fs = 1/3600

#b)
#18288 esantioane, o data pe ora
#18288/24 = 762 zile
#762/365 = putin peste 2 ani



#c)
#daca semnalul a fost esantionat corect, atunci frecventa de esantionare este
#cel putin de doua ori mai mare decat frecventa maxima continuta in semnal,
#deci f < fs/2; f < 1/(3600/2); f < 1/7200
#daca semnalul a fost esantionat optim, atunci frecventa de esantionare are ca valoare minimul posibil
# este mai mare
#decat  de dublu ori frecventa semnalului maxim; asaadar f = 1/7200


#d)
x = np.genfromtxt('archive/Train.csv', delimiter = ',')
x = x[1::, 2]
N = 18288

#plt.plot(x)
#plt.show()

#e) scadem media pentru a elimina componenta continua
x = x - np.mean(x)
X = np.fft.fft(x)

X = abs(X/N)
X = X[:N//2]

f = Fs*np.linspace(0, N//2, N//2)/N

#plt.yscale('log')
plt.plot(f, X)
plt.show()