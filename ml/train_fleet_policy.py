from stable_baselines3 import PPO
from fleet_env import FleetEnv

env = FleetEnv(n_assets=10, daily_budget=3)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=400_000)
model.save("fleet_policy")
