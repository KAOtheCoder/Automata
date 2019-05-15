from TuringTransition import Transition
from Tape import Stack
from Tape import Tape
class TuringMachine:
	
	currentState=' '

	def __init__(self, input, startState):
		self.inputTape = Tape(input)
		self.rules = []
		self.startState = startState
		self.input = None

	def setStartState(self, startState):
		self.startState = startState

	def addRule(self,transition):
		self.rules.append(transition)
	
	def start(self, input):
		self.input = input
		self.currentState = self.startState
		currentTrans = Transition()
		currentTrans=None

		while True:
			if (currentTrans != None):
				self.currentState = currentTrans.getNextState()
			currentTrans = self.checkRule(self.currentState)
			if (currentTrans == None):
				break

		if (self.currentState == 't'):
			print(self.input + " - Kabul Edildi")
		elif(self.currentState != 't'):
			print(self.input + " - Kabul Edilmedi")

	def checkRule(self,state):
		transition = Transition()
		transition=None

		for rl in self.rules:
			if (rl.getCurrentState() == state):
				if (rl.getReadCharacter() == self.inputTape.getCurrent()):
					transition = rl
					transition.printTransition()
					self.inputTape.setCurrent(transition.getWriteCharacter())
					if (transition.getDimension() == 'L'):
						self.inputTape.moveLeft()
					elif(transition.getDimension() == 'R'):
						self.inputTape.moveRight()
					break

		return transition

machine = TuringMachine("00011", 's')

machine.addRule(Transition('s', 'p', '0', 'X', 'R'))
machine.addRule(Transition('s', 'r', 'Y', 'Y', 'R'))
machine.addRule(Transition('p', 'p', '0', '0', 'R'))
machine.addRule(Transition('p', 'q', '1', 'Y', 'L'))
machine.addRule(Transition('p', 'p', 'Y', 'Y', 'R'))
machine.addRule(Transition('q', 'q', '0', '0', 'L'))
machine.addRule(Transition('q', 's', 'X', 'X', 'R'))
machine.addRule(Transition('q', 'q', 'Y', 'Y', 'L'))
machine.addRule(Transition('r', 'r', 'Y', 'Y', 'R'))
machine.addRule(Transition('r', 't', '#', '#', 'R'))

machine.setStartState('s')
machine.start("00011")
