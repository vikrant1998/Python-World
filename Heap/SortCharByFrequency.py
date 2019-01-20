class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqDict = dict()
        for letter in s:
            if letter in freqDict: freqDict[letter] += 1
            else: freqDict[letter] = 1

        import heapq
        q = []
        for key, value in freqDict.items():
            heapq.heappush(q, (value * -1, key))

        res = ''
        while q:
            val, letter = heapq.heappop(q)
            val *= -1
            res += letter * val

        return res

if __name__ == "__main__":
    s1 = "tree"
    s = Solution()
    print(s.frequencySort(s1))