class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        self.newList = list(S)
        self.mainList = list()
        self._letterCasePermuation(0)

    def _letterCasePermuation(self, index):

        if index == len(self.newList) - 1:
            import copy
            self.mainList.append(copy.deepcopy(self.newList))
            return

        for i in range(index, len(self.newList)):
            if self.newList[i].isalpha():
                self.newList[i] = self.newList[i].upper()
                self._letterCasePermuation(i)
                self.newList[i] = self.newList[i].lower()
                self._letterCasePermuation(i)

if __name__ == "__main__":
    s = Solution()
    s.letterCasePermutation("a1b2")