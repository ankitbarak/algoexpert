# Write a function that takes a list of blocks and a list of your required buildings
# and that returns the location (the index) of the block that's most optimal for you.

def apartmentHunting(blocks, reqs):
    minDistFromBlocks = list(map(lambda req: getMinDist(blocks, req), reqs))
	maxDistAtBlocks = getMaxDistAtBlocks(blocks, minDistFromBlocks)
	return getIdxAtMinValue(maxDistAtBlocks)

def getMinDist(blocks, req):
	minDist = [0 for block in blocks]
	closestReqIdx = float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqIdx = i
		minDist[i] = distanceBetween(i, closestReqIdx)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIdx = i
		minDist[i] = min(minDist[i], distanceBetween(i, closestReqIdx))
	return minDist

def getMaxDistAtBlocks(blocks, minDistFromBlocks):
	maxDistAtBlocks = [0 for block in blocks]
	for i in range(len(blocks)):
		minDistAtBlocks = list(map(lambda distances:distances[i], minDistFromBlocks))
		maxDistAtBlocks[i] = max(minDistAtBlocks)
	return maxDistAtBlocks

def getIdxAtMinValue(array):
	idxAtMinValue = 0
	minValue = float("inf")
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue

def distanceBetween(a,b):
	return abs(a - b)

