import numpy as np
from growth_model import GrowthModel
from survival_rul import RULModel

class RULEngine:
    def __init__(self, threshold=1.0):
        self.threshold = threshold

    def estimate(self, ts, ci):
        ts = np.array(ts)
        ci = np.array(ci)

        gm = GrowthModel()
        gm.fit(ts,ci)

        v = gm.velocity()
        current_ci = ci[-1]
        time_to_fail = (self.threshold - current_ci) / v

        return max(time_to_fail,0), v
