class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        arrSize = len(nums)
        self.cache = dict()
        maxVal = 0
        while i < arrSize: 
            res = self._recurse(i, nums)
            if res > maxVal:
                maxVal = res
            i += 1
        return maxVal

    def _recurse(self, i, nums):
        if i >= len(nums):
            return 0

        if i in self.cache:
            return self.cache[i]

        start = 2
        maxTot = nums[i]
        while i + start < len(nums):
            res = self._recurse(i + start, nums)
            res += nums[i]
            if res > maxTot:
                maxTot = res

            start += 1
        self.cache[i] = maxTot
        return maxTot

if __name__ == "__main__":
    nums = [1,2,3,1]
    s = Solution()
    print(s.rob(nums))