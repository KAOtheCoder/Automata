# Stack data structer to use in push down automata.
#
# member data: list of symbols
class Stack:
    # Initilization
    def __init__(self):
        self.data = []

    # Gets symbol top on stack
    # return: top symbol
    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[len(self.data) - 1]

    # Pushes symbol to stack unless symbol is 'None'
    # param symbol: symbol to push
    def push(self, symbol):
        if symbol != None:
            self.data.append(symbol)

    # Pops top symbol from stack
    def pop(self):
        self.data.pop()

    # Gets a copy of the stack.
    # return: copy of the stack
    def copy(self):
        clone = Stack()
        
        for symbol in self.data:
            clone.data.append(symbol)

        return clone