from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def AddEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def DFS(self, u):
        if u not in self.graph.keys(): return
        visited = set([u])
        self.DFS_Recurse(u, visited)

    def DFS_Recurse(self, u, visited):
        print (u)

        for neighbor in self.graph[u]:
            if neighbor not in visited:
                visited.add(u)
                self.DFS_Recurse(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    g.AddEdge(1, 2)
    g.AddEdge(1, 3)
    g.AddEdge(2, 4)
    g.AddEdge(2, 5)
    g.AddEdge(5, 6)
    g.AddEdge(5, 7)

    g.DFS(1)
