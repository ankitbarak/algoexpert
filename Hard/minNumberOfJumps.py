# You are given a non-empty array of positive integers where each integer represents the maximum
# number of steps you can take forward in the array. For example, if the element at index 1 is 3,
# you can go from index 1 to index 2, 3 or 4.
# Write a function that returns the minimum number of jumps needed to reach the final index

# O(n) time | O(1) space
def minNumberOfJumps(array):
    if len(array) == 1:
		return 0
	jumps = 0
	maxReach = array[0]
	steps = array[0]
	for i in range(1, len(array) - 1):
		maxReach = max(maxReach, i + array[i])
		steps -= 1
		if steps == 0:
			jumps += 1
			steps = maxReach - i
	return jumps + 1