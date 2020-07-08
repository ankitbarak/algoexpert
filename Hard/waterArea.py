# You are given an array of non-negative intergers where each non-zero integer represents the height
# of pillar of width 1. Imagine water being poured over all of the pillars;
# write a function that returns the surface area of the water trapped between the pillars
# viewed from the front. Note that spilled water should be ignored.

# O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for x in heights]
	leftMax = 0
	for i in range(len(heights)):
		height = heights[i]
		maxes[i] = leftMax
		leftMax = max(leftMax, height)
	rightMax = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		minHeight = min(rightMax, maxes[i])
		if height < minHeight:
			maxes[i] = minHeight - height
		else:
			maxes[i] = 0
		rightMax = max(rightMax, height)
	return sum(maxes)
