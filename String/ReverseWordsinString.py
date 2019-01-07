class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newList = []
        for letters in s:
            newList.append(letters)

        size = len(newList)
        i = 0

        while i < size:
            j = i + 1
            while j < size and newList[j] != ' ': j += 1
            start, end = i, j - 1
            while start < end:
                newList[start], newList[end] = newList[end], newList[start]
                start += 1
                end -= 1
            i = j
            i += 1

        return ''.join(newList)

if __name__ == "__main__":
    s = Solution()
    res = s.reverseWords("Let's take LeetCode contest")
    print(res)
    if "s'teL ekat edoCteeL tsetnoc" == res:
        print('yeet')
