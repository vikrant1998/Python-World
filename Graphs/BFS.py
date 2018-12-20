from collections import defaultdict
from collections import deque

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def AddEdge(self, u, v):
		if v not in self.graph[u]:
			self.graph[u].append(v)

	def BFS(self, u):
		if u not in self.graph.keys(): return

		visited, queue = set([u]), deque([u])

		while queue:
			element = queue.popleft()
			print (element)

			for neighbor in self.graph[element]:
				if neighbor not in visited:
					queue.append(neighbor)
					visited.add(neighbor)

if __name__ == "__main__":
	g = Graph()
	g.AddEdge(1, 2)
	g.AddEdge(1, 3)
	g.AddEdge(2, 4)
	g.AddEdge(2, 5)
	g.AddEdge(5, 6)
	g.AddEdge(5, 7)

	print(g.graph)
	g.BFS(1)
