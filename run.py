# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

def choose_valid_word(words):
    """ 
    Eliminates words that are less than 6 characters long, have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    available_letters = string.ascii_uppercase
    word_in_play = random.choice(words)
    while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 6:
         word_in_play = random.choice(words)
    print (f"These are the available letters: {available_letters}")
    input("Choose a letter\n")
    
    print(word_in_play)


letters_in_word_in_play = ''
used_letters = ''
lives = 7 
guessing_area = ''

choose_valid_word(words)

