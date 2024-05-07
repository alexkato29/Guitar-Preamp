class SignalChain():
    def __init__(self, chain):
        self.chain = chain
    

    def apply(self, wave):
        """
        Applies all effects to the sound and returns the resulting output
        """
        for effect in self.chain:
            wave = effect.apply(wave)
        return wave