from random import randint


class NameNotStringError(ValueError):
    pass


class SignNotStringError(ValueError):
    pass


class MovingError(ValueError):
    pass


class HeavyComputerPlayer:
    """Represents player who choose letter and number of the field\
         according to simple criteria."""
    def __init__(self, name, pl_sign, moving, board_size):
        if type(pl_sign) != str:
            raise SignNotStringError("Player's sign has to be string type.")
        if type(name) != str:
            raise NameNotStringError('Name has to be string type.')
        self._sign = pl_sign
        if moving != 'up-down' and moving != 'left-right':
            msg = "Player's moving has to be up-down or left-right."
            raise MovingError(msg)
        self._moving = moving
        self.name = name
        self._board_size = board_size

    def take_near_field(self, letter, number, fields):
        if f'{letter}{number}' in fields.keys():
            if fields[f'{letter}{number}'].is_free:
                return (letter, number)
        else:
            return False

    def give_letter_number(self, previous_letter, previous_number, fields):
        fields_to_check = [
            (previous_letter, previous_number + 2),
            (previous_letter, previous_number - 2),
            (previous_letter + 2, previous_number),
            (previous_letter - 2, previous_number)
            ]
        for field in fields_to_check:
            move = self.take_near_field(field[0], field[1], fields)
            if move:
                return move
        letter = randint(0, self._board_size - 1)
        number = randint(0, self._board_size - 1)
        return (letter, number)
