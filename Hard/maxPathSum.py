# Write a function that takes in a Binary Tree and returns its max path sum
# A path is a collection of connected nodes in a tree where no node is connected to more than two
# other nodes; a path sum is the sum of the values of the nodes in a particular path

def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	if tree is None:
		return(0, float("-inf"))
	leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
	rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
	maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
	
	value = tree.value
	maxSumAsBranch = max(maxChildSumAsBranch + value, value)
	maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
	maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
	return(maxSumAsBranch, maxPathSum)