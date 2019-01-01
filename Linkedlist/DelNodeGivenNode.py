# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None: return
        node.val = node.next.val
        nextNode = node.next.next
        del(node.next)
        node.next = nextNode

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
    l1 = None
    l1 = InsertIntoLinkedList(l1, 4)
    l1 = InsertIntoLinkedList(l1, 5)
    l1 = InsertIntoLinkedList(l1, 1)
    l1 = InsertIntoLinkedList(l1, 9)
    s = Solution()
    s.deleteNode(l1.next)
    PrintLinkedList(l1)
