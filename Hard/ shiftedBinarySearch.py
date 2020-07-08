
# Write a function that takes in a sorted array of integers as well as a target integer.
# The function should use a variation of the Binary Search algorithm to detemine if the target integer
# is contained in the array and should return its index if it is , otherwise  - 1

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

# O(log(n)) time | O(1) space
def shiftedBinarySearchHelper(array, target, left, right):
	while left <= right:
		middle = (left + right) // 2
		potentialMatch = array[middle]
		leftNum = array[left]
		rightNum = array[right]
		if target == potentialMatch:
			return middle
		elif leftNum <= potentialMatch:
			if target < potentialMatch and target >= leftNum:
				right = middle - 1
			else:
				left = middle + 1
		else:
			if target > potentialMatch and target <= rightNum:
				left = middle + 1
			else:
				right = middle - 1
	return -1