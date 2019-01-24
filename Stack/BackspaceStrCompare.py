class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        from collections import deque
        s1 = deque()
        s2 = deque()

        for char in S:
            if char != '#':
                s1.append(char)
            else:
                if s1:
                    s1.pop()

        for char in T:
            if char != '#':
                s2.append(char)
            else:
                if s2:
                    s2.pop()

        str1 = ''.join(s1)
        str2 = ''.join(s2)

        if s1 == s2: return True
        return False

if __name__ == "__main__":
    S = "ab#c"; T = "ad#cc"
    s = Solution()
    print(s.backspaceCompare(S, T))