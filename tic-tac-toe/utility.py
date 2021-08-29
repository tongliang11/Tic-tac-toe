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
    if len([i for i in game_state if i == ' ']) == 0:  # tie
        return 'Tie'
    return None


def clear(): print("\033[H\033[J", end="")


def display_board(state, clear_terminal=True):
    if clear_terminal:
        clear()
    print('==Tic-tac-toe==')
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
            f'The empty locations are {empty_locations} (top-left corner starts with location 1), please choose your next move: ')
        if location in [str(_) for _ in empty_locations]:
            return int(location)
        else:
            print('Please choose your next move from the empty locations!')
