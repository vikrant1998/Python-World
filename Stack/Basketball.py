class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        newList = []
        runSum = 0
        for pts in ops:
            if pts == 'C':
                runSum -= newList[-1]
                newList.pop()
            elif pts == 'D':
                runSum += newList[-1] * 2
                newList.append(newList[-1] * 2)
            elif pts == '+':
                runSum += newList[-1] + newList[-2]
                newList.append(newList[-1] + newList[-2])
            else:
                newList.append(int(pts))
                runSum += int(pts)

        return runSum

if __name__ == "__main__":
    s = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    print(s.calPoints(ops))
