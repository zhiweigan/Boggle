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
		self.playerWords = ['pizza', 'green', 'words', 'purple'],[]
		self.computerWordSum = 0
		self.playerScore = 0
		self.computerScore = 0


	def wordScores(self, words, wordPoints):
		for i in range (len(words[0])):
			words[1].append(wordPoints[len(words[0][i])])
		return words

	def isWords(self):
		for i in range(len(self.playerWords[0])-1):
			print('len is ' + str(len(self.playerWords[0])))
			print( 'i is ' + str(i))
			if self.playerWords[0][i] not in self.posWords[0]:
				(self.playerWords[0]).pop(i) 
				i -= 1
			print( 'i is ' + str(i))
			print(self.playerWords[0][i])

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





	def operations(self):#difLvl, boardWords, playerWords):
		#self.posWords[0] = boardWords
		self.posWords = Computer.wordScores(self.posWords, self.wordPoints)
#		print(self.posWords)
		Computer.isWords()
		self.playerWords = Computer.wordScores(self.playerWords, self.wordPoints)
		print(self.playerWords)
		self.computerWordSum = Computer.sumWordScore(self.posWords[1], self.difLvl)
#		print(self.computerWordSum)
		self.opponentWords = Computer.computerWords(self.computerWordSum, self.posWords)
		print(self.opponentWords)
		Computer.scoring(self.playerWords, self.opponentWords)






Computer = Computer()

Computer.operations()