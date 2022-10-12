
# **Hangman**

Hangman is a Python terminal game which runs in the Code Institute terminal on Heroku. 

Link to live site: [here](https://hangmanrachel.herokuapp.com/)
 
  ![This is an image](/assets/images/closeup.png)
 

## **How to Play**

This game is based on the classic pen and paper game. Lots of info can be found on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))
 
In this version:
* There are three options of levels to play:
    
      Easy contains words that are 4-6 letters long.
      
      Medium contains words that are 7-9 letters long.
        
      Hard contains words that are 10-14 letters long. 
* Once your difficulty is decided a  word is picked by your opponent (the computer).
* You must try to guess a given word one letter at a time.
* The word is displayed explaining how long the word is and by "_ ": an underscore with a space after to make it easier to read. 
  eg. "The word is a 5 letter word: word "Apple" = "_ _ _ _ _ "
* You have 7 body parts meaning you can only have 6 wrong answers or you will die.
* You can guess as many correct letters as needed 
* There is an option to get a clue - a "hail Mary" when you only have 2 body parts left. You can sacrifice the next body part in order to 
  reveal one letter in the word, but it means you can only answer correctly after that clue as the next wrong answer will kill you. 
* You have the option to play again one the game is over.
  
**Target Audience:**

Players of all ages are welcome as there are different difficulties to choose from. 
Players who enjoy a story while they play a game. 
People studying English

**User Stories:**

* As a user I can decide whether to read the rules or not.
* As a user I can choose different difficulties so I can challenge myself further when I am ready.
* As a user I can see if I have answered correctly/ incorrectly by the visual display as well as the text confirmation.
* As a user I can get a hint if I am near death.
* As a user I can follow a storyline as I play the game.
* As a user I can play again immediately if I win or die.


## Flowchart:

My initial game flowchart is found below. I have added some features and left others for future features as I developed the game.

 ![This is an image](/assets/images/flowchart.png)
 
##  **Features**

Existing Features

 Intro. 

 The user is welcomed to the game.

  ![This is an image](/assets/images/intro.png)

 Option to read rules: 

 User is offered whether they want to familiarize themselves with the rules of the game or get straight into it.
 
 YES answer 

  ![This is an image](/assets/images/rules_y.png)

  NO answer
 
  ![This is an image](/assets/images/rules_no.png)

User has options of how difficult the game is depending on their ability. 

 3 different levels to choose from:
 EASY, MEDIUM AND HARD

  ![This is an image](/assets/images/easy.png)
 ![This is an image](/assets/images/medium.png) 
 ![This is an image](/assets/images/hard.png)

 Interactive and unique display - Display changes with correct or incorrect answer.
 I created the display through trial and error with basic ascii inputs, wanting it to look
 different to ones that I had seen, and seem as ridiculous as possible with quite a heavy subject.

 Stages of man hangning:

  ![This is an image](/assets/images/stage_1.png)
 ![This is an image](/assets/images/stage_2.png)
 ![This is an image](/assets/images/stage_3.png)
 ![This is an image](/assets/images/stage_4.png)
 ![This is an image](/assets/images/stage_5.png)
 ![This is an image](/assets/images/stage_6.png)
 ![This is an image](/assets/images/stage_7.png)
 ![This is an image](/assets/images/stage_8.png)

 Correct letter display. User is told visually and verbally that they have chosen a correct letter.

 ![This is an image](/assets/images/correct_letter.png)

 Incorrect letter display. User is told visually and verbally that they have chosen a wrong answer.

 ![This is an image](/assets/images/wrong_letter.png)

 Option to get a hint : User can opt to get a hint by sacricing a part of themselves.
  Hint options shows

  ![This is an image](/assets/images/hail_mary_msg.png)

  Accept hint

 ![This is an image](/assets/images/hail_mary_yes.png)

  Deny hint

 ![This is an image](/assets/images/hail_mary_no.png)


 Storyline:
  I choose to add a little extra in a storyline and connect it up depending on what the outcome is. I think this will make progressing with future features even more entertaining. 

 Game win - follows the story

  ![This is an image](/assets/images/win.png)

 Loose Game - follows the story

  ![This is an image](/assets/images/loose.png)

 Option to play again: Yes

  ![This is an image](/assets/images/play_again_yes.png)

 Option to play again: No

 ![This is an image](/assets/images/play_again_no.png)

Future Features

* Make it personal - add username
* Create html and css display
* Option to show either available letters or used letters
* Add option to guess full word
* Add opening display, win and loose display 
* Remove repeated display when letter in in word more than once
* Separate out words that have multiple instances of one letter to add into different categories (eg move from hard to medium)

## TECHNOLOGIES USED: 

Python

## **Testing**
| Feature|  Expectation | Action |  Result |
|--|--|--|-- |
| Rules input:|
||
| Y | Prints rules to the screen and loads choose level input| Input y or Y| Rules are printed to the screen and choose level input is displayed |
| N | No rules are displayed, confirmation message prints to the screen and loads choose level input | Input n or N | No rules are displayed, confirmation message prints to the screen and loads choose level input|
| Invalid | Invalid answer message is displayed and user prompter to enter valid answer| input various characters other than y Y n or N | Invalid answer message is displayed and user prompter to enter valid answer|
|| 
| Choose difficulty input: |
| E for Easy | Users choice is confirmed. Words that are 4, 5 or 6 letters long are only chosen for this input of e or E  | Input e or E in multiple new games| Users choice is confirmed, Only words that are 4, 5 or 6 letters long are only chosen for this input of e or E
|M for Medium | Users choice is confirmed. Words that are 7, 8 or 9 letters long are only chosen for this input of m or M | Input m or M in multiple new games |Users choice is confirmed. Only words that are 7, 8 or 9 letters long are only chosen for this input of m or M
|H for Hard| Users choice is confirmed. Only words that are 10, 11 or 12, 13 or 14 letters long are only chosen for this input of h or H| Input h or H in multiple new games|Users choice is confirmed. Only words that are 10, 11 or 12, 13 or 14 letters long are only chosen for this input of h or H|
| Invalid | User is told of invalid answer and prompted to input valid answers | |Input various invalid keys multiple times | User is told of invalid answer and prompted to input valid answers| 
| Valid input | When difficulty is chosen, full game display appears, available letters and choose letter | Chose all difficulties | When difficulty is chosen, full game display appears, available letters and choose letter |
| Base display dependent on difficulty level | Base display is not disrupted by the length of text within | Coded a cheat to display each word length one at a time | Base display remains in a rectangle box no matter how many characters that are displayed (4 - 14 characters) |
||
| Choose letter input:|
||
| 1st time input | guessed letters list appears after the 1st letter input | Input valid letter for the first time in all levels | Guessed letters appears after the 1st letter input|
| All valid letter input | When a letter is chosen it is removed from available letters and added to guessed letters | Input correct and incorrect letters | All used letters are removed from available letters and added to guessed letters |
| Correct letter input: | If a letter is right the letter appears in the base of the game display replacing the relevant '_' at the correct index. The full word is displayed if guessed.| Input correct letters | the letter appears in the base of the game display replacing the relevant '_' at the correct index. The full word is displayed if guessed.
|| If a letter is right the man stays at the same stage | Input correct letters | Hanged man stays at the same stage |
| Incorrect letter input: | If a letter is wrong the man will be hanged piece by piece | Input multiple wrong letters | Display changes to show new body part of man added to the display for each wrong answer |
| Reused letter input | If a letter that has been used already is tried, a message shows telling the user they have used this letter previously, user is prompted to input a valid letter, available and guessed lists are printed again| Input letter that has been used already | A message appears telling the user they have used this letter previously, user is prompted to input a valid letter, available and guessed lists are printed again |
| Invalid letter inputs:| Inputting more than one letter at a time should not be allowed - an invalid input message should appear informing the user of such user is prompted to input a valid letter, available and guessed lists are printed again| Input multiple letters at a time | Letters cannot input two or more letters at a time is not possible. An invalid input message appears informing the user of such. User is prompted to input a valid letter, available and guessed lists are printed again|
||
| Hail Mary input: |
|| 
|Hail Mary Appearance| Once you only have 2 wrong answers left a warning appears offering you a Hail Mary deal | Played the game until I only had 2 wrong answers left | A warning appears offering a Hail Mary deal |
| Y | Inputting y or Y should print a message choosing a random valid letter from the word to the screen and sacrifices a part of your body in return, choose letter input is called | Input y and Y multiple times in different games | A message is printed to the screen with a random correct letter and sacrifices a part of your body in return, choose letter input is called
| N | Inputting n or N will print a message to screen and choose letter is called | Input n or N in different games | Inputting n or N prints a message to screen and choose letter is called|
| Hail Mary invalid input | Inputting a character that is not y, Y, n or N will trigger an invalid message prompting user to choose again
|Input multiple invalid characters in different games|An invalid message prompting user to choose again with the correct letters|
||
| Win | Game knows when player has won, word is fully completed in base, display story matches a win, play again message matches the winning narrative | Played the game until I won | Game knows when player has won, word is fully completed in base, display story matches a win, play again message matches the winning narrative|
| Loose | Game knows when player has lost, word is printed to the screen not the base, man has all parts hanged in display, play again message matches the loosing narrative | played game until I lost | Game knows when player has lost, word is printed to the screen not the base, man has all parts hanged in display, play again message matches the loosing narrative
||
| Play again inputs:|
| Y | Inputting y or Y will start the game again from difficulty choice | Inputted y or Y in this field | Game starts again from difficulty choice |
| N |Inputting n or N will end the game displaying a message "See you at the next hanging" | Inputted n or N into this field |"See you at the next hanging" is printed to the screen and the game ends |
| Invalid | Inputting a character that is not y, Y, n or N triggers an invalid answer response and user is prompted to input a valid answer | Input various invalid answers in multiple games | An invalid answer response and user is prompted to input a valid answer |

Invalid input testing:

  ![This is an image](/assets/images/invalid_rules.png)
 ![This is an image](/assets/images/invalid_difficulty.png)
 ![This is an image](/assets/images/invalid_input_letters.png)
 ![This is an image](/assets/images/hail_mary_invalid.png)
 ![This is an image](/assets/images/play_again_invalid.png)


## Bugs

**Solved Bugs**

1. Program was printing/returning multiple words (the ones that had 4 letters etc and then the valid one.)When coding a cheat to display the word. Properly indented the print statement to fix. 

1. Variables needed to be changed to global to access and word in play needed to be changed to capitals to recognise a correct answer
   > This was later changed to have variables passed as arguments

1. After guessing a letter you could add in a number or symbol and get the message that you already used that letter instead of knowing it was not a letter. I added a condition to make sure it was alpha and that it was not in available letters
 
1. choose_valid_word was messed up because I had 'and' statements instead of 'or'. Fixed the min and max of each length word also word area is not being completed immediately.

1. word_area delay in printing - moved order in start_game around so word area would automatically update when correct letter was guessed.

1. Adding for loops to all functions with input - welcome, get_clue and end_message and choose_level to ensure they loop until they get a valid answer

1. Remove print statement printing box twice on 8 letter words.

1. Unnumbered bug that was fixed during an earlier big clean up - my \ needed to be \\ in order to not break the lines in graphics as was creating new lines


**Remaining bugs**

 - No bugs remaining that I am aware of.

# Validator testing

 - Pep 8 no longer running.
 Aware that the words.py file is long.
![This is an image](/assets/images/testing.png) 
 

## **Deployment**

 - Fork or clone this repository.
 - Create a new Heroku app 
 - Add a config var with key Port and value 8000 
 - Set the buildbacks to Python and NodeJS in that order
 - Link the Heroku app to the repository
 - Click deploy.

## **Credits**

There were two main tutorials I followed along with a repo I used for comparison etc. I changed as much as possible throughout to make my game differ.

> Code Institute: The deployment terminal but I changed the size of the screen display for easier reading

> Using the latter as a base - this is how I got the list of words file and how to access words and choose words
> Using sets and random choice of word.
> * https://www.youtube.com/watch?v=m4nEnsavl6w&t=136s : Kite
> * https://www.youtube.com/watch?v=8ext9G7xspg&t=1876s : Free Code Camp (from 24.30 mins in)

> Random word list
> * https://www.randomlists.com/data/words.json 

> Repo:
> Used the code base on line 104 to find the index and corresponding placement or letters and printing the display to the terminal using tries.
> * https://github.com/Ryan-Martin22/hangman-2022/blob/main/run.py 

> Check if letter is valid
> * https://www.entechin.com/python-check-if-character-is-letter-in-string/#:~:text=using%20isalpha()%20method%20to,a%20letter%20otherwise%20returns%20false.

> Printing out the alphabet as available letters at first
> https://stackoverflow.com/questions/58960689/is-there-an-already-made-alphabet-list-in-python

> Converting the available letters into a more readable structure
> https://stackoverflow.com/questions/58820927/how-to-use-sort-for-set-values-in-python 

> Converting string to list:
> https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.

> 'if not' use:
> https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python

> Iterable code for replacing '_' with correct letter. I was stuck before this as I has not realised you needed to convert into iterable forms! (list and enumerate)
> https://stackoverflow.com/questions/41608600/enumerate-object-at-0x7f0211ea2360
> https://realpython.com/python-enumerate/

> My single \ in original drawing was causing loads of errors as well as finally breaking the picture - here I found I needed to change them to \\
> https://cplusplus.com/forum/beginner/100126/

> Getting the index of the guess letter and removing it from a str.
> https://thispointer.com/python-how-to-remove-characters-from-a-string-by-index/ 

> Finding the index of the guess 
> https://www.programiz.com/python-programming/methods/string/index 

> Random clue:
> https://pynative.com/python-random-choice/

> Splitting up long strings:
> https://stackoverflow.com/questions/48881196/how-can-i-split-up-a-long-f-string-in-python

## RESOURCES USED:

* Stack Overflow
* Google
* W3 Schools
* Mdn web docs
* YouTube
* Lucid - Flowcharts
* Github Projects

---
