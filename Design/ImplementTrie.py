class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myTrie = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        level = self.myTrie

        for i, char in enumerate(word):
            if char not in level:
                if i == len(word) - 1:
                    level[char] = [dict(), True]
                else:
                    level[char] = [dict(), False]
            else:
                if i == len(word) - 1:
                    res = level[char]
                    level[char] = [res[0], True]

            level = level[char][0]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        level = self.myTrie

        for i, char in enumerate(word):
            if char in level:
                if char in level and i == len(word) - 1 and level[char][1] == True:
                    return True
                level = level[char][0]
            else:
                return False

        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        level = self.myTrie

        for i, char in enumerate(prefix):
            if char in level:
                level = level[char][0]
                if i == len(prefix) - 1:
                    return True
            else:
                return False

        return False

if __name__ == "__main__":
    t = Trie()
    t.insert('hello')
    t.insert('hell')
    t.insert('vikrant')

    print(t.search('hello'))
    print(t.startsWith('vik'))