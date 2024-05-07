import numpy as np

class SignalChain():
    def __init__(self, chain, block_size, samplerate):
        self.chain = chain
        self.block_size = block_size
        self.samplerate = samplerate

        # Tape is the delay recordings. 2 seconds of recording 
        self.tape = np.zeros(shape=(self.samplerate * 2,1))
    

    def apply(self, wave):
        """
        Applies all effects to the sound and returns the resulting output
        """
        # Add the wave block to the tape here
        # This artificial tape takes a long time, maybe there are better methods
        self.tape = np.append(self.tape, wave, axis=0)
        self.tape = self.tape[self.block_size:]

        for effect in self.chain:
            wave = effect.apply(wave, tape=self.tape)  # Not all pedals use the tape, but sent anyway. 
    
        return wave