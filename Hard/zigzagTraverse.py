# Wrtie a function that takes in an n x m two dimensional array (that can be square-shaped when n === m)
# and returns a one-dirmensional array of all the array's elements in zigzag order.
# Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element,
# and proceeds in a zigzag pattern all the way to the bottom right corner

def zigzagTraverse(array):
	height = len(array) - 1
	width =len(array[0]) - 1
	result = []
	row, col = 0, 0
	goingDown = True
	while not isOutOfBounds(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else: 
				row -= 1
				col += 1
	return result

def isOutOfBounds(row, col, height, width):
	return row < 0 or row > height or col < 0 or col > width
