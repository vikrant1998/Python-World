class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        i = 0
        size = len(S)
        depth = 0
        res = 0

        while i < size:
            if S[i] == '(':
                depth += 1
            else:
                depth -= 1

            if i - 1 >= 0 and S[i] == ')' and S[i - 1] == '(':
                res += 2 ** depth

            i += 1

        return res

if __name__ == "__main__":
    S = "(()(()))"
    s = Solution()
    print(s.scoreOfParentheses(S))