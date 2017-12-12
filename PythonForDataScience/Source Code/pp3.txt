
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

rate, data = wav.read('bells.wav')

%matplotlib inline
plt.plot(data)
plt.show()
