# Write a function that takes in a non-negative integer n and returns the number of possible Binary
# Tree topologies that can be created with exactly n ndoes.

# O(n^2) time, O(n) time
def numberOfBinaryTreeTopologies(n):
    cache = [1]
	for m in range(1, n + 1):
		numberOfTrees = 0
		for leftTreeSize in range(m):
			rightTreeSize = m - 1 - leftTreeSize
			numberOfLeftTrees = cache[leftTreeSize]
			numberOfRightTrees = cache[rightTreeSize]
			numberOfTrees += numberOfLeftTrees * numberOfRightTrees
		cache.append(numberOfTrees)
	return cache[n]
