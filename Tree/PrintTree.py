# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root == None: return []
        height = self._FindHeight(root)

        res = [[] for i in range(height)]
        for i, innerList in enumerate(res):
            for j in range(2 ** height - 1):
                res[i].append("")

        from collections import deque
        q = deque()
        distances = dict()
        size = 2 ** height - 1
        d = 2 ** (height - 1)
        q.append([root, size / 2])
        count = 0
        while q:
            qSize = len(q)
            subList = []
            while qSize > 0:
                val = q.popleft()
                element, index = val[0], val[1]
                res[count][index] = str(element.val)
                if element.left != None:
                    q.append([element.left, index - d / 2])
                if element.right != None:
                    q.append([element.right, index + d / 2])
                qSize -= 1
            count += 1
            d /= 2
        return res

    def _FindHeight(self, root):
        if root == None:
            return 0

        l = self._FindHeight(root.left)
        r = self._FindHeight(root.right)
        return max(l, r) + 1

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n1.left = n2; n1.right = n3
    n2.right = n4

    s = Solution()
    s.printTree(n1)