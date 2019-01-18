class Solution(object):
    def rotatedDigits(self, N):
        counts = 0
        for num in range(1, N+1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number:
                continue
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts

if __name__ == "__main__":
    s = Solution()
    print(s.rotatedDigits(10))