
# Given a target and a BST, find the value in a BST that is closest to the target.

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest
		
		
	
