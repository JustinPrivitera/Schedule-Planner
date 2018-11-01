from StringToken import stringToken

def parse(fileText):
	dataList = stringToken(fileText, "\n\t")
	classList = []
	i = 0
	while i < len(dataList): # populates the array
		classList.append([dataList[i], dataList[i + 1], dataList[i + 2]])
		i += 3
	return classList

def convertTimesToInts(classList):
	for i in range(0, len(classList)):
		classList[i][1] = int(classList[i][1])
		classList[i][2] = int(classList[i][2])
	return classList
