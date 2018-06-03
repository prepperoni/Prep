class Queue:
	def __init__(self):
		self.push_stk = []
		self.pop_stk = []

	def enqueue(self, x): 
		self.push_stk.append(x)

	def dequeue(self):
		if self.pop_stk:
			return self.pop_stk.pop()
		elif self.push_stk:
			while self.push_stk:
				self.pop_stk.append(self.push_stk.pop())
			return self.pop_stk.pop()
		else:
			raise Exception("Error: cannot pop empty queue.")