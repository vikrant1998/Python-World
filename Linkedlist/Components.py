# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        newSet = set(G)
        nodeItr = head
        num = 0
        while nodeItr != None:
            if nodeItr.next != None and nodeItr.val in newSet:
                while nodeItr.next != None and nodeItr.val in newSet:
                    nodeItr = nodeItr.next
                num += 1
            elif nodeItr.val in newSet:
                num += 1
            nodeItr = nodeItr.next
        return num

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
    l1 = InsertIntoLinkedList(l1, 0)
    l1 = InsertIntoLinkedList(l1, 1)
    l1 = InsertIntoLinkedList(l1, 2)
    l1 = InsertIntoLinkedList(l1, 3)
    #l1 = InsertIntoLinkedList(l1, 4)
    PrintLinkedList(l1)

    newList = [0, 1, 3]
    s = Solution()
    print(s.numComponents(l1, newList))
