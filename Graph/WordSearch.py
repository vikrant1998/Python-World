class Solution(object):
    def exist(self, board, word):
        if board == [] or board == None or word == '': return False
        visited, val = set(), [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.clear()
                    self.DFS(board, word, visited, i, j, val, [0])
                    if val[0] == True: return True
        return False

    def DFS(self, board, word, visited, x, y, val, wc):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or wc[0] < 0 or wc[0] >= len(word): return
        if val[0] == True: return

        if board[x][y] == word[wc[0]] and (x, y) not in visited and wc[0] == len(word) - 1:
            val[0] = True
            return

        if board[x][y] == word[wc[0]] and (x, y) not in visited:
            wc[0] += 1
            visited.add((x, y))
            self.DFS(board, word, visited, x - 1, y, val, wc)
            self.DFS(board, word, visited, x, y - 1, val, wc)
            self.DFS(board, word, visited, x + 1, y, val, wc)
            self.DFS(board, word, visited, x, y + 1, val, wc)
            visited.remove((x, y))
            wc[0] -= 1
            return

if __name__ == "__main__":
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    s = Solution()
    print(s.exist(board, 'AAB'))
