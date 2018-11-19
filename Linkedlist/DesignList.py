class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class MyLinkedList(object):

    def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.head = None

    def get(self, index):
		"""
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
		tempNode = self.head
		count = 0

		while (tempNode != None and tempNode != count):
			tempNode = tempNode.next
			count += 1

		if (tempNode == count):
			return tempNode.val
		else:
			return -1

    def addAtHead(self, val):
		"""
		Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
		:type val: int
		:rtype: void
		"""
		if (self.head == None):
			self.head = ListNode(val)
			return

		newNode = ListNode(val)
		newNode.next = self.head
		self.head = newNode
		return
		

    def addAtTail(self, val):
		"""
		Append a node of value val to the last element of the linked list.
		:type val: int
		:rtype: void
		"""
		if (self.head == None):
			self.head = ListNode(val)
			return

		tempNode = self.head
		while (tempNode.next != None):
			tempNode = tempNode.next

		tempNode.next = ListNode(val)
		return

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        pass

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        pass


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtHead(3)
obj.addAtHead(4)
obj.addAtTail(2)
obj.addAtTail(5)
obj.addAtTail(7)

tempObj = obj.head
while (tempObj != None):
	print (tempObj.val)
	tempObj = tempObj.next

#obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)