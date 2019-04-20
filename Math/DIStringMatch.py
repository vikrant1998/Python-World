class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        mi = 0
        ma = len(S)
        arr = [0 for i in range(ma + 1)]

        for i, s in enumerate(S):
            if s == 'I':
                arr[i] = mi
                mi += 1
            else:
                arr[i] = ma
                ma -= 1

        arr[len(S)] = ma
        return arr

if __name__ == "__main__":
    S = "DDI"
    s = Solution()
    print(s.diStringMatch(S))