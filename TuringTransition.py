class Transition:

	def __init__(self, currentState='s', nextState='s', readCharacter='s', writeCharacter='s', dimension='s'):
		self.currentState = currentState;
		self.nextState = nextState;
		self.readCharacter = readCharacter;
		self.writeCharacter = writeCharacter;
		self.dimension = dimension;

	def getCurrentState(self):
		return self.currentState;

	def setCurrentState(self,currentState):
		self.currentState = currentState;


	def getNextState(self):
		return self.nextState;

	def setNextState(self,nextState):
		self.nextState = nextState;
	

	def getReadCharacter(self):
		return self.readCharacter;

	def setReadCharacter(self, readCharacter):
		self.readCharacter = readCharacter;

	def getWriteCharacter(self):
		return self.writeCharacter;

	def setWriteCharacter(self, writeCharacter):
		self.writeCharacter = writeCharacter;

	def getDimension(self):
		return self.dimension;
	

	def setDimension(self, dimension):
		self.dimension = dimension;

	def printTransition(self):
		print( "Current State:" + self.currentState + " Read:" + self.readCharacter + " Next State:" + self.nextState + " Write:"
				+ self.writeCharacter + " Dimension:" + self.getDimension() )