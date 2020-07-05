# Write a function that takes in a non-empty sorted array of distinct integers, construct a BST from the integers, and returns the root of the BST.  
# O(nlog(n)) time | O(n) space 

def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)

def constructMinHeightBst(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]
	if bst is None:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)
	constructMinHeightBst(array, bst, startIdx, midIdx - 1)
	constructMinHeightBst(array, bst, midIdx + 1, endIdx)
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
