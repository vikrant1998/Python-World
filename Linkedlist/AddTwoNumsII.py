# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        self.l3 = None
        self._addTwoNumbers(l1, l2)
        return self.l3

    def _pushFront(self, val):
        if self.l3 == None:
            self.l3 = ListNode(val)
            return
        else:
            tempNode = ListNode(val)
            tempNode.next = self.l3
            self.l3 = tempNode

    def _addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        nodeItr1, nodeItr2 = l1, l2
        while nodeItr1 != None:
            stack1.append(nodeItr1.val)
            nodeItr1 = nodeItr1.next
        while nodeItr2 != None:
            stack2.append(nodeItr2.val)
            nodeItr2 = nodeItr2.next

        carry = 0
        while stack1 and stack2:
            el1 = stack1.pop()
            el2 = stack2.pop()
            sumVal = carry + el1 + el2
            carry = sumVal // 10
            self._pushFront(sumVal % 10)
        while stack1:
            el1 = stack1.pop()
            sumVal = carry + el1
            carry = sumVal // 10
            self._pushFront(sumVal % 10)
        while stack2:
            el2 = stack2.pop()
            sumVal = carry + el2
            carry = sumVal // 10
            self._pushFront(sumVal % 10)

        if carry > 0:
            self._pushFront(carry)

def InsertIntoLinkedList(head, val):
    newNode = ListNode(val)
    if head == None:
        head = newNode
        return head

    nodeItr = head
    while nodeItr.next != None:
        nodeItr = nodeItr.next
    nodeItr.next = newNode
    return head

def PrintLinkedList(head):
    if head == None:
        return

    nodeItr = head
    while nodeItr != None:
        print(nodeItr.val)
        nodeItr = nodeItr.next

if __name__ == "__main__":
    l1 = None
    l1 = InsertIntoLinkedList(l1, 7)
    l1 = InsertIntoLinkedList(l1, 2)
    l1 = InsertIntoLinkedList(l1, 4)
    l1 = InsertIntoLinkedList(l1, 3)

    l2 = None
    l2 = InsertIntoLinkedList(l2, 5)
    l2 = InsertIntoLinkedList(l2, 6)
    l2 = InsertIntoLinkedList(l2, 4)

    s = Solution()
    s.addTwoNumbers(l1, l2)
