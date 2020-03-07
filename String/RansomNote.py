class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))