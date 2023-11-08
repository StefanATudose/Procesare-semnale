import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.io.wavfile
import sounddevice



rate, x = scipy.io.wavfile.read('aeiouRecording.wav')

def segment_array(arr, percent_segment=1):
    n = len(arr)
    segment_size = int(n * percent_segment / 100)
    overlap = segment_size // 2
    start = 0
    segments = []

    while start + segment_size < n:
        end = start + segment_size
        segments.append(arr[start:end])
        start = start + segment_size - overlap

    return np.array(segments)


segments = segment_array(x)
spectogram = []

for segment in segments:
    fft_result = np.fft.fft(segment)
    magnitude = np.abs(fft_result)
    spectogram.append(magnitude)

spectrogram = np.array(spectogram)
spectrogram = spectrogram

plt.imshow(np.log1p(spectogram).T, cmap='viridis', aspect = "auto")
plt.colorbar()

plt.savefig('Ex6.png')

plt.show()
