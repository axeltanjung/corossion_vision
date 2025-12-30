from stable_baselines3 import PPO
from corrosion_env import CorrosionEnv

env = CorrosionEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=200_000)
model.save("policy_corrosion")
