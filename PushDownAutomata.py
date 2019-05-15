from StateMachine import StateMachine
from ComputationHistory import ComputationHistory

# Base class for deterministic and non-deterministic push down automatas.
#
# member stateMachine: state machine
# member computationHistory: computation history structure
class PushDownAutomata:
    def __init__(self, computationHistory = False):
        self.stateMachine = StateMachine()
        self.computationHistory = None

        if computationHistory:
            self.computationHistory = ComputationHistory()

    # Adds state.
    # param state: name of state
    def addState(self, state):
        self.stateMachine.addState(state)

    # Adds transition one state to another.
    # param fromState: state transit from
    # param inputStringSymbol: string symbol to red
    # param inputStackSymbol: stack symbol to pop
    # param outputStackSymbol: stack symbol to push
    # param toState: state to transit
    def addTransition(self, fromState, inputStringSymbol, inputStackSymbol, outputStackSymbol, toState):
        self.stateMachine.addTransition(fromState, [inputStringSymbol, inputStackSymbol], [outputStackSymbol], toState)

    # Sets state's acceptance.
    # param state: name of state
    def setStateAccepting(self, state):
        self.stateMachine.setAccept(state, True)

    # Sets state as starting state
    # param state: name of state
    def setStartState(self, state):
        self.stateMachine.setStartState(state)