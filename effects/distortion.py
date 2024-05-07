import time
import numpy as np
from helpers.utils import db_to_gain

class Distortion():
    def __init__(self, volume=-10, drive=10, normalize=True):
        self.volume = volume
        self.drive = drive
        # Normalize automatically adjusts the distortion so that, regardless of level, it is audibly the same volume
        self.normalize = normalize  

    def apply(self, wave, tape=None):
        distorted_wave = np.tanh(wave * db_to_gain(self.drive))

        # Normalizing makes the function take about x5 as long, maybe manual volume is better?
        # Main issue here is I think it takes so long to process that the output audio become glitchy
        if self.normalize:
            orig_rms = np.sqrt(np.mean(np.square(wave)))
            new_rms = np.sqrt(np.mean(np.square(distorted_wave)))
            distorted_wave = distorted_wave * (orig_rms / (new_rms + 1e-10))  # Add tiny value to avoid divide by 0
        
        # This is adds no time.
        else:
            distorted_wave *= db_to_gain(self.volume)

        return distorted_wave