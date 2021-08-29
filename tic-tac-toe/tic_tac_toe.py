import computer_play
from utility import is_winner, display_board, input_location, input_play_num


def two_player_game(game_state):
    display_board(game_state)
    while True:
        for label in ['X', 'O']:
            print(f"Player {label}, it's your turn!")
            location = input_location(game_state)
            game_state[location-1] = label
            display_board(game_state)

            if is_winner(game_state) == 'Tie':
                print("It's a tie!")
                return
            elif is_winner(game_state) == 'X':
                print('X wins!')
                finished = True
                return
            elif is_winner(game_state) == 'O':
                print('O wins!')
                finished = True
                return


def one_player_game(game_state, computer_policy=computer_play.move_random):
    display_board(game_state)
    label_player = 'X'
    label_computer = 'O'
    while True:
        print(f"Player {label_player}, it's your turn!")
        location = input_location(game_state)
        game_state[location-1] = label_player
        display_board(game_state)
        if is_winner(game_state) == 'Tie':
            print("It's a tie!")
            return
        elif is_winner(game_state) == 'X':
            print('X wins!')
            return
        elif is_winner(game_state) == 'O':
            print('O wins!')
            return

        computer_location = computer_policy(game_state)
        game_state[computer_location-1] = label_computer
        display_board(game_state)
        if is_winner(game_state) == 'Tie':
            print("It's a tie!")
            return
        elif is_winner(game_state) == 'X':
            print('X wins!')
            return
        elif is_winner(game_state) == 'O':
            print('O wins!')
            return


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
                "Please enter 'exit' to quit, or any other keys to start a new game: ")) == 'exit' else True
        if player == 1:
            one_player_game(game_state=[' ' for _ in range(
                board_size**2)], computer_policy=computer_play.move_evolutionary)
            play_again = False if (input(
                "Please enter 'exit' to quit, or any other keys to start a new game: ")) == 'exit' else True


if __name__ == '__main__':
    play(3)
