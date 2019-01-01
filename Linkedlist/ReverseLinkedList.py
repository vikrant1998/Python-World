# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head

def InsertIntoLinkedList(head, val):
    newNode = ListNode(val)
    if head == None:
        return newNode

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
    l1  = None
    l1 = InsertIntoLinkedList(l1, 1)
    l1 = InsertIntoLinkedList(l1, 2)
    l1 = InsertIntoLinkedList(l1, 3)
    l1 = InsertIntoLinkedList(l1, 4)
    l1 = InsertIntoLinkedList(l1, 5)
    l1 = InsertIntoLinkedList(l1, 6)

    s = Solution()
    l2 = s.reverseList(l1)
    PrintLinkedList(l2)
