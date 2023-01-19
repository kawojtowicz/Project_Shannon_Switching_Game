from classes import GameRun


def main():
    msg = "\nThis is Shannon Switching Gale\n"
    print(msg)
    game_mode = ''
    while game_mode not in  ['1', '2', '3']:
        msg = 'Please, choose game mode:\n'
        msg += '1  -  human opponent\n2  -  easy computer opponent\n3  -  hard computer opponent\n'
        game_mode = input(msg)
    board_size = ''
    while board_size not in [5, 7, 9]:
        board_size = int(input("Please, choose board size.\n5  -  small\n7  -  medium\n9  -  big\n"))
    if game_mode == '1':
        name1 = ''
        name2 = ''
        while not name1:
            name1 = input("Player 1:\nPlease, enter your name.\n")
        while not name2:
            name2 = input("Player 2:\nPlease, enter your name.\n")
            if name2 == name1:
                input("Player 2:\nYour name cannot be the same as your opponent's.\nChoose another name.")
        game_mode = "Human"
        game_run = GameRun(game_mode, board_size, name1, name2)
    else:
        name1 = input('Please, enter your name.\n')
        game_run = GameRun(game_mode, board_size, name1, 'Computer')
    print(str(game_run._game._board))
    game = game_run.run_game()
    return game


if __name__ == '__main__':
    winner = main()
    if not winner:
        print('Game ended in a draw.')
    else:
        print(f'{winner} won. Congratulations!')
