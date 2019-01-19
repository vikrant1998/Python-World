class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0: return 0
        width = len(A[0])
        height = len(A)

        matrix = [[0 for j in range(width)] for i in range(height)]
        i = height - 1
        j = 0

        while i >= 0:
            j = 0
            while j < width:
                minVal = float("inf")
                # Bottom Left
                if i + 1 < height and j - 1 >= 0:
                    minVal = min(minVal, matrix[i + 1][j - 1] + A[i][j])

                # Bottom Mid
                if i + 1 < height:
                    minVal = min(minVal, matrix[i + 1][j] + A[i][j])

                # Bottom Right
                if i + 1 < height and j + 1 < width:
                    minVal = min(minVal, matrix[i + 1][j + 1] + A[i][j])               

                if i == height - 1:
                    matrix[i][j] = A[i][j]
                else:
                    matrix[i][j] = minVal
                j += 1
            i -= 1

        return min(matrix[0])

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.minFallingPathSum(A))