# O(n) time and O(n) space
# Write a function that takes in an n by m two dimensional array and returns a one-dimensional array 
# of all the array's elements in spiral order. Spiral order starts at the top left corner of the two
# dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element
# has been visited.

def spiralTraverse(array):
    result = []
	startRow, endRow = 0, len(array) - 1
	startCol, endCol = 0, len(array[0]) - 1
	
	while startRow <= endRow and startCol <= endCol:
		for col in range(startCol, endCol + 1):
			result.append(array[startRow][col])
			
		for row in range(startRow + 1, endRow + 1):
			result.append(array[row][endCol])
			
		for col in reversed(range(startCol, endCol)):
			if startRow == endRow:
				break
			result.append(array[endRow][col])
			
		for row in reversed(range(startRow + 1, endRow)):
			if startCol == endCol:
				break
			result.append(array[row][startCol])
		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1
		
	return result
