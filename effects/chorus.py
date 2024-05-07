import numpy as np

class Chorus():
    def __init__(self, rate=1.5, depth=0.002, mix=0.5, samplerate=48000):
        self.rate = rate  # LFO rate in Hz
        self.depth = depth  # Max delay variation in seconds
        self.mix = mix  # Mix ratio between original and effected signal
        self.samplerate = samplerate
        self.phase = 0  # Initialize phase of LFO
        self.phase_increment = 2 * np.pi * self.rate / self.samplerate

    def apply(self, wave, tape):
        return wave