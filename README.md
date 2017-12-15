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

### UI Class

##### Class Variables:
* Timer
* Difficulty Level
* Grid letters
* Score
* List of current words
* List of all possible words

##### Methods:
* gameIntro() ← Intro page with instructions
* startGame() ← Starts a new Boggle game and displays it
* resetGame() ← Resets all variables and starts a boggle game
* pickDifficulty() ← Screen to pick difficulty
* endGame() ← Endgame screen


### Computer Class

##### Class Variables:
* List of all possible words
* List of player words
* List of opponent words
* Difficulty Level
* Word points (for grading of words)

##### Methods:
* wordScores() ← Assigns scores to words
* sumWordScore() ← Sums the scores of all possible words
* computerWords() ← Generates opponent words
* operations() ← Utility Class
