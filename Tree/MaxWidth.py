# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        from collections import deque
        q = deque()

        distances = dict()
        distances[root] = 1

        q.append(root)
        maxVal = 1
        while q:
            qSize = len(q)
            subList = []
            while qSize > 0:
                element = q.popleft()
                if element.left != None:
                    q.append(element.left)
                    subList.append(2 * distances[element])
                    distances[element.left] = 2 * distances[element]
                if element.right != None:
                    q.append(element.right)
                    subList.append(2 * distances[element] + 1)
                    distances[element.right] = 2 * distances[element] + 1
                qSize -= 1

            if subList != []:
                maxVal = max(maxVal, subList[-1] - subList[0] + 1)

        return maxVal

if __name__ == "__main__":
    na = TreeNode(1)
    nb = TreeNode(1)
    nc = TreeNode(1)
    nd = TreeNode(1)
    ne = TreeNode(1)
    nf = TreeNode(1)
    ng = TreeNode(1)

    na.left = nb; na.right = nc
    nb.left = nd
    nd.left = nf
    nc.right = ne
    ne.right = ng

    s = Solution()
    print(s.widthOfBinaryTree(na))   