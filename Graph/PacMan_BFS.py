from collections import defaultdict
from collections import deque
import sys

# Read the maze from an input file.
def ReadMaze():
    inp = []
    for line in sys.stdin:
        inp.append(line)
    inp = [word.strip() for word in inp]
    px, py = int(inp[0].split(' ')[0]), int(inp[0].split(' ')[1])
    fx, fy = int(inp[1].split(' ')[0]), int(inp[1].split(' ')[1])
    r, c   = int(inp[2].split(' ')[0]), int(inp[2].split(' ')[1])
    inp = inp[3:]

    maze = [[0] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            maze[i][j] = inp[i][j]

    return px, py, fx, fy, r, c, maze

# Add to queue based on conditions.
def AddToQueue(queue, x, y, fx, fy, r, c, maze, visited, backtrackMap):
    if x < 0 or x >= r or y < 0 or y >= c: return

    # Add up to the queue.
    if x - 1 >= 0 and x - 1 < r and maze[x - 1][y] != '%' and (x - 1, y) not in visited:
        queue.append((x - 1, y))
        visited.add((x - 1, y))
        backtrackMap[(x - 1, y)] = (x, y)

    # Add left to the queue.
    if y - 1 >= 0 and y - 1 < c and maze[x][y - 1] != '%' and (x, y - 1) not in visited:
        queue.append((x, y - 1))
        visited.add((x, y - 1))
        backtrackMap[(x, y - 1)] = (x, y)

    # Add bottom to the queue.
    if x + 1 >= 0 and x + 1 < r and maze[x + 1][y] != '%' and (x + 1, y) not in visited:
        queue.append((x + 1, y))
        visited.add((x + 1, y))
        backtrackMap[(x + 1, y)] = (x, y)

    # Add right to the queue.
    if y + 1 >= 0 and y + 1 < c and maze[x][y + 1] != '%' and (x, y + 1) not in visited:
        queue.append((x, y + 1))
        visited.add((x, y + 1))
        backtrackMap[(x, y + 1)] = (x, y)

    return queue


# Solve the maze.
def BFS(px, py, fx, fy, r, c, maze):
    visited = set()
    queue = deque()

    visited.add((px, py))
    queue.append((px, py))
    backtrackMap = dict()
    backtrackMap[(px, py)] = None
    found = False

    while queue:
        element = queue.popleft()
        if element[0] == fx and element[1] == fy:
            found = True
            break

        # Add to queue based on conditions.
        queue = AddToQueue(queue, element[0], element[1], fx, fy, r, c, maze, visited, backtrackMap)

    shortestPath = None
    if found:
        shortestPath = FindShortestPath(fx, fy, px, py, backtrackMap)

    return shortestPath

def FindShortestPath(fx, fy, px, py, backtrackMap):
    x, y = fx, fy
    shortestPath = deque()
    while backtrackMap[(x, y)] != None:
        shortestPath.appendleft((x, y))
        x, y = backtrackMap[(x, y)]

    return shortestPath

# Usage: python PacMan_BFS.py < Input/PacMan_BFS.in
if __name__ == "__main__":
    px, py, fx, fy, r, c , maze = ReadMaze()
    shortestPath = BFS(px, py, fx, fy, r, c, maze)

    print (len(shortestPath))
    for element in shortestPath:
        x, y = element[0], element[1]
        op = str(x) + ' ' + str(y)
        print (op)
