class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.hash = {}
        newHash = hash(longUrl)
        short = 'https://tinyurl.com/' + str(newHash)
        self.hash[short] = longUrl
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.hash[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
if __name__ == "__main__":
    c = Codec()
    res = c.encode('https://leetcode.com/problems/design-tinyurl')
    print(res)
    newres = c.decode(res)
    print(newres)
