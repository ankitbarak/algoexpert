# Given a binary search tree, compute the sum of the depth from the root for each node 

def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
# This is the class of the input binary tree.

class BinaryTree:
	def __init__(self, value):
		self.value = value
        self.left = None
        self.right = None

