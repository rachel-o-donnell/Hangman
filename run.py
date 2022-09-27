# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

def choose_valid_word(words):
    """ 
    Eliminates words that are less than 6 characters long, have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    word_in_play = random.choice(words)
    while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 6:
         word_in_play = random.choice(words)
    print(word_in_play)     

def start_game():
    """
    Prints opening message to the terminal, asks player to input a letter,
    checks that the answer is a letter and returns this chosen letter
    """
    print("Welcome to Hangman, you have 7 tries to guess the correct letters or you will be hanged\n")
    print (f"These are the available letters:\n {available_letters}\n")
    chosen_letter = input("Choose a letter: ").upper()
    if chosen_letter.isalpha():
        print (f"You chose letter {chosen_letter}")
    else: 
        print("Invalid answer, you must choose a letter\n")
    return chosen_letter
    


available_letters = sorted(set(string.ascii_uppercase))
used_letters = set()
lives = 7 
guessing_area = ''


start_game()
choose_valid_word(words)
