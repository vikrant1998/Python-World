# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        q = deque()
        q.append(root)
        rightList = []

        while q:
            qSize = len(q)
            if q[qSize-1] != None:
                rightList.append(q[qSize-1].val)
            while qSize > 0:
                element = q.popleft()
                if element != None:
                    if element.left != None:
                        q.append(element.left)
                    if element.right != None:
                        q.append(element.right)
                qSize -= 1

        return rightList

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2; n1.right = n3
    n2.right = n5
    n3.right = n4

    s = Solution()
    print(s.rightSideView(n1))
