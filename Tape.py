class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]
	def push(self , item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

class Tape:
	
	def __init__(self, input):
		self.leftTape = Stack();
		self.rightTape = Stack();
		self.rightTape.push('#');
		for i in range(len(input)-1,-1,-1):
			self.rightTape.push(input[i]);

		self.current = self.rightTape.pop();

	def moveLeft(self):
		self.rightTape.push(self.current)
		if(self.leftTape.isEmpty()):
			self.leftTape.push('#');
		self.current=self.leftTape.pop();

	def moveRight(self):
		self.leftTape.push(self.current);
		if (self.rightTape.isEmpty()):
			self.rightTape.push('#');
		self.current = self.rightTape.pop();
	
	def getCurrent(self):
		return self.current;
	
	def setCurrent(self,nextChar):
		self.current = nextChar;