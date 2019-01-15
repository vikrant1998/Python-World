class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumTillHere = []

        for num in nums:
            if len(self.sumTillHere) == 0:
                self.sumTillHere.append(num)
            else:
                sumVal = self.sumTillHere[-1] + num
                self.sumTillHere.append(sumVal)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0: return self.sumTillHere[j]
        return self.sumTillHere[j] - self.sumTillHere[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)