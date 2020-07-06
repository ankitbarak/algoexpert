# Write a function that takes in a non-empty array of integers
# and returns the maximum sum that can be obtained by summing up 
# all of the integers in a non-empty subarray of the input array. 
# A subarray must only contain adjacent numbers

# O(n) time | O(1) space - where n is the length of the input array
def kadanesAlgorithm(array):
	maxEndingHere = array[0]
	maxSoFar = array[0]
	for i in range(1, len(array)):
		num = array[i]
		maxEndingHere = max(num, maxEndingHere + num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	return maxSoFar
    