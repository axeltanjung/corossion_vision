import numpy as np
from lifelines import WeibullFitter

class RULModel:
    def __init__(self):
        self.wbf = WeibullFitter()

    def fit(self, times_to_fail):
        self.wbf.fit(times_to_fail, event_observed=np.ones(len(times_to_fail)))

    def survival(self, t):
        return float(self.wbf.survival_function_at_times(t))

    def hazard(self, t):
        return float(self.wbf.hazard_at_times(t))
