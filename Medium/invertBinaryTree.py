# Write a function that takes in a Binary Tree and inverts it. In other words, 
# the function should swap every left node in the tree for its corresponding right node.

#O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current is None:
			continue
		swapLeftAndRight(current)
		queue.append(current.left)
		queue.append(current.right)
			
def swapLeftAndRight(tree):
	tree.left, tree.right = tree.right, tree.left
