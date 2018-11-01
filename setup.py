from StringToken import stringToken

def parse(fileText):
	dataList = stringToken(fileText, "\n\t")
	classList = []
	imperative = False
	i = 0
	j = 0
	while i < len(dataList):
		if '#' in dataList[i]:
			j += 1
			imperative = True
			break
		i += 1
	i = j
	while i < len(dataList): # populates the array
		classList.append([dataList[i], dataList[i + 1], dataList[i + 2]])
		i += 3

	impList = []
	if imperative == True:
		impList = stringToken(dataList[0], "#")
	return [classList, impList]

def convertTimesToInts(classList):
	for i in range(0, len(classList)):
		classList[i][1] = int(classList[i][1])
		classList[i][2] = int(classList[i][2])
	return classList
