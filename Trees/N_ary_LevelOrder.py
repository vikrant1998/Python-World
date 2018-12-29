
# Definition for a Node.
class Node(object):
def __init__(self, val, children):
    self.val = val
    self.children = children

class Solution(object):
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
            element = q.popleft()
            subList = []
            if element != None:
                for children in element.children:
                    if children != None:
                        q.append(children)
                        subList.append(children.val)
            levels.append(subList)

        print(levels)


if __name__ == "__main__":
    n1 = Node(1)
    n3 = Node(3)
    n2 = Node(2)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.children = [n3, n2, n4]
    n3.children = [n5, n6]

    s = Solution(n1)
    s.levelOrder()
