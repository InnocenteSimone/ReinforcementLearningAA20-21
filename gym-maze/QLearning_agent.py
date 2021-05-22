import numpy as np
import random


class QLearningAgent:
    #lr 0.7 df 0.618
    def __init__(self,n_state,n_action,learning_rate = 0.7,discount_factor=0.618):
        self.learning_rate = learning_rate  #Learning rate 0 < alpha <= 1 0.9 means that learning can occur quickly, 0 means that the q-values are never update
        self.discount_factor = discount_factor    #Gamma 0.618
        self.n_action = n_action
        self.qtable = np.zeros((n_state, n_action))    
        self.epsilon = 1.0
    

     
    def getTestAction(self,state):
        return np.argmax(self.qtable[state,:])
        
    #taking the biggest Q value for this state
    def getAction(self,state):
        action = np.random.choice(np.arange(self.n_action))
        if random.uniform(0, 1) > self.epsilon:
            action = np.argmax(self.qtable[state,:])
        return action


    def  __getValueQTable(self,state,action):
        return self.qtable[state,action] 

    """
        Learning Rule
    """
    def updateQTable(self,state,action,reward,new_state):
        old_value = self.__getValueQTable(state,action)
        next_max = np.max(self.qtable[new_state,:])
        self.qtable[state,action] = (1-self.learning_rate)*old_value + self.learning_rate * (reward + self.discount_factor*next_max)
    
    """
        Savvalnd load Qtable
    """
    def saveQTable(self,env):
        np.savetxt(f"qtable{env}.csv",self.qtable)
    
    def loadQTable(self,filepath):
        print("LOADING")
        filepath = 'qtableMaze.csv'
        try:
            self.qtable = np.loadtxt(filepath)
        except IOError:
            print("error")
            return None
