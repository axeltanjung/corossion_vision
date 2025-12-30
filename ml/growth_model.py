import numpy as np
from sklearn.linear_model import LinearRegression

class GrowthModel:
    def fit(self, ts, ci):
        self.reg = LinearRegression().fit(ts.reshape(-1,1), ci)

    def velocity(self):
        return self.reg.coef_[0]

    def predict(self, t):
        return self.reg.predict(t.reshape(-1,1))
