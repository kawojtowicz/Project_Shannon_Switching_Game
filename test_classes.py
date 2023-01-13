from classes import Field, Board, Game, GameRun
from classes import InvalidSizeError, EvenSizeError, InvalidSignError
from classes import InvalidIsFreeTypeError, InvalidLetterError
from classes import InvalidNumberError, FieldDoesNotExistError
from classes import FieldIsTakenError, InvalidPlayersClassError
from classes import InvalidNameTypeError, EmptyNameError, MovingTypeError
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

test_fields2 = {
        '00': Field(0, 0), '01': Field(0, 1, True, 'X'),
        '02': Field(0, 2, True, 'X'),
        '03': Field(0, 3, True, 'X'), '04': Field(0, 4),

        '10': Field(1, 0, True, 'O'), '11': Field(1, 1, True, 'X'),
        '12': Field(1, 2, True, 'O'),
        '13': Field(1, 3, True, 'X'), '14': Field(1, 4, True, 'O'),

        '20': Field(2, 0, True, 'X'), '21': Field(2, 1, True, 'X'),
        '22': Field(2, 2),
        '23': Field(2, 3, True, 'X'), '24': Field(2, 4),

        '30': Field(3, 0, True, 'O'), '31': Field(3, 1),
        '32': Field(3, 2, True, 'O'),
        '33': Field(3, 3, True, 'X'), '34': Field(3, 4, True, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, True, 'X'),
        '42': Field(4, 2),
        '43': Field(4, 3, True, 'X'), '44': Field(4, 4, True, 'X')
    }

test_fields3 = {
        '00': Field(0, 0, False, 'O'), '01': Field(0, 1, False, "X"),
        '02': Field(0, 2, False, 'O'),
        '03': Field(0, 3, False, "X"), '04': Field(0, 4),

        '10': Field(1, 0, False, 'O'), '11': Field(1, 1),
        '12': Field(1, 2, False, 'O'),
        '13': Field(1, 3, False, 'O'), '14': Field(1, 4, False, 'O'),

        '20': Field(2, 0), '21': Field(2, 1, False, "X"), '22': Field(2, 2),
        '23': Field(2, 3, False, "X"), '24': Field(2, 4, False, 'O'),

        '30': Field(3, 0, False, 'O'), '31': Field(3, 1),
        '32': Field(3, 2, False, 'O'),
        '33': Field(3, 3, False, 'O'), '34': Field(3, 4, False, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, False, "X"),
        '42': Field(4, 2, False, 'O'),
        '43': Field(4, 3, False, "X"), '44': Field(4, 4)}

test_fields4 = {
        '00': Field(0, 0), '01': Field(0, 1, True, 'X'),
        '02': Field(0, 2, True, 'O'),
        '03': Field(0, 3, True, 'X'), '04': Field(0, 4),

        '10': Field(1, 0, True, 'O'), '11': Field(1, 1, True, 'X'),
        '12': Field(1, 2, True, 'O'),
        '13': Field(1, 3, True, 'X'), '14': Field(1, 4, True, 'O'),

        '20': Field(2, 0, True, 'X'), '21': Field(2, 1, True, 'X'),
        '22': Field(2, 2, True, 'O'),
        '23': Field(2, 3, True, 'X'), '24': Field(2, 4),

        '30': Field(3, 0, True, 'O'), '31': Field(3, 1, True, 'O'),
        '32': Field(3, 2, True, 'O'),
        '33': Field(3, 3, True, 'X'), '34': Field(3, 4, True, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, True, 'X'),
        '42': Field(4, 2),
        '43': Field(4, 3, True, 'X'), '44': Field(4, 4, True, 'X')
    }


def test_create_field():
    field = Field(0, 6)
    assert field._letter == 0
    assert field._number == 6
    assert field.is_free
    assert field._sign == '-'


def test_create_field_invalid_letter():
    with pytest.raises(InvalidLetterError):
        Field(75, 12)


def test_create_field_invalid_number():
    with pytest.raises(InvalidNumberError):
        Field(4, 80)


def test_create_field_invalid_sign():
    with pytest.raises(InvalidSignError):
        Field(5, 12, sign='U')


def test_create_field_invalid_is_free():
    with pytest.raises(InvalidIsFreeTypeError):
        Field(5, 12, 7)


def test_set_sign():
    field = Field(0, 6)
    field.set_sign('O')
    assert field._letter == 0
    assert field._number == 6
    assert not field.is_free
    assert field._sign == 'O'


def test_set_sign_invalid_new_sign():
    field = Field(0, 6)
    with pytest.raises(InvalidSignError):
        field.set_sign('T')


def test__str__():
    field = Field(1, 7)
    assert str(field) == '-'


def test_create_board_normal():
    board = Board(5)
    for key in test_fields_sim.keys():
        assert test_fields_sim[key]._letter == board.fields[key]._letter
        assert test_fields_sim[key]._number == board.fields[key]._number
        assert test_fields_sim[key].is_free == board.fields[key].is_free
        assert test_fields_sim[key]._sign == board.fields[key]._sign
        assert board._size == 5


def test_create_board_even_number():
    with pytest.raises(EvenSizeError):
        Board(6)


def test_create_board_invalid_number():
    with pytest.raises(InvalidSizeError):
        Board(45)
    with pytest.raises(InvalidSizeError):
        Board(3)


def test_create_board_even_size():
    with pytest.raises(EvenSizeError):
        Board(12)


def test_move_normal():
    board = Board(5)
    board.move(0, 0, "X")
    assert board.fields['00']._sign == 'X'
    assert not board.fields['00'].is_free


def test_move_field_does_not_exist():
    board = Board(5)
    with pytest.raises(FieldDoesNotExistError):
        board.move(10, 0, "X")


def test_move_field_taken():
    board = Board(5)
    with pytest.raises(FieldIsTakenError):
        board.move(1, 0, "X")


def test__str__board():
    board = Board(5)
    line = '   01234\n   OOOOO\nA X-X-X-X\nB XO-O-OX\nC X-X-X-X\nD XO-O-OX\nE X-X-X-X\n   OOOOO'
    assert str(board) == line


def test_create_game():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields_sim
    assert game._player1.name == 'Kasia'
    assert game._player2.name == 'Ann'
    assert game._board._size == 5
    assert game._board.fields == test_fields_sim


def test_create_game_board_size_not_int():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidSizeError):
        Game(player1, player2, 'k')


def test_create_game_board_size_not_in_range():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidSizeError):
        Game(player1, player2, 1)
    with pytest.raises(InvalidSizeError):
        Game(player1, player2, 66)


def test_create_game_invalid_players_class():
    player1 = ('Huma', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidPlayersClassError):
        Game(player1, player2, 5)


def test_create_game_invalid_name_type():
    player1 = ('Human', 7, "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidNameTypeError):
        Game(player1, player2, 5)


def test_create_game_empty_name():
    player1 = ('Human', '', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(EmptyNameError):
        Game(player1, player2, 5)


def test_create_game_invalid_moving_type():
    player1 = ('Human', 'Kasia', "X", 'up-dow')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(MovingTypeError):
        Game(player1, player2, 5)


def test_up_down_connected_normal():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['01', '41']
    fields_in = game.up_down_connected(test_fields2, 'X', fields_in)
    assert fields_in == ['01', '41', '11', '21']


def test_up_down_connected_no_new_fields():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['30', '23']
    fields_in = game.up_down_connected(test_fields3, 'X', fields_in)
    assert fields_in == ['30', '23']


def test_left_right_connected_normal():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['10', '12']
    fields_in = game.left_right_connected(test_fields3, 'O', fields_in)
    assert fields_in == ['10', '12', '13', '14']


def test_left_right_connected_no_new_fields():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['21', '30']
    fields_in = game.left_right_connected(test_fields3, 'O', fields_in)
    assert fields_in == ['21', '30']


def test_move_on_or_end_left_right():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['44']
    msg = 'Game won player with X'
    assert game.move_on_or_end_left_right(fields_in, 'X', test_fields2) == msg
    fields_in1 = ['01', '11', '21', '41']
    fields_in1 = game.move_on_or_end_left_right(fields_in1, 'X', test_fields2)
    assert fields_in1 == ['02']


def test_move_on_or_end_left_right_empty_list():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in1 = ['01', '11', '21', '41']
    fields_in1 = game.move_on_or_end_left_right(fields_in1, 'X', test_fields4)
    assert fields_in1 == []


def test_move_on_or_end_up_down():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in = ['42']
    msg = 'Game won player with O'
    assert game.move_on_or_end_up_down(fields_in, 'O', test_fields3) == msg
    fields_in1 = ['10', '12', '13', '14']
    fields_in1 = game.move_on_or_end_up_down(fields_in1, 'O', test_fields3)
    assert fields_in1 == ['24']


def test_move_on_or_end_up_down_empty_list():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    fields_in1 = ['30', '31', '32']
    fields_in1 = game.move_on_or_end_up_down(fields_in1, 'O', test_fields4)
    assert fields_in1 == []


def test_move_in_checking_left_right():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    after = game.move_in_checking_left_right(test_fields2, ['20'], 'X')
    fields_in_after = after
    assert fields_in_after == ['21', '11', '01']


def test_move_in_checking_up_down():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    after = game.move_in_checking_up_down(test_fields3, ['02'], 'O')
    fields_in_after = after
    assert fields_in_after == ['12', '13', '14']


def test_check_if_game_is_finished_left_right():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields2
    msg = 'Game won player with X'
    assert game.check_if_game_is_finished_left_right('X') == msg
    test_fields2['44']._sign = '-'
    assert not game.check_if_game_is_finished_left_right('X')
    test_fields2['44']._sign = 'O'
    assert not game.check_if_game_is_finished_left_right('X')


def test_check_if_game_is_finished_up_down():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields3
    msg = 'Game won player with O'
    assert game.check_if_game_is_finished_up_down('O') == msg
    test_fields3['42']._sign = '-'
    assert not game.check_if_game_is_finished_up_down('O')
    test_fields2['42']._sign = 'X'
    assert not game.check_if_game_is_finished_up_down('O')


def test_create_game_run():
    game_run = GameRun('Human', 5, "Kasia", "Computer")
    assert game_run._player1 == ('Human', "Kasia", 'X', 'left-right')
    assert game_run._player2 == ('Human', "Computer", 'O', 'up-down')
    assert game_run._game_mode == 'Human'
    for key in test_fields_sim.keys():
        assert test_fields_sim[key]._letter == game_run._game._board.fields[key]._letter
        assert test_fields_sim[key]._number == game_run._game._board.fields[key]._number
        assert test_fields_sim[key].is_free == game_run._game._board.fields[key].is_free
        assert test_fields_sim[key]._sign == game_run._game._board.fields[key]._sign
    assert game_run._game._board._size == 5
    assert not game_run.result_of_game


# def test_moving_wrong_letter():
#     game_run = GameRun("Human", 5, 'Kasia', "Player")
#     assert game_run.making_moves("72", game_run._game._player1) == 'wrong letter'


# def test_moving_wrong_number():
#     game_run = GameRun("Human", 5, 'Kasia', "Player")
#     assert game_run.making_moves("A9", game_run._game._player1) == 'invalid number'


# def test_moving_invalid_length():
#     game_run = GameRun("Human", 5, 'Kasia', "Player")
#     assert game_run.making_moves("A33", game_run._game._player1) == 'invalid length'


# def test_moving_normal():
#     game_run = GameRun("Human", 5, "Kasia", "PL")
#     game_run.making_moves('A0', game_run._game._player1)
#     assert game_run._game._board.fields['00']._sign == game_run._game._player1._sign


def test_players_move():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields_sim
    game.players_move('0', '0', game._player1)
    assert not game._board.fields['00'].is_free
