import numpy as np
def move_random(game_state):
    empty_locations = [
        i+1 for i in range(len(game_state)) if game_state[i] == ' ']
    return np.random.choice(empty_locations)