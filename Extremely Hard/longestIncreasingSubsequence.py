# Given a non-empty array of integers, write a function that returns the longest strictly
# increasing subsequence in the array.

# O(n^2) time, O(n) space
def longestIncreasingSubsequence(array):
    seq = [None for x in array]
	lengths = [1 for x in array]
	maxLengthIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
				lengths[i] = lengths[j] + 1
				seq[i] = j
		if lengths[i] >= lengths[maxLengthIdx]:
			maxLengthIdx = i
	return buildSeq(array, seq, maxLengthIdx)

def buildSeq(array, seqs, currentIdx):
	seq = []
	while currentIdx is not None:
		seq.append(array[currentIdx])
		currentIdx = seqs[currentIdx]
	return list(reversed(seq))