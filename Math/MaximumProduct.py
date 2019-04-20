class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        min1, min2 = float("inf"), float("inf")

        for num in nums:
            if num > max1 and num > max2 and num > max3:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2 and num > max3:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1 and num < min2:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)

if __name__ == "__main__":
    nums = [-1,-2,-3]
    s = Solution()
    print(s.maximumProduct(nums))