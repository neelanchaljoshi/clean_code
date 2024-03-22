"""
Entry point for the hangman game.

Run the game from the command line with
    python -m exam.hangman

Depending on your installation, you might need
to call python3 instead of python.
"""

import random
import os

class Database:
    def __init__(self, path = None):
        self.path = path
        self.chosen_word = None

    def load_words_from_file(self):
        with open(self.path, 'r') as file:
            return file.readlines()
    
    def choose_random_word(self):
        words = self.load_words_from_file()
        self.chosen_word = random.choice(words).strip()
        return self.chosen_word

class HangmanGame:
    def __init__(self, max_mistakes=12, path_to_database = None):
        self.word = Database(path_to_database).choose_random_word().upper()
        self.max_mistakes = max_mistakes
        self.mistakes = 0
        self.guessed_letters = set()
        self.unguessed_letters = set(self.word) if self.word else set()
        self.current_guess = ['_'] * len(self.word) if self.word else []
        self.user_input = None

    def start_game(self):
        print("Welcome to Hangman!")
        print("The word has {} letters.".format(len(self.word)))
        print("You can make {} mistakes.".format(self.max_mistakes))

    
    def get_input_from_user(self):
        self.user_input = input("Please enter your guess: ").upper()
    
    def check_if_input_is_valid(self):
        if len(self.user_input) != 1:
            print("Please enter only one letter.")
            return False
        if not self.user_input.isalpha():
            print("Please enter a letter.")
            return False
        return True
    
    def check_if_letter_is_already_guessed(self):
        if self.user_input in self.guessed_letters:
            print("You have already guessed this letter.")
            return True
        return False
    
    def check_if_letter_is_present_in_word(self):
        self.guessed_letters.add(self.user_input)
        if self.user_input in self.unguessed_letters:
            self.unguessed_letters.remove(self.user_input)
            return True
        return False
    
    
    def update_game_state(self):
        if not self.check_if_letter_is_present_in_word():
            self.mistakes += 1
        else:
            for i, letter in enumerate(self.word):
                if letter == self.user_input:
                    self.current_guess[i] = letter
    
    def print_current_status(self):
        print("You have {} mistakes remaining".format(self.max_mistakes - self.mistakes))
        print("Current status is {}\n".format(''.join(self.current_guess)))

    def play_game(self):
        self.start_game()
        while self.mistakes < self.max_mistakes:
            self.get_input_from_user()
            if not self.check_if_input_is_valid():
                self.print_current_status()
                continue
            if self.check_if_letter_is_already_guessed():
                self.print_current_status()
                continue
            self.update_game_state()
            self.print_current_status()
            if not self.unguessed_letters:
                print("You are a master of the English Language. You guessed the word correctly.")
                break
        else:
            print("You are a loser. So dumb. The word was {}".format(self.word))
    



if __name__ == '__main__':
    game = HangmanGame(path_to_database=os.path.join(os.path.dirname(__file__),"..", "resources","words.txt"))
    game.play_game()

    



