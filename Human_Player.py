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
    """Represents player who plays typing letter and number on the keyboard."""
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

    def give_letter_number(self, letter='', number=''):
        edge = 64 + self._board_size
        edge1 = self._board_size - 1
        while not letter:
            letter = input(f"{self.name}, enter letter of choosen field.")
            if len(letter) > 1:
                print('Please, enter one sign.')
                letter = ''
            elif letter != '' and (ord(letter) < 65 or ord(letter) > edge):
                print(f"Your first sign has to be letter A-{chr(edge)}.")
                letter = ''
        while not number:
            border = 48 + self._board_size
            number = input(f"{self.name}, enter number of choosen field.")
            if len(number) != 1:
                print('Please, choose one sign.')
                number = ''
            elif number != '' and ord(number) not in range(48, border):
                print(f"Your second sign has to be number 0-{edge1}.")
                number = ''
        letter = ord(letter) - 65
        number = int(number)
        return (letter, number)
