#import Boggle_Grid
#import Boggle_UI
from random import randint

class Computer():#difLvl, boardWords, playerWords): #need to somehow import the words that can be generated from the letters				
				  #take input from UI for the difficulty level
	"""docstring for ClassName"""
	def __init__(self):#, posWords, playerWords):
		self.posWords = ['pizza', 'wo', 'red', 'iceeee', 'icecrea', 'slime'],[]
		self.opponentWords = [],[]
		self.difLvl = .5
		self.wordPoints = [0, 0, 0, 1, 1, 2, 3, 4, 11, 11, 11, 11, 11, 11, 11, 11, 11]
		self.playerWords = ['pizza', 'words'],[]
		self.computerWordSum = 0


	def wordScores(self, words, wordPoints):
		for i in range (len(words[0])):
			words[1].append(wordPoints[len(words[0][i])])
		return words

	def sumWordScore(self, wordsUsed, difLvl):
		return int((sum(wordsUsed)*(difLvl)))

	def computerWords(self, scoreSum, posWords):

		(self.opponentWords[0]).append(posWords[0][randint(0, len(posWords[1])-1)])
		self.opponentWords = Computer.wordScores(self.opponentWords, self.wordPoints)
		Amy = Computer.sumWordScore(self.opponentWords[1],1)
		Rita = int((self.computerWordSum))
		print(self.opponentWords)
		
		while Amy <= Rita:
			print(str(Amy) + ' Amy')
			Monica = posWords[0][randint(0, len(posWords[1])-1)]
			print(self.opponentWords[0])
			print(Monica)
			if Monica not in self.opponentWords[0]:
				self.opponentWords[0].append(Monica)
				Amy = Computer.sumWordScore(self.opponentWords[1],1)
			print(self.opponentWords[0])
			self.opponentWords = Computer.wordScores(self.opponentWords, self.wordPoints)
			print(self.opponentWords[1])
			
		return self.opponentWords
		# print(self.playerWords)


	def operations(self):#difLvl, boardWords, playerWords):
		#self.posWords[0] = boardWords
		self.posWords = Computer.wordScores(self.posWords, self.wordPoints)
#		print(self.posWords)
		self.playerWords = Computer.wordScores(self.playerWords, self.wordPoints)
#		print(self.playerWords)
		self.computerWordSum = Computer.sumWordScore(self.posWords[1], self.difLvl)
#		print(self.computerWordSum)
		self.opponentWords = Computer.computerWords(self.computerWordSum, self.posWords)
		print(self.opponentWords)





Computer = Computer()

Computer.operations()