# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        from collections import deque
        q = deque()
        q.append(root)
        mainList = []
        mainList.append([root.val])
        count = 0

        while q:
            qSize = len(q)
            rev = 0
            if count % 2 == 0: rev = 1
            subList = []
            while qSize > 0:
                element = q.popleft()
                if element.left != None:
                    q.append(element.left)
                    subList.append(element.left.val)
                if element.right != None:
                    q.append(element.right)
                    subList.append(element.right.val)
                qSize -= 1
            if subList != []:
                if rev == 1:
                    mainList.append(subList[::-1])
                else:
                    mainList.append(subList)
            count += 1
        return mainList

if __name__ == "__main__":
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n12 = TreeNode(12)
    n13 = TreeNode(13)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9; n3.right = n20
    n9.left = n12; n9.right = n13
    n20.left = n15; n20.right = n7

    s = Solution()
    print(s.zigzagLevelOrder(n3))
