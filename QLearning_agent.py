import numpy as np
import random
class QLearningAgent:
    #lr 0.7 df 0.618
    def __init__(self,n_state,n_action,learning_rate = 0.7,discount_factor=0.618):
        self.learning_rate = learning_rate  #Learning rate 0 < alpha <= 1 0.9 means that learning can occur quickly, 0 means that the q-values are never update
        self.discount_factor = discount_factor    #Gamma 0.618
        self.__qtable = qtable = np.zeros((n_state, n_action))
        self.n_action = n_action
        self.epsilon = 1.0
    
    """
        Getter 
    """
    def getDiscoutFactor(self):
        return self.discount_factor
    
    def getEpsilon(self):
        return self.epsilon

    def getQTable(self):
        return self.__qtable

    def getLearningRate(self):
        return self.learning_rate

    """
    #taking the biggest Q value for this state
    def getAction(self,state):
        return np.argmax(self.__qtable[state,:])   
    """
    
    #taking the biggest Q value for this state
    def getAction(self,state):
        action = np.random.choice(np.arange(self.n_action))
        if random.uniform(0, 1) > self.epsilon:
            action = np.argmax(self.__qtable[state,:])   
        return action


    def  __getValueQTable(self,state,action):
        return self.__qtable[state,action] 

    """
        Setter
    """
    def setDiscountFactor(self,value):
        self.discount_factor = value
    
    def setLearningRate(self,value):
        self.learning_rate = value

    def setEpsilon(self,value):
        self.epsilon = value


    """
        Learning Rule
    """
    def updateQTable(self,state,action,reward,new_state):
        old_value = self.__getValueQTable(state,action)
        next_max = np.max(self.__qtable[new_state,:])
        self.__qtable[state,action] = (1-self.learning_rate)*old_value + self.learning_rate * (reward + self.discount_factor*next_max)

    
    """
        Save and load Qtable
    """
    def saveQTable(self):
        np.savetxt('qtable.csv',self.__qtable)
    
    def loadQTable(self):
        try:
            self.__qtable = np.loadtxt('qtable.csv')
        except IOError:
            return None
