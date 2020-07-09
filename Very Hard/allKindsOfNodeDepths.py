# Write a function that takes in a Binary Tree and returns the sum of all
# its subtres nodes depths

# The distance between a node in a Binary Tree and the tre's root is called the node's depth

# O(nlog(n) time), O(h) space where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree

def allKindsOfNodeDepths(root):
    if root is None:
		return 0
	return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)

def nodeDepths(node, depth = 0):
	if node is None:
		return 0
	return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
