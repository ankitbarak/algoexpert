# O(n) time and O(1) space

def longestPeak(array):
	# Set the counter for the peak length
    longestPeakLength = 0
    # Set a starting point from the second element of the array
	i = 1
	while i < len(array) - 1:
		# Determine whether the current element is greater than the previous and the next integer
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
		# If it is not a peak, we increment the index and skip to the next integer to be the current integer
		if not isPeak:
			i += 1
			continue
		# If it is a peak and left index is greater than zero and the right index is less than the length of the array, 
		# we then set a left index and right index to find the length of the peak
		leftIdx = i - 2
		# Keeps on decreasing the left index if the left index gives a smaller value to its right
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		rightIdx = i + 2
		# Keeps on increasing the right index if the right index gives a smaller value to its left
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
		# Compute the current peak length
		currentPeakLength = rightIdx - leftIdx - 1
		# Check whether the previous peak length is longer or the current one is longer, keep the longest
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		# continue our search from the end of our current peak
		i = rightIdx
	return longestPeakLength