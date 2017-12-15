#import json
import random

#generates board and finds all possible words
#randomizer for the letters
#4X4 grid
#return board as a 2d list

# with open('scrabbleDictionary.json.txt') as json_data:
# 	words = json.load(json_data)
# 	print(words)

class Grid:

	def __init__(self):
		self.grid = []
		self.board = ''
	
	def makeBoard(self):
		letters = {0: 'A',
				1: 'B',
				2: 'C', 
				3: 'D', 
				4: 'E', 
				5: 'F', 
				6: 'G', 
				7: 'H', 
				8: 'I', 
				9: 'J', 
				10: 'K',
				11: 'L', 
				12: 'M', 
				13: 'N', 
				14: 'O', 
				15: 'P', 
				16: 'Q', 
				17: 'R',
				18: 'S', 
				19: 'T', 
				20: 'U', 
				21: 'V', 
				22: 'W', 
				23: 'X', 
				24: 'Y', 
				25: 'Z'}
		for i in range(16):
			self.board += (letters[random.randint(0,25)])
		print(self.board)

	#def wordCheck(self):
		#json file used here
		#while i in self.board == true:




game1 = Grid()
game1.makeBoard()

