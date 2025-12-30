import numpy as np

class EnvCorrosionTwin:
    def __init__(self, ci0, v):
        self.ci = ci0
        self.v = v

    def step(self, H, T, S, u=0, dt=1):
        accel = 1 + 0.02*H + 0.03*(T-25) + 0.5*S
        noise = np.random.normal(0,0.01)
        self.ci = max(self.ci + self.v*accel*dt + noise - u, 0)
        return self.ci
