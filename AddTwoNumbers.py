class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class SLinkedList:
	def __init__(self):
		self.val = None

	def l_print(self):
		number = ""
		while self.val:
			number += str(self.val.val)
			self.val = self.val.next
		retval = number
		return retval


	def reverseList(self):

		# Initializing values
		prev = None
		current = self.val
		nex = current.next


		# looping
		while current:
			# reversing the link
			current.next = prev

			# moving to next node
			prev = current
			current = nex
			if nex:
				nex = nex.next

		# initializing head
		self.val = prev




list1 = SLinkedList()

list1.val = Node(2)
e2 = Node(4)
e3 = Node(3)

list1.val.next = e2

e2.next = e3

list1.reverseList()
l1num = list1.l_print()

list2 = SLinkedList()

list2.val = Node(5)
e2 = Node(6)
e3 = Node(4)

list2.val.next = e2

e2.next = e3
list2.reverseList()
l2num = list2.l_print()

s = int(l1num) + int(l2num)
lst = [int(i) for i in str(s)]

l3 = SLinkedList()
l3.val = Node(lst[0])

for k, v in enumerate(reversed(lst[1:])):
	e = Node(v)
	list2.val.next = e2
l3.l_print()