# Write a function that takes in the head of a Singly Linked List and an integer k,
# shifts the list in place (i.e doesn't create a brand new list) by k positions, and return its new head.

def shiftLinkedList(head, k):
    listLength = 1
	listTail = head
	while listTail.next is not None:
		listTail = listTail.next
		listLength += 1
	
	offset = abs(k) % listLength
	if offset == 0:
		return head
	
	newTailPosition = listLength - offset if k > 0 else offset
	newTail = head
	for i in range(1, newTailPosition):
		newTail = newTail.next

	newHead = newTail.next
	newTail.next = None
	listTail.next = head
	return newHead


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
