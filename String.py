# String data structer to use in finite machines.
#
# member data: list of symbols
#     'data' is shallow copied. So do not change it afterwards.
#
# member indicator: index
class String:
    # Initialization.
    # param data: list of symbols
    def __init__(self, data):
        self.data = data
        self.indicator = 0

    # Gets symbol that indicator indicates.
    # return symbol that indicator indicates, 'None' if end of string reached
    def getSymbol(self):
        if self.indicator >= len(self.data):
            return None

        return self.data[self.indicator]

    # Forwards indicator by one.
    def forward(self):
        self.indicator += 1

    # Gets a copy of the string.
    # 'data' is not deep copied since it designed to not change ever.
    # return: copy of the string
    def copy(self):
        clone = String(self.data)
        clone.indicator = self.indicator
        
        return clone