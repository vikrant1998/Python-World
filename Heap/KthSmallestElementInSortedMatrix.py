class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        i, j = 0, 0
        import heapq
        q = []
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                heapq.heappush(q, matrix[i][j])
                j += 1
            i += 1

        val = 0
        while k > 0:
            val = heapq.heappop(q)
            k -= 1

        return val

if __name__ == "__main__":
    matrix = [[1,2],[3,3]]
    k = 2
    s = Solution()
    print(s.kthSmallest(matrix, k))