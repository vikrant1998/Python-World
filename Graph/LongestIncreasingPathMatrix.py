class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0

        self.graph = dict()
        self._BuildGraph(matrix)

    def _BuildGraph(self, matrix):
        i, j = 0, 0
        height = len(matrix)
        width = len(matrix[0])

        while i < height:
            j = 0
            while j < width:
                j += 1

if __name__ == "__main__":
    matrix = [[9,9,4], [6,6,8], [2,1,1]]
    s = Solution()
    print(s.longestIncreasingPath(matrix))