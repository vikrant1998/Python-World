class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowelSet = set()
        vowelSet.add('a')
        vowelSet.add('e')
        vowelSet.add('i')
        vowelSet.add('o')
        vowelSet.add('u')
        inpList = S.split()
        for i, element in enumerate(inpList):
            if len(element) > 0:
                if element[0].lower() in vowelSet:
                    element += 'ma'
                else:
                    element = element[1:] + element[0] + 'ma'

                element += 'a' * (i + 1)
                inpList[i] = element

        outStr = ' '.join(inpList)
        return outStr

if __name__ == "__main__":
    S = "The quick brown fox jumped over the lazy dog"
    check = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    s = Solution()
    if s.toGoatLatin(S) == check:
        print('Yeet')