class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        from collections import deque
        q = deque()

        i = 0
        j = len(A) - 1
        newList = [0 for k in range(len(A))]

        front = 0
        end = len(A) - 1
        while i <= j:
            if i != j:
                if abs(A[i]) > abs(A[j]):
                    newList[end] = A[i] * A[i]
                    end -= 1
                    i += 1
                else:
                    newList[end] = A[j] * A[j]
                    end -= 1
                    j -= 1
            elif i == j:
                newList[end] = A[i] * A[i]
                i += 1
                j -= 1

        return newList


if __name__ == "__main__":
    A = [-7,-3,2,3,11]
    s = Solution()
    print(s.sortedSquares(A))