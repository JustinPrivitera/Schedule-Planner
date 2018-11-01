class node:
	def __init__(self, name, index):
		self.name = name
		self.index = index

	def getName(self):
		return self.name

	def getIndex(self):
		return self.index

	def setName(self, newname):
		self.name = newname

	def setIndex(self, newindex):
		self.index = newindex

def nodeCompare(node1, node2): # returns 1 if the nodes are the same and 0 if they are different
	if node1.name == node2.name and node1.index == node2.index:
		return 1
	else:
		return 0
