from Human_Player import HumanPlayer
from Human_Player import SignNotStringError, MovingError, NameNotStringError
import pytest


def test_cretate_player_normal():
    player1 = HumanPlayer('Kasia', 'X', 'up-down', 5)
    assert player1.name == 'Kasia'
    assert player1._sign == "X"
    assert player1._moving == "up-down"
    assert player1._board_size == 5


def test_cretate_player_SingNotString():
    with pytest.raises(SignNotStringError):
        HumanPlayer('Kasia', 7, "up-down", 8)


def test_cretate_player_MovingError():
    with pytest.raises(MovingError):
        HumanPlayer('pl_na', "Player", "up-dow", 8)


def test_create_player_NameNotStringError():
    with pytest.raises(NameNotStringError):
        HumanPlayer(True, "Player", "up-down", 8)


def test_give_letter_number_normal():
    player = HumanPlayer('Kasia', "X", 'up-down', 5)
    field = player.give_letter_number('A', '0')
    assert field == (0, 0)


def giveA(msg):
    return 'A'


def test_give_letter_number_invalid_letter(monkeypatch):
    monkeypatch.setattr('builtins.input', giveA)
    player = HumanPlayer('name', 'X', 'left-right', 5)
    assert player.give_letter_number('', '0') == (0, 0)


def give0(msg):
    return '0'


def test_give_letter_number_invalid_number(monkeypatch):
    monkeypatch.setattr('builtins.input', give0)
    player = HumanPlayer('name', 'X', 'left-right', 5)
    assert player.give_letter_number('A', '') == (0, 0)
