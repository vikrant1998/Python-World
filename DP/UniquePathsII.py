class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.cache = dict()
        self.grid = obstacleGrid
        if len(self.grid) == 0: return 0
        if len(self.grid[0]) == 1 and self.grid[0][0] == 1: return 0
        if self.grid[len(self.grid) - 1][len(self.grid[0]) - 1] == 1: return 0 
        return self._dfs(0, 0)

    def _dfs(self, i, j):
        if (i, j) in self.cache: return self.cache[(i, j)]
        if i >= len(self.grid) or j >= len(self.grid[0]): return 0
        if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1: return 1
        if self.grid[i][j] == 1: return 0
        numPaths = self._dfs(i + 1, j) + self._dfs(i, j + 1)
        self.cache[(i, j)] = numPaths
        return self.cache[(i, j)]


if __name__ == "__main__":
    grid = [[0,0,0], [0,1,0], [0,0,0]]
    s = Solution()
    print(s.uniquePathsWithObstacles(grid))