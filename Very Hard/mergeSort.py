# Write a function that takes in array of integers and returns a sorted version of that array
# Use the merge sort algorithm to sort the array

# Best: O(n log n) time O(n log n ) space
# Worst: O(n log n) time , O(n log n) space
def mergeSort(array):
	if len(array) == 1:
		return array
	middleIdx = len(array) // 2
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		k += 1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	return sortedArray
    