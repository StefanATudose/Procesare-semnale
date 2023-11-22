import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

poze_document = []
document = PdfPages("doc1.pdf")

x = np.random.random(100)
indici = np.arange(1, 101)

fig, axs = plt.subplots(4)

axs[0].plot(indici, x)

for i in range(3):
    x = np.convolve(x, x, mode='same')
    axs[i+1].plot(indici, x)

document.savefig(fig)
plt.show()

document.close()