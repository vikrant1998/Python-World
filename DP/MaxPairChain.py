class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x: x[1])
        end = float("-inf")
        res = len(pairs)
        
        for pair in pairs:
            if pair[0] > end:
                end = pair[1]
            else:
                res -= 1  
        return res

if __name__ == "__main__":
    s = Solution()
    pairs = [[1,2], [2,3], [3,4]]
    print(s.findLongestChain(pairs))