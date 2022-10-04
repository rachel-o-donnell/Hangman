# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import string
from words import words


def choose_valid_word(level):
    """
    Eliminates words that are less than 6 characters long,
    have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    word_in_play = random.choice(words).upper()
    if level != 'Easy':
        print(f"You have chosen a {level} level")
        if level == 'Medium':
            while '-' in word_in_play or len(word_in_play) > 8 or len(word_in_play) < 5:
                word_in_play = random.choice(words).upper()
            print(word_in_play)
        else:
            while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) < 9:
                word_in_play = random.choice(words).upper()
            print(word_in_play)
    else:
        print(f"You have chosen an {level} level")
    if level == 'Easy':
        while ' ' in word_in_play or '-' in word_in_play or len(word_in_play) > 5:
            word_in_play = random.choice(words).upper()
        print(word_in_play)
    return word_in_play


def welcome():
    """
    Prints opening message to the terminal
    """
    welcome_msg = (
        "Welcome to Hangman, you have 7 tries to guess "
        "the correct letters or you will be hanged\n"
    )
    print(welcome_msg)


def choose_level():
    """
    Asks player to choose a difficulty setting
    """
    chosen_level = ''
    print("Choose your difficulty: \n")
    level = input('Enter e for Easy, m for Medium or h for Hard ').upper()
    if level == 'E':
        chosen_level = "Easy"
    elif level == 'M':
        chosen_level = "Medium"
    elif level == 'H':
        chosen_level = "Hard"
    else:
        print(" \n Invalid input, "
              "you must enter e for Easy, m for Medium or h for Hard \n")
        level = input('Enter e for Easy, m for Medium or h for Hard ')
    return chosen_level


def start_game(word):
    """
    asks player to input a letter,
    checks that the answer is a valid guess buy ensuring it is a letter,
    is in the available letters list,
    and whether it is a correct or incorrect guess
    """
    guessed_letters = set()
    tries = 7
    guessed_word = False
    word_area = '_ ' * len(word)
    print(game_display(tries))
    available_letters = sorted(set(string.ascii_uppercase))
    print(f"These are the available letters:\n {available_letters}\n")
    while tries > 0 and not guessed_word:
        print(f"The word is {len(word)} letters long: \n\n {word_area}\n")
        if guessed_letters:
            print(f"The remaining letters are: {available_letters}\n")
            print('Your guessed letters:', ' '.join(sorted(guessed_letters)))
        chosen_letter = input("\nChoose a letter: ").upper()
        if chosen_letter.isalpha() and chosen_letter in available_letters:
            available_letters.remove(chosen_letter)
            guessed_letters.add(chosen_letter)
            if chosen_letter in word:
                word_spaced = ' '.join(word)
                print(word_spaced)
                word_area_list = list(word_area)
                index_of_correct_letter = [i for i,
                                           letter in enumerate(word_spaced)
                                           if letter == chosen_letter]
                for i in index_of_correct_letter:
                    print(game_display(tries))
                    word_area_list[i] = chosen_letter
                    word_area = "".join(word_area_list)
                    print(word_area)
                print(f"\nYou guessed correctly with the letter "
                      f"{chosen_letter}\n")
                if '_' not in word_area:
                    guessed_word = True
            elif chosen_letter not in word:
                tries = tries - 1
                print(game_display(tries))
                print(f"\nOh no! You have lost this guess with the letter "
                      f"{chosen_letter}\n")
                print(f"You have {tries} remaining guesses \n")
                if tries == 0:
                    print("Oh no! The man has been hanged.")
        elif chosen_letter.isalpha() and chosen_letter not in available_letters:
            print(f"You have already used {chosen_letter} \n")
            print(f"The remaining letters are: {available_letters}\n")
        else:
            print("\n Invalid answer, you must choose a letter\n")
            print(f"The remaining letters are: {available_letters}\n")
    if guessed_word:
        print('\n You win! \n')


def end_message():
    """
    Gives player the option to play again or not
    """
    play_again = input('Ready to play again? Y/N').upper()
    if play_again == 'Y':
        start_game(choose_valid_word(choose_level()))
    elif play_again == 'N':
        print('See you at the next hanging')
    else:
        print("Invalid answer, you must answer 'y' for yes or 'n' for no /n")
        print(play_again)


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
                       \n
                       \n
                       """]

    return hangman_stage[tries]

def main():
    """ 
    All functions
    """
    welcome()
    start_game(choose_valid_word(choose_level()))
    end_message()


main()