import pytest
from ...exam.hangman import HangmanGame, Database
import os


def test_load_words_from_file():
    db = Database(path = os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    assert db.load_words_from_file() == ['happy\n', 'sad\n', 'hehehe\n']

def test_choose_random_word(mocker):
    db = Database(path = os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('random.choice', return_value='happy')
    db.choose_random_word()
    assert db.chosen_word == 'happy'

def test_start_game_printing(mocker):
    printer = mocker.patch('builtins.print')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    game.start_game()
    printer.assert_any_call("Welcome to Hangman!")

def test_initialization_game(mocker):
    mocker.patch('random.choice', return_value='happy')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    assert game.word == 'HAPPY'
    assert game.max_mistakes == 12
    assert game.mistakes == 0
    assert game.guessed_letters == set()
    assert game.unguessed_letters == {'H', 'A', 'P', 'Y'}
    assert game.current_guess == ['_', '_', '_', '_', '_']
    assert game.user_input == None

def test_input_from_user(mocker):
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='h')
    game.get_input_from_user()
    assert game.user_input == 'H'

def test_if_input_is_singular(mocker):
    mocker.patch('builtins.input', return_value='hdkjwhkjdh')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    game.get_input_from_user()
    assert not game.check_if_input_is_valid()

def test_if_input_is_alpha(mocker):
    mocker.patch('builtins.input', return_value='1####')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    game.get_input_from_user()
    assert not game.check_if_input_is_valid()

def test_if_letter_already_guessed(mocker):
    mocker.patch('random.choice', return_value='happy')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='h')
    game.get_input_from_user()
    game.check_if_letter_is_present_in_word()
    assert game.check_if_letter_is_already_guessed()

def test_mistake_updation(mocker):
    mocker.patch('random.choice', return_value='wonderful')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='z')
    game.get_input_from_user()
    game.update_game_state()
    assert game.mistakes == 1


def test_if_letter_not_present_in_word(mocker):
    mocker.patch('random.choice', return_value='bonus')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='z')
    game.get_input_from_user()
    game.update_game_state()
    assert not game.check_if_letter_is_present_in_word()
    assert game.mistakes == 1
    assert game.current_guess == ['_', '_', '_', '_', '_']

def test_if_letter_present_in_word(mocker):
    mocker.patch('random.choice', return_value='tesseract')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', return_value='t')
    game.get_input_from_user()
    assert game.user_input == 'T'
    game.update_game_state()
    assert game.current_guess == ['T', '_', '_', '_', '_', '_', '_', '_', 'T']

def test_short_game_run(mocker):
    mocker.patch('random.choice', return_value='abs')
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__), 'test_words.txt'))
    mocker.patch('builtins.input', side_effect=['a', 'b', 'c', 's'])
    game.play_game()
    assert game.mistakes == 1
