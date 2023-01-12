from Human_Player import HumanPlayer


class InvalidSizeError(ValueError):
    pass


class EvenSizeError(ValueError):
    pass


class InvalidLetterError(ValueError):
    pass


class InvalidNumberError(ValueError):
    pass


class InvalidSignError(ValueError):
    pass


class InvalidIsFreeTypeError(ValueError):
    pass


class InvalidFieldError(ValueError):
    pass


class FieldDoesNotExistError(ValueError):
    pass


class FieldIsTakenError(ValueError):
    pass


class InvalidPlayersClassError(ValueError):
    pass


class InvalidNameTypeError(ValueError):
    pass


class EmptyNameError(ValueError):
    pass


class MovingTypeError(ValueError):
    pass


class Field:
    def __init__(self, letter, number, is_free=True, sign='-'):
        if letter not in range(26):
            raise InvalidLetterError('Letter of field has to be in range A-Z.')
        if number not in range(26):
            msg = 'Number of field has to be in range 0-25.'
            raise InvalidNumberError(msg)
        if sign not in ['-', 'X', 'O']:
            raise InvalidSignError('Sign of a field has to be - or X or O.')
        if type(is_free) != bool:
            raise InvalidIsFreeTypeError('is_free has to be bool type.')
        self._number = number
        self._letter = letter
        self.is_free = is_free
        self._sign = sign

    def __str__(self):
        return self._sign

    def set_sign(self, new_sign):
        if new_sign not in ['-', 'X', 'O']:
            raise InvalidSignError('Sign of a field has to be - or X or O.')
        self._sign = new_sign
        if new_sign != '-':
            self.is_free = False


class Board:
    def __init__(self, size):
        if size > 25 or size < 5 or type(size) != int:
            msg = 'Size of board should be bigger than 5 and lesser than 25.'
            raise InvalidSizeError(msg)
        if size % 2 == 0:
            raise EvenSizeError('Size of board cannot be even.')
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
        key = f"{letter}{number}"
        if key not in self.fields.keys():
            raise FieldDoesNotExistError('Given field does not exist.')
        if not self.fields[key].is_free:
            raise FieldIsTakenError('This field is not free.')
        self.fields[key].set_sign(sign)

    def __str__(self):
        first_line = self._size * 'O'
        board = f'   {first_line}\n'
        line = ''
        for letter in range(self._size):
            for number in range(self._size):
                field_sign = self.fields[f"{letter}{number}"]._sign
                line += field_sign
            board += f'{letter} X{line}X\n'
            line = ''
        board += f'   {first_line}'
        return board


class Game:
    def __init__(self, pl1_inf, pl2_inf, board_size):
        # player is a tuple (class, name, sign, moving)
        if type(board_size) != int:
            raise InvalidSizeError('Board size has to be int type.')
        if board_size < 5 or board_size > 25:
            msg = 'Size of board should be bigger than 5 and lesser than 25.'
            raise InvalidSizeError(msg)
        if pl1_inf[0] not in ['Human'] or pl2_inf[0] not in ['Human']:
            raise InvalidPlayersClassError("Unknown player's class.")
        if type(pl1_inf[1]) != str or type(pl2_inf[1]) != str:
            raise InvalidNameTypeError('Name has to be str type.')
        if not pl2_inf[1] or not pl1_inf[1]:
            raise EmptyNameError('Name cannot be empty.')
        if pl2_inf[2] not in ['X', 'O'] or pl1_inf[2] not in ["X", 'O']:
            raise InvalidSignError("Player's sign has to be 'X' or 'O'.")
        moving = ['up-down', 'left-right']
        if pl2_inf[3] not in moving or pl1_inf[3] not in moving:
            msg1 = 'Moving type has to be up-down or left-right.'
            raise MovingTypeError(msg1)
        self._board = Board(board_size)
        name1 = pl1_inf[1]
        name2 = pl2_inf[1]
        sign2 = pl2_inf[2]
        self._player1 = HumanPlayer(name1, pl1_inf[2], pl1_inf[3], board_size)
        if pl2_inf[0] == 'Human':
            self._player2 = HumanPlayer(name2, sign2, pl2_inf[3], board_size)

    def up_down_connected(self, fields_dict, pl_sign, fields_in):
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
        new_fields_in = []
        for key in fields_in:
            if key[1] == f'{self._board._size - 1}':
                return f'Game won player with {pl_sign}'
            elif fields_dict[f'{key[0]}{int(key[1]) + 1}']._sign == pl_sign:
                new_fields_in.append(f'{key[0]}{int(key[1]) + 1}')
        return new_fields_in

    def move_on_or_end_up_down(self, fields_in, pl_sign, fields_dict):
        new_fields_in = []
        for key in fields_in:
            if key[0] == f'{self._board._size - 1}':
                return f'Game won player with {pl_sign}'
            elif fields_dict[f'{int(key[0]) + 1}{key[1]}']._sign == pl_sign:
                new_fields_in.append(f'{int(key[0]) + 1}{key[1]}')
        return new_fields_in

    def move_in_checking_left_right(self, fields, fields_in, pl_sign):
        fields_in = self.move_on_or_end_left_right(fields_in, pl_sign, fields)
        if type(fields_in) == str:
            return fields_in
        fields_in = self.up_down_connected(fields, pl_sign, fields_in)
        return fields_in

    def move_in_checking_up_down(self, fields, fields_in, pl_sign):
        fields_in = self.move_on_or_end_up_down(fields_in, pl_sign, fields)
        if type(fields_in) == str:
            return fields_in
        fields_in = self.left_right_connected(fields, pl_sign, fields_in)
        return fields_in

    def check_if_game_is_finished_left_right(self, pl_sign):
        fields_in = []
        fields = self._board.fields
        for letter in range(self._board._size):
            if fields[f'{letter}{0}']._sign == pl_sign:
                fields_in.append(f'{letter}{0}')
        while fields_in != []:
            fields_in = self.move_in_checking_left_right(fields, fields_in, pl_sign)
            if type(fields_in) == str:
                return fields_in
        # game in not finished
        return False

    def check_if_game_is_finished_up_down(self, pl_sign):
        fields_in = []
        fields = self._board.fields
        for number in range(self._board._size):
            if fields[f'{0}{number}']._sign == pl_sign:
                fields_in.append(f'{0}{number}')
        while fields_in != []:
            fields_in = self.move_in_checking_up_down(fields, fields_in, pl_sign)
            if type(fields_in) == str:
                return fields_in
        # game in not finished
        return False


class GameRun:
    def __init__(self, game_mode, board_size, name1='Player1', name2='Player2'):
        self._game_mode = game_mode
        self._player1 = ('Human', name1, 'X', 'left-right')
        if self._game_mode == 'Human':
            player2_class = 'Human'
        self._player2 = (player2_class, name2, 'O', 'up-down')
        self._game = Game(self._player1, self._player2, board_size)
        self.result_of_game = False

    def making_moves(self, field_str, player):
        sign = player._sign
        result = True
        # ord_letter = ord(field_str[0])
        # if ord_letter not in range(65, 65 + self._game._board._size):
        #     result = 'wrong letter'
        # elif len(field_str) != 2:
        #     result = 'invalid length'
        # elif int(field_str[1]) not in range(self._game._board._size):
        #     result = 'invalid number'
        if type(result) != str:
            self._game._board.move(field_str[0], field_str[1], sign)
        return result

    def players_move(self, player):
        move1 = ''
        while type(move1) == str:
            field = self._game._player1.give_letter_and_number()
            field = f'{field[0]}{field[1]}'
            move1 = self.making_moves(field, self._game._player1)
            print(str(self._game._board))
        if self._game._player1._moving == 'left-right':
            self.result_of_game = self._game.check_if_game_is_finished_left_right(player._sign)
        else:
            self.result_of_game = self._game.check_if_game_is_finished_up_down(player._sign)

    def run_game(self):
            while not self.result_of_game:
                #players1 move
                #players2 move
                self.players_move(self._game._player1)
                if not self.result_of_game:
                    self.players_move(self._game._player2)
            return self.result_of_game



