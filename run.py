# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

def choose_valid_word(words):
    """ 
    Eliminates words that are less than 6 characters long, have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    global word_in_play
    word_in_play = random.choice(words).upper()
    while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 6:
         word_in_play = random.choice(words).upper()
    print(word_in_play)     

def welcome():
    
    """
    Prints opening message to the terminal
    """
    print("Welcome to Hangman, you have 7 tries to guess the correct letters or you will be hanged\n")
    print (f"These are the available letters:\n {available_letters}\n")

def start_game():
    """
    asks player to input a letter,
    checks that the answer is a valid guess buy ensuring it is a letter,
    is in the available letters list,
    and whether it is a correct or incorrect guess
    """ 
    tries = 7
    while tries > 0:
        global chosen_letter
        chosen_letter = input("Choose a letter: ").upper()
        if chosen_letter.isalpha() and chosen_letter in available_letters:
            available_letters.remove(chosen_letter)
            if chosen_letter in word_in_play:
                print(f"You guessed correctly with the letter {chosen_letter}")
                
            elif chosen_letter not in word_in_play:
                tries = tries -1
                print(f"Oh no! You have lost this guess with the letter {chosen_letter}\n") 
                print(f"you have {tries} remaining")
                   
        else: 
            print("Invalid answer, you must choose a letter\n")
        
   
       
    

available_letters = sorted(set(string.ascii_uppercase))
used_letters = set()

guessing_area = ''

welcome()
choose_valid_word(words)
start_game()

