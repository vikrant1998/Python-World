# Definition for singly-linked list node.
class ListNode(object):

	# Create a new node.
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for singly linked list.
class LinkedList(object):

	# Initialize the linked list.
	def __init__(self):
		self.head = None
	
	# Add a node to the end of the linked list.
	def AddNode(self, x):
		newNode = self.head
		
		# If the list is empty.
		if(newNode == None):
			newNode = ListNode(x)
			self.head = newNode
			return
		
		# If the list is not empty.
		while(newNode.next != None):
			newNode = newNode.next
	
		newNode.next = ListNode(x)
		return
		
	# Print all the nodes of a linked list.
	def PrintNodes(self):
		tempNode = self.head
		
		print ('Nodes:')
		while (tempNode != None):
			print (tempNode.val)
			tempNode = tempNode.next
			
		print('')
		return
		
	# Delete first occurence of a node.
	def DeleteFirstOccurence(self, x):
		tempNode = self.head
		
		# If the list is empty.
		if (tempNode == None):
			return
			
		# Element at the head.
		if (tempNode.val == x):
			nextNode = tempNode.next
			del(tempNode)
			self.head = nextNode
			return

		# Find the node to delete.
		while (tempNode.next != None and tempNode.next.val != x):
			tempNode = tempNode.next
	
		# Can delete the next one.
		if (tempNode.next != None and tempNode.next.val == x):
			nextFinal = tempNode.next.next
			del (tempNode.next)
			tempNode.next = nextFinal
		
		return
		
	# Delete all occurences of a value.
	def DeleteAllOccurences(self, val):
		
		# Empty list.
		if (self.head == None):
			return

		# Delete the elements in the front.
		tempNode = self.head
		while (tempNode != None and tempNode.val == val and tempNode == self.head):
			nextNode = tempNode.next
			del(tempNode)
			tempNode = nextNode
			self.head = tempNode
			
		# Delete the rest of the elements.
		tempNode = self.head
		while (tempNode != None):
			if (tempNode.next != None and tempNode.next.val == val):
				nextNode = tempNode.next.next
				del(tempNode.next)
				tempNode.next = nextNode
			else:
				tempNode = tempNode.next
			
	
if __name__ == "__main__":
	l = LinkedList()
	l.AddNode(1)
	l.AddNode(1)
	l.AddNode(1)
	l.AddNode(2)
	l.AddNode(3)
	l.AddNode(1)
	l.AddNode(1)
	
	l.DeleteAllOccurences(2)
	l.PrintNodes()