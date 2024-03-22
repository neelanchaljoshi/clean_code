import pytest
from ...exam.hangman import HangmanGame, Database
import os


def test_load_words_from_file(mocker):
    db = Database(path = os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    assert db.load_words_from_file() == ['happy\n', 'sad\n', 'hehehe\n']

def test_choose_random_word(mocker):
    db = Database(path = os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('random.choice', return_value='happy')
    db.choose_random_word()
    assert db.chosen_word == 'happy'

def test_start_game_printing(mocker):
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    printer = mocker.patch('builtins.print')
    game.start_game()
    printer.assert_any_call("Welcome to Hangman!")

def test_input_from_user(mocker):
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='a')
    game.get_input_from_user()
    assert game.user_input == 'A'

