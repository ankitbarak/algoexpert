# Write a function that takes in an array of integers and returns an array of 
# the same length, where each element in the output array corresponds to the number of integers
# in the input array that are to the right of the relevant index and that are strictly smaller than the integer at that index.

# In other words, the value at output[i] represents the number of integers that are to the right of i
# and that are strictly smaller than imput[i]

def rightSmallerThan(array):
    rightSmallerCounts = []
	for i in range(len(array)):
		rightSmallerCount = 0
		for j in range(i + 1, len(array)):
			if array[j] < array[i]:
				rightSmallerCount += 1
		rightSmallerCounts.append(rightSmallerCount)
	return rightSmallerCounts
