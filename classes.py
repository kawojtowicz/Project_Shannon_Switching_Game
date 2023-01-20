from Human_Player import HumanPlayer
from RandomComputerPlayer import RandomComputerPlayer
from HeavyComputerPlayer import HeavyComputerPlayer


class InvalidSizeError(ValueError):
    pass


class EvenSizeError(ValueError):
    'Size of board cannot be even.'


class InvalidLetterError(ValueError):
    'Letter of field has to be in range A-I.'


class InvalidNumberError(ValueError):
    'Number of field has to be in range 0-9.'


class InvalidSignError(ValueError):
    'Sign of a field has to be - or X or O.'


class InvalidIsFreeTypeError(ValueError):
    'is_free has to be bool type.'


class FieldDoesNotExistError(ValueError):
    'Given field does not exist.'


class FieldIsTakenError(ValueError):
    'This field is not free.'


class InvalidPlayersClassError(ValueError):
    "Unknown player's class."


class InvalidNameTypeError(ValueError):
    'Name has to be str type.'


class EmptyNameError(ValueError):
    'Name cannot be empty.'


class MovingTypeError(ValueError):
    'Moving type has to be up-down or left-right.'


class GameModeError(ValueError):
    'Game mode has to be 2, 3 or Human.'


class Field:
    """
    Represents field on a board.
    Attributes:
    -location attributes: letter and number
    -sign, is_free: say if one of players took the field or it is free.
    """
    def __init__(self, letter, number, is_free=True, sign='-'):
        if letter not in range(10):
            raise InvalidLetterError()
        if number not in range(10):
            raise InvalidNumberError()
        if sign not in ['-', 'X', 'O']:
            raise InvalidSignError()
        if type(is_free) != bool:
            raise InvalidIsFreeTypeError()
        self._number = number
        self._letter = letter
        self.is_free = is_free
        self._sign = sign

    def __str__(self):
        return self._sign

    def set_sign(self, new_sign):
        if new_sign not in ['-', 'X', 'O']:
            raise InvalidSignError()
        self._sign = new_sign
        if new_sign != '-':
            self.is_free = False


class Board:
    """Represents board of the game. Has a size attribute."""
    def __init__(self, size):
        if size > 9 or size < 5 or type(size) != int:
            msg = 'Size of board should be bigger than 4 and lesser than 10.'
            raise InvalidSizeError(msg)
        if size % 2 == 0:
            raise EvenSizeError()
        self._size = size
        self.fields = {}
        for letter in range(self._size):
            for number in range(self._size):
                self.fields[f'{letter}{number}'] = Field(letter, number)
                if (letter % 2 == 0) and (number % 2 == 1):
                    self.fields[f"{letter}{number}"].set_sign('X')
                elif (letter % 2 == 1) and (number % 2 == 0):
                    self.fields[f"{letter}{number}"].set_sign('O')

    def move(self, letter, number, sign):
        """Changes sign of one of fields."""
        key = f"{letter}{number}"
        if key not in self.fields.keys():
            raise FieldDoesNotExistError()
        if not self.fields[key].is_free:
            raise FieldIsTakenError()
        self.fields[key].set_sign(sign)

    def __str__(self):
        first_line = '   '
        for number in range(self._size):
            first_line += f'{number}'
        second_line = self._size * 'O'
        board = f'{first_line}\n   {second_line}\n'
        line = ''
        for letter in range(self._size):
            for number in range(self._size):
                field_sign = self.fields[f"{letter}{number}"]._sign
                line += field_sign
            board += f'{chr(letter + 65)} X{line}X\n'
            line = ''
        board += f'   {second_line}'
        return board


class Game:
    """Represents game as a connection players and in certain state."""
    def __init__(self, pl1_inf, pl2_inf, board_size):
        # player is a tuple: (class, name, sign, moving)
        b_siz = board_size
        nm = 'Computer Player'
        modes = ['Human', '2', '3']
        if type(board_size) != int:
            raise InvalidSizeError('Board size has to be int type.')
        if board_size < 5 or board_size > 9:
            msg = 'Size of board should be bigger than 5 and lesser than 10.'
            raise InvalidSizeError(msg)
        if pl1_inf[0] not in ['Human', '2', '3'] or pl2_inf[0] not in modes:
            raise InvalidPlayersClassError()
        if type(pl1_inf[1]) != str or type(pl2_inf[1]) != str:
            raise InvalidNameTypeError()
        if not pl2_inf[1] or not pl1_inf[1]:
            raise EmptyNameError()
        if pl2_inf[2] not in ['X', 'O'] or pl1_inf[2] not in ["X", 'O']:
            raise InvalidSignError()
        moving = ['up-down', 'left-right']
        if pl2_inf[3] not in moving or pl1_inf[3] not in moving:
            raise MovingTypeError()
        self._board = Board(board_size)
        name1 = pl1_inf[1]
        name2 = pl2_inf[1]
        sign2 = pl2_inf[2]
        self._player1 = HumanPlayer(name1, pl1_inf[2], pl1_inf[3], board_size)
        if pl2_inf[0] == 'Human':
            self._player2 = HumanPlayer(name2, sign2, pl2_inf[3], board_size)
        elif pl2_inf[0] == '2':
            self._player2 = RandomComputerPlayer(nm, sign2, pl2_inf[3], b_siz)
        elif pl2_inf[0] == '3':
            self._player2 = HeavyComputerPlayer(nm, sign2, pl1_inf[3], b_siz)

    def up_down_connected(self, fields_dict, pl_sign, fields_in):
        """Adds to the list fields which are up/down connected with given."""
        for key in fields_in:
            if f'{int(key[0]) + 1}{key[1]}' in fields_dict.keys():
                if fields_dict[f'{int(key[0]) + 1}{key[1]}']._sign == pl_sign:
                    if f'{int(key[0]) + 1}{key[1]}' not in fields_in:
                        fields_in.append(f'{int(key[0]) + 1}{key[1]}')
            if f'{int(key[0]) - 1}{key[1]}' in fields_dict.keys():
                if fields_dict[f'{int(key[0]) - 1}{key[1]}']._sign == pl_sign:
                    if f'{int(key[0]) - 1}{key[1]}' not in fields_in:
                        fields_in.append(f'{int(key[0]) - 1}{key[1]}')
        return fields_in

    def left_right_connected(self, fields_dict, pl_sign, fields_in):
        """Adds to the list fields which are left/right connected\
             with given."""
        for key in fields_in:
            if f'{key[0]}{int(key[1]) + 1}' in fields_dict.keys():
                if fields_dict[f'{key[0]}{int(key[1]) + 1}']._sign == pl_sign:
                    if f'{key[0]}{int(key[1]) + 1}' not in fields_in:
                        fields_in.append(f'{key[0]}{int(key[1]) + 1}')
            if f'{key[0]}{int(key[1]) - 1}' in fields_dict.keys():
                if fields_dict[f'{key[0]}{int(key[1]) - 1}']._sign == pl_sign:
                    if f'{key[0]}{int(key[1]) - 1}' not in fields_in:
                        fields_in.append(f'{key[0]}{int(key[1]) - 1}')
        return fields_in

    def move_on_or_end_left_right(self, fields_in, pl_sign, fields_dict):
        """Checks if there is a field which touches the right edge.\
             If so, returns player's sign.
         If there is not, returns list of fields of next column connected \
            with one of given fields."""
        new_fields_in = []
        for key in fields_in:
            if key[1] == f'{self._board._size - 1}':
                return f'{pl_sign}'
            elif fields_dict[f'{key[0]}{int(key[1]) + 1}']._sign == pl_sign:
                new_fields_in.append(f'{key[0]}{int(key[1]) + 1}')
        return new_fields_in

    def move_on_or_end_up_down(self, fields_in, pl_sign, fields_dict):
        """Checks if there is a field which touches the down edge.\
             If so, returns player's sign.
         If there is not, returns list of fields of next line connected \
            with one of given fields."""
        new_fields_in = []
        for key in fields_in:
            if key[0] == f'{self._board._size - 1}':
                return f'{pl_sign}'
            elif fields_dict[f'{int(key[0]) + 1}{key[1]}']._sign == pl_sign:
                new_fields_in.append(f'{int(key[0]) + 1}{key[1]}')
        return new_fields_in

    def move_in_checking_left_right(self, fields, fields_in, pl_sign):
        """Makes move in right and returns next fields \
            to check or returns sign of winner."""
        fields_in = self.move_on_or_end_left_right(fields_in, pl_sign, fields)
        if type(fields_in) == str:
            return fields_in
        fields_in = self.up_down_connected(fields, pl_sign, fields_in)
        return fields_in

    def move_in_checking_up_down(self, fields, fields_in, pl_sign):
        """Makes move in down and returns next fields \
            to check or returns sign of winner."""
        fields_in = self.move_on_or_end_up_down(fields_in, pl_sign, fields)
        if type(fields_in) == str:
            return fields_in
        fields_in = self.left_right_connected(fields, pl_sign, fields_in)
        return fields_in

    def if_game_ended_left_right(self, pl_sign):
        """Checks if game is won by player who moves left-right \
            and if so returns winner's sign.
            If game if not finished returns False."""
        fields_in = []
        fields = self._board.fields
        for letter in range(self._board._size):
            if fields[f'{letter}{0}']._sign == pl_sign:
                fields_in.append(f'{letter}{0}')
        while fields_in != []:
            fields_in = \
                self.move_in_checking_left_right(fields, fields_in, pl_sign)
            if type(fields_in) == str:
                return fields_in
        # game in not finished yet:
        return False

    def if_game_ended_up_down(self, pl_sign):
        """Checks if game is won by player who moves up-down \
            and if so returns winner's sign.
            If game if not finished returns False."""
        fields_in = []
        fields = self._board.fields
        for number in range(self._board._size):
            if fields[f'{0}{number}']._sign == pl_sign:
                fields_in.append(f'{0}{number}')
        while fields_in != []:
            fields_in = \
                self.move_in_checking_up_down(fields, fields_in, pl_sign)
            if type(fields_in) == str:
                return fields_in
        # game in not finished yet:
        return False

    def player_move(self, player, lett='', numb='', pr_lett='', pr_numb=''):
        """Takes letter and number of a field from the player \
            and sets his sign on it. """
        if type(player) is HeavyComputerPlayer:
            while not self._board.fields[f'{lett}{numb}'].is_free:
                b_fields = self._board.fields
                lett, numb = \
                    player.give_letter_number(pr_lett, pr_numb, b_fields)
            if self._board.fields[f'{lett}{numb}'].is_free:
                self._board.fields[f'{lett}{numb}'].set_sign(player._sign)
        else:
            while not self._board.fields[f'{lett}{numb}'].is_free:
                if type(player) is HumanPlayer:
                    print('This field is not free. Choose another.')
                lett, numb = player.give_letter_number()
        if self._board.fields[f'{lett}{numb}'].is_free:
            self._board.fields[f'{lett}{numb}'].set_sign(player._sign)


class GameRun:
    """Represents particular gameplay.
    Attributes:
    -game_mode: information which decides about opponent's class
    -player1, player2: players of the game
    -game: connection between players, board
    -result_of_game: says if gameplay is already finished."""
    def __init__(self, game_mode, board_siz, name1='Player1', name2='Player2'):
        if game_mode not in ['Human', '2', '3']:
            raise GameModeError()
        if board_siz not in [5, 7, 9]:
            raise InvalidSizeError('Size has to be 5, 7 or 9.')
        if type(name1) != str or type(name2) != str:
            raise InvalidNameTypeError()
        if not name1 or not name2:
            raise EmptyNameError()
        self._game_mode = game_mode
        self._player1 = ('Human', name1, 'X', 'left-right')
        self._player2 = (self._game_mode, name2, 'O', 'up-down')
        self._game = Game(self._player1, self._player2, board_siz)
        self.result_of_game = False

    def player1_turn(self):
        letter, number = self._game._player1.give_letter_number()
        self._game.player_move(self._game._player1, letter, number)
        print(str(self._game._board))
        self.result_of_game = \
            self._game.if_game_ended_left_right(self._game._player1._sign)
        return (letter, number)

    def player2_turn_heavy(self, last_l, last_n):
        fields = self._game._board.fields
        lett, numb = \
            self._game._player2.give_letter_number(last_l, last_n, fields)
        self._game.player_move(self._game._player2, lett, numb, last_l, last_n)
        print(str(self._game._board))
        self.result_of_game = \
            self._game.if_game_ended_up_down(self._game._player2._sign)

    def player2_turn_human_random(self):
        letter, number =\
            self._game._player2.give_letter_number()
        self._game.player_move(self._game._player2, letter, number)
        print(str(self._game._board))
        self.result_of_game = \
            self._game.if_game_ended_up_down(self._game._player2._sign)

    def run_game(self):
        """Plays the game, returns name of the winner."""
        while not self.result_of_game:
            last_letter, last_number = self.player1_turn()
            if not self.result_of_game:
                if type(self._game._player2) is HeavyComputerPlayer:
                    self.player2_turn_heavy(last_letter, last_number)
                else:
                    self.player2_turn_human_random()
        result = self.result_of_game
        if result:
            if result == 'X':
                return self._game._player1.name
            else:
                return self._game._player2.name
