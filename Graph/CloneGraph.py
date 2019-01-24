# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None

        from collections import deque
        q, cq = deque(), deque()

        headNode = UndirectedGraphNode(node.label)
        q.append(node)
        cq.append(headNode)

        cloneMap = dict()
        cloneMap[headNode.label] = headNode

        while q:
            normalQ = q.popleft()
            cloneQ = cq.popleft()

            for neighbor in normalQ.neighbors:
                if neighbor.label in cloneMap:
                    cloneQ.neighbors.append(cloneMap[neighbor.label])
                else:
                    newNode = UndirectedGraphNode(neighbor.label)
                    cloneMap[newNode.label] = newNode
                    cloneQ.neighbors.append(newNode)

                    q.append(neighbor)
                    cq.append(cloneQ.neighbors[-1])
            
        return headNode

if __name__ == "__main__":
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n3 = UndirectedGraphNode(3)
    n4 = UndirectedGraphNode(4)

    n1.neighbors = [n2, n3, n4]
    n2.neighbors = [n1, n4]
    n3.neighbors = [n1, n4]
    n4.neighbors = [n1, n2, n3]

    s = Solution()
    s.cloneGraph(n1)