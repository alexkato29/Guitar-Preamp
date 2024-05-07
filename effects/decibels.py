import numpy as np

class Decibels():
    def __init__(self):
        pass

    def apply(self, waveform, tape=None):
        avg_amplitude = np.mean(np.square(waveform))
        if avg_amplitude > 0: 
            dB = 20 * np.log10(avg_amplitude)
        else:
            dB = -np.inf 
        return waveform