# Given an array of positive integers representing coin denominations and 
# and a single non-negative integer n representing a target amount of money
# write a function that returns the smallest number of coins needed to make
# change for that target amount using the givne coin denominations.

# If it is impossible to make change for the target amount, return -1
# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
	numOfCoins = [float("inf") for amount in range(n + 1)]
	numOfCoins[0] = 0
	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
	return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
    
