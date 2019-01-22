# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        q = []
        self.finList = None
        self.tail = None
        for start in lists:
            if start != None:
                heapq.heappush(q, (start.val, start))

        while q:
            popVal = heapq.heappop(q)
            insVal, nodePtr = popVal
            self._InsertIntoLinkedList(insVal)
            if nodePtr.next != None:
                heapq.heappush(q, (nodePtr.next.val, nodePtr.next))

        return self.finList

    def _InsertIntoLinkedList(self, val):
        if self.finList == None:
            self.finList = ListNode(val)
            self.tail = self.finList
            return

        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        return


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    mainList = [l1, l2, l3]
    s = Solution()
    s.mergeKLists(mainList)