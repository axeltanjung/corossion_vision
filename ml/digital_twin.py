import numpy as np

class CorrosionTwin:
    def __init__(self, velocity, ci0):
        self.v = velocity
        self.ci = ci0

    def step(self, days=1, noise=0.01):
        eps = np.random.normal(0, noise)
        self.ci = max(self.ci + self.v*days + eps, 0)
        return self.ci

    def maintain(self, reduction=0.4):
        self.ci = max(self.ci - reduction, 0)
