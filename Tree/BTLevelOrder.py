class Solution(object):
    def levelOrder(self, root):
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
        return levels
