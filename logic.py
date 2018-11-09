from StringToken import stringToken

def logic(logicFile = "logic.in", classFile = "outFile", finalOutFile = "finalOutFile"):
	# I should implement this so it can output to a file
	logicText = logicFileParser(logicFile)
	fileText = classFileParser(classFile)

	# filter schedules
	fileText = funcUnitEval(concatenateStatements(logicText), fileText)

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

def concatenateStatements(logicText): # transforms logicText from a list of statements to one huge statement (2d to 1d list)
	if len(logicText) > 1:
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

def printSchedules(fileText):
	fileText = "\n".join(fileText)
	if fileText == "":
		print("No schedules match the given criteria.")
	print(fileText)

def testValidity():
	pass

def funcUnitEval(logicStatement, fileText):
	opIndex = indexOfUnboundedOperator(logicStatement)
	if opIndex == -1:
		return translate(applyImperative(logicStatement[0], fileText))
	else:
		op = logicStatement[opIndex]
		op1 = encode(funcUnitEval(filterParentheses(logicStatement[0 : opIndex]), fileText))
		op2 = encode(funcUnitEval(filterParentheses(logicStatement[opIndex + 1 : len(logicStatement)]), fileText))
		return evaluate(op1, op, op2)

def filterParentheses(logicStatement):
	if logicStatement[0] == "(" and logicStatement[len(logicStatement) - 1] == ")":
		return logicStatement[1 : len(logicStatement) - 1]
	return logicStatement

def evaluate(op1, op, op2): # translaton will be a problem
	op1 = translate(op1)
	op2 = translate(op2)
	if op == "&":
		return evalAnd(op1, op2)
	if op == "|":
		return evalOr(op1, op2)
	return []

def evalAnd(cList1, cList2): # the parameters are 1 dimentsional lists, since the 2nd dimension was turned into strings
	rList = []
	for i in range(0, len(cList1)):
		for j in range(0, len(cList2)):
			if cList1[i] == cList2[j]:
				rList.append(cList1[i])
				break
	return rList

def evalOr(cList1, cList2): # the parameters are 1 dimentsional lists, since the 2nd dimension was turned into strings
	rList = []
	rList.extend(cList1)
	rList.extend(cList2)
	return removeDuplicates(rList)

def removeDuplicates(alist):
	i = 0
	length = len(alist)
	while i < length:
		j = i + 1
		while j < length:
			if alist[i] == alist[j]:
				del alist[i]
				i -= 1
				length -= 1
				break
			j += 1
		i += 1
	return alist

def translate(classList):
	if isinstance(classList[0], list):
		for i in range(0, len(classList)):
			classList[i] = " ".join(classList[i])
			# print(classList[i])
		return classList
	else:
		return classList

def encode(classList):
	for i in range(0, len(classList)):
		classList[i] = stringToken(classList[i], " ")
		# print(classList[i][0])
	return classList

def applyImperative(filterClass, classList): # removes all elements that do not contain the desired class
	i = 0
	newList = classList.copy()
	length = len(newList)
	while i < length:
		if contains(filterClass, newList[i]) == False:
			del newList[i]
			length -= 1
			i -= 1
		i += 1
	return newList

def contains(filterClass, classList):
	for i in range(0, len(classList)):
		if classList[i] == filterClass:
			return True
	return False

def indexOfUnboundedOperator(logicStatement): # logicStatement is a list of logical operands, operators, and parentheses
	parenCount = 0
	for i in range(0, len(logicStatement)):
		if logicStatement[i] == "(":
			parenCount += 1
		elif logicStatement[i] == ")":
			parenCount -= 1
		if parenCount == 0 and (logicStatement[i] == "&" or logicStatement[i] == "|"):
			return i
	return -1
