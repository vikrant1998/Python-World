class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        countMap = dict()
        for element in cpdomains:
            count, domain = element.split()[0], element.split()[1]
            splitList = domain.split('.')
            subStr = ''
            for item in reversed(splitList):
                if subStr == '': subStr = item
                else: subStr = item + '.' + subStr

                if subStr not in countMap:
                    countMap[subStr] = int(count)
                else:
                    countMap[subStr] += int(count)

        finList = []
        for key, value in countMap.items():
            finList.append(str(value) + ' ' + key)

        return finList

if __name__ == "__main__":
    s = Solution()

    cpdomains = ["900 google.mail.com", \
    "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    print(s.subdomainVisits(cpdomains))
