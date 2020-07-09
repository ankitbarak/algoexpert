# Write a function that takes in a sequare-shaped n by n two dimensional array of only 1s
# and 0s and returns a boolean representing whether the input matrix contains a square whose boarders are
# made up of only 0s.

# Note that a 1x1 square doesn't count as a valid square for the purpose of this question. In other words,
# a singular 0 in the input matrix doesn't constitute a square whose boarders are made up of 
# only 0s; a square of zeros has to be at least 2 x 2.

# O(n^3) time, O(n^2) space, n = the height and width of the matrix 
def squareOfZeroes(matrix):
    infoMatrix = preComputeNumOfZeros(matrix)
	n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol + squareLength - 1
				if isSquareOfZeros(infoMatrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False

# r1 is the top row, c1 is the left col
# r2 is the bottom row, c2 is the right col

def isSquareOfZeros(infoMatrix, r1, c1, r2, c2):
	squareLength = c2 - c1 + 1
	hasTopBoarder = infoMatrix[r1][c1]["numZerosRight"] >= squareLength
	hasLeftBoarder = infoMatrix[r1][c1]["numZerosBelow"] >= squareLength
	hasBottomBoarder = infoMatrix[r2][c1]["numZerosRight"] >= squareLength
	hasRightBoarder = infoMatrix[r1][c2]["numZerosBelow"] >= squareLength
	return hasTopBoarder and hasLeftBoarder and hasBottomBoarder and hasRightBoarder

def preComputeNumOfZeros(matrix):
	infoMatrix = [[x for x in row] for row in matrix]
	n = len(matrix)
	for row in range(n):
		for col in range(n):
			numZeros = 1 if matrix[row][col] == 0 else 0
			infoMatrix[row][col] = {
				"numZerosBelow": numZeros,
				"numZerosRight": numZeros,
			}
	lastIdx = len(matrix) - 1
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < lastIdx:
				infoMatrix[row][col]["numZerosBelow"] += infoMatrix[row + 1][col]["numZerosBelow"]
			if col < lastIdx:	
				infoMatrix[row][col]["numZerosRight"] += infoMatrix[row][col + 1]["numZerosRight"]
	return infoMatrix