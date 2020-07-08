# Write a function that takes in the heads of two Singly Linked Lists
# that are in sorted order, respectively. The function should merge the lists
# in place (i.e. it shouldn't create a brand new list) and return the 
# head of the merged list; the merged list should be in sorted order.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(1) space, whee n is number of nodes in the first 
# linked list and m is the number of nodes in the second linked list
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
	p1Prev = None
	p2 = headTwo
	while p1 is not None and p2 is not None:
		if p1.value < p2.value:
			p1Prev = p1
			p1 = p1.next
		else:
			if p1Prev is not None:
				p1Prev.next = p2
			p1Prev = p2
			p2 = p2.next
			p1Prev.next = p1
	if p1 is None:
		p1Prev.next = p2
	return headOne if headOne.value < headTwo.value else headTwo

