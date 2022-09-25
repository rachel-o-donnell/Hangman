# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words

def choose_valid_word(words):
    """ 
    Eliminates words that are less than 6 characters long, have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    word_in_play = random.choice(words)
    while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 6:
         word_in_play = random.choice(words)
    print(word_in_play)



choose_valid_word(words)