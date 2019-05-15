from PushDownAutomaton import PushDownAutomaton
from String import String
from Stack import Stack
from StateMachine import StateMachine
from StateMachine import Transition
from ComputationHistory import ComputationHistoryTree

# Non-Deterministic push down automaton.
#
# member currentSteps: holds datas for current steps, designed for step by step running.
class NonDeterministicPushDownAutomaton(PushDownAutomaton):
    # Stores datas for current step.
    #
    # member state: name of current state
    # member string: current string
    # member stack: current stack
    # member node: node in computation history
    class ComputationStep:
        def __init__(self, state, string, stack, node = None):
            self.state = state
            self.string = string
            self.stack = stack
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
        computationStep = self.ComputationStep(self.stateMachine.startState, String(string), Stack())
        self.currentSteps = [computationStep]
        
        if self.computationHistory != None:
            self.computationHistory = ComputationHistoryTree()
            self.computationHistory.inputTypes = ["Str", "Pop"]
            self.computationHistory.outputTypes = ["Push"]
            self.computationHistory.root = ComputationHistoryTree.Node(self.stateMachine.startState, [])
            computationStep.node = self.computationHistory.root

    # Runs one step(one branch) of automaton.
    # return: acceptance
    #     'True' means execution end by accepting
    #     'False' means execution end by accepting
    #     'None' means execution not ended yet
    def runStep(self):
        accept = None
        nextSteps = []

        for step in self.currentSteps: # run each step sequentially
            stringSymbol = step.string.getSymbol() # get symbol from string
            stackSymbol = step.stack.peek() # get symbol from stack

            transitions = self.stateMachine.getTransitions(step.state, [None, None])
            
            if stackSymbol != None: # check for not dublicating branches
                transitions.extend(self.stateMachine.getTransitions(step.state, [None, stackSymbol]))
                
            if stringSymbol != None: # check for not dublicating branches
                transitions.extend(self.stateMachine.getTransitions(step.state, [stringSymbol, None]))

                if stackSymbol != None: # check for not dublicating branches
                    thisTransitions = self.stateMachine.getTransitions(step.state, [stringSymbol, stackSymbol])
                   
                    if len(thisTransitions) > 0:
                        transitions.extend(thisTransitions)
                    else:
                        step.node.transitions.append(Transition([stringSymbol, stackSymbol], None, None)) # a branch died out

            for transition in transitions: # create branch in 'nextSteps' for each transition
                stack = step.stack.copy()
                string = step.string.copy()

                if transition.inputs[0] != None: # if used input symbol
                    string.forward()

                if transition.inputs[1] != None: # if stack is not empty pop
                    stack.pop()

                stack.push(transition.outputs[0])

                computationStep = self.ComputationStep(transition.to, string, stack)
                nextSteps.append(computationStep)
                
                if self.computationHistory != None: # create node in computation history tree
                    computationStep.node = ComputationHistoryTree.Node(transition.to, [])
                    step.node.transitions.append(Transition(transition.inputs, transition.outputs, computationStep.node))

            if stringSymbol == None: # reached to end of string 
                thisAccept = self.stateMachine.isAccepting(step.state)

                if thisAccept:
                    accept = True

                if self.computationHistory != None: # log final state
                    step.node.transitions.append(Transition([], thisAccept, None))

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