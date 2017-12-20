import json
import random

#generates board and finds all possible words


#Sources:
#json Dictionary File: https://github.com/simplewilliamz/scrabble/blob/master/scrabbleDictionary.json
#Import/Use Dictionary File: https://stackoverflow.com/questions/20199126/reading-json-from-a-file
#Dice Configuration: https://boardgames.stackexchange.com/questions/29264/boggle-what-is-the-dice-configuration-for-boggle-in-various-languages



class Grid:

	def __init__(self):
		self.grid = [['']*4]*4
		self.inputWords = ['hello', 'goodbye', 'ttyyl']
		self.possibleWords =[]

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
 			dictionary = json.loads(json_data.read())
		for i in self.inputWords:
 			if i in dictionary:
 				self.possibleWords.append(i)
 			else:
 				print('Word does not exist.')

	def findWords(self, i , j, str):
 		visited[i][j] = True
 		str = str + self.grid[i][j]
 		self.inputWords.append(str)
 		for x = i-1, x <= i+1, x<4:
 			i++
 		for y = j-1, y <= j+1, y<4:
 			j++
 			
 	def variables():
 		str = ''
		int(i) = 0
 		int(j) = 0
		visited = [[0]*4]*4
		for i in range(4):
			for j in range(4):
				findWords(i, j, str)


game1 = Grid()
game1.makeBoard()
game1.wordCheck()

