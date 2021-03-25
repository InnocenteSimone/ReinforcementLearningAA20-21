from QLearning_agent import QLearningAgent
import gym
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import random
import matplotlib.pyplot as plt

env = gym.make('Taxi-v3')

state_space_n = env.observation_space.n #500 Numero degli stati possibili del gioco
action_space_n = env.action_space.n #6 #Numero di azioni possibili

train_episodes = 5000
max_steps = 99

max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

agent = QLearningAgent(state_space_n,action_space_n)

training_rewards = []
epsilons = []
listEpisode = []

for episode in range(train_episodes):
    #Reset dell'ambiente per ogni episodio/epoca
    state = env.reset()
    step = 0

    #Valore totale dei reward nell'episodio corrente
    total_training_rewards = 0
    done = False

    for step in range(max_steps): 

        #Viene utilizzata epsilon(all'interno di QLearning) per effettuare un trade-off tra Exploration e Exploitation        
        
        """
        action = env.action_space.sample()  #Exploration
        if random.uniform(0, 1) > agent.getEpsilon():
            action = agent.getAction(state) #Exploitation
        """
        action = agent.getAction(state)
        #Eseguo l'azione e osservo l'ambiente grazie alla libreria gym
        new_state, reward, done, info = env.step(action)
        #Aggiorno la QTable con la formula
        agent.updateQTable(state,action,reward,new_state)

        total_training_rewards+=reward

        state = new_state

        if done == True:
            break
    
    #Riduzione della epsilon
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    agent.setEpsilon(epsilon)
    
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)
    
    listEpisode.append(episode)

    print(f"Episode {episode} - Reward: {total_training_rewards})")


plt.plot(listEpisode,training_rewards)
plt.xlabel("Episode")
plt.ylabel("Rewards")
plt.show()

plt.plot(listEpisode,epsilons)
plt.show()
print ("Training score over time: " + str(sum(training_rewards)/train_episodes))

#agent.saveQTable()
#agent.loadQTable()

total_epochs, total_penalties = 0, 0
test_episodes = 100
env.reset()
listrewards = []
listEpisode = []

for episode in range(test_episodes):
    state = env.reset()
    epochs, penalties, reward = 0,0,0
    total_rewards = 0
    done = False
    print("******************************************************************")
    print("EPISODE ", episode)

    while not done:
        #env.render()
        action = agent.getAction(state)
        new_state,reward,done,info = env.step(action)

        if reward == -10:
            penalties += 1
        
        total_rewards += reward
        epochs+=1
    
        state = new_state

    total_penalties += penalties
    total_epochs += epochs
    
    listEpisode.append(episode)
    
    listrewards.append(total_rewards)
    #env.render()
    
    print("Score: ", total_rewards)

plt.plot(listEpisode,listrewards)
plt.xlabel("Episode")
plt.ylabel("Rewards")
plt.show()

env.close()

print(f"Results after {test_episodes} episodes:")
print("Mean score over time: " + str(sum(listrewards) / test_episodes))
print(f"Average timesteps per episode: {total_epochs / test_episodes}")
print(f"Average penalties per episode: {total_penalties / test_episodes}")
