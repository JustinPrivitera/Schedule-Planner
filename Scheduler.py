# <date>
# Justin Privitera
# <name>
# <version>
#
# Version History:
# <dates, versions, and descriptions>
#
# <Purpose>
#
# <Instructions>

import sys

from StringToken import stringToken

#def scheduler(inFile, outFile):
def scheduler(inFile):
	inputFile = open(inFile, "r")
	fileText = inputFile.read()
	inputFile.close()
	#outputFile = open(outFile, "w")

	classList = convertTimesToInts(parse(fileText))
	scheduleList = generateSchedules(fillScheduleWithClassList(classList), classList)

	timeList = getTimeList(classList)


	#outputFile.write(stuff)
	#outputFile.close()

def parse(fileText):
	dataList = stringToken(fileText, "\n\t")
	classList = [][]
	j = 0
	i = 0
	while i < len(dataList): # populates the array
		classList[j].append([dataList[i], dataList[i + 1], dataList[i + 2]])
		i += 3
		j += 1
	return classList

def getTimeList(classList):
	timeList = [][]
	for i in range(0, len(classList)):
		timeList[i] = getNumbersBetween(classList[i][1], classList[i][2])
	return timeList

def getNumbersBetween(upper, lower): # not needed for computation, but needed for display
	numList = []
	i = lower
	while i <= upper:
		 numList.append(i)
		 i += 1
	return numList

def convertTimesToInts(classList):
	for i in range(0, len(classList)):
		classList[i][1] = int(classList[i][1])
		classList[i][2] = int(classList[i][2])
	return classList

def fillScheduleWithClassList(classList):
	scheduleList = [][]
	for i in range(0, len(classList)):
		node = node(classList[i][0], i)
		scheduleList.append([node])
	return scheduleList

def generateSchedules(scheduleList, classList): # this is messed up
	i = 0
	while i < len(scheduleList):
		j = i + 1
		while j < len(scheduleList):
			if checkLists(scheduleList[i], scheduleList[j], classList) == 1:
				scheduleList.append(scheduleList[i] + scheduleList[j])
			j += 1
		i += 1
	return removeDuplicates(scheduleList)

def checkLists(list1, list2, classList): # the lists are lists of nodes
	if checkDuplicates(list1, list2) == 1:
		i = 0
		j = 0
		while i < len(list1):
			j = 0
			while j < len(list2):
				if checkConflict(list1[i].index, list2[j].index, classList) == 1:
					return 0
				else:
					j += 1
			i += 1
		return 1
	else:
		return 0

def checkDuplicates(list1, list2):
	i = 0
	j = 0
	while i < len(list1):
		j = 0
		while j < len(list2):
			if nodeCompare(list1[i], list2[j]) == 1:
				return 0
			else:
				j += 1
		i += 1
	return 1


def checkConflict(class1, class2, classList): # returns a 1 if there is a conflict, a 0 if none
	if classList[class1][1] == classList[class2][1]: # if starttimes are equal
		return 1
	elif classList[class1][2] == classList[class2][2]: # if endtimes are equal
		return 1
	elif classList[class1][1] > classList[class2][1] and classList[class1][1] < classList[class2][2]: # if we start in the middle of the other class
		return 1
	elif classList[class1][2] > classList[class2][1] and classList[class1][2] < classList[class2][2]: # if we end in the middle of the other class
		return 1
	else:
		return 0

def removeDuplicates(scheduleList):
	i = 0
	while i < len(scheduleList):
		j = i + 1
		while j < len(scheduleList):
			

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

def nodeCompare(node1, node2):
	if node1.name == node2.name and node1.index == node2.index:
		return 1
	else:
		return 0
