from RandomComputerPlayer import RandomComputerPlayer
from RandomComputerPlayer import NameNotStringError, MovingError
from RandomComputerPlayer import SignNotStringError
import pytest


def test_create_RandomCopmuterPlayer_normal():
    player = RandomComputerPlayer('pl_name', 'O', 'up-down', 5)
    assert player.name == 'pl_name'
    assert player._moving == 'up-down'
    assert player._board_size == 5
    assert player._sign == 'O'


def test_create_RandomComputerPlayer_invalid_sign():
    with pytest.raises(SignNotStringError):
        RandomComputerPlayer('pl_name', 8, 'up-down', 5)


def test_create_RandomComputerPlayer_invalid_name():
    with pytest.raises(NameNotStringError):
        RandomComputerPlayer(0, "O", 'up-down', 5)


def test_create_RandomComputerPlayer_invalid_moving():
    with pytest.raises(MovingError):
        RandomComputerPlayer('name', "O", 'up-dow', 5)


def give4(a, b):
    return 4


def test_give_letter_number(monkeypatch):
    player = RandomComputerPlayer('name', 'O', 'up-down', 5)
    monkeypatch.setattr('RandomComputerPlayer.randint', give4)
    assert player.give_letter_number() == (4, 4)
