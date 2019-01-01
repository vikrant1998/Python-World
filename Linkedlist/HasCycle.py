# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast: return True

        return False

if __name__ == "__main__":
    n3 = ListNode(3)
    n2 = ListNode(2)
    n0 = ListNode(0)
    n_4 = ListNode(-4)

    n3.next = n2
    n2.next = n0
    n0.next = n_4
    n_4.next = n2

    s = Solution()
    print(s.hasCycle(n3))
