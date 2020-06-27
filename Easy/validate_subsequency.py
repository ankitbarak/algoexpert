

def isValidSubsequence(array, sequence):
    """
    	Given two non-empty arrays of integers, write a function to determine whether the second array is a subsequence of the first one.
    """
	arridx = 0
	seqidx = 0
	while arridx < len(array) and seqidx < len(sequence):
		if array[arridx] == sequence[seqidx]:
			seqidx += 1
		arridx += 1
	return seqidx == len(sequence)