from StringToken import stringToken
from Stack import *

def logic(logicFile = "logic.in", classFile = "outFile", finalOutFile = "finalOutFile"):
	# I should implement this so it can output to a file
	logicText = logicFileParser(logicFile)
	fileText = classFileParser(classFile)

	# filter schedules
	for i in range(0, len(logicText)):
		if len(logicText[i]) == 1:
			fileText = filterOne(logicText[i][0], fileText)
	# all other cases must still be added

	printSchedules(fileText)

def logicFileParser(logicFile): # parse logic
	inputFile = open(logicFile, "r")
	logicText = stringToken("".join(stringToken(inputFile.read(), " ")), "\n") # removes all spaces, then separates on newlines
	inputFile.close()
	for i in range(0, len(logicText)): # replace newlines by generating a 2d list, with each element being a list of the desired elements
		logicText[i] = stringToken(logicText[i], "()&|", 'f')
	return logicText

def classFileParser(classFile):
	# parse schedule list
	inputFile = open(classFile, "r")
	fileText = stringToken(inputFile.read(), "\n")
	inputFile.close()
	for i in range(0, len(fileText)):
		fileText[i] = stringToken(fileText[i], " ")
	return fileText

def filterOne(filterClass, fileText): # removes all elements that do not contain the desired class
	i = 0
	length = len(fileText)
	while i < length:
		if contains(filterClass, fileText[i]) == False:
			del fileText[i]
			length -= 1
			i -= 1
		i += 1
	return fileText

def contains(filterClass, classList):
	for i in range(0, len(classList)):
		if classList[i] == filterClass:
			return True
	return False

def printSchedules(fileText):
	for i in range(0, len(fileText)):
		fileText[i] = " ".join(fileText[i])
	print("\n".join(fileText))

def testValidity():
	pass


