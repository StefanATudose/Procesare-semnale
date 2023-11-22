import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

poze_document = []
document = PdfPages("doc2.pdf")

n = 3

x = np.random.randint(1, 51, n)
y = np.random.randint(1, 51, n)

conv_automat = np.convolve(x, y)

conv_de_mana= np.zeros(n*2 -1)

for i in range (n):
    for j in range (n):
        conv_de_mana[i+j] += x[i] * y[j]


dimensiune_conv = len(x) + len(y) - 1
x_padded = np.pad(x, (0, dimensiune_conv - len(x)), mode='constant')
y_padded = np.pad(y, (0, dimensiune_conv - len(y)), mode='constant')

x_fft = np.fft.fft(x_padded)
y_fft = np.fft.fft(y_padded)

produs_frecvente = np.multiply(x_fft, y_fft)

conv_prin_fft = np.real(np.fft.ifft(produs_frecvente))

print(f"Convolutia din np: {conv_automat}")

print(f"Convolutia prin inmultire de polinoame{conv_de_mana}")

print(f"Convolutia prin fft si inmultire element-wise, apoi ifft {conv_prin_fft}")



