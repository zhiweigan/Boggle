from random import randint

class Computer():#difLvl, boardWords, playerWords): #need to somehow import the words that can be generated from the letters				
				  #take input from UI for the difficulty level
	"""docstring for ClassName"""
	def __init__(self, posWords, playerWords, difficulty):#, posWords, playerWords):
		self.posWords = [posWords,[]]
		self.opponentWords = [],[]
		self.difLvl = difficulty
		self.wordPoints = [0, 0, 0, 1, 1, 2, 3, 4, 11, 11, 11, 11, 11, 11, 11, 11, 11]
		self.playerWords = [playerWords,[]]
		self.computerWordSum = 0
		self.playerScore = 0
		self.computerScore = 0

	def wordScores(self, words, wordPoints):
	# gives the points that are earned by each word and assign the point values to the corresponding place on the next layerof list
		for i in range (len(words[0])):
			words[1].append(wordPoints[len(words[0][i])])
		return words

	#https://stackoverflow.com/questions/2104305/finding-elements-not-in-a-list
	def isWords(self): 
		# checks to see if inputs from the user are words that could be made in the board- gets rid of them if they are not
		self.playerWords[0] = list(set(self.playerWords[0]) - set(self.posWords[0]))


	def sumWordScore(self, wordsUsed, difLvl):
		return int((sum(wordsUsed)*(difLvl)))

	def computerWords(self, scoreSum, posWords): 
	# generates a full list of words that the CPU finds based on the total words that could be found on the board
		(self.opponentWords[0]).append(posWords[0][randint(0, len(posWords[1])-1)])
		self.opponentWords = Computer.wordScores(self,self.opponentWords, self.wordPoints)
		Amy = Computer.sumWordScore(self,self.opponentWords[1],1)
		Rita = int((self.computerWordSum))
		
		while Amy <= Rita:
			Monica = posWords[0][randint(0, len(posWords[1])-1)]
			if Monica not in self.opponentWords[0]:
				self.opponentWords[0].append(Monica)
				Amy = Computer.sumWordScore(self,self.opponentWords[1],1)
			(self.opponentWords[1]).clear()
			self.opponentWords = Computer.wordScores(self,self.opponentWords, self.wordPoints)
			
		return self.opponentWords

	def scoring(self, player, computer): 
	# compares the words that the user finds and the words found by the CPU, gives points to each player based only on words exclusively in their list
		for i in range (len(player[0])):
			if player[0][i] not in computer[0]:
				self.playerScore += player[1][i]
		for i in range (len(computer[0])):
			if computer[0][i] not in player[0]:
				self.computerScore += computer[1][i] 

	def operations(self): # performs all the actual actions in the class
		#print(self.posWords)
		self.posWords = Computer.wordScores(self, self.posWords, self.wordPoints) 
		# takes the possible words generated in other class and formats them to this class, then finds score each word would earn
		Computer.isWords(self)
		# removes all strings inputted by user that are not words
		self.playerWords = Computer.wordScores(self, self.playerWords, self.wordPoints)
		# finds the points earned by each word the user inputed
		self.computerWordSum = Computer.sumWordScore(self, self.posWords[1], self.difLvl)
		# finds the ammount of points that could be earned by the words the CPU "finds"
		self.opponentWords = Computer.computerWords(self, self.computerWordSum, self.posWords)
		# finds the words that give the CPU the points that it should be generating
		Computer.scoring(self, self.playerWords, self.opponentWords)
		# compares words found by user and CPU and makes the socres they actually earn a callable variable


