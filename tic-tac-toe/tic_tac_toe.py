import computer_policy as computer
from utils import is_winner, display_board, input_location, input_play_num, input_play_label


class Tic_tac_toe:
    def __init__(self, board_size, player_num, policy=computer.move_random):
        """Initialize game parameters

        Args:
            board_size (int): width or height of the board
            player_num (int or None): 1 or 2 or None, if None, User will be asked to choose the number of players
            policy (function): a function that takes game_state and returns a move. Defaults to computer.move_random.
        """
        self.board_size = board_size
        self.game_state_initial = [' ' for _ in range(self.board_size**2)]
        self.player_num = player_num
        assert player_num in [
            1, 2, None, 0, False], "player_num has to be either 1, 2, or None (0)"
        self.computer_policy = policy

    def play(self):
        display_board(self.game_state_initial)
        play_again = True
        while play_again:
            game_state = list(self.game_state_initial)
            player = input_play_num() if not self.player_num else self.player_num
            if player == 2:
                self.two_player_game(game_state)
                play_again = False if (input(
                    "Please enter 'exit' to quit, or any other keys to start a new game: ")) == 'exit' else True
            if player == 1:
                self.one_player_game(
                    game_state, computer_policy=self.computer_policy)
                play_again = False if (input(
                    "Please enter 'exit' to quit, or any other keys to start a new game: ")) == 'exit' else True

    @staticmethod
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

    @staticmethod
    def one_player_game(game_state, computer_policy=computer.move_random):
        display_board(game_state)
        label_player = input_play_label()
        label_computer = 'O' if label_player == 'X' else 'X'
        while True:
            if label_player == 'X':
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
            else:
                computer_location = computer_policy(
                    game_state, computer_label='X')
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


if __name__ == '__main__':
    Tic_tac_toe(board_size=4, player_num=0,
                policy=computer.move_evolutionary).play()
