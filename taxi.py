from QLearning_agent import QLearningAgent

import gym
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import random

env = gym.make('Taxi-v3')

state_space_n = env.observation_space.n #500
action_space_n = env.action_space.n #6

print("Action Space {}".format(env.action_space))   # Discrete(6)
print("State Space {}".format(env.observation_space)) # Box(0,255,(210,160,3),uint80)

train_episodes = 10
test_episodes = 100
max_steps = 100
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

agent = QLearningAgent(state_space_n,action_space_n)


for episode in range(train_episodes):
    state = env.reset()
    step = 0
    done = False
    for step in range(max_steps): 
        exp_exp_tradeoff = random.uniform(0, 1)
        
        action = env.action_space.sample()
        if exp_exp_tradeoff > agent.getEpsilon():
            action = agent.getBestAction(state)

        new_state, reward, done, info = env.step(action)

        agent.updateQTable(state,action,reward,new_state)
        state = new_state
        if done == True:
            break

        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
        agent.setEpsilon(epsilon)

print(agent.getQTable())