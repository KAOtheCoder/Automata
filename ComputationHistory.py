from StateMachine import Transition

# Base class for computation histories.
#
# member inputTypes: list of input type names
# member outputTypes: list of output type names
#     These type names can be leave out if you want to use your own printing/visualization system.
class ComputationHistory:
    # Initialization
    def __init__(self):
        self.inputTypes = []
        self.outputTypes = []

# Computation history as list.
#
# member computationList: list of computation nodes
class ComputationHistoryList(ComputationHistory):
    # Computation Node for computation list.
    #
    # member state: name of state
    # member transition: transition used to transit next node
    class Node:
        # Initialization.
        # param state: name of state
        # param transition: transition used to transit next node
        def __init__(self, state, transition):
            self.state = state
            self.transition = transition

    # Initialization.
    def __init__(self):
        super().__init__()
        self.computationList = []
        
    # Appends new node to computation list.
    def addNode(self, state, transition):
        self.computationList.append(self.Node(state, transition))

    # Translate node information to string.
    # param node: node
    def nodeToString(self, node):
        string = "Q[" + str(node.state) + "]"

        for i in range(len(node.transition.inputs)):
            string += " x " + str(self.inputTypes[i]) + "[" + str(node.transition.inputs[i]) + "]"

        string += " -> "

        if node.transition.to == None:
            if node.transition.outputs == None:
                string += "DIED"
            elif node.transition.outputs == True:
                string += "ACCEPTED"
            else:
                string += "REJECTED"
        else:
            string += "Q[" + str(node.transition.to) + "]"

            for i in range(len(node.transition.outputs)):
                string += " , " + str(self.outputTypes[i]) + "[" + str(node.transition.outputs[i]) + "]"

        return string

    # Translates all list information to string.
    def toString(self):
        string = ""

        for node in self.computationList:
            string += self.nodeToString(node) + "\n"

        return string

# Computation history as tree.
#
# member root: root node of computation tree
class ComputationHistoryTree(ComputationHistory):
    # Computation Node for computation tree.
    #
    # member state: name of state
    # member transitions: transitions used to transit branch nodes
    #     'transition.to' used to refer transited node itself instead of state name
    class Node:
        # Initialization.
        # param state: name of state
        # param transitions: transitions used to transit branch nodes
        #     'transition.to' used to refer transited node itself instead of state name
        def __init__(self, state, transitions = []):
            self.state = state
            self.transitions = transitions

    # Initialization.
    def __init__(self):
        super().__init__()
        self.root = None

    # Translate node information to string.
    # param node: node
    def nodeToString(self, node):
        string = ""

        for transition in node.transitions:
            string += "Q[" + str(node.state) + "]"

            for i in range(len(transition.inputs)):
                string += " x " + str(self.inputTypes[i]) + "[" + str(transition.inputs[i]) + "]"

            string += " -> "

            if transition.to == None:
                if transition.outputs == None:
                    string += "DIED"
                elif transition.outputs == True:
                    string += "ACCEPTED"
                else:
                    string += "REJECTED"
            else:
                string += "Q[" + str(transition.to.state) + "]"

                for i in range(len(transition.outputs)):
                    string += " , " + str(self.outputTypes[i]) + "[" + str(transition.outputs[i]) + "]"

            string += "\n"

        return string

    # Translates all tree information to string.
    def toString(self):
        if self.root == None:
            return ""

        string = ""
        step = 1
        nodes = [self.root]

        while len(nodes) > 0:
            stepString = "STEP " + str(step) + ":\n"
            nextNodes = []

            contextString = ""
            for node in nodes:
                contextString += self.nodeToString(node)
                
                for transition in node.transitions:
                    if transition.to != None:
                        nextNodes.append(transition.to)

            if contextString != "":
                string += stepString + contextString

            nodes = nextNodes
            step += 1

        return string