class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or grid == []: return 0
        if grid == [[]]: return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        from collections import deque
        i = 0
        j = 0

        for innerList in grid:
            j = 0
            for val in innerList:
                if val == '0' or (i, j) in visited:
                    j += 1
                    continue

                islands += 1
                q = deque()
                q.append((i, j))
                visited.add((i, j))

                while q:
                    x, y = q.popleft()
                    # Top
                    if x - 1 >= 0 and (x - 1, y) not in visited and grid[x - 1][y] == '1':
                        visited.add((x - 1, y))
                        q.append((x - 1, y))

                    # Left
                    if y - 1 >= 0 and (x, y - 1) not in visited and grid[x][y - 1] == '1':
                        visited.add((x, y - 1))
                        q.append((x, y - 1))

                    # Down
                    if x + 1 < rows and (x + 1, y) not in visited and grid[x + 1][y] == '1':
                        visited.add((x + 1, y))
                        q.append((x + 1, y))

                    # Right
                    if y + 1 < cols and (x, y + 1) not in visited and grid[x][y + 1] == '1':
                        visited.add((x, y + 1))
                        q.append((x, y + 1))

                j += 1
            i += 1

        return islands

if __name__ == "__main__":
    s = Solution()

    grid = [['1','1','0','0','0'],\
    ['1','1','0','0','0'],\
    ['0','0','1','0','0'],\
    ['0','0','0','1','1']]

    grid = [["1","1","1"],\
            ["0","1","0"],\
            ["1","1","1"]]

    '''
    grid = [["1","1","0","0","0"],\
            ["1","1","0","0","0"],\
            ["0","0","1","0","0"],\
            ["0","0","0","1","1"]]
    '''

    print(s.numIslands(grid))
