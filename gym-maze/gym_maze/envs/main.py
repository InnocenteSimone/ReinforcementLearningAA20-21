from gym_maze.envs.maze_env import MazeEnv
import gym
import random
env = gym.make("maze-v01")

for i in range(2):
    env.render()
    action = random.randint(0,3)
    print(action)
    env.step(action)
    print("")