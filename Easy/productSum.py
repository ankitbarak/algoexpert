"""
Write a function that takes in a special array and return its product sum.
A special array is an non-empty array that contains either integers or othe "special" arrays
The product sum of a "special" array is the sume of its elements, where "special" arrays inside it
are summed themsevles and then multiplied by their level of depth
"""

def productSum(array, mult = 1):
	sums = 0
    for element in array:
		if type(element) is list:
			sums += productSum(element, mult + 1)
		else:
			sums += element
	return sums * mult
			
	