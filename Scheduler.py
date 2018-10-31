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

	classList = parse(fileText)
	timeList = getTimeList(classList)

	returnList

	#outputFile.write(stuff)
	#outputFile.close()

def parse(fileText):
	dataList = stringToken(fileText, "\n\t")
	classList = [][]
	tempList = []
	j = 0
	i = 0
	while i < len(dataList): # populates the array
		tempList.append(dataList[i])
		tempList.append(dataList[i + 1])
		tempList.append(dataList[i + 2])
		i += 3
		classList[j] = tempList
		j += 1
	return classList

def getTimeList(classList):
	timeList = [][]
	for i in range(0, len(classList)):
		timeList[i] = getNumbersBetween(classList[i][1], classList[i][2])
	return timeList

def getNumbersBetween(upper, lower):
	numList = []
	i = lower
	while i <= upper:
		 numList.append(i)
		 i += 1
	return numList
