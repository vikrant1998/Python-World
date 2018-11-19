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
				
	# Remove duplicates from sorted list.
	def RemoveDuplicatesFromSortedList(self):
	
		# Empty list.
		if (self.head == None):
			return

		# Iterate through the list and delete.
		tempNode = self.head
		while (tempNode != None and tempNode.next != None):
			if (tempNode.val == tempNode.next.val):
				nextNode = tempNode.next.next
				del(tempNode.next)
				tempNode.next = nextNode
			else:
				tempNode = tempNode.next
	
# Add node to end of the list.
def AddNewNode(head, val):
	if (head == None):
		head = ListNode(val)
		return head
	
	tempNode = head
	while (tempNode.next != None):
		tempNode = tempNode.next
	
	tempNode.next = ListNode(val)
	return head
		

# Merge two sorted lists.
def MergeTwoSortedLists(l1, l2):
	
	newList = None
	# If one of the lists is empty.
	if (l1 == None):
		newList = l2
		return newList
	if (l2 == None):
		newList = l1
		return newList
	
	l1Temp = l1
	l2Temp = l2
	
	# Iterate through both the lists.
	while (l1Temp != None and l2Temp != None):
		if (l1Temp.val < l2Temp.val):
			newList = AddNewNode(newList, l1Temp.val)
			l1Temp = l1Temp.next
		else:
			newList = AddNewNode(newList, l2Temp.val)
			l2Temp = l2Temp.next
		
	# Rest of list1.
	while (l1Temp != None):
		newList = AddNewNode(newList, l1Temp.val)
		l1Temp = l1Temp.next
		
	# Rest of list2.
	while (l2Temp != None):
		newList = AddNewNode(newList, l2Temp.val)
		l2Temp = l2Temp.next

	return newList
				
if __name__ == "__main__":
	l1 = None
	l1 = AddNewNode(l1, 1)
	l1 = AddNewNode(l1, 3)
	l1 = AddNewNode(l1, 5)
	
	l2 = None
	l2 = AddNewNode(l2, 2)
	l2 = AddNewNode(l2, 4)
	
	l3 = MergeTwoSortedLists (l1, l2)
	l3Temp = l3
	while (l3Temp != None):
		print (l3Temp.val)
		l3Temp = l3Temp.next