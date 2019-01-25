class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        s = []
        res = [0 for i in range(len(T))]

        for i, element in enumerate(T):
            if len(s) == 0:
                s.append((element, i))
            else:
                newVal = element
                while len(s) > 0 and newVal > s[-1][0]:
                    popVal = s.pop()
                    res[popVal[1]] = i - popVal[1]
                s.append((element, i)) 

        return res

if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    s.dailyTemperatures(T)