
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):

    """ Most queue problems you need the queue size. """
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        from collections import deque
        if root == None: return []
        q = deque()
        q.append(root)

        levels = []
        levels.append([root.val])

        while q:
            qSize = len(q)
            subList = []
            while qSize > 0:
                element = q.popleft()
                if element and element.children:
                    for children in element.children:
                        subList.append(children.val)
                        q.append(children)
                qSize -= 1
            if subList != []: levels.append(subList)
        return levels

if __name__ == "__main__":
    n2 = Node(2, None)
    n8 = Node(8, None)
    n4 = Node(4, [n8])
    n5 = Node(5, None)
    n7 = Node(7, None)
    n6 = Node(6, [n7])

    n3 = Node(3, [n5, n6])
    n1 = Node(1, [n3, n2, n4])

    s = Solution()
    res = s.levelOrder(n1)
    print(res)
