import numpy as np
class QLearningAgent:
    
    def __init__(self,n_state,n_action):
        self.learning_rate = 0.7  #Learning rate 0 < alpha <= 1
        self.discount_factor = 0.618    #Gamma
        self.__epsilon = 0.1
        self.__qtable = qtable = np.zeros((n_state, n_action))
    

    def setDiscountFactor(self,value):
        self.discount_factor = value

    def getDiscoutFactor(self):
        return self.discount_factor
    
    def getEpsilon(self):
        return self.__epsilon

    def setEpsilon(self,value):
        self.__epsilon = value

    def  __getValueQTable(self,state,action):
        return self.__qtable[state,action]

    def getQTable(self):
        return self.__qtable
    
    def getBestAction(self,state):
        return np.argmax(self.__qtable[state,:])

    def updateQTable(self,state,action,reward,new_state):
        old_value = self.__getValueQTable(state,action)
        next_max = np.max(self.__qtable[new_state,:])
        self.__qtable[state,action] = (1-self.learning_rate)*old_value + self.learning_rate * (reward + self.discount_factor*next_max)