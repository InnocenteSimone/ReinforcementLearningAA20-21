import gym
from gym import error, spaces, utils
from gym.utils import seeding
from enum import Enum
import numpy as np
"""
Maze = [
    "|---------|",
    "|    E    |",
    "| www ww  |",
    "|w        |",
    "|w  w  w  |",
    "|w  wwwww |",
    "|w   S  w |",
    "|---------|",
]
"""
Maze = [
    "|---------|",
    "|         |",
    "|         |",
    "| E       |",
    "|         |",
    "|         |",
    "|    S    |",
    "|---------|",
]

dictionary = {}

"""
MAP1 = [
    "+---------+",
    "|        G|",
    "|         |",
    "|         |",
    "|wwwwwwww |",
    "|         |",
    "|   s     |",
    "+---------+",
]
"""


class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    """
        Popola il dictionary con la mappatura possibili posizioni -> integer
    """

    def __populateDict(self):
        count = -1
        for i,row in enumerate(Maze):
            for j,column in enumerate(row):
                if(column != "|" and column != "-" and column != "w"):
                    count+=1
                    dictionary[(i,j)] = count
    
    def getIndexValue(self,tupleVal):
        return dictionary.get(tupleVal)
    
    def __init__(self):
        #Colonna,riga
        self.agent_loc = (6,5)
        self.exit_loc = (3,2) #(3,1)
        self.invalid = ['|','-','w']

        self.action_space = spaces.Discrete(4)
        #self.observation_space = spaces.Box(low=0,high=4,shape=(5, 4),dtype=np.int16)
        self.observation_space = spaces.Discrete(54) #88 posizioni nel maze, di cui 34 non possibili 88-34=54 - 7 = 47
        self.maze = Maze.copy()
        self.__populateDict()

        

    def reset(self):
        self.__init__()
        return self.getIndexValue(self.agent_loc)

    def step(self, action):
        current_loc = self.agent_loc    #Old position
        if(action == Action.UP.value):
            self.agent_loc = (self.agent_loc[0]-1,self.agent_loc[1])
        elif (action == Action.DOWN.value):
            self.agent_loc = (self.agent_loc[0]+1,self.agent_loc[1])
        elif (action == Action.LEFT.value):
            self.agent_loc = (self.agent_loc[0],self.agent_loc[1]-1)
        elif (action == Action.RIGHT.value):
            self.agent_loc = (self.agent_loc[0],self.agent_loc[1]+1)
        
        reward = 0
        done = False
        info = []
        """
        if self.agent_loc in [(self.exit_loc[0]-1,self.exit_loc[1]),(self.exit_loc[0],self.exit_loc[1]-1),(self.exit_loc[0]+1,self.exit_loc[1]),(self.exit_loc[0],self.exit_loc[1]+1)]:
            reward = 0.2
        """

        if self.maze[self.agent_loc[0]][self.agent_loc[1]] in self.invalid:
            # if the move is invalid, return it back
            self.agent_loc = current_loc

        if self.maze[self.agent_loc[0]][self.agent_loc[1]] == 'E':
            reward = 1
            done = True

    
        


        self.moveAgent(current_loc,action)

       

        return self.getIndexValue(self.agent_loc), reward, done, info

    def moveAgent(self,oldLoc,action):
        if(oldLoc!=self.agent_loc):
            copy = self.maze[self.agent_loc[0]]
            stringList = list(copy)
            index = copy.find("S")
            if(action == Action.RIGHT.value):
                index += 1
                stringList[index-1] = ' '
                stringList[index] = "S"
                copy = ''.join(stringList)
                self.maze[self.agent_loc[0]] = copy
            
            if(action == Action.LEFT.value):
                index -= 1
                stringList[index+1] = ' '
                stringList[index] = "S"
                copy = ''.join(stringList)
                self.maze[self.agent_loc[0]] = copy
            
            
            copyArray = [self.maze[oldLoc[0]-1],self.maze[oldLoc[0]],self.maze[oldLoc[0]+1]]
            index = copyArray[1].find("S")
            stringListArray = []

            if (action == Action.UP.value):
                stringListArray.extend([list(copyArray[0]),list(copyArray[1])])
                stringListArray[0][index] = 'S'
                stringListArray[1][index] = ' '
                copyArray[0] = ''.join(stringListArray[0])
                copyArray[1] = ''.join(stringListArray[1])
                self.maze[self.agent_loc[0]] = copyArray[0]
                self.maze[self.agent_loc[0]+1] = copyArray[1]

            if (action == Action.DOWN.value):
                stringListArray.extend([list(copyArray[1]),list(copyArray[2])])
                stringListArray[0][index] = ' '
                stringListArray[1][index] = 'S'
                copyArray[1] = ''.join(stringListArray[0])
                copyArray[2] = ''.join(stringListArray[1])
                self.maze[self.agent_loc[0]] = copyArray[2]
                self.maze[self.agent_loc[0]-1] = copyArray[1]

    def render(self, mode='human'):
        for el in self.maze:
            for el1 in el:
                print(el1,end='')
            print("")
        print("")
    
    
    def close(self):
        pass