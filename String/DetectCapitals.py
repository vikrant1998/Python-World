class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '': return True
        capCount, lwrCount = 0, 0

        # All caps check and all small check.
        for val in word:
            if val.isupper(): capCount += 1
            else: lwrCount += 1

        if capCount == len(word) or lwrCount == len(word):
            return True

        if word[0].isupper() and lwrCount == len(word) - 1:
            return True

        return False

if __name__ == "__main__":
    word1 = "Geetcode"
    s = Solution()
    print(s.detectCapitalUse(word1))