class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        q = []

        if nums1 == [] or nums2 == [] or k == 0:
            return []
        
        count = 0
        
        for val1 in nums1:
            for val2 in nums2:
                heapq.heappush(q, (val1 + val2, [val1, val2]))
                count += 1

        res = []
        
        while k > 0 and len(q) > 0:
            sumVal, ans = heapq.heappop(q)
            res.append(ans)
            k -= 1

        return res