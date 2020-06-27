"""
Summing all the branches in a binary search tree.
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	ls = []
	computeBranchSums(root, 0, ls)
	return ls
		
def computeBranchSums(node, currentSum, ls):
	if node is None:
		return
	new_currentSum = currentSum + node.value
	if node.left is None and node.right is None:
		ls.append(new_currentSum)
		return
	computeBranchSums(node.left, new_currentSum, ls)
	computeBranchSums(node.right, new_currentSum, ls)
