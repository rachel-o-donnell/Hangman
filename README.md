![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome rachel-o-donnell,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

bug 1:
program was printing/returning multiple words (the ones that had 4 letters etc and Then the last one.) Properly indented te print statement to fix. 

bug 2 : variables needed to be changed to global to access and word in play needed to be changed to capitals to recognise a correct ans


bug 3: After guessing a letter you could add in a number or symbol and get the message that you already used that letter instead of knowing it was not a letter. 
I added a condition to make sure it was alpha and that it was not in available letters

bug that was fixed during a big clean up - my \ neaded to be \\ in order to not break the lines in graphics.

bug 5: 
choose_valid_word was messed up because I had and statements instead of or. Fixed the min and max of each length word also
word area is not being completed immediately.

bug 6: word_area delay in printing - moved order in start_game around so word area would update before being printed.


figuring out how to connect the words inside the base of the display was lengthy!

if you input the and invalid y/n at rules a 2nd time it 


credit
https://thispointer.com/python-how-to-remove-characters-from-a-string-by-index/ getting the index of the guess letter and removing it from a string