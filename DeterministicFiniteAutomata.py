from FiniteAutomata import FiniteAutomata
from String import String
from ComputationHistory import ComputationHistoryList
from StateMachine import StateMachine
from StateMachine import Transition

# Deterministic finite automata.
#
# member currentStep: holds datas for current step, designed for step by step running.
class DeterministicFiniteAutomata(FiniteAutomata):
    # Stores datas for current step.
    #
    # member state: name of current state
    # member string: current string
    class ComputationStep:
        def __init__(self, state, string):
            self.state = state
            self.string = string

    # Initialization.
    # param computationHistory: whether store computation history list while running
    #     'True' for create compoutation history
    #     'False' for not record computation history
    def __init__(self, computationHistory = False):
        super().__init__(computationHistory)
        self.currentStep = None
    
    # Prepares automata to run.
    # Must be called before step by step running.
    #
    # param string: list of symbols
    def setup(self, string):
        self.currentStep = self.ComputationStep(self.stateMachine.startState, String(string))

        if self.computationHistory != None:
            self.computationHistory = ComputationHistoryList()
            self.computationHistory.inputTypes = ["Str"]

    # Runs one step(one transition) of automata.
    # return: acceptance
    #     'True' means execution end by accepting
    #     'False' means execution end by accepting
    #     'None' means execution not ended yet
    def runStep(self):
        symbol = self.currentStep.string.getSymbol() # get symbol from string

        if symbol == None: # reached to end of string 
            accept = self.stateMachine.isAccepting(self.currentStep.state) # is final state accepting
            
            if self.computationHistory != None: # log final state
                self.computationHistory.addNode(self.currentStep.state, Transition([], accept, None))

            return accept

        transition = self.stateMachine.getLastTransition(self.currentStep.state, [symbol]) # get transition suits symbol

        if transition == None: # if no transintion available then die
            transition = Transition([symbol], None, None)

        if self.computationHistory != None:
            self.computationHistory.addNode(self.currentStep.state, transition)

        # update current state
        self.currentStep.state = transition.to
        self.currentStep.string.forward()

        if self.currentStep.state == None: # dead means end as rejected
            return False

        return None

    # Runs automata until it halts.
    #
    # param string: list of symbols
    # return: acceptance
    #     'True' means accepted
    #     'False' means rejected
    def run(self, string):
        self.setup(string)

        accept = self.runStep()
        while accept == None:
            accept = self.runStep()
        
        return accept