class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.kVal = k
        self.heapList = []
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        import heapq
        if len(self.heapList) < self.kVal:
            heapq.heappush(self.heapList, (val))
        elif val > self.heapList[0]:
            heapq.heappop(self.heapList)
            heapq.heappush(self.heapList, val)

        return self.heapList[0]

if __name__ == "__main__":
    # Your KthLargest object will be instantiated and called as such:
    k = 1
    nums = [4,5,8,2]
    obj = KthLargest(k, nums)
    print(obj.add(3))
