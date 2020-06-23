
# Compute the nth Fibonacci term. O(n) time with O(1) space

def getFib(n):
	fib2terms = [0, 1]
	counter = 3
	while n >= counter:
		nextterm = fib2terms[0] + fib2terms[1] 
		fib2terms[0] = fib2terms[1] 
		fib2terms[1] = nextterm
		counter += 1
	return fib2terms[1] if n > 1 else fib2terms[0]



