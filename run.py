import random
import string
from words import words


def get_word(level):
    """
    Eliminates words that are less than 6 characters long,
    have spaces or have hyphens
    Randomly chooses a word for our game.
    """
    word_in_play = random.choice(words).upper()
    if level != 'Easy':
        print(f"You have chosen a {level} level")
        if level == 'Medium':
            while len(word_in_play) < 7 or len(word_in_play) > 9:
                word_in_play = random.choice(words).upper()
            print(word_in_play)
        else:
            while len(word_in_play) < 10 or len(word_in_play) > 14:
                word_in_play = random.choice(words).upper()
            print(word_in_play)
    else:
        print(f" You have chosen an {level} level")
    if level == 'Easy':
        while len(word_in_play) < 4 or len(word_in_play) > 6:
            word_in_play = random.choice(words).upper()
    return word_in_play


def welcome():
    """
    Prints opening message to the terminal and prints the rules of the game
    if the player chooses to see them
    """
    print(' Welcome to your scheduled hanging. \n\n'
          ' If the fates allow, you can save yourself from certain death.\n')
    answer = input(' Would you like to know the rules? Y/N ').upper()
    if answer == 'Y':
        rules = (
                '\n  Hangman is a game where you try to guess a given word '
                'one letter at a time. \n  If your answer is wrong you will be'
                ' hanged piece by piece.\n\n  Your body will be hanged in 7 '
                'parts, so you can only have 6 wrong answers or you will die. '
                '\n  You can guess as many correct letters as needed to be '
                'saved. \n\n  There are 3 different levels : \n  '
                'Easy contains words that are 4-6 letters long \n  '
                'Medium contains words that are 7-9 letters long \n  '
                'Hard contains words that are 10-14 letters long \n  '
            )
        print(rules)
    elif answer == 'N':
        print('\n  Ok, crowd are getting impatient anyways \n')
    else:
        print('\n  Invalid answer, you must type either Y or N')
        input(' Do you need to know the rules? Y/N ')


def choose_level():
    """
    Asks player to choose a difficulty setting
    """
    chosen_level = ''
    print(" Choose your difficulty: \n")
    level = input(' Enter (E)asy, (M)edium or (H)ard ').upper()
    if level == 'E':
        chosen_level = "Easy"
    elif level == 'M':
        chosen_level = "Medium"
    elif level == 'H':
        chosen_level = "Hard"
    else:
        print(" \n Invalid input, "
              "you must enter e for Easy, m for Medium or h for Hard \n")
        level = input(' Enter (E)asy, (M)edium or (H)ard ')
    return chosen_level


def start_game(word):
    """
    asks player to input a letter,
    checks that the answer is a valid guess buy ensuring it is a letter,
    is in the available letters list,
    and whether it is a correct or incorrect guess
    """
    guessed = set()
    tries = 7
    guessed_word = False
    word_spaced = ' '.join(word)
    word_area = '_ ' * len(word)
    print(game_display(tries))
    base(word, word_area)
    alphabet = sorted(set(string.ascii_uppercase))
    available = ' '.join(alphabet)
    print(f" Available letters:\n\n {available}\n")
    print(word)
    while tries > 0 and not guessed_word:
        if tries == 2:
            get_clue(word, guessed, tries, word, word_area)
            tries = tries - 1
        if guessed:
            print(f" Remaining letters: {available}\n")
            print(' Guessed letters:', ' '.join(sorted(guessed)))
        guess = input("\n Choose a letter: ").upper()
        if guess.isalpha() and guess in available:
            ind = available.index(guess)
            if len(available) > ind:
                available = available[0: ind:] + available[ind + 1::]
            guessed.add(guess)
            if guess in word:
                print(word_spaced)
                word_area_list = list(word_area)
                index_of_correct_letter = [i for i,
                                           letter in enumerate(word_spaced)
                                           if letter == guess]
                for i in index_of_correct_letter:
                    print(game_display(tries))
                    base(word, word_area)
                    word_area_list[i] = guess
                    word_area = "".join(word_area_list)
                    print(word_area)
                print(f"\n Phew! You guessed correctly with the letter "
                      f"{guess}\n")
                if '_' not in word_area:
                    guessed_word = True
            elif guess not in word:
                tries = tries - 1
                print(game_display(tries))
                base(word, word_area)
                if tries != 0:
                    print(f"\n Oh no! You have lost this guess with the letter"
                          f" {guess}\n")
                    print(f" You have {tries} remaining wrong guesses before "
                          "your demise.\n")
                if tries == 0:
                    print(' Whelp! The crowd is satiated from a suspensful '
                          'hanging. \n'
                          ' The only part of your body with any life left '
                          'is your curly locks blowing in the wind.\n')
                    end_message()
        elif guess.isalpha() and guess not in available:
            print(f"\n You have already used {guess} \n")
        else:
            print("\n  Invalid answer, you must choose a letter\n")
            print(f" The remaining letters are: {available}\n")
    if guessed_word:
        print('\n You survived! The crowd has been mesmerised by your curly'
              ' bufont and are cheering for more.\n\n You have been '
              'approached to star on the front cover of "Hangings Monthly" and'
              ' offered \n a sponsorship deal with "Cauldron Curls '
              '- curls so defined it must be witchcraft". \n\n'
              ' It pays well but will surely draw more attention, and another'
              ' date with the gallows.\n\n')
        end_message()
    return word_area


def get_clue(available, guessed, tries, word, word_area):
    '''
    gives clue
    itterate through wrod area until if finds a '_' - checks this
     against word and reveals the letter.
        removes from available letters and prints hail mary
        tries + 1
    '''
    hail_mary = input(' !!! WARNING !!! \n '
                      'You are gangerously close to death. \n '
                      'You can sacrifice the next part of yourself to reveal'
                      ' one letter \n Do you want a hail mary? Y/N ').upper()
    print(hail_mary)
    if hail_mary == 'Y':
        tries = tries - 1
        random_clue = random.choice(available)
        while random_clue not in word or random_clue in guessed:
            random_clue = random.choice(available)
        print(game_display(tries))
        base(word, word_area)
        print(f" \n Here is a letter in the word '{random_clue}'\n")
    elif hail_mary == 'N':
        print(" \n Ok, it's your life. \n")
    else:
        print('\n  Invalid answer, you must type either Y or N \n')
        input('Do you want a hail Mary? Y/N ')


def end_message():
    """
    Gives player the option to play again or not
    """
    play_again = input(' Take the deal and risk your life again? Y/N ').upper()
    if play_again == 'Y':
        start_game(get_word(choose_level()))
    elif play_again == 'N':
        print('\n See you at the next hanging!')
    else:
        print(" Invalid answer, you must answer 'y' for yes or 'n' for no /n")
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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |""",

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
                        | ______________________________________
                        |/                                     /|
                        /____________________________________ / |
                       |                                     |  |"""]
    return hangman_stage[tries]


def base(word, word_area):
    '''
    Prints the base box of the game display with the details of the word
    and word area without disrupting the size of the box container no matter
    the length of the word
    '''
    if len(word) == 4:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |             Word: {word_area}          | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 5:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |           Word: {word_area}          | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 6:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |           word: {word_area}        | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 7:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |         Word: {word_area}        | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 8:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |         word: {word_area}      | /
                       |_____________________________________|/
                       \n""")
        print(box)
    elif len(word) == 9:
        box = (f"""                       |      The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |        Word: {word_area}     | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 10:
        box = (f"""                       |     The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |       Word: {word_area}    | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 11:
        box = (f"""                       |     The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |      Word: {word_area}   | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 12:
        box = (f"""                       |     The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |     Word: {word_area}  | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 13:
        box = (f"""                       |     The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |    Word: {word_area} | /
                       |_____________________________________|/
                       \n""")
    elif len(word) == 14:
        box = (f"""                       |     The word is"""
               f""" {len(word)} letters long     |  |
                       |                                     |  |
                       |  Word: {word_area} | /
                       |_____________________________________|/
                       \n""")
    print(box)


def main():
    """
    All functions
    """
    welcome()
    start_game(get_word(choose_level()))


main()
