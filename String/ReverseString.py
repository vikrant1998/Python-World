class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        newList = []
        for letter in s:
            newList.append(letter)

        size = len(newList)
        i = 0

        while i < size / 2:
            newList[i], newList[size - i - 1] = newList[size - i - 1], newList[i]
            i += 1

        return ''.join(newList)

if __name__ == "__main__":
    s = Solution()
    str = "A man, a plan, a canal: Panama"
    res = "amanaP :lanac a ,nalp a ,nam A"
    print(s.reverseString(res))
