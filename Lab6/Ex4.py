import numpy as np
import matplotlib.pyplot as plt

#a
date = np.genfromtxt('archive/Train.csv', delimiter = ',')
date = date[1::, 2]

y = np.random.randint(0, 18000)
x = date[y:y+72]            #incepand cu un mom random, 73 de ore
print(len(x))
ore = np.arange(72)


#b
plt.plot(ore, x, label = f"Semnal original")
for w in [5, 9, 13, 17]:
    filtru = np.convolve(x, np.ones(w), 'valid') / w
    plt.plot(ore[-len(filtru):], filtru, label = f"W={w}")

plt.legend()
plt.show()


#c

