# Transition from one state to another.
#
# member inputs: inputs list
# An input might be a symbol from string, stack or a tape.
# 'None' refers empty string(epsilon).
#
# member outputs: outputs list
# An output might be a symbol to push stack or write to tape.
# When to is None:
#   'True' means accepted
#   'False' means rejected
#   'None' means died
#
# member to: state to transit
# Inputs might be a symbol from string, stack or a tape.
# 'None' refers empty string(epsilon).
# When to is 'None' it means transition end by accept, reject or die.
class Transition:
    # Initilization.
    # param inputs: inputs list
    # param outputs: outputs list
    # param to: state to transit
    def __init__(self, inputs, outputs, to):
        self.inputs = inputs
        self.outputs = outputs
        self.to = to

# State.
#
# member accept: acceptance of state
# 'True' means accepting state
# 'False' means rejecting state
# 'None' means neighter accepting or rejecting state
#
# member transitions: list of transitions
class State:
    # Initilization.
    # param accept: acceptance of state
    #     'True' means accepting state
    #     'False' means rejecting state
    #     'None' means neighter accepting or rejecting state
    def __init__(self, accept = None):
        self.accept = accept
        self.transitions = []

    # Checks whether state is accepting.
    # return: 'True' if accepting, 'False' otherwise
    def isAccepting(self):
        return self.accept == True

    # Checks whether state is rejecting.
    # return: 'True' if rejecting, 'False' otherwise
    def isRejecting(self):
        return self.accept == False

    # Gets the first transition from transitions.
    # param inputs: list of inputs
    # return: first transition found, if no transition found 'None' returned
    def getFirstTransition(self, inputs):
        for transition in self.transitions:
            if transition.inputs == inputs:
                return transition

        return None

    # Gets the last transition from transitions.
    # Suggested for retrivieving transition in deterministic automata.
    # param inputs: list of inputs
    # return: first transition found, if no transition found 'None' returned
    def getLastTransition(self, inputs):
        for transition in self.transitions[::-1]:
            if transition.inputs == inputs:
                return transition

        return None

    # Gets all transitions suits the given inputs.
    # param inputs: list of inputs
    # return: list of transitions found
    def getTransitions(self, inputs):
        transitions = []

        for transition in self.transitions:
            if transition.inputs == inputs:
                transitions.append(transition)

        return transitions

    # Adds new transition to transitions.
    # param inputs: inputs list
    # param outputs: outputs list
    # to: state to transit
    def addTransition(self, inputs, outputs, to):
        self.transitions.append(Transition(inputs, outputs, to))

# State Machine that stores states and transition between them.
#
# member states: dictionary of states
# key: state name (Highly suggested to use a hashable type)
# value: State class represents state
#
# member startState: name of start state
class StateMachine:
    # Initialization.
    def __init__(self):
        self.states = {}
        self.startState = None

    # Adds transition.
    # If states with given names not exist, they created.
    # param fromState: state name of transition from
    # param inputs: inputs list
    # param outputs: outputs list
    # param toState: state name of transition to
    def addTransition(self, fromState, inputs, outputs, toState):
        self.addState(fromState)
        self.addState(toState)
        self.states[fromState].addTransition(inputs, outputs, toState)

    # Adds state if it not exists.
    # param state: name of state
    def addState(self, state):
        if self.states.get(state) == None:
            self.states[state] = State()

    # Sets acceptance of a state.
    # If state with given name not exist, it created.
    # param state: name of state
    # param accept: acceptance
    #   'True': accepting
    #   'False': rejecting
    #   'None': neutral
    def setAccept(self, state, accept):
        self.addState(state)
        self.states[state].accept = accept

    # Sets start state.
    # If state with given name not exist, it created.
    # param state: name of state
    def setStartState(self, state):
        self.addState(state)
        self.startState = state

    # Checks whether state is accepting.
    # param state: name of state
    # return: 'True' if accepting, 'False' otherwise
    def isAccepting(self, state):
        return self.states[state].isAccepting()

    # Checks whether state is rejecting.
    # param state: name of state
    # return: 'True' if rejecting, 'False' otherwise
    def isRejecting(self, state):
        return self.states[state].isRejecting()

    # Gets the first transition of a state.
    # param state: name of state
    # param inputs: list of inputs
    # return: first transition found, if no transition found 'None' returned
    def getFirstTransition(self, state, inputs):
        return self.states[state].getFirstTransition(inputs)

    # Gets the last transition of a state.
    # param state: name of state
    # param inputs: list of inputs
    # return: last transition found, if no transition found 'None' returned
    def getLastTransition(self, state, inputs):
        return self.states[state].getLastTransition(inputs)

    # Gets all transitions suits the inputs from a state.
    # param state: name of state
    # param inputs: list of inputs
    # return: list of transitions found
    def getTransitions(self, state, inputs):
        return self.states[state].getTransitions(inputs)