import gym

env = gym.make('SpaceInvaders-v0')

"""
Ogni ambiente fornisce un action_space e un observation_space, questi attributi sono di tipo Space
e descrivono il formato delle azioni e delle osservazioni valide
"""

#print(env.action_space)         # Discrete(6)
#print(env.observation_space)    # Box(0,255,(210,160,3),uint80)

"""
Lo spazio discreto fornisce dei numeri non negativi che andranno a rappresentare le azioni disponibili.
In questo caso esistono azioni da 0 a 5
Il Box rappresenta un box n-dimensionale
"""
"""
The v0 envinroment of Space Invaders returns an image as part of the state. 
We extract the shape of the image to pass to structure our neural network
In this environment, the observation is an RGB image of the screen, which is an array of shape (210, 160, 3) 
"""

#height,width,channels = env.observation_space.shape #210 160 3
#actions = env.action_space.n #6

print(env.unwrapped.get_action_meanings())  #['NOOP', 'FIRE', 'RIGHT', 'LEFT', 'RIGHTFIRE', 'LEFTFIRE']

episodes = 5    #Numero di giocate
for episode in range(1,episodes+1):
    state = env.reset()     #Reset dell'ambiente
    done = False
    score = 0
    
    while not done:
        env.render()
        action = env.action_space.sample()
        n_state,reward,done,info = env.step(action)
        score+=reward
    print("Episode:{} Score:{}".format(episode,score))
env.close()
