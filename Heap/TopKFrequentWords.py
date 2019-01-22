class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq

        q = []
        countDict = dict()

        for word in words:
            if word not in countDict:
                countDict[word] = 1
            else:
                countDict[word] += 1

        for key, value in countDict.items():
            heapq.heappush(q, (value * -1, key))

        res = []
        while k > 0:
            times, word = heapq.heappop(q)
            k -= 1
            subList = []
            subList.append(word)
            while len(q) > 0 and times == q[0][0] and k > 0:
                times1, word1 = heapq.heappop(q)
                subList.append(word1)
                k -= 1

            sList = (sorted(subList))
            for element in sList:
                res.append(element)

        return res

if __name__ == "__main__":
     words = ["i", "love", "leetcode", "i", "love", "coding"]
     words1 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
     k = 4
     s = Solution()
     print(s.topKFrequent(words1, k))