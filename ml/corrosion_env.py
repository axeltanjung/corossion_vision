import gymnasium as gym
import numpy as np
from env_twin import EnvCorrosionTwin

class CorrosionEnv(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(0,2,(4,))
        self.reset()

    def reset(self,seed=None):
        self.H = np.random.uniform(0.4,0.9)
        self.T = np.random.uniform(20,40)
        self.S = np.random.uniform(0,1)
        self.twin = EnvCorrosionTwin(ci0=0.2, v=0.005)
        return np.array([self.twin.ci,self.H,self.T,self.S]), {}

    def step(self,action):
        u = [0,0.2,0.4][action]
        ci = self.twin.step(self.H,self.T,self.S,u)
        cost = [0,1,3][action]
        reward = -(ci + cost)
        done = ci >= 1.0
        return np.array([ci,self.H,self.T,self.S]), reward, done, False, {}
