import json
import random

#generates board and finds all possible words
#randomizer for the letters
#4X4 grid
#return board as a 2d list



class Grid:

	def __init__(self):
		self.line1 = ''
		self.line2 = ''
		self.line3 = ''
		self.line4 = ''
		self.possibleWords = ''

	def makeBoard(self):
		die0 = ['R', 'I', 'F', 'O', 'B', 'X']
		die1 = ['I', 'F', 'E', 'H', 'E', 'Y']
		die2 = ['D', 'E', 'N', 'O', 'W', 'S']
		die3 = ['U', 'T', 'O', 'K', 'N', 'D']
		die4 = ['H', 'M', 'S', 'R', 'A', 'O']
		die5 = ['L', 'U', 'P', 'E', 'T', 'S']
		die6 = ['A', 'C', 'I', 'T', 'O', 'A']
		die7 = ['Y', 'L', 'G', 'K', 'U', 'E']
		die8 = ['Qu', 'B', 'M', 'J', 'O', 'A']
		die9 = ['E', 'H', 'I', 'S', 'P', 'N']
		die10 = ['V', 'E', 'T', 'I', 'G', 'N']
		die11 = ['B', 'A', 'L', 'I', 'Y', 'T']
		die12 = ['E', 'Z', 'A', 'V', 'N', 'D']
		die13 = ['R', 'A', 'L', 'E', 'S', 'C']
		die14 = ['U', 'W', 'I', 'L', 'R', 'G']
		die15 = ['P', 'A', 'C', 'E', 'M', 'D']

		print(die0[random.randint(0,5)], die1[random.randint(0,5)], die2[random.randint(0,5)], die3[random.randint(0,5)])
		print(die4[random.randint(0,5)], die5[random.randint(0,5)], die6[random.randint(0,5)], die7[random.randint(0,5)])
		print(die8[random.randint(0,5)], die9[random.randint(0,5)], die10[random.randint(0,5)], die11[random.randint(0,5)])
		print(die12[random.randint(0,5)], die13[random.randint(0,5)], die14[random.randint(0,5)], die15[random.randint(0,5)])

	def wordCheck(self):
		with open('scrabbleDictionary.json.txt') as json_data:
 			self.possibleWords = json.load(json_data)
 			print(self.possibleWords)





game1 = Grid()
game1.makeBoard()
game1.wordCheck()

