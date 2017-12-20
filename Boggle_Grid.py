import json
import random

#generates board and finds all possible words


#Sources:
#json Dictionary File: https://github.com/simplewilliamz/scrabble/blob/master/scrabbleDictionary.json
#Import/Use Dictionary File: https://stackoverflow.com/questions/20199126/reading-json-from-a-file
#Dice Configuration: https://boardgames.stackexchange.com/questions/29264/boggle-what-is-the-dice-configuration-for-boggle-in-various-languages

def inbounds(x,y):
	return x >= 0 and x < 4 and y >= 0 and y < 4

dx = [1,1,1,0,-1,-1,-1,0]
dy = [0,1,-1,1,0,-1,1,-1]

class Grid:
	def __init__(self):
		self.grid = []
		self.inputWords = []
		self.possibleWords =[]

	#make Board out of random dice rolls
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

		self.grid.append([die0[random.randint(0,5)], die1[random.randint(0,5)], die2[random.randint(0,5)], die3[random.randint(0,5)]])
		self.grid.append([die4[random.randint(0,5)], die5[random.randint(0,5)], die6[random.randint(0,5)], die7[random.randint(0,5)]])
		self.grid.append([die8[random.randint(0,5)], die9[random.randint(0,5)], die10[random.randint(0,5)], die11[random.randint(0,5)]])
		self.grid.append([die12[random.randint(0,5)], die13[random.randint(0,5)], die14[random.randint(0,5)], die15[random.randint(0,5)]])


	#Make self.possibleWords a list with all possible words based on a scrabble dictionary
	def wordCheck(self):
		with open('scrabbleDictionary.json.txt') as json_data:
			dictionary = json.loads(json_data.read())
		for i in self.inputWords:
			if i.lower() in dictionary:
				self.possibleWords.append(i)
		self.possibleWords = list(set(self.possibleWords))

	#Recursive algorithm to find all possible words - similar to BFS, http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
	def findWords(self, i , j):
		self.visited[i][j] = True
		self.str = self.str + self.grid[i][j]
		self.inputWords.append(self.str)
		for z in range(8):
			if inbounds(i + dy[z], j + dx[z]) and self.visited[i + dy[z]][ j + dx[z]] == 0:
				Grid.findWords(self, i+dy[z], j + dx[z])

		self.str = self.str[:-1]
		self.visited[i][j] = False

	#Start recursive function
	def variables(self):
		self.str = ''
		self.visited = [[0]*4]*4
		for i in range(4):
			for j in range(4):
				Grid.findWords(self, i, j)



