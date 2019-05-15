from FiniteAutomaton import FiniteAutomaton
from String import String
from StateMachine import StateMachine
from StateMachine import Transition
from ComputationHistory import ComputationHistoryTree

# Non-Deterministic finite automaton.
#
# member currentSteps: holds datas for current steps, designed for step by step running.
class NonDeterministicFiniteAutomaton(FiniteAutomaton):
    # Stores datas for current step.
    #
    # member state: name of current state
    # member string: current string
    # member node: node in computation history
    class ComputationStep:
        def __init__(self, state, string, node = None):
            self.state = state
            self.string = string
            self.node = None

    # Initialization.
    # param computationHistory: whether store computation history tree while running
    #     'True' for create compoutation history
    #     'False' for not record computation history
    def __init__(self, computationHistory = False):
        super().__init__(computationHistory)
        self.currentSteps = None

    # Prepares automaton to run.
    # Must be called before step by step running.
    #
    # param string: list of symbols
    def setup(self, string):
        computationStep = self.ComputationStep(self.stateMachine.startState, String(string))
        self.currentSteps = [computationStep]
        
        if self.computationHistory != None:
            self.computationHistory = ComputationHistoryTree()
            self.computationHistory.inputTypes = ["Str"]
            self.computationHistory.root = ComputationHistoryTree.Node(self.stateMachine.startState, [])
            computationStep.node = self.computationHistory.root

    # Runs one step (one branch) of automaton.
    # return: acceptance
    #     'True' means execution end by accepting
    #     'False' means execution end by accepting
    #     'None' means execution not ended yet
    def runStep(self):
        accept = None
        nextSteps = []

        for step in self.currentSteps: # run each step sequentially
            symbol = step.string.getSymbol() # get symbol from string

            if symbol == None: # reached to end of string
                thisAccept = self.stateMachine.isAccepting(step.state)

                if thisAccept:
                    accept = True

                if self.computationHistory != None: # log final state
                    step.node.transitions.append(Transition([], thisAccept, None))

                continue

            transitions = self.stateMachine.getTransitions(step.state, [symbol]) # get transitions suits symbol

            if len(transitions) > 0:
                # copy string for each branch,
                # cuz string indicators might be different since some transitions uses empty string('None')
                string = step.string.copy()
                string.forward()

                for transition in transitions: # create branch in 'nextSteps' for each transition
                    computationStep = self.ComputationStep(transition.to, string)
                    nextSteps.append(computationStep)
                    
                    if self.computationHistory != None: # create node in computation history tree
                        computationStep.node = ComputationHistoryTree.Node(transition.to, [])
                        step.node.transitions.append(Transition(transition.inputs, transition.outputs, computationStep.node))

            elif self.computationHistory != None: # add computatiopn history a dead branch
                step.node.transitions.append(Transition([symbol], None, None))

            transitions = self.stateMachine.getTransitions(step.state, [None]) # get all empty string transitions

            for transition in transitions: # create branch in 'nextSteps' for each transition
                computationStep = self.ComputationStep(transition.to, step.string)
                nextSteps.append(computationStep)
                
                if self.computationHistory != None: # create node in computation history tree
                    computationStep.node = ComputationHistoryTree.Node(transition.to, [])
                    step.node.transitions.append(Transition(transition.inputs, transition.outputs, computationStep.node))

        self.currentSteps = nextSteps # update current steps

        if accept == True:
            return True

        if len(self.currentSteps) == 0: # all branches are died out none of them accepted, so reject
            return False

        return None

    # Runs automaton until it halts.
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