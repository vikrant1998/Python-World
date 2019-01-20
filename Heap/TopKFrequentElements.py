class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countDict = dict()
        for num in nums:
            if num not in countDict: countDict[num] = 1
            else: countDict[num] += 1

        import heapq
        q = []
        for key, value in countDict.items():
            if len(q) < k:
                heapq.heappush(q, (value, key))
            else:
                if value > q[0][0]:
                    heapq.heappop(q)
                    heapq.heappush(q, (value, key))

        finList = []
        while q:
            element = heapq.heappop(q)
            finList.insert(0, element[1])
 
        return finList

if __name__ == "__main__":
    nums = [1]
    k = 1
    s = Solution()
    print(s.topKFrequent(nums, k))