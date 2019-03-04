class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m, self.n = 0, 0
        self.cache = dict()
        if grid == None or len(grid) == 0: return 0
        self.m, self.n = len(grid), len(grid[0])

        return self._recurse(0, 0, grid)

    def _recurse(self, i, j, grid):
        if (i, j) in self.cache: return self.cache[(i, j)]
        if i >= self.m or j >= self.n: return -1
        if i == self.m - 1 and j == self.n - 1: return grid[i][j]

        right = self._recurse(i, j + 1, grid)
        down = self._recurse(i + 1, j, grid)

        retVal = 0
        if right == -1: retVal = down + grid[i][j]
        elif down == -1: retVal = right + grid[i][j]
        else: retVal = min(down, right) + grid[i][j]
        self.cache[(i, j)] = retVal
        return retVal

if __name__ == "__main__":
    s = Solution()
    grid = [[1,3,1], [1,5,1], [4,2,1]]
    print(s.minPathSum(grid))