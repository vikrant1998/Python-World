class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = ['q', 'w', 'e', 'r', 't', 'y',\
        'u', 'i', 'o', 'p']
        second = ['a', 's', 'd', 'f', 'g', 'h',
        'j', 'k', 'l']
        third = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        finList = []
        for single1 in words:
            single = single1.lower()
            count1, count2, count3 = 0, 0, 0
            for letter in single:
                if letter in first: count1 += 1
                elif letter in second: count2 += 1
                elif letter in third: count3 += 1
            sz = len(single)
            if sz == count1 or sz == count2 or sz == count3:
                finList.append(single1)

        return finList

if __name__ == "__main__":
    s = Solution()
    words = ['Hello', 'Alaska', 'Dad', 'Peace']
    print(s.findWords(words))
