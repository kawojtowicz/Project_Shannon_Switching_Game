from random import randint


class NameNotStringError(ValueError):
    pass


class SignNotStringError(ValueError):
    pass


class MovingError(ValueError):
    pass


class HeavyComputerPlayer:
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

    def give_letter_and_number(self, previous_letter, previous_number, fields, letter='', number=''):
        if f'{previous_letter}{int(previous_number) + 2}' in fields.keys():
            if fields[f'{previous_letter}{int(previous_number) + 2}'].is_free:
                letter = previous_letter
                number = int(previous_number) + 2
            elif fields[f'{previous_letter}{int(previous_number) - 2}'].is_free:
                letter = previous_letter
                number = int(previous_number) - 2
            elif fields[f'{int(previous_letter) + 2}{previous_number}'].is_free:
                letter = int(previous_letter) + 2
                number = previous_number
            elif fields[f'{int(previous_letter) - 2}{previous_number}'].is_free:
                letter = int(previous_letter) - 2
                number = previous_number
        else:
            letter = randint(0, self._board_size - 1)
            number = randint(0, self._board_size - 1)
        return (letter, number)