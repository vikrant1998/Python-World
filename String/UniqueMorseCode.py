class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        uniqueCode = set()
        for word in words:
            conversion = ''
            for letters in word:
                conversion += wordMap[ord(letters) % 97]
            uniqueCode.add(conversion)

        return len(uniqueCode)

if __name__ == "__main__":
    s = Solution()
    words = ["vtpke","vngc","vnqr","gbzx","qvdx"]
    print(s.uniqueMorseRepresentations(words))
