from classes import Field, Board, Game, GameRun
from classes import InvalidSizeError, EvenSizeError, InvalidSignError
from classes import InvalidIsFreeTypeError, InvalidLetterError
from classes import InvalidNumberError, FieldDoesNotExistError
from classes import FieldIsTakenError, InvalidPlayersClassError
from classes import GameModeError
from classes import InvalidNameTypeError, EmptyNameError, MovingTypeError
from HeavyComputerPlayer import HeavyComputerPlayer
from RandomComputerPlayer import RandomComputerPlayer
from Human_Player import HumanPlayer
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
        '00': Field(0, 0), '01': Field(0, 1, False, 'X'),
        '02': Field(0, 2, False, 'X'),
        '03': Field(0, 3, False, 'X'), '04': Field(0, 4),

        '10': Field(1, 0, False, 'O'), '11': Field(1, 1, False, 'X'),
        '12': Field(1, 2, False, 'O'),
        '13': Field(1, 3, False, 'X'), '14': Field(1, 4, False, 'O'),

        '20': Field(2, 0, False, 'X'), '21': Field(2, 1, False, 'X'),
        '22': Field(2, 2),
        '23': Field(2, 3, False, 'X'), '24': Field(2, 4),

        '30': Field(3, 0, False, 'O'), '31': Field(3, 1),
        '32': Field(3, 2, False, 'O'),
        '33': Field(3, 3, False, 'X'), '34': Field(3, 4, False, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, False, 'X'),
        '42': Field(4, 2),
        '43': Field(4, 3, False, 'X'), '44': Field(4, 4, False, 'X')
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
        '00': Field(0, 0), '01': Field(0, 1, False, 'X'),
        '02': Field(0, 2, False, 'O'),
        '03': Field(0, 3, False, 'X'), '04': Field(0, 4),

        '10': Field(1, 0, False, 'O'), '11': Field(1, 1, False, 'X'),
        '12': Field(1, 2, False, 'O'),
        '13': Field(1, 3, False, 'X'), '14': Field(1, 4, False, 'O'),

        '20': Field(2, 0, False, 'X'), '21': Field(2, 1, False, 'X'),
        '22': Field(2, 2, False, 'O'),
        '23': Field(2, 3, False, 'X'), '24': Field(2, 4),

        '30': Field(3, 0, False, 'O'), '31': Field(3, 1, False, 'O'),
        '32': Field(3, 2, False, 'O'),
        '33': Field(3, 3, False, 'X'), '34': Field(3, 4, False, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, False, 'X'),
        '42': Field(4, 2),
        '43': Field(4, 3, False, 'X'), '44': Field(4, 4, False, 'X')
    }

test_fields5 = {
        '00': Field(0, 0), '01': Field(0, 1, False, 'X'),
        '02': Field(0, 2, False, 'O'),
        '03': Field(0, 3, False, 'X'), '04': Field(0, 4),

        '10': Field(1, 0, False, 'O'), '11': Field(1, 1, False, 'X'),
        '12': Field(1, 2, False, 'O'),
        '13': Field(1, 3, False, 'X'), '14': Field(1, 4, False, 'O'),

        '20': Field(2, 0, False, 'X'), '21': Field(2, 1, False, 'X'),
        '22': Field(2, 2, False, 'O'),
        '23': Field(2, 3, False, 'X'), '24': Field(2, 4, False, 'O'),

        '30': Field(3, 0, False, 'O'), '31': Field(3, 1, False, 'O'),
        '32': Field(3, 2, False, 'O'),
        '33': Field(3, 3, False, 'X'), '34': Field(3, 4, False, 'O'),

        '40': Field(4, 0), '41': Field(4, 1, False, 'X'),
        '42': Field(4, 2, False, 'X'),
        '43': Field(4, 3, False, 'X'), '44': Field(4, 4, False, 'X')
    }


def test_create_field():
    field = Field(0, 6)
    assert field._letter == 0
    assert field._number == 6
    assert field.is_free
    assert field._sign == '-'


def test_create_field_invalid_letter():
    with pytest.raises(InvalidLetterError):
        Field(75, 9)


def test_create_field_invalid_number():
    with pytest.raises(InvalidNumberError):
        Field(4, '')
    with pytest.raises(InvalidNumberError):
        Field(4, 12)


def test_create_field_invalid_sign():
    with pytest.raises(InvalidSignError):
        Field(5, 9, sign='U')


def test_create_field_invalid_is_free():
    with pytest.raises(InvalidIsFreeTypeError):
        Field(5, 9, 7)


def test__str__():
    field = Field(1, 7)
    assert str(field) == '-'
    field2 = Field(1, 1, sign='X')
    assert str(field2) == 'X'


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
    with pytest.raises(InvalidSignError):
        field.set_sign(7)


def test_create_board_normal():
    board = Board(5)
    for key in test_fields_sim.keys():
        assert test_fields_sim[key]._letter == board.fields[key]._letter
        assert test_fields_sim[key]._number == board.fields[key]._number
        assert test_fields_sim[key].is_free == board.fields[key].is_free
        assert test_fields_sim[key]._sign == board.fields[key]._sign
    assert board._size == 5


def test_create_board_size_even_number():
    with pytest.raises(EvenSizeError):
        Board(6)


def test_create_board_invalid_number():
    with pytest.raises(InvalidSizeError):
        Board(45)
    with pytest.raises(InvalidSizeError):
        Board(3)


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
    line = '   01234\n   OOOOO\nA X-X-X-X\nB XO-O-OX\nC X-X-X-X\n'
    line += 'D XO-O-OX\nE X-X-X-X\n   OOOOO'
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
    player3 = ('Human', 'Kasia', "X", 'up-down')
    player4 = ('6', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidPlayersClassError):
        Game(player3, player4, 5)


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


def test_create_game_invalid_sign():
    player1 = ('Human', 'Kasia', "T", 'up-dow')
    player2 = ('Human', 'Ann', "O", 'left-right')
    with pytest.raises(InvalidSignError):
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
    msg = 'X'
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
    msg = 'O'
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


def test_if_game_ended_left_right():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('Human', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields2
    msg = 'X'
    assert game.if_game_ended_left_right('X') == msg
    test_fields2['44']._sign = '-'
    assert not game.if_game_ended_left_right('X')
    test_fields2['44']._sign = 'O'
    assert not game.if_game_ended_left_right('X')


def test_if_game_ended_up_down():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields3
    msg = 'O'
    assert game.if_game_ended_up_down('O') == msg
    test_fields3['42']._sign = '-'
    assert not game.if_game_ended_up_down('O')
    test_fields2['42']._sign = 'X'
    assert not game.if_game_ended_up_down('O')


def test_player_move_HumanPlayer():
    player1 = ('Human', 'Kasia', "O", 'up-down')
    player2 = ('Human', 'Ann', "X", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields_sim
    game.player_move(game._player1, 0, 0)
    assert game._board.fields['00']._sign == "O"
    assert not game._board.fields['00'].is_free


def test_player_move_HeavyComputerPlayer_field_free():
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('3', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields4
    game.player_move(game._player2, 2, 4)
    assert game._board.fields['24']._sign == "O"
    assert not game._board.fields['24'].is_free


def give00(self, previous_letter, previous_numer, fields):
    return (0, 0)


def test_player_move_HeavyComputerPlayer_field_taken(monkeypatch):
    player1 = ('Human', 'Kasia', "X", 'up-down')
    player2 = ('3', 'Ann', "O", 'left-right')
    game = Game(player1, player2, 5)
    game._board.fields = test_fields5
    monkeypatch.setattr(HeavyComputerPlayer, 'give_letter_number', give00)
    game.player_move(game._player2, 1, 1, 2, 2)
    assert game._board.fields['22']._sign == "O"
    assert not game._board.fields['22'].is_free


def test_create_game_run():
    game_run = GameRun('Human', 5, "Kasia", "Computer")
    assert game_run._player1 == ('Human', "Kasia", 'X', 'left-right')
    assert game_run._player2 == ('Human', "Computer", 'O', 'up-down')
    assert game_run._game_mode == 'Human'
    line = '   01234\n   OOOOO\nA X-X-X-X\nB XO-O-OX\n'
    line += 'C X-X-X-X\nD XO-O-OX\nE X-X-X-X\n   OOOOO'
    assert str(game_run._game._board) == line


def test_create_game_run_GameModeError():
    with pytest.raises(GameModeError):
        GameRun(9, 7, 'Kasia', 'Player 2')


def test_create_game_run_InvalidSizeError():
    with pytest.raises(InvalidSizeError):
        GameRun('2', 99, 'Kasia', 'Player 2')


def test_create_game_run_InvalidNameTypeError():
    with pytest.raises(InvalidNameTypeError):
        GameRun('3', 7, 8, 'Player 2')


def test_create_game_run_EmptyNameError():
    with pytest.raises(EmptyNameError):
        GameRun('3', 7, '', 'Player 2')


def give44(arg, a='', b='', c='', d=''):
    return (4, 4)


def test_run_game_X_wins(monkeypatch):
    game_run = GameRun("2", 5, "Kasia", "Ola")
    test_fields2['44'].set_sign('-')
    test_fields2['44'].is_free = True
    game_run._game._board.fields = test_fields2
    monkeypatch.setattr(HumanPlayer, 'give_letter_number', give44)
    assert game_run.run_game() == 'Kasia'


def give43(self):
    return (4, 3)


def test_run_game_O_wins(monkeypatch):
    game_run = GameRun("2", 5, "Kasia", "Ola")
    test_fields3['43'].set_sign('-')
    test_fields3['43'].is_free = True
    game_run._game._board.fields = test_fields3
    monkeypatch.setattr(HumanPlayer, 'give_letter_number', give44)
    monkeypatch.setattr(RandomComputerPlayer, 'give_letter_number', give43)
    assert game_run.run_game() == 'Computer Player'


def test_player1_turn(monkeypatch):
    game_run = GameRun('2', 5, 'name')
    game_run._game._board.fields = test_fields_sim
    monkeypatch.setattr(HumanPlayer, 'give_letter_number', give44)
    tuple = game_run.player1_turn()
    assert game_run._game._board.fields['44']._sign == 'X'
    assert not game_run._game._board.fields['44'].is_free
    assert not game_run.result_of_game
    assert tuple == (4, 4)


def test_player1_turn_end(monkeypatch):
    game_run = GameRun('2', 5, 'name')
    game_run._game._board.fields = test_fields2
    test_fields2['44']._sign = '-'
    test_fields2['44'].is_free = True
    monkeypatch.setattr(HumanPlayer, 'give_letter_number', give44)
    tuple = game_run.player1_turn()
    assert game_run._game._board.fields['44']._sign == 'X'
    assert not game_run._game._board.fields['44'].is_free
    assert game_run.result_of_game
    assert tuple == (4, 4)


def test_player2_turn_hevy(monkeypatch):
    game_run = GameRun('3', 5, 'name')
    monkeypatch.setattr(HeavyComputerPlayer, 'give_letter_number', give44)
    game_run.player2_turn_heavy(4, 2)
    assert game_run._game._board.fields['44']._sign == 'O'
    assert not game_run._game._board.fields['44'].is_free
    assert not game_run.result_of_game


def give42(arg, b='', c='', d=''):
    return (4, 2)


def test_player2_turn_end_heavy(monkeypatch):
    game_run = GameRun('3', 5, 'name')
    test_fields3['42']._sign = '-'
    test_fields3['42'].is_free = True
    game_run._game._board.fields = test_fields3
    monkeypatch.setattr(HeavyComputerPlayer, 'give_letter_number', give42)
    game_run.player2_turn_heavy(4, 4)
    assert game_run._game._board.fields['42']._sign == 'O'
    assert not game_run._game._board.fields['42'].is_free
    assert game_run.result_of_game


def test_player2_turn_human_random(monkeypatch):
    game_run = GameRun('2', 5, 'pl_nam')
    monkeypatch.setattr(RandomComputerPlayer, 'give_letter_number', give44)
    game_run.player2_turn_human_random()
    assert game_run._game._board.fields['44']._sign == 'O'
    assert not game_run._game._board.fields['44'].is_free
    assert not game_run.result_of_game


def test_player2_turn_end_human_random(monkeypatch):
    game_run = GameRun('2', 5, 'name')
    test_fields3['42']._sign = '-'
    test_fields3['42'].is_free = True
    game_run._game._board.fields = test_fields3
    monkeypatch.setattr(RandomComputerPlayer, 'give_letter_number', give42)
    game_run.player2_turn_human_random()
    assert game_run._game._board.fields['42']._sign == 'O'
    assert not game_run._game._board.fields['42'].is_free
    assert game_run.result_of_game