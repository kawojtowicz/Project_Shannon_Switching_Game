from HeavyComputerPlayer import HeavyComputerPlayer
from HeavyComputerPlayer import NameNotStringError, MovingError
from HeavyComputerPlayer import SignNotStringError
from classes import Field
import pytest


test_fields_sim = {
        '00': Field(0, 0), '01': Field(0, 1, False, "X"), '02': Field(0, 2),
        '03': Field(0, 3, False, "X"), '04': Field(0, 4),

        '10': Field(1, 0, False, 'O'), '11': Field(1, 1),
        '12': Field(1, 2, False, 'O'),
        '13': Field(1, 3), '14': Field(1, 4, False, 'O'),

        '20': Field(2, 0), '21': Field(2, 1, False, "X"), '22': Field(2, 2),
        '23': Field(2, 3, False, "X"), '24': Field(2, 4),

        '30': Field(3, 0, False, 'O'), '31': Field(3, 1),
        '32': Field(3, 2, False, 'O'),
        '33': Field(3, 3), '34': Field(3, 4, False, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, False, "X"), '42': Field(4, 2),
        '43': Field(4, 3, False, "X"), '44': Field(4, 4)}


def test_create_HaevyCopmuterPlayer_normal():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    assert player.name == 'name'
    assert player._moving == 'up-down'
    assert player._board_size == 5
    assert player._sign == 'O'


def test_create_HeavyComputerPlayer_invalid_sign():
    with pytest.raises(SignNotStringError):
        HeavyComputerPlayer('name', 8, 'up-down', 5)


def test_create_HeavyComputerPlayer_invalid_name():
    with pytest.raises(NameNotStringError):
        HeavyComputerPlayer(0, "O", 'up-down', 5)


def test_create_HeavyComputerPlayer_invalid_moving():
    with pytest.raises(MovingError):
        HeavyComputerPlayer('name', "O", 'up-dow', 5)


def test_take_near_field_normal():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    assert player.take_near_field(0, 0, test_fields_sim) == (0, 0)


def test_take_near_field_not_free():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    test_fields_sim['00'].set_sign('X')
    test_fields_sim['00'].is_free = False
    assert not player.take_near_field(0, 0, test_fields_sim)


def test_give_letter_number_not_free_right():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    assert player.give_letter_number(2, 2, test_fields_sim) == (2, 4)


def test_give_letter_number_not_free_left():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    test_fields_sim['24'].is_free = False
    assert player.give_letter_number(2, 2, test_fields_sim) == (2, 0)


def test_give_letter_number_not_free_down():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    test_fields_sim['20'].is_free = False
    test_fields_sim['24'].is_free = False
    assert player.give_letter_number(2, 2, test_fields_sim) == (4, 2)


def test_give_letter_number_not_free_up():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    test_fields_sim['20'].is_free = False
    test_fields_sim['24'].is_free = False
    test_fields_sim['42'].is_free = False
    assert player.give_letter_number(2, 2, test_fields_sim) == (0, 2)


def test_give_letter_number_edge_right():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    assert player.give_letter_number(2, 4, test_fields_sim) == (2, 2)


def test_give_letter_number_edge_left():
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    assert player.give_letter_number(2, 0, test_fields_sim) == (2, 2)


def test_give_letter_number_edge_down():
    player = HeavyComputerPlayer('pl_name', 'O', 'up-down', 5)
    test_fields_sim['31'].is_free = False
    assert player.give_letter_number(3, 3, test_fields_sim) == (1, 3)


def give4(a, b):
    return 4


def test_give_letter_number_edge_up(monkeypatch):
    player = HeavyComputerPlayer('name', 'O', 'up-down', 5)
    test_fields_sim['31'].is_free = False
    test_fields_sim['13'].is_free = False
    monkeypatch.setattr('HeavyComputerPlayer.randint', give4)
    assert player.give_letter_number(1, 1, test_fields_sim) == (4, 4)
