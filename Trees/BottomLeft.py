# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None

        from collections import deque
        q = deque()
        q.append(root)
        lastVal = root.val
        while q:
            qSize = len(q)
            while qSize > 0:
                element = q.popleft()
                lastVal = element.val
                if element.right != None: q.append(element.right)
                if element.left != None: q.append(element.left)
                qSize -= 1

        return lastVal

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2; n1.right = n3
    n2.left = n4
    n3.left = n5; n3.right = n6
    n5.left = n7

    s = Solution()
    s.findBottomLeftValue(n1)
