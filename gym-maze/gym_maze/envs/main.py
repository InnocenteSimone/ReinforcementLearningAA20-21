from gym_maze.envs.maze_env import MazeEnv
import gym
import random
env = gym.make("maze-v01")

env.render()
done = False
while not done:
    print("Choose action:(0=UP, 1=DOWN, 2=LEFT, 3=RIGHT)")
    action = input()
    _,_,done,_ = env.step(int(action))
    env.render()