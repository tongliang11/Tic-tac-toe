def identity_list(a_list):
    if a_list:
        for _ in a_list:
            if a_list[0] != _:
                return False
        return True
    else:
        raise Exception('Empty list!')


def is_winner(game_state):
    # winning_blocks = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
    #              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    n = int(len(game_state)**0.5)
    winning_blocks = [[i for i in range(j,j+n)] for j in range(0,n*n,n)] + [[i for i in range(j,n*n,n)] for j in range(n)] + [[i for i in range(0,n*n,n+1)],[i for i in range(n-1,n*n-n+1,n-1)]]
    for indices in winning_blocks:
        if identity_list([game_state[i] for i in indices]):
            if game_state[indices[0]] != ' ':
                return game_state[indices[0]]
    if len([i for i in game_state if i == ' ']) == 0:  # tie
        return 'Tie'
    return None


def clear(): print("\033[H\033[J", end="")


def display_board(game_state, clear_terminal=True):
    if clear_terminal:
        clear()
    n = int(len(game_state)**0.5)
    print('='*(int(len(game_state)**0.5*1.5)-3)+'Tic-tac-toe'+'='*(int(len(game_state)**0.5*1.5)-3))
    for i in range(n):
        for j in range(n):
            if j==0:
                print(end=' ')
            if game_state[i*n+j] == ' ':
                print(i*n+j+1,end='')
            else:
                print(game_state[i*n+j], end='')
            if j != n-1:
                print(' | ', end='')
            else:
                print()
                if i != n-1:
                    print('---|'*(n-1)+'---')


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
            f'The empty locations are {empty_locations}, please choose your next move: ')
        if location in [str(_) for _ in empty_locations]:
            return int(location)
        else:
            print('Please choose your next move from the empty locations!')


def input_play_label():
    while True:
        player = input(
            "Which stone do you want to play with? 'X' goes first and 'O' goes second. ")
        if player in ['X', 'x']:
            return 'X'
        elif player in ['O',  'o', '0']:
            return 'O'
        else:
            print(
                "Please choose between 'X' and 'O' to be your tic-tac-toe stone, 'X' goes first.")


if __name__ == '__main__':
    display_board([' ']*9)