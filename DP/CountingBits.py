class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        self.resList = []
        self.count = 0
        self.cache = dict()
        self.cache[0] = 0
        for i in range(0, num + 1):
            self.count = 0
            res = self._recurse(i)
            self.resList.append(res)
        return self.resList

    def _recurse(self, num):
        if num == 0:
            return 0

        if num in self.cache:
            self.count += self.cache[num]
            return self.count

        if num >= 1:
            if num % 2 == 1 or num == 1:
                self.count += 1
            self._recurse(num / 2)
        
        if num not in self.cache:
            self.cache[num] = self.count
        return self.count

if __name__ == "__main__":
    num = 5
    s = Solution()
    print(s.countBits(num))