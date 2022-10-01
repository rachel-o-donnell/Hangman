# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string


def choose_valid_word():
    """
    Eliminates words that are less than 6 characters long,
    have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    word_in_play = random.choice(words).upper()
    while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 6:
        word_in_play = random.choice(words).upper()
    print(word_in_play)
    return word_in_play


def welcome():
    """
    Prints opening message to the terminal
    """
    global available_letters
    available_letters = sorted(set(string.ascii_uppercase))
    welcome_msg = (
        "Welcome to Hangman, you have 7 tries to guess "
        "the correct letters or you will be hanged\n"
        )
    print(welcome_msg)
    print(f"These are the available letters:\n {available_letters}\n")


def start_game(word):
    """
    asks player to input a letter,
    checks that the answer is a valid guess buy ensuring it is a letter,
    is in the available letters list,
    and whether it is a correct or incorrect guess
    """
    used_letters = set()
    tries = 7
    guessed_word = False
    word_area = '_' * len(word)
    print(game_display(tries))
    while tries > 0 and not guessed_word:
        print(f"The word is {len(word)} letters long: \n {word_area}")
        chosen_letter = input("Choose a letter: ").upper()
        if chosen_letter.isalpha() and chosen_letter in available_letters:
            available_letters.remove(chosen_letter)
            if chosen_letter in word:
                word_area_list = list(word_area)
                index_of_correct_letter = [i for i,
                                           letter in enumerate(word)
                                           if letter == chosen_letter]
                for i in index_of_correct_letter:
                    word_area_list[i] = chosen_letter
                    word_area = "".join(word_area_list)
                    print(word_area)
                print(f"You guessed correctly with the letter "
                      f"{chosen_letter}\n")
                print(f"The remaining letters are: {available_letters}")
                if '_' not in word_area:
                    guessed_word = True
            elif chosen_letter not in word:
                tries = tries - 1
                print(f"Oh no! You have lost this guess with the letter "
                      f"{chosen_letter}\n")
                print(game_display(tries))
                print(f"you have {tries} remaining")
                print(f"The remaining letters are: {available_letters}")
                print(word_area)
                if tries == 0:
                    print("Oh no! The man has been hanged.")
        elif chosen_letter.isalpha() and chosen_letter not in available_letters:
            print(f"You have already used {chosen_letter}")
        else:
            print("Invalid answer, you must choose a letter\n")
    if guessed_word:
        print('You win!')


def game_display(tries):
    """
    displays the visuals of the game to the player
    """
    hangman_stage = ["""
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |             %",     @@|@@     ,"%
                        |                \\      |      /
                        |                 \\     |     /
                        |                  \\____|____/
                        |                       |
                        |                       |
                        |                       |
                        |                     __|__
                        |                    /     \\
                        |                   /       \\
                        |                  /         \\
                        |                 |          |
                        |                 \\         /
                        |                  \\       /
                        |                   \\     /
                        |                 %=/      \\=%
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,
                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |             %",     @@|@@     ,"%
                        |                \\      |      /
                        |                 \\     |     /
                        |                  \\____|____/
                        |                       |
                        |                       |
                        |                       |
                        |                     __|__
                        |                    /
                        |                   /
                        |                  /
                        |                 |
                        |                 \\
                        |                  \\
                        |                   \\
                        |                 %=/
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |             %",     @@|@@     ,"%
                        |                \\      |      /
                        |                 \\     |     /
                        |                  \\____|____/
                        |                       |
                        |                       |
                        |                       |
                        |                       |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |             %",     @@|@@     ,"%
                        |                \\      |      /
                        |                 \\     |     /
                        |                  \\____|____/
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |             %",     @@|@@
                        |                \\      |
                        |                 \\     |
                        |                  \\____|
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |                     @@|@@
                        |                       |
                        |                       |
                        |                       |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /                    @@@~
                        |/                   @@@@@@@@___
                        |                  @| x  x |@@@~~
                        |                  @|__~___|@~~~
                        |                     @@|@@
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """,

                     """
                         ________________________
                        |   /                   |
                        |  /                    |
                        | /
                        |/
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        | ____________________________________
                        |/                                   /|
                        /___________________________________/ |
                       |                                   | /
                       |___________________________________|/
                       """]

    return hangman_stage[tries]


welcome()
start_game(choose_valid_word())
