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
