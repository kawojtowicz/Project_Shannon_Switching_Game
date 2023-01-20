from random import randint


class NameNotStringError(ValueError):
    pass


class SignNotStringError(ValueError):
    pass


class MovingError(ValueError):
    pass


class RandomComputerPlayer:
    """Represents player who draws letter ans number of the field."""
    def __init__(self, name, pl_sign, moving, board_size):
        if type(pl_sign) != str:
            raise SignNotStringError("Player's sign has to be string type.")
        if type(name) != str:
            raise NameNotStringError('Name has to be string type')
        self._sign = pl_sign
        if moving != 'up-down' and moving != 'left-right':
            msg = "Player's moving has to be up-down or left-right."
            raise MovingError(msg)
        self._moving = moving
        self.name = name
        self._board_size = board_size

    def give_letter_number(self, letter='', number=''):
        letter = randint(0, self._board_size - 1)
        number = randint(0, self._board_size - 1)
        return (letter, number)
