class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumVal = nums[0]
        maxSum = nums[0]
        arrSize = len(nums)
        i = 1
        while i < arrSize:
            if nums[i] + sumVal > nums[i]:
                sumVal = nums[i] + sumVal
            else:
                sumVal = nums[i]

            if sumVal > maxSum:
                maxSum = sumVal
            i += 1 
        return maxSum

if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))