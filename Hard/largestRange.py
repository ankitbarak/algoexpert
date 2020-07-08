# Write a function that takes an array of integers and returns an array
# of length 2 representing the largest range of integers contained in that array.

# The first number in the output array should be the first number in the range while 
# the second number should be the last number in the range

def largestRange(array):
    bestRange = []
	longestLength = 0
	nums = {}
	for num in array:
		nums[num] = True
	for num in array:
		if not nums[num]:
			continue
		nums[num] = False
		currentLength = 1
		left = num - 1
		right = num + 1
		while left in nums:
			nums[left] = False
			currentLength += 1
			left -= 1
		while right in nums:
			nums[right] = False
			currentLength += 1
			right += 1
		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left + 1, right - 1]
	return bestRange
