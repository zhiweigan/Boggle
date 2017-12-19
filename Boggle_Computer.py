#import Boggle_Grid
#import Boggle_UI
from random import randint

class Computer():#difLvl, boardWords, playerWords): #need to somehow import the words that can be generated from the letters				
				  #take input from UI for the difficulty level
	"""docstring for ClassName"""
	def __init__(self, posWords, playerWords, difficulty):#, posWords, playerWords):
		self.posWords = posWords,[]
		self.opponentWords = [],[]
		self.difLvl = difficulty
		self.wordPoints = [0, 0, 0, 1, 1, 2, 3, 4, 11, 11, 11, 11, 11, 11, 11, 11, 11]
		self.playerWords = playerWords,[]
		self.computerWordSum = 0
		self.playerScore = 0
		self.computerScore = 0


	def wordScores(self, words, wordPoints):
		for i in range (len(words[0])):
			words[1].append(wordPoints[len(words[0][i])])
		return words

	def isWords(self):
		for i in range(len(self.playerWords[0])-1):
			if self.playerWords[0][i] not in self.posWords[0]:
				(self.playerWords[0]).pop(i) 
				i -= 1

	def sumWordScore(self, wordsUsed, difLvl):
		return int((sum(wordsUsed)*(difLvl)))

	def computerWords(self, scoreSum, posWords):

		(self.opponentWords[0]).append(posWords[0][randint(0, len(posWords[1])-1)])
		self.opponentWords = Computer.wordScores(self.opponentWords, self.wordPoints)
		Amy = Computer.sumWordScore(self.opponentWords[1],1)
		Rita = int((self.computerWordSum))
		
		while Amy <= Rita:
			Monica = posWords[0][randint(0, len(posWords[1])-1)]
			if Monica not in self.opponentWords[0]:
				self.opponentWords[0].append(Monica)
				Amy = Computer.sumWordScore(self.opponentWords[1],1)
			(self.opponentWords[1]).clear()
			self.opponentWords = Computer.wordScores(self.opponentWords, self.wordPoints)
			
		return self.opponentWords

	def scoring(self, player, computer):
		for i in range (len(player[0])):
			if player[0][i] not in computer[0]:
				self.playerScore += player[1][i]
		for i in range (len(computer[0])):
			if computer[0][i] not in player[0]:
				self.computerScore += computer[1][i] 





	def operations(self):
		self.posWords = Computer.wordScores(self.posWords, self.wordPoints)
		Computer.isWords()
		self.playerWords = Computer.wordScores(self.playerWords, self.wordPoints)
		self.computerWordSum = Computer.sumWordScore(self.posWords[1], self.difLvl)
		self.opponentWords = Computer.computerWords(self.computerWordSum, self.posWords)
		Computer.scoring(self.playerWords, self.opponentWords)






Computer = Computer()

Computer.operations()