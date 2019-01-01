# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return True
        #res = [True]
        #nodeItr1, nodeItr2 = [head], head
        # self._isPalindromeRecurse(nodeItr1, nodeItr2, res)
        newList = []
        nodeItr = head
        while nodeItr != None:
            newList.append(nodeItr.val)
            nodeItr = nodeItr.next

        if newList == newList[::-1]: return True
        return False
        #return res[0]

    def _isPalindromeRecurse(self, nodeItr1, nodeItr2, res):
        if nodeItr1[0] == None or nodeItr2 == None: return
        if res[0] == False: return
        if nodeItr1[0] == None and nodeItr2 != None:
            res[0] = False
            return
        if nodeItr1[0] != None and nodeItr2 == None:
            res[0] = False
            return
        self._isPalindromeRecurse(nodeItr1, nodeItr2.next, res)
        if nodeItr1[0].val != nodeItr2.val:
            res[0] = False
            return
        else:
            nodeItr1[0] = nodeItr1[0].next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    s = Solution()
    print(s.isPalindrome(n1))
