# Write a function that takes in an array of unique integers and returns
# an array of all permutations of those integers in no particular order

def getPermutations(array):
    permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, currentPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i + 1:]
			newPermutation = currentPermutation + [array[i]]
			permutationsHelper(newArray, newPermutation, permutations)