# Write a function that takes in a Binary Tree (where nodes have an additional pointer
# to their parent node) and traverses it iteratively using the in-order tree-traversal technique;
# the traversal should specifically not use recursion. As the tree is being traversed,
# a callback function passed in as an argument to the main function should be called on each node


def iterativeInOrderTraversal(tree, callback):
    previousNode = None
	currentNode = tree
	while currentNode is not None:
		if previousNode is None or previousNode == currentNode.parent:
			if currentNode.left is not None:
				nextNode = currentNode.left
			else:
				callback(currentNode)
				nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
		elif previousNode == currentNode.left:
			callback(currentNode)
			nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
		else:
			nextNode = currentNode.parent
		previousNode = currentNode
		currentNode = nextNode
		
			
