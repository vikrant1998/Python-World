class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h1 = dict()

        for char in s:
            if char not in h1:
                h1[char] = 1
            else:
                h1[char] += 1

        h2 = dict()
        for char in t:
            if char not in h1:
                return char
            if char not in h2:
                h2[char] = 1
            else:
                h2[char] += 1

        for key, value in h1.items():
            if h2[key] != h1[key]:
                return key 


if __name__ == "__main__":
    s1 = "abcd"
    t = "abcde"
    s = Solution()
    print(s.findTheDifference(s1, t))