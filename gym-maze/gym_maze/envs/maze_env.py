import gym
from gym import error, spaces, utils
from gym.utils import seeding
from enum import Enum
import numpy as np
Maze = [
    "|----------|",
    "|    E     |",
    "|          |",
    "|          |",
    "|          |",
    "|    S     |",
    "|----------|",
]

class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        print("init")
        #Colonna,riga
        self.agent_loc = (5,5)
        self.exit_loc = (1,5)
        self.invalid = ['|','-']

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0,high=4,shape=(5, 4),dtype=np.int16)
        self.maze = Maze

    def reset(self):
        self.__init__()

    def step(self, action):
        current_loc = self.agent_loc
        if(action == Action.UP.value):
            self.agent_loc = (self.agent_loc[0]+1,self.agent_loc[1])
        elif (action == Action.DOWN.value):
            self.agent_loc = (self.agent_loc[0]-1,self.agent_loc[1])
        elif (action == Action.LEFT.value):
            self.agent_loc = (self.agent_loc[0],self.agent_loc[1]-1)
        elif (action == Action.RIGHT.value):
            self.agent_loc = (self.agent_loc[0],self.agent_loc[1]+1)


        reward = 0
        done = False
        info = []

        if self.maze[self.agent_loc[0]][self.agent_loc[1]] in self.invalid:
            # if the move is invalid, return it back
            self.agent_loc = current_loc

        if self.maze[self.agent_loc[0]][self.agent_loc[1]] == 'E':
            reward = 1  
            done = True

        
        moveAgent(current_loc,self.agent_loc)

        return self.agent_loc, reward, done, info

    def moveAgent(currentPos,newPos):
        if(currentPos!=newPos):
            pass
            #self.maze[currentPos()[0]][currentPos()]

    def render(self, mode='human'):
        for el in self.maze:
            for el1 in el:
                print(el1,end='')
            print("")
    def close(self):
        pass