from StateMachine import StateMachine
from ComputationHistory import ComputationHistory

# Base class for deterministic and non-deterministic finite automatas.
#
# member stateMachine: state machine
# member computationHistory: computation history structure
class FiniteAutomata:
    # ınitialization.
    # param computationHistory: whether store computation history list while running
    #     'True' for create compoutation history
    #     'False' for not record computation history
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
    # param inputSymbol: string symbol
    # param toState: state to transit
    def addTransition(self, fromState, inputSymbol, toState):
        self.stateMachine.addTransition(fromState, [inputSymbol], [], toState)

    # Sets state's acceptance.
    # param state: name of state
    def setStateAccepting(self, state):
        self.stateMachine.setAccept(state, True)

    # Sets state as starting state
    # param state: name of state
    def setStartState(self, state):
        self.stateMachine.setStartState(state)
