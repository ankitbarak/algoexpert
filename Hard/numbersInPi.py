# Given a string representation of the first n digits of Pi and a list of positive integers
# (all in string format), write a function that returns the smallest number of spaces that can be
# added to the n digits of Pi such that all resulting numbers are found in the list integers.

# If no number of spaces to be added exists such that all resulting numbers are found in the list of
# integers, the function should return -1

# O(n^3 + m) time | O(n + m) space, where n is the number of digits in Pi and m is the number of favorite numbers
def numbersInPi(pi, numbers):
	numbersTable = {number: True for number in numbers}
	minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
	return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbersTable, cache, idx):
	if idx == len(pi):
		return -1
	if idx in cache:
		return cache[idx]
	minSpaces = float("inf")
	for i in range(idx, len(pi)):
		prefix = pi[idx: i + 1]
		if prefix in numbersTable:
			minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)
	cache[idx] = minSpaces
	return cache[idx]
    
