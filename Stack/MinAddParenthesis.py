class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        myStack = []
        count = 0

        for char in S:
            if char == '(':
                myStack.append(char)
            else:
                if len(myStack) > 0:
                    myStack.pop()
                elif len(myStack) == 0:
                    count += 1

        count += len(myStack)

        return count

if __name__ == "__main__":
    S = "()))(("
    s = Solution()
    print(s.minAddToMakeValid(S))