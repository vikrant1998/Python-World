# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        if root == None: return []
        q = deque()
        q.append(root)
        levels = list()
        levels.append([root.val])
        while q:
            qSize = len(q)
            sublist = []
            while qSize > 0:
                element = q.popleft()
                if element != None:
                    if element.left:
                        q.append(element.left)
                        sublist.append(element.left.val)
                    if element.right:
                        q.append(element.right)
                        sublist.append(element.right.val)
                qSize -= 1
            if sublist: levels.append(sublist)
        return levels[::-1]

if __name__ == "__main__":
    s = Solution()
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9; n3.right = n20
    n20.left = n15; n20.right = n7

    print(s.levelOrderBottom(n3))
