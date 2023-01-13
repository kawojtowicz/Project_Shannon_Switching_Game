from classes import Field, Board, Game, GameRun
from classes import InvalidSizeError, EvenSizeError, InvalidFieldError
from classes import FieldIsTakenError
from Human_Player import HumanPlayer, InvalidLetterError, TooManySignsError
from Human_Player import InvalidNumberError
from Human_Player import SignNotStringError, MovingError, NameNotStringError


def main():
    msg = "This is Shannon Switching Gale\nPlease, choose game mode.\n"
    msg += 'Enter 1 to play with your friend.'
    game_mode = input(msg)
    board_size = int(input("Please, choose board size 5-25"))
    if game_mode == '1':
        name1 = input("Player 1:\nPlease, enter your name.")
        game_mode = "Human"
        class2 = 'Human'
        name2 = input("Player 2:\nPlease, enter your name.")
        game_run = GameRun(game_mode, board_size, name1, name2)
    else:
        player1_name = input('Please, enter your name.')
    # player1_info = ('Human', player1_name, 'X', 'up-down')
    # player2_info = (player2_class, player2_name, 'O', 'left-right')
    # representation = str(game._board)
    print(str(game_run._game._board))
    game = game_run.run_game(game)
    return game


if __name__ == '__main__':
    print(main())
