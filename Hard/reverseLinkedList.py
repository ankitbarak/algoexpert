# Write a function that takes in the head of a Singly Linked List,
# reverses the list in place (i.e. doesn't create a brand new list), and 
# reutrns its new head.

# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def reverseLinkedList(head):
    p1, p2 = None, head
	while p2 is not None:
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
	return p1
