class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        q = deque()
        finList = []

        for i, num in enumerate(nums):
            while len(q) > 0 and q[-1][1] < num: q.pop()
            q.append((i, num))
            while len(q) > 0 and q[-1][0] - q[0][0] >= k: q.popleft()
            if len(q) > 0 and i >= k - 1: finList.append(q[0][1])

        return finList

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    s = Solution()
    s.maxSlidingWindow(nums, k)