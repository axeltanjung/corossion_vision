import gymnasium as gym
import numpy as np
from env_twin import EnvCorrosionTwin

class FleetEnv(gym.Env):
    def __init__(self, n_assets=10, daily_budget=3):
        self.n = n_assets
        self.daily_budget = daily_budget
        self.reset()

        self.action_space = gym.spaces.Discrete(self.n * 3)
        self.observation_space = gym.spaces.Box(0, 2, (self.n + 1,))

    def reset(self, seed=None):
        self.twins = [EnvCorrosionTwin(ci0=np.random.uniform(0.1,0.4), v=0.005) for _ in range(self.n)]
        self.budget = self.daily_budget
        return self._state(), {}

    def _state(self):
        return np.array([t.ci for t in self.twins] + [self.budget])

    def step(self, action):
        asset = action // 3
        level = action % 3
        u = [0, 0.2, 0.4][level]
        cost = [0, 1, 3][level]

        reward = 0

        if cost <= self.budget:
            self.twins[asset].ci = max(self.twins[asset].ci - u, 0)
            self.budget -= cost

        # natural degradation
        for t in self.twins:
            t.step(H=0.7, T=30, S=0.4)

        # risk penalty
        reward = -sum(t.ci for t in self.twins)

        done = self.budget <= 0
        return self._state(), reward, done, False, {}