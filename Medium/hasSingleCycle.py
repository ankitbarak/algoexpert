# You are given an array of integers where each integer represents a jump of its value in the array.
# For instance, the integer 2 represents a jump of two indicies forward in the array; the integer -3
# represents a jump of three indicies backward in the array 

# If a jump spills past the array's bounds, it wraps over to the other side.
# For instance, a jump of -1 at index 0 brings us to the last index in the array.
# Similarly, a jump of 1 at the last index in the array brings us index 0.

# Write a function that returns a boolean representing whether the jumps in the array form a single
# cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element in
# array is visited exactly once before landing back on the starting index.

# O(n) time | O(1) space

def hasSingleCycle(array):
    numElementsVisited = 0
	currentIdx = 0
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		numElementsVisited += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0


def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
	