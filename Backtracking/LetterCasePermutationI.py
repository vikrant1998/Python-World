class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S == "":
            return [""]

        self.newList = list(S)
        self.outSet = set()
        self._letterCasePermuation(0)
        return list(self.outSet)

    def _letterCasePermuation(self, index):
        if index >= len(self.newList):
            return

        if index == len(self.newList) - 1:
            self.newList[index] = self.newList[index].lower()
            self.outSet.add(''.join(self.newList))
            self.newList[index] = self.newList[index].upper()
            self.outSet.add(''.join(self.newList))
            return

        if self.newList[index].isalpha():
            self.newList[index] = self.newList[index].lower()
            self._letterCasePermuation(index + 1)
            self.newList[index] = self.newList[index].upper()
            self._letterCasePermuation(index + 1)
        else:
            self._letterCasePermuation(index + 1)

if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("po"))