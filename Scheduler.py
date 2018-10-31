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

def scheduler(inFile, outFile)
	inputFile = open(inFile, "r")
	fileText = inputFile.read()
	inputFile.close()
	outputFile = open(outFile, "w")

	classList = stringToken(fileText, "\n\t")

	#outputFile.write(stuff)
	outputFile.close()
