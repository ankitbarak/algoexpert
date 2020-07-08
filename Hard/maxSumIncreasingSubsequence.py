# Write a function that takes in a non-empty array of integers and returns
# the greatest sum that can be generated from a strictly-increasing subsequence in the array
# as well as an array of the numbers in that subsequence.

def maxSumIncreasingSubsequence(array):
	seqs = [None for x in array]
	sums = [num for num in array]
	maxSumIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				seqs[i] = j
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
	return [sums[maxSumIdx], buildSequence(array, seqs, maxSumIdx)]
	

def buildSequence(array, seqs, currentIdx):
	seq = []
	while currentIdx is not None:
		seq.append(array[currentIdx])
		currentIdx = seqs[currentIdx]
	return list(reversed(seq))
	
