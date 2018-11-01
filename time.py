def getTimeList(classList):
	timeList = []
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
