"""
Check if a string is a palidrome.
"""
def isPalindrome(string):
    leftpointer = 0
	rightpointer = len(string) - 1
	endpoint = len(string) // 2
	while leftpointer < endpoint:
		if string[leftpointer] != string[rightpointer]:
			return False
		leftpointer  += 1
		rightpointer -= 1
	return True
	