from gym.envs.registration import register

register(
    id='maze-v01',
    entry_point='gym_maze.envs:MazeEnv',
)