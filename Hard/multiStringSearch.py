# Write a function that takes in a big string and an array of small strings,
# all of which are smaller in length than the big string. The function should return
# an array of booleans, where each boolean represents whether the small string at that index in the array
# of small strings is contained in the big string

# Note that you can't use language-built in string matching methods

# O(bns) time, O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
	for i in range(len(bigString)):
		if i + len(smallString) > len(bigString):
			break
		if isInBigStringHelper(bigString, smallString, i):
			return True
	return False

def isInBigStringHelper(bigString, smallString, startIdx):
	leftBigIdx = startIdx
	rightBigIdx = startIdx + len(smallString) - 1
	leftSmallIdx = 0
	rightSmallIdx = len(smallString) - 1
	while leftBigIdx <= rightBigIdx:
		if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
			return False
		leftBigIdx += 1
		rightBigIdx -= 1
		leftSmallIdx += 1
		rightSmallIdx -= 1
	return True
