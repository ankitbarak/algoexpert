# Find two numbers in the array that sums to the target number
# O(nlogn) and O(1) space

def sum2num(arr, target):
	# Sort the array
	arr.sort()
	# Create two pointers
	left_pointer = 0
	right_pointer = len(arr) - 1
	while left_pointer < right_pointer:
		# Compute the sum based on current pointers
		current = arr[left_pointer] + arr[right_pointer]
		# If the sum is higher than the target, we move the right pointer to left
		if current > target:
			right_pointer -= 1
		# If the sum is lower than the target, we move the left pointer to right 
		elif current < target:
			left_pointer += 1
		# If they are equal, we return the corresponding number
		else:
			return [arr[left_pointer], arr[right_pointer]] 
	# If we cannot find any, then return an empty list
	return []
