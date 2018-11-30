from collections import defaultdict
from collections import deque

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)
		
	def AddEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, u):
		visited, queue = set(), deque([u])
		visited.add(u)
		while queue: 
			vertex = queue.popleft()
			print (vertex)
			for neighbor in self.graph[vertex]: 
				if neighbor not in visited: 
					visited.add(neighbor) 
					queue.append(neighbor) 
		
if __name__ == "__main__":
	g = Graph()
	g.AddEdge(0, 1)
	#g.AddEdge(1, 0)
	g.BFS(1)