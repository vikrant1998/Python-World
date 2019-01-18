class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0; j = len(S) - 1
        l = list(S)

        while i < j:
            if l[i].isalpha() and l[j].isalpha():
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            if not l[i].isalpha():
                i += 1
            if not l[j].isalpha():
                j -= 1

        outStr = ''.join(l)
        return outStr

if __name__ == "__main__":
    s = Solution()
    S = "a-bC-dEf-ghIj"
    s.reverseOnlyLetters(S)