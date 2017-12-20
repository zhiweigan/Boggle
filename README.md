# Boggle
Made by the BoggleBuddies

This program allows the user to play Boggle with the computer at three different difficulty levels.

## Grid Class - Connie

### Variables
16 die
4 lines
Possible Words

### Methods
1. Make Board
	* Choose a random letter from each die's array of letters
	* Print die letters in 4 rows

2. Find all Possible Words
	* Import json file containing a dictionary of possible words
	* Additional Feature: Check player and opponent words against dictionary

### Sources
* json dictionary file: https://github.com/simplewilliamz/scrabble/blob/master/scrabbleDictionary.json
* How to import json file: https://docs.python.org/3.6/library/json.html
* How to access json file: https://stackoverflow.com/questions/20199126/reading-json-from-a-file

### UI Class – Zhi

##### Class Variables:
* Timer
* Difficulty Level
* Grid letters
* Score
* List of current words
* List of all possible words

##### Methods:
* text_objects(text, font) ← Creates a pygame text object and separates it into a rectangle object and a text object. White in color.
* text_objects_black(text, font) ← Creates a pygame text object and separates it into a rectangle object and a text. Black in color.
* button(msg,x,y,w,h,ic,ac,action=None,args=None) ← Creates a button object which leads to a function with message msg, position (x,y), w in width and h in height. ic is the base color and ac is the color when your mouse is hovering. Action is the function.
* quitGame() ← Quit game
* checkWord() ← Returns true, helper function
* instructions() ← Instructions page
* game_intro() ← Game Intro page
* inbounds(x,y) ← In bounds helper function, checks if x and y are in bounds
* endscreen() ← End screen Page
* difficultySelect() ← Difficulty select
* game(difficulty) ← Actual game class, difficulty level as parameter



### Computer Class – Jack

##### Class Variables:
* List of all possible words, points for each word
* List of player input words, points for each word
* List of opponent words, points for each word
* Difficulty Level (as a fraction of 100)
* Word points (for grading of words)
* Player Score
* Computer Score

##### Methods:
* wordScores() ← Assigns the score that each possible word on board would get
* sumWordScore() ← Sums the scores of all word for a player(user or CPU)
* computerWords() ← Generates opponent words based on a percentage of total possible score
* scoring() ← compares score worthy words by user and CPU and gives points if the other doesn't have them
* operations() ← Utility Class
