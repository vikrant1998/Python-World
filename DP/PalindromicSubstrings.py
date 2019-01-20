class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        self.numDromes = 0

        for i in range(len(s)):
            self._CenterExpand(i, i, s)
            self._CenterExpand(i, i + 1, s)

        return self.numDromes

    def _CenterExpand(self, start, end, s):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            self.numDromes += 1

if __name__ == "__main__":
    s1 = "aaaaa"
    s = Solution()
    print(s.countSubstrings(s1))