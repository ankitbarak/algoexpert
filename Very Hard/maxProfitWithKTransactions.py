# You are given an array of positive integers representing the prices of 
# a single stock on various days (each index in the array represents a different dat).
# You are also given an integer k, which represents the number of transcations you're allowed to make.
# One transaction consists of buying the stock on a given day and selling it on another, later day.

# Write a function that returns the maximum profit that you can make by buying
# and selling the stock, given k transcation.

# Note that you can only hold one share of the stock at a time; in other words, you can't buy more
# than one share of the stock on any given day, and you can't buy a share of the stock if you are still
# holding another share. Also, you don't need to use all k transcation that you are allowed.

# O(nk) time , O(n) space
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	evenProfits = [0 for d in prices]
	oddProfits = [0 for d in prices]
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		if t % 2 == 1:
			currentProfits = oddProfits
			previousProfits = evenProfits
		else:
			currentProfits = evenProfits
			previousProfits = oddProfits
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
			currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
	return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]