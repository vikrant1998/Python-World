class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()

        AMap = dict()
        BMap = dict()
        dontIncl = set()

        for element in A:
            if element not in AMap: AMap[element] = 1
            else: AMap[element] += 1

        for key, value in AMap.items():
            if AMap[key] > 1:
                dontIncl.add(key)
                del AMap[key]

        for element in B:
            if element not in BMap: BMap[element] = 1
            else: BMap[element] += 1

        for key, value in BMap.items():
            if BMap[key] > 1:
                dontIncl.add(key)
                del BMap[key]

        finSet = set()
        for key, value in AMap.items():
            if key not in BMap.keys() and key not in dontIncl:
                finSet.add(key)

        for key, value in BMap.items():
            if key not in AMap.keys() and key not in dontIncl:
                finSet.add(key)

        return list(finSet)

if __name__ == "__main__":
    s = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"

    A = "apple apple"
    B = "banana"
    print(s.uncommonFromSentences(A, B))
