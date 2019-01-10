# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        from collections import deque
        q = deque()
        q.append(root)
        largestVals = []
        while q:
            qSize = len(q)
            maxVal = float("-inf")
            while qSize > 0:
                element = q.popleft()
                if element.val > maxVal: maxVal = element.val
                if element.left != None: q.append(element.left)
                if element.right != None: q.append(element.right)
                qSize -= 1
            largestVals.append(maxVal)
        return largestVals

if __name__ == "__main__":
    n1 = TreeNode(1)
    n3a = TreeNode(3)
    n2 = TreeNode(2)
    n5 = TreeNode(5)
    n3b = TreeNode(3)
    n9 = TreeNode(9)

    n1.left = n3a; n1.right = n2
    n3a.left = n5; n3a.right = n3b
    n2.right = n9

    s = Solution()
    print(s.largestValues(n1))
