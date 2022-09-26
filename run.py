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

def start_game():
    print("Welcome to Hangman, you have 7 tries to guess the correct letters or you will be hanged\n")
    print (f"These are the available letters: {available_letters}\n")
    input("Choose a letter ")
    
    return(word_in_play)



available_letters = sorted(set(string.ascii_uppercase))
used_letters = set()
lives = 7 
guessing_area = ''

start_game()
word = choose_valid_word(words)
identify_letter()
