class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = dict()
        for char in s:
            if char not in h:
                h[char] = 1
            else:
                h[char] += 1

        for i, char in enumerate(s):
            if h[char] == 1:
                return i
        return -1

if __name__ == "__main__":
    s1 = "loveleetcode"
    s = Solution()
    print(s.firstUniqChar(s1))