# You are given an array of integers and an integer. Write a 
# function that moves all instances of that integer in the array
# to the end of the array and returns the array
# The function should perform this in place (i.e. it should mutate the input array)
# and doesn't need to maintain the order of the other integers.
# We have two solutions here
def moveElementToEnd(array, toMove):
	"""
		O(n) time and O(n) space
	"""
	yesList = []
	noList = []
	for i in array:
		if i == toMove:
			yesList.append(i)
		else:
			noList.append(i)
	return noList + yesList


def moveElementToEnd2(array, toMove):
	"""
		O(n) time and O(1) space
	"""
	left = 0
	right = len(array) - 1
	while left < right:
		while left < right and array[right] == toMove:
			right -= 1
		if array[left] == toMove:
			swap(left, right, array)
		left += 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]




