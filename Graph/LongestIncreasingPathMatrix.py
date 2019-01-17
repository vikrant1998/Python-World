class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0

        from collections import defaultdict, deque
        self.edgeCounter = dict()
        self.graph = defaultdict(list)
        self.distances = dict()
        self._BuildGraph(matrix)

        q = deque()
        for key, value in self.graph.items():
            if self.edgeCounter[key] == 0:
                q.append(key)
                self.distances[key] = 1

        maxDist = 1

        while q:
            element = q.popleft()
            self.edgeCounter[element] = 0
            for neighbor in self.graph[element]:                
                self.edgeCounter[neighbor] -= 1
                self.graph[element] = [i for i in self.graph[element] if i != neighbor]
                if self.edgeCounter[neighbor] == 0:
                    q.append(neighbor)
                    self.distances[neighbor] = self.distances[element] + 1
                    if self.distances[neighbor] > maxDist:
                        maxDist = self.distances[neighbor]

        return maxDist

    def _BuildGraph(self, matrix):
        i, j = 0, 0
        height = len(matrix)
        width = len(matrix[0])

        while i < height:
            j = 0
            while j < width:
                self.distances[(i, j)] = 0
                if (i, j) not in self.edgeCounter:
                    self.edgeCounter[(i, j)] = 0
                
                # Up
                if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                    self.graph[(i, j)].append((i - 1, j))
                    if (i - 1, j) not in self.edgeCounter: self.edgeCounter[(i - 1, j)] = 1
                    else: self.edgeCounter[(i - 1, j)] += 1
                # Left
                if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                    self.graph[(i, j)].append((i, j - 1))
                    if (i, j - 1) not in self.edgeCounter: self.edgeCounter[(i, j - 1)] = 1
                    else: self.edgeCounter[(i, j - 1)] += 1
                # Down
                if i + 1 < height and matrix[i + 1][j] > matrix[i][j]:
                    self.graph[(i, j)].append((i + 1, j))
                    if (i + 1, j) not in self.edgeCounter: self.edgeCounter[(i + 1, j)] = 1
                    else: self.edgeCounter[(i + 1, j)] += 1
                # Right
                if j + 1 < width and matrix[i][j + 1] > matrix[i][j]:
                    self.graph[(i, j)].append((i, j + 1))
                    if (i, j + 1) not in self.edgeCounter: self.edgeCounter[(i, j + 1)] = 1
                    else: self.edgeCounter[(i, j + 1)] += 1
                    
                j += 1
            i += 1

if __name__ == "__main__":
    matrix = [[7,7,5],
              [2,4,6],
              [8,2,0]]
    s = Solution()
    print(s.longestIncreasingPath(matrix))