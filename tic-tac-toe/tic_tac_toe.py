import os
import shutil
from computer_play import move_random


def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


def clear(): return os.system('clear')


def display_board(state, clear_terminal=True):
    if clear_terminal:
        clear()
    print('===Tic-tac-toe===')
    for i in range(int(len(state)**0.5)):
        for j in range(int(len(state)**0.5)):
            print(state[i*int(len(state)**0.5)+j], end='')
            if j != int(len(state)**0.5)-1:
                print('|', end='')
            else:
                print()
                if i != int(len(state)**0.5)-1:
                    print('=:=:=')


def input_play_num():
    while True:
        player = input(
            "How many players? Press '1' for single player game, press '2' for double player game: ")
        if player in ['1', '2']:
            return int(player)
        else:
            print(
                'Please press number 1 or number 2 to indicate how many players there are.')


def input_location(game_state):
    empty_locations = [
        i+1 for i in range(len(game_state)) if game_state[i] == ' ']
    while True:
        location = input(
            f'The empty locations are {empty_locations} (right top cornor starts with 1), please choose your next move: ')
        if location in [str(_) for _ in empty_locations]:
            return int(location)
        else:
            print('Please choose your next move from the empty locations!')


def identity_list(a_list):
    if a_list:
        for _ in a_list:
            if a_list[0] != _:
                return False
        return True
    else:
        raise Exception('Empty list!')


def is_winner(game_state):
    same_line = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for index_list in same_line:
        if identity_list([game_state[i] for i in index_list]):
            if game_state[index_list[0]] != ' ':
                return game_state[index_list[0]]
    return None


def two_player_game(game_state):
    display_board(game_state)
    finished = False
    while not finished:
        for label in ['X', 'O']:
            print(f"Player {label}, it's your turn!")
            location = input_location(game_state)
            game_state[location-1] = label
            display_board(game_state)
            if is_winner(game_state):
                print(f'{is_winner(game_state)} wins!')
                finished = True
                break


def one_player_game(game_state):
    display_board(game_state)
    finished = False
    while not finished:
        label_player = 'X'
        label_computer = 'O'
        print(f"Player {label_player}, it's your turn!")
        location = input_location(game_state)
        game_state[location-1] = label_player
        display_board(game_state)
        if is_winner(game_state):
            print(f'{is_winner(game_state)} wins!')
            finished = True
        computer_location = move_random(game_state)
        game_state[computer_location-1] = label_computer
        display_board(game_state)
        if is_winner(game_state):
            print(f'{is_winner(game_state)} wins!')
            finished = True


def play(board_size=3):
    game_state = [' ' for _ in range(board_size*board_size)]
    display_board(game_state)
    play_again = True
    while play_again:
        player = input_play_num()
        if player == 2:
            two_player_game(game_state=[' ' for _ in range(
                board_size**2)])
            play_again = False if (input(
                "Please enter 'exit' to quit, or any other keys to continue playing: ")) == 'exit' else True
        if player == 1:
            one_player_game(game_state=[' ' for _ in range(
                board_size**2)])
            play_again = False if (input(
                "Please enter 'exit' to quit, or any other keys to continue playing: ")) == 'exit' else True


if __name__ == '__main__':
    play()
