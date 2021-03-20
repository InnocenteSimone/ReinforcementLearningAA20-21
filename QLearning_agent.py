import numpy as np
class QLearningAgent:
    
    def __init__(self,n_state,n_action,learning_rate = 0.7,discount_factor=0.5):
        self.learning_rate = learning_rate  #Learning rate 0 < alpha <= 1
        self.discount_factor = discount_factor    #Gamma 0.618
        self.__epsilon = 0.1
        self.__qtable = qtable = np.zeros((n_state, n_action))
    

    """
        Getter 
    """
    def getDiscoutFactor(self):
        return self.discount_factor
    
    def getEpsilon(self):
        return self.__epsilon

    def getQTable(self):
        return self.__qtable

    def getAction(self,state):
        return np.argmax(self.__qtable[state,:])   

    def  __getValueQTable(self,state,action):
        return self.__qtable[state,action] 

    """
        Setter
    """
    def setDiscountFactor(self,value):
        self.discount_factor = value
    
    def setEpsilon(self,value):
        self.__epsilon = value


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
            self.__qtable = np.loadtxt('qtable2.csv')
        except IOError:
            return None

    
    def fit():
        pass