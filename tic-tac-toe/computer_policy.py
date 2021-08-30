import random
import time
from utils import is_winner


def move_random(game_state, computer_label='O', delay=0.5):
    empty_locations = [
        i for i in range(len(game_state)) if game_state[i] == ' ']
    time.sleep(delay)  # fake computer thinking delay
    return random.choice(empty_locations)+1


def move_evolutionary(game_state, computer_label='O', rounds=1000):
    empty_locations = [
        i for i in range(len(game_state)) if game_state[i] == ' ']
    if empty_locations.__len__() == 0:
        return -1
    elif empty_locations.__len__() == 1:
        return empty_locations[0] + 1
    else:
        winning_prob = []
        for next_move in empty_locations:
            _game_state = list(game_state)
            _game_state[next_move] = computer_label
            winner = []
            for i in range(rounds):
                winner.append(_random_self_play(list(_game_state)))

            winning_prob.append(
                len([_ for _ in winner if _ == computer_label])/rounds)

        return empty_locations[max(range(len(empty_locations)), key=lambda x:winning_prob[x])]+1


def _random_self_play(game_state, label_computer1='X'):
    label_computer2 = 'O' if label_computer1 == 'X' else 'X'
    while True:

        computer_location1 = move_random(game_state, delay=0)
        game_state[computer_location1-1] = label_computer1

        if is_winner(game_state):
            return is_winner(game_state)
        computer_location2 = move_random(game_state, delay=0)
        game_state[computer_location2-1] = label_computer2

        if is_winner(game_state):
            return is_winner(game_state)


def move_Q_table(game_state):
    pass


if __name__ == '__main__':
    print(move_evolutionary(['O', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']))
