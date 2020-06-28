# Worst: O(n^2) time O(1) space
# Best: O(n^2) time O(1) space

def selectionSort(array):
    # find the smallest number in the array
	currentIdx = 0
	while currentIdx < len(array) - 1:
		smallestIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx = i
		# Once we have found the smallest number, swap the two
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array
	
			
def swap(i , j, array):
	array[i], array[j] = array[j], array[i]
	Palindrome

if __name__ == '__main__':
	s = "abc"
	key = 2
	print(ord(s[0]))
	print(chr(ord(s[0])))
	print(chr(ord(s[0])+ key))

		
