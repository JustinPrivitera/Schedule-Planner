class Stack:

	def __init__(self, capacity):
		self.num_items = 0
		self.capacity = capacity
		self.items = [None]*capacity

	def push(self, item):
		if self.is_full():
			raise IndexError("The Stack is full")
		self.items[self.num_items] = item
		self.num_items += 1

	def pop(self):
		if self.is_empty():
			raise IndexError("The Stack is empty")
		self.num_items -= 1
		return self.items[self.num_items]
		
	def peek(self):
		if self.is_empty():
			raise IndexError("The Stack is empty")
		return self.items[self.num_items - 1]

	def size(self):
		return self.num_items

	def is_full(self):
		return self.num_items == self.capacity

	def is_empty(self):
		return self.num_items == 0
