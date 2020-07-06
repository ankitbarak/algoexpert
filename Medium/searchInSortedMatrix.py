
# Write a function that returns an array of the row and column indicies of the target integer if it's
# contained in the matrix, otherwise [-1, -1]

# O(n + m) time | O(1) space 
def searchInSortedMatrix(matrix, target):
    row = 0
	col = len(matrix[0]) -1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row, col]
	return [-1, -1]