class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or grid == []: return 0
        if grid == [[]]: return 0

        x = len(grid)
        y = len(grid[0])
        per = 0

        for i, list in enumerate(grid):
            for j, val in enumerate(list):
                if val == 1:
                    if j - 1 < 0: per += 1
                    if i + 1 == x: per += 1
                    if i - 1 < 0: per += 1
                    if j + 1 == y: per += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0: per += 1
                    if i + 1 < x and grid[i + 1][j] == 0: per += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 0: per += 1
                    if j + 1 < y and grid[i][j + 1] == 0: per += 1
        return per

if __name__ == "__main__":
    area = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    s = Solution()
    print(s.islandPerimeter(area))
