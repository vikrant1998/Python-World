class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h1 = dict()
        h2 = dict()

        for char in s:
            if char not in h1:
                h1[char] = 1
            else:
                h1[char] += 1

        for char in t:
            if char not in h2:
                h2[char] = 1
            else:
                h2[char] += 1

        if len(h1) != len(h2):
            return False

        for key, value in h1.items():
            if key not in h2 or value != h2[key]:
                return False

        return True

if __name__ == "__main__":
    s1 = u'a'
    t = u'b'
    s = Solution()
    print(s.isAnagram(s1, t))
