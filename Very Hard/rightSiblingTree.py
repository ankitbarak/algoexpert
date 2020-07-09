# Write a function that takes in a Binary Tree, transforms it into a 
# Right Sibling Tree and ruturns its root.

# A Right Sibling Tree is obtained by making every node in a Binary Tree have its right
# property point to its right sibling (the node immediately to its right one the same level)
# instead of its right child

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    mutate(root, None, None)
	return root

def mutate(node, parent, isLeftChild):
	if node is None:
		return
	left, right = node.left, node.right
	mutate(left, node, True)
	if parent is None:
		node.right = None
	elif isLeftChild:
		node.right = parent.right
	else:
		if parent.right is None:
			node.right = None
		else:
			node.right = parent.right.left
	mutate(right, node, False)
	
