class TooManySignsError(ValueError):
    pass


class InvalidLetterError(ValueError):
    pass


class InvalidNumberError(ValueError):
    pass


class NameNotStringError(ValueError):
    pass


class SignNotStringError(ValueError):
    pass


class MovingError(ValueError):
    pass


class HumanPlayer:
    def __init__(self, name, pl_sign, moving, board_size):
        if type(pl_sign) != str:
            raise SignNotStringError("Player's sign has to be string type.")
        if type(name) != str:
            raise NameNotStringError('Name has to be string type.')
        self._sign = pl_sign
        if moving != 'up-down' and moving != 'left-right':
            msg = "Player's moving has to be up-down or left-right"
            raise MovingError(msg)
        self._moving = moving
        self.name = name
        self._board_size = board_size
        # to edit

    def give_letter_and_number(self, letter='', number=''):
        edge = 64 + self._board_size
        edge1 = self._board_size - 1
        while letter == '':
            letter = input("Enter letter of choosen field.")
            if len(letter) > 1:
                print('"Please, enter one sign"')
                letter = ''
            if ord(letter) < 65 or ord(letter) > edge:
                print(f"Your first sign has to be letter A-{edge}")
                letter = ''
        while number == '':
            number = input("Enter number of choosen field.")
            if int(number) not in range(self._board_size + 1):
                print(f"Your second sign has to be number 0-{edge1}")
                number = ''
        letter = ord(letter) - 65
        number = int(number)
        return (letter, number)
# try:
#                 move1 = game._player1.give_letter_and_number()
#             except :
#                 key = f'{move1[0]}{move1[1]}'
#                 if key not in game._board._fields.keys():
#                     print("This field does not exist. Choose another one.")
#                 elif not game._board._fields[key].is_free:
#                     print("This field is not free. Please choose another one.")