# Check a given array of integers whether or not it is non-increasing or non-decreasing

def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			isNonDecreasing = False
		if array[i] > array[i - 1]:
			isNonIncreasing = False
			
	return isNonDecreasing or isNonIncreasing
	