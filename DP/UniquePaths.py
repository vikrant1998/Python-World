class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0: return 0
        self.grid = [[0 for i in range(n)] for j in range(m)]
        self.cache = dict()
        return self._dfs(0, 0)

    def _dfs(self, i, j):
        if (i, j) in self.cache: return self.cache[(i, j)]
        if i >= len(self.grid) or j >= len(self.grid[0]): return 0
        if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1: return 1
        numPaths = self._dfs(i + 1, j)
        numPaths += self._dfs(i, j + 1)
        self.cache[(i, j)] = numPaths
        return self.cache[(i, j)]

if __name__ == "__main__":
    s = Solution()
    s.uniquePaths(3, 2)