class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i = 0
        j = 0

        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False
                j += 1
            i += 1

        return True

if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,1,2,3],
              [9,5,1,2]]
    s = Solution()
    print(s.isToeplitzMatrix(matrix))