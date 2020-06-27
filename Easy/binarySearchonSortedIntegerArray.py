"""
Implement binary search for a sorted array of integers with a target integer

"""

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
	while left <= right:
		middle = (left + right) // 2 # round down after dividing by 2
		element = array[middle]
		if target == element:
			return middle
		elif target < element:
			right = middle - 1
		else:
			left = middle + 1
	return -1
		
		
	
	
