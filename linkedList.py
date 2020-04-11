#Linked List implementation

class Node:
	data = None
	next = None

	def __init__(self, d):
		self.data = d

class LinkedList:
	head = None

	def __init__(self, d):
		self.head = Node(d)

	def insert(self, d):
		newNode = Node(d)
		n = self.head
		while(n.next!=None):
			n = n.next
		n.next = newNode

	def delete(self, d):
		n = self.head
		if n.data==d:
			head = n.next
			return
		while n.next!=None:
			if n.next.data==d:
				n.next = n.next.next
				return
			n = n.next

	def tail(self):
		n = self.head
		while n.next!=None:
			n = n.next
		return n.data

	def printList(self):
		n = self.head
		while n!=None:
			print(n.data)
			n = n.next

#l = LinkedList(1)
#l.printList()