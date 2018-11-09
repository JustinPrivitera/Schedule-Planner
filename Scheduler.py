from setup import *
from time import *
from node import *
from MergeSort import merge_sort
from logic import logic

#def scheduler(inFile, outFile):
def scheduler(numClasses = 0, inFile = "inFile", outFile = "outFile"):
	inputFile = open(inFile, "r")
	fileText = inputFile.read()
	inputFile.close()
	outputFile = open(outFile, "w")

	initClassList = parse(fileText)
	imperativeList = initClassList[1]
	classList = convertTimesToInts(initClassList[0])
	scheduleList = generateSchedules(fillScheduleWithClassList(classList), classList)

	# printScheduleList(scheduleList, numClasses, imperativeList)
	writeScheduleList(scheduleList, numClasses, imperativeList, outputFile)

	#timeList = getTimeList(classList)

	outputFile.close()

	logic()
	print()

def fillScheduleWithClassList(classList):
	scheduleList = []
	for i in range(0, len(classList)):
		newnode = node(classList[i][0], i)
		scheduleList.append([newnode])
	return scheduleList

def printScheduleList(scheduleList, numClasses, imperativeList):
	for i in range(0, len(scheduleList)):
		if numClasses == 0 or len(scheduleList[i]) == numClasses:
			if containsAll(scheduleList[i], imperativeList) or len(imperativeList) == 0:
				for j in range(0, len(scheduleList[i])):
					print(scheduleList[i][j].name, end = " ")
				print()

def writeScheduleList(scheduleList, numClasses, imperativeList, outputFile):
	for i in range(0, len(scheduleList)):
		if numClasses == 0 or len(scheduleList[i]) == numClasses:
			if containsAll(scheduleList[i], imperativeList) or len(imperativeList) == 0:
				for j in range(0, len(scheduleList[i])):
					outputFile.write(scheduleList[i][j].name + " ")
				outputFile.write("\n")

def generateSchedules(scheduleList, classList):
	i = 0
	while i < len(scheduleList):
		j = i + 1
		while j < len(scheduleList):
			if checkLists(scheduleList[i], scheduleList[j], classList) == 1:
				scheduleList.append(merge_sort(scheduleList[i] + scheduleList[j]))
			j += 1
		i += 1
	return removeDuplicates(scheduleList)

def checkLists(list1, list2, classList): # the lists are lists of nodes; returns a 1 if there are no conflicts or duplicates, returns a 0 if there is a conflict or duplicate
	if checkDuplicates(list1, list2) == 1: # if there are no duplicates
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

def checkDuplicates(list1, list2): # returns 0 if there is a duplicate and 1 if there are none
	i = 0
	while i < len(list1):
		j = 0
		while j < len(list2):
			if nodeCompare(list1[i], list2[j]) == 1: # if the nodes are the same
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
			if len(scheduleList[i]) == len(scheduleList[j]):
				diff = False
				for k in range(0, len(scheduleList[i])):
					if nodeCompare(scheduleList[i][k], scheduleList[j][k]) == 0:
						diff = True
						break
				if diff == False:
					del scheduleList[j]
					j -= 1
			j += 1
		i += 1
	return scheduleList
