from StringToken import stringToken
from Stack import *

def logic(logicFile = "logic.in", classFile = "outFile", finalOutFile = "finalOutFile"):
	# I should implement this so it can output to a file
	logicText = logicFileParser(logicFile)
	fileText = classFileParser(classFile)

	# filter schedules
	# for i in range(0, len(logicText)):
	# 	if len(logicText[i]) == 1:
	# 		fileText = filterOne(logicText[i][0], fileText)
	# all other cases must still be added

	printSchedules(fileText)

def logicFileParser(logicFile): # parse logic
	inputFile = open(logicFile, "r")
	logicText = stringToken("".join(stringToken(inputFile.read(), " ")), "\n") # removes all spaces, then separates on newlines
	inputFile.close()
	for i in range(0, len(logicText)): # replace newlines by generating a 2d list, with each element being a list of the desired elements
		logicText[i] = stringToken(logicText[i], "()&|", 'f')
	return logicText

def classFileParser(classFile): # parse schedule list
	inputFile = open(classFile, "r")
	fileText = stringToken(inputFile.read(), "\n")
	inputFile.close()
	for i in range(0, len(fileText)):
		fileText[i] = stringToken(fileText[i], " ")
	return fileText

def concatenateStatements(logicText): # transforms logicText from a list of statements to one huge statement
	for i in range(0, len(logicText)):
		if len(logicText[i]) > 1:
			logicText[i].insert(0, "(")
			logicText[i].append(")")
	newText = []
	# 3 cases
	# case (i): there is only one statement
	if len(logicText) == 1:
		newText.extend(logicText[0])
	# case (ii): there are two statements
	else:
		newText.extend(logicText[0])
		newText.append("&")
		newText.extend(logicText[1])
		# case (iii): there are more than 2 statements
		if len(logicText) > 2:
			for i in range(2, len(logicText)):
				newText.insert(0, "(")
				newText.append(")")
				newText.append("&")
				newText.extend(logicText[i])
	return newText

# def filterOne(filterClass, fileText): # removes all elements that do not contain the desired class
# 	i = 0
# 	length = len(fileText)
# 	while i < length:
# 		if contains(filterClass, fileText[i]) == False:
# 			del fileText[i]
# 			length -= 1
# 			i -= 1
# 		i += 1
# 	return fileText

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

def applyLogic(logicText, fileText): # both are 2d lists
	pass

	#--------forget the below--------
	# for each logical statement of logicText
	# for i in range(0, len(fileText)):
		# I think if there's only one thing in the list then we can apply much simpler logic
		# for each functional unit of the logical statement
			# for every element of the functional unit
			# count = countOperands(logicText[j])
			# for k in range(0, count):
				# I want to run it as an imperative against the classlist, creating a result as a 1-dimensional list
			# then I want to compare each output of the functional unit to it's corresponding operand output, applying logic as necessary to either limit or expand the output
			# or the other case is that there is only one operand
		# then I want to save the results, probably as a 2d list again

def indexOfUnboundedOperator(logicStatement): # logicStatement is a list of logical operands, operators, and parentheses
	parenCount = 0
	for i in range(0, len(logicStatement)):
		if logicStatement[i] == "(":
			parenCount += 1
		elif logicStatement[i] == ")":
			parenCount -= 1
		if ___:
			return i
	return -1

# def countOperands(logicStatement):
# 	count = 0
# 	for i in range(0, logicStatement):
# 		if logicStatement[i] != "(" or logicStatement[i] != ")" or logicStatement[i] != "&" or logicStatement[i] != "|":
# 			count += 1
# 	return count
