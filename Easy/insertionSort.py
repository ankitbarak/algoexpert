def insertionSort(array):
	"""
		Best case: O(n) time and O(1) space
		Average: O(n^2) time and O(1) space
		Worst O(n^2) time | O(1) space
	"""
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j - 1, array)
			j -= 1
	return array

def swap(i, j, arr):
	arr[i], arr[j] = arr[j], arr[i]
		
		
