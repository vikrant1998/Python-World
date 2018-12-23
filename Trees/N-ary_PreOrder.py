# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        elements = []
        self._preorder(root, elements)
        return elements

    def _preorder(self, root, elements):
        if root == None: return

        elements.append(root.val)
        if root.children:
            for element in root.children:
                self._preorder(element, elements)

if __name__ == "__main__":
    s = Solution()

    f2 = Node(2, None)
    f4 = Node(4, None)
    f5 = Node(5, None)
    f6 = Node(6, None)
    f3 = Node(3, [f5, f6])
    f1 = Node(1, [f3, f2, f4])

    print(s.preorder(f1))
