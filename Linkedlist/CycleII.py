# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head
        check = 0

        while slow != None and fast != None and fast.next != None and (slow != fast or check == 0):
            slow = slow.next
            fast = fast.next.next
            check = 1

        if slow == None or fast == None or fast.next == None: return None
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow